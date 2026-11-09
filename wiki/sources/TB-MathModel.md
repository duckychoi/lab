---
title: "TB-MathModel — 실제 CUMCM·MCM 18문제를 컨테이너 터미널 과제로, Lean 4 의무 624개로 실현 가능성까지 게이트. 최고 64.58%, 오픈 모델 59.81% 를 1/100 비용으로"
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, agentic, lean4, verifiable, math-modeling, terminal-bench]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/papers/2611.08237]
reliability: medium
---

**논문**: [2611.08237](https://huggingface.co/papers/2611.08237) · IDEA FinAI · 업보트 12 · 코드 [wxj630/terminal-bench-math-modeling](https://github.com/wxj630/terminal-bench-math-modeling) ★5 · 원제 *"The **First** Agentic and Verifiable Benchmark for …"*

## 핵심 인사이트
> [!insight] LLM 판사 대신 "기준 근접 + 물리적 실현 가능" 두 조건을 기계 검증
> 최종 질문의 수치 핵심을 **수상 논문 여러 편의 재현값**과 비교(기준보다 나은 답은 감점 없음 = 방향성 단측 채점), **프로그램 게이트(6종 불변식) + Lean 4 증명 의무 624개** — 불가능한 답은 0점. ⇒ 에이전트 장기 과제의 궤적 수집용 신호로도 설계.

> [!warning] 비용 문장 원문 깨짐 — 볼트 판독
> 초록 원문: *"the strongest reach … 64.58%, while the `\2.54` open model holds 59.81% at 1/100`$` the cost"*. LaTeX 이스케이프가 어긋난 것으로 보이며 **"$2.54 오픈 모델 · 1/100 비용"** 으로 읽힌다(볼트 추정 — 확인 필요). 18문제 × 7출전 × 3시드 = 소표본, 모델별 표 미열람.

## 도메인별 추출 (ai-news)
- **신뢰도**: 논문 + 코드(★5) · 소표본 벤치
- **즉시 활용**: NO(연구용) — 단 "단측 채점 + 실현 가능성 게이트" 설계는 자체 에이전트 평가에 차용 가능
- **허와 실**: "First" 주장은 제목에만 — 볼트 미검증

## 관련 페이지
- [[벤치마크-외부축]] · [[하네스-설계-축]] · [[VisSearch-Bench]](11-08 벤치)

## 원본
- 출처: https://huggingface.co/papers/2611.08237
- 확인 범위: HF papers API 초록(볼트 재조회 · 64.58/59.81/624/18 검출)
- 신뢰도: ⭐⭐
