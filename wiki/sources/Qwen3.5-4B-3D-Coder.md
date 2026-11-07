---
title: "ccore/Qwen3.5-4B-3D-Coder — Three.js 씬 생성 개인 풀 파인튜닝. 평가는 개발 중 쓰던 프롬프트 8개, 데이터는 MiniMax 생성"
type: source
domain: local-llm
tags: [local-llm, hf-model, qwen3.5, fine-tune, threejs, 3d, code-generation, gguf, synthetic-data]
created: 2026-11-07
updated: 2026-11-07
sources: [https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder]
reliability: low
---

**HF**: [ccore/Qwen3.5-4B-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder) · 다운로드 **190,243(30일 = 누적)**(볼트 11-07 API · 수집기 11-06 157,157 → **+33,086/1일**) · ♥811 · trendingScore 412 · Apache-2.0 · base `Qwen/Qwen3.5-4B` · 4.54B · created 10-25 · sha `4b9f05f3`(lastModified 11-06T01:12Z) · GGUF Q4_K_M·Q8_0 · FP16 safetensors · 기술보고서 PDF

## 핵심 인사이트
> [!insight] 4B 모델 + 4,146예 합성 데이터로 "좁은 코드 장르" 하나를 판다
> 개인 개발자(CCORE)의 **비공식** 파인튜닝. 합성 데이터 **4,146예(학습 3,933 / 검증 213)**(볼트 카드 grep 확인), 데이터셋 `ccore/ThreeJS-3D-Scenes` 공개. 수집기의 보고서 PDF 판독에 따르면 프롬프트·사고 과정·완성 HTML/JS 를 **MiniMax M3.1 Flash 로 생성**했고, 풀 파인튜닝 약 59h10m + 16K LoRA 45m20s(RTX PRO 6000 Blackwell 1장, LoRA 단계는 L4), RL 없음. 원본 Qwen3.5-4B mmproj 를 붙이면 **참조 이미지 → Three.js 씬**도 된다고 한다. 즉 **"프런티어급 모델 출력을 증류해 소형 모델을 한 장르 전문가로"** 만드는 개인 규모 레시피.

> [!warning] 벤치 없음 — 보고서 스스로 "exploratory"
> 카드에 정량 벤치 0건(수집기 grep · 볼트 카드 재조회 동일 261행). 수집기 PDF 판독: **개발 중 쓰던 프롬프트 8개**로 체크포인트 비교, 케이스당 최대 5회 시도 · 최대 3곳 국소 수리 허용 → Checkpoint 8 이 8/8 수용(총 18회 호출). 보고서 문구 *"not a uniform first-attempt success benchmark"*. 볼트는 PDF 를 재열람하지 않았다(MiniMax·8/8 은 카드에 없음 = 수집기 단독 근거).
> - 학습 데이터가 **타사 모델(MiniMax) 출력** — 해당 약관상 경쟁 모델 학습 허용 여부 미확인.
> - LM Studio 에서 **MTP 를 꺼야** 정상 동작(카드 명시, 볼트 grep 2건).
> - 하루 +3.3만 다운로드의 원인은 미분석(개인 GGUF 치고 이례적) → [[계수기-배수]].

## 도메인별 추출 (local-llm)
- **실용성 판단**: 4B GGUF Q4_K_M — 노트북 GPU/CPU 로 실행 가능. 지연 수치 없음.
- **트레이드오프**: 장르 특화 vs 범용 코딩 능력 손실 여부 미측정.
- **Hermes 적용**: NO — 3D 씬 생성은 현재 에이전트 용도와 무관. 다만 **"특화 소형 모델 = 합성 데이터 4천 건 + GPU 1장 60시간"** 이라는 비용 기준점은 유용.
- **오픈소스 구현체**: 가중치·데이터셋 공개.

## 관련 페이지
- [[Qwen]] · [[MiniMax]] · [[AI-3D-생성]] · [[특화-역류]] · [[계수기-배수]]
- 같은 날 모델: [[LFM3-1.7B]] · [[DeepSeek-V4.1-Flash-1017-Uncensored-GSQ-RCO-GGUF]]

## 원본
- 출처: https://huggingface.co/ccore/Qwen3.5-4B-3D-Coder
- 확인 범위: HF API expand(볼트 11-07) · 카드 raw grep(4,146 · 3,933 · MTP 검출 / MiniMax · 8/8 미검출) · 보고서 PDF 는 수집기 판독만 · 추론 실행 0회
- 신뢰도: ⭐ (개인 비공식 · 벤치 없음 · 합성 데이터 출처 약관 미확인)
