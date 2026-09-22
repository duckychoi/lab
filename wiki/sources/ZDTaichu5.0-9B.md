---
title: "ZDTaichu5.0-9B — Qwen3.5-9B 대비 18승 9패, 공간을 얻고 OCR·지식을 내줬다 (그리고 부모가 기계판독 필드에 없다)"
type: source
domain: ai-news
tags: [ai-news, hf-model, vlm, spatial-reasoning, embodied, agent, qwen, c-radio, nvidia-license, 파생저장소-식별, 파생표기-함정, 비매칭-비교, local-llm]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# ZDTaichu5.0-9B (TaichuAI)

> [!insight] 🎯 핵심 인사이트 — **"일반 시각을 희생하지 않았다"는 카드 문장을 카드 자신의 표가 반박한다**
> README 20행 원문: *"**Rather than trading broad visual competence for specialization**, it layers a more comprehensive spatial, embodied, and agent capability profile on top."*
> 볼트 재집계(3개 HTML 표 27행, 자기 백본 `Qwen3.5-9B` 열 대비) — **18승 9패** ✅ 수집기와 일치. 🎯 그런데 **표별로 쪼개면 그림이 다르다**:
> | 표 | 승 | 패 | 패배 항목 |
> |---|---|---|---|
> | 공간·체화(9행) | **8** | 1 | CV-Bench(86.82 vs 87.19) |
> | 일반 시각·수학·OCR(7행) | **2** | **5** | MathVista·MathVerse VO(76.40 vs **84.14**)·MMStar·RealWorldQA·OCRBench(85.50 vs 89.20) |
> | 지식·지시·추론·에이전트(11행) | 8 | 3 | MMLU-Pro(77.20 vs 82.50)·MMLU-Redux·**HMMT Feb 2026**(72.70 vs 73.48) |
> 🔴 **일반 시각 표에서는 2승 5패다.** "trading 하지 않았다"가 아니라 **정확히 트레이드했다.** 수집기 결론(*"공간·에이전트를 얻고 일반 시각/지식 일부를 내줬다"*)이 맞고 카드 서술이 틀렸다.
> ⚠️ 수집기 패배 목록의 "HMMT"는 **HMMT Feb 2026**이다 — **Feb 2025는 승**(84.20 vs 83.20).
> 📌 볼트 추정: Qwen3.5-9B는 원래 **자체 비전 인코더를 가진 VLM**(HF pipeline `image-text-to-text`)이고 ZDTaichu는 그 인코더를 **C-RADIOv4-H로 교체**했다. OCR·문서 계열 하락이 인코더 교체 탓인지는 카드가 분리하지 않았다(ablation 없음).

> [!warning] ⚠️ **TAU2-Bench 87.7 > GPT-5.2 87.1 — 평가 조건이 다른 두 숫자** ✅ 수집기 정확
> † 각주 원문: *"Local TAU2-Bench and Claw-Eval general evaluations use **DeepSeek-V4-Flash-0731 as the simulated user and/or judge**; externally reported scores follow the evaluation setup of their cited sources."* → 자사 점수는 DeepSeek 시뮬레이터, GPT-5.2 87.1은 외부 보고 조건. **0.6점 차로 "leads"를 주장하기엔 조건이 안 맞는다** → [[비매칭-비교]].
> 🔴 수집기 미전달: **‡ 각주는 정의만 있고 표 어디에도 ‡ 표시가 없다**(*"EASI results use the supplied export reviewed on 2026-09-08"* — EASI 결과 행 자체가 없음). **어느 수치가 외부 인용인지 표시가 끊겼다.**
> ✅ 다중이미지 공간 벤치(ViewSpatial·MMSI·MindCube-tiny·VSI)에 `<think>`·`\boxed{}` 출력형식 지시 추가 — 원문 명시. 이 4개가 **전부 볼드+밑줄(전체 1위)** 인 벤치다. 형식 지시가 비교 모델에도 동일 적용됐는지는 **미기재**.

