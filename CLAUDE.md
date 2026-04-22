# LLM Wiki Schema — Obsidian WS

이 파일은 Claude가 이 vault를 **LLM wiki**로 관리할 때 따르는 스키마다.
Andrej Karpathy의 [LLM Wiki 패턴](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)을 기반으로 한다.

> **핵심 원칙**: Claude가 wiki를 쓰고 유지한다. 사용자는 소스를 큐레이션하고, 방향을 잡고, 좋은 질문을 한다.

---

## 디렉토리 구조

```
Obsidian_WS/              ← vault root
├── CLAUDE.md             ← 이 파일: wiki 스키마 + 워크플로우
├── wiki/                 ← Claude가 소유하는 wiki 레이어
│   ├── index.md          ← 모든 wiki 페이지의 카탈로그 (항상 최신 유지)
│   ├── log.md            ← append-only 활동 로그
│   ├── overview.md       ← 전체 지식 베이스 big-picture 요약
│   ├── concepts/         ← 개념 설명 페이지
│   ├── entities/         ← 인물, 도구, 모델, 회사 페이지
│   ├── domains/          ← 도메인별 종합 요약
│   └── sources/          ← 소스별 요약 페이지
├── raw/                  ← 원본 소스 레이어 (불변 — Claude는 읽기만)
│   └── assets/           ← 다운로드된 이미지
├── AI News/              ← AI 뉴스 클리핑 (raw sources)
├── Cinema Studio/        ← 시네마 스튜디오 관련 (raw sources)
└── Vibe Coding/          ← 바이브 코딩 관련 (raw sources)
```

---

## Wiki 페이지 형식

### 필수 frontmatter

```yaml
---
title: 페이지 제목
type: concept | entity | domain | source | synthesis
tags: [태그1, 태그2]
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: [소스1, 소스2]  # 이 페이지가 참조하는 소스 목록
---
```

### 파일 명명 규칙
- 소문자 kebab-case: `novel-view-synthesis.md`
- 한국어 주제는 영문 slug로: `qwen-image-edit.md`
- 날짜 prefix 불필요 (log.md에서 추적)

### 크로스 레퍼런스
- Obsidian wikilink 사용: `[[개념명]]`, `[[entities/qwen]]`
- 외부 링크는 인라인: `[텍스트](URL)`
- 소스 인용: `(출처: [[sources/qwen-image-edit-blog]])`

---

## 그래프 / 시각화

**Obsidian 내장 Graph View** — 기본 시각화. 우리 wikilinks 구조와 즉시 호환.  
**Juggl 플러그인** — 노드 타입별 CSS 스타일링 지원. `.obsidian/juggl.css` 설정으로 type별 색상 적용.  
**Graph Analysis 플러그인** — co-citation, 링크 예측으로 lint 보강.

`wiki/graph.json` — Claude가 topology 파악용으로 읽는 구조화된 요약.  
갱신 필요 시: `python3 scripts/wiki-graph.py` (ingest 후 수동 실행, 또는 요청 시)

---

## 세 가지 핵심 Operations

### 1. Ingest (소스 추가)

**최소 3개 파일 (항상):** sources/[slug].md 생성 + index.md 1줄 추가 + log.md 1항목 추가  
**조건부:** concept/entity 페이지는 두 번째 소스에서도 등장할 때만 생성. domain 업데이트는 실질적 변화가 있을 때만.

`/ingest` 스킬 참조. 상세 흐름과 기준은 스킬 파일에 있음.

### 2. Query (질문)

wiki에 질문할 때:

```
1. wiki/index.md 읽어서 관련 페이지 파악
2. 관련 페이지들 읽기
3. 답변 합성 + 인용 포함
4. 가치 있는 답변은 wiki 페이지로 저장 제안
5. wiki/log.md에 query 항목 추가 (선택)
```

`/query` 스킬로 실행.

### 3. Lint (상태 점검)

wiki 건강 상태 점검:

```
점검 항목:
- 페이지 간 모순 / 구 정보
- 인바운드 링크 없는 orphan 페이지
- cross-reference 누락
- 독립 페이지가 필요한 개념 (현재 언급만 됨)
- 데이터 갭 (web search로 채울 수 있는 것)
```

`/lint` 스킬로 실행.

---

## index.md 형식

```markdown
# Wiki Index

> 마지막 업데이트: YYYY-MM-DD | 총 N개 페이지

## Concepts (개념)
- [[concepts/llm-wiki]] — LLM으로 유지하는 개인 지식 베이스 패턴
- [[concepts/novel-view-synthesis]] — 단일 이미지에서 새로운 시점 생성

## Entities (도구 / 모델 / 인물)
- [[entities/qwen-image]] — Alibaba의 멀티모달 이미지 편집 모델

## Domains (도메인)
- [[domains/ai-ml]] — AI/ML 전반 종합
- [[domains/cinema-studio]] — 시네마 스튜디오 지식 베이스
- [[domains/vibe-coding]] — Vibe coding / AI 코딩 지식 베이스

## Sources (소스 요약)
- [[sources/qwen-image-edit-blog]] — Qwen-Image-Edit 공식 블로그 요약
```

---

## log.md 형식

각 항목 prefix: `## [YYYY-MM-DD] operation | title`

```markdown
## [2026-04-10] setup | LLM Wiki 초기 세팅
초기 wiki 구조 생성. CLAUDE.md, index.md, log.md, overview.md 작성.
관련 파일: wiki/ 전체, CLAUDE.md

## [2026-04-10] ingest | Qwen Novel View Synthesis Research
Research.md의 Qwen 관련 내용을 wiki로 정리.
생성: sources/qwen-research.md, entities/qwen-image.md, concepts/novel-view-synthesis.md
```

grep 가능하도록 prefix를 일관되게 유지: `grep "^## \[" wiki/log.md`

---

## 도메인별 컨텍스트

### AI News
AI 뉴스 클리핑 영역. 인제스트 후 `wiki/domains/ai-ml.md`와 관련 entity 페이지 업데이트.

### Cinema Studio
시네마 스튜디오 관련 지식. `wiki/domains/cinema-studio.md` 중심으로 관리.

### Vibe Coding
AI 보조 코딩, 프롬프트 엔지니어링, 에이전트 워크플로우 관련.
`wiki/domains/vibe-coding.md` 중심으로 관리.

---

## Claude의 책임

- wiki 레이어의 모든 파일 생성/수정/유지
- 크로스 레퍼런스 항상 최신 상태 유지
- ingest할 때마다 index.md와 log.md 반드시 업데이트
- 사용자에게 "이 발견을 wiki 페이지로 저장할까요?" 주기적으로 제안
- raw 소스는 절대 수정하지 않음

## 사용자의 책임

- 소스 큐레이션 (어떤 자료를 추가할지 결정)
- 분석 방향 지정
- 좋은 질문 던지기
- wiki의 의미와 방향에 대해 생각하기
