---
title: "DPDM — LLM 은 표현만, 판단은 동결된 표형 예측기 LimiX-2 가. 78.80→84.92% 는 '각자의 이력 예산' 조건, 동일 조건은 82.33%"
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent, decision-making, tabular-foundation-model, limix, in-context-learning, stable-ai, 비매칭-비교]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/papers/2611.02075, LimiX-2.md]
reliability: medium
---

**논문**: arXiv 2611.02075 · HF 업보트 **81**(볼트 11-08 API) — 🔴 수집기 11-07 보고 **114** 와 불일치 → [[계수기-배수]] · 소속 [[Stable-AI]] · 코드 링크 없음

## 핵심 인사이트
> [!insight] "경험 학습"을 LLM 밖으로 빼냈다
> 도구 판단·후보 선호·추론 단계 평가를 전부 *증거 + 질의 → 조건부 예측* 하나로 통일. LLM(Qwen3.5-27B)은 기록을 의미 표현으로 바꾸기만 하고, **구조화 데이터로 사전학습된 동결 예측기 하나([[LimiX-2]])**가 배포 중 쌓인 이력을 컨텍스트로 받아 목표를 예측한다. **두 모델 모두 파라미터 업데이트 없이** 이력이 늘수록 정확도가 오른다 ⇒ 에이전트의 "경험"이 가중치가 아니라 **표형 ICL 컨텍스트**에 쌓인다. 볼트가 9월에 정리한 LimiX-2 의 `p(x,y)` 설계가 에이전트 의사결정의 백엔드로 쓰인 첫 사례.

> [!warning] 헤드라인 수치의 조건이 다르다
> 초록 원문: *"78.80% with few-shot prompting to 84.92% **under their respective evaluated history budgets**, and reaches **82.33% with identical histories and queries**"*. ⇒ **같은 조건 비교는 +3.53%p**이고 +6.12%p 는 DPDM 에 더 큰 이력 예산을 준 결과다 → [[비매칭-비교]]. ToolPRMBench BFCL **+34.26%p** · ToolSandbox **+28.87%p** 도 *"at the methods' respective evaluated history budgets"* 단서가 붙어 있다. 수집기 요약은 "(각자 이력 예산)"을 괄호로 남겼다 — ✅ 한정어 보존.

## 도메인별 추출 (ai-news)
- **즉시 활용**: NO(코드 없음). 다만 *"라우팅·도구선택 로그를 표로 쌓고 표형 예측기로 판단"* 은 우리 봇 라우팅 개선 아이디어로 유효.
- **6개월 영향력**: 표형 파운데이션 모델(TabPFN·LimiX)이 에이전트 스택의 "판단 레이어"로 들어오는 흐름.
- **허와 실**: 50벤치 평균의 구성 미확인(초록만).

## 관련 페이지
- [[LimiX-2]] · [[Stable-AI]] · [[TabPFN]] · [[비매칭-비교]] · [[계수기-배수]]
- 같은 배치: [[Drex]](같은 "생성 없이 결정" 축)

## 원본
- 출처: https://huggingface.co/papers/2611.02075
- 확인 범위: HF papers API 초록 원문(볼트 11-08) · 본문 미열람
- 신뢰도: ⭐⭐
