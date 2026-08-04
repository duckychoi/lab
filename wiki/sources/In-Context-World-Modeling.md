---
title: In-Context World Modeling (ICWM) — 로봇 제어용 인컨텍스트 월드 모델링
type: source
domain: ai-news
tags: [ai-news, hf-daily-paper, robotics, world-model, vla, in-context-learning, embodied-ai]
created: 2026-06-27
updated: 2026-06-28
sources: []
reliability: medium
---

# In-Context World Modeling for Robotic Control (ICWM)

> [!insight] 핵심 인사이트
> HF 데일리 페이퍼 상위(upvote 45, 2026-06-28 ← 41, 06-27). **시스템 식별(system identification)을 인컨텍스트 적응 문제로 재정의**한 연구. 기존 VLA(Vision-Language-Action) 모델은 현재 관측+언어 지시에만 조건을 걸어, 카메라 시점이 바뀌거나 로봇 형태가 달라지면 일반화에 실패한다. ICWM은 정책이 **짧은 자기생성·태스크 무관 상호작용 기록**에서 시스템 변수(카메라 각도, 로봇 모폴로지 등)를 스스로 추론하게 만든다. 일반적인 in-context learning이 "태스크를 시연"하는 것과 달리, ICWM은 "**시스템이 어떻게 작동하는가**"를 파악하는 데 초점을 둔다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF 데일리 상위(upvote 45, 06-28)로 커뮤니티 관심 높음. 단 실로봇·시뮬 실험 결과가 논문 클레임 수준이라 동료평가 전. 자동수집은 OpenMOSS로 태깅했으나 페이퍼 페이지상 1저자 Siyin Wang·SII(상하이) 소속으로, 정확한 주관 기관은 검증 필요.
- **즉시 활용**: NO — 로봇 제어 도메인. 내 워크플로우와 직접 무관.
- **6개월 영향력**: 중간 — "파인튜닝 없이 새 환경 제로샷 적응"은 embodied AI의 핵심 난제. 성공하면 VLA 배포 비용 구조를 바꾼다.
- **대체 관계**: 별도 도구 대체 아님. 월드 모델 계열([[Cosmos-3]], [[DreamX-World-1.0]], [[Kairos-World-Model-Stack]])의 "적응" 축 보강.
- **허와 실**: "novel camera viewpoint에서 표준 VLA 대비 유의미 개선"이 핵심 주장. 시연/벤치 규모는 추가 확인 필요.
- **액션**: 관망. 로보틱스/월드모델 동향 추적용 북마크.

> [!note] 방법 요점
> 컨텍스트 윈도우를 활용해 정책이 task-agnostic 상호작용 히스토리로부터 시스템 변수를 자동 추론 → 파라미터 업데이트 없이 새 구성에 적응. 시뮬·실로봇 실험에서 표준 VLA 베이스라인 대비 개선(특히 새 카메라 시점).

> [!warning] 신뢰도 주의
> 주관 기관 표기(OpenMOSS vs SII) 불일치 — 자동수집 메타와 페이퍼 페이지가 다름. 동료평가 전 프리프린트.

## 관련 페이지
- [[Cosmos-3]]
- [[DreamX-World-1.0]]
- [[Kairos-World-Model-Stack]]
- [[Qwen-AgentWorld]]
- [[openpilot]]

## 원본
- 출처: https://huggingface.co/papers/2606.26025
- HF 데일리: upvote 45 (2026-06-28) ← 41 (2위, 06-27)
- 1저자/소속: Siyin Wang 외, SII(추정) — 자동수집은 OpenMOSS 태깅
- 신뢰도: ⭐⭐⭐ (HF 상위 프리프린트, 동료평가 전)
