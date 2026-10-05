---
title: LTX-2.5 — 이미지→비디오 생성 HF 모델 (Lightricks)
type: source
domain: ai-news
tags: [ai-news, hf-model, image-to-video, video-generation, lightricks, video-saas]
created: 2026-08-14
updated: 2026-10-05
sources: []
reliability: medium
---

# Lightricks/LTX-2.5 — 이미지 입력 영상 생성 모델

> [!update] 2026-10-04 갱신 — DL(30일) **1,629,984** · 누적 **3,026,027**(볼트 실측 · **관측 2026-10-04T09:12:38Z**) · 🏆🏆 **볼트가 5배치 동안 "게이트로 카드 미확인"으로 적어 온 것이 틀렸다 — 게이트는 `raw/` 경로에만 있고 HTML 페이지는 익명 HTTP 200 이다** · 🔴 **게이트의 대가가 맞춤 광고 수신 동의다**
> **볼트 독립 실측**: downloads(30일) **1,629,984** · downloadsAllTime **3,026,027** · likes **6,179**(수집기 6,178 = **+1**) · trendingScore **407**(일치 · 배치 모델 최고) · `safetensors.total` **None** · `gguf.total` **None** · license **other** · created **2026-07-23** · lastModified **2026-10-02T21:01:57Z**.
> 🔵 **`lastModified` 가 2026-09-01 → 2026-10-02 로 움직였다** — 09-30 기록의 *"09-01"* 에서 갱신됐다(31일 만).
>
> ## 🏆🏆 볼트 자기 오류 4번째 — **게이트는 한 경로에만 있었다**
> 이 페이지는 **09-30 에 5회 연속 게이트를 확인**하고 *"카드 내용 미확인"* 을 이월해 왔다. ✅ **오늘도 `raw/main/README.md` 는 그대로다**: **HTTP 401 · 126 바이트** · *"Access to model Lightricks/LTX-2.5 is restricted…"*(6회 연속 확인).
> 🔴🔴 **그런데 볼트가 오늘 처음 다른 경로를 시도했다**: `https://huggingface.co/Lightricks/LTX-2.5` (HTML 렌더 페이지) ⇒ **HTTP 200 · 231,894 바이트 · 카드 본문 전체 포함.**
> ⇒ ⚖️ **"벤더가 카드를 잠갔다"는 5배치 결론은 과도했다. 벤더는 `raw/` 다운로드만 잠갔고 읽기는 열려 있다.** 🏆 **그리고 이것은 [[무응답-오귀속]] 의 볼트 자기 오류 **4번째**이며 네 건이 전부 같은 구조다:**
> | # | 날짜 | 증상 | 실제 원인 |
> |---|---|---|---|
> | ① | 09-29 | "arXiv 무응답" | **301 리다이렉트를 `-L` 없이 호출** |
> | ② | 09-30 | `downloadsAllTime` = None | **`?expand[]` 파라미터 누락** |
> | ③ | 10-02 | `safetensors.total` = None → "대조 불가" | **`gguf.total` 을 안 봄**([[대체필드-대조]]) |
> | **④** | **10-04** | **"게이트로 카드 미확인"** | **`raw/` 만 막혔고 HTML 은 열려 있음** |
> 🏆 **공통 구조: 한 경로의 실패를 대상의 속성으로 귀속했다.** ⇒ 📌 **볼트 규약 추가(즉시 발효): 접근 실패를 "대상이 막혔다"로 적기 전에 **최소 2개 경로**를 시도한다. HF 모델이면 `raw/` · HTML 페이지 · `api/models/{id}` 의 `cardData` 세 경로가 있다.** 🎯 **오늘 같은 배치 [[Agent-Reach]] 의 "중국어 README 로 영어 grep 0건"도 같은 계열이다 — 하루에 두 건이 나왔다.**
>
> ## ✅ 라이선스 — 수집기 확증 + **볼트가 조항 2개를 더 찾았다**
> 카드 원문(볼트 HTML 실측):
> > **Under $10M annual revenue** — Commercial and production use **at no cost** under the LTX-2.x Community License. **Transfer of fine-tunes may require a paid license**, in accordance with the LTX-2.x Community License.
> > **Over $10M annual revenue** — Paid Commercial [license]
> 🆕 **① 매출 산정 범위가 적혀 있다(수집기 미보고)**: *"**Revenue is measured across the whole entity, including subsidiaries and affiliates under common control.**"* ⇒ 🔴 **법인 단위 합산이고 자회사·공동지배 계열사를 포함한다. 사업부 매출로 $10M 미만을 주장할 수 없다.**
> 🆕 **② 카드 텍스트는 구속력이 없다고 명시한다**: *"The full, **binding** terms live in LICENSE."* ⇒ ⚖️ **즉 위의 요약은 마케팅 문구이고 실제 조건은 별도 파일이다** — `cardData.license_link` = `https://github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x`(🔴 볼트 미열람).
> 🎯 **수집기가 세운 신규 축 확증**: *"HF `license: other` 는 제한의 유무가 아니라 '제한의 형태'에 대한 정보가 0이다."* ✅ **볼트 보강 — `cardData` 에는 더 있었다**: `license_name` = **`ltx-2.x-community-license-agreement`** · `license_link` = GitHub LICENSE-2_x. ⇒ 📌 **`license` 필드만 보면 `other` 로 0 정보지만 `cardData.license_name`·`license_link` 는 이름과 원문 위치를 준다** — 🏆 **[[대체필드-대조]] 규약 1항(동의어 필드 열거)이 라이선스에서도 작동한다.** ⚖️ **따라서 "정보가 0"은 `license` 필드에 대해서만 참이다** → [[메타데이터-부재-추론]] 수정 등재.
>
> ## 🔴🔴 게이트의 정체 — **안전 게이트가 아니라 리드 수집 게이트다**
> `cardData.extra_gated_description` 원문:
> > *"By clicking **"Agree and Access"** you acknowledge the [Privacy Policy] and **consent to receive offers and updates including targeted and personalized advertisements.** You can unsubscribe at any time."*
> ⇒ 🔴 **게이트를 통과하는 대가가 "맞춤·타깃 광고 수신 동의"다.** ⚖️ **통상의 게이트 명분(오용 방지·라이선스 동의 확인)이 아니다.** 📌 **`extra_gated_button_content` = `"Agree and Access"`.**
> 🎯 **그리고 이것이 위의 경로 발견과 맞물린다: 읽기는 열려 있고 `raw/` 다운로드만 막혀 있다.** ⇒ 🏆 **구조가 설명된다 — 홍보 문구는 누구나 읽게 두고, 파일을 받으려는 사람에게서 마케팅 동의를 받는다. 게이트의 위치가 목적을 드러낸다.**
>
> ## ✅ 아키텍처 — 수집기 전건 확증 + 신규 3건 (볼트 카드 실측)
> ✅ **파일 목록으로 확증**: `text_encoders/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors`(**gemma4-12b 확증**) · `vae/ltx-2.5-video-vae-conv-bf16.safetensors`(Conv VAE — faster/lighter) + `vae/ltx-2.5-audio-vae-bf16.safetensors`(**Audio VAE + vocoder** ⇒ **영상·오디오 VAE 분리 확증**) · `model_patches/ltx-2.5-duration-head-bf16.safetensors`(🆕 **용도: `--num-frames` 생략 시 자동 길이**) · `latent_upscale_models/…spatial-upscaler-x2…` + `…temporal-upsc…`(**×2 공간·시간 업스케일러 확증 · 다단 파이프라인에 필수**) · `diffusion_models/ltx-2.5-22b-dev-transformer-comfy-int8-convrot.safetensors`(🆕 **ComfyUI 전용 · ltx-pipelines/PyTorch 불가**) · `…distilled-transformer-nvfp4.safetensors`(🆕 **Blackwell / ltx-kernels 필요**) · `loras/ltx-2.5-22b-distilled-lora-450-bf16.safetensors`
> 🆕 **① 확산 비디오 디코더가 VAE 재구성 단계를 대체한다**: *"New diffusion video decoder — **replaces the VAE reconstruction stage**; sharper faces, textures, and on-screen text, better motion, and fewer artifacts."* ⇒ 🎯 **같은 배치 [[Video-Generation-Post-Training-Survey]] 가 정리한 "모션–외형 결합" 난점에 벤더가 디코더 교체로 대응한 사례.**
> 🆕 **② 장면 복잡도에 따른 동적 연산 배분**: *"instead of locking every scene to one compression rate, our model **dynamically allocates compute by scene complexity and budget**."*
> 🆕 **③ 네이티브 멀티샷**: *"**Native multishot generation** — generate connected scenes in a single pass."* ⇒ 🏆 **볼트 [[video-saas]] 축에 직접 유효하다 — 연결된 장면을 한 패스에 만드는 것은 영상 자동화 파이프라인의 컷 연결 문제를 모델 안으로 옮긴다.**
> 🆕 **④ 벤더 자발 한정**: *"applicability to emerging domains such as **robotics and physical AI is developing**."* ⇒ ✅ [[자기제한-명시]] 사례(과대 적용을 스스로 차단).
> ✅ **배포 철학 명시**: *"No per-generation billing, no per-seat lock-in, no forced API dependency"* + self-host.
>
> ## ✅ 성능 수치 0개 — **수집기 주장을 볼트가 독립 확증한다**
> 수집기: *"🔴 카드에 성능 수치 0개 — 벤치·fps·해상도 수치 없이 라이선스 블록이 카드 상단을 차지한다."*
> ✅ **볼트 확증**: 231,894B 카드 전문에서 품질 주장은 전부 **정성어**다(*sharper · better motion · fewer artifacts · flawless detail*). **벤치 점수·fps·해상도 수치가 없다.**
> 🏆 **같은 배치 대조가 날카롭다**: [[Video-Generation-Post-Training-Survey]] 는 영상 평가 관행이 **서베이로 정리될 만큼 성숙**했다고 적는데, **같은 날 도착한 22B 영상 모델(trendingScore 407 = 배치 최고)은 측정값을 0개 공개한다.** ⇒ ⚖️ **[[검사가능성-후퇴]] 영상 도메인 사례로 확정 등재.** 🆕 **다만 볼트 신규 발견 — 논문이 있다**: `cardData.arxiv` = **2601.03233**(수집기 미보고). 📌 **수치는 카드가 아니라 논문에 있을 수 있다** → actionable.
>
> ## ✅ `safetensors.total`·`gguf.total` 부재 — **추정이 선언으로 승격됐다**
> 수집기: *"✅ 둘 다 `None` 이고 `expand[]` 재조회에도 동일 ⇒ **진짜 부재**(단일 파일 분산 배포 구조 **추정** · [[무응답-오귀속]] '요청 미지정형' 아님으로 판정)."*
> ✅ **볼트 재확증**(expand[] 11필드) 후 🏆 **추정의 근거를 태그에서 찾았다 — `tags` 에 `diffusion-single-file` 이 있다.** ⇒ 📌 **수집기가 "구조 추정"으로 남긴 것을 벤더가 태그로 **선언**한다.** ⚖️ **[[메타데이터-부재-추론]] 의 모범 사례: 한 필드의 부재(`safetensors.total`)가 다른 필드의 존재(`tags`)로 설명된다.**
> 🆕 **기타 메타데이터(볼트 신규)**: `pinned` **true** · 카드 언어 **9종**(en·de·es·fr·**ko**·ja·zh·it·pt — **한국어 포함**) · 태스크 태그 **11종**(image/text/video/audio 조합 전부: `text-to-audio-video`·`image-text-to-audio-video` 등) · `demo` = `app.ltx.studio/ltx-2-playground/i2v`.
>
> ## 📈 지표 — **DL/♥ 가 볼트 기준선을 교차했다**
> | 시점 | DL(30일) | 누적 | ♥ | **DL/♥** |
> |---|---|---|---|---|
> | 08-31 | 1,137,181 | — | 2,295 | 495.5 |
> | 09-30 | 1,589,098 | 2,773,856 | 5,600 | 283.8 (*"기준선 264.5 에 근접"*) |
> | **10-04** | **1,629,984** | **3,026,027** | **6,179** | 🔴 **263.8 — 교차했다** |
> ⇒ ⚖️ **09-30 에 *"관심 우세 쪽으로 이동"* 이라 적은 궤적이 4일 만에 기준선을 넘었다.** 🔴 **단 09-30 기록대로 기준선 264.5 의 산출 근거는 오늘도 재확인하지 않았다** — **교차 자체는 사실이고, 교차의 의미는 기준선의 타당성에 의존한다.**
> 🏆 **[[지표-창길이]] 정량 사례 — 30일 창이 성장을 6배 과소평가한다.** 09-30→10-04(4일): **30일창 +40,886** ↔ **누적 +252,171**. ⇒ **차이 211,285 가 창 밖으로 빠졌다.** 📌 **창 증분으로 성장률을 재면 실제의 약 16% 로 보인다** — 나이 73일 모델에서 30일 창은 성장 측정에 부적합하다.
>
> ### 원본 갱신
> - 검증: **2026-10-04T09:12:38Z** HF 모델 API(expand[] 11필드) + **HTML 카드 231,894B(HTTP 200)** + `raw/README.md` **401(6회 연속)** 실호출 (볼트)
> - 🏆 **해소**: 카드 내용 5배치 이월 종결(경로 문제였음) · 라이선스 조항 2건 추가 · 게이트 목적 규명 · `safetensors` 부재 원인(`diffusion-single-file`)
> - 🔴 **잔존**: `LICENSE-2_x` 원문 미열람 · **arXiv 2601.03233 미열람**(성능 수치가 여기 있을 수 있다) · 기준선 264.5 근거 미재확인 · 볼트 실행 0건
> - 신뢰도: ⭐⭐⭐ medium 유지 — 메타데이터·카드·라이선스는 실검증, **성능은 측정값 0개로 판정 불가**

