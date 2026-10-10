---
title: Lightricks
type: entity
domain: video-saas
tags: [기업, HuggingFace, 영상생성, 오디오생성, gated, 이스라엘]
created: 2026-09-29
updated: 2026-10-10
sources: [LTX-2.5.md, LTX-2.md]
reliability: medium
---

# Lightricks

> [!update] 2026-10-04 갱신 — 🏆🏆 **[[LTX-2.5]] 카드를 볼트가 처음 읽었다(5배치 "게이트" 결론은 경로 오류였다)** · 🔴 **게이트의 대가가 맞춤 광고 동의다**
> **볼트 실측(2026-10-04T09:12:38Z)**: `Lightricks/LTX-2.5` DL(30일) **1,629,984** · 누적 **3,026,027** · likes **6,179** · trendingScore **407**(배치 모델 최고) · license **other** · lastModified **2026-10-02**(09-01 → 갱신됨).
> 🔴🔴 **볼트 자기 오류 정정**: `raw/main/README.md` 는 **6회 연속 HTTP 401**(126B)이지만 **`https://huggingface.co/Lightricks/LTX-2.5` HTML 페이지는 익명 HTTP 200 · 231,894B 로 카드 본문 전체를 준다.** ⇒ ⚖️ **벤더는 `raw/` 다운로드만 잠갔고 읽기는 열어 뒀다. "벤더가 카드를 잠갔다"는 5배치 결론이 과도했다** → [[무응답-오귀속]] ④경로형.
>
> ## 🔴 라이선스 — **이 벤더의 사업 모델이 드러난다**
> **LTX-2.x Community License** (`cardData.license_name` = `ltx-2.x-community-license-agreement` · 원문 `github.com/Lightricks/LTX-2/blob/main/LICENSE-2_x`):
> - **연매출 $10M 미만** → 상업·프로덕션 사용 **무료** · **단 *"Transfer of fine-tunes may require a paid license"***
> - **연매출 $10M 초과** → **유료 상업 라이선스**
> - 🆕 **매출 산정 범위 명시(볼트 발견)**: *"Revenue is measured **across the whole entity, including subsidiaries and affiliates under common control**."* ⇒ 🔴 **사업부 매출로 $10M 미만을 주장할 수 없다.**
> - 🆕 **카드 텍스트는 구속력 없음 명시**: *"The full, **binding** terms live in LICENSE."*
> - ✅ **자기 포지셔닝**: *"No per-generation billing, no per-seat lock-in, no forced API dependency"* + self-host
> 🔴🔴 **게이트는 안전 장치가 아니라 리드 수집이다** — `extra_gated_description`: *"By clicking **'Agree and Access'** you acknowledge the Privacy Policy and **consent to receive offers and updates including targeted and personalized advertisements.**"* ⇒ 🎯 **읽기는 열고 받기에 마케팅 동의를 붙였다. 게이트의 위치가 목적을 드러낸다.**
>
> ## ✅ 기술 스택 (볼트 카드 실측 · 파일 목록 기준)
> **22B DiT** 2계열(dev / distilled) · 양자화 **bf16 · comfy-int8-convrot**(🆕 **ComfyUI 전용 · ltx-pipelines/PyTorch 불가**) · **nvfp4**(🆕 **Blackwell / ltx-kernels 필요**) · 텍스트 인코더 **gemma4-12b**(+proj) · **영상 VAE(Conv) 와 오디오 VAE(+vocoder) 분리** · **×2 공간·시간 잠재 업스케일러**(다단 파이프라인 필수) · **`duration-head`**(🆕 용도: `--num-frames` 생략 시 자동 길이) · distilled LoRA 450
> 🆕 **볼트 신규 3건**: ① **확산 비디오 디코더가 VAE 재구성 단계를 대체**(*"sharper faces, textures, on-screen text, better motion, fewer artifacts"*) ② **장면 복잡도·예산에 따른 동적 연산 배분**(고정 압축률 탈피) ③ **네이티브 멀티샷**(*"generate connected scenes in a single pass"*) ⇒ 🏆 **③이 볼트 [[video-saas]] 축에 직접 유효하다 — 컷 연결을 모델 안으로 옮긴다.**
> ✅ **벤더 자발 한정**: *"applicability to emerging domains such as **robotics and physical AI is developing**"* → [[자기제한-명시]].
> 🆕 **메타데이터**: `arxiv` **2601.03233**(🔴 **논문 존재 · 수집기 미보고 · 볼트 미열람 — 성능 수치가 여기 있을 수 있다**) · `demo` `app.ltx.studio/ltx-2-playground/i2v` · 카드 언어 **9종(ko 포함)** · 태스크 태그 **11종** · `tags` 에 **`diffusion-single-file`**(⇒ `safetensors.total`·`gguf.total` 둘 다 `None` 인 **이유를 벤더가 태그로 선언**한다 · [[메타데이터-부재-추론]]) · `pinned` true
> 🔴 **성능 수치 0개 확증** — 231,894B 전문에서 품질 주장이 전부 정성어(*sharper · better motion · fewer artifacts*)이고 벤치·fps·해상도 수치가 없다. 🏆 **같은 배치 [[Video-Generation-Post-Training-Survey]] 가 영상 평가 관행을 서베이로 정리할 만큼 성숙했다고 적는데, 이 벤더(trendingScore 407 = 최고)는 측정값을 0개 낸다** → [[검사가능성-후퇴]] 영상 도메인 사례 확정.
> 📉 **DL/♥ = 263.8 — 볼트 기준선 264.5 를 교차했다**(09-30 283.8 *"근접"* → 교차). 🔴 기준선 산출 근거는 오늘도 미재확인.

