---
title: "qm — 멀티플레이어 에이전트 하네스 (Slack + 웹)"
type: source
domain: ai-news
tags: [ai-news, github, agent-harness, multiplayer, slack, scope, self-host]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# qm

> [!warning] raw 요약이 설계를 뒤집어 적었다 — 이 배치 3번째 왜곡
> raw: *"여러 사람이 **하나의 에이전트 작업 세션을 공유·개입**하는 하네스"*
> README 실측: *"Employees each get their **own isolated workspace** and work independently **without affecting each other**, and they can **also** collaborate ... in channels."*
> → **1차 설계는 "공유"가 아니라 "격리"다.** 협업은 그 위에 얹힌 2차 계층이다. raw는 이름의 "멀티플레이어"에서 공유를 추론한 것으로 보인다.
> raw가 *"실제 동시성 보장 범위는 원문 미확인"* 이라 스스로 단 유보가 옳았고, 확인해 보니 **전제 자체가 반대**였다.

> [!insight] 핵심 인사이트
> 진짜 단위는 세션이 아니라 **스코프(scope)** 다. **사람마다, 그리고 방(room)마다** 각각의 메모리·파일·keychain 뷰·권한·cron·웹앱·durable 샌드박스를 가진다. 그리고 **하네스 비종속** — Pi·OpenCode·Codex·[[Claude-Code-워크플로우]]가 **같은 코어를 구동**한다. 즉 이건 "또 하나의 에이전트"가 아니라 **에이전트를 조직 단위로 배치하는 다중 테넌시 레이어**다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐14,757 · fork 1,791 · TypeScript · MIT · pushed 2026-09-09(당일) · 생성 2026-07-29. 6주 만에 1.4만 스타.
- **즉시 활용**: **부분 NO** — 스타트업 팀 배포가 전제다(Slack 워크스페이스 + 자체 배포). 1인 사용자에게는 과설계. 다만 **스코프 분리 모델 자체는 1인에게도 훔칠 가치가 있다**.
- **6개월 영향력**: 개인 비서형 하네스와 **조직형 하네스**가 갈라지는 지점. "에이전트를 회사에 도입한다"가 계정 문제가 아니라 **스코프·권한·메모리 격리 설계 문제**임을 명시한다.
- **대체 관계**: [[Claude-Code-워크플로우]]를 대체하지 않고 **감싼다** — Claude Code를 코어 중 하나로 꽂아 쓴다.
- **허와 실**: 설치 안내가 *"Tell your coding agent `Let's deploy https://github.com/yc-software/qm`"* 다. 배포 난이도를 에이전트에게 떠넘기는 방식이라 **실제 배포 비용은 README로 판정 불가**. 3rd-party 호스팅(agent37.com)이 별도 존재.

> [!insight] 훔칠 설계 — 스킬의 소유권과 승격
> *"Skills are **scope-owned** and shareable **by grant**, with **admin-gated promotion** to the whole org, and skill packs imported from git repositories."*
> → 내 스킬 운영(현재 40여 개 평면 나열)에 바로 대응되는 모델: **개인 스킬 → 검증 → 승격**. [[에이전트-스킬]] 에 이 3단계를 축으로 추가할 것.

> [!action] 당장 할 것
> 배포하지 말고 **스코프 표를 베낀다**: 내 환경에서 (메모리 / 파일 / 키 / 권한 / cron / 샌드박스) 6개 축이 각각 어디에 묶여 있는지 적어 본다. 지금은 전부 "전역"에 묶여 있을 가능성이 높다.

## 관련 페이지
- [[에이전트-스킬]]
- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[Comp-AI-CRM]]

## 원본
- 출처: https://github.com/yc-software/qm
- 실측(2026-09-09): ⭐14,757 · fork 1,791 · TypeScript · MIT · created 2026-07-29 · pushed 2026-09-09 · archived=False
- raw 대비 드리프트: **완전 일치**
- 신뢰도: ⭐⭐⭐