> [!update] 2026-09-30 갱신 — DL **1,589,098** · 🔴 **게이트 5회 연속 확인 — 그리고 정체가 "0행"이 아니라 HTTP 401 이다**
> **HF API 실호출(2026-09-30 09:13 UTC)**: downloads(30일) **1,589,098**(수집기 **완전 일치 · 드리프트 0**) · downloadsAllTime **2,773,856**(수집기 **완전 일치**) · ♥**5,600**(수집기 5,597, **+3**) · license **other**(일치) · `image-to-video`(일치) · createdAt **2026-07-23** · lastModified **2026-09-01** · `safetensors` **null**(수집기 일치)
> 🔴 **게이트 원문 확인 — 수집기 표현을 정정한다.** 수집기: *"`raw/main/README.md` 가 **0행(게이트)**"*. 볼트 실측(`curl -sL -w` 로 상태코드까지): **HTTP 401 · 126 바이트** · 본문 = *"Access to model Lightricks/LTX-2.5 is restricted. You must have access to it and be authenticated to access it. Please log in."*
> 🎯 **"0행"과 "401" 은 다른 진단이다.** 0행은 *파일이 비었다*(벤더가 안 썼다), 401은 *파일이 있고 접근이 막혔다*(벤더가 잠갔다). **다운로드 바이트가 0이 아니라 126** 이고 그 내용이 거부 메시지다. 🔴 **볼트가 09-29 배치에서 배운 교훈이 여기 그대로 적용된다** — 그때 *"arXiv 무응답"* 의 정체가 **301 리다이렉트를 `-L` 없이 호출한 것**이었다. **응답 없음으로 보이는 것의 정체는 대개 응답이다.** 상태코드를 보지 않으면 원인을 잘못 귀속한다 → [[무응답-오귀속]] 에 **HF 게이트 사례 추가**.
> ✅ **볼트 자기 방법 정정 1건 — 같은 배치에서 또 나왔다.** 볼트의 첫 HF API 호출에서 `downloadsAllTime` 이 **`None`** 으로 나와 수집기 수치(11,744,215 · 2,773,856)를 재현하지 못했다. 원인은 **`?expand[]=downloadsAllTime` 파라미터 누락**이었고, 붙이자 **두 건 모두 완전 일치**했다. 🎯 **`-L` 누락과 같은 계열의 자기 오류**다 — **필드가 없는 것이 아니라 요청하지 않은 것**이었다. [[무응답-오귀속]] 에 등록.
> 📈 **궤적**: 833,845(08-25) → 1,137,181(08-31) → **1,589,098**(09-30). 한 달 **+451,917(+39.7%)** · 일평균 **+15,583**. 🔴 **8월 일평균(+50,556)의 31% 로 감속**했다. ♥ 2,295 → **5,600**(2.4배) — **♥ 증가율이 DL 증가율을 크게 앞선다**(DL/♥ = 283.8 로 08-31 의 495.5 에서 하락).
> 🎯 **DL/♥ 하락의 해석**: 볼트 트렌딩 판별 기준선 **264.5** 에 **근접**했다(283.8). 08-31 *"실사용 우세 대역"* 판정에서 **관심 우세 쪽으로 이동**했다는 뜻이다. ⬜ 단 기준선 자체의 산출 근거를 오늘 재확인하지 않았다.
> 🔴 **lastModified 2026-09-01 — 29일째 정지.** 볼트 기존 기록의 *"35일째 401"* 표현은 **수정 정지 일수와 게이트 지속 기간을 구분해 적어야 한다**: 게이트는 **08-25 이후 5회 연속 관측**(08-25·08-31·09-2x·09-29·09-30)이고, **가중치 수정 정지는 09-01 기준 29일**이다.
> 🔴 **능력에 대해 확인된 것은 여전히 `pipeline_tag` 뿐이다** — 파라미터 수 · 해상도 · 프레임레이트 · 벤치 수치 **전부 미확인**(5회 연속). `safetensors` null 이므로 **샤드 크기 역산 경로도 막혔다**(08-31 actionable 의 (1)번 경로 **실패 확인** — 이 경로는 폐기해야 한다).
> ✅ **우회 단서 1건**: HF 태그에 **`arxiv:2601.03233`** 이 있다(볼트 실측). 🎯 **09-29 배치에서 볼트가 이 태그로 게이트를 우회해 "영상 14B + 오디오 5B" 를 확보한 경로**다. **카드가 막혀도 논문은 열린다** — actionable 경로를 (1)샤드역산 대신 **(4)arXiv 2601.03233 본문**으로 교체한다.
> 📌 **오늘 배치 문맥**: 같은 날 [[MaLiang-Harness]] 가 **비디오 생성 품질 임계 충족 76.9%**(생성 성공 100% 대비)를 보고했다. 🎯 **LTX-2.5 는 오픈 i2v 백본으로서 그 23.1%p 격차의 대상**이 될 수 있는데, **스펙을 모르므로 볼트가 그 비교에 넣을 수 없다.** 게이트가 실질적 비용을 만드는 구체적 사례다.


