---
title: nvidia/Qwen3.6-35B-A3B-NVFP4
type: source
domain: ai-news
tags: [ai-news, local-llm, quantization, nvfp4, nvidia, moe]
created: 2026-07-05
updated: 2026-07-05
sources: [Qwen3.6-35B-A3B-NVFP4.md]
reliability: high
---

# nvidia/Qwen3.6-35B-A3B-NVFP4

Qwen3.6 35B(A3B, MoE)을 NVIDIA **NVFP4 4비트**로 양자화한 배포판. 유효 파라미터 ~19B로 경량 추론을 목표로 한다.

## 핵심 인사이트

> [!insight] 벤더 네이티브 양자화가 커뮤니티 표준(GGUF)에 계속 침투
> [[Qwen3.6-27B-NVFP4]](2026-07-04)에 이어 NVIDIA가 35B A3B까지 NVFP4로 직접 양자화 배포. GGUF/unsloth 커뮤니티 표준([[Qwen3.6-35B-A3B-GGUF]]) 대비 **NVIDIA 하드웨어에서 4비트 효율 극대화**가 강점이자 함정(하드웨어 종속). MoE(A3B=활성 3B급)라 이미 가벼운 모델을 4비트로 더 눌러 단일 GPU 로컬 추론을 겨냥. → local-llm 직결.

> [!warning] 하드웨어 종속 / 수치 미검증
> NVFP4는 NVIDIA 최신 GPU에서 이점이 크며 타 하드웨어 이식성은 제한적. HF 6.52M DL은 원본 [[Qwen3.6-35B-A3B]] 계열 합산일 수 있어 순수 NVFP4 채택량은 별도 확인 필요.

## 도메인별 추출 (ai-news)

- **신뢰도**: HF 6.52M DL(계열 합산 추정), NVIDIA 공식 배포 → 배포처는 high, 순 채택 수치는 medium.
- **즉시 활용**: 조건부 YES — 최신 NVIDIA GPU 로컬 추론 시 4비트로 VRAM 절감.
- **6개월 영향력**: 벤더 포맷(NVFP4) vs 커뮤니티(GGUF) 로컬 양자화 표준 경쟁 심화.
- **대체 관계**: [[Qwen3.6-35B-A3B-GGUF]](llama.cpp) 대비 NVIDIA 특화 대안.
- **허와 실**: "유효 19B급" 효율은 하드웨어 전제. 비 NVIDIA 환경엔 무의미.
- **액션**: 보유 GPU가 NVFP4 지원 시 GGUF와 지연·품질 대조 벤치.

## 관련 페이지
- [[Qwen3.6-27B-NVFP4]]
- [[Qwen3.6-35B-A3B]]
- [[Qwen3.6-35B-A3B-GGUF]]
- [[NVIDIA]]

## 원본
- 출처: https://huggingface.co/nvidia/Qwen3.6-35B-A3B-NVFP4
- 신뢰도: ⭐⭐⭐ (NVIDIA 공식 / HF 6.52M DL 계열 합산 / 하드웨어 종속)
