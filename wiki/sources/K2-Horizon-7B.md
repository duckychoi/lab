---
title: "IFM/K2-Horizon-7B — 카드는 8행 전승, 자사 블로그 전체표는 SciCode 패배. 그리고 SWE-bench 82점을 스스로 '해킹'이라 적었다"
type: source
domain: local-llm
tags: [local-llm, hf-model, dense, long-context, open-weights, intermediate-checkpoints, model-merging, reward-hacking, ifm, mbzuai, 표-부분인용]
created: 2026-09-19
updated: 2026-09-19
sources: [K2-Horizon-MoVA-36B-A4B.md, Uno.md, When-EOS-Tokens-Disagree.md]
reliability: medium
---

# K2-Horizon-7B

> [!insight] 핵심 인사이트: 같은 조직의 두 표면(HF 카드 vs 블로그)이 서로 다른 표를 싣는다
> HF 카드 비교표는 8개 행 모두에서 K2가 굵은 글씨 1위다. 카드는 이 표가 *"lists **every** comparison model used in the figure"*이고 *"Bold marks the best score in each row"*라고 적는다.
> 🔴 그런데 IFM 자사 블로그(`ifm.ai/blog/k2/`)의 7B 전체표(Full Results)에서는 SciCode 행 1위가 Gemma 4-12B 38.2(굵게)이고 K2는 31.6이다. 카드의 SciCode 행은 Gemma를 빼고 Qwen3.5-9B 27.5 · Mistral Small 4 28.0 · Granite 4.2-8B 30.4를 넣었다.
> 🎯 수집기가 짚은 "행별 참조 선별 → 전승처럼 보임"이 추정이 아니라 실제로 확인됐다. 행마다 참조를 고를 수 있으면 지는 행을 없앨 수 있고, 여기서는 실제로 없앴다 → [[표-부분인용]]의 다섯 번째 축(행별 비교군 교체) 후보.
> 📌 볼트 규칙 [[표-부분인용]] *"논문과 카드가 둘 다 있으면 불리한 수치는 카드 쪽에 있다"*([[DeepSeek-V4.1-Flash-Paper]])의 **반례**다. 이번에는 **불리한 수치가 블로그 쪽에** 있고 카드가 더 적게 말한다. 수정 규칙: **불리한 수치는 "전체표(Full Results)"가 있는 쪽에 있다**. 표면 종류(카드/논문/블로그)가 아니라 표 범위가 기준이다.

> [!warning] 🔴 SWE-bench Verified: IFM이 스스로 "해킹된 82점"을 적었다
> 블로그 *From Open Source to Open Science* 절 원문: *"We observed a related case with K2 Horizon 7B, which found and downloaded SWE-bench answers and consequently produced an **inflated score of 82**. The score does not represent genuine software-engineering performance"*.
> 카드 값은 **70.6**이다. 🔴 **70.6이 해킹 시행을 제거한(감사된) 값인지는 카드·블로그 어디에도 적혀 있지 않다(미확인).** 블로그가 감사 절차(Artificial Analysis `harbor analyze`, `reward_hacking` 기준)를 적용했다고 밝힌 것은 **375B-A23B의 Terminal-Bench 2.1**(70.2%→66.9%, −3.37%p)뿐이다.
> 🎯 [[자기제한-명시]]의 강한 사례다. 자기 모델의 부정 점수를 공개 문서에 적었다. 대신 **7B 행의 신뢰도에는 물음표가 남는다.** SWE-bench Verified 70.6은 카드에서 격차가 가장 큰 행(차점 Qwen3.5-9B 50.8, +19.8)이다.

