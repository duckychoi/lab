---
title: "mradermacher/gemma-4-31B-it-ARA-heretic-GGUF — Gemma 4 31B 거부 제거(ARA)판의 정적 GGUF"
type: source
domain: local-llm
tags: [local-llm, gguf, gemma, abliteration, heretic, uncensored]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF]
reliability: medium
---

**모델**: [mradermacher/gemma-4-31B-it-ARA-heretic-GGUF](https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF) · 다운로드 **149,532**(볼트 11-16 · 수집기 116,423) · 좋아요 304 · apache-2.0 · base `richardyoung/gemma-4-31B-it-ARA-heretic`(dl **551** · 좋아요 0) ← [[Gemma-4-31B]] · 생성 2026-11-07.

## 핵심 인사이트
> [!insight] 관심은 측정된 원본이 아니라 측정 안 된 양자화본에 몰린다
> 원본 다운로드 551 vs GGUF 14.9만 — **270배**. 그런데 거부율 · 능력 수치는 전부 원본(BF16) 기준이고, 실제로 받아 쓰는 GGUF 에서는 미측정이다. → [[원본-파생-역전]] · [[파생저장소-식별]].

## 도메인별 추출 (local-llm)
- **실용성 판단**: Q2_K 12.0GB ~ Q8_0 32.7GB · **Q4_K_M 18.8GB**(24GB GPU 1장 가능) · Q6_K 25.3GB · 비전 mmproj Q8_0/f16 포함 · imatrix 판은 별도 `-i1-GGUF`.
- **원본 카드 수치 (richardyoung README · 볼트 확인)**: [[heretic]] v2.0.0 **ARA**(Arbitrary-Rank Ablation, 21–56층). 개발셋 거부 **28/100 vs 원본 99/100**(37행), KL 0.084; 홀드아웃 WildGuard 유해 프롬프트 972개 거부율 **0.6% [0.3, 1.3] vs 89.3%**(591행); 능력 변화 **−2.18%p**(MMLU-Pro · GSM8K · IFEval · HumanEval · MBPP 평균, 592행).
- **트레이드오프**: 거부 −88.7%p 에 능력 −2.18%p. 단 모델당 최적화 1회 · 거부 판정은 자동 판정기 · "답변 의향"이지 답변 유해성 측정 아님(수집기 판독).
- **Hermes 적용**: 필요 없음. 거부 제거 모델은 볼트 용도에 쓰지 않는다.

> [!warning] 원본 카드 하단 벤치 표는 이 모델의 측정치가 아니다
> MMLU Pro 85.2% · LiveCodeBench v6 80.0% 등은 Google [[Gemma-4-31B]] 카드를 옮긴 것(수집기 판독) → [[표-부분인용]] 의 역방향(남의 표 차용). 출처 논문 "Is Abliteration Getting Harder?" arXiv 링크는 "추가 예정".

> [!note] 라이선스
> Apache-2.0 + OpenRAIL++ v1.0 용도 제한(충돌 시 베이스 우선). `LICENSE_OpenRAIL++.md` 지역 조항 0건(수집기). Gemma 4 라이선스 본문 미열람.

## 관련 페이지
- [[heretic]] · [[Gemma-4-31B]] · [[Gemma-4-31B-JANG_4M-CRACK]] · [[Huihui-Qwen3.8-27B-abliterated-GGUF]] · [[Qwen3.8-Flash-Next-GSQ-RCO-abliterated-GGUF]] · [[Google]] · [[원본-파생-역전]] · [[SteerDistill]](양자화 후 재측정의 필요)

## 원본
- 출처: https://huggingface.co/mradermacher/gemma-4-31B-it-ARA-heretic-GGUF · https://huggingface.co/richardyoung/gemma-4-31B-it-ARA-heretic
- 확인 범위: HF models API 2건 메타 · 원본 README 37 · 589–592행(볼트) · 🔴 GGUF 파일 크기 · 라이선스 파일 · 하단 표 출처는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐ (DL 15만 · 양자화본 미측정)
