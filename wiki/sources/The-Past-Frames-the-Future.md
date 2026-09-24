---
title: "The Past Frames the Future — AR 비디오 생성 메모리 서베이 (메모리를 조작적으로 정의한다)"
type: source
domain: video-saas
tags: [video-saas, agent-memory, autoregressive, survey, long-horizon, world-model, 분류체계]
created: 2026-09-24
updated: 2026-09-24
sources: []
reliability: medium
---

# The Past Frames the Future — 컨텍스트 창 밖으로 밀려난 과거를 어떻게 지키는가

**논문**: https://huggingface.co/papers/2609.28466 (arXiv 2609.28466)
**업보트**: **33** (볼트 실측 33 — 드리프트 **0**) · **부속 GitHub**: `HaroldChen19/Awesome-AR-Video-Memory` ★**30**
**게시**: arXiv **2026-09-23** → HF 등재 **2026-09-24** = **1일 차** (이번 배치 최단)

> [!insight] 핵심 인사이트 — **정의가 본문이다**
> 서베이의 실제 기여는 분류가 아니라 **메모리의 조작적 정의**다. 초록 원문:
> > *"we formulate memory operationally as **persistent historical information maintained across outer AR steps, capable of influencing future generation even after the originating evidence is no longer locally accessible**"*
> 🎯 **"원 증거가 로컬에 없어진 뒤에도 미래 생성에 영향을 주는가"** — 이 한 줄이 판정 기준이 된다. 긴 컨텍스트를 그냥 넣은 것은 메모리가 아니고, **증거가 사라진 뒤에도 남는 것**만 메모리다. 볼트 [[암묵을-명시로]] 의 교과서 사례: 다들 "메모리"라 부르던 것에 **반증 가능한 경계**를 그었다.

> [!note] 도메인 판정 — `video-saas` 주도메인 · `local-llm` 교차
> 수집기가 교차 후보로 적었고 볼트가 **주도메인은 `video-saas` 유지, `local-llm` 교차로 확정**한다. 근거: 대상이 **AR 비디오 생성**이고 보존 대상이 *엔티티 정체성·동적 상태·개입에 의한 인과 변화* 로 **영상 내용**이다. 다만 스키마 도메인 2가 "에이전트 메모리"를 포함하므로 [[에이전트-메모리-레이어]] 와 **같은 문제의 다른 모달리티**로 교차 연결한다.

## 5축 분류 체계 — 초록 축자

| 축 | 원문 | 내용 |
|---|---|---|
| **I. Forms** | *"the representational carriers of history"* | 과거를 무엇에 담는가 (표현 매체) |
| **II. Functions** | *"the specific semantic and physical information requiring preservation"* | 무엇을 보존해야 하는가 |
| **III. Operations** | *"the lifecycle of **writing, reading, updating, managing, and integrating** memory"* | 5단 수명주기 |
| **IV. Learning** | *"the optimization of memory behaviors under **closed-loop rollouts**"* | 닫힌 루프 롤아웃에서의 최적화 |
| **V. Evaluation** | *"the paradigms for **diagnosing genuine memory capabilities**"* | *진짜* 메모리인지 진단 |

🎯 **축 V가 이 서베이의 날이다** — *"genuine"* 이라는 단어를 저자가 골랐다. 즉 **메모리처럼 보이지만 아닌 것**이 문헌에 있다는 전제다. [[측정도구-먼저-반증]] 과 정확히 같은 태도.

## 문제 정의 — 병목의 위치

초록이 병목을 구조적으로 짚는다: *"as the generated sequence expands, practical models must operate under **strictly bounded context windows, storage, and computational limits**. Consequently, critical historical information, e.g., **entity identities, dynamic states, and intervention-induced causal changes**, often leaves the active context **long before its relevance diminishes**."*
📌 핵심은 마지막 구절이다 — **관련성이 사라지기 훨씬 전에 컨텍스트에서 밀려난다.** 문제는 용량이 아니라 **퇴출 시점과 관련성 감쇠의 불일치**다.

**열린 과제 4개**(초록 명시): 조합 가능·자원 인식 메모리 아키텍처 · **신뢰할 수 있는 상태 갱신** · self-rollout 학습 · **표준화된 평가**.

> [!warning] 🔴 한계 — 서베이라 성능 비교에 쓸 수 없다
> - **초록 내 정량 수치 0개.** 자체 실험·벤치마크가 없다(서베이의 정의상 정상).
> - 🔴 **따라서 이 페이지를 어떤 비교표에도 인용하지 않는다.** 용도는 **분류 체계와 정의**뿐이다.
> - 📌 다만 이것은 [[Spatial-Interactor]]·[[RewardVerse]] 의 *"수치 0개"* 와 **성질이 다르다**: 저 둘은 성능을 주장하면서 수치가 없고, 이건 **성능을 주장하지 않는다.** → reliability `medium`(서베이로서 유효), 저 둘은 `low`.
> - ⬜ **부속 레포 ★30 은 매우 작다** — Awesome 리스트이므로 큐레이션 품질 미확인. 미열람.
> - 🔴 arXiv 본문 미열람 — 5축 하위 분류의 실제 항목을 모른다.

## 도메인별 추출 (video-saas · 교차 local-llm)

- **기능 벤치마킹**: 🟡 직접 구현 대상은 아니다. 다만 **Operations 5단(쓰기·읽기·갱신·관리·통합)** 은 내 영상 파이프라인의 **장면 간 상태 전달** 설계 체크리스트로 바로 쓸 수 있다 — [[reat]] 에서 장면을 이어 붙일 때 무엇을 넘기는가를 이 5단으로 점검.
- **크리에이터 인사이트**: 사용자가 긴 영상에서 불만족하는 지점이 **"캐릭터가 달라진다"** 인데, 초록이 그것을 `entity identities` 로 **1급 보존 대상**으로 명명했다. 갭이 확인됐다.
- **프롬프트 패턴**: ⬜ 없음(서베이).
- **워크플로우**: 🎯 **`closed-loop rollouts`(축 IV)** 가 시사점이다 — 메모리를 학습으로 다루려면 생성 결과를 다시 입력으로 돌려야 한다. 내 파이프라인은 현재 단방향이다.
- **디자인 레퍼런스**: 해당 없음.
- **경쟁 우위 빈틈**: **"표준화된 평가 부재"** 를 저자가 열린 과제로 남겼다. 같은 배치 [[HappyWorld-Bench]] 가 **바로 그 빈틈을 메우려는 시도**다 — 🎯 **같은 날 HF 데일리에 문제 제기(1일 차)와 해결 시도(3일 차)가 동시에 올라왔다.**

## 관련 페이지
- [[HappyWorld-Bench]] — 같은 배치, 이 서베이가 남긴 "표준 평가 부재"를 메우는 쪽
- [[SpeakerMem-R1]] — 같은 배치, 대화 쪽 메모리(같은 문제 다른 모달리티)
- [[에이전트-메모리-레이어]] · [[mem0]] · [[VoiceMem]]
- [[월드모델]] · [[Diffusion-월드모델]] · [[AI-영상-생성-2026]]
- [[암묵을-명시로]] · [[측정도구-먼저-반증]]
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2609.28466
- 확인 범위: **HF 논문 API 초록 전문**(볼트 직접 조회) · `githubRepo`·`githubStars` 실측(★30) · **arXiv 본문 미열람** · **Awesome 레포 미열람**
- 신뢰도: ⭐⭐ (**medium** — 업보트 33 · 조작적 정의와 5축 체계는 유효 · 단 수치 0개로 비교 불가)