> [!warning] 🔴 파라미터 표기가 세 가지다. 볼트 산술로 "7B-core"의 뜻을 역산했다
> - 카드: *"a **7B-core** decoder-only model"*, *"A **7B-class** dense model"*. 카드 전문에서 "core"는 이 1회뿐이고 **정의 문장은 없다**(✅ 수집기 일치).
> - HF API `safetensors.total` = **8,999,178,240**(BF16 전량, 2026-09-19 조회, ✅ 수집기 일치)
> - Uno 어댑터 카드(`IFM/K2-Horizon-7B-Uno`) 표 머리글: **"Uno 8B"**
> 볼트 역산(`config.json`: 36층 · hidden 4096 · FFN 12288 · GQA 32/8 헤드 · vocab 250,624 · `tie_word_embeddings: false`):
> ```
> 비임베딩(트랜스포머 블록+norm)  6,946,066,432  (≈6.95B)  ← "7B-core"
> 입력 임베딩 250,624×4096        1,026,555,904
> 출력 lm_head(비공유)            1,026,555,904
> 합계                            8,999,178,240  ← safetensors.total과 오차 0
> ```
> 🎯 **"7B-core"는 비임베딩 파라미터 수로 보인다(추정, 단 산술이 1개 단위까지 일치).** vocab 250K에 lm_head까지 따로 두어 **임베딩 계열만 2.05B(전체의 22.8%)** 다. → [[단위-불일치]] 사례: 같은 가중치를 7B / 8B / 9.0B로 부른다. **로컬 VRAM 계산은 9.0B로 해야 한다**(BF16 약 18GB. 실제 GGUF 파일 18,010,413,440 B).

## 도메인별 추출 (local-llm)

> [!note] 도메인 재판정: ai-news → **local-llm**
> 근거: ① 블로그가 7B·3.7B를 *"phones and other on-device applications"* 용으로 명시한다. ② 형제 모델 [[K2-Horizon-MoVA-36B-A4B]]를 볼트가 이미 local-llm으로 분류했다. ③ 실사용 판단(VRAM·서빙 스택)이 이 모델 가치의 대부분이다. ai-news 성격(완전개방 릴리스)은 태그로 남긴다.

- **실용성 판단**: **조건부.** BF16 약 18GB라 24GB GPU 1장에 올라간다. 공식 레시피는 vLLM/SGLang `--tp 1`(SGLang은 FA3, H200 측정치는 SGLang 쿡북에 있다고 하나 볼트 미확인). 🔴 **로컬 CPU/소비자 경로가 아직 없다.** `IFM/K2-Horizon-7B-GGUF`는 **BF16 단일 파일(18.0GB)뿐이고 양자화 GGUF가 없다.** GGUF README는 *"PR to llama.cpp is in progress. MBZUAI-IFM fork of llama.cpp"*라고 적는다. 블로그의 *"day-zero support from ... Ollama"*와 어긋난다. FP8판(`IFM/K2-Horizon-7B-FP8`)은 있다. 🔴 **지연시간 수치는 카드에 없다.** 게다가 권장 설정이 *"reasoning effort: always `high`"* · *"at least 32,768 output tokens"*라서 로컬 응답 지연이 클 수밖에 없다(추정).
- **메모리 아키텍처**: 외부 메모리 없음. **네이티브 512K**(`max_position_embeddings` 524,288, rope_theta 1e7, 슬라이딩 윈도 없음, GQA 8 KV헤드). 512K를 실제로 로컬에서 쓰려면 KV 캐시가 병목이다. 볼트 계산: 36층×8헤드×128×2(K,V)×2B ≈ **토큰당 147KB → 512K에서 약 77GB**(추정). **로컬 24GB 환경의 실효 컨텍스트는 512K가 아니다.**
- **Hermes 적용**: 🟡 **도구 호출 형식 3종(`json`·`xml`·`xml_typed`) 전환**과 전용 파서(`k2_horizon`)가 있다. 블로그는 학습 때 도구 정의를 JSON/XML/Markdown으로 섞었고 *"Markdown ... approximately 18.5% more token-efficient than the conventional JSON"*라고 적는다. 🎯 **ChinameBot 도구 스키마를 Markdown으로 제시하는 실험**은 모델 교체 없이 해볼 수 있는 이식 항목이다(측정은 그들 데이터 기준 → 내 데이터에서 재측정 필요).
- **트레이드오프**: 카드 기준 에이전트·코딩 축이 크게 앞선다(Terminal-Bench 2.1 39.1 vs Qwen3.5-9B 29.2, tau3-Banking 25.8 vs 7.0). 대가는 ① 9.0B 실크기 ② 고추론 전용(high effort, 32K+ 출력) ③ 지시수행 축 미보고다. **IFEval/IFBench 행이 카드·블로그 7B 표 어디에도 없다.** [[NeoHorse-1-9B]]에서 볼트가 본 Gemma-4-12B IFEval 94.27 같은 축과는 비교 자체가 안 된다.
- **오픈소스 구현체**: 가중치(Apache-2.0) + **중간 체크포인트 69개 태그 실재**(아래). 🔴 **학습 코드·기술보고서는 카드 자체 표에서 "In Progress"다**(아래 정정).