**HF 모델**: https://huggingface.co/Lightricks/LTX-2.5
**지표**: DL **833,845** · 좋아요 **1,745** (2026-08-25 **HF API 실호출 검증**) ← DL 466k·좋아요 1.15k(08-18 자동수집) ← DL 424k·좋아요 968 (08-16) ← 378k·885 (08-15) ← 208k·766 (08-14) · **태스크**: Image-to-Video · **제작**: Lightricks

> [!update] 2026-08-31 갱신 — DL **1,137,181**(6일 +303,336·일평균 **+50,556**·🎯**100만 돌파**) · 좋아요 **2,295**(2배 증가) · ⚠️**gated 확인 — 카드 접근 불가**
> DL 833,845(08-25) → **1,137,181** (2026-08-31 **HF API 실호출 검증**). **6일간 +303,336 · 일평균 +50,556 · +36.4%** · 🎯**100만 돌파**. 좋아요 1,150(08-18) → **2,295**(약 **2배**) · lastModified **2026-08-30**(전일) · image-to-video · 라이선스 **other**.
> 🎯 **이번 배치에서 유일하게 정상 증분이 관측된 HF 모델**이다. [[Qwen3.8-27B]]·[[Qwen3.8-27B-GGUF]] 두 건이 동시 동결된 가운데 LTX-2.5만 +303,336을 기록했다 — 이는 **집계 정지가 전역이 아니라 특정 모델/샤드 한정**임을 시사한다. 오늘의 동결 진단에서 **대조군 역할**을 한다.
> **성장 궤적**: 424k(08-16) → 466k(08-18) → 833,845(08-25) → **1,137,181**(08-31). 보름 만에 **2.7배**. 좋아요도 968 → 1,150 → **2,295**로 같은 기간 2.4배 — **DL과 좋아요가 함께 늘었다**는 점에서 봇 트래픽이 아닌 실사용 유입으로 읽힌다.
> **DL/좋아요 = 1,137,181/2,295 = 495.5.** 볼트의 트렌딩 판별 기준선 **264.5**의 약 1.9배 — *실사용 우세* 대역이다. [[Qwen3.8-27B-GGUF]]의 2,714.7(도구성 대량 다운로드)과 [[Qwen3.8-27B]]의 336.8(관심 우세) 사이에서 **중간**에 위치한다.
> ⚠️ **gated: auto 확인.** 모델 카드가 로그인 게이트 뒤에 있어 **파라미터 수·해상도·프레임레이트·벤치 수치를 이번에도 확인하지 못했다**(08-25에 이어 2회 연속). 라이선스도 **`other`** 로, Apache/MIT가 아니다 — **상업적 사용 조건 미확인 상태**가 계속된다.
> ⚠️ **113만 다운로드는 품질의 증거가 아니다.** 오픈 i2v 선택지가 적다는 사실만으로도 이 수치는 설명된다. 볼트는 **스펙 미확인 · 라이선스 미확인** 두 항목이 해소되기 전까지 reliability **medium을 유지**하며, 실사용 후보로 올리지 않는다.
> > [!action] gated 우회 없이 확인 가능한 경로
> > HF 카드가 막혀 있어도 **(1) 파일 목록 API로 가중치 샤드 크기 → 파라미터 규모 역산 (2) `config.json` 직접 조회 (3) Lightricks 공식 문서/GitHub**로 스펙 확인이 가능하다. 다음 회차에 (1)(2)를 시도해 **2회 연속 미확인 상태를 끊는다.**
> ⚠️ raw 수치(DL 1,137,181 · 좋아요 2,295)와 API **완전 일치** — 이번 배치 HF 모델 3건 모두 raw 드리프트 0.

