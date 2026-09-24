---
title: "RewardVerse — 루브릭을 먼저 만들고 그 루브릭으로 채점한다 (초록 수치 0개)"
type: source
domain: video-saas
tags: [video-saas, reward-model, rubric, rl, scalar-drift, 수치부재]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: low
---

# RewardVerse — `scalar drift` 를 이름 붙이고 중간 표현으로 막는다

**논문**: https://huggingface.co/papers/2609.22947 (arXiv 2609.22947)
**업보트**: **20** (볼트 실측 20 · 수집기 19 → 드리프트 **+1**) · **부속 GitHub**: `2kxx/RewardVerse` ★**3**
**게시**: arXiv **2026-09-19** → HF 등재 **2026-09-24** = **5일 차**

> [!insight] 핵심 인사이트 — **문제에 이름을 붙이는 것이 절반이다**
> 초록이 실패 양식을 명명한다: *"This leads to **scalar drift**, where the **scoring scale collapses or shifts across different prompts**, making the reward unreliable for RL."*
> 🎯 **주관적 품질을 단일 스칼라로 직접 뱉게 하면 프롬프트마다 척도가 무너진다** — 그래서 **평가 기준(루브릭)을 먼저 생성하고 그 루브릭으로 채점**하는 중간 표현을 넣는다(*"a stable semantic anchor"*). 볼트 09-17 관찰(*"논문 5건 중 4건이 먼저 이름을 붙인다"*)의 이번 배치 재현.

> [!warning] 🔴 볼트 정정 — 수집기가 부속 GitHub 레포를 누락했다
> 수집기는 이 논문에만 *"부속: GitHub …"* 항목을 쓰지 않았다(나머지 4건 중 3건엔 썼다). 볼트 `GET /api/papers/2609.22947` 실측: **`githubRepo: https://github.com/2kxx/RewardVerse` · `githubStars: 3`**.
> 📌 **필드는 있었다.** 이것은 09-21 요청 2(*"필드가 없으면 파라미터를 시도하라"*)의 반대 사례 — **파라미터 문제가 아니라 단순 누락**이다. 값이 ★3으로 작아서 무의미해 보였을 수 있으나, **작은 값과 없는 값은 다르다.**

## 구조 — RGPO 2단계

- **문제**: 기존 비디오 보상 모델이 *"directly map complex, subjective video quality into a single score **without explicit evaluation criteria**"*
- **처방**: 동적 루브릭을 **평가 질의와 채점자 사이의 중간 표현**으로 삽입. 무제약 직접 채점 대신 → **명시적 기준 생성 → 루브릭 기반 채점**
- **RGPO (Rubric-Guided Policy Optimization)**:
  1. **자기진화 seed 루브릭**으로 채점자 워밍업 (*"warms up the scorer using self-evolving seed rubrics"*)
  2. **루브릭 생성기를 질의적응형으로 공동 최적화**하며 채점자를 **인간 평점에 지속 정렬** (*"while continuously aligning the scorer with human ratings"*)
- **평가**: **16차원 EvalVerse 벤치** + 외부 데이터셋, **pointwise·pairwise 양쪽**

> [!warning] 🔴 치명적 한계 — 초록에 수치가 **0개**다
> - 성능 주장이 **`"achieves state-of-the-art performance on both pointwise and pairwise evaluation"`** 뿐이다. **값이 없다.**
> - 🔴 SOTA를 **주장하면서** 수치가 없다 → [[Spatial-Interactor]](*"consistent gains"* 로 SOTA 주장 안 함)보다 **한 칸 더 나쁘다.**
> - 🔴 **16차원 EvalVerse 의 차원별 값 없음** = 분포 지표 부재. 16개 축을 만들어 놓고 초록에 한 축도 안 보여준다.
> - 🔴 **비교 대상(베이스라인) 미명시.**
> → `reliability: low`. **성능 비교에 인용 금지.** 볼트 [[BPO]]·[[Spatial-Interactor]] 와 동류 처분.

> [!insight] 🎯 볼트 교차 — 같은 처방이 두 모달리티에서 같은 달에 나왔다
> 볼트 [[RULER-SVG]](09-23 인제스트)가 **루브릭 기반 보상**을 SVG 생성에 적용했다. RewardVerse는 **같은 처방을 비디오에** 적용한다.
> 🔴 **그런데 비교에 쓸 수 있는 쪽은 RULER-SVG 뿐이다** — RULER-SVG는 절대 점수(0~1)를 냈고 이쪽은 수치가 없다. **동일 처방의 두 사례 중 하나만 측정 가능하다.**
> 📌 이것이 [[표-부분인용]]·[[측정도구-먼저-반증]] 과 다른 종류의 문제다: 부분인용은 인용 범위 안에서 사실이지만, **여기는 인용할 것 자체가 없다.**

## 도메인별 추출 (video-saas)

- **기능 벤치마킹**: 🟡 보상 모델은 내 SaaS의 직접 구현 대상이 아니다. 단 **"평가 기준을 먼저 생성하고 그 기준으로 채점"** 패턴은 **내가 생성 영상 품질을 자동 판정할 때 그대로 쓸 수 있다** — LLM에게 점수를 바로 묻지 말고 기준을 먼저 뽑게 한다. 난이도 낮음, 스택 불필요.
- **크리에이터 인사이트**: `scalar drift` 는 크리에이터가 체감하는 *"어제는 8점이던 게 오늘은 5점"* 의 기술적 이름이다. 갭 명명됨.
- **프롬프트 패턴**: 🎯 **직접 적용 가능** — 2단 프롬프트(기준 생성 → 기준 적용)가 단일 채점 프롬프트보다 안정적이라는 주장. **수치 없이도 구조는 베낄 수 있다.**
- **워크플로우**: 생성 → 자동 평가 → RL 루프. 내 파이프라인은 자동 평가가 없다.
- **디자인 레퍼런스**: 해당 없음.
- **경쟁 우위 빈틈**: 영상 품질 자동 판정은 아직 신뢰할 수 없다는 것이 이 논문의 전제다. **그 전제가 내 툴의 기회이기도 하다** — 자동 판정 대신 사람이 보는 단계를 남기는 설계가 정당화된다.

> [!question] 미해결 질문
> EvalVerse 16차원은 무엇인가? SOTA 주장의 상대는 누구인가? 루브릭 생성 비용(추가 LLM 호출)이 채점 안정성 이득을 상쇄하지 않는가?

## 관련 페이지
- [[RULER-SVG]] — 같은 처방(루브릭 보상), 다른 모달리티, **이쪽만 수치 있음**
- [[Spatial-Interactor]] · [[BPO]] — 초록 수치 0개 동류
- [[The-Past-Frames-the-Future]] · [[HappyWorld-Bench]] — 같은 배치 영상 평가축
- [[측정도구-먼저-반증]] · [[암묵을-명시로]] · [[요약자와-판정자-분리]]
- [[AI-영상-생성-2026]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2609.22947
- 확인 범위: **HF 논문 API 초록 전문**(볼트 직접 조회) · **`githubRepo`·`githubStars` 볼트 실측**(수집기 누락분 보충, ★3) · **arXiv 본문 미열람**
- 신뢰도: ⭐ (**low** — 업보트 20이나 초록 수치 0개 · SOTA 주장에 값 없음 · 베이스라인 미명시)
