---
title: "XPENG AI — 자율주행 기업이 그라운딩 파운데이션 모델을 냈다"
type: entity
domain: slam-3dgs
tags: [slam-3dgs, entity, 기업, 자율주행, 로보틱스, 임바디드-AI, 중국]
created: 2026-10-13
updated: 2026-10-13
sources: [GroundingPI.md]
reliability: medium
---

# XPENG AI (샤오펑)

> [!insight] 한 줄
> **[[GroundingPI]] 의 소속 조직.** 🆕 **볼트가 HF paper API 의 `organization` 필드에서 발굴했다 — 수집기 보고에는 없던 정보다.**

**HF 조직**: `XPENG AI`(`_id` 6aa24a85fc727b9188a95572)
**제출자**: Qize Yu(`Skywalker0410`) · 저자 **26명**
**공개 자산**: projectPage `groundingpi.github.io` · GitHub `groundingpi/GroundingPI`(★**24** · Apache-2.0) · HF 모델 1 · Space 3

> [!insight] 📌 **왜 이 조직이 이 논문을 내는지가 설명된다**
> XPENG(샤오펑)은 전기차·자율주행 기업이다. [[GroundingPI]] 의 평가 구성이 그 정체성과 정확히 일치한다:
> - **nuScenes** 오픈루프 L2 **0.296m** — 자율주행 궤적 예측
> - **RoboTwin 2.0** OOD 4설정 · **RoboCasa-GR1** — 로봇 조작
> - 자기 규정 *"foundation models of **physical intelligence**"*
> 🎯 ⇒ **범용 VLM 경쟁이 아니라 "차량·로봇에 들어갈 지각 백본"을 만드는 것이 목적**으로 보인다. 📌 **이것이 [[특화-역류]] 의 동기 측 설명이다** — 4B 전용 모델이 대형 범용 모델을 그라운딩에서 이기는 구조는 **용도가 좁기 때문에 가능**하다.

> [!warning] 🔴 **관심도가 주장과 반대다 — GitHub ★24**
> 34엔트리 SOTA(평균 **73.68%**)·44 베이스라인 비교를 주장하는 논문의 공식 레포가 **★24 · fork 2 · open_issues 0**(볼트 API 실측).
> ⚖️ **공개 9일차**(2026-09-30 생성)라 누적 시간이 짧다 — **절대 비교는 공정하지 않다.**
> 🎯 그러나 같은 배치 [[rea]](★179,917)와의 **7,496배** 격차는 기록해 둔다 ⇒ [[관심-검증-역상관]] 의 **역방향 사례**.

> [!question] 미해결
> - XPENG AI 의 **다른 공개 모델/논문** 이력 미조사(HF 조직 페이지 미열람).
> - GroundingPI 가 **양산 차량에 들어가는지** 미상(논문·레포 모두 언급 없음).
> - 조직 규모·설립 시점 미확인.

## 관련 페이지
- [[GroundingPI]] — 본 조직의 유일 확인 소스
- [[특화-역류]] · [[비매칭-비교]] — 전용 4B vs 범용 대형
- [[관심-검증-역상관]] — 검증 풍부 · 관심 없음
- [[임바디드-AI]] · [[월드모델]] · [[slam-3dgs]]

## 원본
- 출처: HF paper API `api/papers/2609.39601` → `organization` 필드 · GitHub API `groundingpi/GroundingPI`
- 수집: 2026-10-13 · 🆕 **볼트 발굴**(수집기 미수집 메타데이터)
- 신뢰도: ⭐⭐
