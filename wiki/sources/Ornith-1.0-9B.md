---
title: deepreinforce-ai/Ornith-1.0-9B — 자기개선형 오픈소스 에이전틱 코딩 모델
type: source
domain: local-llm
tags: [ai-news, hf-model, agentic-coding, self-improving, rl, 9b, local-llm, swe-bench]
created: 2026-07-01
updated: 2026-07-04
sources: []
reliability: medium
---

# Ornith-1.0-9B (deepreinforce-ai/Ornith-1.0-9B)

> [!insight] 핵심 인사이트
> HF 다운로드 **1.47M (2026-07-04 재확인, 07-01과 동일 수준 유지)** — HF 트렌딩 최상위권을 며칠째 지킴(급락 없이 안정 = 일회성 스파이크 아닌 지속 채택 신호). **에이전틱 코딩에 특화된 자기개선형(self-improving) 오픈소스 모델 패밀리 Ornith-1.0**의 최경량(9B-Dense) 멤버. 패밀리는 9B/31B-Dense + 35B/397B-MoE로 구성되고 **Gemma 4·Qwen 3.5 위에 사후학습**, **MIT 라이선스**. 핵심은 **자기개선 학습 프레임워크** — RL로 해답 롤아웃뿐 아니라 그 롤아웃을 이끄는 **스캐폴드(scaffold)까지 함께 생성·최적화**해 더 나은 탐색 궤적을 스스로 발견한다. 9B가 SWE-bench Verified **69.4**, Terminal-Bench 2.1(Terminus-2) **43.1**로 [[Qwen3.5-9B]](각 53.2 / 21.3)를 크게 앞서고 35B급과 맞먹는 구간이 있음 — **단일 GPU 배포 가능한 소형 모델의 에이전틱 코딩 상한을 끌어올린 사례**. 앞서 만든 [[Ornith-1.0-35B]] 페이지가 "베이스·벤치 미공개"로 남겨둔 공백을 이 모델카드가 메운다.

## 도메인별 추출 (local-llm / ai-news 교차)

- **실용성 판단**: 9B-Dense = **단일 GPU 로컬 배포 가능**. `<think>` 추론 블록 + tool_call을 내는 reasoning 모델이라 vLLM 등 최신 런타임 필요(reasoning/tool 파서 활성화). 로컬에서 굴릴 수 있는 코딩 에이전트 모델로 현실적.
- **메모리 아키텍처**: 해당 없음 — 코딩 에이전트 모델. 컨텍스트는 벤치에서 128K~400K까지 사용.
- **Hermes 적용**: 로컬 코딩 에이전트가 필요할 때 [[gemma-4-12B-coder-GGUF]] 대안. 9B로 SWE-bench 69.4는 로컬 코딩 보조로 실용 후보.
- **트레이드오프**: 9B 치고 벤치가 높으나 reasoning 모델이라 토큰 생성량↑(think 블록). 실제 지연시간·비용은 로컬 하드웨어에서 실측 필요.
- **오픈소스 구현체**: HF 공개 + MIT. GGUF판은 [[Ornith-1.0-35B]] 참조(같은 패밀리).

> [!insight] 벤치마크 (모델카드, 5회 평균)
> - SWE-bench Verified: **69.4** (Qwen3.5-9B 53.2 / Gemma4-12B 44.2)
> - SWE-bench Multilingual: 52.0 · SWE-bench Pro: 42.9
> - Terminal-Bench 2.1 (Terminus-2): **43.1** / (Claude Code) 40.6
> - NL2Repo: 27.2 · Claw-eval Avg: 63.1

> [!warning] 신뢰도 주의
> 벤치마크는 **모델카드 자체 측정**(harness·온도 명시는 됨). 데일리 다운로드 1.47M는 관심도 신호이지 품질 보증이 아님. "자기개선" 주장의 실효는 내 실사용 태스크에서 직접 검증 필요. 397B-MoE 등 상위 멤버 성능과 혼동 금지 — 이 페이지는 9B 한정.

> [!action] 당장 할 것
> 단일 GPU/Apple Silicon에서 9B 로드 → 실제 리포 수정 태스크 1건으로 [[gemma-4-12B-coder-GGUF]] 대비 정확도·속도 비교. 합격 시 로컬 코딩 보조 후보 편입.

## 관련 페이지
- [[Ornith-1.0-35B]]
- [[Qwen3.5-9B]]
- [[gemma-4-12B-coder-GGUF]]
- [[gemma-4-12B-agentic-GGUF]]
- [[Dockerless]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/deepreinforce-ai/Ornith-1.0-9B
- HuggingFace 다운로드: 1.47M (좋아요 316, 2026-07-01)
- 베이스: Gemma 4 · Qwen 3.5 위 사후학습 · 라이선스 MIT · 패밀리 9B/31B-Dense·35B/397B-MoE
- 신뢰도: ⭐⭐⭐ (공개 벤치·MIT·다운로드 최상위 — 벤치는 자체 측정, 자기개선 실효 미검증)
