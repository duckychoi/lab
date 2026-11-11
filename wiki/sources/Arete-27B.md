---
title: "Arete-27B — Qwen3.8-27B 에 SFT 만으로 국가 프레이밍 답변을 22% → 0.9% 로: 사실 점수 2.32 → 2.98/5 (teacher 3.96 · 자체 평가셋 · 디코딩 조건 다름)"
type: source
domain: local-llm
tags: [local-llm, hf-model, fine-tuning, sft, value-alignment, qwen, nousresearch]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/NousResearch/Arete-27B]
reliability: medium
---

**모델**: [NousResearch/Arete-27B](https://huggingface.co/NousResearch/Arete-27B) · dl30 **3,431** · likes **416** · created 2026-11-06 · Apache-2.0 · base `Qwen/Qwen3.8-27B` · 27.36B (HF models API 볼트 실측)

## 핵심 인사이트
> [!insight] 구조를 건드리지 않고 SFT 만으로 답변 성향을 옮긴다
> 7개 가치 범주에 대해 **2만 프롬프트**(카드 63행 "twenty thousand")를 만들고 teacher(Inkling) 응답으로 **SFT 만** 수행했다. 자체 Propaganda_Eval(803문항 · 판정 LLM Grok 4.7)에서 사실 점수 **2.32 → 2.98 / 5**, 선전 프레이밍 포함 답변 **22% → 0.9%**, 0점 답변 359 → 216(카드 21·137·140·146행). 일반 능력은 Hermes Bench 65.77% → 65.60%(154행)로 유지.

> [!warning] 측정 범위 안에서의 감소다
> - **평가셋 · 루브릭 · 판정 모델 선택이 전부 개발사 자체 설계**다. 판정은 LLM 1종.
> - 사실 점수 2.98 은 **teacher 3.96** 은 물론 같은 표의 **Nemotron 3 Ultra 3.22** 보다도 낮다(카드 132·136행). "편향 제거 완료"가 아니다.
> - 디코딩 조건: Arete · Qwen 은 thinking off · temperature 0, 다른 행은 temperature 0.6 — 카드가 *"not identical decoding settings"* 라고 직접 적었다(142행). 정방향 사례.
> - Terminal-Bench 2.1 67% → 70% 에 대해 카드는 *"We do not take credit for any seeming improvement"* 라고 명시(159행). 요약할 때 이 문장을 떼면 [[한정어-탈락]] 이 된다 — 수집기는 지켰다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: [[Qwen3.8-27B]] 를 이미 돌리는 환경이면 같은 하드웨어로 교체 가능(구조 변경 없음 — 수집기: 비전 인코더 동결 · MTP 헤드 비활성).
- **메모리 아키텍처**: 해당 없음.
- **Hermes 적용**: 조건부 — 정치·사회 주제 답변이 필요한 용도일 때만 의미. 코딩·일반 용도에서는 원본과 차이 없음(Hermes Bench 0.17%p 차, 카드는 노이즈로 해석).
- **트레이드오프**: 일반 능력 손실 없음(카드 측정 범위) ↔ 특정 주제 답변 성향 변화. 다른 방향의 편향이 생겼는지는 이 평가셋으로 알 수 없다.
- **오픈소스 구현체**: 가중치 Apache-2.0 · 평가셋 `NousResearch/Propaganda_Eval` 공개(카드 93행).

## 관련 페이지
- [[NousResearch]] · [[Qwen3.8-27B]] · [[hermes-agent]] · [[DeepSeek-V4-Pro-Qwen3.5-9B-UNCENSORED-heretic]](검열 제거 계열 — 방법이 다르다: 저쪽은 거부 제거, 이쪽은 SFT) · [[Ripple-65B-Preview]]

## 원본
- 출처: https://huggingface.co/NousResearch/Arete-27B
- 확인 범위: HF models API · 카드 raw(9,533B) 수치 행 대조 · 🔴 평가셋 · 루브릭 미열람 · 실행 0건
- 신뢰도: ⭐⭐ (dl30 3,431 · 자체 평가)
