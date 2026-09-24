---
title: "HappyWorld-Bench — 월드모델을 '상호작용 후에도 세계가 남는가'로 재는 3트랙 벤치"
type: source
domain: slam-3dgs
tags: [slam-3dgs, 월드모델, benchmark, embodied, spatial, video-world-model, elo, 측정도구]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: high
---

# HappyWorld-Bench — 영상 품질이 아니라 상태 일관성을 잰다

**논문**: https://huggingface.co/papers/2609.24308 (arXiv 2609.24308)
**업보트**: **35** (HF 데일리 **1위** · 볼트 실측 35 — 드리프트 **0**)
**게시**: arXiv **2026-09-21** → HF 데일리 등재 **2026-09-24** = **3일 차** → [[게시일-이중화]]

> [!insight] 핵심 인사이트
> **월드모델 평가의 질문을 바꾼다: "잘 생성하는가"가 아니라 "에이전트가 건드린 뒤에도 세계가 신뢰할 만한가".** 초록 원문: *"evaluates **whether generated worlds remain reliable as agents interact with them**"*. 🎯 볼트 [[월드모델]]·[[Diffusion-월드모델]] 축이 그동안 **생성 품질 지표**로만 채워져 있었는데, 이 벤치는 **상호작용·수정·재방문 이후의 상태 보존**을 1급 측정 대상으로 올린다. 측정 대상을 먼저 재정의하는 [[측정도구-먼저-반증]] 의 이번 배치 대표 사례.

> [!note] 🔀 도메인 재판정 — 수집기 `ai-news` → 볼트 **`slam-3dgs`**
> 수집기가 후보로 적었고 볼트가 **확정**한다. 근거: ① **embodied 트랙 254 케이스** + embodied 후보 **8종** 평가 ② **spatial world models** 9종 — 배치 정확도·편집 실행이 공간 조작 지표다 ③ 볼트 선례 동일 — [[ReactHuman]]·[[ActionPiece]] 를 *"VLA = 시각+언어+액션 · 로봇 조작 벤치"* 근거로 `slam-3dgs` 재판정했다. 도메인 3 정의(로봇/공간/카메라)에 정면으로 들어온다.
> 📌 교차 도메인: `video-saas`(video world model 14종) — 영상 생성 평가축과 겹친다.

## 규모·수치 — 초록 축자 대조 (볼트 직접 확인)

| 항목 | 값 | 초록 원문 |
|---|---|---|
| video 프롬프트 | **1,138** | *"comprises 1,138 video prompts"* |
| spatial 장면 | **300** | *"300 spatial scenes"* |
| embodied 케이스 | **254** | *"254 embodied test cases"* |
| 평가 대상 | video **14** · spatial **9** · embodied **8** | *"We evaluate 14 video world models, 9 spatial systems, and 8 embodied candidates"* |
| spatial 배치 정확도 | **70.14%** | *"**at best** 70.14% placement accuracy"* — **절대 정확도, %p 아님** |
| spatial 편집 실행 | **73.33%** | *"and 73.33% edit execution"* |

✅ **수집기 인용 6/6 초록과 문자 일치.** 한정어 *"at best"* → *"최고"* 로 보존 ✅ (**한정어 보존 9배치 연속**).

## 능력 체계 — W1~W6 + Arena

- **6단 능력 프레임워크(W1–W6)**: *"from generative construction to unified world modeling"* — 생성적 구성에서 통합 월드모델링까지 계층화. 🔴 **W1~W6 각 단계의 정의는 초록에 없다**(이름만).
- **3개 독립 트랙**: video / spatial / embodied — *"three independent evaluation tracks"*
- **HappyWorld-Arena**: 인간 A/B 비교 → **모델 단위 Elo**. 자동 지표(*"behavioral correctness"*)와 **상호보완**으로 설계됨.
  🎯 인간 Elo + 자동 지표 병행은 볼트가 [[mem0]] 에서 본 *"자는 열고 피측정물은 닫았다"* 와 반대 구도다 — **여기선 두 종류의 자를 같이 공개한다.**

> [!warning] 🔴 초록 기준 한계 — 3트랙 중 2트랙은 수치가 없다
> - **video·embodied 트랙 수치가 초록에 하나도 없다.** 서술만 있다: video *"reduced consistency during **extended rollouts and revisits**"* · embodied *"struggle to **preserve state across multi-step actions**"*.
> - 🔴 **분포 지표 없음(초록 기준)** — 모델별·항목별 값이 없다. 70.14%/73.33% 는 **최고값 2개**이고 9종의 분포는 알 수 없다. (수집기 09-23 요청 3 "분포 없으면 없다고 적어라" → **수집기가 이번엔 명시했다** ✅)
> - 🔴 **`githubRepo` 필드 `null`** — 볼트 `GET /api/papers/2609.24308` 실측으로 재확인(`githubStars` 도 `null`). 코드·데이터 공개 경로 없음. **단 이건 "공개 안 했다"가 아니라 "HF 논문 API에 등록 안 됐다"** 이다 → [[메타데이터-부재-추론]]
> - 🔴 **arXiv 본문 미열람** — 초록만.

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: 이 논문은 SOTA를 주장하지 않는다 — **자(尺)를 제안한다.** spatial 최고가 70.14%라는 것은 *"9종 중 최고가 70%대"* 이므로 **공간 월드모델은 아직 3할을 틀린다.**
- **실시간 가능성**: ⬜ 초록에 지연·fps 수치 0개. 판단 불가.
- **카메라 파이프라인**: ⬜ 초록에 입력 형식 서술 없음. spatial 300 장면의 구성 미확인.
- **응용 가능성**: 🟡 직접 쓸 일은 적으나 **"상호작용 후 일관성"이라는 평가 축**은 내 영상 파이프라인에도 적용된다 — 장면을 이어 붙였을 때 엔티티가 유지되는가. [[The-Past-Frames-the-Future]](같은 배치)가 같은 문제를 생성 쪽에서 다룬다.
- **필수 레퍼런스**: arXiv 2609.24308 본문 — **W1~W6 정의와 embodied 254 케이스 구성**이 초록에 없어서 본문이 필요하다. actionable 등록.

> [!question] 미해결 질문
> W1~W6 각 능력의 조작적 정의는? embodied 254 케이스는 시뮬인가 실제 로봇인가? Arena Elo와 자동 지표가 어긋난 모델이 있었는가(있다면 그게 가장 중요한 결과다)?

## 관련 페이지
- [[월드모델]] · [[Diffusion-월드모델]] · [[임바디드-AI]]
- [[Spatial-Interactor]] — 같은 배치, 같은 재판정(공간+상호작용)
- [[The-Past-Frames-the-Future]] — 같은 배치, 생성 쪽 일관성 문제
- [[ReactHuman]] · [[ActionPiece]] — 재판정 선례
- [[측정도구-먼저-반증]] · [[게시일-이중화]] · [[메타데이터-부재-추론]]
- [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2609.24308
- 확인 범위: **HF 논문 API 초록 전문**(볼트 직접 조회) · `githubRepo`/`githubStars` **`null` 실측** · **arXiv 본문 미열람**
- 신뢰도: ⭐⭐⭐ (HF 데일리 1위 · 업보트 35 · 규모 수치 구체 · 단 2/3 트랙 수치 부재)
