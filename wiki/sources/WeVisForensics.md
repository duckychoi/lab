---
title: "WeVisForensics — 조사관 1 + 검사관 서브에이전트로 AI 생성 영상 탐지 (평균 95.2% · +9.0% · 벤치별 내역 미확인)"
type: source
domain: video-saas
tags: [video-saas, paper, ai-generated-video-detection, forensics, multi-agent, rl, tencent]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.21373]
reliability: medium
---

**논문**: arXiv 2611.21373 · 업보트 54(볼트 11-22 · 수집기 11-21 51) · [[Tencent]] · 저자 7 · 코드 [Tencent/WeVisForensics](https://github.com/Tencent/WeVisForensics) ★51

## 핵심 인사이트
> [!insight] 탐지를 "한 모델의 판정"에서 "어디를 볼지 정하는 조사"로 바꿨다
> 조사관 에이전트가 어떤 아티팩트를 어느 구간에서 볼지 · 언제 결론낼지를 RL 로 빠르게 학습하고, 시각 · 음성 단서별 검사관 서브에이전트는 주석된 아티팩트 구간으로 느리게 개선(이중 시간척도 최적화 DTPO). 학습용 ForenCue-30K.

> [!warning] 평균값만 있다
> 초록 수치는 in-domain · out-of-domain · agentic 벤치 **평균 95.2% · 기존 최고 대비 +9.0%**(볼트 초록 대조 일치). 벤치별 내역과 가장 나쁜 열은 초록에 없다 — OOD 단독 수치가 실사용 지표인데 평균에 묻혀 있다([[복합지표-분해]]). 본문 표 미열람.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 생성 영상 SaaS 에 "AI 생성 표시/검출" 요구가 붙을 때의 참조 구조. 서브에이전트가 구간 단위 근거를 내므로 설명 가능한 판정에 유리.
- **크리에이터 인사이트**: 플랫폼의 AI 영상 라벨링 의무가 강해지면 탐지기가 업로드 파이프라인의 게이트가 된다 — 내 산출물이 어떻게 판정되는지 알아야 한다.
- **경쟁 우위 빈틈**: 탐지기 정확도 평균이 95% 여도 새 생성 모델(H3 · Kling 최신)에 대한 OOD 가 핵심 — 미확인.

## 관련 페이지
- [[Tencent]] · [[WeMM-Video]] (같은 날 · 같은 조직) · [[복합지표-분해]] · [[AI-영상-생성-2026]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.21373
- 확인 범위: HF papers API(초록 전문 · 업보트 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐
