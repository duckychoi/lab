---
title: "gliner2.5-multi-v1 — 287M 다국어 경계(boundary) 정보추출. 카드가 적은 가중치 크기가 실물과 다르고, 한국어는 인코더 사전학습까지만 확인된다"
type: source
domain: ai-news
tags: [ai-news, huggingface, information-extraction, ner, relation-extraction, multilingual, mdeberta, on-device, cpu-inference, fastino, 컨테이너]
created: 2026-09-19
updated: 2026-09-19
sources: [GLiNER2.md]
reliability: medium
---

# fastino/gliner2.5-multi-v1

> [!insight] 핵심 인사이트 — **"287M"의 2/3는 어휘 임베딩이다. 연산 체급은 86M 인코더다**
> 인코더 `microsoft/mdeberta-v3-base` 모델카드 원문: *"**86M backbone parameters** with a vocabulary containing 250K tokens which introduces **190M parameters in the Embedding layer**."* → 86M + 190M = 276M, 나머지 약 11M이 GLiNER2.5 boundary 헤드(추정: 287,355,159 − 276M).
> 🎯 **임베딩은 조회(lookup)라 연산이 거의 없다.** 따라서 추론 비용은 "287M 모델"이 아니라 **86M 트랜스포머 12층 + 헤드**에 가깝다(추정 — 볼트 실측 아님). 이게 *"CPU first"* 가 이 크기에서 성립하는 구조적 이유다.
> 📌 반대로 **디스크·메모리는 287M 전부**를 먹는다 — 그리고 그 크기가 카드 서술과 다르다(아래 정정).

> [!warning] 🔴 볼트 정정 — **카드의 "~594 MB (mostly FP16)"는 실물과 맞지 않는다. 실물은 FP32 1.15GB다**
> ```
> 모델카드 본문 (## Model details)      Weights: ~594 MB (mostly FP16)
> HF API safetensors 필드               {"F32": 287355159, "total": 287355159}
> HF tree API model.safetensors size    1,149,461,028 bytes (≈1.15 GB)
> 검산                                  1,149,461,028 / 287,355,159 ≈ 4.0 bytes/param → FP32
> ```
> 🎯 **파일이 FP32로 저장돼 있다.** 594MB는 FP16 기준 크기(287M×2B≈575MB)와 근사하므로, 카드가 **로드 후 `quantize=True`(GPU fp16) 상태 또는 이전 빌드**를 적은 것으로 보인다(추정). `encoder_config/config.json` 의 `"dtype": "float16"` 도 **설정 필드일 뿐 저장 텐서 dtype이 아니다.**
> 📌 **수집기는 카드 문장을 정확히 옮겼다** — 오류는 인용이 아니라 **카드가 실물을 틀리게 기술**한 데 있다. → [[파생표기-함정]] 의 계보(*"description은 소스가 아니다"*): 카드 산문은 저자의 서술이고, 실물은 safetensors 헤더다. **배포 전 메모리 예산은 1.15GB로 잡아야 한다.**

> [!note] 컨테이너 관계 — 이 페이지가 구성원이다
> 이 체크포인트는 레포 [[GLiNER2]] 가 담는 9종 중 하나다([[컨테이너-중복]] 규약). **이 모델 고유의 지표·한계는 여기에만** 적고, 아키텍처 2종·로더 제약·체크포인트 목록은 [[GLiNER2]] 에만 적는다. 이 페이지의 다운로드·♥는 **이 체크포인트의 것**이고 레포 ★1,977과 섞지 않는다.

## 도메인별 추출 (ai-news)

- **신뢰도**: 다운로드 **183,555**(API `downloads`, 30일) · 누적 **183,684**(`downloadsAllTime`) · ♥**207**(`likes`) · `trendingScore` **117** = HF 모델 트렌딩 **39위**(`/api/models?sort=trendingScore` 상위 100 중 순위, 2026-09-19) · 생성 2026-08-14 · 수정 2026-09-17 · Apache-2.0 · `library_name: gliner2`. 🔴 **벤치 수치 0개**(카드 653행). → **medium**: 실사용은 강하게 확인되나(누적의 99.9%가 최근 30일) 품질 근거가 없다.
- **즉시 활용**: **YES (영어) / 미검증 (한국어)** — `AutoExtractor.from_pretrained("fastino/gliner2.5-multi-v1")` 한 줄. 로컬 CPU/CUDA/MPS. 엔티티·분류·레코드·관계·스팬속성을 한 스키마로. 헤드는 config 원문상 `enable_records: true` · `enable_relations: true` · 분류 손실 가중 1.0 → **카드 서술 *"Heads enabled: classification, records, relations"* 와 config 일치**.
- **6개월 영향력**: "LLM 없이 구조화 추출"의 다국어 기본값 후보. 영어는 README 스스로 `gliner2.5-base-v1` 을 권한다 — **이 모델의 존재 이유는 비영어**이고, 그 비영어 성능 근거가 없다는 게 핵심 공백이다.
- **대체 관계**: 다국어 NER(예: XLM-R 계열 NER 파인튠) + 제로샷 분류기 + LLM JSON 추출을 한 모델로 대체 시도. PII 전용이면 같은 컨테이너의 span 파인튠이 따로 있다([[GLiNER2]] 참조).
- **허와 실**: 아래 두 섹션.
- **액션**: 한국어 실측(아래 action).

