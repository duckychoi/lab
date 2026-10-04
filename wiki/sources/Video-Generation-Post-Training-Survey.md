---
title: "Video Generation Models: A Survey of Post-Training and Alignment — 영상 생성 사후학습·정렬 최초 종합 서베이"
type: source
domain: video-saas
tags: [video-saas, ai-news, hf-papers, survey, post-training, alignment, rlhf, reward-model, distillation, inference-time, taxonomy]
created: 2026-10-04
updated: 2026-10-04
sources: []
reliability: medium
---

# Video Generation Models: A Survey of Post-Training and Alignment (arXiv 2610.00812)

> [!insight] 🏆 핵심 인사이트 — **어제 수집분을 분류할 틀을 오늘 얻었다. 새 수치는 0이다.**
> 이 논문의 가치는 성능 주장이 아니라 **분류 체계**다. 사후학습을 **통합 프레임**으로 두고, 정렬 신호가 *어떻게 강제되는지* 로 **암묵적 정렬 ↔ 명시적 정렬**을 가른 뒤 네 범주로 조직한다:
> **① 지도 미세조정 · ② 자기학습·증류 · ③ 선호·보상 기반 · ④ 추론시점 기법**
> 🎯 **10-03 수집분 [[Adaptive-Reward-Routing]](오디오-비디오 확산 다중보상)이 ③범주에 정확히 들어간다.** ⇒ 📌 **볼트가 어제 "개별 기법"으로 받은 것이 오늘 "범주 안의 한 점"이 된다.** ⚖️ **서베이의 효용이 이것이다 — 새 사실을 주지 않고 이미 가진 것의 좌표를 준다.**

> [!note] 영상 고유의 난점 4가지 (초록 원문)
> 이미지·텍스트 생성과 달리 영상 정렬에는 고유 난점이 있다고 적는다:
> - **시간축 오차 누적** (error accumulation over time)
> - **모션–외형 결합** (motion-appearance coupling)
> - **다목적 트레이드오프** (multi-objective trade-offs)
> - **시간 속성에 대한 감독 부족** (limited supervision for temporal properties)
> 🎯 **네 번째가 볼트 video-saas 축에 가장 직접적이다** — *"시간 속성을 감독할 라벨이 부족하다"* 는 것은 **영상 자동화 파이프라인에서 품질을 자동 판정할 수단이 없다**는 뜻이고, 볼트가 [[AI-영상-생성-2026]] 에서 반복 관측한 문제다.
> **열린 과제로 적는 것**: 확장 가능한 보상 설계 · 장기 시간 일관성 · 안정성–표현력 트레이드오프 · 안전 인식 생성.

## 🔬 선언된 구현체 3단 층 — **②층 탈락 · 수집기 가설 확증**

수집기가 볼트에 넘긴 질문: *"`githubRepo` people-robots/Awesome-Video-Generation-Post-Training ★202(**큐레이션 리스트형이므로 "코드"가 아닐 가능성 높음** → 10-03 확립 3단 층의 ②`languages` 확인 필요)."*
🏆 **볼트 실행 결과 — 가설이 맞다:**

| 층 | 판정 | 실측(2026-10-04T09:12Z) |
|---|---|---|
| ① 선언이 있는가 | ✅ | `githubRepo` = `people-robots/Awesome-Video-Generation-Post-Training` · ★**203**(볼트) ↔ 수집기 202 = **드리프트 +1** |
| ② **코드가 있는가** | 🔴 **아니다** | `GET /languages` = **`{}`** |
| ③ 쓸 수 있는가 | — | (무의미 · 참고로 `license` = **MIT**) |

🔴 **`GET /contents/` 루트 실측**: `LICENSE`(1,066B) · **`README.md` 146,734B** · **`arxiv.md` 61,873B** · **`conference.md` 45,880B** · `figures/`(디렉터리). ⇒ ⚖️ **큐레이션 리스트 확정. `size` 86,791KB(≈85MiB)는 코드가 아니라 `figures/` 다.**
- 레포 실측: fork **5** · created **2025-12-22T18:57:51Z**(논문보다 **9개월 먼저** 생겼다) · pushed **2026-10-03T05:00:12Z**

