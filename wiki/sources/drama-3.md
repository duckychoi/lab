---
title: "fishaudio/drama-3 — 카드는 속도만, 품질은 논문에만. 그리고 논문은 WER·SIM 을 '최적화하면 안 되는 지표'라고 주장한다"
type: source
domain: ai-news
tags: [ai-news, tts, voice-cloning, multi-speaker, moe, streaming, speech-editing, fish-audio, 짝아티팩트, 벤치마크외부축, 라이선스]
created: 2026-10-24
updated: 2026-10-24
sources: []
reliability: medium
---

# fishaudio/drama-3 (Fish Audio Drama 3)

**HF**: https://huggingface.co/fishaudio/drama-3
**논문**: arXiv **2610.18010v2** *"Fish Audio Drama 3 Technical Report"* (v1 2026-10-13 · v2 10-14 · cs.SD · 저자 16명) — **카드가 링크한 짝 아티팩트**
**실측(2026-10-24T09:06Z · 18:06 KST · `expand[]`)**: 다운로드 **17,017**(수집기 일치) · likes **958**(일치) · trendingScore **359** · `pipeline_tag` text-to-speech · `gated: false` · createdAt **2026-10-01T04:34Z**(공개 +23.2일) · lastModified 10-17T05:06Z
**파라미터**: `safetensors.total` **35,899,643,008**(≈35.9B = BF16 3.69B + **F8_E4M3 32.21B**) ⇒ 카드 *"35B · FP8 MoE experts, remaining weights in bf16"* **검증 통과**(FP8 비중 89.7%) · 별도 `codec.pth` 1.87GB
**신뢰도**: ⭐⭐ (다운로드 1.7만 · 논문 有 · 품질 수치는 자기보고이며 카드에는 0건 · 라이선스 표기 3중 불일치)

> [!insight] 🏆 핵심 인사이트 — **품질 수치를 카드에서 뺀 건 누락이 아니라 입장이다. 그리고 그 입장 아래에서 Drama 3 는 전작보다 표준 지표가 나쁘다**
> - **카드**: H200 서빙 **속도표 2개뿐**(TTFA·RTF·처리량). WER·CER·SIM·MOS **0건**.
> - **논문 §3.3·§5.2**: RL 보상을 **학습된 인간선호 보상모델 하나**로 두고 WER·SIM 보상을 **의도적으로 뺐다**. 근거로 Expresso 에서 *속삭임은 SIM 을 0.310 낮추고, SIM 보상은 기본 낭독을 62.0~99.7% 쌍에서 선호한다* 를 제시 ⇒ **"표준 지표는 연기(expressiveness)를 벌한다."**
> - ⇒ 🎯 이것은 [[벤치마크-외부축]] 의 **역방향**이다: 보통은 저자가 *점수가 못 잡는 불리한 축*을 덧붙이는데, 여기서는 저자가 *표준 점수 자체를 자기 목표에 반하는 축*으로 규정하고 카드에서 내렸다.
> - 🔴 **그런데 전작과 같은 표준 지표로 대면 Drama 3 가 진다**: Seed-TTS-Eval 최종 test-en WER **1.54** / test-zh CER **0.83** vs Fish Audio **S2 0.99 / 0.54**([[VoxCPM]] README 표 인용값) ⇒ **WER 1.56배 · CER 1.54배 나쁨**. 논문은 Seed-TTS-Eval 에서 **S2 와 비교하지 않는다**(SFT 체크포인트와만 비교) — S2 는 **속도(271 vs 177 fps)** 와 다국어표에서만 소환된다.
> ⇒ 📌 **읽는 법**: Drama 3 는 *"더 정확한 TTS"* 가 아니라 *"더 연기하는 TTS"* 로 포지셔닝했고, 그 대가가 표준 지표 후퇴로 **측정돼 있다**(볼트가 두 문서를 맞대어야 보인다 → [[짝-아티팩트-조회]]).
> - 🔴 **자기가 고른 연출 축에서도 확정 우위는 아니다**: Step-Audio-Edit(LLM 판정)에서 Step-Audio-EditX 에 감정 58.2 vs 69.3 · 준언어 2.32 vs 2.89 로 지고 스타일만 81.8 vs 63.8 로 이긴다. 인간 청취 평가는 0건. ⇒ **현재 근거로 확정되는 Drama 3 의 우위는 "한 모델에 기능을 묶었다"와 "서빙 속도" 둘뿐이다.**

## 🔍 카드 수치 검증 (속도 — 자기보고, 내부 산술은 정합)

Table 1 (H200 1장 · 스트리밍 · Seed-TTS 영어 프롬프트 · **사전 인코딩된 참조 `vq_codes` 사용** · temp 1.0 / top_p 0.9 / top_k 30 / max_new_tokens 500 · 4회 평균)

