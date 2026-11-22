---
title: "latent MoE — expert 를 좁은 잠재 폭에서 돌려 expert 수를 수백 개로 늘리는 구조"
type: concept
domain: local-llm
tags: [local-llm, moe, architecture, sparsity, edge-inference]
created: 2026-11-22
updated: 2026-11-22
sources: [ZONOS3-Mini.md, Edge0-145B-NVFP4.md, Hy4-flash-GGUF.md]
reliability: medium
---

## 정의
> [!insight] 총량은 키우고 토큰당 연산은 묶는다
> 각 expert 를 모델 은닉 폭보다 좁은 잠재(latent) 폭에서 계산해 expert 하나의 비용을 줄이고, 그만큼 expert 수를 수백 개로 늘려 토큰당 소수만 라우팅하는 MoE 변형. 볼트 3개 소스가 카드에서 이 용어를 쓴다(구현 세부는 각 카드 서술 기준이며 볼트는 논문을 대조하지 않았다).

## 2026-11-22 신설 근거 (3소스)
- [[ZONOS3-Mini]] — TTS · 64 experts top-2 · 총 800M / 활성 약 100M.
- [[Edge0-145B-NVFP4]] — 48개 층의 routed expert 를 latent 폭 1792 로 교체 · 층당 512 experts 중 10개 · 145B / 10.12B.
- [[Hy4-flash-GGUF]] — 512 experts 중 16개 + 공유 1개 · 220B / 약 12B.

## 왜 중요한가
- 로컬 추론의 병목이 연산(활성)에서 **적재 · 스트리밍(총량)** 으로 옮겨 간다 → [[Tideway]] · [[Edge0-35B-A3B-preview]] 의 "메모리 계층을 바꾸는" 엔진들이 같이 나오는 이유.
- expert 가 수백 개면 표준 런타임 지원이 늦다 — [[Edge0-145B-NVFP4]] 는 전용 엔진, [[Hy4-flash-GGUF]] 는 미병합 PR 빌드가 필요했다.
- 크기 표기가 갈라진다 → [[파라미터-다중표기]].

## 관련 페이지
- [[파라미터-다중표기]] · [[Tideway]] · [[Edge0]] · [[local-llm]]
