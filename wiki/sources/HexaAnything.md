---
title: "HexaAnything — 로봇 상태를 코드로 꺼냈다는 주장. 그런데 개선폭이 초록에 한 자리도 없다"
type: source
domain: slam-3dgs
tags: [slam-3dgs, ai-news, hf-paper, 로보틱스, VLA, WAM, code-as-policy, 임바디드-AI, 수치부재, 자기진화, 제목-본문-괴리]
created: 2026-09-29
updated: 2026-09-29
sources: []
reliability: low
---

# HexaAnything — Self-Evolving Coding Agents: From Digital Programs to Physical-World Intelligence

> [!insight] 핵심 인사이트 — **진단이 처방보다 강하다. 문제는 성능이 아니라 표현이라고 말한다**
> 초록 축자: *"The root cause lies in **representation**: task requirements, conditions, progress, and failure recovery are **implicitly encoded in action sequences, making them difficult to inspect or revise**."*
> 🎯 **이 한 문장이 페이지의 값어치다.** VLA/WAM 이 관측→행동을 직결하면 **과제 상태가 행동 시퀀스 안에 녹아 버려 검사도 수정도 안 된다.** 그래서 레이아웃·시점이 조금만 바뀌어도 실패한다.
> 처방: **Physical Coding** — `Code as World`(객체·관계·제약·진행 기록) + `Code as Policy`(계획·검증·복구·실행 조직). VLA/WAM 은 **폐기 대상이 아니라 호출되는 도구**가 된다(*"calls perception, planning, and control tools, **including VLA/WAM policies**"*).
> 📌 **[[암묵을-명시로]] 의 로보틱스판이며, 같은 배치 [[YuE2]](음악)와 정확히 같은 수사다** — 암묵적으로 처리되던 중간 표현을 **읽을 수 있는 형태로 꺼내면 검사·수정·재사용이 따라온다.** 🎯 **하루에 두 도메인에서 같은 처방이 독립적으로 도착했다.**

> [!warning] 🔴🔴 **결과 섹션에 숫자가 하나도 없다 — 수집기 경고를 볼트가 확인했다**
> 초록에서 성능을 말하는 문장 전부(축자):
> - *"On RoboCasa365, HexaAnything **improves** Composite-Unseen and overall success **over XR-1 VLA**"* — 개선폭 **없음**
> - *"its Harness-trained HexaModel **beats the base on every split**"* — 폭 **없음** 🎯 **수집기가 누락한 세 번째 무수치 주장**
> - *"the agent autonomously completes physics experiments and most tabletop tasks, **often faster than published results**"* — *"most"*, *"often"*, 기준 문헌 **미특정**
> 📌 **볼트 판정: 초록만으로는 이 방법이 얼마나 좋은지 원리적으로 알 수 없다.** [[표-부분인용]] 이 "표에서 유리한 행만 뽑는" 문제였다면, 이건 **표 자체를 초록에 올리지 않은** 경우다 — [[벤치마크-이미지-봉인]] 과 효과는 같고 수단만 다르다(이미지 대신 **본문 유보**).
> 🔴 **따라서 이 페이지는 성능을 인용하지 않는다.** 인용 가능한 것은 **진단·구조·호출관계**뿐이다.

> [!warning] 🟡 제목과 본문의 층위가 다르다 — 수집기 지적 **확인**
> 제목: *"**Self-Evolving Coding Agents**: From Digital Programs to Physical-World Intelligence"* / 본문 주제: **로봇 조작 정책**.
> 초록 마지막이 층위를 더 벌린다: *"enabling evolution from tools and Harness to **model weights, architectures, and ultimately hardware and task design**"* · *"future work targets weight internalization, **autonomous redesign of architectures, languages, representations, and tasks**"*.
> 📌 **"자기진화"의 실제 관측 범위는 *"We observe data, model, and tool self-evolution"* 한 줄이고, 나머지는 전부 future work 다.** 하드웨어 자율 재설계는 **전망**이다. → [[RSI-프레이밍]] 사례 추가(같은 배치 [[TraceDance]] 와 대비: 저쪽은 *"could"* 한 줄, 이쪽은 **문단 전체**).

## 도메인별 추출 (slam-3dgs)

> [!note] 🔀 **도메인 재판정: 수집기 `ai-news` → 볼트 `slam-3dgs`**
> 내용 본체가 **로봇 조작 정책·VLA/WAM·듀얼암 실기(AgileX)** 다. 볼트 도메인 정의상 `slam-3dgs`(로봇) 축이 맞다. `ai-news` 는 보조 태그로 유지.

- **현재 SOTA**: 🔴 **판정 불가.** 비교 대상은 **XR-1 VLA** 하나이며 개선폭 미제시. RoboCasa365 리더보드 위치를 초록으로 알 수 없다.
- **실시간 가능성**: 🔴 **초록에 지연·주기·fps 수치 0건.** *"often faster than published results"* 는 속도 주장이지만 **기준도 값도 없다.**
- **카메라 파이프라인**: ⬜ 미기술. 지각(perception)을 **도구로 호출**한다고만 함 — 어떤 센서·표현인지 불명.
- **응용 가능성**: 🟡 **개념 차용은 즉시 가능.** `Code as World`(상태를 코드로) 는 볼트의 [[검사가능성-공사]] 와 같은 처방이고, **에이전트 일반**에 적용된다 — 로봇이 아니어도 "상태를 문자로 꺼내면 검사·복구가 가능해진다".
- **필수 레퍼런스**: **XR-1 VLA**(비교 기준) · **RoboCasa365**(벤치) · **PhyBench** — 셋 다 볼트 미보유. 🔴 **이 논문을 평가하려면 먼저 XR-1 기준선을 알아야 한다.**

> [!action] 당장 할 것
> arXiv **2609.35432** 본문에서 **RoboCasa365 수치표** 확보 — 이 페이지의 전부가 거기 걸려 있다. 🎯 **오늘 arXiv 경로를 고쳤으므로 실행 가능하다**([[무응답-오귀속]]). 우선순위 **중간**(로보틱스는 볼트 실행 축이 아님).

## 관련 페이지
- [[암묵을-명시로]] · [[검사가능성-공사]] · [[RSI-프레이밍]] · [[표-부분인용]] · [[벤치마크-이미지-봉인]] · [[자기제한-명시]]
- [[임바디드-AI]] · [[월드모델]] · [[Diffusion-월드모델]] · [[하네스-설계-축]] · [[slam-3dgs]]
- 같은 배치: [[YuE2]] — 🎯 **같은 처방, 다른 도메인** · [[TraceDance]] · [[DN-MOPD]] · [[무응답-오귀속]]

## 원본
- 출처: https://huggingface.co/papers/2609.35432 · arXiv **2609.35432**
- 실측(2026-09-29 09:08 UTC · HF papers API): 업보트 **41**(수집기 41 → **드리프트 0**) · 게재 **2026-09-28** · 초록 전문 정상 수신(손상 없음)
- 수집기 대조: 🎯 **수집기 경고 2건 모두 확인** — 무수치 주장 · 제목-본문 층위차. 볼트 추가: **무수치 주장이 3건**(HexaModel 누락) · future work 범위가 초록의 약 1/4
- 확인 범위: 초록 전문. 🔴 본문·수치표·코드·영상 미확인 · 🔴 미실행 · 🔴 XR-1/RoboCasa365 기준선 미보유
- 신뢰도: ⭐⭐ **low** — API 로 서지는 확정했으나 **성능 주장이 단 하나도 정량 검증 불가**. 진단·구조는 인용 가능.