| 동시성 | 처리량(frames/s) | TTFA p50 | TTFA p95 | RTF |
|--:|--:|--:|--:|--:|
| 1 | 166.7 | **88.9 ms** | 90.8 ms | **0.131** |
| 16 | 927.6 | 210.1 ms | 287.2 ms | 0.373 |
| 64 | 1,687.3 | 450.9 ms | **1,020.1 ms** | **0.801** |

✅ 수집기 수치 전건 일치(conc1 TTFA p50 88.9ms · RTF 0.131 · conc64 RTF 0.801 · TTFA p95 1,020ms).
✅ 카드 본문 산술 재계산 일치: conc16 *"재생보다 ~2.7배 빠름"* = 1/0.373 = **2.68** · Table 2 보코더 2번째 GPU 분리 *"+72% 처리량 · −37% TTFA"* = 4,160/2,422 = **1.72** · 1 − 2,146/3,403 = **36.9%**.
🧮 볼트 추정(카드에 없음): 처리량 × RTF = 166.7 × 0.131 ≈ **21.8 프레임/오디오초** ⇒ 코덱 프레임률 ~22Hz 대로 보인다. conc64 스트림당 1,687.3/64 = 26.4 fps 와 RTF 0.801 이 이 추정과 정합(21.8/26.4 ≈ 0.83).

> [!warning] 🔴 **같은 회사·같은 GPU·같은 단일 스트림인데 카드 166.7 fps ↔ 논문 271 fps**
> 논문 초록·§4: *"At a concurrency of 1, Drama 3 decodes 271 frames per second on one NVIDIA H200 GPU, against 177 for S2"* · 카드 Table 1 conc1 처리량 **166.7 frames/s**. 비 1.63배. 정의가 다를 가능성(논문 = 순수 디코드 속도 · 카드 = 스트리밍 요청 단위 종단 처리량)이 크지만 **양 문서 모두 차이를 설명하지 않는다** → [[문서내-값충돌]](문서 간) · [[단위-불일치]]. ⇒ 인용 시 **어느 정의인지 함께 적는다.**
> 또 카드 속도는 **참조 음성을 미리 인코딩한(`vq_codes`) 조건**이다 — 실제 클로닝 첫 요청의 참조 인코딩 시간은 TTFA 88.9ms 에 **포함되지 않는다**.

## 📊 품질 — 논문에만 있는 수치 (자기보고 · 볼트가 arXiv HTML v2 로 확인)

**① Seed-TTS-Eval (Table 4 · SFT vs Drama 3)**
| | test-zh CER 첫 테이크 | 최종 | test-en WER 첫 테이크 | 최종 | 플래그(zh/en) |
|---|--:|--:|--:|--:|--:|
| SFT | 1.66 | 0.84 | 3.49 | 1.60 | 2.82% / 3.40% |
| **Drama 3** | **1.00** | **0.83** | **2.20** | **1.54** | 1.24% / 1.84% |
> [!warning] "최종"은 재생성 후 값이다
> §5.1: *"Outputs that fail simple signal checks … are regenerated and rescored."* ⇒ 최종값은 **실패 테이크를 다시 뽑은 값**이고 베이스라인 수치는 *"quoted from their papers"* — 베이스라인도 같은 재생성을 했는지 **불명** → [[비매칭-비교]]. 첫 테이크 en **2.20** 은 [[VoxCPM]] README 의 VoxCPM2 **1.84** 보다 나쁘고, 최종 **1.54** 는 낫다 ⇒ **재생성 여부가 순위를 뒤집는다.**
- 스트리밍 vs 비스트리밍(test-en 1,088문장): WER **1.86 / 1.83** · SIM 둘 다 **0.640** ⇒ *"Streaming costs no quality"* (Table 4 최종 1.54 와 또 다른 값 — 샘플링 조건 차이로 보이나 미설명)

**② 클로닝 (Table 5 · LibriSpeech-PC test-clean · OmniVoice 채점 방식)**
| 시스템 | WER | SIM | UTMOS |
|---|--:|--:|--:|
| Drama 3 (참조 1) | 1.85 | 0.605 | 4.31 |
| Drama 3 (참조 3) | 1.85 | 0.633 | 4.31 |
| [[OmniVoice]] | **1.30** | **0.729** | 4.28 |
| Qwen3-TTS | 1.60 | 0.704 | **4.41** |
| CosyVoice 3 | 1.59 | 0.694 | 4.28 |
> [!warning] 🔴 본문이 표의 1위를 건너뛰었다 → [[표-부분인용]]
> 본문: *"With one reference, Drama 3's UTMOS of 4.31 is above the 4.28 of OmniVoice and CosyVoice 3."* — **같은 표의 Qwen3-TTS 4.41 은 언급하지 않는다.** 실제로 Drama 3 는 이 표에서 **WER·SIM 꼴찌, UTMOS 2위**다.

