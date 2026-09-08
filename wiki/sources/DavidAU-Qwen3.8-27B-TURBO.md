---
title: DavidAU Qwen3.8-27B-TURBO — 파일명에 벤치 점수를 박은 모델, 그리고 메타데이터가 틀렸다
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, qwen, fine-tune, uncensored, abliterated, 자체측정, 메타데이터불일치, 재배포자층]
created: 2026-09-08
updated: 2026-09-08
sources: []
reliability: low
---

# DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF

**HF**: https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF
**다운로드(30일)**: **348,753** (2026-09-08 API 실측 · raw 348,753 **완전 일치** · **2회 측정 동일값**)
**좋아요 314 · 생성 2026-09-01 · 최종수정 2026-09-08(당일) · `gated: False` · Apache-2.0**
**베이스 모델**: `DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NM-DAU` (**같은 배포자의 다른 리포**)
**태그**: `gguf` `unsloth` `fine tune` `heretic` `uncensored` `abliterated` `ara` `MTP GGUF Quants` `Regular GGUF Quants` `qwen3_8` `qwen3_6` `qwen3_5` `multi-stage tuned` `thinking`

> [!warning] 🔴 **`pipeline_tag` 가 `image-text-to-text` 다 — 실제는 텍스트 코더/창작 모델**
> raw 지적을 **API로 확인**했다: `pipeline_tag: image-text-to-text`. 태그 목록·이름·설명 어디에도 **비전 능력의 근거가 없고**, `qwen3_8` `NEO-CODER` `thinking` 은 전부 텍스트 계열이다.
> → **메타데이터 오류가 확정**된다. 영향은 실용적이다: HF의 **파이프라인 필터·자동 로더가 이 모델을 잘못 분류**하며, `library_name` 도 **미설정**(`None`)이라 자동 추론이 더 어렵다.
> 📌 볼트 규칙: **`pipeline_tag` 를 모델 성격 판정에 쓰지 않는다.** 재배포자 층에서는 카드 메타데이터가 손으로 관리되며 **틀릴 수 있다.** 이름·태그·베이스 모델을 교차 확인해야 한다.

> [!warning] 🔴 **파일명에 벤치 점수가 들어 있다 — `735-882`**
> 리포 이름의 **`735-882`** 는 raw 기재상 **ARC-C 735 / ARC-E 880**(자체 측정)을 가리킨다. 파일명 자체가 마케팅 문구인 셈이다.
> **자체 주장**: ARC-C **735**(8bit, 원본 대비 **+144**) · ARC-E **880** · 4bit **718** · 사고 토큰 **1/2~1/10 축소**(TURBO).
> **🔴 전부 자체 측정이며 독립 리더보드 근거가 없다.** raw 기재 정확. 추가 벤치는 *"community 탭 참조"* 로 **외부화**돼 있다 — 즉 **저자가 검증 책임을 커뮤니티에 넘겼다.**
> → 09-07 [[Tiel-Coder-35B-A3B-GGUF]] 는 같은 재배포자 층이면서 **통제군 + 자기 열세 3분해**를 공개해 🟡 조건부 인용 등급을 받았다. **이 모델은 그 조건을 충족하지 않는다** — 통제군도, 자기 열세 공개도, 측정 프로토콜도 없다.
> ⚠️ **"+144"라는 개선 폭이 특히 의심스럽다.** 파인튜닝(융합·abliteration)으로 ARC-Challenge가 그만큼 오르는 것은 이례적이며, **abliteration(거부 제거)은 일반적으로 능력을 약간 떨어뜨린다**는 것이 통설이다. 볼트는 이 주장을 **인용하지 않는다.**

> [!insight] 🎯 **그럼에도 DL 348,753 — 그리고 이건 "현역" 단계다**
> 이 배치의 세 모델 중 **유일하게 최종수정이 오늘(2026-09-08)** 이다. 생성 09-01 이후 **일주일간 계속 갱신 중**이며, DL 34.8만은 **1주일 만의 값**이다.
> → [[gpt2]] 페이지에서 정리한 **생애 단계 3분류**에서 이 모델은 **"현역(사용 중)"** 에 해당한다. 값이 정착돼 있고(2회 측정 동일) 리포는 활발하다.
> **수요의 정체**: 태그의 `uncensored` `abliterated` `heretic` 가 말해 준다. 09-07 [[Huihui-Qwen3.8-27B-abliterated-GGUF]](**벤치 전무·DL 219만**)와 **같은 시장**이다.
> 📌 볼트 관측 재확인: **거부 제거 시장은 벤치마크를 요구하지 않는다.** 구매 동기가 *"더 똑똑한가"* 가 아니라 *"거절하지 않는가"* 이므로, **품질 검증 없이도 큰 수요가 성립**한다. 09-07에 세운 이 명제가 **다른 배포자·다른 모델에서 재현**됐다(2번째 사례).