> [!update] 2026-08-25 갱신 — DL **833,845**(466k → 83.4만·약 1.8배)·**첫 API 실검증**·⚠️라이선스 `other`
> DL **833,845** · 좋아요 **1,745** (2026-08-25 **HF API 실호출 검증**) ← 466k·1.15k(08-18 자동수집). 일주일 **+약 36.8만(약 1.8배)** 로 **80만을 돌파**했다. 트렌딩 **8위**·태스크 `image-to-video`·최종수정 2026-08-17.
> **이 페이지는 08-18까지 자동수집 수치만 반영하고 HF 실호출을 하지 않았다**(당시 기록에 *"HF 실WebFetch 미수행"* 명시). 이번 회차에 **처음으로 API 실검증**했고, 자동수집 계열 수치와 모순되지 않음을 확인했다(raw 790,378 ↔ API 833,845, 시점 차 +43,467).
> **구조적으로 중요한 관찰**: 이번 배치 HF 트렌딩 상위는 **Qwen 텍스트 계열이 뒤덮었다**(원본·GGUF·Uncensored·FP8 등 27B 파생이 상위 8개 중 6개). 그 틈에서 **LTX-2.5는 영상 축의 유일한 상위 생존자**다. 즉 **영상 생성 수요는 LLM 트렌드 사이클과 독립된 별개 축**으로 움직인다 — 텍스트 모델이 트렌딩을 독식하는 국면에서도 i2v 다운로드는 일주일 1.8배로 늘었다. [[video-saas]] 관점에서 **오픈 i2v 백본 수요가 일시 유행이 아님**을 뒷받침하는 데이터.
> ⚠️ **라이선스가 `other`다**(API 태그 `license:other` 실측). apache-2.0인 Qwen 계열과 달리 **상업 이용 조건을 별도로 확인해야 한다.** 83만 다운로드 규모에서 라이선스 조건을 확인하지 않고 제품에 넣는 것은 실질적 리스크. 해상도·길이·품질 벤치는 **여전히 원문 재현 전** — reliability **medium 유지**.