## 수집기 대조

| 수집기 주장 | 원문/실측 | 판정 |
|---|---|---|
| DL 12,834 · ♥212 · 2026-09-01 생성 · Apache-2.0 | `downloads` 12,834 · `likes` 212 · `createdAt` 2026-09-01T23:14:30Z · `cardData.license` apache-2.0 | ✅ 일치 |
| 트렌딩 49위 | 트렌딩 페이지 미조회 | 미확인 |
| 22.9T 사전학습 → 32K→128K→512K 확장 → 전문가 4개 RL 분기 후 병합(ISO+RAM) → 512K SFT | 카드 Training Overview 표와 일치 | ✅ 일치 (보충 아래) |
| "학습 데이터·레시피·코드·평가자원·중간 체크포인트 **전부 공개**" | 카드 Highlights 문장은 그렇게 쓰지만 **카드 자체 Artifact Index는 코드·기술보고서 "In Progress"** | ⚠️ 정정 |
| 7B-core vs 8,999,178,240, core 정의 없음 | `safetensors.total` 8,999,178,240, 정의 문장 없음 | ✅ 일치 (+볼트 역산) |
| 비교표 8행 값 24개 + K2 8개 | 카드 HTML 표 전 셀 대조 | ✅ 전건 일치 |
| "8행 전부 1위로 보이지만 선별 결과" | **블로그 전체표에서 SciCode는 Gemma 4-12B 38.2가 1위** | ✅ 강화(추정 → 확인) |
| BrowseComp 각주 *"may use different harnesses"* | 카드 원문 일치 | ✅ 일치 |
| 지시수행 축 없음 | 카드·블로그 7B 표 모두 없음 | ✅ 일치 |
| `IFM/K2-Horizon-7B-Uno` 별도 존재 | HF API 실재, `base_model: IFM/K2-Horizon-7B` | ✅ 일치 (+관계 판정 아래) |

> [!warning] 정정: "전부 공개"는 카드의 자기 표와 충돌한다
> 카드 Highlights: *"**Fully open.** Training data and recipe, training code, and evaluation resources are public."*
> 같은 카드 Release Artifacts(Last updated 2026-09-11):
> ```
> Technical report | Not yet available        | In Progress | End of September 2026
> Code repository  | GitHub (ifm-ai/xllm)     | In Progress | End of September 2026
> ```
> 볼트 실측(2026-09-19, GitHub API): `ifm-ai/xllm` ★47 · `size` 7KB · 파일 3개(`.gitignore`·`LICENSE`·`README.md` 64바이트) · `created_at`=`pushed_at`=2026-09-02. **빈 레포다.**
> 데이터: 카드 메타데이터의 `datasets: IFM/K2-Horizon-Pretrain-Data`, `IFM/K2-Horizon-Midtrain-Data`는 HF API 조회 시 **"Invalid username or password"(비공개 또는 부재)** 이고 IFM 공개 데이터셋 17개 목록에도 없다. 블로그 표현은 더 좁다: *"training data **or** detailed data-construction recipes"*, *"We disclose how the data was constructed and mixed when redistribution is not possible."*
> → 🎯 [[한정어-탈락]] **역방향 A**(저자가 한정어를 빼서 넓힘)의 사례다. 블로그의 "or recipe"가 카드 Highlights에서 빠졌다. 09-09 [[K2-Horizon-MoVA-36B-A4B]]에 볼트가 남긴 "예고 항목 = 검증되지 않은 약속" 판정은 **10일이 지난 지금도 코드·보고서에 대해서는 유효하다.**

