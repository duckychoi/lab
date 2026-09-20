---
title: "ReactHuman — MLLM이 3건 중 1건의 위험을 오처리하고, 규모로 줄지 않는다"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-paper, embodied, benchmark, mllm, robotics, physics, safety]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# ReactHuman: A Physics-Grounded Benchmark for Human-Like Reactive Decision-Making in Embodied MLLMs

> [!insight] 핵심 인사이트 — **"이해했는가"가 아니라 "즉시 움직였는가"를 잰다**
> 기존 평가는 직관물리를 **영상 QA로 수동적으로** 묻거나, **길게 계획하는 과제**(내비게이션·재배치)를 본다. 초록 원문: *"**none measure whether a model can turn physical understanding into immediate, safety-critical action**."*
> ReactHuman은 평가 대상 MLLM을 **시뮬레이션 휴머노이드의 두뇌**로 앉히고 미끄러지는 접시·떨어지는 칼 같은 급작 위험을 준다. **17개 이벤트 계열 · 1,000+ 비트단위 재현 가능 장면**, 정답은 **240Hz 강체 시뮬레이션에서 주석 없이(annotation-free)** 도출.
> 🎯 **적대적 객체**: 외형과 물리가 모순되는 것들 — **폼(foam) 모루, 강철 사과**. *"appearance contradicts their physics"*.
> 🎯 **결정을 실제로 실행한다**: *"We **physically execute every committed plan** so that decisions have observable consequences."* — 답을 채점하는 게 아니라 **결과를 관측**한다.
> 채점: **3축(reasonable · safe · physically grounded) × 5지표.**

> [!warning] 🔴 결과 — 실패가 규모로 줄지 않는다
> MLLM **7종** 평가. 초록 원문 그대로:
> - *"models mishandle **roughly one hazard in three**"* — 약 3건 중 1건 오처리
> - *"act from **fixed dispositions rather than the observed scene**"* — 장면이 아니라 **고정 성향**대로 행동
> - *"**trust appearance over motion**"* — 운동보다 **외형**을 신뢰(폼 모루/강철 사과가 정확히 이걸 겨눈다)
> - *"**miss interception points at meter scale** even when the chosen action is correct"* — 행동이 맞아도 요격점을 **미터 단위**로 놓침
> - 🔴 *"**none of these failures shrink with model scale**"*
> 🎯 **마지막 줄이 이 논문의 핵심이다.** 네 실패가 전부 규모 비민감이면, 이건 *"더 큰 모델을 기다리면 되는 문제"* 가 아니라 **표현·인터페이스 문제**다. 📌 볼트 [[하네스-설계-축]] 의 *"모델을 바꾸지 않고 감싸는 층을 바꾼다"* 와 같은 결론에 **임바디드 쪽에서 도달**한다.

> [!note] ✅ 수집기 정확도 — 이 건은 전건 일치했다
> 17개 계열 · 1,000+ 장면 · 240Hz · 주석 없음 · 적대적 객체 2종 · 3축 5지표 · 7종 평가 · 3건 중 1건 · 규모 비감소 — **볼트 초록 대조에서 불일치 0.** 한정어(*"roughly"* → *"약"*)도 보존됐다.

> [!warning] 🔴 다만 수집기가 *"GitHub 레포 없음"* 으로 끝낸 자리에 **공개 아티팩트가 있다**
> 초록 마지막 줄: *"The benchmark can be found here: **https://huggingface.co/datasets/Alan123/reacthuman-benchmark-scaled**"*
> 볼트 실측(HF datasets API): **존재 · 파일 2,111개 · gated false · created 2026-07-11**.
> ✅ **코드 레포는 없지만 벤치마크 데이터셋은 공개돼 있다.** 📌 볼트 요청 3(*"★ 옆에 파일 트리 크기(코드 유무)"*)의 역방향 사례 — **레포 유무만 보면 "아무것도 없음"으로 잘못 분류된다.** HF 논문에는 **datasets/spaces 표면**이 따로 있다.

> [!warning] 🔴 그런데 그 데이터셋이 사실상 쓰이지 않고 있다
> **다운로드 567 · 좋아요 1.** 같은 대상의 **논문 업보트는 52**다.
> 🎯 **논문에 52표, 데이터셋에 좋아요 1.** 그리고 데이터셋은 **2026-07-11 생성** — 논문이 HF 데일리에 오른 09-14보다 **2개월 앞선다.** 두 달 동안 거의 아무도 받지 않았고, 논문이 뜬 뒤에도 567이다.
> 📌 **주목과 채택이 같은 축이 아니라는 것이 한 대상에서 동시에 측정된 드문 경우**다. 볼트가 트렌딩·업보트를 신호로 써 온 것에 대한 직접적 반례.

