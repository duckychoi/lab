---
title: IFM — K2-Horizon MoE 모델 공개 조직
type: entity
domain: local-llm
tags: [entity, model-publisher, moe, mova, open-weights, 검증대기]
created: 2026-09-09
updated: 2026-09-09
sources: [K2-Horizon-MoVA-36B-A4B.md]
reliability: low
---

# IFM

> [!note] 정체
> **K2-Horizon-MoVA-36B-A4B** (36B 저장 / 4B 활성 MoE + MoVA 어텐션, 네이티브 512K)를 Apache-2.0으로 공개한 HF 조직. 볼트 최초 수집 **2026-09-09**.

## 확인된 사실

- **모델**: [[K2-Horizon-MoVA-36B-A4B]] — 생성 2026-09-01, 수집 시점 다운로드 **3,205** · ♥247 · Apache-2.0 · gated=False.
- **기술 주장**: **MoVA(Mixture-of-Values)** 어텐션. Terminal-Bench 2.1에서 카드 비교표 **전 모델 1위(58.6)**.
- **공개 상태**: 가중치만 공개. **중간 체크포인트 · 학습 데이터 · 코드는 "예고(coming)" 상태로 미공개.**

> [!warning] 신뢰도 low — 검증 대기
> ① 조직 실체·소속을 볼트가 **전혀 확인하지 못했다**. 이름 `IFM` 의 의미도 미확인.
> ② 벤치마크가 **전부 자체 보고**이며 제3자 재현이 없다.
> ③ **미공개 예고 항목**이 있다 — 09-08 [[AutoHedge]] 건에서 정착한 규칙(*README의 "Coming soon"은 검증되지 않은 약속*) 적용 대상.
> ④ 생성 8일차, 다운로드 3,205로 **커뮤니티 검증이 아직 형성되지 않았다.**
> → **엔티티로 등록하되 주장은 인용하지 않는다.** 4주 뒤 재확인 대상(→ actionable).

## 관련 페이지
- [[K2-Horizon-MoVA-36B-A4B]]
- [[에이전트축-분기]]
- [[측정도구-먼저-반증]]
