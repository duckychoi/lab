---
title: "MaLiang-Harness — '코드가 돌아가는 것'과 '요청대로 보이는 것'을 분리해 이름을 붙였다(P2V gap)"
type: source
domain: video-saas
tags: [video-saas, ai-news, hf-paper, arxiv, harness, image-generation, video-generation, program-synthesis, verification, P2V-gap, 측정도구-먼저-반증]
created: 2026-09-30
updated: 2026-09-30
sources: []
reliability: high
---

# MaLiang-Harness: A Programmable Path to Image and Video Generation

**HF 논문**: https://huggingface.co/papers/2609.34309 · **arXiv**: 2609.34309
**지표(2026-09-30)**: upvote **189**(수집기 09:04 관측 185 대비 **+4** · 볼트 09:13 실측) · **데일리 2위** · 공개 **2026-09-28**(수집기 일치)
**도메인 재판정**: 수집기 `ai-news` → 볼트 **`video-saas`**. 이미지·비디오 생성의 **품질 검증 루프**가 주제이므로 볼트 도메인 1(영상 AI SaaS)의 *"기능 벤치마킹 · 프롬프트 패턴 · 워크플로우"* 템플릿이 정면으로 적용된다.

> [!insight] 🎯 핵심 인사이트 — **볼트가 영상 생성에서 반복해 본 실패를 논문이 정의로 승격시켰다**
> 초록 원문: *"A program can **execute correctly while violating the requested composition, appearance, or motion**. We define this discrepancy as the **Program-to-Visual (P2V) gap**."*
> 📌 **이것이 오늘 배치에서 볼트에 가장 직접적으로 쓸모 있는 한 문장이다.** 볼트의 [[video-saas]] 도메인은 *"프롬프트↔결과 쌍"* 을 추출 항목으로 두고 있는데, **그 쌍이 어긋나는 현상에 이름과 측정틀이 생겼다.** 지금까지 볼트는 이것을 사례별로만 기록했다.
> 🎯 **핵심 설계는 "공통 리비전"이다** — *"to make the evolving visual program, its construction history, and its verification **share a common revision reference**."* 즉 프로그램·이력·검증이 **같은 판본을 가리킨다**. 3요소:
> - **PEG**(Persistent Executable Generation) — 프로그램과 태스크 맥락을 보존
> - **TGP**(Traceable Generation Process) — 편집을 **렌더된 증거에 연결**
> - **REV**(Revision-aware Editing and Verification) — 복원 지원 + **완료 전 현재 리비전 검사**
> 📌 **[[검사가능성-공사]] 의 생성 도메인판이다.** 볼트가 [[Ternary-Bonsai-2-27B]] 에서 *"검사 가능하게 공사한 사례"* 로 평가한 것과 같은 성격인데, 이쪽은 **검사를 아키텍처에 넣었다**.

> [!insight] ✅ 벤치 수치 있음 — 수집기 인용 **전건 일치**(볼트 arXiv 원문 대조)
> 초록 원문: *"We evaluate **11 powerful closed-source MLLMs** on MaLiang-IBench and **four** on MaLiang-VBench … **GPT-6-Astra achieves 100% generation success on both benchmarks**, with **96.0% of image tasks** and **76.9% of video tasks** meeting all quality thresholds."*
> ✅ 수집기 보고(11종·4종·100%·96.0%·76.9%)와 **글자 단위 일치**. 측정 3축도 명시: **generation success · visual quality · computational cost**.
> 🎯 **그런데 논문의 결론 문장이 수치보다 강하다**: *"The comparison also reveals a **mismatch between general capability scores and visual generation performance**, with similarly scored models differing substantially…"*
> 📌 **[[측정도구-먼저-반증]] 의 정면 증거다.** 범용 능력 점수(일반 벤치)가 시각 생성 성능의 **대리지표로 무효**라고 논문이 직접 말한다. 볼트가 모델 선택을 일반 벤치로 하면 안 된다는 것을 **11종 대조로 보여 준 첫 소스**다.
> 🔴 **단 100%는 "성공률"이고 품질이 아니다** — 같은 문장에서 GPT-6-Astra 는 생성 성공 100%이면서 **비디오 품질 임계 충족은 76.9%** 다. **생성 성공과 품질 충족의 23.1%p 격차**가 곧 P2V gap 의 실측값이다.

