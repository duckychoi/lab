---
title: ISTA-DASLab
type: entity
domain: local-llm
tags: [local-llm, quantization, gguf, research-lab, gsq, rco]
created: 2026-09-22
updated: 2026-10-10
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

---

## 🔄 2026-10-06 갱신 (인제스트 2026-10-10) — 벤더 중 가장 강한 자기제한 규율

> [!insight] 산출물 갱신 — [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]]
> 다운로드 **2,244,732**(전체 = 30일 동일) · likes 626 · trendingScore 237 · apache-2.0 · lastModified 2026-09-29
> **GSQ(arXiv 2604.18556) + RCO(arXiv 2605.00649)** 로 텐서마다 양자화 타입을 따로 배정해 4개 크기를 낸다.
> - **IQ3_S(3.50bpw · 83.6GB)**: 과제평균 **93.26 vs BF16 93.12**(354GB)
> - **IQ3_XXS(3.00bpw · 75.8GB)**: 과제평균 **92.57 = 99.4%** 를 **4.7배 작은 크기**로

> [!insight] 🏆🏆 이 조직이 볼트 [[자기제한-명시]] 의 벤더 최강 사례다
> ZS 평균이 BF16 대비 **100.3~101.4%** 로 나오는데 카드가 직접 적는다:
> > *"차이는 대략 1 표준오차 내이고 **개선이 아니라 동등으로 읽어야 한다**"*
>
> ⇒ 🏆 **[[숨김유인-부호]] 반례 중 가장 강한 형태다** — [[QuantCode]] 의 역행 수치는 **그 자체가 기여**였으나, 이쪽은 **자기 우위를 깎는 것이 기여가 아니다.** 유인에 순수하게 반한다.
> 🔗 10-10 [[Trace2Env]] 의 [[유의성-자기제한]] 과 **같은 통계 규율**이다 — 벤더와 논문 양쪽에서 동일 규율이 관측됐다.

> [!insight] 🆕 포맷이 독립 변수라는 분해를 제시한다
> `Q2_0` 가 `IQ2_XS` 보다 **작은데** 프롬프트 처리량 **3.4배**(367.49 vs 108.19 t/s)·지연 **1.9배 낮음**이고 원인은 **룩업테이블 디코딩 비용**이다. 디코드 안정성 폭도 **2.0 vs 45.1** 로 갈린다.
> ⇒ 🆕 **[[복합지표-분해]] 신규 유형: 동일 비트폭에서 "포맷"이 독립 변수다.**
> 🔴 **단 프리필 우위가 균일하지 않다** — RAG 9.6배·writing 6.8배·coding 6.2배인데 **stem·math·reasoning 은 0.8~0.9배 역전**(카드가 먼저 적는다) → [[배수-조건분산]]

> [!insight] 🎯 `mmproj` 분리 배포가 확인됐다
> **`mmproj` 가 BF16 0.91GB 로 분리 배포**된다 ⇒ 10-05 볼트의 [[Ternary-Bonsai-2-27B]] **비전 타워 미집계 추정**이 **다른 레포에서 구조적으로 확인됐다**(같은 llama.cpp 생태계가 비전을 별 파일로 뺀다).
> 🆕 **2샤드 구조**: 샤드2(28.8GB · `per_layer_token_embd` **51.2B** IQ4_NL)는 룩업이므로 디스크 상주 가능 ⇒ **"총 다운로드 66.4GB" ≠ "상주 필요 37.6GB"** → [[단위-불일치]] 6번째 유형.

> [!warning] ⚠️ 자기제한이 강한 카드에도 설명 없는 공백이 있다
> **IQ3_S 의 ZS 평균이 `n/a`** 이고 **카드가 이유를 적지 않는다** — [[구조적-영값]] 아님, **보고 누락**이다.

## 관련 페이지 (갱신 추가)
- [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] · [[자기제한-명시]] · [[숨김유인-부호]]
- [[유의성-자기제한]] · [[배수-조건분산]] · [[단위-불일치]]
- [[Ternary-Bonsai-2-27B]] · [[Trace2Env]] · [[QuantCode]]