> [!warning] 🔴 **컨텍스트 길이가 세 곳에서 세 값이다**
> README Model Overview: **"Up to 128K tokens"** · `config.json` `llm_config.max_position_embeddings`: **262,144** · README vLLM 서빙 예시: `--max-model-len **220000**`.
> 어느 것이 검증된 운용 한계인지 카드가 말하지 않는다 → [[단위-불일치]] 계열(명목값↔설정값↔운용값).

> [!warning] ⚠️ **파생 표기 — 부모가 산문과 LICENSE 파일에만 있다** ✅ 수집기 정확
> HF `cardData` 에 `base_model`·`base_model_relation`·`license` **셋 다 없음**. 부모는 README 산문(*"Qwen3.5-9B LLM Decoder"*)·`THIRD_PARTY_LICENSES.md`·`NOTICE` 에만. `config.json` 내부 `llm_config.model_type: qwen3_5_text`(32층·hidden 4096·MTP 1층)가 기계적 흔적의 전부다.
> 🎯 [[파생저장소-식별]] 의 탐지키(`base_model` → `base_model_relation`)가 **둘 다 비어 있는 사례** — HF 트리에서 Qwen3.5-9B 파생으로 **집계되지 않는다** → [[파생표기-함정]].

> [!note] 📌 라이선스 — **NVIDIA OML이 전체 가중치를 덮는다**
> 루트 `LICENSE`(8,836 B) = `LICENSES/NVIDIA-Open-Model-License.txt`(8,836 B, 동일 크기). README 원문: *"model weights … under the **NVIDIA Open Model License Agreement**, with the Qwen3.5 Apache-2.0 license … retained."* 원인: 비전 백본 `nvidia/C-RADIOv4-H`(license `nvidia-open-model-license`, 리비전 `0057b339…` 고정)의 **파생모델 의무**가 전파.
> 🎯 **Apache-2.0 백본(Qwen3.5-9B)에 NVIDIA 인코더를 붙이는 순간 결과물 라이선스가 NVIDIA 쪽으로 이동한다** — 로컬 VLM 조립 시 인코더 선택이 라이선스 선택이다([[NVIDIA]]).
> 🔴 `NOTICE` 가 *"See LICENSES/MIT-OpenGVLab.txt"* 를 참조하지만 **39개 파일 전수 조회에 그 파일이 없다**(LICENSES/ 에는 Apache-2.0·NVIDIA-OML·README 2개뿐).

> [!note] 📌 볼트 실측 (2026-09-22, HF API) — 원본이 1,833배
> | | `TaichuAI/ZDTaichu5.0-9B` | 원본 `Qwen/Qwen3.5-9B` |
> |---|---|---|
> | 다운로드(30일) | **5,078**(수집기 3,750) | **9,307,599** |
> | 좋아요 | **307**(수집기 215) | **2,010** |
> | 라이선스 | (메타 없음) NVIDIA OML | Apache-2.0 |
> | 생성 | 2026-09-04 | 2026-02-27 |
> 🔴 수집기가 건너뛴 원본 DL을 채웠다. 역전 없음 — [[원본-파생-역전]] 해당 없음(원본/파생 **1,833배**). 좋아요 비율은 6.5배로 훨씬 좁다.
> 파일 **39개 전수** · BF16 **9.79B**(9,794,197,512) · `custom_code`(modeling.py·cradio_model.py 등, `trust_remote_code` 필수) · GitHub `Taichu-AI/ZDTaichu5.0-9B` ★**923**.
> 🔴 **서빙은 포크 필요**: *"We adapted the vLLM v0.26.0 branch with the architecture, quantization, and speculative decoding features"* — `Taichu-AI/vllm` 브랜치 `v0.26.0-zdtaichu`(★3) 또는 `registry-dx.wair.ac.cn` Docker 이미지. 업스트림 vLLM 미지원.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ✅ 27행 표·조건 각주·라이선스 경계 문서화. 🔴 전 수치 자체 측정·논문 없음 · 핵심 기법 *"Entropy-Gated Adaptive Recurrent Reasoning"* 은 **설명 한 문장뿐, 논문·ablation 없음** · 컨텍스트 3중 표기 · 고아 각주 · 누락 라이선스 파일.
- **즉시 활용**: **조건부** — 9.79B BF16 ≈ 20GB, 단일 GPU 가능. 🔴 단 transformers는 `trust_remote_code`, vLLM은 **포크 필수**. 로컬 공간추론 VLM이 필요하면 후보, 범용 OCR·문서라면 **원본 Qwen3.5-9B가 더 낫다**(표 기준).
- **6개월 영향력**: 로봇·VLA 백본으로서 **다시점 공간 벤치(MindCube-tiny 78.27 · ViewSpatial 62.50)가 Gemini 3 Pro·GPT-5.2보다 높다는 주장**은 주목할 만하다 — 단 형식 지시 추가 조건.
- **대체 관계**: 같은 9~10B급 STEP3-VL-10B·gemma4-8B-E4B와 경쟁. Qwen3.5-9B를 **공간 특화 방향으로 대체**, 일반 시각은 대체 못 함.
- **허와 실**: 허 = "trading 없음"(실제 일반시각 2승5패), TAU2 "leads"(조건 상이). 실 = 공간 9행 중 8승, 4개 다시점 벤치 전체 1위.
- **액션**: 아래.