> [!note] GGUF·MTP — 로컬 실행 관점에서는 유의미
> `MTP GGUF Quants` + `Regular GGUF Quants` 두 종을 제공. **MTP(Multi-Token Prediction)** 양자화를 별도로 낸 것은 **추론 속도 지향**이며, TURBO(사고 토큰 축소) 주장과 방향이 일치한다.
> → 이 배치 [[Uno]](병렬 토큰 생성으로 3배 가속)와 **목적이 같고 층이 다르다** — 저기는 학습된 diffusion 가중치, 여기는 양자화 배포. **"토큰을 여러 개 한꺼번에"** 라는 발상이 논문 층과 재배포 층에서 동시에 관측된다.
> ⚠️ **속도 주장(사고 토큰 1/2~1/10)도 자체 측정**이며 프로토콜이 없다.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **🟡 조건부.** GGUF·27B·Apache-2.0·`gated: False` — **실배포는 가능**하다. 27B GGUF는 4bit 기준 대략 16GB 내외로 소비자 GPU 상단/통합 메모리에서 돌아간다(볼트 추정, 실측 아님). **다만 성능 주장이 검증 불가**하므로 도입 근거는 성능이 아니라 **거부 제거**뿐이다.
- **메모리 아키텍처**: 해당 없음(모델 자체).
- **Hermes 적용**: **🔴 권장하지 않음.** [[ChinameBot]]/[[hermes-agent]] 계열에 검증 안 된 abliterated 모델을 넣으면 **품질 회귀를 감지할 수 없다**(볼트에 회귀 테스트가 없다).
- **트레이드오프**: 저자 주장(정확도 ↑ + 사고 토큰 ↓)은 **둘 다 좋아진다**는 형태인데, 이런 주장은 대개 **측정 조건이 다르다.** 통제 조건 미공개.
- **오픈소스 구현체**: 본 리포 자체. 베이스는 **같은 배포자의 다른 리포**(외부 검증 없이 자기 계보 안에서 순환).
- **즉시 활용**: **🔴 NO.** 성능 근거 없음 + 메타데이터 오류 + 자기 참조 계보.

> [!action] 당장 할 것
> **"재배포자 층 인용 기준"을 [[검사가능성-공사]] 에 정식 등재**한다. 09-07 [[Tiel-Coder-35B-A3B-GGUF]](🟡 통제군 있음)와 본 건(🔴 없음)이 **같은 층에서 갈린 두 사례**이므로 기준선을 그을 수 있다: **통제군 + 프로토콜 + 자기 열세 공개** 중 **2개 이상**이면 조건부 인용, 아니면 인용 금지.

> [!question] 미해결
> **ARC-C +144가 사실인가** — 검증 수단이 없다. 독립 리더보드에 등재되지 않았고, community 탭은 **본 회차에서 확인하지 않았다**(다음 회차 확인 대상).
> **abliteration이 능력을 떨어뜨린다는 통설과 +144 주장의 충돌** — 둘 중 하나는 틀렸고 볼트는 어느 쪽인지 모른다.

## 관련 페이지
- [[Huihui-Qwen3.8-27B-abliterated-GGUF]] — **같은 시장(거부 제거)·같은 구조(벤치 없이 큰 DL)**. 2번째 사례
- [[Tiel-Coder-35B-A3B-GGUF]] — **같은 재배포자 층인데 근거 등급이 갈린 대조군**
- [[gpt2]] · [[Minimax-h3_Singularity]] — 같은 배치·생애 단계 3분류(이 건이 **"현역"**)
- [[Uno]] — **같은 목적(다중 토큰 가속), 다른 층**
- [[Alibaba]] — Qwen 원 개발사 · [[local-llm]] · [[검사가능성-공사]]

## 원본
- 출처: https://huggingface.co/DavidAU/Qwen3.8-27B-TURBO-Fable-Cold-Fusion-735-882-Heretic-Uncensored-NEO-CODER-MAX-MTP-GGUF
- 수집: 2026-09-08 자동수집 (local-llm)
- 검증: HF 모델 API 실측 (2026-09-08 · DL 348,753 raw와 **완전 일치·2회 측정 동일** · `pipeline_tag` 오류 확인 · `library_name` 미설정 확인)
- 신뢰도: ⭐⭐ (지표 실측 · **성능 전부 자체 측정·통제군 없음** · **메타데이터 오류** · 자기 참조 계보)
