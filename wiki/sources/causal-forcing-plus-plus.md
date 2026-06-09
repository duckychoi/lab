---
title: Causal Forcing++ — 실시간 인터랙티브 영상 생성 (자기회귀 확산 증류)
type: source
domain: ai-news
tags: [ai-news, video-saas, diffusion, autoregressive, distillation, real-time, interactive-video]
created: 2026-05-16
updated: 2026-05-16
sources: []
reliability: high
---

# Causal Forcing++ (arXiv 2605.15141)

> [!insight] 핵심 인사이트
> 자기회귀 확산 증류를 소수 스텝으로 확장하여 **실시간 인터랙티브 영상 생성** 속도를 대폭 향상. "Causal Forcing" 기법은 영상 생성에서 시간적 인과성(causal structure)을 활용해 병렬 증류가 가능하게 한다. video-saas 도메인에서 인터랙티브 영상 생성의 실용화 임계점을 낮추는 핵심 기술.

**arXiv**: https://huggingface.co/papers/2605.15141
**업보트**: (신규, 2026-05-16)
**신뢰도**: ⭐⭐⭐

## 도메인별 추출 (video-saas + ai-news)

- **신뢰도**: ⭐⭐⭐ — HuggingFace 논문 페이지 등재, 동료 심사 전이나 HF 커뮤니티 관심 확인
- **즉시 활용**: 현재는 연구 단계. 코드 공개 여부 확인 필요
- **6개월 영향력**: **실시간 인터랙티브 영상 생성**이 게임·교육·가상 환경에 도입 가능한 수준으로 속도 개선되면 video-saas 전체 지형 변화. [[SANA-WM]](NVIDIA 선형 확산 트랜스포머, 분 단위 영상)과 상호 보완적 방향
- **대체 관계**: 기존 확산 모델의 느린 추론 한계를 증류로 극복 → [[Sulphur-2-base]](로컬 T2V) 대비 인터랙티브 실시간 세계 모델 방향
- **핵심 기술**: 자기회귀(AR) + 확산(Diffusion) 하이브리드 증류. Causal 구조가 시간 축 병렬화 가능하게 함
- **허와 실**: "실시간"의 정의(fps 수치) 미확인. 해상도·길이 제한 조건 확인 필요

> [!note] 배경 정보
> "Causal Forcing"은 자기회귀 모델 훈련에서 과거 토큰만 조건으로 사용하는 인과적 마스킹 원리를 확산 모델에 이식한 개념. 이를 "++"으로 확장하여 소수 스텝(2~4 스텝)에서도 고품질 영상 생성 가능하게 한 것.

> [!question] 미해결 질문
> 실제 추론 지연시간은? 30fps 실시간 생성 가능 해상도는? 논문 코드 공개 계획?

## 관련 페이지
- [[SANA-WM]] — NVIDIA 선형 확산 트랜스포머 효율적 세계 모델
- [[Sulphur-2-base]] — 오픈소스 텍스트→비디오 확산 모델
- [[AI-영상-생성-2026]] — 영상 AI 생태계 전체 지형도
- [[Matrix-Game-3.0]] — 장기 메모리 실시간 스트리밍 인터랙티브 월드 모델
- [[AnyFlow]] — NVIDIA 임의 스텝 영상 생성 flow map distillation

## 원본
- 출처: https://huggingface.co/papers/2605.15141
- arXiv: 2605.15141
- 신뢰도: ⭐⭐⭐ (HF 논문 페이지, 동료심사 전)
