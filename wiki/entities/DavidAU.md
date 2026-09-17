---
title: DavidAU
type: entity
domain: ai-news
tags: [entity, huggingface, quantization, gguf, uncensored, community, derivative]
created: 2026-09-17
updated: 2026-09-17
sources: [Qwen3.8-27B-TWIN-TURBO-709-GGUF.md, DavidAU-Qwen3.8-27B-TURBO.md]
reliability: low
---

# DavidAU

HuggingFace 커뮤니티 모델 제작자. 오픈 베이스 모델을 **다단계 파인튜닝·머지·탈검열·GGUF 양자화**해 재배포한다.

> [!insight] 🔍 볼트가 실측한 것 — 한 저자가 트렌딩 목록을 시리즈로 채운다
> **2026-09-17 HF 목록 API 상위 200 실측**: 이 저자의 `Qwen3.8-27B` 파생이 **최소 5건**(9위 ts350 · 33위 ts139 · 137위 ts34 · 138위 ts34 · 151위 ts32).
> 🎯 **명명 규칙이 시리즈다**: `Qwen3.8-27B-[TWIN-]TURBO-Fable-Cold-Fusion-NNN-...`. 번호(709·735-882)만 다르다.
> 🔴 **볼트는 이미 [[DavidAU-Qwen3.8-27B-TURBO]]**(`Cold-Fusion-735-882`)**를 보유한 상태에서 09-17에 `Cold-Fusion-709-L` 을 받았다.** `org/name` 리터럴 grep은 **0히트**였다 → [[파생저장소-식별]] 의 핵심 사례.
> 📌 저자 자기 진술(카드 186행): *"ELEVEN 모델 모두 700 arc-c 초과"* — **시리즈 규모를 본인이 밝힌다.**

> [!warning] 🔴 신뢰도 low 근거 — 자체 측정 계열 전체가 같은 미공개 방법론을 공유한다
> arc-c 수치(709/701/591)가 카드에 실재하나:
> - 🔴 **분모 미공개** (몇 문항인지 없음) · 🔴 **하네스 미공개** (어떤 평가 도구인지 없음)
> - 🔴 같은 저자의 다른 주장들(*"Qwen3.5 9B가 640 ARC-C"* 203·561행)이 **같은 방법론을 공유** → 계열 전체가 **반증 불가**
> 🔴 마케팅 문구: *"Closed source level of intelligence"* · *"The OpenAI, Claude and Gemini zone of intelligence"* — **제3자 검증 0.**

> [!insight] ✅ 그런데 카드는 정직한 축도 갖고 있다
> 🎯 **단계별 표 4개를 다 적고 우선순위까지 밝혔다**: *"Stage 2 was balanced based on **ultra low KLD first** (performance, quality) matched with low refusal rate second."*
> 그 결과 **KL↔거부 상충 축**이 4점으로 드러난다(KL 0.0025→거부 68/100 · KL 0.0535→거부 0/100).
> 🔴 **09-17 수집기 오류는 이 정직성을 못 읽은 데서 나왔다** — 첫 표(STAGE 1, 타인 작업)를 이 레포에 귀속시켜 **68점 오류**. → [[표-부분인용]] 2번 사례.
> 📌 **판정: 과장은 헤드라인에 있고 데이터는 본문에 정직하게 있다.** 둘을 함께 읽어야 한다.

## 관련 페이지
- [[Qwen3.8-27B-TWIN-TURBO-709-GGUF]] · [[DavidAU-Qwen3.8-27B-TURBO]] — 제작물(같은 시리즈 2건)
- [[파생저장소-식별]] — 🎯 저자 시리즈가 리터럴 필터를 통과하는 구조 · [[표-부분인용]] — 4개 표 중 1개 독해
- [[Alibaba]](Qwen3.8-27B 원류) · [[한정어-탈락]] · [[선택비용과-중복성]] · [[HuggingFace]] · [[ai-news]]
