---
title: "XingChen-AGI/Xing4.0-29B-A4B — '첫 Ascend 전량 학습'은 규모 한정어가 떠받친다. 선대 TeleChat3-MoE는 105B~1T를 이미 Ascend로 학습했다"
type: source
domain: local-llm
tags: [local-llm, hf-model, moe, mla, mhc, mtp, ascend, mindspore, china-telecom, telechat, agent, 한정어-탈락, 표-부분인용]
created: 2026-09-19
updated: 2026-09-19
sources: []
reliability: low
---

# Xing4.0-29B-A4B

> [!insight] 핵심 인사이트: "첫"은 규모 한정어가 있어야 성립한다. 그 한정어는 언어마다 다르다
> HF 카드 원문(영어): *"It is **the first model of this scale** trained **entirely** on the Ascend NPU platform **with the MindSpore framework**"*.
> GitHub `README_zh.md` 원문(중국어): *"是**国内首个**基于**国产算力与国产框架**完成训练、**面向复杂工程任务深度优化**的**百亿参数**大模型"*(국내 최초로 국산 연산력·국산 프레임워크로 학습을 완료하고 복잡한 엔지니어링 과제에 깊이 최적화된 백억(10B)급 파라미터 대형 모델).
> 🔴 같은 회사 선대 보고서(카드가 인용한 arXiv 2512.24157 *Training Report of TeleChat3-MoE*) 초록: *"parameter counts ranging from **105 billion to over one trillion**, trained **end-to-end on Ascend NPU cluster**"*.
> 🎯 **더 큰 모델을 이미 Ascend로 끝까지 학습한 선례가 같은 계보 안에 있다.** 그래서 "첫" 주장은 **"이 규모(29B)"라는 한정어로만 참이다.** 더 작은 규모의 최초라는 뜻이다. 중국어판은 한정어를 더 쌓는다(国内 · 百亿参数 · 面向复杂工程任务深度优化). *"Ascend만으로 학습한 첫 모델"*로 옮기는 순간 틀린 문장이 된다 → [[한정어-탈락]].
> 📌 TeleChat3-MoE가 **MindSpore를 전용으로** 썼는지는 볼트가 확인하지 못했다. TeleChat3 README는 *"完全基于国产算力训练"* + Atlas 800T A2에서 MindSpore 학습 "지원"이라고만 적는다. "with the MindSpore framework"가 선대와의 실질 차이일 가능성은 남는다(미확인).

> [!warning] 🔴 굵은 글씨 오류 확인. 그리고 자사 GitHub 본문은 그 오류를 스스로 부정한다
> HF 카드 표의 굵은 글씨는 4개이고 **모두 Xing 열**이다: Claw-Eval 76.55 · **SWE-bench Verified 75.00** · Terminal-Bench 2.1 57.50 · DeepresearchBII 60.80.
> SWE-bench Verified 같은 행 **Qwen3.6-35B-A3B는 76.00**이다(✅ 수집기 일치). 카드는 굵은 글씨의 뜻을 정의하지 않는다. 다만 나머지 3개 굵은 칸은 모두 실제 행 최고값이므로 "행 최고" 관례로 읽히고, 그 관례로는 **오류**다.
> 🎯 결정적 대조: GitHub README(같은 조직, `XingChen-AGI/Xing4.0-29B-A4B`)의 **같은 표에는 굵은 글씨가 전혀 없고**, 본문은 *"On SWE-bench Verified (75.0), it **approaches** Qwen3.6-35B-A3B (76.0)"*라고 쓴다. **텍스트는 졌다고 말하는데 HF 카드의 서식은 이겼다고 표시한다.** 서식은 HF 카드에만 덧칠됐다. → 🎯 **볼트 규칙 후보: 굵은 글씨는 주장이지 데이터가 아니다. 행 최고값은 볼트가 직접 계산한다.**

