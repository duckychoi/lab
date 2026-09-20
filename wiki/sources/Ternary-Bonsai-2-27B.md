---
title: "Ternary-Bonsai-2-27B — 1.72bit는 '이상값'이고 출하물은 1.75/2.13이다"
type: source
domain: ai-news
tags: [ai-news, hf-model, gguf, quantization, ternary, 27b, local-llm, 단위-불일치, 검사가능성-후퇴]
created: 2026-09-20
updated: 2026-09-20
sources: [Bonsai-27B.md]
reliability: medium
---

# Ternary-Bonsai-2-27B-gguf (prism-ml)

> [!insight] 핵심 인사이트 — **전 구간 삼진, 그리고 로테이션이 진짜 장치다**
> [[Qwen3.8-27B]] 파생. 임베딩·어텐션 투영·MLP 투영·LM 헤드까지 **전 구간 삼진 {−1,0,+1} g128**(그룹 128마다 FP16 스케일 1개).
> 🎯 **README가 덜 광고하는 핵심**: 가중치가 **회전된 기저(rotated basis)** 에 저장된다 — 블록 1024 **하다마드 직교 회전**을 오프라인으로 가중치에 접어 넣고, 런타임이 활성값에 대응 변환을 건다. *"the packed model **declares its rotation as metadata**, so a runtime either applies the matching transform **or refuses to load the file**."* → **포맷이 오용을 거부하도록 설계됐다.**
> 성능(자사 화이트페이퍼): 14개 thinking 벤치 평균 **84.78 = FP16의 98.2%**, 통상 IQ2_XXS 빌드 **72.59** 를 크게 상회, **3배 용량의 UD-Q4_K_XL과 0.4점 차**. 수학 **96.57** · 코딩 **89.42** · 에이전틱 툴콜 **74.92**. 컨텍스트 **262K**.
> 구성: 27.36B = 언어 백본 24.35B(64블록) + 임베딩/LM헤드 2.54B + **비전 타워 0.46B**(별도 mmproj Q8_0 0.63GB, 이미지 입력 시에만 적재).

> [!warning] 🔴 수집기 정정 1 — **"실측 1.72 bit/weight · ~5.9GB"는 출하물이 아니라 이상값이다**
> README `Memory Requirement` 표는 **4행**이고, 수집기는 **2행(FP16·이상값)** 만 옮겼다:
>
> | Format | True bits/weight | Size | Reduction |
> |---|---|---|---|
> | FP16 (baseline) | 16.0 | ~54 GB | 1.0x |
> | **Ternary g128 (ideal)** | **1.72** | **5.8 GB** | **~9.3x** |
> | **GGUF PTQ1_0** (dense trits) | **1.75** | **5.95 GB** | **~9.0x** |
> | **GGUF PQ2_0** (2-bit slots) | **2.13** | **7.21 GB** | **~7.5x** |
>
> 🔴 **수집기는 *"실측 1.72 bit/weight"* 라 썼는데, README 헤드라인이 그 행에 `(ideal)` 라벨을 직접 달고 있다** — *"~9.3x smaller than FP16 **(ideal)**"*. **실측이 아니라 정보이론 목표값이다.**
> 🔴 **실제 내려받는 파일은 둘 뿐이고 어느 것도 1.72가 아니다**: PTQ1_0 = 1.75bit/5.95GB, PQ2_0 = **2.13bit/7.21GB**.
> 📌 [[한정어-탈락]]([`(ideal)` 라벨 탈락]) × [[표-부분인용]](4행 중 2행) × [[단위-불일치]](목표값↔출하물)가 **한 셀에서 겹쳤다.**

> [!warning] 🔴 수집기 정정 2 — **"~5.9GB"와 "~47 tok/s"는 서로 다른 파일의 수치다**
> README `Choosing a Packing`: *"**PQ2_0** ... is the pack **measured on Apple Silicon**."*
> 🎯 **즉 M5 Max ~47 tok/s 는 7.21GB PQ2_0 의 값**이고, 5.95GB 는 PTQ1_0 이다. 수집기 한 줄(*"언어 모델 ~5.9GB ... Apple M5 Max에서 ~47 tok/s"*)은 **두 아티팩트의 수치를 한 모델의 스펙처럼 붙였다.**
> 📌 [[단위-불일치]] 의 **양자화 도메인 사례** — 지금까지 이 개념은 파라미터 수(552B↔763B)와 가속 배수 분모([[FastVideo]])에서 나왔다. 여기서는 **같은 레포 안 두 파일**이다.

> [!warning] 🔴 수집기 정정 3 — *"고정밀 예외 없음"* 은 README 문장과 다르다
> README 원문: *"no high-precision escape hatches **behind a low-bit label**"* 이고, 같은 문서가 **예외의 크기를 적는다**: *"**26.2M parameters (0.0976%)** — the recurrent state path of the linear-attention layers, plus the normalization weights — **remain in higher precision and are counted in the 1.72 figure**."*
> ✅ **정확한 진술은 "고정밀 예외가 없다"가 아니라 "고정밀 예외가 0.0976% 있고 그것까지 세어서 1.72다"** 이다. 🎯 **이게 오히려 더 강한 주장인데** 수집기 표현은 약한 쪽으로 틀렸다.