> [!warning] 🔴 폐쇄형 모델만 평가했다 — 오픈웨이트 적용 가능성 미확인
> *"11 powerful **closed-source** MLLMs"*. 오픈웨이트 모델 평가가 **초록에 없다**. 볼트가 추적하는 [[Qwen3.8-27B]] 계열·[[LTX-2.5]] 같은 오픈 백본에서 이 하네스가 작동하는지는 **미확인**이다.
> 🎯 이건 볼트에 실질적 제약이다 — 하네스는 *"모델을 바꾸지 않고 층만 바꾼다"* 는 축인데([[하네스-설계-축]]), **그 층이 약한 모델에서도 이득을 주는지가 이 논문으로는 안 나온다.** 11종 전부 폐쇄형이면 **"강한 모델에서 더 잘 된다"와 "층이 기여한다"를 구분할 수 없다.**
> ⬜ 본문 미열람 — 오픈웨이트 결과·절제 실험(ablation) 유무 확인 필요(actionable 등록).

## 도메인별 추출 (video-saas)

- **기능 벤치마킹**: **P2V 검증 루프를 내 SaaS에 넣을 수 있다.** 필요 스택 = 프로그램 생성(코드) + 렌더 백엔드 + **렌더 결과를 판정하는 MLLM 검사기** + 리비전 저장소. 난이도는 **검사기 정의에 몰려 있다** — "요청한 구도·외형·모션을 어겼는지"를 자동 판정하는 부분이 전부다.
- **크리에이터 인사이트**: 사용자가 원하는 것(=요청한 구도·외형·모션) vs 툴이 주는 것(=실행되는 코드)의 갭에 **이름이 붙었다.** 제품 언어로 쓸 수 있다 — *"돌아가는 것"이 아니라 "맞는 것"* 을 판다.
- **프롬프트 패턴**: 🔴 초록에 구체 프롬프트 없음. 대신 구조적 처방 = **편집을 렌더 증거에 연결(TGP)** · **완료 전 검사(REV)**.
- **워크플로우**: `프로그램 생성 → 렌더 → 검사 → 수정` 을 **판본 기준으로 반복**. 볼트의 [[reat-render]] 계열 파이프라인에 검사 단계를 끼울 자리가 정확히 보인다.
- **디자인 레퍼런스**: 해당 없음(UI 소스 아님).
- **경쟁 우위 빈틈**: **생성 성공 100% vs 비디오 품질 76.9%** 의 23.1%p 격차 = 상용 최강 모델에도 남은 공백. 여기가 제품 차별화 지점이다.

## 관련 페이지
- [[하네스-설계-축]] — 이 소스가 추가하는 "생성 검증" 층
- [[Raven]] · [[Omni-IO-Skills]] — 같은 배치 하네스 논문 3건 중 나머지
- [[측정도구-먼저-반증]] — 범용 점수 ≠ 생성 성능, 11종 대조 증거
- [[검사가능성-공사]] — 검사를 아키텍처에 넣은 사례
- [[LTX-2.5]] — 같은 배치 영상 생성 모델(오픈, 단 게이트)
- [[video-saas]] — 도메인 누적

## 원본
- 출처: https://huggingface.co/papers/2609.34309 · arXiv 2609.34309
- 신뢰도: ⭐⭐⭐ (upvote 189 데일리 2위 · **벤치 수치 전건 원문 일치** · 단 폐쇄형 모델 한정)
- 검증: 2026-09-30 09:13 UTC arXiv 원문 직접 열람(43,903 바이트) — 제목·초록 전문 대조, 수치 **전건 일치**