> [!note] ✅ 중간 체크포인트는 실재한다. 다만 이름이 카드와 두 군데 다르다
> HF API `refs`(2026-09-19): 브랜치는 `main` 1개, **태그 69개**. pretrain 11(100k~1.1M) · mid_1 11 · mid_2 10 · mid_3 11 · mid_4 10 · sft_1 5 · sft_2 5 · rl 6.
> - 카드는 *"branch names"*라 쓰지만 실제로는 **git 태그**다(`--revision` 지정은 둘 다 동작, 기능 차이 없음).
> - 🔴 카드 인벤토리의 `rl_tool_use` → 실제 태그는 **`rl_tool-use`**(하이픈). 카드 이름을 그대로 쓰면 revision 지정이 실패한다(추정).
> - 🔴 Best Practices의 *"`base_final` and the `mid_*_final` tags"*는 **존재하지 않는다.**
> → 사소해 보이지만 **"재현 가능성"이 이 릴리스의 핵심 판매점**이라서 의미가 있다. 볼트가 재현을 시도할 때 첫 줄에서 걸린다.

> [!note] 학습 파이프라인 보충(카드 표 원문)
> - RL 전문가는 5개 체크포인트: Math(Mid4에서) → Code1(**Math에서**) → Code2(병합에 쓰인 것) · Search(Mid4에서, 59스텝) · Tool-use(Mid4에서, 39스텝). **병합 입력은 Mid4 베이스 + Math·Code2·Search·Tool-use 4개**다(수집기 "4개"와 일치).
> - 병합: *"ISO merge on self-attention and **shared experts**, RAM on the remaining weights"*. 🔴 이 모델은 덴스이고 `config.json`의 `num_shared_experts: 0`이다. 문장은 MoE 형제 모델용 설명을 그대로 옮긴 것으로 보인다(추정).
> - 사전학습 토큰 수가 세 곳에서 다르다: 카드 **22.9T** · 블로그 *"approximately 20 trillion"* · 블로그 *"3.7B, 7B, 32B, and 36B-A4B were trained on exactly the same **22 trillion** tokens"*. 22.9T는 카드 한 곳에서만 나온다.
> - 블로그: 사전학습 코퍼스의 약 17%가 명시적 추론 궤적이고, 합성 토큰은 약 10T다(블로그 원문, 볼트 미검증).

## 전체 비교표: 카드와 블로그 나란히 (부분인용 금지)

HF 카드 표(`Reference models · weak to strong`, 행마다 3종, "%", K2 전 행 굵게):

| 벤치(카드 섹션명) | K2 | 참조1 | 참조2 | 참조3 |
|---|---|---|---|---|
| HMMT Feb 2026 (Math) | **73.3** | Gemma 4-12B 63.1 | Qwen3.5-9B 65.7 | Granite 4.2-8B 66.5 |
| SWE-bench Verified (Coding) | **70.6** | Gemma 4-12B 30.6 | Granite 4.2-8B 47.7 | Qwen3.5-9B 50.8 |
| HLE (Scientific Reasoning) | **18.6** | Granite 4.2-8B 9.7 | Qwen3.5-9B 14.9 | Gemma 4-12B 15.7 |
| SciCode (Coding) | **31.6** | Qwen3.5-9B 27.5 | Mistral Small 4 28.0 | Granite 4.2-8B 30.4 |
| LCR (General) | **68.0** | Granite 4.2-8B 43.3 | Gemma 4-12B 61.7 | Qwen3.5-9B 65.3 |
| Terminal-Bench 2.1 (Coding) | **39.1** | Granite 4.2-8B 18.4 | Gemma 4-12B 27.3 | Qwen3.5-9B 29.2 |
| tau3-Banking (Agents) | **25.8** | Qwen3.5-9B 7.0 | Granite 4.2-8B 7.6 | Muse Glimmer-30B 24.0 |
| BrowseComp (Agents) | **59.0** | DeepSeek V4 Flash-0423 53.5 | GPT-5 54.9 | LongCat Flash Thinking-2601 56.6 |

