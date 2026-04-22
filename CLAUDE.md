# LLM Wiki Schema

이 파일은 너(LLM)가 이 위키의 구조, 컨벤션, 워크플로우를 이해하게 해주는 설정 파일이다.
너는 이 위키의 **유일한 작성자이자 관리자**다. 사람은 소스 제공과 질문을 담당하고, 너는 나머지 전부를 담당한다.

---

## 디렉터리 구조

```
vault/
├── CLAUDE.md              ← 지금 이 파일 (위키 스키마)
├── index.md               ← 모든 위키 페이지 목록 및 한 줄 요약
├── log.md                 ← ingest/query/lint/graph 시간순 기록
├── raw.md                 ← 인제스트 대기 소스 목록 (처리 후 항목 삭제)
├── actionable.md          ← 당장 써먹을 수 있는 것들 (전 도메인 통합)
├── wiki/
│   ├── entities/          ← 인물, 기업, 제품, 프로젝트
│   ├── concepts/          ← 아이디어, 이론, 프레임워크, 용어
│   ├── sources/           ← 소스별 요약 페이지
│   ├── synthesis/         ← 교차 도메인 통찰, 비교, 패턴
│   ├── domains/           ← 도메인별 누적 인사이트
│   │   ├── video-saas.md
│   │   ├── local-llm.md
│   │   ├── slam-3dgs.md
│   │   └── ai-news.md
│   └── queries/           ← 보존된 질문과 답변
├── canvas/                ← 도메인별 지식 그래프 Canvas 파일
│   ├── video-saas.canvas
│   ├── local-llm.canvas
│   ├── slam-3dgs.canvas
│   ├── ai-news.canvas
│   └── overview.canvas    ← 전체 도메인 연결 지도
└── bases/                 ← 도메인별 Bases 데이터베이스 뷰
    ├── sources.base       ← 전체 소스 목록 (도메인/날짜/신뢰도 필터)
    └── actionables.base   ← actionable 항목 관리 (우선순위/상태 필터)
```

---

## 핵심 원칙

1. **raw.md 는 인제스트 대기열** — ingest 완료 후 해당 항목 즉시 삭제
2. **wiki/ 는 LLM 소유** — LLM이 생성·수정·유지, 사람은 읽기만
3. **옵시디언 풀 포맷 필수** — 모든 페이지는 아래 문서 표준을 준수
4. **wikilink 밀도 높게** — 연결이 많을수록 그래프가 풍부해짐. 관련 페이지는 반드시 `[[링크]]`
5. **canvas 항상 최신** — ingest마다 해당 도메인 canvas 업데이트
6. **요약이 아닌 인사이트** — "이것이 존재한다"가 아닌 "왜 중요하고 어떻게 쓸 수 있는가"
7. **actionable.md 항상 갱신** — 실행 가능한 항목 발견 시 즉시 추가

---

## 옵시디언 문서 표준 (모든 wiki 페이지 적용)

### 프론트매터 (필수)
```yaml
---
title: 페이지 제목
type: entity | concept | source | synthesis | query | domain
domain: video-saas | local-llm | slam-3dgs | ai-news | general
tags: [태그1, 태그2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [소스파일명.md, ...]
reliability: high | medium | low   ← GitHub 스타/HF 다운로드 기반
---
```

### Callout 사용 규칙
```markdown
> [!insight] 핵심 인사이트
> 이 소스에서 가장 중요한 한 가지

> [!action] 당장 할 것
> 구체적인 실행 항목

> [!warning] 주의 / 신뢰도 낮음
> 검증 필요하거나 과장된 클레임

> [!note] 배경 정보
> 맥락 이해를 위한 보조 정보

> [!question] 미해결 질문
> 더 조사가 필요한 것
```

### 섹션 구조 (source 타입 기준)
```markdown
## 핵심 인사이트
> [!insight] ...

## 도메인별 추출
(해당 도메인 템플릿 질문에 대한 답)

## 시각 분석 결과  ← 영상/이미지 소스인 경우
(장면별 설명, UI 패턴, 프롬프트↔결과)

## 관련 페이지
- [[연관 엔티티]]
- [[연관 개념]]
- [[유사 소스]]

## 원본
- 출처: URL 또는 파일
- 신뢰도: ⭐⭐⭐ (GitHub 스타 수 / HF 다운로드 기반)
```

### wikilink 작성 원칙
- 인물/기업/제품은 항상 `[[이름]]` — entities/ 페이지 자동 연결
- 개념/기술은 항상 `[[개념명]]` — concepts/ 페이지 자동 연결
- 같은 도메인 소스끼리 `[[소스제목]]` 으로 상호 참조
- 3개 이상 소스에서 등장한 개념은 반드시 concepts/ 독립 페이지 생성

---

## 4대 도메인 & 인사이트 추출 템플릿