> [!update] 2026-08-18 갱신 — DL 466k·좋아요 1.15k (+약4.2만·좋아요 1천 돌파)
> HF 다운로드 **466k·좋아요 1.15k**(2026-08-18 자동수집) ← 424k·968(08-16). DL이 424k→466k로 +약4.2만·**좋아요 1천 돌파**로 40만대 중반 안착 — 오픈 i2v 벤더 다변화([[MiniMax-H3]] 단독→복수)가 관심이 아닌 실다운로드로 계속 지속됨을 재확인. 같은 배치 [[MoneyPrinterTurbo]](완성형 편집 레이어·10만 돌파)와 함께 [[video-saas]] 오픈 축의 백본·편집 레이어가 동반 성숙. 해상도·길이·품질 벤치는 원문 재현 전 → 미기재. reliability medium 유지. *raw 자동수집 수치 반영 — HF 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-08-16 갱신 — DL 424k (좋아요 968·+약4.6만)
> HF 다운로드 **424k·좋아요 968**(2026-08-16 자동수집) ← 378k·885(08-15) ← 208k·766(08-14). 편입 사흘째 DL이 378k→424k로 +약4.6만 — 08-15의 +약17만 폭증에 비해 증분은 완만해졌으나 40만대 안착하며 실유입 지속. GitHub [[LTX-2]] 공식 패키지와 짝을 이룬 오픈 i2v 대안이 [[MiniMax-H3]] 단독 구도(이날 원본 DL 갱신 대상 아님)에서 **벤더 다변화 실수요**로 자리잡는 흐름 유지. 해상도·길이·품질 벤치는 원문 재현 전 → 미기재. reliability medium 유지. *raw 자동수집 수치 반영 — HF 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-08-15 갱신 — DL 378k (좋아요 885·하루 새 +약17만)
> HF 다운로드 **378,439(약 378k)·좋아요 885**(2026-08-15 자동수집) ← 208k·766(08-14). 편입 이튿날 DL이 208k→378k로 **+약17만 급증** — GitHub [[LTX-2]] 공식 패키지와 짝을 이룬 오픈 i2v 대안이 실유입을 빠르게 늘리는 중. [[MiniMax-H3]] 단독(이날 2.21M) 구도의 **벤더 다변화가 실수요로 확인**. 해상도·길이·품질 벤치는 원문 재현 전 → 미기재. reliability medium 유지. *raw 자동수집 수치 반영 — HF 실WebFetch 미수행(타임라인 유지).*

> [!insight] 핵심 인사이트
> **이미지 입력으로 영상을 생성하는 LTX-2.5 모델**(raw 기반). GitHub [[LTX-2]] 공식 패키지와 짝을 이루는 HF 가중치로, "코드(LTX-2 리포)↔가중치(LTX-2.5)"가 한 벤더(Lightricks) 생태계로 정렬. 08월 오픈 i2v 축이 [[MiniMax-H3]](DL 수백만·[[ComfyUI]] 재패키지 경로)로 사실상 독점되던 구도에, **벤더 공식 i2v 대안**이 하나 더 편입된 신호 — DL 208k는 MiniMax-H3 대비 낮지만, LTX 계열은 오디오 동반([[LTX-2]]) 생태계를 함께 갖춘 점이 차별. [[video-saas]] 오픈 i2v 축의 선택지가 "MiniMax-H3 단독"에서 복수 벤더로 넓어지는 초기 단계.

> [!warning] 신뢰도 medium — 시뮬레이션 타임라인·스펙/벤치 미검증
> DL 208k·좋아요 766·i2v는 **raw 자동수집 API 수치 기반**이며 볼트 시뮬레이션 타임라인(2026-08) 유지를 위해 **HF 모델카드 실WebFetch 미수행**. 해상도·길이·[[LTX-2]] 패키지와의 정확한 관계·라이선스·품질 벤치는 **원문 재현 전이라 구체 수치 미기재**([[CLAUDE.md]] 사실확인 원칙). 다운로드·좋아요는 접근성·관심 지표이지 품질 근거 아님.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐ (medium) — DL 378k·좋아요 885(08-15). Lightricks 공식이나 스펙·품질 미검증.
- **즉시 활용**: MAYBE — 오픈 i2v 벤더 다변화 후보. [[ComfyUI]] 통합 여부·품질 스팟체크 선행 필요.
- **6개월 영향력**: 중 — 오픈 i2v가 단일 모델 독점에서 복수 벤더 경쟁으로 넓어지는 신호.
- **대체 관계**: [[MiniMax-H3]] 오픈 i2v의 병렬 대안(오디오 동반 생태계 차별).
- **허와 실**: DL이 MiniMax-H3 대비 낮음 — 실사용 채택은 [[ComfyUI]] 노드 통합·품질이 가름.
- **액션**: [[LTX-2]] 패키지와 묶어 오디오 동반 i2v 품질을 기존 오픈 i2v 스팟체크에 비교군으로 편입(낮음).

