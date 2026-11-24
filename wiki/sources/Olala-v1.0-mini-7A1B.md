---
title: "OVHaiLLM/Olala-v1.0-mini-7A1B — 유럽산 Mamba-3/어텐션 하이브리드 MoE(활성 1B) · 🔴 공식 llama.cpp/vLLM 미지원(자체 포크 필수)"
type: source
domain: local-llm
tags: [local-llm, hf-model, mamba, hybrid-architecture, moe, europe, runtime-fork-dependency]
created: 2026-11-24
updated: 2026-11-24
sources: [https://huggingface.co/OVHaiLLM/Olala-v1.0-mini-7A1B]
reliability: medium
---

**HF**: dl30 63,289(볼트 API 11-24 · 수집기 11-23 62,806) · 좋아요 304(수집기 278) · 생성 2026-10-30 · 카드상 출시 11-19 · 내부 ID `94836be2…`(수집기 `6ae472d5…` — 🔴 볼트 API 재확인값) · base_model `OVHaiLLM/Olala-v1.0-mini-7A1B-SFT` · safetensors 6,773,124,144 파라미터

## 핵심 인사이트
> [!insight] 36층 중 어텐션은 7층뿐 — KV캐시 비용을 구조적으로 잘라냈지만, 그 대가가 "포크 의존"이다
> OVHcloud 그룹(프랑스)의 총 6.8B · 토큰당 활성 약 1B 모델. 36층 = **Mamba-3 29층 + 어텐션 7층**(5층마다 1개, KV캐시는 7층만), 각 층 뒤 256 expert(6 활성) + 공유 expert 1. 컨텍스트 32K, 추론 강도 4단계, 다턴 도구 호출 · 검색을 RL 로 학습. JUPITER · Jean Zay · MeluXina 유럽 슈퍼컴퓨터에서 12.8T 토큰 학습(공개 데이터 + 자체 합성), 사전학습 언어에 한국어 포함. Apache-2.0.

> [!warning] 🔴 카드 명시 제약 — 실행 도구가 포크 의존
> **공식 llama.cpp · vLLM · Ollama · LM Studio · mlx-lm 으로는 아직 못 돌린다(자체 포크 필요)**, 일반 양자화 레시피는 **NaN 발생 → 공식 GGUF/MLX 만 사용**, **Mamba 상태는 float32 필수**. 맥 16GB MLX 5.4GB · llama.cpp 포크 GGUF 6–14GB. [[선언된-구현체-공백]] 의 역방향: 구현체는 있는데 표준 런타임이 따라오지 못했다.

> [!warning] 지는 행 — 같은 체급 경쟁 모델에 다수 열세
> **카드 표(전 모델을 자체 클러스터 · 동일 코드로 측정, 열 귀속 확인)**: 같은 A1B 급 Granite-4.0-H-Tiny · OLMoE 에는 대부분 크게 앞섬(AIME 2025 61.3 vs 4.7 · 0.0). 🔴 **지는 행**: 같은 체급 **Ling-3.0-tiny(7.9B-A1.3B) 에 GPQA-D 50.5 vs 68.7 · AIME25 61.3 vs 70.0 · BFCL v3 59.6 vs 68.3 · MGSM 68.7 vs 73.7**, 더 작은 **LFM3-1.7B(dense) 에도 IFBench 57.7 vs 70.0 · GPQA 50.5 vs 62.6 · AIME25 61.3 vs 79.3**, Qwen3.5-4B 에 GPQA 50.5 vs 75.8 · MGSM 68.7 vs 88.8. 이기는 쪽은 Qwen3.5-4B 대비 IFBench 57.7 vs 49.7 · HumanEval+ 88.3 vs 83.4 정도. 안전성 표: RL 후 공격 성공률 12.5% → 6.3%지만 **과잉 거부 7.0% → 10.7% · 추론 넘침 11.8% → 15.0% 로 악화**.

## 도메인별 추출 (local-llm)
- **[[파라미터-다중표기]] 표본 추가**: 7A1B = 총 7B · 활성 1B · safetensors 6.8B — "7B" 라고만 적으면 활성 1B 의 실사용 속도가 보이지 않는다.
- **실용성**: 효율 주장은 있으나 동급 대비 성능 우위가 약하고 **실행 도구가 포크 의존** — 지켜볼 대상. 공식 런타임 지원이 떨어지는 순간(병합)이 실사용 판단 시점.
- **동향 신호**: 유럽 주권 컴퓨팅(JUPITER · Jean Zay · MeluXina)에서 학습한 오픈 모델, 한국어를 사전학습 언어에 명시 — 소스 다변화가 성능보다 먼저 확장되는 단계.
- **액션**: 없음(관찰).

## 관련 페이지
- [[Mamba4]] · [[파라미터-다중표기]] · [[선언된-구현체-공백]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/OVHaiLLM/Olala-v1.0-mini-7A1B
- 확인 범위: HF models API(볼트 11-24) · 카드 표 · 제약 문구는 수집기 11-23 판독 · safetensors 파라미터 수 재확인 미실시 · 실행 0
- 신뢰도: ⭐⭐⭐
