---
title: Edge0
type: entity
domain: local-llm
tags: [local-llm, edge-ai, moe, mlx, 조직]
created: 2026-09-13
updated: 2026-09-13
sources: [Edge0-35B-A3B-preview.md]
reliability: medium
identifiers: [Edge0, Edge0-AI]
---

# Edge0

**HF 조직**: `Edge0` · **GitHub**: `Edge0-AI/edge0`(프레임워크)

> [!insight] 노선 — **모델을 줄이지 않고 메모리 계층을 바꾼다**
> 엣지 추론 진영의 통상 경로는 **모델을 작게 만드는 것**(증류·소형 모델)이다. Edge0은 **35B급을 그대로 두고 메모리 위치를 바꾼다** — 4비트 전문가 가중치를 스토리지에 상주시키고 라우팅된 것만 스트리밍한다.
> 🎯 차별 부품은 **prerouter** — 다음 스텝에 필요한 전문가를 한 스텝 앞서 예측해 스트리밍 지연을 forward 계산에 겹친다. 오프로드의 고질병(전문가 로드 대기)을 **예측으로 숨기는** 접근.
> **같은 배치 [[MetroLLM-Bench]] 와 정확히 반대 방향이다** — 저쪽은 4B로 줄여 2.6GB를 만들고, 이쪽은 35B를 둔 채 3GiB에 욱여넣는다. **엣지로 가는 두 경로**가 같은 날 올라왔다.

> [!warning] 조직 실체 미확인 · `preview` 단계
> 조직 소개·소속·인물 정보가 공개되어 있지 않다. 배포물은 실재하고([[Edge0-35B-A3B-preview]] 34.66B safetensors 실측 · Apache-2.0) 다운로드 1,596·♥626·트렌딩 3위로 실사용 흔적도 있으나, **벤치는 전부 자체 측정**(*"All benchmarks were run by us"*)이고 릴리스는 `preview` 다.
> → **reliability medium.** [[IFM]](09-09, 조직 미확인 + 자체보고 + 예고만 → low)보다는 높다 — **가중치와 프레임워크가 실제로 공개되어 있기 때문**이다.

> [!warning] 플랫폼 종속
> MLX 백엔드 → **현재 Apple Silicon 전용**. 다른 백엔드는 예고 상태다. "엣지"를 표방하지만 **실측 환경은 Mac mini M4 Pro 24GB** 였다.

## 배포물
- [[Edge0-35B-A3B-preview]] — 35B MoE(활성 3B), int4 + Recover-LoRA + prerouter. 베이스 `Qwen/Qwen3.5-MoE-35B-A3B`([[Alibaba]])

## 관련 페이지
- [[Edge0-35B-A3B-preview]] · [[Alibaba]] · [[MetroLLM-Bench]]
- [[IFM]] · [[XHToken]] — 조직 실체 미확인 선례
- [[파생표기-함정]] · [[한정어-탈락]]