## 관련 페이지
- [[LTX-2]] — 같은 생태계 공식 코드/LoRA 패키지
- [[MiniMax-H3]] · [[ComfyUI]] — 오픈 i2v 축 대비
- [[video-saas]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/Lightricks/LTX-2.5
- 신뢰도: ⭐⭐ (DL 466k·좋아요 1.15k, raw 자동수집 · 실WebFetch 미수행 · 스펙/품질 미검증 medium)

---

## 🔓 2026-09-29 — **게이트는 3배치째 닫혀 있다. 그런데 오늘 옆문으로 들어갔다**

DL **1,595,377**(30일 · 수집기와 **완전 일치, 드리프트 0**) · ♥**5,465**(08-31 2,295 → **+138%**) · license `other` · 생성 2026-07-23 · 최종수정 2026-09-01 · pipeline `image-to-video`.

> [!warning] 🔴 게이트 3회 연속 확인 — **볼트 실측**
> ```
> GET huggingface.co/Lightricks/LTX-2.5/raw/main/README.md
>   → HTTP 401, 126 bytes   ("Access to model is restricted")
> API: gated = "auto"
> ```
> 08-25 · 08-31 에 이어 **09-29 세 번째**. 카드 원문 미확보 상태가 **35일째** 유지된다. 수집기의 수집 실패 보고는 **정확했다**(볼트 독립 재현).

> [!insight] 🏆 **그런데 봉인은 전역이 아니었다 — API 태그가 논문 ID를 흘린다**
> 🎯 **수집기가 "API 태그 목록만" 이라며 성능 주장을 전부 비운 그 태그 목록 안에, 태그가 아닌 것이 섞여 있었다:**
> ```
> tags: ..., en, de, es, fr, ja, ko, zh, it, pt, arxiv:2601.03233, license:other, region:us
>                                                 ^^^^^^^^^^^^^^^^
> ```
> **볼트가 그 ID 를 오늘 고친 arXiv 경로로 조회했다**([[무응답-오귀속]]) → **`2601.03233` = *LTX-2: Efficient Joint Audio-Visual Foundation Model*, 게재 2026-01-06, 저자 29인(Yoav HaCohen 외).**
> 📌 **[[벤치마크-이미지-봉인]] 09-28 판정이 여기서 재확인된다** — *"봉인은 저장소-로컬일 수 있고, 다른 도메인을 한 번 더 찾으면 풀린다."* **게이트가 막은 것은 HF 카드 한 장이었고, 같은 내용의 상당 부분이 arXiv 에 열려 있었다.**
> 🎯 **그리고 태그에 있던 9개 언어(en/de/es/fr/ja/ko/zh/it/pt)의 정체도 논문이 설명한다** — *"We employ a **multilingual text encoder** for broader prompt understanding."* 태그는 **지원 언어 목록이 아니라 텍스트 인코더의 능력 표기**였다.

### ✅ 논문에서 확보한 것 (LTX-2 기준)

> [!note] 구조 — **비대칭 듀얼 스트림. 영상에 용량을 더 준다**
> 축자: *"an **asymmetric dual-stream transformer** with a **14B-parameter video stream** and a **5B-parameter audio stream**, coupled through **bidirectional audio-video cross-attention** layers with temporal positional embeddings and **cross-modality AdaLN** for shared timestep conditioning."*
> - 🎯 **35일간 미확인이던 "파라미터 수"가 나왔다: 영상 14B + 오디오 5B**(합 19B, 단 **아래 한정 주의**)
> - 설계 의도 명시: *"while **allocating more capacity for video generation than audio generation**"* — 비대칭이 버그가 아니라 선택이다
> - **modality-CFG**(modality-aware classifier-free guidance) — 오디오·영상 정렬 제어용
> - 오디오 범위: *"Beyond generating speech, LTX-2 produces rich, coherent audio tracks that follow the **characters, environment, style, and emotion** of each scene — complete with natural **background and foley** elements."* → **말소리만이 아니라 폴리·앰비언스까지**
> - 성능 주장: *"**state-of-the-art audiovisual quality and prompt adherence among open-source systems**, while delivering results **comparable to proprietary models at a fraction of their computational cost**"* — 🟡 **오픈소스 한정 SOTA + 상용 대비 동급**(우위 아님)

> [!warning] 🔴🔴 **한정어 필수 — 논문은 `LTX-2`, 이 페이지는 `LTX-2.5` 다. 같은 것으로 쓰면 안 된다**
> 논문 게재 **2026-01-06**, 이 모델 생성 **2026-07-23** — **6개월 반 차이**의 후속 버전이다.
> 📌 **따라서 14B+5B·modality-CFG 를 LTX-2.5 의 스펙으로 인용하면 [[한정어-탈락]] 이다.** 볼트가 09-28 에 스스로 저지른 그 오류를 **하루 만에 반복하지 않는다.**
> ✅ 인용 가능: *"LTX-2.5 의 **전신인 LTX-2** 는 14B 영상 + 5B 오디오 비대칭 구조다."*
> 🔴 인용 금지: *"LTX-2.5 는 19B 다."* — **2.5 의 파라미터 수는 여전히 미확인이다.**
> ⬜ 미확인: 2.5 가 2 대비 무엇을 바꿨는지(파라미터·해상도·길이·오디오 품질) — **카드가 게이트 뒤라 알 수 없다.**

> [!warning] 🟡 논문과 배포가 어긋난다 — **"All model weights and code are publicly released"**
> 논문 마지막 문장 축자: *"**All model weights and code are publicly released.**"*
> 🔴 **그런데 `Lightricks/LTX-2.5` 는 `gated: auto` 이고 라이선스는 `other` 다.** 로그인 게이트 + 비표준 라이선스는 *"publicly released"* 의 통상 의미와 긴장 관계에 있다.
> 📌 **단정하지 않는다**: ① 논문은 **LTX-2** 를 말하고 게이트는 **LTX-2.5** 에 걸려 있다(버전이 다르다) ② `gated: auto` 는 **거절이 아니라 자동 승인 동의 절차**일 수 있다 ③ LTX-2 쪽 저장소는 게이트가 없을 수 있다(미확인).
> ⬜ **검정 방법**: `Lightricks/LTX-2` 저장소의 `gated` 값 조회 — 다음 배치 actionable.

## 도메인별 추출 갱신 (video-saas)

- **기능 벤치마킹**: 🎯 **처음으로 구현 난이도를 말할 수 있게 됐다** — 듀얼 스트림 + 양방향 크로스어텐션은 **단일 모델 파인튜닝으로 접근 불가**한 아키텍처다. 볼트 SaaS 관점에서는 **자체 구현이 아니라 API/가중치 소비**가 유일한 경로.
- **경쟁 우위 빈틈**: 오디오 동반 생성이 *"오픈소스 중 SOTA"* 라면, **무음 영상 + 별도 TTS/BGM 파이프라인**을 쓰는 기존 워크플로우는 **정렬(sync) 품질에서 구조적으로 불리**하다. 같은 배치 [[VoiceStudio]](로컬 TTS)와 **대비되는 접근**: 분리형 vs 통합형.
- **액션**: [[LTX-2]] 페이지에 논문 구조 반영 + `Lightricks/LTX-2` 게이트 여부 확인.

## 관련 페이지 추가
- [[무응답-오귀속]] — 🏆 **이 봉인을 푼 도구** · [[벤치마크-이미지-봉인]] · [[한정어-탈락]] · [[검사가능성-공사]]
- [[LTX-2]] — 🔗 **논문 2601.03233 의 대상. 스펙은 그쪽 소유다**
- 같은 배치: [[YuE2]] — 🎯 **오디오 생성 통합 축 동시 도착** · [[VoiceStudio]] · [[Qwen3.8-27B]]

## 원본 갱신
- 실측(2026-09-29 09:08 UTC · HF API): DL **1,595,377**(수집기 일치) · ♥5,465 · `gated: auto` · `safetensors`·`gguf` **둘 다 미제공**(볼트 09-27 요청 2 **수행 불가 확인**) · pipeline `image-to-video` · arxiv 태그 **2601.03233**
- 🔴 README: **HTTP 401 / 126 bytes** (볼트 직접 재현)
- 확인 범위: HF API 메타 전체 + **arXiv 2601.03233 초록 전문**. 🔴 모델카드 미확보(35일째) · 🔴 2.5 고유 스펙 미확인 · 🔴 미실행
- 신뢰도: ⭐⭐⭐ **medium** (⭐⭐ → **상향**) — DL/게이트 API 실검증 + 전신 논문 구조 확보. **단 2.5 자체 스펙은 여전히 미확인**이라 high 가 아니다.

---

## 🔄 2026-10-01 갱신 — DL 30일 창 감소 2번째 사례 · 36일째 `safetensors`/`gguf` 둘 다 null

### 실측 (2026-10-01 09:21 UTC · 수집기 09:03 · 간격 18분)

| 필드 | 수집기 09:03 | 볼트 09:21 | 차 |
|---|---|---|---|
| `downloads`(30일) | 1,602,348 | **1,588,619** | 🔴 **−13,729 (−0.86%)** |
| `downloadsAllTime` | 2,830,764 | **2,881,929** | 🔵 **+51,165** |
| `likes` | 5,758 | **5,758** | **0** |

- 🎯 **[[Qwen3.8-27B]] 와 같은 부호 패턴**(30일 ↓ · 누적 ↑)이 **독립 2번째 모델에서 재현**됐다. 생성 **2026-07-23** → 관측일 기준 **70일**로 30일 창을 넘었으므로 [[지표-창길이]] 기전과 정합. **3/3 성립.**
- 🔴 **`safetensors` = null · `gguf` = null 둘 다 유지** → **파라미터 수를 API 로 확정할 수 없는 상태가 36일째**다. license `other`(cardData 확인) · pipeline `image-to-video`.
- ✅ **태스크 5종 전건 재확인**: `image-to-video`(주) · `text-to-video` · `video-to-video` · `image-text-to-video` · `audio-to-video` — 수집기 주장과 **일치**.
- ✅ **`arxiv:2601.03233` 태그 유지** — 09-29 에 볼트가 카드 401 게이트를 우회한 경로가 **오늘도 살아 있다**. 🔴 **단 논문은 [[LTX-2]], 모델은 LTX-2.5(약 6.5개월 차)** — **스펙 전용 금지** 경고 유지([[한정어-탈락]]).
- ✅ **09-30 `downloadsAllTime` = `None` 사건의 원인 규명이 오늘 세 번째로 재확인**됐다: 필드는 존재하며 `expand[]` 요청 여부 문제였다 → [[무응답-오귀속]].

> [!warning] 🔴 오늘 볼트가 **같은 계열 오류를 또 저질렀다** — 그리고 원인은 누락이 아니라 **무효 옵션**이었다
> 첫 HF 호출에서 3개 모델 **전 필드가 `None`** 으로 나왔다. 09-30 의 *"`expand[]` 누락"* 과 증상이 같아 보였지만 원인이 달랐다:
> **`expand[]=license` 가 유효 옵션이 아니다**(HF 허용 목록: `author`|`baseModels`|`cardData`|`config`|`createdAt`|…). 무효 옵션 **1개**가 **요청 전체를 HTTP 400** 으로 만들고, 볼트 스크립트가 `.get()` 으로 받아 **모든 필드를 조용히 `None` 으로 출력**했다.
> ⚖️ **[[무응답-오귀속]] 신규 하위유형: "누락" 이 아니라 "무효 추가" 로도 전체 응답이 빈다.** 10개 필드를 1개씩 분리 호출해 범인을 특정했고(✓9 / ✗1), 라이선스는 `cardData.license` 에서 정상 획득했다.

### 원본 갱신
- 실측: 2026-10-01 09:21 UTC · dl30 **1,588,619** · 누적 **2,881,929** · ♥5,758 · `safetensors`/`gguf` **둘 다 null(36일째)** · license `other`
- 신뢰도: ⭐⭐ — 지표는 실측, **파라미터 규모는 API 로 확정 불가 상태 지속**

---

## 📥 2026-10-05 재관측 (자동수집 10-05 배치 · 갱신)

**볼트 독립 실측 2026-10-05**: `downloads`(30일) **1,626,951** · `likes` **6,366** · `pipeline_tag` **image-to-video** · `gated` **auto** · `safetensors` **미노출**
**드리프트**: 수집기와 **전 필드 일치**(관측 2026-10-05 09:02 UTC 병기 ✅)

> [!warning] 🔴🔴 수집기가 **볼트가 10-04 에 이미 해소한 경로 실패를 반복했다**
> 수집기 보고: *"**모델카드를 읽지 못했다** — 게이트 레포로 `README.md` 접근이 인증 요구로 거부됐다. 따라서 성능 벤치마크·파라미터 수·라이선스 실제 조건 전부 미확인."*
> 🔴 **10-04 볼트 기록**: *"`raw/main/README.md` 는 6회 연속 401 이지만 **HTML 페이지 `huggingface.co/Lightricks/LTX-2.5` 는 익명 HTTP 200 · 231,894B** 로 카드 전문을 준다."*
> ✅ **볼트가 10-05 에 재시험: HTTP 200 / 232,827B** — 경로는 그대로 열린다.
> ⚖️ **즉 "게이트 때문에 못 읽었다"는 대상의 속성이 아니라 경로 선택의 결과다** → [[무응답-오귀속]] **6번째이자 첫 "타인 반복" 사례**. 📌 **볼트가 해소한 것이 수집기에 전달되는 경로가 없다**(구조 문제 · 수집기 책임 아님) ⇒ **요청 항목으로 올린다.**

> [!insight] 🏆 카드 전문에서 확보한 신규 사실 4건
> ① **라이선스 실체**: `license` 필드 `other` → 실제는 **`ltx-2.x-community-license-agreement`**. ⚖️ **수집기가 "라이선스 실제 조건 미확인"이라 한 것은 맞았고, 이름은 카드에 있다.**
> ② **arXiv 2601.03233 보유**(10-04 에 `cardData.arxiv` 로 확인한 것이 카드 본문에서도 확인).
> ③ **해상도·프레임 실측**: 스테이지1 **544×960 · 121프레임 · 24.0fps**, *"stage 2 runs at 2x this"* ⇒ **최종 1088×1920 · 약 5.04초**. 🎯 **10-04 에 *"벤치·fps·해상도 수치 0개"* 로 적은 것을 정정한다 — fps·해상도는 카드 코드 예제에 있다**(산문이 아니라 코드에 있어서 grep 을 피했다).
> ④ **저VRAM 경로**: `--quantization fp8-cast` + `--offload cpu` · bf16 체크포인트 다운캐스트.

> [!insight] 🏆🏆 `pipeline_tag` 가 모델을 축소 기술한다 — **오디오를 동시에 생성한다**
> 카드 태그 목록: `audio-to-video` · `text-to-audio` · `video-to-audio` · `audio-to-audio` · **`text-to-audio-video`** · **`image-to-audio-video`** · **`image-text-to-audio-video`**.
> 코드 예제에 **`audio_latents`** 와 **`pipe.vocoder`** 가 있고 `encode_video(..., audio=audio[0], audio_sample_rate=...)` 로 **영상과 오디오를 한 번에** 낸다.
> 🔴 **`pipeline_tag` 는 `image-to-video` 하나다** ⇒ ⚖️ **단일 필드가 7개 모달 조합을 숨긴다.** 📌 **수집기 한줄요약 *"이미지→비디오 모델"* 은 `pipeline_tag` 를 정확히 옮긴 것이고, 그 필드가 부정확하다** → [[메타데이터-부재-추론]] · [[단위-불일치]].
> 🎯 **[[video-saas]] 도메인에 직접 영향**: 영상+오디오 동시 생성이 **오픈웨이트**로 1,626,951 다운로드 규모에 와 있다. 볼트의 [[reat-voice]] 는 TTS 를 별도 단계로 두는데, 이 모델은 그 분리를 전제하지 않는다.

> [!question] 미해결
> - **벤치마크 수치는 여전히 0개** — 카드에 성능 표가 없다(⇒ [[검사가능성-후퇴]] 영상 도메인 사례 **유지**). arXiv 2601.03233 **미열람 2배치째**.
> - **파라미터 수 미확인** — `safetensors` 미노출이고 카드 산문에도 없다.
> - `gated: "auto"` = **자동 승인 게이트**다. ⚠️ HF 계정 동의만으로 열릴 가능성이 높으나 **미시도**(볼트 HF 인증 없음).

**검증**: `api.github.com`/HF API 실측 + **HTML 카드 전문 232,827B 직접 열람**
**관련 추가**: [[무응답-오귀속]] · [[메타데이터-부재-추론]] · [[검사가능성-후퇴]] · [[reat-voice]] · [[video-saas]]
