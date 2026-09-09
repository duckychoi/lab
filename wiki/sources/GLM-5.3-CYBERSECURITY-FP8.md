---
title: "dealignai/GLM-5.3-CYBERSECURITY-FP8 — 거부 제거 변형 (도메인 한정 주장 검증)"
type: source
domain: ai-news
tags: [ai-news, hf-model, abliterated, refusal-removal, glm, safety, 카드자기모순]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# GLM-5.3-CYBERSECURITY-FP8

> [!warning] 카드의 **자기 규정**과 카드의 **자기 측정**이 서로 어긋난다 — 이 배치 최중요 발견
> raw는 카드의 포지셔닝 문장을 그대로 옮겼다: *"카드가 스스로 '**범용 uncensor가 아니다**'라고 명시하며 저작권 축자재현은 여전히 소프트 거부"*.
> 그 문장은 카드에 실제로 있다(`**This is a CYBERSECURITY-DOMAIN CRACK ... not a general-purpose uncensor.**`).
> **그러나 같은 카드의 벤치마크 표가 그 문장을 반박한다:**
> - *"**All other harm categories at 76–100%**(bio, chem, fraud, weapons, explosives, violence, misinfo, political-extremism, harassment) — **the refusal direction generalized broadly.**"*
> - *"Real harm-refusal on this crack is **80–84% direct comply**, 3–4 soft-refuses per surface, **~zero hard-refuses**."*
> - 실제로 남아 있는 거부는 **저작권뿐**(44개 행동, TRUE_COMPLY **16% / 11% / 20%**).
> → **"사이버보안 도메인 한정"은 의도이지 결과가 아니다.** 카드 스스로 이유도 적었다 — *"refusals share [a common direction]"*, 즉 **거부 방향이 도메인별로 분리돼 있지 않아** 하나를 지우면 광범위하게 지워진다.
> **볼트 판정: 이 모델은 사실상 범용 거부제거 모델로 분류해야 한다.** 유일한 예외가 저작권이라는 점은 아이러니하게도 *"학습 코퍼스에 없던 축은 안 지워졌다"* 는 증거일 뿐이다.

> [!insight] 일반화 가능한 교훈 — 거부는 도메인별로 국소화되지 않는다
> 이 카드는 **의도치 않게 정렬 연구 결과 하나를 실측 보고**했다: *한 도메인만 겨냥해 거부를 제거해도 **거부 방향이 공유돼 있어 전 도메인으로 일반화된다.***
> 볼트의 abliteration 클러스터([[heretic]] · [[Qwen3.8-27B-OBLITERATED]] · [[Huihui-Qwen3.8-27B-abliterated-GGUF]] · [[gemma-4-e4b-obliterated]] · [[Gemma-4-31B-JANG_4M-CRACK]])에 **"도메인 한정 크랙은 성립하지 않는다"** 는 반례 근거로 편입.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ (기술 정보로서) — 다운로드 **19,433**(09-09 3회 측정 전부 고정) · ♥334 · gated=False · MIT · 생성 2026-08-30 · base_model **JANGQ-AI/GLM-5.3-FP8**. 수치는 정확하나 **모델 자체의 안전성 주장은 자기 데이터로 반증됨**.
- **즉시 활용**: **NO — 채택하지 않는다.** 볼트는 기록만 한다.
- **6개월 영향력**: [[GLM-5.3]] 계열 파생 생태계가 커지는 흐름의 일부. 더 중요한 건 **"도메인 한정 abliteration"이라는 마케팅 범주가 성립하지 않는다**는 근거가 생겼다는 것.
- **대체 관계**: 없음(채택 대상 아님).
- **허와 실**: **허 = 도메인 한정 주장. 실 = 아래 운용 제약**(이 부분은 카드가 매우 정직하다).

> [!note] 운용 제약 — 이 카드에서 실제로 값진 부분 (8× DGX Spark GB10 필드 테스트, @0xMagnus)
> raw가 정확히 옮긴 항목들이며 볼트 재확인 완료:
> - **`reasoning_effort` 는 `"low"` 와 `"high"` 만 반영**된다. `off`·`medium`·`max`·미설정·YAML 비따옴표 `off:`(불리언 `false` 로 파싱) — **전부 `max` 로 흐른다.** 이 체크포인트에서 **추론을 끌 방법은 없다**; 최소는 `"low"`.
> - **FP8에서 에이전트/툴루프는 `low` 권장.** `high`/`max` 에서는 `<think>` 안에서 `max_tokens` 예산을 전부 태우고 **답변 0토큰(finish=`length`)** 이 나올 수 있다. 샘플링 파라미터로 구제되지 않는다 — **루프가 아니라 예산 소진**. 굳이 쓰려면 `max_tokens ≥ 8000`.
> - **1M 컨텍스트(decode-context-parallel)는 `glm_moe_dsa` 에서 막혀 있다** (DSA 인덱서 `k_cache` 가 DCP 랭크에 복제되는데 MLA KV는 샤딩 → `fp8_ds_mla` 에서 page size 오류). **실사용 상한: TP8 H200 기준 ~131K(MTP 사용) / ~160K(미사용).**
> - **MTP**: 스톡 vLLM에서 비작동. ciprianveg의 B12X sparse-MLA vLLM 포크 + `--draft-attention-backend B12X_MLA_SPARSE` 에서 작동 보고(**코딩 프롬프트 디코드 +48%**).
> - 131K 컨텍스트는 8× H200 · `max-num-seqs 24` 에서 동작(**약 2.98× 동시성 여유**).

> [!action] 당장 할 것
> 모델은 받지 않는다. **`reasoning_effort` 폴백 함정만 [[vllm]] 페이지에 이식한다** — *"설정하지 않은 값이 조용히 최대치로 흐르고, 그 결과 답변이 0토큰으로 끝난다"* 는 [[GLM-5.3]] 계열 전반에서 재현될 수 있는 운용 버그다.

## 관련 페이지
- [[GLM-5.3]]
- [[GLM-5.3-Flash]]
- [[Zhipu-AI]]
- [[heretic]]
- [[Qwen3.8-27B-OBLITERATED]]
- [[vllm]]

## 원본
- 출처: https://huggingface.co/dealignai/GLM-5.3-CYBERSECURITY-FP8
- 실측(2026-09-09): 다운로드 **19,433** · ♥334 · gated=False · MIT · created 2026-08-30
- raw 대비 드리프트: 다운로드 **완전 일치**(3회 측정 고정 재확인)
- 자매 모델: dealignai/GLM-5.3-UNCENSORED-FP8 (범용 버전이라고 카드가 안내)
- 신뢰도: ⭐⭐ (수치 high / 자기규정 주장 low)