## 한국어 지원 여부 — 원문을 다시 찾았다

> [!warning] 🔴 **이 모델 자체의 지원 언어 목록은 어디에도 없다** (✅ 수집기 주장 일치 + 추적 확장)
> 카드·README·config 원문 전수 검색 결과:
> - 카드 메타데이터 `language: [multilingual, en]` · 본문 *"Language: Multilingual"* · *"across languages"* — **언어명 0개**
> - README: 언어명이 등장하는 곳은 **단어 분할기 절의 "Chinese" 하나**뿐(아래)
> - `korean`/`한국어` 문자열: 카드·README **0히트**
>
> **그래서 한 단계씩 거슬러 올라갔다(볼트 실측, 2026-09-19)**:
> ```
> gliner2.5-multi-v1 config  model_name: microsoft/mdeberta-v3-base
>   → mDeBERTa 카드 원문     "trained with CC100 multilingual data" / "2.5T CC100 data as XLM-R"
>   → HF statmt/cc100 카드   language 109개, 'ko' 포함 ✅
>   (mDeBERTa 카드 language 메타는 XNLI 평가 15개 언어만 나열 — ko 없음. 사전학습 언어 ≠ 평가 언어)
> ```
> 🎯 **확인된 것: 인코더는 한국어 텍스트로 사전학습됐다(CC100 경유).**
> 🔴 **확인 안 된 것: 추출 헤드가 한국어 예시로 학습됐는가.** GLiNER2.5 multi의 학습 데이터 구성은 카드·README에 **미공개**. 참고로 원 GLiNER2 논문(v1 span)의 학습 데이터는 *"news articles, Wikipedia, legal texts, PubMed abstracts, and ArXiv"* + GPT-4o 합성 254,334건이며 **언어 구성을 밝히지 않았고 평가는 전부 영어 벤치**(CrossNER·SST-2·SNIPS 등)다.
> → **판정: 한국어는 "인코더 사전학습 수준의 교차언어 전이에 기대는 상태" — 지원 여부 미확인.** 수집기의 *"mDeBERTa 사전학습 언어에 의존한다는 것만 추정(추정)"* 은 정확하며, 이번에 **CC100 ⊃ ko** 까지는 사실로 격상됐다.

> [!warning] 🔴 한국어 실무 함정 (추정 — 코드 미실행) — **기본 단어 분할기가 공백 기준이다**
> README 원문: *"GLiNER2 first splits text into **word tokens** … The default `"whitespace"` splitter is the one used to train public checkpoints."* 비공백 언어는 `"char"` 분할기를 쓰라고 하면서 예시는 *"such as Chinese"* 뿐.
> 한국어는 공백이 있으므로 `whitespace` 로 돌지만, **어절 = 체언+조사**다(`삼성전자가`). 스팬 경계가 단어 토큰 단위라면 **엔티티가 조사를 포함해 반환될 가능성**이 있다(추정). `char` 로 바꾸면 경계는 풀리지만 README 경고 그대로 *"Changing a pretrained model's word boundaries can affect quality unless the model was trained with the same splitter"*.
> 🎯 **한국어에서는 "조사 붙은 스팬 vs 학습 분포 이탈" 트레이드오프가 생길 수 있다** — 실측 전에는 둘 중 무엇이 나은지 모른다.

## 능력 제한 — 카드 본문 (✅ 수집기 대조 일치)

- 인코딩 윈도 `max_len=4096` (config 원문 일치). `extract(...)` 는 *"with `max_len` **truncates**"*.
- 긴 문서는 `extract_long(chunk_size=384, chunk_overlap=64)` — 카드 원문 제한 3개 전부:
  - *"A span is kept only if its start and end fall in the **same chunk**."*
  - *"A relation is kept only if both endpoints were extracted in the same chunk."*
  - *"Boundary models can represent arbitrarily long spans **inside one encoded window**; they do not stitch a mention whose endpoints never co-occur."*
