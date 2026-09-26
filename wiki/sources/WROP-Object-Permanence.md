---
title: "WROP — 물체 영속성을 '창발했는가' 대신 '가르칠 수 있는가'로 바꾼 데이터 인프라"
type: source
domain: slam-3dgs
tags: [slam-3dgs, ai-news, world-model, object-permanence, video-generation, benchmark, elo, 측정도구-먼저-반증]
created: 2026-09-26
updated: 2026-09-26
sources: []
reliability: high
---

# Training Object Permanence in World Models (WROP)

> [!insight] 핵심 인사이트 — 질문을 **평가**에서 **학습**으로 옮겼다
> 초록이 두 질문을 순서대로 던진다: *"Do video models have emerged object permanence in them? **If not, could we train them** with a core-cognition inspired dataset?"*
> 🎯 **두 번째 질문이 이 논문의 자리다.** 09-24 배치의 [[HappyWorld-Bench]] 가 *"지속되었는지 어떻게 재는가"* 였다면, WROP는 **재는 도구를 만든 뒤 그 도구로 학습셋을 찍어낸다** — 시험 300문항과 **학습 코퍼스 150만 샘플**을 같이 낸다. 벤치가 훈련 데이터의 부산물이 아니라 **훈련 데이터가 벤치 설계의 부산물**이다.
> 설계가 인지과학을 그대로 따른다: 수작업 과제 **150개**를 **6개 인지 범주**로 나누고, Blender 생성기가 **속도·조명·카메라각 등 교란변수만 랜덤화하면서 과제의 인지 구조는 보존**한다(과제당 10,000+ 샘플). → **변인 통제가 데이터 생성 단계에 박혀 있다.**

> [!note] 평가 — 14개 모델 블라인드 Elo
> reference-to-video **3** · edit **7** · continuation **4** = **14개** 영상 모델을 블라인드 쌍대비교 Elo로 세운다. 자체 모델 **PWM-WROP(16B)** 는 *"ranks **first among continuation models** and **third overall**, behind only a **statistical tie** between two reference-to-video models"*.
> 🎯 **자기 순위를 정확히 좁혀 적었다** — "3위"이고, 위의 둘은 **부문이 다르고 서로 동률**이다. *"전체 1위"* 라 쓸 유혹을 피했고 **동률이라는 사실까지 초록에 넣었다.** [[한정어-탈락]] 의 반대 사례.
> 공개 범위 주장: 데이터 · 시험 · **모델 답안** · 점수 · 가중치 · AWS Trainium2 네이티브 PyTorch 학습 스택. **답안과 점수까지 연다면** [[검사가능성-공사]] 기준에서 상위다.

> [!warning] ⚠️ 초록에 Elo 절대값이 없다
> 초록의 수치 토큰은 **150 · 10,000+ · 1.5M · 300 · 14 · 16B** 로 전부 **규모**이고, **성능 값(Elo 점수·부문별 점수)은 0개**다. *"3위"* 는 순위이지 격차가 아니다.
> 🔴 즉 **"얼마나 잘하는가"는 이 페이지에서 대조 불가**다. 볼트 *"논문 초록만"* 누적 이슈에 해당(오늘 5건 중 이 건 포함 4건이 같은 상태).
> ✅ 다만 **부속 GitHub이 있다**: `hokindeng/object-permanence` (★**12**, HF API 실측) — 🔴 **수집기가 기재하지 않았다**(09-24 요청 3 재위반).

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: ⬜ **판정 불가** — Elo 절대값 미공개. 말할 수 있는 것은 *"continuation 부문에서 16B 자체 모델이 1위"* 라는 **순위 사실**뿐이다.
- **실시간 가능성**: 해당 없음(생성 모델 평가 연구). ⬜ PWM-WROP 추론 속도 미제시.
- **카메라 파이프라인**: **Blender 합성**이 입력이다 — 카메라각을 교란변수로 랜덤화한다. 🔴 **실사 일반화는 검증되지 않았다**(전 과제가 합성). [[HappyWorld-Bench]](embodied 254케이스)·[[Spatial-Interactor]](시뮬+실제 궤적)와 달리 **실제 촬영 트랙이 없다.**
- **응용 가능성**: 🎯 **물체 영속성은 [[월드모델]] 의 최소 요건이자 로봇 가림(occlusion) 처리의 전제**다. 가려진 물체가 존재를 유지한다고 모델이 믿지 못하면 SLAM 루프클로저·추적이 근본에서 흔들린다. 150만 샘플 공개는 **파인튜닝 자원으로 직접 쓸 수 있다.**
- **필수 레퍼런스**: 논문 arXiv 2609.28654 + `hokindeng/object-permanence`. 🎯 09-24 [[The-Past-Frames-the-Future]](서베이가 *"표준화된 평가 부재"* 를 열린 과제로 남김)와 **한 주 간격으로 짝**을 이룬다 — 오늘 그 빈틈의 **두 번째 메움**이다([[HappyWorld-Bench]] 에 이어).

> [!question] 미해결 질문
> 합성(Blender) 학습이 실사 영상 모델의 물체 영속성으로 전이되는가? 초록은 학습 코퍼스를 공개한다고만 하고 **전이 실험 결과를 언급하지 않는다.**

## 관련 페이지
- [[월드모델]] · [[Diffusion-월드모델]] · [[임바디드-AI]] · [[검사가능성-공사]]
- [[HappyWorld-Bench]] · [[The-Past-Frames-the-Future]] · [[Spatial-Interactor]] · [[측정도구-먼저-반증]]

## 원본
- 출처: https://huggingface.co/papers/2609.28654 (arXiv 2609.28654)
- 실측(2026-09-26 HF API): upvote **190** · `publishedAt` **2026-09-23** · 저자 **31명** · githubRepo `hokindeng/object-permanence` ★**12**
- 수집기 대조: upvote 189 → 볼트 190(**+1**) · 제목·초록 수치 **6/6 축자 일치**(150·6범주·10,000+·1.5M·300·14모델) · 🔴 **부속 GitHub 미기재**
- 🔴 게시일 주의: 수집기는 *"직전 발행일 09-25"* 라 했으나 **논문 자체 `publishedAt` 은 09-23** — 데일리 목록일과 발행일이 다르다([[게시일-이중화]])
- 확인 범위: **초록 전문.** 🔴 본문 미열람 · 🔴 부속 레포 미열람 · 🔴 데이터셋 미다운로드
- 신뢰도: ⭐⭐⭐⭐ **high** — 규모 수치 전건 일치 · 자기 순위를 동률까지 밝힘. (성능 절대값 부재로 ⭐5는 아님)