### 도메인 1: 영상 AI SaaS (video-saas)
태그: `video-saas`, `higgsfield`, `runway`, `kling`, `영상자동화`

**영상 URL 인제스트 시 필수 선행:**
```
1. /down-video [URL]         → ~/down-video/ 에 저장
2. /down-analysis [파일]     → 트랜스크립트 + 장면별 시각 분석
3. 시각 분석 결과를 인사이트 추출 주요 입력으로 사용
```

시각 정보 추출 항목:
- UI/UX 패턴: 화면 레이아웃, 색상 팔레트, 타이포그래피, 전환 효과
- 워크플로우 시퀀스: 단계별 화면 변화, 버튼 흐름, UX 결정
- 프롬프트↔결과 쌍: 입력 텍스트 → 출력 영상 품질 매핑
- 디자인 수치: 추정 폰트 크기, 여백, 색상코드

인제스트 추출 템플릿:
- **기능 벤치마킹**: 내 SaaS에 구현하려면? 난이도/필요 스택?
- **크리에이터 인사이트**: 사용자가 원하는 것 vs 툴이 주는 것의 갭
- **프롬프트 패턴**: 좋은 결과를 만드는 구체적 프롬프트/파라미터
- **워크플로우**: 실제 end-to-end 제작 흐름 (화면 기록 기반)
- **디자인 레퍼런스**: 참고할 UI 패턴, 전환 효과, 레이아웃
- **경쟁 우위 빈틈**: 기존 툴 대비 차별화 포인트

Canvas 파일: `canvas/video-saas.canvas`

---

### 도메인 2: Local/Edge/Small LLM + 에이전트 메모리 (local-llm)
태그: `local-llm`, `edge-ai`, `slm`, `agent-memory`, `on-device`

인제스트 추출 템플릿:
- **실용성 판단**: 실배포 가능? 어떤 하드웨어? 지연시간 수치?
- **메모리 아키텍처**: RAG/KV/압축/외부DB 중 어떤 방식?
- **Hermes 적용**: 지금 당장 ChinameBot에 적용 가능? 방법?
- **트레이드오프**: 성능 vs 속도 vs 비용 구체적 수치
- **오픈소스 구현체**: 당장 쓸 수 있는 repo?

Canvas 파일: `canvas/local-llm.canvas`

---

### 도메인 3: 로봇 SLAM / 3DGS / 카메라 (slam-3dgs)
태그: `slam`, `3dgs`, `gaussian-splatting`, `camera`, `robotics`

인제스트 추출 템플릿:
- **현재 SOTA**: 최고 오픈소스 구현체? 벤치마크 수치?
- **실시간 가능성**: 30fps+ 가능? 어떤 조건?
- **카메라 파이프라인**: 입력 형식, 처리 방식
- **응용 가능성**: 내가 만들 수 있는 것과 연결점
- **필수 레퍼런스**: 반드시 읽어야 할 논문/repo

Canvas 파일: `canvas/slam-3dgs.canvas`

---

### 도메인 4: AI 뉴스 / GitHub 트렌딩 (ai-news)
태그: `ai-news`, `github-trending`, `workflow`, `tool`

**신뢰 소스 기준:**
- GitHub: 스타 1000+ 또는 당일 급상승만
- AI 모델: HuggingFace 1순위 (다운로드 수 + 벤치마크 + 논문)
- 신뢰도 낮은 클레임은 `> [!warning]` 표시

인제스트 추출 템플릿:
- **신뢰도**: 스타 수 / HF 다운로드 / 논문 유무 명시
- **즉시 활용**: 지금 내 워크플로우에 쓸 수 있나? YES/NO + 이유
- **6개월 영향력**: 내 작업 방식을 어떻게 바꿀 수 있나?
- **대체 관계**: 지금 쓰는 어떤 도구를 대체/강화하나?
- **허와 실**: 마케팅 걷어내면 실제 능력은?
- **액션**: star/fork/설치/실험 중 지금 할 것?

Canvas 파일: `canvas/ai-news.canvas`

---

## 작업(Operations)

### Ingest (새 소스 추가)

1. 소스 읽기 + 도메인 분류
2. **영상 URL이면 down-video → down-analysis 선행**
3. 도메인 인사이트 템플릿 질문에 답하며 내용 파악
4. `wiki/sources/` 에 **옵시디언 풀 포맷** 페이지 생성
5. 관련 entity/concept 페이지 업데이트 (wikilink 연결)
6. `wiki/domains/{도메인}.md` 누적 인사이트 갱신
7. **`canvas/{도메인}.canvas` 업데이트** — 새 노드 추가, 연결선 갱신
8. 기존 주장과 모순 시 `> [!warning]` 명시
9. `actionable.md` 갱신 (실행 가능 항목 추가)
10. `index.md` 업데이트
11. `raw.md` 에서 해당 항목 삭제
12. `log.md` 기록:
    ```
    ## [YYYY-MM-DD] ingest | 소스 제목
    - 도메인: video-saas | local-llm | slam-3dgs | ai-news
    - 추가 페이지: X개 | 업데이트 페이지: Y개
    - 핵심 인사이트: (요약 말고 배운 것 한 줄)
    - canvas 업데이트: YES/NO
    - actionable 추가: YES/NO
    ```