> [!insight] 🏆🏆 **★ 역전 폭이 오늘 67배다 — 10-03 결론이 더 극단적으로 재확인됐다**
> 10-03 에 볼트는 *"★이 커도 코드 존재를 보증하지 않는다 — ★는 논문에 대한 관심을 재고 레포 내용을 재지 않는다"* 고 적었다(★52 코드 0 ↔ ★21 Python 4.2MB).
> **오늘 같은 배치 안에서 격차가 더 벌어진다:**
> | 논문 | 레포 ★ | `languages` | 코드 실체 |
> |---|---|---|---|
> | **이 서베이** | **203** | `{}` | 🔴 **0**(마크다운 254KB + figures) |
> | [[Stop-Thinking-Too-Early]] | **3** | Python 534,805B | ✅ 실코드 |
> | [[DMM]] | **3** | Python 792,840B + **Cuda 159,633B** | ✅ **실코드(CUDA 포함)** |
> | [[X-Tree]] | **2** | `{}` | 🔴 **0**(2파일 6KB) |
> ⇒ ⚖️ **★203 이 ★3 두 건보다 코드가 적다(0이다). 비율로 67배 역전이다.** 🏆 **그리고 이번엔 원인이 설명된다: 서베이의 레포는 "큐레이션 목록"이고 목록은 읽는 사람이 많다. ★는 *유용성* 을 재며, 유용성이 코드일 필요가 없다.** 📌 **따라서 10-03 결론을 다듬는다: ★는 "코드 품질"이 아니라 "대상의 유용성"을 재고, 큐레이션 목록은 코드 0 으로도 유용하다.** → [[선언된-구현체-공백]] · [[원본-파생-역전]].

> [!warning] ⚠️ 서베이이므로 **신규 수치 0건** — 인용할 때 주의
> 초록에 성능 수치가 없는 것이 **결함이 아니다**(서베이의 정상 상태다). 🔴 **그러나 볼트가 이 페이지를 나중에 인용할 때 "이 서베이가 ~를 보였다"로 쓰면 오류가 된다. 이 논문이 보인 것은 분류이고, 수치는 전부 피인용 논문들의 것이다.** → [[출처표시-무력화]] 경계.
> 📌 **`arxiv.md` 61,873B + `conference.md` 45,880B 는 볼트에게 "다음에 읽을 것 목록"이다** — 🔴 미열람.

> [!insight] 🎯 같은 배치 교차 — **평가 관행은 서베이가 될 만큼 성숙했는데, 같은 날 온 22B 영상 모델은 수치가 0개다**
> 이 서베이는 *"commonly used datasets, benchmarks, and evaluation practices"* 를 리뷰할 만큼 영상 평가 관행이 쌓였다고 적는다.
> 🔴 **그런데 같은 배치 [[LTX-2.5]](Lightricks · 22B · trendingScore 407 = 배치 모델 최고)의 모델 카드에는 성능 수치가 0개다**(벤치·fps·해상도 없음 · 카드 상단은 라이선스 블록).
> ⇒ ⚖️ **평가 틀의 공급과 벤더의 사용이 갈린다. 재야 할 것이 정리됐는데 측정값을 공개하지 않는다.** 🏆 **[[검사가능성-후퇴]] 의 영상 도메인 사례로 등재** — 같은 날 한쪽은 측정 체계를 서베이로 정리하고 다른 쪽은 측정값을 안 낸다.

## 도메인별 추출 (video-saas)

> [!note] 🔄 도메인 재판정 — 수집기 `ai-news` → 볼트 `video-saas`
> 수집기 메모: *"🎯 볼트 `video-saas` 도메인과 ai-news 경계 건 — 내용은 video-saas 쪽이나 1차 소스가 HF 논문이라 수집 시점 도메인은 ai-news 로 둔다(**볼트 재판정 후보**)."*
> ⚖️ **볼트 판정: `domain: video-saas` 로 둔다.** 📌 근거 — 볼트 도메인은 **소스의 출처가 아니라 주제**로 나뉜다(`ai-news` 는 "GitHub 트렌딩/모델 릴리스" 축이다). 내용이 전부 영상 생성 정렬이고 [[video-saas]] 도메인 페이지의 축적 대상이다. ✅ **tags 에 `ai-news` 를 병기해 검색 양쪽에서 잡히게 한다.**