> [!warning] 파라미터 29B vs `safetensors.total` 31,215,031,088: 볼트 역산으로 원인 확인(추정)
> ✅ 수집기 값 일치(HF API 2026-09-19: BF16 31,215,028,352 + F32 2,736 = **31,215,031,088**).
> 볼트 역산(`config.json`: 40층 · hidden 3584 · MLA q_lora 768/kv_lora 512 · 처음 2층 덴스 FFN 9216 · 나머지 38층 MoE 64전문가×1024 + 공유 1 · vocab 131,072 · `tie_word_embeddings: false` · **`num_nextn_predict_layers: 1`** · mHC `hc_mult: 4`):
> ```
> 본체 40층 + 임베딩 + lm_head        29,477,977,984
> mHC 파라미터(hc_fn 등, 80개 모듈)       ≈27,530,000
>   → 본체 소계                        ≈29.51B   ← 카드 "29B"
> MTP 층(model.layers.40) 블록 본체       769,998,144
> MTP 층 자체 embed_tokens + shared_head.head  939,524,096  (131,072×3584 ×2, 중복 사본)
>   → 합계                             ≈31.215B  ← safetensors.total (잔차 < 0.001%)
> 활성 파라미터(볼트 추정)             ≈3.9B     ← 카드 "4B active"
> ```
> 🎯 **수집기의 "MTP 층 포함 여부 미기재(추정 원인)"가 산술로 뒷받침된다.** 차이 1.71B 중 0.94B는 MTP 층에 **임베딩·출력 헤드를 중복 저장**했기 때문이다(`model.safetensors.index.json`에 `model.layers.40.embed_tokens.weight`·`model.layers.40.shared_head.head.weight`가 실재). → [[단위-불일치]]: 카드의 "29B"는 **추론 본체**, 파일은 **학습 체크포인트 전체**를 센다. **로컬 VRAM은 MTP를 안 쓰면 29.5B, 쓰면 31.2B로 잡는다.**

## 도메인별 추출 (local-llm)

> [!note] 도메인 재판정: ai-news → **local-llm** (ai-news 태그 병기)
> 근거: ① 활성 약 3.9B MoE라 **토큰당 연산은 4B급**이다. ② 볼트는 같은 형태(36B-A4B)의 [[K2-Horizon-MoVA-36B-A4B]]를 local-llm으로 분류했다. ③ 카드가 Claude Code·OpenClaw·**Hermes** 등 에이전트 프레임워크 적응을 명시한다. 핵심 주장(Ascend 자립)은 ai-news 성격이라 태그로 남긴다.

- **실용성 판단**: 🔴 **현재는 NO(메인라인 기준).** HF 카드 서두는 *"compatible with Transformers, vLLM, SGLang, KTransformers, and other mainstream inference frameworks"*라고 쓴다. 그런데 GitHub README는 *"submitted ... via pull requests, which are currently under review and **not yet merged** into their main branches"*라고 쓴다. 볼트 실측(GitHub API, 2026-09-19) 결과 5개 PR이 **전부 `open` · `merged: false`**다: sglang#39793 · vllm#57135 · TensorRT-LLM#19283 · llama.cpp#29012 · ktransformers#2168. → [[한정어-탈락]] 역방향 A(카드가 "PR 브랜치 한정"을 뺐다).
  - 용량: BF16 약 62.4GB(`total_size` 62,430,071,008 B). `-GGUF` 레포는 **IQ4_NL 한 종류(3분할, 합 20,104,013,088 B ≈ 20.1GB)** 뿐이고, llama.cpp PR이 미병합이라 **메인라인 llama.cpp로는 못 돌린다.** FP8판 있음. 24GB GPU + 병합된 llama.cpp라면 IQ4_NL로 올라갈 크기다(추정). **지연시간 수치는 카드에 없다.**