### Query (질문)
1. `index.md` 읽기
2. `wiki/domains/` 관련 도메인 페이지 우선 참조
3. 관련 wiki 페이지 읽어 답변 합성 + wikilink 인용
4. 좋은 답변은 `queries/` 에 옵시디언 포맷으로 저장
5. `log.md` 기록

### Graph (지식 그래프 분석 + 시각화)
소스 5개 이상 쌓이거나 사용자 요청 시:

```bash
VAULT="/home/monday/vault"

# 1. 전체 wikilink 맵 추출
grep -roh '\[\[[^\]]*\]\]' "$VAULT/wiki" | sort | uniq -c | sort -rn

# 2. 고아 노드 탐지 (연결 없는 페이지)
find "$VAULT/wiki" -name "*.md" | while read f; do
  page=$(basename "$f" .md)
  count=$(grep -rl "\[\[$page\]\]" "$VAULT/wiki" 2>/dev/null | wc -l)
  [ "$count" -eq 0 ] && echo "고아: $page"
done

# 3. 허브 노드 탐지 (많이 연결된 핵심 개념)
grep -roh '\[\[[^\]]*\]\]' "$VAULT/wiki" | sed 's/\[\[//;s/\]\]//' | sort | uniq -c | sort -rn | head -20
```

분석 후:
- **`canvas/overview.canvas` 업데이트** — 전체 지식 그래프, 도메인 간 연결선
- **HTML 그래프 생성** → `/tmp/wiki-graph.html` 으로 저장 후 사용자에게 sendfile
  - D3.js force-directed graph
  - 노드: 각 wiki 페이지 (도메인별 색상)
  - 엣지: wikilink 연결
  - 클릭 시 페이지 설명 팝업
- 연결이 없는 개념들 사이에 새 연결 제안
- synthesis/ 에 새 교차 인사이트 페이지 생성 기회 탐지
- `log.md` 기록

### Synthesis (교차 분석)
도메인 내 소스 5개+ 또는 사용자 요청 시:
- 도메인 내 패턴 추출
- 도메인 간 연결 발견 (예: 3DGS + 영상자동화 교차점)
- `wiki/synthesis/` 에 저장
- canvas/overview.canvas 에 synthesis 노드 추가

### Lint (위키 건강 점검)
- 페이지 간 모순 탐지 → `> [!warning]` 표시
- 고아 페이지 탐지 → canvas에서 연결선 없는 노드
- 인사이트 템플릿 미답변 항목 탐지
- `actionable.md` 30일+ 대기 항목 재검토 플래그
- 낡은 주장 표시

---

## Canvas 파일 형식 (도메인별)

각 domain canvas는 다음 구조로 유지:
```
[도메인 허브 노드] ← 중앙 큰 노드
    ├── [소스 클러스터] ← 소스별 노드
    ├── [엔티티 클러스터] ← 관련 인물/기업
    ├── [개념 클러스터] ← 핵심 개념들
    └── [actionable 클러스터] ← 실행 항목들
```
- ingest마다 새 노드 추가, 관련 노드 간 엣지 연결
- 노드 색상: sources=파란, entities=초록, concepts=보라, actionables=주황

---

## Bases 파일 형식

### sources.base
- 컬럼: 제목, 도메인, 날짜, 신뢰도(⭐), 핵심인사이트, actionable여부
- 필터: 도메인별, 날짜별, 신뢰도별

### actionables.base
- 컬럼: 항목, 도메인, 출처, 우선순위, 상태, 추가일
- 필터: 상태(대기/진행/완료), 우선순위별

---

## actionable.md 형식

```markdown
## [YYYY-MM-DD] 항목 제목
- **도메인**: video-saas | local-llm | slam-3dgs | ai-news
- **출처**: [[소스페이지]]
- **할 것**: 구체적 행동 (설치, 실험, 구현, 읽기 등)
- **우선순위**: 높음 | 중간 | 낮음
- **상태**: 대기 | 진행중 | 완료 | 보류
```

---

## 언어 정책

- 위키 페이지: **한국어** (소스가 영어여도 한국어로 작성)
- 프론트매터: 영어 허용
- 기술 용어: 원어 병기 (예: `가우시안 스플래팅 (Gaussian Splatting)`)

---

## 현재 도메인 (2026-04-09)
video-saas | local-llm | slam-3dgs | ai-news
