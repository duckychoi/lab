---
title: "autotrust/AutoTrust-Decider-Pro-Vision-27B-v1.1 (카드명 AutoTrust-JEV-27B v1.1) — Qwen3.8-27B 기반 선택지 확률 결정 모델"
type: source
domain: local-llm
tags: [local-llm, decision-model, system-one, routing, tool-selection, vllm, qwen3.8, text-classification]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/autotrust/AutoTrust-Decider-Pro-Vision-27B-v1.1]
reliability: medium
---

**모델**: [autotrust/AutoTrust-Decider-Pro-Vision-27B-v1.1](https://huggingface.co/autotrust/AutoTrust-Decider-Pro-Vision-27B-v1.1) · dl30 **147,541**(= 누적) · likes 1,551 · apache-2.0 · safetensors 27,356,728,560 파라미터 · pipeline `text-classification` · library vLLM · created/modified 2026-10-17 (HF API 볼트 실측 — 수집기와 일치). 수집기 `ai-news` → 볼트 재분류 `local-llm`.

> [!note] 이름이 셋이다
> 레포 `AutoTrust-Decider-Pro-Vision-27B-v1.1` · 카드 제목 `AutoTrust-JEV-27B v1.1` · 카드의 다운로드 명령은 `autotrust/AutoTrust-JEV-27B-v1.1`. 후자를 HF API 로 조회하면 **307 → 현재 레포명**(볼트 실측) — 레포가 개명됐고 카드는 구 이름을 쓴다. 볼트 파일명은 카드 제목을 따랐다 → [[정규명-우선-중복검사]].

## 핵심 인사이트
> [!insight] 생성하지 않고 고른다 — 그리고 같은 크기 기준 모델을 36행 중 35행에서 이긴다
> 질문과 함께 주어진 선택지마다 확률을 매기는 결정 모델([[System-One-모델]]). vLLM 엔드포인트만으로는 결정 API 가 아니고, `jev_vllm_engine.py` 가 프롬프트를 렌더링해 **선택지 코드로 제한된 토큰 1개**를 요청하고 로그확률을 선택지 확률로 바꾼다(카드 181행). 결정 readout head(`lm_head.safetensors` 2.54GB) 포함.
> Decision Index 0.3 공개 스위트: **Public index 67.31** · 37개 벤치 · 140,178 요청. 영역별 스킬 점수(우연 수준 = 0): 도구·자동화 **85.19** · 언어 이해 73.38 · 검색·분류 66.97 · 지식·추론 **55.16** · 예술·취향 51.08.
> 전체 결과 표(과제 점수 ×100 — 볼트가 카드 72–130행을 행 단위로 셌다, GSM8K 는 "비교 안 함"이라 제외한 36행):
> - vs **JEV-27B**(같은 크기 기준 모델): **35승 1패**(패: Amazon ESCI 52.11 < 54.56).
> - vs **Jev 1.14**(참조 모델): **26승 10패** — 패배는 BBH 86.05 < 93.19 · MMLU-Pro 73.65 < 82.13 · CLadder · MuSR · **GPQA Diamond 54.59 < 75.51** · HLE 16.57 < 19.36 · PhishNChips 72.00 < 83.75 · ESCI · cfcolor · Habermas. 지식·추론에 몰려 있다.
> - 가장 큰 격차: 가전 제어 시뮬레이터 **89.77** vs 52.27 / 45.45 · ACOS 56.39 vs 19.48 / 33.14.

> [!warning] 수집기 판독 3건 정정
> 1. **"베이스 모델 미명시(NOTICE.base 만 언급)"** → 볼트가 `NOTICE.base` 를 열었다: *"d3 (Decision 3.0) · Copyright 2026 vLLM Semantic Router Team · **Built on Qwen/Qwen3.8-27B (Apache-2.0)**"*. `decision_config.json` 에도 `"base_model": "Qwen/Qwen3.8-27B"` + 고정 revision. → [[Qwen3.8-27B]] 파생. [[메타데이터-부재-추론]](카드에 없다 ≠ 레포에 없다 — 100바이트짜리 파일에 있었다).
> 2. **"비전 입력 근거 없음"** → `config.json` 은 `Qwen3_5ForConditionalGeneration` · `image_token_id` · `"language_model_only": false`, 레포에 `preprocessor_config.json` · `video_preprocessor_config.json` 존재. 아키텍처는 멀티모달이다. 다만 카드는 "text decision model"이라 하고 평가도 전부 텍스트 — **비전 결정 성능은 측정되지 않았다**가 정확한 서술이다.
> 3. **두 표의 지표가 다르다** — 수집기가 나란히 적은 "BFCL 96.25 · CLINC150+OOS 97.06 · BANKING77 93.63 · API-Bank 87.36"은 **스킬 점수**(우연 보정), "MMLU-Pro 73.65 · GPQA 54.59 · HLE 16.57"은 **과제 점수**다. 같은 벤치의 과제 점수는 BFCL 97.23 · CLINC 97.08 · BANKING 93.71 · API-Bank 87.60, MMLU-Pro 의 스킬 점수는 70.36(카드 143행). 카드 스스로 *"Raw index(75.62) and skill index are different metrics and should not be interchanged"* 라고 적는다 → [[단위-불일치]].

> [!warning] 검증 상태
> *"self-reported pending maintainer verification"*. 참조 2열은 재실행이 아니라 공개된 랩 결과를 옮긴 것(같은 고정 코퍼스). 도구 선택 점수는 *"should not be interpreted as end-to-end autonomous-agent evaluations"*(141행). HLE 는 우연 수준에 가깝다고 카드가 명시(144행). 같은 주 [[SO-Arena]] 는 결정 모델의 정확도 1위가 신뢰성 7위라고 보고 — 이 카드에는 선택지 변경 안정성 · 답 부재 인식 지표가 없다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 27B · bf16 약 52GB(샤드 6개) — 대형 GPU 필요. 지연은 "토큰 1개"라 생성형 대비 짧을 것(수치 없음).
- **메모리 아키텍처**: 해당 없음. 다만 [[System-One-모델]]의 "후보 측 캐시" 유형.
- **Hermes 적용**: 보류 — 에이전트의 **도구 선택 · 의도 분류 · 라우팅 판정기**로는 맞는 형태(BFCL · CLINC · 가전 제어가 강점)이나 27B 는 판정기로 쓰기에 무겁다. 더 작은 JEV 계열이 나오면 재검토.
- **트레이드오프**: 도구·의도 결정 ↑ / 지식·추론 ↓(Jev 1.14 대비).
- **오픈소스 구현체**: 레포에 `serve_vllm.sh` · `jev_vllm_engine.py` · `jev_format.py` 포함. apache-2.0.

## 관련 페이지
- [[System-One-모델]] · [[Jeva]] · [[SearchJev]] · [[VideoJev]] · [[SO-Arena]] · [[Actor-Judge-Teacher]] · [[Qwen3.8-27B]] · [[Qwen]] · [[vllm]] · [[메타데이터-부재-추론]] · [[단위-불일치]] · [[정규명-우선-중복검사]]

## 원본
- 출처: https://huggingface.co/autotrust/AutoTrust-Decider-Pro-Vision-27B-v1.1
- 확인 범위: HF API 메타 · 파일 트리 · 카드 raw(10,664B) 14–202행 · `NOTICE.base` · `config.json` · `decision_config.json` 직접 판독 · 구 이름 307 확인 · 🔴 Decision Index 원자료 · 평가 키트 미열람 · 실행 미확인
- 신뢰도: ⭐⭐ (likes 1,551 · 자체 측정 · 검증 대기)
