---
title: Qwen3.6-35B-A3B-MTP-GGUF — MTP 자기투기 가속 로컬 멀티모달 MoE
type: source
domain: ai-news
tags: [ai-news, local-llm, qwen, moe, mtp, gguf, multimodal]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: high
---

# unsloth/Qwen3.6-35B-A3B-MTP-GGUF

> [!insight] 핵심 인사이트
> [[Qwen3.6-35B-A3B]]의 **MTP(Multi-Token Prediction) + GGUF** 배포판. DL **771,609**. 35B 총 / **3B 활성 MoE**(256 experts, routed 8 + shared 1), **Gated DeltaNet + Gated Attention 하이브리드** 40층, 네이티브 262K(YaRN 1.01M), 텍스트+이미지+비디오 멀티모달. MTP = 다중 토큰 동시 예측 **자기투기 디코딩**으로 "**정확도 손실 없이 ~1.5-2배 빠른 추론**". 1비트~16비트 GGUF로 로컬 배포. Apache 2.0.

**HF Model**: https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF  
**다운로드**: 771,609  
**신뢰도**: ⭐⭐⭐⭐ (모델카드 실측·DL 77만·Apache 2.0)

## 도메인별 추출

- **신뢰도**: ⭐⭐⭐⭐ — 모델카드 아키텍처·DL WebFetch 실측. unsloth 배포로 신뢰. 벤치는 원본 Qwen 수치
- **즉시 활용**: YES — 3B 활성 MoE라 **소비자 GPU에서 35B급 품질**. MTP로 로컬 추론 1.5-2배 가속 = [[LMCache]] prefix 캐시와 결합 시 TTFT+throughput 이중 최적화
- **6개월 영향력**: [[Linear-Attention-Architectures]]가 설명한 하이브리드 구조 + MTP 자기투기가 **로컬 추론 효율의 표준 조합**으로. [[ThinkingCap-Qwen3.6-27B-GGUF]](추론길이↓)·[[Qwen3.6-27B-NVFP4]](메모리↓)와 함께 "효율 3축(속도·길이·메모리)" 완성
- **대체 관계**: 동일 베이스의 [[Qwen3.6-35B-A3B-GGUF]]·[[Qwen3.6-35B-A3B-NVFP4]] 대비 **MTP 가속**이 차별 — 속도가 병목이면 이 배포판
- **Hermes 적용**: 로컬 멀티모달 백엔드 후보. 262K 컨텍스트 + MTP로 긴 문맥·빠른 응답 동시
- **액션**: 로컬 서빙에 MTP GGUF + LMCache 조합으로 TTFT/throughput 벤치 측정

> [!action] 당장 할 것
> Q4_K_M MTP GGUF를 로컬에 올리고 [[LMCache]] prefix 캐시와 결합해 TTFT·throughput을 비-MTP 대비 측정한다.

## 관련 페이지
- [[Qwen3.6-35B-A3B]]
- [[Alibaba]]
- [[Linear-Attention-Architectures]]
- [[LMCache]]
- [[ThinkingCap-Qwen3.6-27B-GGUF]]

## 원본
- 출처: https://huggingface.co/unsloth/Qwen3.6-35B-A3B-MTP-GGUF
- 신뢰도: ⭐⭐⭐⭐ (모델카드 실측·DL 77만)
