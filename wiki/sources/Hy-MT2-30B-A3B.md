---
title: Hy-MT2-30B-A3B — Tencent 대형 번역 MoE 모델
type: source
domain: ai-news
tags: [ai-news, tencent, translation, moe, multilingual, local-llm]
created: 2026-05-26
updated: 2026-05-26
sources: []
reliability: medium
---

# Hy-MT2-30B-A3B — Tencent 30B MoE 번역 특화 모델

> [!insight] 핵심 인사이트
> Tencent의 30B MoE 구조 번역 모델. 전체 파라미터 30B이지만 실질 활성 파라미터 3B만 사용 → 효율적 추론 가능. 경량 버전 [[Hy-MT2-1.8B]]와 함께 라인업 구성.

## 핵심 인사이트

**아키텍처**: MoE (Mixture of Experts) 30B 총 파라미터, 활성 3B
- 30B 풀 모델 대비 추론 속도 대폭 향상
- 1.8B 대비 번역 품질·언어 커버리지 향상 예상

**[[Hy-MT2-1.8B]]와의 관계**: 경량(1.8B)·고성능(30B-A3B) 이원 구성
- 1.8B: 빠른 추론, 단순 번역, 엣지 배포
- 30B-A3B: 고품질 번역, 서버 배포, 복잡한 언어쌍

**Tencent 번역 전략**: Hunyuan 생태계에서 번역 특화 모델 라인업 강화 — HuggingFace 공개 배포로 오픈소스 번역 시장 공략

> [!note] 배경 정보
> Tencent의 번역 오픈소스: [[Hy-MT2-1.8B]] (HF 7,470 DL) + Hy-MT2-30B-A3B (HF 2,090 DL)
> NLLB, OPUS-MT 등 기존 오픈소스 번역 대안으로 포지셔닝

## 도메인별 추출 (ai-news)

- **신뢰도**: HuggingFace 모델 2,090 다운로드 — 초기 단계, 검증 미흡
- **즉시 활용**: 조건부 YES — 다국어 번역 파이프라인에서 NLLB/OPUS 대안으로 테스트 가능
- **6개월 영향력**: 중소 번역 수요에서 로컬 배포 옵션 추가. MoE 3B 활성이면 T4급 GPU에서도 실행 가능
- **대체 관계**: 기존 NLLB-200, OPUS-MT 대체 후보 (한국어 포함 다국어)
- **허와 실**: 다운로드 2,090은 아직 낮음 — 품질 벤치마크 공개 자료 확인 필요
- **액션**: 한국어↔영어↔중국어 번역 테스트 후 품질 비교

> [!action] 당장 할 것
> HF에서 Hy-MT2-30B-A3B GGUF 양자화 버전 확인 후 로컬 테스트

## 관련 페이지

- [[Hy-MT2-1.8B]]
- [[Lance]]
- [[Zhipu AI]]

## 원본

- 출처: https://huggingface.co/tencent/Hy-MT2-30B-A3B
- 신뢰도: ⭐⭐ (HF 공개 모델, 초기 단계)
