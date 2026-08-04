---
title: Scaling Native Multimodal Pre-Training From Scratch (CUHK·Tencent)
type: source
domain: ai-news
tags: [ai-news, hf-paper, multimodal, scaling-laws, vision-language, pretraining, tencent]
created: 2026-07-27
updated: 2026-07-27
sources: []
reliability: medium
---

# Scaling Native Multimodal Pre-Training From Scratch (2607.22043)

**arXiv**: https://huggingface.co/papers/2607.22043
**저자/기관**: Haoyuan Wu·Bei Yu(홍콩중문대 CUHK) / Aoqi Wu·Hai Wang·Jiajia Wu·Jinxiang Ou([[Tencent]] LLM Dept) / HF ↑11

> [!insight] 핵심 인사이트
> 비전-언어 모델을 **처음부터(from scratch) 네이티브 멀티모달로 학습**할 때의 **컴퓨트-최적 자원 배분(스케일링 법칙)**을 규명. 핵심 발견: 언어 목표와 멀티모달 목표가 **서로 다른 스케일링 거동**을 보인다 — **언어 학습은 데이터 구성 변화에 대체로 둔감(invariant)**한 반면 **멀티모달 최적화는 데이터 비율에 매우 민감(highly sensitive)**. 최소 loss가 예측 가능한 멱법칙을 따르며, 텍스트 비중이 큰 혼합일수록 효율을 위해 더 큰 모델이 필요함을 보인다. 또한 네이티브 멀티모달 사전학습이 **텍스트 성능을 보존하면서 공간 추론을 개선**하고 **in-context learning**(특히 시각 접지가 도움되는 추상 공간 태스크)을 가능케 함을 실증 — 즉 "멀티모달을 나중에 붙이기"보다 **처음부터 함께 학습**의 근거를 데이터·컴퓨트 예산 지도로 제공. 이 위키가 추적해온 [[LTX-2]]·[[Qwen3.6-27B]] 등 멀티모달 모델들의 **학습 레시피 하부 이론**.

## 핵심 인사이트

> [!note] 발견 (초록 실검증)
> - **거동 분리**: 언어 목표 = 데이터 구성에 둔감 / 멀티모달 목표 = 데이터 비율에 민감
> - **컴퓨트-최적 법칙**: 최소 loss가 멱법칙, 텍스트-헤비 혼합일수록 더 큰 모델 필요
> - **텍스트 성능 보존**: 네이티브 멀티모달 사전학습이 텍스트 능력 훼손 없이 공간추론↑
> - **in-context learning**: 시각 접지가 추상 공간 태스크에 유리
> - **의의**: 컴퓨트 예산↔데이터 구성→최적 파라미터·토큰 배분 매핑 제공

> [!action] 멀티모달 모델 선택·이해의 배경 지식
> 직접 학습할 일은 없지만, "멀티모달은 데이터 비율에 민감·텍스트는 둔감"은 오픈 멀티모달 모델(내가 쓰는 이미지·비전 모델)의 강약을 읽는 렌즈. 데이터 믹스 공개 모델을 고를 때 참고.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF ↑11, CUHK·Tencent·초록 실검증. 미래형 2607.x ID·구체 스케일링 계수 미확보·재현 전 medium.
- **즉시 활용**: NO — 사전학습 스케일링 이론. 직접 적용 아님, 배경 지식.
- **6개월 영향력**: "네이티브 멀티모달 from scratch"의 컴퓨트-최적 레시피가 정립되면, 후발 오픈 멀티모달 모델의 데이터 믹스 설계가 이론 근거를 얻음. 비전 접지→추상 추론 향상은 에이전트 공간지능([[ReferTrack]]·[[Show-Dont-Tell-ProVisE]]) 계보와 연결.
- **대체 관계**: "LLM 먼저, 비전 어댑터 나중" 관행에 **처음부터 통합 학습** 근거 제시(부분 대체 논거).
- **허와 실**: 스케일링 법칙은 실험 범위 밖 외삽이 위험 — 초대형·초소형에선 깨질 수 있음.
- **액션**: 원문 공개 시 데이터 비율↔모델 크기 트레이드오프 표 확인 → 멀티모달 모델 선택 기준화.

## 관련 페이지
- [[Tencent]] — 공저 기관
- [[LTX-2]] — 멀티모달 생성모델(하부 이론 연결)
- [[Qwen3.6-27B]] — 멀티모달 오픈모델
- [[ReferTrack]] — 시각 접지→공간 추론 계보
- [[Show-Dont-Tell-ProVisE]] — 생성 픽셀 기반 공간인지
- [[Scaling-Native-Multimodal-Pretraining]]

## 원본
- 출처: https://huggingface.co/papers/2607.22043 (arXiv 2607.22043)
- 저자: Haoyuan Wu·Bei Yu(CUHK) / Aoqi Wu 외(Tencent LLM Dept) / HF ↑11
- 발견: 언어(둔감) vs 멀티모달(민감) 스케일링 분리, 컴퓨트-최적 배분 법칙
- 신뢰도: ⭐⭐⭐ (초록·저자·기관 실검증, 계수 미확보·미래형 ID·재현 전 medium)
