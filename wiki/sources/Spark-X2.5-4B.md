---
title: "XHToken/Spark-X2.5-4B — 네이티브 1M 컨텍스트 4B 에이전트 모델"
type: source
domain: local-llm
tags: [local-llm, hf-model, slm, long-context, hybrid-attention, agent, on-device, ascend]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# Spark-X2.5-4B

> [!insight] 핵심 인사이트
> 4B에서 **네이티브 1M 컨텍스트**를 **full-attention 1층 + sliding-window 3층 하이브리드**로 달성. 200개 이상 언어. **HF 트렌딩 1위**(수집 시점).
> raw의 판정 — *"동급 SOTA는 전 축이 아니라 **에이전트 축 한정**으로 읽어야 한다"* — 은 **카드 표 실측으로 확인됐고, 볼트는 여기서 한 단계 더 좁힌다.**

> [!warning] 볼트 정정 — "에이전트 축 우위"도 **축 안에서 갈린다**
> raw는 에이전트 축을 통째로 우위로 적었지만, **같은 표에 패배가 섞여 있다**(vs Qwen3.5-9B):
> - **이기는 쪽 — 브라우징·장기 툴사용**: BrowseComp **40.9 vs 8.3**(4.9배) · τ³-bench **30.4 vs 9.3** · MCP-Atlas **54.6 vs 47.4** · Workspace Bench **31.2 vs 25.5** · VitaBench2.0 **25.2 vs 15.6**
> - **지는 쪽 — 단발 함수호출**: **BFCL-V4 65.1 vs 66.1** · **τ²-bench 75.1 vs 79.1**
> → 정확한 요약은 *"에이전트 축 우위"* 가 아니라 **"다단계·탐색형 에이전트 과제에서 우위, 단발 함수호출은 동급 이하"**.
> **그리고 raw가 통째로 빠뜨린 강점이 있다 — 수학**: AIME 2026 **90.7 vs 88.2** · HMMT Feb 2026 **81.2 vs 70.8** · IMO-AnswerBench **74.2 vs 69.8** — **9B를 전부 이긴다.**

## 도메인별 추출 (local-llm)

- **실용성 판단**: **YES — 이 배치에서 가장 실용적.** 4B에 Apache-2.0, **Ollama·LM Studio·llama.cpp·MLX·vLLM·SGLang** 전부 지원. 온디바이스 배포 즉시 가능.
- **메모리 아키텍처**: SWA 3 + full 1 하이브리드로 **KV 캐시 크기와 성능을 동시에 잡는 것**이 명시적 설계 목표. 장문맥 전용 학습 단계에 **수천억 토큰**, 시퀀스 길이 1M까지 확장.
- **Hermes 적용**: **직접 후보.** 카드가 **Codex · Claude Code · OpenClaw · Hermes** 하네스와 "깊이 통합"을 명시한다 — [[hermes-agent]] 에 그대로 꽂아 볼 수 있다.
- **트레이드오프**: **지식·장문맥추론은 확실히 열세** — GPQA **67.4 vs 77.2** · HLE **12.3 vs 14.3** · AA-LCR **56.3 vs 63.0** · SWE-Bench Verified **41.6 vs 53.1**. 즉 **"아는 것"을 물으면 지고 "찾아오는 것"을 시키면 이긴다.** 4B에 1M 컨텍스트를 넣은 설계와 정확히 부합한다.
- **오픈소스 구현체**: 가중치 공개(Apache-2.0), 1.7B 자매 모델 동시 공개, LLaMA-Factory 파인튜닝 지원.

> [!note] 학습 배경
> 약 **20조 토큰** 사전학습. **화웨이 Ascend 클러스터**에서 학습. 후처리는 도메인별 교사 정책을 만든 뒤 **MOPD**로 단일 배포 모델에 통합. 하드웨어 지원에 NVIDIA 외 **Huawei·Hygon·HOUMO.AI** 명시 — 중국 국산 가속기 생태계 대응 모델.

> [!warning] 벤치마크 표 읽기 주의
> 비교 수치 다수에 **별표(`*`)** 가 붙어 있다(Qwen3.5-9B의 BFCL-V4 66.1*, τ²-bench 79.1* 등). 카드에 별표 범례를 볼트가 확인하지 못했다 — **자체 재현치일 가능성**이 있으므로 타사 수치는 원 출처 대조 없이 인용하지 말 것.

> [!action] 당장 할 것
> **`ollama pull` 로 받아 BrowseComp류 과제 하나만 돌려 본다.** 검증 포인트는 벤치마크 재현이 아니라 **"1M 컨텍스트가 4B에서 실제로 쓸 만한가"** — 특히 한국어 장문에서. 200+ 언어 주장의 한국어 실측은 카드에 없다.

## 관련 페이지
- [[Qwen3.6-35B-A3B]]
- [[hermes-agent]]
- [[K2-Horizon-MoVA-36B-A4B]]
- [[에이전트축-분기]]
- [[Hierarchical-Sparse-Attention]]
- [[XHToken]]

## 원본
- 출처: https://huggingface.co/XHToken/Spark-X2.5-4B
- 실측(2026-09-09): 다운로드 **10,661**(3회 고정) · ♥**944** · gated=False · Apache-2.0 · created 2026-08-24
- raw 대비 드리프트: 다운로드 **완전 일치** / ♥ 942 → **944 (+2)**
- base_model: XHToken/Spark-X2.5-4B-Base
- 신뢰도: ⭐⭐⭐