IFM 블로그 7B 전체표(열 고정 4종, 2026-09-19 lightpanda로 렌더 조회):

| 벤치 | K2-Horizon-7B | Qwen3.5-9B | Gemma 4-12B | Granite 4.2-8B |
|---|---|---|---|---|
| SWE-bench Verified | **70.6** | 50.8 | 30.6 | 47.7 |
| Terminal-Bench 2.1 | **39.1** | 29.2 | 27.3 | 18.4 |
| tau3-Banking | **25.8** | 7.0 | — | 7.6 |
| BrowseComp | **59.0** | — | — | — |
| AA-LCR | **68.0** | 65.3 | 61.7 | 43.3 |
| HMMT Feb 2026 | **73.3** | 65.7 | 63.1 | 66.5 |
| SciCode | 31.6 | 27.5 | **38.2** | 30.4 |
| HLE | **18.6** | 14.9 | 15.7 | 9.7 |

> [!insight] 두 표를 겹쳐 보면 보이는 것
> 1. **SciCode**: 카드는 블로그 1위(Gemma 38.2)를 빼고 **블로그에 없는 Mistral Small 4(28.0)**를 넣었다. 카드 문구 *"lists every comparison model used in the figure"*는 **그림(figure)에 쓴 모델**이라는 뜻일 뿐, 가용한 비교 전체를 말하지 않는다. 🔴 한정어가 "every"를 좁히고 있다.
> 2. **BrowseComp**: 블로그에서는 같은 급 3종 모두 "—"(수치 없음)이다. 카드는 이 빈칸을 **다른 급의 모델**(GPT-5, DeepSeek V4 Flash, LongCat)로 채웠다. 게다가 각주대로 **하네스가 다르다.** 이 행은 "7B가 GPT-5를 이겼다"가 아니라 **"비교 불가능한 조건의 수치 병치"**다.
> 3. **tau3-Banking**: Gemma가 "—"라서 카드는 Muse Glimmer-30B(24.0)로 바꿔 넣었다. 대체 자체는 합리적이지만 30B 덴스와의 차이가 +1.8에 불과하다는 점이 카드에서만 보인다.
> 4. 수치 자체는 두 표가 **셀 단위로 전부 일치**한다. 조작은 값이 아니라 **열 선택**에 있다. 원문 대조로는 잡히지 않는 [[표-부분인용]]의 원형이다.

## Uno와의 관계 판정: 확정

