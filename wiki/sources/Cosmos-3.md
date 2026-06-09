---
title: Cosmos 3 — NVIDIA 옴니모달 월드 모델 (291명 저자)
type: source
domain: ai-news
tags: [ai-news, hf-paper, nvidia, world-model, omni-modal, video-generation, robotics, T2I, I2V]
created: 2026-06-04
updated: 2026-06-06
sources: []
reliability: high
---

# Cosmos 3 — NVIDIA 언어·이미지·비디오·오디오·액션 단일 Mixture-of-Transformers

**논문**: https://huggingface.co/papers/2606.02800  
**GitHub**: https://github.com/NVIDIA/cosmos — ⭐9,500 (2026-06-06)  
**저자**: NVIDIA (291명 저자)  
**라이선스**: OpenMDW-1.1

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 언어·이미지·비디오·오디오·액션을 **단일 Mixture-of-Transformers(MoT)**로 처리·생성하는 NVIDIA 옴니모달 월드 모델. T2I·I2V SOTA, **RoboArena 1위 정책 모델**. 전체 코드·가중치·데이터 OpenMDW-1.1 라이선스로 공개. 291명 저자 — NVIDIA 연구 전 역량 총동원.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — NVIDIA 공식, 291인 저자, arXiv + HF 동시 공개
- **즉시 활용**: YES — 오픈소스 공개, 로봇 제어 정책·영상 생성·멀티모달 이해 직접 활용 가능
- **6개월 영향력**: 로봇 AI + 영상 생성 + 멀티모달 세 도메인에 동시 영향. RoboArena 1위는 로봇 제어 정책 분야의 즉각적 벤치마크 교체. T2I/I2V SOTA는 [[Seedance]], [[Higgsfield]] 영향
- **대체 관계**: Google Gemini Ultra 대비 오픈소스. GPT-4o 대비 비디오+로봇 특화
- **허와 실**: OpenMDW-1.1 라이선스의 상업적 활용 조건 확인 필요

> [!action] 당장 할 것
> RoboArena 1위 로봇 정책 모델 확인. T2I/I2V 성능이 기존 비디오 AI 워크플로에 미치는 영향 평가. OpenMDW-1.1 상업 조건 검토.

## 기술 요약

- **아키텍처**: Mixture-of-Transformers (MoT) — 모달리티별 전문가 라우팅
- **입출력**: 언어↔이미지↔비디오↔오디오↔액션 전 방향 가능
- **로봇**: RoboArena 1위 — 비전-액션 정책 최고 성능
- **라이선스**: OpenMDW-1.1 (오픈 라이선스이나 특정 제한 가능)

## 관련 페이지

- [[Humanoid-GPT]] — 휴머노이드 로봇 전신 제어 (로봇 AI 도메인)
- [[PF-OPSD]] — 월드 모델+LLM 결합 추론 (유사 접근)
- [[Seedance]] — 영상 AI SaaS (T2I/I2V 경쟁 도메인)
- [[NVIDIA]] — NVIDIA 모델 시리즈

## 원본

- 출처: https://huggingface.co/papers/2606.02800
- GitHub: https://github.com/NVIDIA/cosmos (⭐9,500, 2026-06-06)
- arXiv: 2606.02800
- 저자: NVIDIA, 291명
- 라이선스: OpenMDW-1.1
- 신뢰도: ⭐⭐⭐⭐⭐
