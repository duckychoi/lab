#!/usr/bin/env python3
"""
wiki-graph.py — LLM Wiki 3D 그래프 생성기
wiki/ 디렉토리의 마크다운 파일을 파싱해서
wiki/graph.json (Claude용) + wiki-graph.html (3D 시각화) 생성

실행: python3 scripts/wiki-graph.py
"""

import os
import re
import json

VAULT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WIKI_DIR   = os.path.join(VAULT_ROOT, "wiki")
OUT_JSON   = os.path.join(WIKI_DIR, "graph.json")
OUT_HTML   = os.path.join(VAULT_ROOT, "wiki-graph.html")

TYPE_COLORS = {
    "concept":   "#7c6af7",  # 보라
    "entity":    "#4fc3f7",  # 하늘
    "domain":    "#81c784",  # 초록
    "source":    "#ffb74d",  # 주황
    "overview":  "#ef5350",  # 빨강
    "index":     "#ffffff",  # 흰색
    "synthesis": "#f06292",  # 핑크
    "unknown":   "#666688",  # 회색
}

TYPE_LABELS = {
    "concept":   "개념",
    "entity":    "엔티티",
    "domain":    "도메인",
    "source":    "소스",
    "overview":  "개요",
    "index":     "인덱스",
    "synthesis": "분석",
    "unknown":   "기타",
}


def parse_frontmatter(text):
    """YAML frontmatter 파싱 (pyyaml 없이)"""
    meta = {}
    if not text.startswith("---"):
        return meta, text
    end = text.find("\n---", 3)
    if end == -1:
        return meta, text
    block = text[3:end].strip()
    for line in block.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip()
            v = v.strip()
            if v.startswith("[") and v.endswith("]"):
                v = [x.strip().strip('"\'') for x in v[1:-1].split(",") if x.strip()]
            meta[k] = v
    return meta, text[end + 4:]


def extract_wikilinks(text):
    """[[링크]] 또는 [[링크|별칭]] 패턴 추출"""
    raw = re.findall(r'\[\[([^\]|#]+?)(?:[|#][^\]]*?)?\]\]', text)
    links = []
    for r in raw:
        r = r.strip()
        if r and not r.endswith(".png") and not r.endswith(".jpg"):
            links.append(r)
    return links


def slug_from_path(path, wiki_dir):
    """wiki/ 기준 상대 경로를 slug로 변환"""
    rel = os.path.relpath(path, wiki_dir)
    return rel.replace("\\", "/").removesuffix(".md")


def resolve_link(link, all_slugs):
    """wikilink 텍스트를 slug로 해석 (파일명만 있는 경우도 처리)"""
    link = link.strip().replace("\\", "/")
    if link in all_slugs:
        return link
    # 파일명만 있을 경우 매칭
    link_name = link.split("/")[-1].lower()
    for slug in all_slugs:
        if slug.split("/")[-1].lower() == link_name:
            return slug
    return None


def scan_wiki(wiki_dir):
    nodes = {}
    raw_links = {}  # slug -> [raw wikilink strings]

    for root, _, files in os.walk(wiki_dir):
        for fname in files:
            if not fname.endswith(".md"):
                continue
            fpath = os.path.join(root, fname)
            slug  = slug_from_path(fpath, wiki_dir)
            text  = open(fpath, encoding="utf-8").read()
            meta, body = parse_frontmatter(text)

            ntype  = meta.get("type", "unknown")
            title  = meta.get("title", slug.split("/")[-1])
            tags   = meta.get("tags", [])
            if isinstance(tags, str):
                tags = [tags]
            sources = meta.get("sources", [])
            if isinstance(sources, str):
                sources = [sources]

            # 본문 첫 단락 추출 (툴팁용)
            lines = [l for l in body.strip().splitlines() if l.strip() and not l.startswith("#")]
            excerpt = lines[0][:120] if lines else ""

            nodes[slug] = {
                "id":      slug,
                "title":   title,
                "type":    ntype,
                "tags":    tags,
                "sources": sources,
                "excerpt": excerpt,
                "color":   TYPE_COLORS.get(ntype, TYPE_COLORS["unknown"]),
                "file":    f"wiki/{slug}.md",
            }
            raw_links[slug] = extract_wikilinks(text)

    # 링크 해석
    all_slugs = set(nodes.keys())
    links = []
    seen_edges = set()

    for src_slug, wlinks in raw_links.items():
        for wl in wlinks:
            tgt_slug = resolve_link(wl, all_slugs)
            if tgt_slug and tgt_slug != src_slug:
                edge = tuple(sorted([src_slug, tgt_slug]))
                if edge not in seen_edges:
                    seen_edges.add(edge)
                    links.append({"source": src_slug, "target": tgt_slug})

    # inbound link 수 계산 (노드 크기 결정)
    inbound = {s: 0 for s in nodes}
    for lnk in links:
        inbound[lnk["target"]] = inbound.get(lnk["target"], 0) + 1

    for slug in nodes:
        nodes[slug]["inbound"] = inbound.get(slug, 0)
        nodes[slug]["val"]     = max(1, inbound.get(slug, 0)) * 2 + 3

    return list(nodes.values()), links