> [!action] 당장 할 것
> 볼트 [[파생저장소-식별]] 에 **"base_model 미설정 + 인코더 교체형 VLM"** 탐지 규칙 후보로 이 사례를 넘긴다 — `config.json` 의 `llm_config.model_type`(`qwen3_5_text`)이 산문 외 유일한 기계적 부모 흔적이다.

> [!question] 미해결 질문
> 1. 실제 운용 컨텍스트는 128K·220K·262K 중 무엇인가.
> 2. Qwen3.5-9B 열의 점수는 자체 재측정인가 Qwen 공표치인가 — † 두 행 외엔 미기재.
> 3. 엔트로피 게이트 재귀추론의 기여분 — ablation 없음.

## 관련 페이지
- [[TaichuAI]]  *(09-22 연결)*
- [[파생저장소-식별]]
- [[파생표기-함정]]
- [[비매칭-비교]]
- [[단위-불일치]]
- [[원본-파생-역전]]
- [[표-부분인용]]
- [[NVIDIA]]
- [[Alibaba]]
- [[DeepSeek]]
- [[ai-news]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/TaichuAI/ZDTaichu5.0-9B
- 볼트 실측(2026-09-22, HF API): DL 5,078 · 좋아요 307 · created 2026-09-04 · lastMod 2026-09-20 · gated false · cardData에 base_model/relation/license **없음** · BF16 9,794,197,512 · 파일 39 · custom_code
- 원본 실측: `Qwen/Qwen3.5-9B` DL 9,307,599 · 좋아요 2,010 · Apache-2.0 · image-text-to-text · created 2026-02-27
- 부속 실측: `nvidia/C-RADIOv4-H` license nvidia-open-model-license · GitHub `Taichu-AI/ZDTaichu5.0-9B` ★923 · `Taichu-AI/vllm` ★3(브랜치 v0.26.0-zdtaichu 실재)
- 수치 출처: README **648행 전문**(HTML 표 3개 27행 전수 파싱 · †‡ 각주 · Quickstart · License) + `config.json` · `NOTICE` · `THIRD_PARTY_LICENSES.md` · `LICENSES/README.md`
- raw 대비: ✅ 18승 9패·TAU2 †·NVIDIA OML·base_model 미설정 일치 · 🔴 **원본 DL 미조회 → 9,307,599 채움** · 🎯 **표별 분해(일반시각 2승5패)로 카드 "no trading" 반증** · 🔴 **컨텍스트 128K/220K/262K 3중 표기** · 🔴 **‡ 고아 각주 · MIT-OpenGVLab.txt 누락** · 🔴 **vLLM 포크 필수** · ⚠️ "HMMT"는 Feb 2026만 패배
- 신뢰도: ⭐⭐ (표·각주 공개·라이선스 문서화 / 자체 측정 단일 출처·논문 없음·카드 내부 불일치 3건)
