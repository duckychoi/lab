---
title: "PISA / PISA-E — 프롬프트별 비용 인지 단일 모델 라우팅과 앙상블 라우팅"
type: source
domain: local-llm
tags: [local-llm, routing, inference-cost, ensemble, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.10193]
reliability: medium
---

**논문**: arXiv 2611.10193 · HF 업보트 19 · 저자 4명(Saul Urso · Emanuele Carlini · Patrizio Dazzi · Matteo Mordacchini) · 코드 링크 없음 · HF Daily 11-12 페이지.

## 핵심 인사이트
> [!insight] 라우터의 다음 단계 — "어떤 모델 하나"가 아니라 "몇 개를, 어떤 조합으로"
> PISA 는 소프트 클러스터 소속도 + 모델별 예측기로 개별 모델 능력을 추정하는 단일 모델 라우터. PISA-E 는 그 추정 위에서 **앙상블 구성과 크기를 프롬프트별로** 고르며, 다루기 쉬운 앙상블 성공 대리 지표 덕에 앙상블 전용 학습이 필요 없다. 비용–품질 선호는 **추론 시 재학습 없이** 조절. → 볼트 [[LLMRouter]] 계열의 확장.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 4개 라우팅 벤치(ID · OOD). PISA = 평가한 단일 라우터 중 매크로 평균 비용–성능 hypervolume 1위. PISA-E = 품질 우선 시 앙상블 기법 중 1위, 최강 경쟁 대비 **+2.09%p(ID) · +2.87%p(OOD)**; 일부 저비용 운영점에선 경쟁 기법 성능을 넘으면서 평균 추론 비용 **약 −36%(ID) · −25%(OOD)**.
- **트레이드오프**: 앙상블은 호출 수만큼 지연이 늘 수 있다 — 초록은 비용만 말하고 **지연은 언급 없음**.
- **Hermes 적용**: 로컬 소형 모델 + 클라우드 대형 모델 혼용 구성에서 "쉬운 프롬프트는 로컬" 라우팅의 설계 참고. 코드가 없어 직접 적용은 NO.

> [!warning] "평가한 기법 중"
> 두 1위 주장 모두 *"among the evaluated"* 한정. 대상 모델 풀 · 절대 점수 · 벤치 이름은 초록에 없음 → [[비매칭-비교]] 여부 확인 불가.

## 관련 페이지
- [[LLMRouter]] · [[선택비용과-중복성]] · [[비매칭-비교]] · [[SteerDistill]](같은 배치 · 추론 비용 축) · [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2611.10193
- 확인 범위: HF papers API 초록 전문 · 저자(볼트) · 🔴 본문 미열람 · 코드 없음
- 신뢰도: ⭐⭐
