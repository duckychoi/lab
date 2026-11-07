---
title: "NVIDIA auto-ontology — NL→SQL 답에 근거·계보를 붙이는 온톨로지 계층. 정확도 개선은 아직 숫자로 없다"
type: source
domain: ai-news
tags: [ai-news, github-trending, nvidia, ontology, knowledge-graph, text-to-sql, mcp, agent-grounding, nim]
created: 2026-11-07
updated: 2026-11-07
sources: [https://github.com/NVIDIA/auto-ontology]
reliability: medium
---

**GitHub**: [NVIDIA/auto-ontology](https://github.com/NVIDIA/auto-ontology) **★9,479 · 포크 753 · 오픈이슈 75**(api.github.com 2026-11-07 볼트 실측 · 수집기 11-06 관측 ★8,049 → **+1,430/1일**) · Apache-2.0 · Python · created 2026-04-27 · pushed 2026-11-06T23:03Z · 릴리스 0건 · daily 트렌딩 **1위**(11-06, 당일 +2,679)

## 핵심 인사이트
> [!insight] "답"이 아니라 "답 + 실행한 SQL + 쓴 정의 + 계보"를 돌려주는 계층
> 에이전트가 사내 DB에 자연어로 질의할 때 가장 큰 위험은 **틀린 지표 정의로 그럴듯한 숫자를 내는 것**이다. auto-ontology 는 메타데이터에서 온톨로지·지식그래프를 생성(Discover)하고, 지표·엔티티 정의를 에이전트에 주입(Ground)하며, 생성 쿼리를 인증된 정의·계보와 대조(Validate)하고, MCP·CLI·API 로 노출(Expose)한 뒤, 사용자 교정을 되먹인다(Learn). 즉 **NL→SQL 의 정확도를 모델이 아니라 의미 계층으로 끌어올리려는 설계**다.

> [!warning] 정확도 수치 0건 — 평가 레포도 결과 미게시
> - README 전체에서 정확도 관련 언급은 **"BIRD 같은 text-to-SQL 벤치를 돌리려면 …을 참조"** 1줄뿐이다(볼트 grep `accuracy|bird` = 1행).
> - 링크된 `NVIDIA/ontology-sql-eval` 은 **`NVIDIA/auto-ontology-eval` 로 301 리다이렉트**(볼트 재확인). 수집기에 따르면 그 README 도 대조군 설계(BIRD 실행정확도 · BEAVER `ex_acc`)만 있고 **결과 수치는 없다**.
> - ★ 하루 +1,430 의 급상승은 "NVIDIA + 온톨로지 + MCP" 노출 효과이며, 성능 근거가 아니다 → [[스타-근거-비동행]].

## 도메인별 추출 (ai-news)
- **신뢰도**: ★9.5k · NVIDIA 공식 · 논문 없음 · 정량 평가 미게시.
- **즉시 활용**: **NO(보류)** — 기본 추론 경로가 NVIDIA NIM(`nvapi-…` 키) 전제다. 기본값 LLM `nemotron-3.5-lightning-30b-a3b` · 임베딩 `nemotron-3-embed-1b` · 리랭커 `llama-nemotron-rerank-vl-1b-v2`. 스택은 Next.js 16 · FastAPI+LangChain · Postgres+pgvector · 선택형 HashiCorp Vault 로 무겁다. 사내 데이터 웨어하우스가 없는 개인 워크플로우에는 대상이 없다.
- **6개월 영향력**: "에이전트에 데이터 접근을 줄 때 **정의 계층을 MCP 로 따로 노출**한다"는 패턴은 [[에이전트-메모리-레이어]] · [[LLM-Wiki]] 와 같은 결 — 지식을 모델 밖에 구조화하고, 답에 근거를 붙인다.
- **대체 관계**: dbt 시맨틱 레이어 · Cube 같은 메트릭 레이어 + text-to-SQL 에이전트 조합을 하나로 묶으려는 시도. 개념적으로 [[EvoOntology]] 와 비교 대상.
- **허와 실**: "근거와 계보를 같이 준다"는 **검사가능성** 쪽 주장은 README 퀵스타트 예시(답 + 실행 SQL + 추론 단계)로 확인된다. "더 정확하다"는 주장은 **검증 불가**. README 가 *"currently not accepting external contributions"* 를 명시 — Apache-2.0 이지만 외부 기여는 닫혀 있다(볼트 grep 1건 확인).
- **액션**: star 만. `NVIDIA/auto-ontology-eval` 에 결과가 게시되면 재방문.

## 관련 페이지
- [[NVIDIA]] · [[EvoOntology]] · [[에이전트-메모리-레이어]] · [[LLM-Wiki]] · [[검사가능성-공사]]
- [[스타-근거-비동행]] · [[선언된-구현체-공백]] (벤치 절은 있으나 결과가 없음)
- 같은 날: [[scenario-skills]] · [[garden-skills]] · [[agent-switch]] · [[pr-agent]]

## 원본
- 출처: https://github.com/NVIDIA/auto-ontology · https://github.com/NVIDIA/auto-ontology-eval
- 확인 범위: GitHub API(볼트 11-07 재조회) · README raw 전체 grep(`not accepting external contributions` 1건 · `accuracy|bird` 1건) · `ontology-sql-eval` 301 대상 확인 · 평가 레포 README 는 수집기 기준(볼트 미열람) · 설치·실행 0회
- 신뢰도: ⭐⭐ (NVIDIA 공식 · ★9.5k · 정량 근거 없음)