def build_graph_json(nodes, links):
    return {
        "meta": {
            "generated": __import__("datetime").datetime.now().strftime("%Y-%m-%d %H:%M"),
            "node_count": len(nodes),
            "link_count": len(links),
            "type_legend": TYPE_LABELS,
            "color_legend": TYPE_COLORS,
        },
        "nodes": nodes,
        "links": links,
    }


def build_html(graph):
    data_js = json.dumps(graph, ensure_ascii=False, indent=2)

    type_legend_html = "".join(
        f'<span class="leg-item"><span class="leg-dot" style="background:{c}"></span>{TYPE_LABELS.get(t, t)}</span>'
        for t, c in TYPE_COLORS.items() if t != "unknown"
    )

    return f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>Wiki 3D Graph</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#0a0a12;color:#e0e0f0;font-family:'Segoe UI',system-ui,sans-serif;overflow:hidden}}
#graph-container{{width:100vw;height:100vh}}

#ui{{position:fixed;top:0;left:0;right:0;z-index:10;pointer-events:none}}
#header{{background:rgba(10,10,18,.85);backdrop-filter:blur(8px);border-bottom:1px solid #2e2e42;padding:.6rem 1.2rem;display:flex;align-items:center;gap:1rem;pointer-events:all}}
#header h1{{font-size:.9rem;font-weight:700;background:linear-gradient(135deg,#c4b5fd,#4fc3f7);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}}
.meta-pill{{font-size:.72rem;color:#8888aa;background:#1a1a24;border:1px solid #2e2e42;border-radius:10px;padding:.15rem .55rem}}
#legend{{display:flex;flex-wrap:wrap;gap:.4rem;margin-left:auto}}
.leg-item{{display:flex;align-items:center;gap:.3rem;font-size:.7rem;color:#8888aa}}
.leg-dot{{width:8px;height:8px;border-radius:50%;flex-shrink:0}}

#tooltip{{position:fixed;pointer-events:none;z-index:20;background:rgba(22,20,38,.95);border:1px solid #3a3560;border-radius:10px;padding:.8rem 1rem;max-width:260px;display:none}}
#tooltip .tt-type{{font-size:.68rem;font-weight:700;letter-spacing:.07em;text-transform:uppercase;margin-bottom:.3rem}}
#tooltip .tt-title{{font-size:.92rem;font-weight:700;margin-bottom:.4rem}}
#tooltip .tt-excerpt{{font-size:.78rem;color:#8888aa;line-height:1.5;margin-bottom:.4rem}}
#tooltip .tt-tags{{display:flex;flex-wrap:wrap;gap:.25rem}}
#tooltip .tt-tag{{font-size:.67rem;background:#1a1a2e;border:1px solid #2e2e42;border-radius:8px;padding:.1rem .35rem;color:#7c6af7}}
#tooltip .tt-links{{font-size:.72rem;color:#555577;margin-top:.3rem}}

#controls{{position:fixed;bottom:1.2rem;right:1.2rem;z-index:10;display:flex;flex-direction:column;gap:.5rem;align-items:flex-end}}
.ctrl-btn{{background:rgba(22,20,38,.9);border:1px solid #2e2e42;color:#8888aa;font-size:.75rem;padding:.4rem .8rem;border-radius:8px;cursor:pointer;transition:all .15s}}
.ctrl-btn:hover{{background:#1a1a3a;color:#e0e0f0;border-color:#7c6af7}}
.ctrl-btn.active{{background:#2a1a4a;color:#c4b5fd;border-color:#7c6af7}}

#search{{position:fixed;top:3.2rem;left:1rem;z-index:10;display:flex;gap:.4rem}}
#search input{{background:rgba(22,20,38,.9);border:1px solid #2e2e42;color:#e0e0f0;font-size:.8rem;padding:.4rem .7rem;border-radius:8px;width:200px;outline:none}}
#search input:focus{{border-color:#7c6af7}}
#search input::placeholder{{color:#555577}}

#info-panel{{position:fixed;left:1rem;bottom:1.2rem;z-index:10;background:rgba(10,10,18,.85);border:1px solid #2e2e42;border-radius:10px;padding:.6rem .9rem;font-size:.72rem;color:#555577;line-height:1.8}}
#info-panel .hi{{color:#8888aa}}
</style>
</head>
<body>

<div id="ui">
  <div id="header">
    <h1>Wiki 3D Graph</h1>
    <span class="meta-pill" id="meta-nodes">N nodes</span>
    <span class="meta-pill" id="meta-links">N links</span>
    <span class="meta-pill" id="meta-gen">-</span>
    <div id="legend">{type_legend_html}</div>
  </div>
</div>

<div id="search">
  <input type="text" id="search-input" placeholder="노드 검색..." oninput="onSearch(this.value)">
</div>

<div id="tooltip">
  <div class="tt-type" id="tt-type"></div>
  <div class="tt-title" id="tt-title"></div>
  <div class="tt-excerpt" id="tt-excerpt"></div>
  <div class="tt-tags" id="tt-tags"></div>
  <div class="tt-links" id="tt-links"></div>
</div>

<div id="graph-container"></div>

<div id="controls">
  <button class="ctrl-btn" onclick="resetCamera()">카메라 리셋</button>
  <button class="ctrl-btn" id="btn-labels" onclick="toggleLabels()">라벨 토글</button>
  <button class="ctrl-btn" id="btn-float" onclick="toggleFloat()">Float 토글</button>
</div>

<div id="info-panel">
  <span class="hi">드래그</span> 회전 &nbsp;
  <span class="hi">스크롤</span> 줌 &nbsp;
  <span class="hi">우클릭</span> 이동 &nbsp;
  <span class="hi">호버</span> 상세
</div>

<script src="https://unpkg.com/3d-force-graph@1.73.2/dist/3d-force-graph.min.js"></script>
<script>
const GRAPH_DATA = {data_js};

const typeColors = GRAPH_DATA.meta.color_legend;
const typeLabels = GRAPH_DATA.meta.type_legend;

// meta 표시
document.getElementById('meta-nodes').textContent = GRAPH_DATA.meta.node_count + ' nodes';
document.getElementById('meta-links').textContent = GRAPH_DATA.meta.link_count + ' links';
document.getElementById('meta-gen').textContent   = GRAPH_DATA.meta.generated;

// 노드 ID → 객체 맵
const nodeMap = {{}};
GRAPH_DATA.nodes.forEach(n => nodeMap[n.id] = n);

let showLabels = true;
let floatMode  = false;
let highlighted = null;

const Graph = ForceGraph3D()(document.getElementById('graph-container'))
  .backgroundColor('#0a0a12')
  .graphData(GRAPH_DATA)
  .nodeLabel(n => '')   // 커스텀 툴팁 사용
  .nodeColor(n => {{
    if (highlighted) {{
      if (n.id === highlighted) return n.color;
      const connected = GRAPH_DATA.links.some(
        l => (l.source.id||l.source) === highlighted && (l.target.id||l.target) === n.id ||
             (l.target.id||l.target) === highlighted && (l.source.id||l.source) === n.id
      );
      return connected ? n.color : '#1a1a24';
    }}
    return n.color;
  }})
  .nodeVal(n => n.val || 4)
  .nodeOpacity(0.9)
  .nodeResolution(10)
  .linkColor(() => '#2e2e42')
  .linkWidth(0.8)
  .linkOpacity(0.5)
  .linkDirectionalParticles(n => 1)
  .linkDirectionalParticleWidth(1.2)
  .linkDirectionalParticleColor(() => '#7c6af7')
  .linkDirectionalParticleSpeed(0.004)
  .onNodeHover(node => {{
    document.getElementById('graph-container').style.cursor = node ? 'pointer' : 'default';
    if (node) showTooltip(node);
    else hideTooltip();
    highlighted = node ? node.id : null;
    Graph.nodeColor(Graph.nodeColor()); // 리렌더
  }})
  .onNodeClick(node => {{
    // 카메라 포커스
    const dist = 80;
    const distRatio = 1 + dist / Math.hypot(node.x, node.y, node.z);
    Graph.cameraPosition(
      {{ x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }},
      node,
      1200
    );
  }});

// 라벨 (Three.js SpriteText)
// 라벨은 별도 주입 없이 CSS2D로 처리
if (typeof SpriteText !== 'undefined') {{
  Graph.nodeThreeObject(n => {{
    if (!showLabels) return null;
    const sprite = new SpriteText(n.title || n.id.split('/').pop());
    sprite.color = n.color;
    sprite.textHeight = 3;
    return sprite;
  }});
}}

// 툴팁
function showTooltip(node) {{
  const tt = document.getElementById('tooltip');
  document.getElementById('tt-type').textContent = typeLabels[node.type] || node.type;
  document.getElementById('tt-type').style.color  = node.color;
  document.getElementById('tt-title').textContent  = node.title || node.id;
  document.getElementById('tt-excerpt').textContent = node.excerpt || '';

  const tagsEl = document.getElementById('tt-tags');
  tagsEl.innerHTML = (node.tags||[]).map(t => `<span class="tt-tag">#${{t}}</span>`).join('');

  const linksEl = document.getElementById('tt-links');
  const linkCount = GRAPH_DATA.links.filter(
    l => (l.source.id||l.source) === node.id || (l.target.id||l.target) === node.id
  ).length;
  linksEl.textContent = `연결 ${{linkCount}}개 · 인바운드 ${{node.inbound||0}}개`;

  tt.style.display = 'block';
}}

document.addEventListener('mousemove', e => {{
  const tt = document.getElementById('tooltip');
  if (tt.style.display === 'block') {{
    tt.style.left = (e.clientX + 16) + 'px';
    tt.style.top  = (e.clientY - 10) + 'px';
    // 화면 밖 넘침 방지
    const rect = tt.getBoundingClientRect();
    if (rect.right > window.innerWidth - 10)
      tt.style.left = (e.clientX - rect.width - 16) + 'px';
    if (rect.bottom > window.innerHeight - 10)
      tt.style.top  = (e.clientY - rect.height + 10) + 'px';
  }}
}});

function hideTooltip() {{
  document.getElementById('tooltip').style.display = 'none';
}}

// 검색
function onSearch(query) {{
  if (!query.trim()) {{
    Graph.nodeColor(n => n.color);
    return;
  }}
  const q = query.toLowerCase();
  Graph.nodeColor(n => {{
    const match = (n.title||'').toLowerCase().includes(q) ||
                  (n.id||'').toLowerCase().includes(q) ||
                  (n.tags||[]).some(t => t.toLowerCase().includes(q));
    return match ? '#ffffff' : '#1a1a2a';
  }});
}}

// 카메라 리셋
function resetCamera() {{
  Graph.cameraPosition({{ x: 0, y: 0, z: 300 }}, {{ x: 0, y: 0, z: 0 }}, 1000);
}}

// 라벨 토글 (기본 라벨 없음 — SpriteText 없을 때 대비)
function toggleLabels() {{
  showLabels = !showLabels;
  document.getElementById('btn-labels').classList.toggle('active', showLabels);
}}

// Float 모드 토글
function toggleFloat() {{
  floatMode = !floatMode;
  document.getElementById('btn-float').classList.toggle('active', floatMode);
  if (floatMode) {{
    Graph.d3Force('charge').strength(-120);
    Graph.d3Force('link').distance(60);
  }} else {{
    Graph.d3Force('charge').strength(-80);
    Graph.d3Force('link').distance(40);
  }}
  Graph.d3ReheatSimulation();
}}

// 초기 카메라
Graph.cameraPosition({{ z: 280 }});
</script>
</body>
</html>
"""


def main():
    print(f"[wiki-graph] wiki/ 스캔 중: {WIKI_DIR}")
    nodes, links = scan_wiki(WIKI_DIR)
    print(f"[wiki-graph] 노드 {len(nodes)}개, 링크 {len(links)}개 발견")

    graph = build_graph_json(nodes, links)

    # graph.json 저장 (Claude가 topology 파악용)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(graph, f, ensure_ascii=False, indent=2)
    print(f"[wiki-graph] 저장: {OUT_JSON}")

    # HTML 저장
    html = build_html(graph)
    with open(OUT_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"[wiki-graph] 저장: {OUT_HTML}")
    print(f"[wiki-graph] 완료! 브라우저에서 wiki-graph.html 열기")


if __name__ == "__main__":
    main()
