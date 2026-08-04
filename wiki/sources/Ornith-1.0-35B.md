---
title: deepreinforce-ai/Ornith-1.0-35B-GGUF — 35B 모델 GGUF 양자화 로컬 배포본
type: source
domain: local-llm
tags: [ai-news, hf-model, gguf, quantization, 35b, local-llm, text-generation]
created: 2026-06-30
updated: 2026-07-16
sources: []
reliability: medium
---

# Ornith-1.0-35B (deepreinforce-ai/Ornith-1.0-35B-GGUF)

> [!note] 2026-07-16 갱신
> HF 다운로드 **1.79M (좋아요 899, 1일 전 업데이트)** ← 437k (07-06). 열흘 새 4배 급증으로 200만에 근접 — 35B-MoE GGUF가 로컬 대형 구동 수요의 실질 주력으로 자리. 최근 리포 업데이트가 재유입을 견인한 것으로 보임. [[Ornith-1.0-9B]] 대비도 격차가 좁혀지는 추세. 벤치·양자화 품질은 여전히 패밀리 자체 측정 기반(직접 검증 필요).

> [!note] 2026-07-06 갱신
> HF 다운로드 **437k** (2026-07-06, ← 285k 07-02 ← 157k 06-30; 나흘 새 +152k 지속 증가). 급락 없이 꾸준히 오르는 곡선 = *일시적 관심이 아니라 지속 채택* — 35B-MoE GGUF를 실제로 로컬에서 돌리는 수요가 굳어짐. [[Ornith-1.0-9B]](1.47M) 대비 낮지만 대형 모델치고 견조. 벤치·양자화 품질은 여전히 패밀리 자체 측정 기반(직접 검증 필요).

> [!insight] 핵심 인사이트
> HF 다운로드 **437k** (2026-07-06, ← 285k 07-02 ← 157k 06-30). **35B 규모 모델의 GGUF 양자화 배포본** — llama.cpp 계열에서 대형 모델을 로컬 구동하려는 수요로 다운로드 상위에 진입. 제작처 "deepreinforce-ai"라는 이름은 RL 기반 학습 지향을 시사. 흥미로운 우연 — 같은 날 인제스트된 [[Scaling-the-Horizon]] 논문이 "35B로 조 단위 파라미터급"을 주장하는데, 35B는 *고성능과 로컬 구동 가능성의 경계선* 크기라는 공통 맥락. [[Qwythos-9B]](9B)·[[gemma-4-12B-coder-GGUF]](12B)보다 큰, 로컬에서 굴릴 수 있는 상한급 모델.

## 도메인별 추출 (local-llm)

- **실용성 판단**: 35B GGUF는 양자화(Q4~Q5) 시 24~32GB VRAM 또는 통합 메모리에서 구동 가능 — 고사양 로컬 머신/Apple Silicon 상위 기종 대상. 일반 엣지엔 부담.
- **메모리 아키텍처**: GGUF 양자화로 메모리 풋프린트 축소. 양자화 레벨별 품질 저하 측정 필요.
- **Hermes 적용**: 12B 코더보다 추론력이 필요한 작업에 후보. 단 지연시간·메모리 비용이 9B/12B 대비 크게 증가.
- **트레이드오프**: 35B 품질 vs 9B/12B 대비 2~4배 메모리·느린 토큰 생성. 품질 이득이 비용을 정당화하는지 태스크별 검증.
- **오픈소스 구현체**: GGUF라 llama.cpp/Ollama/LM Studio에서 즉시 로드 가능.

> [!note] 정체 규명 (2026-07-01, [[Ornith-1.0-9B]] 모델카드로 확인)
> Ornith-1.0은 **에이전틱 코딩 특화 자기개선형 모델 패밀리**(9B/31B-Dense·35B/397B-MoE), **Gemma 4·Qwen 3.5 위 사후학습**, **MIT 라이선스**. 이 35B는 **35B-MoE**로 추정. RL로 해답+스캐폴드를 함께 최적화하는 자기개선 프레임워크가 "deepreinforce-ai" 네이밍의 실체. 9B조차 SWE-bench Verified 69.4를 찍어 35B-MoE는 그 이상일 가능성 — 단 이 GGUF 배포본의 정확한 멤버(35B-MoE 여부)와 양자화 품질은 재확인 필요.

> [!warning] 신뢰도 주의
> 벤치마크는 패밀리 모델카드 **자체 측정**. 다운로드 157k는 관심도 신호이지 품질 보증이 아님. GGUF 양자화 레벨별 품질 저하 + 이 배포본이 35B-MoE인지(활성 파라미터 규모) 직접 확인 필요.

## 관련 페이지
- [[Ornith-1.0-9B]]
- [[Qwythos-9B]]
- [[gemma-4-12B-coder-GGUF]]
- [[gemma-4-12B-agentic-GGUF]]
- [[Scaling-the-Horizon]]
- [[Dockerless]]
- [[GLM-5.2]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/deepreinforce-ai/Ornith-1.0-35B-GGUF
- HuggingFace 다운로드: 437k (2026-07-06) ← 285k (07-02) ← 157k (좋아요 492, 06-30) — 나흘 새 +152k 지속
- 베이스: Gemma 4 · Qwen 3.5 위 사후학습(에이전틱 코딩) · MIT · 패밀리 9B/31B-Dense·35B/397B-MoE
- 신뢰도: ⭐⭐ (패밀리 정체 규명됨 — GGUF 배포본 멤버·양자화 품질은 직접 검증 필요)