> [!note] 정체
> [[LTX-2.5]]·[[LTX-2]] 영상/오디오 생성 모델을 배포하는 **HuggingFace 조직 계정**. arXiv 2601.03233 의 저자 **29인** 규모로 보아 **개인이 아닌 연구팀을 갖춘 조직**이다(제1저자 Yoav HaCohen).

## 볼트가 아는 것

- [[LTX-2.5]] — `Lightricks/LTX-2.5` · **DL 1,595,377**(30일 · 볼트 실측 2026-09-29) · ♥5,465 · **`gated: auto`** · license **`other`** · created 2026-07-23
- [[LTX-2]] — 논문 **arXiv 2601.03233** *"LTX-2: Efficient Joint Audio-Visual Foundation Model"*(2026-01-06 · 저자 29인) · **영상 14B + 오디오 5B 비대칭 듀얼 스트림**
- 제품 포지션: **오디오까지 같은 모델이 생성**하는 통합 영상 모델. *"state-of-the-art ... among open-source systems"*(자기보고)

## 🎯 볼트가 주목하는 것 — **공개 태도가 엇갈린다**

| 채널 | 개방도 |
|---|---|
| 논문(arXiv) | ✅ **완전 공개** — 구조·설계의도·한계까지 초록에 명시 |
| 모델카드(HF) | 🔴 **`gated: auto`** — 볼트 3회 연속 401(08-25 · 08-31 · 09-29) |
| 라이선스 | 🟡 **`other`** — Apache/MIT 아님, 상업적 사용 조건 미확인 |

🔴 **논문 마지막 문장은 *"All model weights and code are publicly released"* 다.** 게이트·비표준 라이선스와 긴장 관계에 있다.
📌 **단정하지 않는다** — 논문은 **LTX-2**, 게이트는 **LTX-2.5** 에 걸려 있다(6.5개월 차이의 다른 버전). `gated: auto` 는 거절이 아니라 자동 승인 절차일 수 있다. **`Lightricks/LTX-2` 저장소의 `gated` 값 조회로 검정 가능**하다.

🎯 **볼트 실무 결론**: 이 조직의 **스펙 정보는 HF 가 아니라 arXiv 에서 온다.** 카드가 막혀도 논문 경로가 열려 있다 → [[벤치마크-이미지-봉인]](채널 봉인) · [[무응답-오귀속]].

> [!warning] ⬜ 볼트가 확인하지 않은 것
> **조직의 다른 모델·회사 정보·소속 국가·상업 제품 라인을 조회하지 않았다.** 모델카드 전문을 **한 번도 읽지 못했다**(35일째). LTX-2 저장소의 게이트 여부 미확인.