**③ 다국어 (Table 6 · MiniMax Multilingual 24개 언어 · 오류율 %)** — 🇰🇷 내 워크플로 관점 발췌
| 언어 | Drama 3 | OmniVoice | Fish S2 | ElevenLabs v4 |
|---|--:|--:|--:|--:|
| **Korean (CER)** | 2.36 | 2.65 | **1.18** | 2.63 |
| English (WER) | **1.13** | 1.56 | 1.62 | 1.56 |
| Japanese (CER) | 5.02 | 4.03 | **2.76** | 3.66 |
| Chinese (CER) | **0.63** | 1.01 | 0.73 | 0.66 |
- 🎯 **한국어는 전작 S2 가 2배 낫다**(1.18 vs 2.36). 단 S2·OmniVoice 는 *"quoted from their papers, which used their own scoring"*, ElevenLabs 는 Fish 가 API 로 직접 돌림 ⇒ **같은 열 안에서도 채점 주체가 다르다.**

**④ 연출 수정 — 자기가 내세운 축 (Table 9 · Step-Audio-Edit · 판정자 Gemini-2.5-Pro)**
| 지표 | Drama 3 (Iter 0→3) | Step-Audio-EditX (0→3) |
|---|--:|--:|
| 감정 정확도 | 55.5 → **58.2** | 53.6 → **69.3** |
| 스타일 정확도 | 76.5 → **81.8** | 45.6 → 63.8 |
| 준언어 이벤트(1~3점) | 1.32 → **2.32** | 1.91 → **2.89** |
> [!warning] 🔴 **"연기하는 TTS" 서사의 축에서도 3개 중 2개를 진다**
> Drama 3 가 이기는 것은 **스타일 1개**. 감정은 3회 수정 후 **11.1점 열세**, 준언어 이벤트도 열세. 또 Step-Audio-EditX 값은 *"quoted from … its paper, with the judge scores reported there"*, Drama 3 는 *"our own run"* ⇒ 판정 실행 주체가 다르다([[비매칭-비교]]). 🎯 **판정자는 LLM(Gemini-2.5-Pro)이고, 인간 블라인드 청취 평가는 논문 어디에도 없다**(볼트 HTML 본문 검색: listening test·human evaluation·CMOS·win rate against **0건**). ⇒ *"인간 선호"는 보상모델 학습 데이터에만 있고, 평가에는 없다.*

**⑤ 편집(인필링)**: Ming-Freeform 중국어 삽입·치환 SIM **0.909 / 0.898**(CosyEdit2 0.89) · Cartesia Sonic-3 인필 API 대비 중국어 WER **3.69 vs 8.64**(basic). 영어에선 SSR-Speech·CosyEdit2 가 WER·SIM 모두 앞선다(Table 7).

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: HF 17,017 dl(공개 23일 · dl/♥ **17.8 : 1**) · arXiv 기술보고서 有 · 품질은 전부 자기보고 · SGLang-Omni / vLLM-Omni **출시일 지원**(카드 명령 제공).
- **즉시 활용**: 🟡 **조건부 YES** — 내 `/reat-voice` 파이프라인(내 쇼츠 내레이션·더빙 생성)은 라이선스상 **"Hosted Service 아님"** 범주(*"generating speech for content that You create … narration, dubbing"*)이고 연매출 **USD 500,000 미만**이면 상업 사용 가능. 🔴 **반대로 내 SaaS 에서 사용자에게 TTS/보이스클로닝 기능을 제공하는 것은 "Hosted Service" 로 별도 계약 필요.** 하드웨어: FP8 35.9B ≈ 가중치만 ~36GB(추정) ⇒ **H100/H200급 1장**, 소비자 GPU 불가.
- **6개월 영향력**: *"한 모델이 클로닝·다화자(최대 16)·자연어 연출·재녹음(previous_takes)·인필 편집·스트리밍"* 을 묶었다. 영상 더빙 파이프라인에서 **"대사 한 단어 고치기 = 해당 구간만 재생성"** 이 API 수준으로 내려온 것이 가장 큰 변화(`previous_takes` 예시 K1·K5).
- **대체 관계**: [[VoxCPM]](Apache-2.0 · 2B · 로컬 가능) / [[OmniVoice]](Apache-2.0) / ElevenLabs 의 **대체가 아니라 상위 포지션 실험**. 정확도·한국어·라이선스·하드웨어 4개 축 모두에서 VoxCPM2·OmniVoice 가 로컬 기본값으로 더 낫고, Drama 3 의 우위는 **다화자 장면·연출 지시·편집**에 한정된다.
- **허와 실**: 속도표는 산술 정합 ✅ · 단 참조 사전 인코딩 조건 · 카드↔논문 fps 불일치. 품질은 *"표준 지표를 버렸다"* 는 서사와 함께 **전작 대비 후퇴가 수치로 존재**. "인간 선호" 우위를 직접 보여주는 **인간 블라인드 청취 평가는 논문 전체에 없다**(§5.6 연출 평가는 Gemini-2.5-Pro 판정 · 감정·준언어에서 Step-Audio-EditX 에 열세).
- **액션**: 아래 참조.

