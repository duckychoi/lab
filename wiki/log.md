---
title: Wiki Activity Log
type: log
updated: 2026-04-18
cssclasses:
  - wide-page
---

# Wiki Activity Log

> [!log] Append-Only Record
> 모든 wiki 활동의 시간순 기록. 각 항목은 `## [YYYY-MM-DD] operation | title` 형식.

```bash
grep "^## \[" wiki/log.md | tail -10   # 최근 10개 항목
grep "ingest" wiki/log.md              # ingest 항목만
```

---

## [2026-04-18] ingest | Pretext — Text Measurement & Layout Library

소스: `/home/ducky/Useful_tools/pretext/` (로컬 클론)

> [!abstract] Key Takeaways
> - 순수 JS/TS 멀티라인 텍스트 측정/레이아웃 라이브러리
> - DOM reflow 없이 텍스트 높이 예측 (Canvas `measureText` 기반)
> - CJK, 아랍어, 동남아시아어, 이모지 등 모든 언어 지원
> - 두 가지 사용 케이스: 높이 예측 + 수동 라인 레이아웃 (Canvas/SVG/WebGL)
> - `@chenglou/pretext` v0.0.5, MIT 라이선스, chenglou 제작

| Action | Files |
|---|---|
| Created | `raw/pretext-analysis.md`, `wiki/sources/pretext-analysis.md`, `wiki/entities/pretext.md` |
| Updated | `wiki/index.md`, `wiki/log.md`, `wiki/domains/vibe-coding.md` |

---

## [2026-04-17] enhancement | Wiki Visual Redesign

wiki 전체 페이지의 시각적 품질 개선.

**변경 내용:**
- CSS 스니펫 추가 (`.obsidian/snippets/wiki-styles.css`)
  - 커스텀 callout 타입: `definition`, `insight`, `model`, `architecture`, `limitation`, `open-question`, `log`
  - 태그 pill 스타일, 코드블록 둥근 테두리, HR 그라데이션
- `wiki/index.md` — Mermaid 지식 맵, 테이블 기반 카탈로그로 재설계
- `wiki/overview.md` — At a Glance 섹션, Mermaid 토폴로지, callout 활용
- `wiki/log.md` — callout + 코드 블록으로 재구조화
- 모든 wiki 페이지 — callout, 시각적 계층강화, frontmatter `cssclasses` 추가

**업데이트:** wiki 전체 파일

---

## [2026-04-10] ingest | Qwen Novel View Synthesis Research Notes

소스: `Research.md` (기존 vault 파일 — Claude Code 대화에서 생성된 연구 노트)

> [!abstract] Key Takeaways
> - Qwen-Image-Edit: MMDiT 기반 20B 파라미터 이미지 생성/편집 모델
> - 실제 3D mesh 없이 diffusion prior로 novel view synthesis 수행
> - 시점 변화는 텍스트 프롬프트(토큰)로 조건 부여
> - Qwen2.5-VL(semantic) + VAE Encoder(visual appearance) 이중 인코딩
> - 한계: strict 3D consistency 보장 안 됨

| Action | Files |
|---|---|
| Created | `concepts/novel-view-synthesis.md`, `entities/qwen-image.md`, `sources/qwen-research-notes.md` |
| Updated | `wiki/index.md`, `wiki/domains/ai-ml.md` |

---

## [2026-04-10] ingest | Karpathy LLM Wiki Pattern

소스: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

> [!abstract] Key Takeaways
> - RAG와 달리 LLM이 wiki를 점진적으로 빌드하고 유지함
> - 세 레이어: raw sources → wiki → schema (CLAUDE.md)
> - 핵심 operations: ingest, query, lint
> - index.md(내용 카탈로그) + log.md(시간순 기록) 두 가지 특수 파일

| Action | Files |
|---|---|
| Created | `concepts/llm-wiki.md`, `sources/karpathy-llm-wiki.md` |
| Updated | `wiki/index.md`, `wiki/overview.md` |

---

## [2026-04-10] setup | LLM Wiki 초기 세팅

Andrej Karpathy의 LLM wiki 패턴을 이 Obsidian vault에 적용.

| Action | Files |
|---|---|
| Created | `CLAUDE.md`, `wiki/index.md`, `wiki/log.md`, `wiki/overview.md`, `wiki/concepts/llm-wiki.md`, `wiki/concepts/novel-view-synthesis.md`, `wiki/entities/qwen-image.md`, `wiki/domains/ai-ml.md`, `wiki/domains/cinema-studio.md`, `wiki/domains/vibe-coding.md`, `wiki/sources/karpathy-llm-wiki.md`, `wiki/sources/qwen-research-notes.md`, `.claude/skills/ingest/SKILL.md`, `.claude/skills/query/SKILL.md`, `.claude/skills/lint/SKILL.md` |

**적용 기반 소스:**
- https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- 기존 `Research.md` (Qwen Novel View Synthesis 연구 노트)
