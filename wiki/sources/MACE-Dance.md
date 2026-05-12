---
title: MACE-Dance — 음악 기반 댄스 영상 생성 MoE 캐스케이드 모델
type: source
domain: ai-news
tags: [ai-news, video-saas, hf-paper, music-to-dance, moe, 3d-motion, video-generation, pose-animation, sota]
created: 2026-05-11
updated: 2026-05-11
sources: []
reliability: high
---

# MACE-Dance: 음악→댄스 영상 생성

> [!insight] 핵심 인사이트
> **MoE(Mixture of Experts) 기반 캐스케이드** 구조로 **음악 → 3D 동작 → 영상 합성**을 단계별 분리 처리. 3D 댄스 생성 및 포즈 기반 애니메이션 **각각 SOTA** 달성. "음악을 넣으면 캐릭터가 맞춰 춤추는 영상"이 실용 수준에 도달. [[AI-영상-생성-2026]]에서 가장 실용적 응용 가능한 연구 중 하나 — 크리에이터 콘텐츠 자동화에 즉시 연결.

## 도메인별 추출 (video-saas)

- **기능 벤치마킹**: 음악→댄스 영상 자동 생성. MoE 캐스케이드: 각 전문가 모듈이 다른 음악 장르/스타일 처리 → 다양성+일관성 동시 확보
- **크리에이터 인사이트**: 뮤직비디오, SNS 댄스 콘텐츠 자동화 직접 연결. 사람이 춤추는 영상 없이 음악만으로 고품질 댄스 영상 생성
- **프롬프트 패턴**: 음악 파일(오디오) 입력 → 리듬 분석 → 3D 동작 시퀀스 → 포즈 기반 영상 렌더링
- **워크플로우**: Music → MACE-Dance → 댄스 영상. 기존 T2V(텍스트→영상)와 달리 음악이 직접 동작을 구동
- **경쟁 우위 빈틈**: 음악-동작 동기화가 기존 영상 AI(Runway, Kling 등)의 약점 — MACE-Dance가 채우는 갭

## 핵심 내용

### 아키텍처
- **MoE 캐스케이드**: 음악 특성에 따라 다른 전문가 모듈 활성화
- **3단계 파이프라인**:
  1. 음악 분석 (리듬, 비트, 감정)
  2. 3D 동작 생성 (SOTA)
  3. 포즈 기반 영상 합성 (SOTA)

### 성능
- 3D 댄스 생성 SOTA
- 포즈 기반 애니메이션 SOTA

> [!action] 당장 할 것
> 공개 데모/API 확인 → 뮤직비디오 자동화 영상 SaaS 기능으로 통합 가능성 검토

## 관련 페이지
- [[AI-영상-생성-2026]]
- [[Seedance]]
- [[Higgsfield]]
- [[OmniShow]]
- [[LPM-1.0]]
- [[MACE-Dance]] → video-saas 도메인 교차

## 원본
- 출처: https://arxiv.org/abs/2512.18181
- 신뢰도: ⭐⭐ (arXiv 논문)