- **메모리 아키텍처**: 외부 메모리 없음. **MLA**(KV를 kv_lora_rank 512로 압축)라서 GQA 대비 **긴 컨텍스트 KV 캐시가 작다**(로컬에서 256K를 노릴 때 유리한 구조, 정량은 미측정). 컨텍스트 256K 네이티브(`max_position_embeddings` 262,144, YaRN factor 64 · original 4,096), 512K 확장.
- **Hermes 적용**: 🟡 카드가 *"targeted adaptation and format alignment for agent frameworks such as OpenCode, Claude Code, OpenClaw, and **Hermes**"*라고 명시한다. 볼트 [[hermes-agent]]와 같은 것인지 확인되지 않았다(추정 가능성 높음). **추론 스택 PR이 병합되기 전에는 적용 불가.** 병합 후 1순위 실험 대상이다. Terminal-Bench 2.1 57.50 · Claw-Eval 76.55가 이 비교군 안에서 1위인 축이 바로 ChinameBot에 필요한 축이다.
- **트레이드오프**: 에이전트/도구 축(Claw-Eval·Terminal-Bench·DeepresearchBII)에서 이기고, **지시수행(IFBench −3.00 vs Gemma)·장문맥(AA.LCR −5.00 vs Gemma)·수학(AIME −2.70 vs Qwen)**에서 진다. → [[에이전트축-분기]]가 또 재현됐다. 지시수행 약세는 봇 용도에서 감점이다.
- **오픈소스 구현체**: 가중치 Apache-2.0 · GitHub `XingChen-AGI/Xing4.0-29B-A4B` ★63 · fork 3 · open issues 0(2026-09-19). LLaMA-Factory·MindFormers 파인튜닝 튜토리얼 포함. **학습 코드·데이터는 공개하지 않았다.**

## 수집기 대조

| 수집기 주장 | 원문/실측 | 판정 |
|---|---|---|
| DL 3,073 · 2026-09-16 생성 · Apache-2.0 | `downloads` 3,073 · `createdAt` 2026-09-16T06:44:40Z · apache-2.0 | ✅ 일치 |
| ♥539 | `likes` **542** | ⚠️ +3 드리프트(조회 시각 차이, 오류 아님) |
| 트렌딩 6위 | 미조회 | 미확인 |
| 중국전신 AI · 총 29B/활성 4B · 라우팅 64/활성 4/공유 1 · MLA+mHC+MTP · 256K→512K | 카드 표·Highlights·`config.json` 일치 | ✅ 일치 |
| *"이 규모에서 Ascend NPU+MindSpore만으로 학습한 첫 모델"* | 영어 원문 일치. 단 중국어판 한정어 상이 · 선대 TeleChat3-MoE 105B~1T Ascend 학습 | ✅ 인용 일치 · ⚠️ 맥락 보충 |
| 학습 처리량 약 96% 향상(기본 대비) | *"approximately **96%** over out-of-the-box performance"* | ✅ 일치 |
| safetensors 31,215,031,088 · MTP 추정 원인 | 일치 · 볼트 역산으로 확인 | ✅ 일치 (+강화) |
| 9행 값 27개 | 카드 표 전 셀 대조 | ✅ 전건 일치 |
| 6개 축 1위 아님 / 3개 축 1위 | 볼트 행별 최대값 계산 일치 | ✅ 일치 |
| SWE-bench Verified 굵은 글씨 오류(75.00 vs 76.00) | 카드 원문 확인 · GitHub 본문 "approaches" | ✅ 일치 (+자사 텍스트 모순) |
| 측정 프로토콜(SWE 210K SWE-agent · TB terminus-2 3회 · Tau3 4회 · AIME 5회) | 각주 원문 일치 | ✅ 일치 · 누락 보충 아래 |
| 비교 모델 수치 측정 주체 미명시 | 각주는 전부 "We evaluate **Xing4.0-29B-A4B**" | ✅ 일치 |

> [!note] 각주 보충(수집기가 옮기지 않은 것)
> - **Claw-Eval 3회 평균** · **AA.LCR 3회 평균**. IFBench · SWE-bench 두 종 · DeepresearchBII는 **회차 미기재**다.
> - Terminal-Bench 2.1은 **24시간 타임아웃** · `max_tokens` 64K.
> - DeepresearchBII는 **OpenCode 하네스 + Exa MCP 서버 활성**. 검색 도구 조건이 붙은 수치다. 비교 모델이 같은 조건이었는지는 적혀 있지 않다.
> - Tau3-Bench 링크는 `sierra-research/tau-bench`(원 tau-bench 레포)를 가리킨다. tau3 전용 하네스인지 불명확하다(미확인).
> - 온도가 벤치마다 1.0/0.8로 다르다(SWE·AIME·AA.LCR 1.0, 나머지 0.8).