- **기능 벤치마킹**: 🟡 **직접 구현 대상은 ④추론시점 기법**이다 — 재학습 없이 붙으므로 볼트 규모에서 유일하게 현실적이다. 🔴 구체 기법 목록은 PDF 필요.
- **크리에이터 인사이트**: 🎯 **"사전학습 모델이 인간 의도를 신뢰성 있게 따르지 못한다"** 가 이 서베이의 출발점이다 — 볼트가 [[Higgsfield-심층분석]] 등에서 본 *"프롬프트대로 안 나온다"* 는 사용자 불만이 **연구 측에서도 1차 문제로 정식화돼 있다**는 확인.
- **프롬프트 패턴**: 🔴 없음 — 정렬 *학습* 서베이이고 프롬프트 공학이 아니다.
- **워크플로우**: 🟡 사후학습 파이프라인의 4단 분류를 **품질 개선 경로의 지도**로 쓸 수 있다.
- **디자인 레퍼런스**: 해당 없음.
- **경쟁 우위 빈틈**: 🏆 **"시간 속성 감독 부족"과 "확장 가능한 보상 설계"가 명시적 열린 과제다.** ⇒ 📌 **영상 품질을 자동 판정하는 축이 아직 없다는 뜻이고, 그것을 가진 제품이 차별화된다.**
- **신뢰도**: ⭐⭐⭐ medium — 저자 **13명**(배치 최대) · upvote 44 · 레포 ★203 · *"first comprehensive review"* 자칭. 🔴 **서베이이므로 1차 검증 대상이 아니고, 볼트는 분류 체계만 취한다.**

> [!question] 미해결 질문
> - ④**추론시점 기법**의 구체 목록 — 재학습 없이 붙는 것이 실제로 몇 개인가?
> - *"first comprehensive review"* 주장의 **선행 서베이 대조** 여부
> - `arxiv.md`·`conference.md` 254KB 의 내용 — 볼트 video-saas 도메인에 이미 있는 항목과 **중복률**은?
> - 레포가 **논문보다 9개월 먼저** 생겼다(2025-12-22) — 목록이 먼저고 논문이 나중인가? ⇒ 🎯 [[원본-파생-역전]] 후보

## 관련 페이지
- [[Adaptive-Reward-Routing]] — 🎯 어제 수집분, 이 서베이 **③선호·보상 기반** 범주에 들어간다
- [[LTX-2.5]] — 같은 배치, **평가 틀 ↔ 수치 부재** 대조
- [[선언된-구현체-공백]] — ②층 탈락 · **★ 역전 67배**
- [[검사가능성-후퇴]] — 평가 관행 성숙 ↔ 벤더 미공개
- [[출처표시-무력화]] — 서베이 인용 시 수치 귀속 주의
- [[원본-파생-역전]] — 레포가 논문보다 9개월 선행
- [[AI-영상-생성-2026]] · [[video-saas]] · [[Higgsfield-심층분석]] · [[Remotion]]
- [[Stop-Thinking-Too-Early]] · [[DMM]] · [[X-Tree]] — 같은 배치 3단 층 비교군
- [[게시일-이중화]] — publishedAt 09-30 ↔ HF daily 10-02 ↔ 수집 10-04
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.00812
- 저자 13명: Chaoyu Li · Xiaoyi Gu · Yogesh Kulkarni · Eun Woo Im · Mohammadmahdi Honarmand · Zeyu Wang · Juntong Song · Fei Du · Xilin Jiang · Kexin Zheng · Tianzhi Li · Fei Tao · Pooyan Fazli
- 큐레이션 레포: https://github.com/people-robots/Awesome-Video-Generation-Post-Training — ★**203** · MIT · 🔴 `languages={}` **코드 0** · README 146KB + arxiv.md 62KB + conference.md 46KB
- 지표: upvote **44** · publishedAt **2026-09-30** · submittedOnDailyAt **2026-10-02**
- 검증: **2026-10-04T09:12:13Z** HF 논문 API + GitHub API/languages/contents 실호출 (볼트)
- 신뢰도: ⭐⭐⭐ (분류 체계는 즉시 유용 / 🔴 신규 수치 0 · 코드 0 · PDF·목록 미열람)
