---
title: Know Before Fix — QA로 레포 지식을 먼저 획득하는 이슈 해결 파이프라인
type: source
domain: ai-news
tags: [ai-news, hf-paper, swe-bench, code-agent, repository-knowledge, issue-resolution, retrieval]
created: 2026-07-15
updated: 2026-07-15
sources: []
reliability: medium
---

# Know Before Fix: QA-Driven Repository Knowledge Acquisition for Software Issue Resolution

> [!insight] 핵심 인사이트
> HF 추천 3 (2026-07-15). **코드 이슈를 고치기 전에 "이 레포가 어떻게 생겼나"를 QA(질문-답변) 방식으로 먼저 학습해 수정 대상 파악 정확도를 높이는 파이프라인.** 기존 SWE-bench류 에이전트가 이슈를 받자마자 곧바로 파일을 뒤지며 패치를 시도한다면, 이쪽은 그 앞단에 *레포에 대한 질문을 스스로 생성·답변해 구조·의존성·규칙을 내재화*하는 단계를 끼운다("고치기 전에 알아라"). 이는 이 위키의 인제스트 철학과 동형 — **소스를 즉시 요약하지 말고, 먼저 도메인 템플릿 질문에 답하며 구조를 파악한 뒤 작성**하는 것과 같은 발상. 코드 에이전트판 "read-before-write". [[Long-Horizon-Terminal-Bench]]가 진단한 "에이전트가 어디서 이탈하나" 문제의 처방 각도.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF 추천 3으로 주목도는 낮음. 미래형 ID(2607.11111)로 초록 수준 자동수집 기반·원문 미검증(reliability medium).
- **즉시 활용**: MAYBE — Claude Code 워크플로우에서 큰 레포 진입 시 "먼저 QA로 구조 파악" 프리스텝을 프롬프트 관행으로 차용 가능(파일 즉시 편집 전 아키텍처 질의).
- **6개월 영향력**: SWE-bench류 자동 이슈 해결에서 "탐색 전 지식 획득" 단계가 표준 서브루틴이 되는 흐름. 오호출·엉뚱한 파일 수정을 줄임.
- **대체 관계**: 순수 검색(RAG) 기반 코드 로컬라이제이션을 보완 — 검색이 "관련 청크"라면 이건 "구조적 이해"를 선제.
- **허와 실**: 자가 QA 품질이 낮으면 앞단 오버헤드만 늘고 정확도 이득 미미. 실제 SWE-bench 점수 개선 폭은 원문 확인 필요.
- **액션**: 대형 레포 작업 시 "핵심 QA 5문항 자문자답 → 그다음 수정" 프롬프트 관행을 개인 워크플로우에 실험 적용.

## 관련 페이지
- [[Long-Horizon-Terminal-Bench]]
- [[Know-Before-Fix]]
- [[Claude-Code-워크플로우]]
- [[LLM-Wiki]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.11111
- HF 추천: 3 (2026-07-15)
- 신뢰도: ⭐⭐ (미래형 ID·초록 수준 자동수집, 원문 미검증)