## 관련 페이지
- [[LTX-2.5]] · [[LTX-2]] · [[벤치마크-이미지-봉인]] · [[무응답-오귀속]] · [[한정어-탈락]]
- [[YuE2]] — 오디오 생성 통합 계열(학계) · [[debpalash]] — 분리형 로컬 대비축 · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/Lightricks · 논문 https://arxiv.org/abs/2601.03233
- 볼트 실측: HF API `models/Lightricks/LTX-2.5` + README 401(126B) + arXiv API (2026-09-29 09:08~09:09 UTC)
- 신뢰도: ⭐⭐⭐ (모델 메타·논문 서지 실검증 · 조직 정보 자체는 미조회)

> [!update] 2026-09-30 — [[LTX-2.5]] DL **1,589,098** · 🔴 **게이트 5회 연속 · 정체는 "0행"이 아니라 HTTP 401**
> 볼트 실측(09-30 09:13): DL30 **1,589,098**(드리프트 0) · allTime **2,773,856**(완전 일치) · ♥**5,600** · license **other** · created 2026-07-23 · **lastModified 2026-09-01(29일 정지)** · `safetensors` **null**
> 🔴 **README 실측 = HTTP 401 · 126바이트** *"Access to model … is restricted … Please log in."* — **빈 파일이 아니라 인증 거부**다 → [[무응답-오귀속]].
> 🔴 `safetensors` null 로 **샤드 역산 경로 폐기 확정**. ✅ 우회는 태그 **`arxiv:2601.03233`** 뿐(09-29에 이 경로로 "영상 14B+오디오 5B" 확보).
> 🎯 **능력 확인된 것은 `pipeline_tag` 하나**(5회 연속). [[Qwen]] 의 apache-2.0+공개와 **정반대 극**.

---

## 🔄 2026-10-10 갱신 — [[LTX-2.5]] 이월 3건 미해소, 새 정보 1건

**다운로드 1,687,531**(30일) / **3,457,585**(전체누적) · likes **7,100**(배치 최대) · trending 7위 · lastModified 2026-10-02

> [!insight] 🏆 새 정보 — 30일/전체누적이 분리된 유일한 금일 모델이다
> **최근 30일이 전체의 48.8%** ⇒ 📌 **성장이 최근에 쏠려 있다.** 10-05 [[marketingskills]] 평탄 성장의 **반대편 사례**이고, 금일 다른 3건([[laya]]·[[Qwen-Image-2.1-Uncensored-GGUF]]·[[Ternary-Bonsai-2-27B]])은 **30일 == 전체누적(창 무의미 구간)** 이다.
> ⇒ ⚖️ **같은 배치에서 창 길이의 두 극단이 함께 관측됐다.** → [[지표-창길이]]

> [!warning] 🔴 이월 3건이 금일도 해소되지 않았다
> ① `gated: "auto"` **승인 미시도**(3배치째) ② `safetensors.total`·`gguf` **둘 다 None = 파라미터 수를 메타데이터에서 얻을 수 없다** ③ arXiv **2601.03233 3배치째 미열람**
> ⇒ 🆕 **누적 우회법 ⑦ 후보: `diffusion-single-file` 모델의 파라미터는 파일 목록(`/tree/main`) 바이트에서 역산해야 한다. 금일 미시도.** → [[대체필드-대조]]

> [!insight] 🎯 오디오 동시 생성 경로 — 볼트 한계 11번 재확인
> 태그 **18개 중 오디오 관련 6개**(text-to-audio · video-to-audio · audio-to-audio · text-to-audio-video · image-to-audio-video · image-text-to-audio-video).
> 📌 **`video-saas.canvas` 에 들어가야 한다는 미처리 항목이 금일 태그로 또 확인됐다.**

## 관련 페이지 (갱신 추가)
- [[LTX-2.5]] · [[지표-창길이]] — 쏠림 사례 48.8%
- [[대체필드-대조]] — 우회법 ⑦ 후보
- [[AI-영상-생성-2026]] · [[video-saas]]