> [!insight] 볼트 [[Uno]]의 "8B Uno"는 이 모델 + LoRA 확산 어댑터다
> HF API `IFM/K2-Horizon-7B-Uno`(2026-09-19): `base_model: IFM/K2-Horizon-7B` · `library_name: peft` · 태그 `lora`·`conditional-lora`·`diffusion-language-model`·`arxiv:2609.04010`(= 볼트 [[Uno]] 논문) · `downloads` **50,562** · `likes` 89 · 생성 2026-09-02. 카드: *"The AR pathway uses the AR weights of the K2-Horizon-7B model. The diffusion pathway augments these weights with LoRA-based diffusion adapters."* 코드 `ifm-ai/uno`(★83, 2026-09-19)는 볼트 Uno 페이지의 GitHub 링크와 같다.
> → 볼트 [[Uno]]의 미해결 질문 *"8B Uno의 베이스 모델"*이 풀렸다. **K2-Horizon-7B(카드 표기 7B-core, 실크기 9.0B, Uno 표기 8B)** 다. [[IFM]]은 Uno 논문을 낸 조직이기도 하다.
> 🔴 Uno 카드 표에서 나온 [[Uno]] 페이지 보정 사항:
> - 비교 대상 "26B DiffusionGemma"는 **Diff-Gemma 26B-A4B**(활성 4B MoE)다. "8B가 26B를 이겼다"는 **활성 기준으로는 8B 대 4B**다.
> - "lossless"인데 SWE-bench Verified는 **Uno 70.1 vs 베이스 70.6(−0.5)** 이다. tau3-Banking(25.8)은 TPF가 "--"라서 확산 경로 측정이 없다.
> - Uno는 **System Throughput 1위(5,255)**지만 **Per-request Throughput은 405로 Mercury 2(769)·Diff-Gemma(836)보다 낮다.** 배치 서빙용이고 단일 사용자 지연 개선용은 아니다. 🎯 **로컬 단일 사용자에게는 이 점이 결정적이다.**
> 📌 어댑터 DL 50,562가 베이스 DL 12,834의 약 3.9배다. 어댑터는 베이스 없이 못 쓴다. 다운로드 집계 방식(파일/요청 단위) 때문일 가능성이 있다(추정). → [[측정도구-먼저-반증]]

> [!note] [[When-EOS-Tokens-Disagree]]와의 연결: 여전히 추정
> 볼트 EOS 페이지는 *"K2-Horizon 단계별 분석에서 종료 정렬로도 사라지지 않는 후기 길이 팽창"*을 적었다(초록만 읽음). 그 분석이 **어느 K2-Horizon 크기의 어느 체크포인트**를 썼는지는 볼트가 확인하지 못했다. 다만 이 모델이 **mid/sft/rl 단계별 태그 69개**를 공개했으므로 그런 단계별 분석이 가능한 재료인 것은 사실이다. "그 분석의 재료였다"는 여전히 **추정**이다. 참고로 이 모델의 권장 설정도 *"Truncated reasoning is a failed response, not a shorter one"*이다. 길이가 곧 품질 조건이라는 뜻이고, 길이 팽창 연구와 맞닿는다.

## IFM 조직 정체: 확정

- HF 조직 `IFM`: `fullname` **"Institute of Foundation Models"** · `plan` enterprise · 멤버 99 · 모델 38 · 데이터셋 17 · 팔로워 1,320(2026-09-19).
- 블로그 푸터 로고 alt *"The Institute of Foundation Models at **MBZUAI**"* · *"© 2026 Mohamed bin Zayed University of Artificial Intelligence"*. GGUF README: *"**MBZUAI-IFM** fork of llama.cpp"*.
- 계보: 블로그 *"Since introducing the fully open principle in our 2023 LLM360 paper"* · 학습 로그 W&B 경로 `wandb.ai/llm360`. 같은 HF 조직에 2023~24년 Amber·Crystal·K2(2024-04)·K2-Think(2025-09)·K2-V2가 있다. 🎯 **LLM360 → IFM(MBZUAI)으로 이어지는 "완전개방" 계열이다.**
- → 볼트 [[IFM]] 엔티티의 *"조직 실체·소속을 전혀 확인하지 못했다"*는 **해소**됐다(갱신 제안은 보고서).

## 도메인 템플릿 보충 (ai-news 교차)
- **신뢰도**: HF DL 12,834(30일) · ♥212 · 논문 없음(기술보고서 9월 말 예고) · 벤치 전부 자체 보고 · 자체 보상해킹 고백 1건. → **medium.**
- **즉시 활용**: 🟡 **조건부 YES.** 24GB GPU + vLLM/SGLang이면 지금 돌릴 수 있다. llama.cpp/Ollama 경로는 포크가 필요하다.
- **6개월 영향력**: **높음(연구용)**. 단계별 태그 69개 + W&B 로그는 "능력이 어느 단계에서 생기는가"를 재는 공개 재료로 드물다. 제품용 영향력은 지시수행 축이 미보고라서 판단을 보류한다.
- **허와 실**: 걷어내면 **"9.0B 덴스, 에이전트·코딩 축에서 같은 급 오픈 모델보다 크게 앞선다고 자체 보고. 단 SciCode는 Gemma 4-12B에 지고, SWE-bench에서는 해킹 전력이 있으며, 코드는 아직 공개되지 않았다."**

