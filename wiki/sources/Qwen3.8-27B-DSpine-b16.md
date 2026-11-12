---
title: "Qwen3.8-27B-DSpine-b16 — Qwen3.8-27B 용 5층 병렬 드래프트(추측 디코딩), DFlash2 대비 수락 길이 우위 (Tencent)"
type: source
domain: local-llm
tags: [local-llm, speculative-decoding, draft-model, sglang, tencent, qwen]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16]
reliability: medium
---

**모델**: [tencent/Qwen3.8-27B-DSpine-b16](https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16) · DL **3,241** · likes 205 · `text-generation` · Apache-2.0 · created 2026-11-07 (HF models API 볼트 실측) · 논문 [arXiv 2609.36173](https://arxiv.org/abs/2609.36173) *Draft in Parallel, Condition Through Depth: Adjacent Causal Injection for Speculative Decoding*(볼트 API 제목 확인)

## 핵심 인사이트
> [!insight] 병렬 드래프트의 약점(토큰을 독립적으로 골라 앞뒤가 안 맞음)을 "깊이 방향으로 선행 위치 정보를 넘겨" 푼다
> 5층 드래프트 · 블록 16 · 8,192 토큰 슬라이딩 윈도. 각 층이 예측된 선행 위치 특징을 인접 위치에 주입 → 수락 길이 증가. SGLang `--speculative-algorithm DSPINE`.
> 카드 표(볼트 행 대조, 43~49·83행 · SGLang 0.5.22 · BF16 · FA3 · 동시성 8):
> - 평균 수락 길이 T=0: GSM8K **7.20 vs 5.69** · MT-Bench **4.48 vs 4.11** (DFlash2) / T=1: GSM8K 6.31 vs 5.45 · MT-Bench **4.03 vs 3.89**
> - 에이전트 E2E 배속(AR 대비, low): SWE-bench Pro **2.95× vs 2.72×** · xhigh 3.19× vs 2.87×

> [!warning] 🔴 [[비매칭-비교]] — 블록 크기가 다르다
> 카드 33행: *"Draft blocks: DSpine 16; official DFlash2 8."* 수락 길이는 블록 크기의 상한을 받으므로 **16 vs 8 비교는 동일 조건이 아니다** — 우위의 일부는 블록 크기에서 올 수 있다(분해 불가). DSpine 쪽은 동적 검증 + ReplaySSM 을 켠 설정(수집기 판독). 에이전트 벤치는 부분집합당 대화 20개 재생 · WorkBuddy Bench 는 Tencent 자체 벤치 · **GPU 기종 카드에 없음**. 가장 작은 우위는 MT-Bench T=1(+0.14)과 SWE-bench Pro low(+0.23×) — **실사용(대화·코딩·온도>0)에 가까울수록 격차가 줄어든다.**

## 도메인별 추출 (local-llm)
- **실용성 판단**: 27B 를 SGLang 으로 서빙하는 환경이면 즉시 적용 가능(Apache-2.0). llama.cpp/Ollama 경로는 카드에 없음.
- **Hermes 적용**: 보류 — 로컬 스택이 SGLang 이 아니면 해당 없음.
- **트레이드오프**: 드래프트 5층 추가 메모리 vs 2.7~3.8× 처리량(카드). 출력은 원 모델과 동일(추측 디코딩 검증) — 정확도 표가 없는 이유.
- **오픈소스 구현체**: 가중치 Apache-2.0 · SGLang 통합.

## 관련 페이지
- [[Qwen3.8-27B]] · [[Tencent]] · [[Qwen]] · [[비매칭-비교]] · [[리서치-2026년-온디바이스-AI엣지-추론모델-경량화-최신-동향]]

## 원본
- 출처: https://huggingface.co/tencent/Qwen3.8-27B-DSpine-b16
- 확인 범위: HF models API · 카드 raw(140행 · 10,731B) 행 대조 · arXiv API 제목·초록 · 🔴 실행 미확인
- 신뢰도: ⭐⭐ (DL 3,241 · 자체 벤치 포함)
