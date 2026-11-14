---
title: "SimpleHC — Hyper-Connections 를 분해해 믹싱을 걷어낸 단순화 (학습 시간 +2.4% · 15B→30B MoE · arXiv 2611.05984)"
type: source
domain: ai-news
tags: [ai-news, architecture, hyper-connections, residual, training-efficiency, moe]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.05984]
reliability: medium
---

**논문**: [arXiv 2611.05984](https://huggingface.co/papers/2611.05984) *On the Design of Hyper-Connections: Simplification, Stability, and Scalability* · 업보트 **26**(수집기: 22) · 저자 11명(Xiangdong Zhang … **Junchi Yan**) · 발행 2026-11-04 · 코드 aHapBean/SimpleHC ★20 (HF papers API 볼트 실측)

## 핵심 인사이트
> [!insight] 두 부품 중 하나만 있어도 된다 — 그리고 비용의 원인은 믹싱이 아니었다
> 프런티어 LLM 에 채택이 늘고 있는 Hyper-Connections(HC/mHC)를 분해:
> 1. **효과**: "믹싱 없는 학습형 읽기/쓰기 게이트"와 "고정 게이트 + 무제약 믹싱" — **둘 중 하나만으로 mHC 와 비슷한 성능**.
> 2. **비용**: 학습 오버헤드의 큰 원인은 믹싱이 아니라 **확장된 잔차 상태에 반복 접근**하는 것(믹싱이 없어도 발생).
>
> SimpleHC = 잔차 믹싱 제거 + 공유 메모리 접근(층별 게이트가 그룹 진입 상태를 공유 → 배치 읽기 · 지연 쓰기, 스칼라 보정으로 앞선 서브층 기여를 정확히 보존). 최대 시험 규모에서 바닐라 잔차 대비 **엔드투엔드 학습 시간 +2.4%**, 15B → 30B MoE 에서 mHC 와 비슷한 성능, 더 매끄러운 그래디언트.

> [!warning] 절감 폭은 초록에 없다
> +2.4% 는 바닐라 대비다. mHC 자체의 오버헤드 수치가 초록에 없어 "얼마나 줄였나"는 본문 확인 필요. 성능은 "comparable"(우위 주장 아님).

## 도메인별 추출 (ai-news)
- **신뢰도**: 업보트 26 · 코드 공개 · 15B–30B 규모 실험.
- **즉시 활용**: NO — 사전학습 아키텍처 선택의 문제.
- **6개월 영향력**: 공개 모델 카드에 HC 변종이 등장할 때 읽는 기준(믹싱 유무 · 게이트 방식).
- **대체 관계**: mHC 의 단순화 대안.
- **허와 실**: "단순한 쪽이 같은 성능"이라는 절제된 주장. 수치 하나(+2.4%).
- **액션**: 없음.

## 관련 페이지
- [[선택비용과-중복성]](둘 중 하나로 충분 = 중복된 부품) · [[Mamba4]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2611.05984
- 확인 범위: HF papers API 초록 전문 · 저자 · 🔴 본문 · 코드 미열람
- 신뢰도: ⭐⭐ (업보트 26 · 코드 공개)