- 🎯 **관계 추출은 청크 크기가 상한이다** — 384단어 청크에서 한 문단 건너의 주어–목적어 관계는 **조용히 사라진다**(에러 없음). 문서 전체 관계 그래프 용도라면 청크를 키우거나 `max_len` 안에서 한 번에 넣어야 한다.
- 🔴 **추가 관찰(추정)**: 인코더 config의 `max_position_embeddings: 512` · `position_buckets: 256`(DeBERTa 상대위치). mDeBERTa는 512 길이로 사전학습됐는데 boundary 헤드는 4096 윈도를 선언한다. 상대위치 인코딩이라 **동작은 하겠지만 512 초과 구간 품질은 어떤 문서에도 측정돼 있지 않다.** "4096 안이면 임의 길이 스팬"은 **표현 가능성**이지 **정확도 보장**이 아니다.

## 수집기 대조

- ✅ 일치: 다운로드 183,555 · ♥207 · 트렌딩 39위 · 생성 2026-08-14 · Apache-2.0 · mDeBERTa-v3-base · 287M · 헤드 전부 활성 · `max_len=4096` · 청크 384/64 · same-chunk 제한 2건 · 언어 메타 `multilingual`·`en` 뿐 · 카드 653행 · 벤치 수치 0 · arXiv:2507.18546 볼트 0히트(볼트 grep 재확인)
- 🔴 정정 1건: *"가중치 약 594MB·주로 FP16"* → **실물 model.safetensors 1,149,461,028 bytes · safetensors `F32` 287,355,159** (카드 서술 자체가 실물과 불일치. 수집기 인용은 정확)
- ⬆️ 격상 1건: 한국어 — "mDeBERTa 의존(추정)" → **"인코더 사전학습 CC100에 ko 포함(확인) / 헤드 학습 언어 미공개(미확인)"**

> [!action] 당장 할 것
> **한국어 10문장 실측 (우선순위 높음 — 이 모델 채택 여부를 가르는 유일한 미지수)**: 뉴스 문장에 `person`·`organization`·`location`·`product` 스키마로 `whitespace` vs `char` 분할기 각각 실행 → ① 조사 포함 여부 ② 누락률 ③ CPU 지연 기록. 메모리 예산은 **1.15GB(FP32)** 로 잡는다. 결과가 괜찮으면 ChinameBot 대화 로그 엔티티 추출(LLM 호출 대체)에 연결 검토.

> [!question] 미해결 질문
> - GLiNER2.5 multi의 **학습 데이터 언어 구성**은? (카드·README 미공개. Fastino에 문의하거나 `docs/gliner2_5_boundary_architecture.md` 확인 필요)
> - 카드의 *"~594 MB (mostly FP16)"* 는 이전 리비전의 실물이었나? HF 커밋 이력 미확인.
> - 512 초과 윈도에서 boundary 헤드 정확도는? 측정 없음.
> - 30일 다운로드 18만의 주체는? (CI·파이프라인 반복 다운로드 비중 미확인 — [[측정도구-먼저-반증]])

## 관련 페이지
- [[GLiNER2]] — 컨테이너 (아키텍처·로더·체크포인트 목록은 그쪽)
- [[컨테이너-중복]]
- [[MiniCPM]] — 같은 규약의 첫 사례
- [[파생표기-함정]] — 카드 서술 vs 실물 헤더
- [[메타데이터-부재-추론]] — 언어 메타 부재에서 인코더 계보로 추적
- [[측정도구-먼저-반증]]
- [[Microsoft]] — mDeBERTa-v3 원저
- [[Fastino]] *(신설 제안)*
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/fastino/gliner2.5-multi-v1 (README·config.json·encoder_config/config.json, 2026-09-19 조회)
- 측정: HF API `downloads` 183,555 · `downloadsAllTime` 183,684 · `likes` 207 · `trendingScore` 117 · `createdAt` 2026-08-14T14:28:43Z · `lastModified` 2026-09-17T01:28:37Z · `safetensors` {F32: 287,355,159} · tree `model.safetensors` 1,149,461,028 B (2026-09-19)
- 인코더 계보: https://huggingface.co/microsoft/mdeberta-v3-base (카드) · https://huggingface.co/datasets/statmt/cc100 (카드 language 109개, ko 포함)
- 신뢰도: ⭐⭐⭐ (DL 18만/30일 · 벤치 0 · 카드–실물 불일치 1건)