> [!warning] 🔴 그리고 볼트 자신의 v1 페이지가 같은 오류를 갖고 있었다 — **정정한다**
> 볼트 [[Bonsai-27B]](v1, 2026-07-18 작성)는 *"**1.71bit(~7.2GB**, FP16 대비 **9.4배** 축소)"* 라고 적었다.
> 🔴 **이 세 수치는 함께 성립할 수 없다**: 27B × 1.71bit ÷ 8 ≈ **5.8GB**이고 54GB ÷ 5.8GB ≈ **9.3~9.4배**다. **7.2GB로는 7.5배**다.
> ✅ **v2 README가 원인을 설명해 준다**: v1도 **패킹이 둘**이었고(파일 목록에 `PQ2_0`·`Q2_0`·`Q2_g64` 실재), 볼트는 **이상값의 bit/배수**와 **2-bit 슬롯 패킹의 파일 크기**를 **한 줄에 섞어 적었다.** v2의 PQ2_0 이 정확히 **7.21GB** 인 것이 방증이다.
> 📌 **즉 볼트는 14개월 전에 이미 [[표-부분인용]] 을 당했고, 그 사실을 v2가 와서야 알았다.** → [[Bonsai-27B]] 에 정정 반영.

> [!warning] 🔴 **검사가능성이 v1보다 후퇴했다** — 이번 배치의 구조적 발견
> 볼트 파일트리 실측(HF API):
> - **v1** `Ternary-Bonsai-27B-gguf`: `.eval_results/aime_2026.yaml` · `.eval_results/gsm8k.yaml` · `.eval_results/mmmu_pro.yaml` **+ `eval-results` 태그**
> - **v2** `Ternary-Bonsai-2-27B-gguf`: **`.eval_results/` 없음 · `eval-results` 태그 없음**
> 🎯 **같은 벤더가 더 좋은 점수(80.49→84.78 계열)를 주장하면서 기계판독 가능한 평가 산출물을 뺐다.** 근거는 이제 **GitHub의 PDF 화이트페이퍼 한 개**뿐이다.
> 📌 [[검사가능성-공사]] 는 *"여러 생태계가 '확인되지 않음' 칸을 만든다"* 는 수렴이었는데, **이건 반대 방향의 첫 실측 사례**다 → 신설 [[검사가능성-후퇴]]([[Agora]] 와 함께 n=2).

> [!warning] 🔴 실행 전제 — **stock llama.cpp로는 못 돌린다. 그리고 조용히 틀린다.**
> README 원문: *"**Stock llama.cpp will not run these files.** It rejects `PQ2_0` and `PTQ1_0` as unknown types, and **it loads `Q2_0` without any warning and produces garbage**, because it has no Hadamard activation runtime."*
> 🔴 **볼트 [[Bonsai-27B]] 의 07-18 actionable 이 정확히 이 지뢰를 밟는다**: *"llama.cpp/Ollama로 `Ternary-Bonsai-27B-gguf` 받아 8GB급 하드웨어에서 thinking 태스크 실측"* — **v1 파일 목록에 `Q2_0` 이 있으므로 stock llama.cpp가 경고 없이 로드하고 쓰레기를 뱉었을 것**이고, 볼트는 그걸 **모델 품질로 오해했을 것**이다.
> ✅ **실행하지 않아서 틀린 결론을 피했다. 이번엔 실행 전에 알았다.** 필요: `PrismML-Eng/llama.cpp` 포크(CUDA/Metal) · MLX·mlx-swift 포크도 별도.

