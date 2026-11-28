---
title: "Ternary-Bonsai-2.5-27B-GGUF — 에이전트 특화 삼진 양자가 전작의 약점을 뒤집었다 (prism-ml · Qwen3.8-27B 파생)"
type: source
domain: ai-news
tags: [ai-news, model, quantization, ternary, gguf, agent, qwen3.8-27b, prism-ml, mtp]
created: 2026-11-28
updated: 2026-11-28
sources: [https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF]
reliability: medium
---

**모델**: https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF · **다운로드 382,546**(볼트 API 11-28 · 생성 2026-11-24라 30일 창 = 누적 — [[지표-창길이]]) · 트렌딩 4위 · ♥655 · **Apache-2.0** · 베이스 [[Qwen3.8-27B]](baseModels relation='quantized' — 볼트 API 확인) · [[Prism-ML]] · [[prism-ml]]

## 핵심 인사이트
> [!insight] 전작의 63%였던 에이전트 코딩이 FP16의 90%까지 올라왔다 — 특화 양자의 세대 점프
> 1.76bpw 삼진(ternary) 양자로 **5.93GB(≈FP16의 1/9)**. 전작 [[Ternary-Bonsai-2-27B]] 대비: **SWE-bench Verified 60.8→75.6 · Terminal-Bench 2.1 52.8→60.1 · DeepSWE 0→27.0** — 에이전트 특화 학습이 양자 손실을 상쇄하고 역전. 툴콜 5종 평균 **77.2 vs FP16 77.7**(유지), MTP 디코드 1.5~1.8배 · H200/B200 기준 ~300 tok/s.

> [!warning] 같은 모델 안에서 지표가 양분된다 — "에이전트용"이면 쓸 만, "범용"이면 손해([[복합지표-분해]])
> 지는 행: **일반 16벤치 82.1 vs 84.3 · 코딩 54.2 vs 55.5** — 이 비교 상대는 수집기 판독 기준 용량 1.7배인 GSQ-RCO IQ3_XXS 양자. 즉 1/9 크기로 에이전트 지표는 유지했지만, 범용 지표는 더 큰 양자에게도 진다. 수치는 전부 모델 카드 **자기보고**(전작과 동일 한계).

## 도메인별 추출 (ai-news)
- **즉시 활용**: 27B급 로컬 에이전트(툴콜 · SWE 작업)를 소비자 GPU에서 돌릴 때 1순위 후보 — 5.93GB + 툴콜 유지 + SWE 75.6.
- **세대 비교**: Bonsai 2(에이전트 코딩 FP16의 63%) → Bonsai 2.5(90%) — "특화 양자는 범용 대체 불가"를 확인하면서도 특화 영역 격차를 거의 닫은 사례.
- **시리즈 추적**: [[Ternary-Bonsai-2-27B]] 페이지에 후속 도착 기록 갱신(이번 배치 수행).
- **액션**: 없음(관찰 — 로컬 에이전트 구성 시 Bonsai 2.5 IQ3_XXS급 재검토).

## 관련 페이지
- [[Ternary-Bonsai-2-27B]] · [[Qwen3.8-27B]] · [[Prism-ML]] · [[prism-ml]] · [[지표-창길이]] · [[복합지표-분해]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/prism-ml/Ternary-Bonsai-2.5-27B-GGUF
- 확인 범위: HF API(볼트 11-28 — DL 382,546 · 생성일 · ♥ · Apache-2.0 · baseModels='quantized'→Qwen3.8-27B 일치) · 벤치 수치(툴콜 · SWE · 일반/코딩 지는 행 — 모델 카드 자기보고, 수집기 11-28 판독 인용) · 실행 0
- 신뢰도: ⭐⭐ (DL·메타 실측 · 벤치는 카드 자기보고 · 시리즈 전례상 검증된 발표자)
