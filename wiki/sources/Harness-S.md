---
title: "Harness-S — 실패한 그룹만 형제 하니스로 구조해 RL. 9B 가 GRPO 대비 크게 오르지만 AppWorld·SWE-Gym 에선 프런티어 아래"
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent-rl, harness, grpo, appworld, swe-gym, sjtu]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/papers/2611.04277]
reliability: medium
---

**HF**: upvote **57**(볼트 11-07 · 수집기 32 · 11-06 3위) · Shanghai JiaoTong University · 저자 11명 · arXiv 2611.04277 · 코드 [DeepExperience/Harness-S](https://github.com/DeepExperience/Harness-S) **★55 · Apache-2.0**(볼트 11-07 · 수집기 ★31 · HF 캐시 20)

## 핵심 인사이트
> [!insight] 하니스 변형은 서로 다른 실패를 고친다 — 그 차이를 학습 신호로 쓴다
> 공통 베이스에서 진화시킨 하니스 변형들이 **서로 다른 실패를 고친다**(Locality · Complementarity · Nonstationarity)는 관찰에서 출발. 수리 방향별 **형제 하니스 풀을 오프라인 진화로 만들어 고정**하고, 학습 중 **베이스 하니스 초기 시도가 전부 실패한 그룹만** 같은 정책이 형제 하니스로 재롤아웃해 RL 그룹을 대체한다. 평가는 다시 원래 하니스 `H_0` 에서 — 즉 **하니스를 바꿔 얻은 성공 궤적을 정책 안으로 증류**한다. 볼트 [[하네스형-에이전틱-RL]] · [[하네스-설계-축]] 의 "하니스가 성능의 절반" 논지를 RL 로 되먹인 사례.

> [!warning] Table 1 (`Pass@3` / `Avg@3`, 테스트 하니스 `H_0`) — 볼트 본문 검출 12/12
> - Qwen3.5-9B: GRPO **64.89 / 53.31 → Harness-S 72.52 / 62.34**(AppWorld) · SWE-Gym Pass@3 28.13 → 40.00 · DBBench 69.67 → 76.33. 4B AppWorld Pass@3 60.31 → 67.56.
> - 프런티어 대조(같은 `H_0`): GPT-6-Sol AppWorld **82.82** · SWE-Gym **53.13** — **9B Harness-S 는 이 둘에서 프런티어보다 낮다**. DBBench 76.33 만 GPT-6-Sol 71.33 을 넘고, GLM-5.3-Flash 76.67 보다는 0.34 낮다.
> - Harness-S 행만 `± 표준편차` 가 있고 비교 행에는 없다. Table 3 행동 빈도(예: "Schema lookup before first API use" 22.9 → 38.2 → 67.6%)는 **LLM 이 궤적을 라벨링한 값** → [[요약자와-판정자-분리]].

## 도메인별 추출 (ai-news)
- **신뢰도**: SJTU · 코드 공개(★55, `.py` 202개 · CI 포함).
- **즉시 활용**: NO — RL 학습 인프라 필요.
- **6개월 영향력**: 소형 로컬 모델을 에이전트로 쓸 때 "하니스를 고치면 되는 실패"와 "정책이 배워야 하는 실패"를 분리하는 관점.
- **허와 실**: GRPO 대비 +7~12점은 강하지만 "프런티어 수준"은 DBBench 한 칸.
- **액션**: 읽기 — [[Harness-Design-Empirical]] · [[Self-Evolving-Agent-Harness]] 와 묶어 하니스 축 정리 시 참조.

## 관련 페이지
- [[하네스형-에이전틱-RL]] · [[하네스-설계-축]] · [[Harness-Design-Empirical]] · [[Self-Evolving-Agent-Harness]] · [[HarnessOpt-Bench]]
- [[요약자와-판정자-분리]] · [[Qwen]]
- 같은 날 논문: [[VFlash]] · [[BestRand]] · [[TailSteer]] · [[WeLM-Image]]

## 원본
- 출처: https://huggingface.co/papers/2611.04277 · https://arxiv.org/html/2611.04277v1 · https://github.com/DeepExperience/Harness-S
- 확인 범위: HF API · arXiv HTML 전문 grep(수집기 인용 12개 수치 전부 검출) · GitHub API · 실행 0회
- 신뢰도: ⭐⭐ (SJTU · 코드 공개)