> [!note] 📌 볼트 실측 (2026-09-20, HF API)
> 다운로드(30일) **1,908,396** — 🔴 수집기 기록 **1,516,960** 대비 **+391,436 (+25.8%)**. **배치 최대 드리프트**이고, 09-16 생성 모델의 30일 창이 아직 차오르는 중이라는 뜻이다.
> 좋아요 **1,315**(수집기 1,310) · base_model `Qwen/Qwen3.8-27B` ✅ · **Apache-2.0** ✅ · created 2026-09-16T23:40 · lastMod 2026-09-17T18:44
> 🎯 **v1이 아직 더 사랑받는다**: v1 좋아요 **1,370** > v2 **1,315**. v1 다운로드도 **662,554**(볼트 07-26 기록 631,970 → +3만).
> 🎯 **벤더가 남의 라벨을 직접 고발한다**: *"a widely-used '2-bit' build of Qwen3.8-27B is really **2.8 bits/weight at 9.4 GB**"* — **[[단위-불일치]] 를 벤더가 경쟁사에 적용한 사례**다. 🔴 그리고 같은 배치 [[Swift-Qwen3.8-27B-GGUF]] 가 **바로 그 IQ2_XXS 계열을 출하한다.**

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐ — ✅ 문서 품질은 배치 최상급(4행 표·패킹별 분리·예외 0.0976% 명시·실행 전제 경고). 🔴 **그러나 모든 성능 수치가 자사 화이트페이퍼 PDF 단일 출처이고 v1에 있던 eval 산출물이 사라졌다.** 제3자 재현 **미확인**.
- **즉시 활용**: **YES, 단 전제 하나.** 5.95GB(PTQ1_0)면 8GB VRAM·노트북에서 27B급이 돈다. 🔴 **반드시 PrismML 포크 바이너리**를 써야 한다 — stock으로는 거부되거나 **조용히 쓰레기**.
- **6개월 영향력**: 🎯 **"라벨 비트수 ≠ 실제 비트수"가 벤더 간 쟁점이 됐다.** 2.8bit를 "2-bit"로 파는 관행을 **경쟁 벤더가 수치로 지적**하면 저비트 표기 규범이 생길 수 있다.
- **대체 관계**: v1([[Bonsai-27B]], Qwen3.6 기반)을 **세대 교체**. IQ2_XXS·UD-Q4_K_XL 계열과 직접 경쟁.
- **허와 실**: 🔴 **걷어내야 할 것은 "1.72bit/5.9GB/9.3배"라는 숫자 묶음 자체다** — 셋 다 `(ideal)` 행에서 왔다. 실제 거래는 **5.95GB@1.75bit(9.0배)** 또는 **7.21GB@2.13bit(7.5배)**.
- **액션**: ① PrismML 포크로 PTQ1_0 실행 ② 🎯 **화이트페이퍼 PDF를 [[docling]] 으로 파싱해 14개 벤치 표를 전사** — 같은 배치 두 항목이 서로를 검증한다.

> [!action] 당장 할 것
> **[[docling]] + Bonsai-2 화이트페이퍼 PDF.** 성공하면 (1) docling 실검증 (2) 사라진 eval 산출물의 대체 (3) 볼트 자기한계 *"그림/표 속 수치 미전사"* 돌파 — **세 개가 한 번에 해결된다.** 이번 배치에서 가장 비용 대비 이득이 큰 실행 항목이다.

> [!question] 미해결 질문
> 1. **왜 v1의 `.eval_results/` 를 뺐는가** — 미확인.
> 2. 84.78의 **14개 벤치 구성** — 화이트페이퍼 PDF 안. 미열람.
> 3. **PTQ1_0 vs PQ2_0 의 품질 차** — README는 속도 차만 말한다. 84.78이 **어느 패킹의 값인지 확인되지 않았다.**

## 관련 페이지
- [[Bonsai-27B]]
- [[Qwen3.8-27B]]
- [[Swift-Qwen3.8-27B-GGUF]]
- [[검사가능성-후퇴]]
- [[단위-불일치]]
- [[표-부분인용]]
- [[한정어-탈락]]
- [[파생저장소-식별]]
- [[docling]]
- [[Prism-ML]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/prism-ml/Ternary-Bonsai-2-27B-gguf
- 볼트 실측(2026-09-20, HF API): 다운로드(30일) **1,908,396**(수집기 1,516,960 · **+25.8%**) · 좋아요 **1,315** · base_model `Qwen/Qwen3.8-27B` · Apache-2.0 · created 2026-09-16T23:40:56Z · lastMod 2026-09-17T18:44:01Z · **파일: F16 · PTQ1_0 · PQ2_0 + mmproj BF16/Q8_0 (총 6, `.eval_results/` 없음)**
- 대조군 v1 실측: `prism-ml/Ternary-Bonsai-27B-gguf` 다운로드 **662,554** · 좋아요 **1,370** · base `Qwen/Qwen3.6-27B` · **`.eval_results/` 3종 + `eval-results` 태그 보유**
- 수치 출처: README **306행 전문 중 상위 150행 실열람**(Memory Requirement 4행 표 · Shipped Components 표 · Choosing a Packing · Quickstart 경고)
- raw 대비: 볼트 추가 = 🔴 **`(ideal)` 라벨 탈락 적발(1.72/5.8GB/9.3배는 출하물 아님)** · 🔴 **5.9GB↔47tok/s 가 서로 다른 패킹** · 🔴 **"고정밀 예외 없음" 정정(0.0976% 존재·포함 계수)** · 🔴 **볼트 v1 페이지 7.2GB↔9.4배 모순 원인 규명 및 정정** · 🔴 **v1 대비 eval 산출물 제거 = [[검사가능성-후퇴]] 사례 1** · 🔴 **stock llama.cpp 무경고 오작동 경고 발굴(v1 actionable 무효화)**
- 신뢰도: ⭐⭐ (문서 품질 최상 · 지표 실측 / **단일 PDF 출처 · eval 산출물 제거 · 제3자 재현 0**)
