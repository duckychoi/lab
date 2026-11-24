---
title: "gepa-ai/gepa — LLM 반성 + 파레토 진화 탐색으로 프롬프트 · 코드 · 에이전트 구성을 최적화(GEPA)"
type: source
domain: ai-news
tags: [ai-news, github, prompt-optimization, evolutionary-search, reflective-evolution, evaluation, dspys]
created: 2026-11-24
updated: 2026-11-24
sources: [https://github.com/gepa-ai/gepa, https://arxiv.org/abs/2507.19457]
reliability: medium
---

**GitHub**: ★7,558(볼트 API 11-24 · 수집기 11-23 7,543) · 당일 +10(Jupyter Notebook Trending) · 표기 Jupyter Notebook(핵심은 Python 패키지 `pip install gepa`) · MIT · 생성 2025-08-05 · HEAD `ce5b0d6e3d`(11-09 — 최근 push 느림) · 논문 arXiv 2507.19457

## 핵심 인사이트
> [!insight] 트레이스를 스칼라 보상 하나로 뭉개지 않는다 — 실패 로그를 읽고 진화한다
> 평가 지표가 있는 모든 **텍스트 파라미터**(시스템 프롬프트 · 코드 · 에이전트 구조 · 스케줄링 정책 · SVG)를 최적화. 루프: 파레토 전선에서 후보 선택 → 미니배치 실행으로 전체 실행 트레이스 수집 → LLM 이 에러 · 프로파일 로그를 읽고 실패 원인 진단 → 조상들의 교훈을 반영해 변이 → 개선 시 채택. RL 이 트레이스를 스칼라 보상으로 압축하는 것과의 차별점이 스스로의 정체성. DSPy 에 `dspy.GEPA` 내장, 임의 아티팩트용 `optimize_anything` API, Claude Code 용 플러그인(`/plugin install gepa-optimize-anything@gepa`) 제공.

> [!warning] 상단 표 수치 다수는 외부 사례 인용
> README 본체 수치: AIME 2025 GPT-4.1 Mini **46.6% → 56.6%**(+10%p, 평가 150회) · DSPy 전체 프로그램 진화 MATH **67% → 93%** · 평가 횟수 100–500회 vs GRPO 5,000–25,000+("RL보다 35배 빠름") · ARC-AGI 에이전트 32% → 89% · Jinja 코딩 에이전트 해결률 55% → 82%. 🔴 반면 **"90배 저렴(Databricks)" · 클라우드 스케줄링 −40.2% 등 상단 표 다수는 외부 블로그 · 자사 블로그 링크로만 제시된 사례 수치**이고 같은 조건 대조표는 README 에 없다([[비매칭-비교]] 위험). reflection LM 으로 GPT-5 급 상위 모델 호출 비용이 별도로 든다.

## 도메인별 추출 (ai-news)
- **실용성**: 평가 함수만 짤 수 있으면 스킬 · 프롬프트 튜닝에 바로 쓸 수 있는 성숙 도구. **볼트의 `auto-research` 스킬 자율 개선 루프와 목적이 겹친다** — 후보 비교 대상.
- **구조적 위치**: 가중치를 전혀 건드리지 않고 **텍스트 파라미터만 진화**시킨다 → [[동결-교정층]] (신설)의 3번째 표본 — 본체(모델)는 동결, 판단·교정은 바깥층.
- [[RSI-프레이밍]] 관점: 볼트에는 [[RSIHub]] · [[RSI-프레이밍]]에 언급만 있고 소스 문서가 없었다 — 이번이 첫 소스 등재.
- **액션**: 설치 후 볼트 스킬 1개에 적용 시험(actionable 등재).

## 관련 페이지
- [[RSIHub]] · [[RSI-프레이밍]] · [[에이전트-스킬]] · [[SkillEvaluator]] · [[동결-교정층]] · [[ai-news]]

## 원본
- 출처: https://github.com/gepa-ai/gepa · arXiv 2507.19457
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 · 생성일 — 볼트 11-24) · README 수치는 수집기 11-23 판독, 볼트 문자열 검증 미실시 · 논문 본문 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐
