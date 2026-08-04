---
title: Bonsai-27B-gguf — Qwen3.6-27B 삼진(ternary) 양자화 GGUF (1.71bit/w)
type: source
domain: ai-news
tags: [ai-news, hf-model, gguf, quantization, ternary, 27b, local-llm, edge, text-generation]
created: 2026-07-17
updated: 2026-07-26
sources: []
reliability: medium
---

# Bonsai-27B (prism-ml/Ternary-Bonsai-27B-gguf)

> [!update] 2026-07-26 갱신 — 63만 돌파 (WebFetch 실검증)
> `Ternary-Bonsai-27B-gguf` HF 다운로드 **631,970**(좋아요 **1,034**, base_model `Qwen/Qwen3.6-27B` WebFetch 실확인) ← 07-21 집계 432k(좋아요 873). 닷새 새 +20만·좋아요 +161·**좋아요 1,000 돌파**로 극단 양자화(삼진 1.71bit·~7.2GB) 실사용 관심이 오히려 가속. 태그에서 `ternary`·`2-bit`·`on-device`·`hybrid-attention` 재확인. 이번 배치 신규 [[Nanbeige4.2-3B]](3B 에이전틱)와 함께 "작게 만들기" 로컬 축 지속 — Bonsai는 대형 압축, Nanbeige는 소형 정밀. reliability medium 유지(벤치 자체 리포트·독립 재현 전).

> [!update] 2026-07-21 갱신 — 다운로드 성장
> `Ternary-Bonsai-27B-gguf` HF 다운로드 **432k**(좋아요 **873**) ← 07-18 집계 301,893(좋아요 695). 사흘 새 +13만·좋아요 +178로 실사용 관심 지속. 삼진 1.71bit(~7.2GB, FP16의 95%) 정체·벤치는 07-18에 규명된 대로(자체 리포트). 07-19 배치 이후에도 [[airllm]](레이어 스와핑)·[[ktransformers]](MoE CPU 오프로딩)와 함께 **로컬 대형 구동 4축(양자화/KV재사용/레이어스와핑/MoE오프로딩)** 의 "극단 양자화" 항으로 자리 유지. reliability medium 유지(독립 재현 전).

> [!update] 2026-07-18 갱신 — 정체 규명 (어제 "미확인" 해소)
> 07-17엔 "베이스·양자화·벤치 전부 미확인(reliability low)"이었으나, 07-18 자동수집으로 **정체가 밝혀짐**: **[[Qwen3.6-27B]]의 삼진(-1,0,+1) 양자화 GGUF**. 실질 **1.71 bit/weight(~7.2GB, FP16 대비 9.4배 축소)**로 **15개 thinking 벤치 평균 80.49 = FP16(원본)의 95% 유지**, IQ2_XXS(72.73)를 크게 상회. 즉 "이름·크기 마케팅" 의심(어제 경고)이 **오히려 근거 있는 극단 압축 모델**로 확인됨 — 삼진 양자화로 정확도 95%를 지키며 9.4배 줄인 것이 사실이면 중형 로컬의 유력 후보. 리포는 `Ternary-Bonsai-27B-gguf`(DL **301,893**·좋아요 695); 07-17에 집계된 `Bonsai-27B-gguf`(DL 1.05M)와 리포명·수치가 달라 **변종/재업로드 가능성** — 동일 프로젝트로 통합 기록하되 정확한 리포 대응은 모델카드 확인 필요. reliability low→**medium** 상향(벤치는 자체 리포트, 독립 재현 전).

> [!insight] 핵심 인사이트
> HF 다운로드 **1.05M (2026-07-17, 좋아요 359)**. 27B급 모델의 **GGUF 양자화 배포판**으로, 로컬/엣지(llama.cpp·Ollama·LM Studio)에서 소비자 하드웨어로 돌리는 것이 목적. 다운로드 100만+는 실사용 관심을 방증하지만 **벤치마크·베이스 모델 정체·학습 데이터가 자동수집 단계에서 미확인**. 이름 "Bonsai(분재)"는 "작게 다듬은 로컬 모델"이라는 포지셔닝 암시 — [[Ornith-1.0-35B]]·[[Qwythos-9B]]·[[MiniCPM5-1B]]로 이어지는 **GGUF 로컬 배포 생태계**의 27B 항으로, 9B([[Qwythos-9B]])와 35B([[Ornith-1.0-35B]]) 사이 중형 구간을 채운다.

> [!warning] 신뢰도 medium — 벤치 자체 리포트
> 베이스([[Qwen3.6-27B]])·양자화(삼진 1.71bit)는 규명됐으나 **평균 80.49·FP16 대비 95%는 배포자 자체 리포트**로 독립 재현 전. GGUF 다운로드는 여러 양자화 파일 합산이라 유니크 사용자와 다를 수 있고, 07-17(1.05M)↔07-18(301,893) 수치·리포명 불일치는 미해소 — 실측 로컬 벤치로 확인 필요.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ — 베이스·양자화 규명 + 벤치(자체 리포트) 확보. 독립 재현은 미완.
- **즉시 활용**: YES(후보) — 삼진 1.71bit로 ~7.2GB면 **8GB VRAM/CPU에서도 27B급 추론** 가능. IQ2_XXS 대비 정확도 우위라 극단 압축 로컬 후보로 유력.
- **6개월 영향력**: 삼진(ternary) 양자화가 "정확도 95% 유지하며 9.4배 축소"를 실증하면, [[Qwen3.6-27B-NVFP4]]·IQ2 계열 저비트 경쟁에 **1.71bit 프런티어**를 추가 — 중형 로컬의 하드웨어 문턱을 크게 낮춤.
- **대체 관계**: [[Qwythos-9B]](9B)·[[Ornith-1.0-35B]](35B) 사이 27B 항. 같은 [[Qwen3.6-27B]] 베이스의 [[Qwen3.6-27B-NVFP4]](4bit)보다 **더 공격적인 1.71bit** — 크기 우선이면 Bonsai, 정확도 여유는 NVFP4.
- **허와 실**: 어제의 "이름 마케팅" 의심이 **정당한 극단 압축**으로 반전. 단 80.49는 자체 벤치 — "FP16의 95%"를 액면가로 믿지 말고 실사용 태스크로 검증.
- **액션**: llama.cpp/Ollama로 `Ternary-Bonsai-27B-gguf` 받아 8GB급 하드웨어에서 thinking 태스크 실측 → IQ2_XXS·[[Qwen3.6-27B-NVFP4]]와 정확도·속도·VRAM 3자 비교.

## 관련 페이지
- [[Qwythos-9B]]
- [[Ornith-1.0-35B]]
- [[Qwen3.6-27B]]
- [[Qwen3.6-27B-NVFP4]]
- [[MiniCPM5-1B]]
- [[Nanbeige4.2-3B]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/prism-ml/Ternary-Bonsai-27B-gguf
- HuggingFace 다운로드: 631,970 (2026-07-26 WebFetch 실검증, 좋아요 1,034, base_model `Qwen/Qwen3.6-27B`) ← 432k(07-21) ← 301,893(07-18). cf. `Bonsai-27B-gguf` 1.05M(2026-07-17) 리포명·수치 불일치(변종/재업로드 추정)
- 스펙: Qwen3.6-27B 삼진(-1,0,+1) 양자화, 1.71bit/weight(~7.2GB, FP16 9.4배↓), 15 thinking 벤치 평균 80.49(FP16의 95%), IQ2_XXS(72.73) 상회 — 자체 리포트
- 신뢰도: ⭐⭐⭐ (베이스·양자화 규명, 벤치 자체 리포트·독립 재현 전)
