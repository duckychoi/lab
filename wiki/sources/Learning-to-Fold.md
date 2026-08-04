---
title: Learning to Fold — RL 기반 양손 의류 접기 VLA (LeHome Challenge 2026 수상)
type: source
domain: ai-news
tags: [ai-news, hf-papers, robotics, vla, rl, bimanual, manipulation, deformable]
created: 2026-06-29
updated: 2026-06-29
sources: []
reliability: medium
---

# Learning to Fold (LeHome Challenge 2026)

> [!insight] 핵심 인사이트
> HF 데일리 페이퍼 (upvote 4, 2026-06-29). VLA 정책을 **RL로 개선**해 양손(bimanual) 로봇이 천처럼 **변형 가능한 물체(의류)를 접는** 어려운 조작 태스크를 수행. 성공 추정과 어드밴티지 계산을 **하나의 공유 네트워크**로 처리하는 게 핵심 설계. **LeHome Challenge 2026에서 온라인 1위·오프라인 2위** 수상으로 실증된 결과. [[Translation-as-Bridging-Action]]과 함께 이번 데일리의 *체현 조작(embodied manipulation)* 클러스터를 형성 — 강체(rigid)를 넘어 변형체·양손 협응이라는 난도 높은 영역으로 로봇 학습이 전진 중.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 대회 수상(온라인 1위)이라는 외부 검증이 있어 단순 논문보다 신뢰 가점. upvote는 4로 낮으나 결과는 구체적.
- **즉시 활용**: NO — 로봇 하드웨어·조작 연구 영역, 내 워크플로우 직접 적용점 없음.
- **6개월 영향력**: 중간 — 변형체·양손 조작은 가사 로봇의 핵심 난제. "성공 추정+어드밴티지 공유 네트워크" 설계는 다른 RL 정책에도 전이 가능한 아이디어.
- **대체 관계**: 기존 모방학습 단독 접근을 RL 미세개선으로 *보강*하는 계보.
- **허와 실**: 대회 환경 수상이 곧 임의 가정환경 일반화는 아님. 천 종류·조명·초기 상태 변화에 대한 강건성은 별도 검증.
- **액션**: 읽기 — RL 어드밴티지·성공추정 통합 설계만 메모. 직접 구현 대상 아님.

> [!note] 배경 정보
> LeHome Challenge = 가정 환경 로봇 조작 벤치마크 대회. 양손 의류 접기는 변형체+양손 협응이 겹쳐 로봇 조작 중 최난도 군에 속함.

## 관련 페이지
- [[VLA]]
- [[Translation-as-Bridging-Action]]
- [[HiVLA]]
- [[Guava-Embodied-Manipulation]]

## 원본
- 출처: https://huggingface.co/papers/2606.27163
- HF 데일리: upvote 4 (2026-06-29) | LeHome Challenge 2026 온라인 1위·오프라인 2위
- 신뢰도: ⭐⭐⭐ (대회 수상 외부 검증 — 가정환경 일반화는 미검증)
