---
title: Orca — The World is in Your Mind (범용 월드 파운데이션 모델)
type: source
domain: ai-news
tags: [ai-news, hf-paper, world-model, world-foundation-model, multimodal, embodied-ai, next-state-prediction]
created: 2026-07-01
updated: 2026-07-01
sources: []
reliability: medium
---

# Orca: The World is in Your Mind (HF papers 2606.30534)

> [!insight] 핵심 인사이트
> **HF 데일리 페이퍼 1위 (↑158, 2026-07-01).** "다음 토큰/프레임/액션"을 따로 최적화하는 대신 **Next-State-Prediction(다음 상태 예측)** 하나로 통합해, 멀티모달 신호로부터 **단일 월드 잠재공간(unified world latent space)**을 학습하는 범용 **월드 파운데이션 모델**. 학습을 두 축으로 나눈 게 핵심 — **무의식 학습(unconscious learning)**은 연속 영상에서 촘촘한 자연 상태전이를, **의식 학습(conscious learning)**은 언어로 기술된 사건·VQA 감독으로 드문 의미 있는 상태전이를 잡는다. 사전학습은 **영상 12.5만 시간 + 사건 주석 1.6억 건** 규모. 학습 후 백본을 **얼려두고 경량 모달리티 디코더만** 붙여 텍스트 생성·이미지 예측·**체현 액션 생성(embodied action)** 세 갈래로 읽어내며, 동급 특화 모델을 능가한다고 주장. [[World-Action-Models-Survey]]·[[In-Context-World-Modeling]]가 정리한 "월드 모델→행동" 흐름의 파운데이션 모델판.

## 도메인별 추출 (ai-news / slam-3dgs 교차)

- **신뢰도**: ⭐⭐⭐ — HF 데일리 1위(↑158)로 관심도는 최상위. 단 "동급 특화 모델 초과"는 논문 자체 벤치이고 baseline·규모 세부는 원문 확인 필요. 저자·소속 미표기 상태.
- **즉시 활용**: NO — 파운데이션 모델 연구로, 당장 내 워크플로에 붙일 오픈 구현체는 아직 없음(코드 공개 여부 확인 필요). 개념적 방향성 참고용.
- **6개월 영향력**: 높음 — "언어 월드 모델([[Qwen-AgentWorld]])"·"인컨텍스트 월드 모델링([[In-Context-World-Modeling]])"에 이어 **단일 잠재공간+동결 백본+경량 디코더**라는 재사용 아키텍처가 표준화되면, 영상·로봇·이미지 예측을 한 백본으로 처리하는 파이프라인이 열림.
- **대체 관계**: 영상 생성·VLA·이미지 예측을 각각 별도 모델로 돌리던 구조를 *하나의 월드 백본 + 디코더*로 통합 시도. [[slam-3dgs]] 축(체현 액션)과 [[video-saas]] 축(이미지/영상 예측)의 교차점.
- **허와 실**: "The World is in Your Mind"·"unconscious/conscious learning" 같은 네이밍은 서사적 포장. 실체는 next-state-prediction + frozen backbone + lightweight decoder라는 공학적 조합. 12.5만 시간 영상 규모는 재현 장벽이 큼(개인 재현 불가).
- **액션**: 코드/체크포인트 공개 여부와 embodied action readout 벤치 세부 확인 → 공개 시 로봇/영상 도메인 관심 목록에 편입.

> [!question] 미해결 질문
> 코드·가중치 공개? "동급 특화 모델 초과"의 baseline과 규모? embodied action readout의 실제 로봇 태스크 성능?

## 관련 페이지
- [[World-Action-Models-Survey]]
- [[In-Context-World-Modeling]]
- [[Qwen-AgentWorld]]
- [[Trimming-Long-Tail]]
- [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2606.30534 (arXiv:2606.30534)
- HF 데일리: 1위 ↑158 (2026-07-01)
- 신뢰도: ⭐⭐⭐ (데일리 1위 관심도 — 벤치 baseline·코드 공개는 미확인)