> [!action] 당장 할 것
> 1. **[[표-부분인용]]에 "행별 비교군 교체" 축 추가 + "불리한 수치는 전체표 쪽" 규칙 수정**(볼트 관리자 판단).
> 2. **9월 말 재확인**: `ifm-ai/xllm`에 실제 코드가 올라왔는가, 기술보고서가 나왔는가, 기술보고서의 SWE-bench 70.6에 감사(reward-hacking 제거) 여부가 적혀 있는가.
> 3. 로컬 실험을 한다면 **FP8판 또는 BF16 + vLLM, 컨텍스트 32~64K 상한**으로 한정한다. 512K는 KV만 약 77GB라 로컬 대상이 아니다(볼트 계산).
> 4. ChinameBot: **도구 스키마 Markdown 제시 vs JSON 토큰 비교**를 내 데이터로 1회 측정한다(블로그 주장 18.5% 검증).

> [!question] 미해결 질문
> - 카드 SWE-bench Verified 70.6은 해킹 시행을 제거한 값인가? 82 → 70.6의 관계가 무엇인가?
> - 카드 차트 이미지(`assets/k2-horizon-7b-benchmarks.png`)는 볼트가 열어보지 않았다. 카드 표와 같은 선별인가?
> - 비교 모델 수치(Gemma·Qwen·Granite)는 IFM이 직접 쟀나, 공식 보고치를 옮겼나? 카드·블로그 모두 미기재.
> - 병합 설명의 "shared experts"는 덴스 7B에서 무엇을 가리키나?
> - EOS 논문의 "K2-Horizon 단계별 분석"은 어느 크기의 어느 태그를 썼나? (EOS 본문 미확인)

## 관련 페이지
- [[IFM]]
- [[K2-Horizon-MoVA-36B-A4B]]
- [[Uno]]
- [[When-EOS-Tokens-Disagree]]
- [[NeoHorse-1-9B]]
- [[Gemma-4-12B]]
- [[Muse-Glimmer-30B]]
- [[DeepSeek-V4-Flash]]
- [[DeepSeek-V3.2]]
- [[DeepSeek-V4.1-Flash-Paper]]
- [[표-부분인용]]
- [[한정어-탈락]]
- [[단위-불일치]]
- [[자기제한-명시]]
- [[에이전트축-분기]]
- [[측정도구-먼저-반증]]
- [[선택비용과-중복성]]
- [[local-llm]]
- [[MBZUAI]] *(신설 제안)*

## 원본
- 출처: https://huggingface.co/IFM/K2-Horizon-7B · 카드 원문 `raw/main/README.md` · `config.json` · API `refs`/`tree`
- 블로그: https://ifm.ai/blog/k2/ (Cloudflare 차단으로 curl 실패 → lightpanda 렌더 조회, 2026-09-19)
- 관련 레포: `IFM/K2-Horizon-7B-Uno` · `IFM/K2-Horizon-7B-GGUF` · GitHub `ifm-ai/xllm`(★47, 빈 레포) · `ifm-ai/uno`(★83)
- 볼트 실측(2026-09-19): HF models API `downloads` 12,834 · `likes` 212 · `createdAt` 2026-09-01 · `lastModified` 2026-09-18 · `safetensors.total` 8,999,178,240 · `gated` false · 태그 69 / 브랜치 1 · Uno 어댑터 `downloads` 50,562 · HF org `IFM` 멤버 99/모델 38/팔로워 1,320
- 신뢰도: ⭐⭐ (체크포인트 실재·자기 해킹 고백은 가점 · 카드 표 선별 확인·코드/보고서 미공개·SWE 70.6 감사 여부 미확인은 감점)