> [!note] 📌 볼트 실측 (2026-09-20)
> 업보트 **52**(수집기 일치) · 저자 **8** · **githubRepo: None** · 🔴 게시일 `publishedAt` **2026-09-09** / `submittedOnDailyAt` **2026-09-14**(5일 차) — 수집기 *"게시 09-14"* 는 데일리 등재일 → [[게시일-이중화]].

## 도메인별 추출 (slam-3dgs)

> 📌 **도메인 배정**: 수집기는 `ai-news` 로 보냈다. 볼트는 **`slam-3dgs` 로 재판정**한다 — 시뮬레이션 휴머노이드 · 240Hz 강체 물리 · 로봇 두뇌 배치가 스키마의 *로봇/카메라* 축이고, 09-19 [[ActionPiece]] → `slam-3dgs` 재판정과 **같은 근거**다.

- **현재 SOTA**: 🔴 **이 벤치에서는 SOTA가 없다** — 7종 전부 3건 중 1건을 놓친다. 개별 모델명·점수는 초록에 없다.
- **실시간 가능성**: 🎯 **벤치 자체가 240Hz 시뮬레이션**이고 반사 행동을 요구하므로 **지연이 평가 안에 내장**돼 있다. 다만 **MLLM 추론 지연 수치는 초록에 없다** — 요격점을 미터 단위로 놓치는 것이 *판단 오류*인지 *지연*인지 초록만으로는 구분되지 않는다.
- **카메라 파이프라인**: 시뮬레이션 렌더 입력. 실제 센서·캘리브레이션 요소 없음.
- **응용 가능성**: 🎯 **볼트 임바디드 축([[PhysBrain]] → [[ActionPiece]] → [[PhysBrain-1.5]])에 처음 붙는 "평가자"다.** 지금까지 그 계보는 전부 **모델** 쪽이었고 **잴 자가 없었다.** 09-19 볼트 기록 *"버전이 오르며 평가가 제어 → 이해로 좁아짐"* 이 문제였는데, **ReactHuman은 반대로 이해 → 제어로 되돌린다.**
- **필수 레퍼런스**: 데이터셋(2,111파일)이 공개돼 있으므로 **읽지 않고 받을 수 있다.**

> [!action] 당장 할 것
> `Alan123/reacthuman-benchmark-scaled` 를 받아 **장면 1개를 열어 본다** — 2,111파일의 구조를 보면 *"비트단위 재현"* 이 무엇을 의미하는지(시드? 상태덤프? 궤적?)가 확인된다. **볼트 코드 실행 0건을 깰 가장 값싼 후보**다(모델 추론 불필요).

> [!question] 미해결 질문
> 1. **7종 MLLM이 무엇인지** 초록에 없다 — 본문 미열람.
> 2. *"3건 중 1건"* 의 **지표 정의**(5지표 중 어느 것?) 미상.
> 3. 다운로드 567 · 좋아요 1 의 원인 — **접근성 문제인지 관심 부재인지** 모른다.

## 관련 페이지
- [[PhysBrain]]
- [[ActionPiece]]
- [[PhysBrain-1.5]]
- [[DeepCybo]]
- [[하네스-설계-축]]
- [[게시일-이중화]]
- [[상대속도-가림]]
- [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2609.10895 · https://arxiv.org/abs/2609.10895 · 데이터셋 https://huggingface.co/datasets/Alan123/reacthuman-benchmark-scaled
- 볼트 실측(2026-09-20): 업보트 **52** · 저자 **8** · githubRepo None · `publishedAt` **2026-09-09** / `submittedOnDailyAt` **2026-09-14** · 데이터셋 **파일 2,111 · 다운로드 567 · 좋아요 1 · gated false · created 2026-07-11**
- raw 대비: 볼트 추가 = ✅ **초록 대조 불일치 0(수집기 정확)** · 🔴 **"레포 없음" 자리에 공개 데이터셋 실재** · 🔴 **업보트 52 ↔ 데이터셋 좋아요 1 = 주목·채택 분리 실측** · 🔀 **도메인 ai-news → slam-3dgs 재판정** · 🔴 **게시일 5일 차**
- 신뢰도: ⭐⭐ (초록 전건 일치 · 데이터셋 실공개 / 모델명·지표 정의·본문 미확인)