## 전체 비교표 (카드 원문, 부분인용 금지)

| 벤치 | Xing4.0-29B-A4B | Gemma4-26B-A4B | Qwen3.6-35B-A3B | 행 1위(볼트 계산) |
|---|---|---|---|---|
| IFBench | 69.67 | **72.67** | 65.50 | Gemma |
| AIME2026 | 90.00 | 88.30 | **92.70** | Qwen |
| AA.LCR | 61.00 | **66.00** | 62.00 | Gemma |
| Tau3-Bench | 64.63 | 58.90 | **67.20** | Qwen |
| Claw-Eval | **76.55** | 71.49 | 74.54 | Xing |
| SWE-bench Verified | 75.00 *(카드는 굵게)* | 53.00 | **76.00** | Qwen |
| Terminal-Bench 2.1 | **57.50** | 30.00 | 51.50 | Xing |
| SWE-bench Multilingual | 66.00 | 51.00 | **67.20** | Qwen |
| DeepresearchBII | **60.80** | 39.30 | 59.70 | Xing |

> [!insight] 표를 전부 읽으면 보이는 것
> - **Qwen3.6-35B-A3B가 4행, Gemma가 2행, Xing이 3행에서 1위다.** 비교군 3종 중 최다 1위는 Xing이 아니라 **Qwen**이다.
> - Xing의 이기는 축 3개는 모두 **에이전트 하네스 의존 벤치**(Claw-Eval·Terminal-Bench·DeepresearchBII)다. 하네스 조건이 비교 모델과 같았는지 불명확한 바로 그 축들이다.
> - ✅ **대조: [[K2-Horizon-7B]]와 달리 이 카드는 비교군을 행마다 바꾸지 않는다**(3열 고정). 그래서 지는 6개 행이 그대로 보인다. **서식(굵은 글씨) 1건을 빼면 표 구성은 정직하다.**

## 조직·계보

- HF 카드: *"a next-generation large language model in the Xing series (**formerly [TeleChat](https://github.com/Tele-AI/TeleChat3)**), developed by **China Telecom Artificial Intelligence Technology Co., Ltd.**"* (✅ 구 TeleChat · China Telecom 관계는 카드 원문에 명시)
- 중국어판: *"由**中电信人工智能科技有限公司**研发，是**星辰语义大模型**系列（原 TeleChat）的新一代模型"*. 조직명 "XingChen" = 星辰(TeleChat의 중국어 브랜드 "星辰语义大模型").
- 🔴 선대 TeleChat3 README는 개발 주체를 *"**中国电信人工智能研究院**"*(China Telecom AI 연구원, TeleAI)으로 적는다. **법인명이 다르다**(科技有限公司 vs 研究院). 두 법인의 관계는 원문에 없다(미확인).
- 카드 인용 논문: TeleChat3-MoE 학습 보고서(2512.24157, 저자 54명) · TeleChat2/2.5/T1 기술보고서(2507.18013). 🎯 **96% 향상에 쓴 기법 중 "DVM 자동 그래프-연산자 융합"은 TeleChat3-MoE 보고서 초록에도 있다**(*"DVM-based operator fusion"*). 효율 기법 일부는 선대에서 이어졌다.
- HF 조직 `XingChen-AGI`: 멤버 10 · 모델 3(본체·GGUF·FP8) · 팔로워 101 · `isVerified` false(2026-09-19). GitHub 레포 생성 2026-09-17.
- 📌 좋아요/다운로드 비율: ♥542 / DL 3,073 ≈ **0.18**. [[K2-Horizon-7B]]는 212/12,834 ≈ 0.017로 **약 10배 차이**다. 생성 3일차라 DL이 아직 쌓이지 않은 탓이 크다([[DeepSeek-V4.1-Flash]] "공개 후 72시간 지표 무효" 규칙 경계선). 판정에는 쓰지 않는다.

