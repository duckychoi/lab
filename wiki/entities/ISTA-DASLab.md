---
title: ISTA-DASLab
type: entity
domain: local-llm
tags: [local-llm, quantization, gguf, research-lab, gsq, rco]
created: 2026-09-22
updated: 2026-09-22
sources: [Qwen3.8-Flash-Next-GSQ-RCO-GGUF.md, Qwen3.8-27B-GSQ-RCO-GGUF.md]
reliability: medium
---

# ISTA-DASLab

HF `ISTA-DASLab`. 이름으로 보아 오스트리아 IST Austria의 분산 알고리즘·시스템 연구실로 보이나 ⬜ **소속은 볼트가 직접 확인하지 않았다.** 양자화 연구 출하 조직.

> [!insight] 🎯 방법 — **텐서마다 다른 타입을 예산 안에서 배분**
> GSQ(Gumbel-Softmax 스칼라 양자화)로 텐서별 후보를 만들고 RCO(리만 제약최적화)로 352개 텐서에 타입을 배정한다. **할당표를 공개**한다(파일 18개).
> 볼트 보유 2건: [[Qwen3.8-27B-GSQ-RCO-GGUF]](high) → [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]](medium).

> [!warning] 🔴 같은 조직의 두 번째 카드가 첫 번째보다 약하다
> Flash-Next 카드는 *"Mirrors the Qwen3.8-27B card"* 라면서 **Unsloth 대조와 perplexity가 빠졌고**, 라이선스는 메타 `apache-2.0` ↔ 본문 "원본 상속"(원본 `qwen-community-1.0`) **모순된 채 복사**됐다. 🎯 **조직 단위로 신뢰도를 옮기지 않는다** — 카드마다 따로 판정.
> ✅ 반대로 볼트 미해결 2건을 풀어 준 조직이기도 하다: `-lm`/`--lazy-mode` 는 **stock llama.cpp 플래그**(포크 불필요), `Q2_0` 은 **업스트림 GGML 표준 타입**(Bonsai 깨짐은 타입이 아니라 가중치 회전 탓으로 추정, 실행 미검증).

## 관련 페이지
- [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] · [[Qwen3.8-27B-GSQ-RCO-GGUF]] · [[Qwen3.8-Flash-Next]]
- [[Ternary-Bonsai-2-27B]] · [[Prism-ML]] · [[파생저장소-식별]]
- [[local-llm]]