> [!warning] 🔴 라이선스 표기가 세 곳에서 다르다 → [[간판-지체]] · [[문서내-값충돌]]
> ① `cardData.license_name` = **`fish-audio-research-license`** · `license_link` = **`LICENSE.md`** ② 레포 실제 파일 = **`LICENSE`**(`LICENSE.md` **없음** — 링크 깨짐) · 본문 제목 *"FISH AUDIO COMMUNITY LICENSE AGREEMENT Version 1.0 — Last Updated: October 13, 2026"* ③ README 하단 *"Fish Audio Community License"*.
> ⇒ 🎯 **메타데이터(간판)는 "연구 라이선스", 실제 문서는 "연매출 50만 달러 미만 상업 허용 커뮤니티 라이선스"** — 간판이 본문보다 **더 제한적으로** 멈춰 있다(과소표기형 간판 지체). HF 라이선스 필터로 거르면 **상업 가능 모델을 연구 전용으로 오분류**하게 된다.

> [!action] 액션 후보
> - (중간) [[VoxCPM]] 과 **한국어 대사 10문장 A/B**(같은 참조 음성) — 논문 Table 6 의 한국어 CER 2.36(Drama 3) vs 다른 채점의 1.18(S2)이 실제 청감에서 어떤지. 단 Drama 3 는 H100/H200급 필요 → 클라우드 1시간 단위로만.
> - (중간) 내 SaaS 기획에서 TTS 를 **"사용자 직접 입력 기능"으로 넣을지 "내가 연출한 결과물만 납품"으로 둘지** 결정할 때 이 라이선스의 Hosted Service 조항(§III(c))을 기준 사례로 사용.
> - (낮음) 다화자 장면(`<|speaker:N|>` 최대 16)으로 **대본 1편 더빙 시험** — 볼트 수치가 아니라 이 모델의 유일한 차별점(장면 단위 생성)을 직접 확인

> [!question] 미해결
> ① 카드 166.7 fps ↔ 논문 271 fps 의 정의 차이 ② Seed-TTS-Eval 에서 S2 와의 **동일 조건** 비교(논문에 없음 · S2 0.99/0.54 는 VoxCPM README 의 인용값이라 채점 조건 미확인) ③ 인간 블라인드 청취 평가 — **논문에 없음 확인**, 외부 평가 출현 여부 추적 ④ `createdAt` 10-01 인데 라이선스·논문은 10-13 — 공개 전 비공개 기간인지 ⑤ 카드 본문 *"the same … wav the cloning example above uses"* — **위에 클로닝 예시가 없다**(편집 잔재)

## 관련 페이지
- [[Fish-Audio]] ← 개발사 (🆕 엔티티)
- [[VoxCPM]] · [[voxcpm2]] · [[VoxCPM2-HF]] · [[OmniVoice]] · [[higgs-audio-v3-tts]] · [[pocket-tts]] ← 볼트 내 오픈 TTS 비교군
- [[Qwen]] ← 백본 초기화(논문: *"initialized from a pre-trained Qwen3.5 language model"*)
- [[vllm]] ← vLLM-Omni 지원
- [[벤치마크-외부축]] · [[짝-아티팩트-조회]] · [[표-부분인용]] · [[비매칭-비교]] · [[간판-지체]] · [[문서내-값충돌]] · [[단위-불일치]]

## 원본
- 출처: https://huggingface.co/fishaudio/drama-3
- 열어 본 것: HF API `?expand[]=downloads,downloadsAllTime,likes,createdAt,lastModified,gated,safetensors` · `raw/main/README.md`(HTTP 200 · 7,996 B) · `raw/main/LICENSE` · `tree/main` · arXiv API + **arXiv HTML v2 본문**(§3.3·§4·§5.1~5.6) · VoxCPM GitHub README(S2 비교값)
- 관측: 2026-10-24T09:06Z (18:06 KST)
- 신뢰도: ⭐⭐