## 도메인 템플릿 보충 (ai-news 교차)
- **신뢰도**: HF DL 3,073 · ♥542 · GitHub ★63 · 선대 기술보고서 있음(본 모델 전용 보고서 없음) · 벤치 전부 자체 보고 · 서식 오류 1건 · 추론 스택 미병합. → **low**.
- **즉시 활용**: **NO.** 추론 PR 5건이 전부 미병합이다.
- **6개월 영향력**: **중간.** 🎯 비-NVIDIA 학습 스택(Ascend 910C + MindSpore/MindFormers)으로 **에이전트 벤치 경쟁력이 있는 29B MoE**가 나왔다는 산업적 신호다. PR이 병합되면 로컬 에이전트 후보가 된다.
- **대체 관계**: 병합 후 [[Qwen3.6-35B-A3B]] · [[Gemma-4-26B]]와 같은 슬롯(활성 3~4B MoE 로컬 에이전트)을 놓고 경쟁한다.
- **허와 실**: 걷어내면 **"Ascend로 학습한 29B-A4B MoE. 에이전트 하네스 벤치 3개에서 앞서고 나머지 6개에서 뒤진다. '첫 Ascend 학습'은 규모 한정 주장이고, 선대가 더 큰 모델로 이미 했다."**

> [!action] 당장 할 것
> 1. **추론 PR 5건 병합 추적**(특히 llama.cpp#29012 · vllm#57135). 병합 전에는 설치하지 않는다.
> 2. 병합 후 ChinameBot 후보 평가: **IFBench 69.67(Gemma 72.67보다 낮음)이므로 지시 준수 테스트를 먼저** 한다.
> 3. 볼트 규칙 제안: **"굵은 글씨는 주장이지 데이터가 아니다. 행 최고값은 볼트가 계산한다"**(관리자 판단).

> [!question] 미해결 질문
> - TeleChat3-MoE는 MindSpore만으로 학습했나? 그렇다면 영어판 "first ... with the MindSpore framework"도 규모 한정어만 남는다.
> - 비교 모델(Gemma4-26B-A4B·Qwen3.6-35B-A3B) 수치는 자체 측정인가, 공식 보고치 인용인가? 동일 하네스·동일 회차였나?
> - 카드의 "Hermes"는 Nous Research의 [[hermes-agent]]인가?
> - 96% 향상의 기준선("out-of-the-box")은 어떤 설정인가? 절대 처리량(TFLOPS/MFU) 수치가 없다.
> - MTP 층은 추론 시 speculative decoding용으로 쓰이나? PR 코드 미확인.

## 관련 페이지
- [[K2-Horizon-7B]]
- [[K2-Horizon-MoVA-36B-A4B]]
- [[Qwen3.6-35B-A3B]]
- [[Gemma-4-26B]]
- [[hermes-agent]]
- [[opencode]]
- [[한정어-탈락]]
- [[표-부분인용]]
- [[단위-불일치]]
- [[에이전트축-분기]]
- [[측정도구-먼저-반증]]
- [[DeepSeek-V4.1-Flash]]
- [[local-llm]]
- [[China-Telecom]] *(신설 제안)*

## 원본
- 출처: https://huggingface.co/XingChen-AGI/Xing4.0-29B-A4B · 카드 원문 `raw/main/README.md` · `config.json` · `model.safetensors.index.json`
- GitHub: https://github.com/XingChen-AGI/Xing4.0-29B-A4B (`README.md`, `README_zh.md`) · 선대 https://github.com/Tele-AI/TeleChat3 (README) · arXiv 2512.24157 초록(HF papers API + arXiv API)
- 볼트 실측(2026-09-19): HF models API `downloads` 3,073 · `likes` 542 · `createdAt` 2026-09-16 · `lastModified` 2026-09-18 · `safetensors.total` 31,215,031,088 · `gated` false · GitHub API ★63/fork 3/open issues 0 · 추론 PR 5건 `state: open`, `merged: false` · GGUF IQ4_NL 합 20,104,013,088 B
- 신뢰도: ⭐ (표 구성은 정직하고 각주가 상세한 점은 가점 · 서식 오류·추론 스택 미병합·"첫" 주장 한정어 의존·전 벤치 자체 보고는 감점)
