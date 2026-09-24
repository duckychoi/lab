---
title: "Spatial-Interactor — 상호작용 궤적으로 VLM에 상태 전이를 가르친다 (초록 수치 0개)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, vlm, spatial-reasoning, 온폴리시-증류, robotics, curriculum, 수치부재]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: low
---

# Spatial-Interactor — 정적 QA가 아니라 `관측 → 행동 → 후속 관측`

**논문**: https://huggingface.co/papers/2609.23038 (arXiv 2609.23038)
**업보트**: **22** (볼트 실측 22 · 수집기 20 → 드리프트 **+2**) · **부속 GitHub**: `ZJU-OmniAI/Spatial-Interactor` ★**6**
**게시**: arXiv **2026-09-19** → HF 등재 **2026-09-24** = **5일 차**

> [!insight] 핵심 인사이트
> **정적 QA로는 상태 전이를 가르칠 수 없다는 진단이 이 논문의 축이다.** 초록: *"Current spatial training primarily focuses on **static questions** about object attributes and spatial relations, providing **limited direct supervision for state transitions**; in contrast, **interaction trajectories naturally connect a preceding observation, an action, and a subsequent observation**"*.
> 🎯 **데이터 형식 자체가 지도 신호다** — 새 손실함수도 새 아키텍처도 아니고, *궤적으로 저장하면 전이가 라벨이 된다*. 볼트 [[ActionPiece]]·[[ReactHuman]] 이 같은 방향을 다뤘고 이건 그 학습 레시피 쪽이다.

> [!note] 🔀 도메인 재판정 — 수집기 `ai-news` → 볼트 **`slam-3dgs`**
> 근거: ① 데이터가 **시뮬+실제 상호작용 궤적**(LSI-108K) ② L2가 **self-state 전이** = 자기 시점·자기 운동 추정으로 카메라/신체 축 ③ 볼트 선례 [[ActionPiece]] 재판정 근거(*"VLA = 시각+언어+액션"*)와 동형. 도메인 3.

## 구조 — 3단 커리큘럼 + 2단 학습

- **L1** 수동 world-state 전이 (*"passive world-state transitions"*)
- **L2** 능동 self-state 전이 (*"active self-state transitions"*)
- **L3** 장기 상호작용 궤적 (*"long-horizon interaction trajectories"*)
- **데이터셋**: **LSI-108K** (Learning from Spatial Interaction) — *"from simulated and real interaction trajectories, with tasks aligned with the objective of each level"*
- **학습 2단계**: L1·L2 에 **SFT** → L3 에 **On-Policy Distillation(OPD)**
  🎯 **OPD 내부가 `privileged self-distillation` 이다**: *"a teacher branch **given segment-level transition descriptions** supervises the student's on-policy CoT"* — 교사가 **학생이 못 보는 구간별 전이 설명을 특권 정보로 받고** 학생의 온폴리시 CoT를 감독한다. → [[온폴리시-증류]] 의 **특권정보 변종** 첫 사례

> [!warning] 🔴 치명적 한계 — 초록에 정량 수치가 **0개**다
> - 성능 주장 전부가 **`"consistent gains in local transition modeling and long-horizon integration"`** 한 문장이다.
> - 🔴 **벤치마크 이름조차 없다** — *"across **multiple VLMs and spatial benchmarks**"*. 무엇으로 쟀는지 초록에서 알 수 없다.
> - 🔴 **분포 지표 없음** (초록 기준 — 애초에 점 하나도 없다).
> - 🔴 **베이스 VLM 미명시** — *"multiple VLMs"* 뿐.
> → **수치 대조가 원천적으로 불가능한 상태로 수록한다.** 볼트 [[BPO]](09-23, 초록 수치 0개, reliability low)와 **같은 부류이고 같은 처분**: `reliability: low`.
> 📌 이 페이지는 **분류·설계 참조로만 쓴다.** 성능 비교에 인용 금지.

> [!insight] 🎯 그런데 이 부재는 09-21 수집기 요청 3의 정확한 대상이다
> 수집기 요청 3: *"집계값에 분포가 없으면 「초록에 분포 지표 없음」을 **명시로 적어라**"*. 이 건에서 수집기는 **명시했다** — *"🔴 ⚠️ 초록에 정량 수치가 0개다… 벤치마크 이름조차 없다"*.
> ✅ **요청 3 이행 확인.** 없다고 적는 것과 안 적는 것은 다르고, 이번엔 적었다. **수치 0개인 논문을 수치 0개라고 밝히고 넘긴 것은 누락이 아니라 규율이다.**

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: ⬜ **판단 불가** — 수치 0개. SOTA 주장조차 없다(*"consistent gains"* 는 SOTA 주장이 아니다 — 이 절제는 오히려 정직한 쪽).
- **실시간 가능성**: ⬜ 지연·fps 초록에 없음.
- **카메라 파이프라인**: 🟡 **L2 self-state 전이가 시점 변화를 다룬다** — *"local state transitions caused by object motion **and viewpoint changes**"*. 카메라 이동이 명시적 학습 대상. 단 입력 형식(RGB/RGBD/포즈) 미확인.
- **응용 가능성**: 🟡 직접 응용은 낮다. 다만 **"궤적으로 저장하면 전이가 라벨이 된다"** 는 데이터 설계 원리는 내 파이프라인 로그에도 적용된다 — 행동 전후 상태를 쌍으로 남기면 나중에 학습 데이터가 된다.
- **필수 레퍼런스**: arXiv 2609.23038 본문 — **벤치마크 이름과 수치가 초록에 없으므로 본문 없이는 이 논문을 평가할 수 없다.** [[BPO]] 와 함께 actionable 등록.

> [!question] 미해결 질문
> LSI-108K의 시뮬 대 실제 비율은? 어떤 벤치로 쟀는가(이게 없으면 나머지가 의미 없다)? `privileged self-distillation` 에서 특권 정보를 뺀 대조군이 있는가?

## 관련 페이지
- [[온폴리시-증류]] — 특권정보 변종
- [[HappyWorld-Bench]] — 같은 배치, 같은 재판정(공간+상호작용), 이쪽은 **자(尺)**
- [[ActionPiece]] · [[ReactHuman]] — 재판정 선례 · 같은 축
- [[BPO]] — 초록 수치 0개 동류 선례
- [[임바디드-AI]] · [[월드모델]] · [[JEPA]]
- [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2609.23038
- 확인 범위: **HF 논문 API 초록 전문**(볼트 직접 조회) · `githubStars` 실측(★6) · **arXiv 본문 미열람** · **GitHub 레포 미열람**
- 신뢰도: ⭐ (**low** — 업보트 22이나 초록 정량 수치 0개 · 벤치마크명 부재 · 대조 불가)
