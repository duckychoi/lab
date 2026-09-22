---
title: "video-shotcraft — Remotion 제품영상 에이전트 스킬 (157 레시피 카드)"
type: source
domain: video-saas
tags: [video-saas, github, remotion, agent-skill, motion-design, claude-code, 영상자동화]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# video-shotcraft

> [!insight] 핵심 인사이트 — 내 도메인에 가장 직접적인 이번 배치 항목
> raw는 이것을 `ai-news` 로 분류했지만 **[[AI-영상-생성-2026|video-saas]] 도메인이 맞다.** Remotion 기반 제품영상 자동제작 스킬 — **내가 만들고 있는 것과 같은 계열**이다.
> 핵심 구조: **샷 레시피 카드(프롬프트 아님, 재현 가능한 레시피) + 네이티브 Remotion 컴포넌트**(`demos/<category>/<name>/<Component>.tsx`, **정규화 진행도 `t` 로 구동되는 결정적 컴포넌트**) + 라이브 갤러리 프리뷰.

> [!warning] 같은 README 안에 숫자가 세 개 — raw의 지적이 맞았고, 한 단계 더 있었다
> - 레포 **description**: `152 shot recipe cards, 209 motion previews`
> - README **헤드라인**: `**157** shot recipe cards · **214** styles · **214** motion previews`
> - README **Motion Workbench 절**: `**216** demo motions`
> raw는 앞의 두 개 불일치를 잡았다(정확). 볼트 추가 확인으로 **세 번째 숫자**가 나왔다.
> 152/209는 README 변경이력 문단(*"2026-08 · 48 new cards — 104 → 152 cards / 209 previews"*)의 **과거 값**이며, 레포 description이 그 시점에 멈춘 것이다.
> → **09-08 규칙 재확인: 레포 description은 소스가 아니다.** 그리고 **README 헤드라인조차 내부적으로 어긋날 수 있다** — 숫자를 인용할 땐 *어느 줄에서 왔는지*까지 적을 것.

## 도메인별 추출 (video-saas)

- **기능 벤치마킹**: **높은 이식 가치.** 내 [[Claude-Code-워크플로우]] 의 reat-* 파이프라인과 같은 문제(대본→씬→모션→렌더)를 푼다. 차이는 **모션을 "레시피 카드"라는 재사용 단위로 카탈로그화**했다는 점.
- **크리에이터 인사이트**: 갭을 **워크벤치**로 메웠다 — 납품 후 브라우저에서 CapCut 스타일로 계속 편집(`node workbench/scripts/open.mjs <project>`). 샷/트랜지션/자막/SFX **트랙으로 분해**되고, **프리뷰와 렌더가 프레임 동일(pixel-parity verified)**.
- **프롬프트 패턴**: 프롬프트가 아니라 **결정적 컴포넌트 + 정규화 시간 `t`**. 즉 *"모델에게 잘 부탁하기"를 버리고 "재현 가능한 코드"로 내려간 것* — 내 파이프라인이 가야 할 방향과 일치.
- **워크플로우**: 8라운드 프레임 단위 리뷰로 209개 후보 모션에서 48개를 추려 넣었다고 밝힘 → **큐레이션 비용을 명시**한 드문 사례.
- **디자인 레퍼런스**: 전부 de-branded — 중립 플레이스홀더 카피 + **교체 가능한 단일 `ACCENT` 색 변수**. 내 템플릿 설계에 그대로 쓸 규약.
- **경쟁 우위 빈틈**: 형제 프로젝트 **video-talkcraft**(내레이션 영상, 78 모션 카드, **문자당 median 20–40ms 로컬 정렬**, 7계층 안티-슬라이드쇼 샷 시스템)가 따로 있다. **나레이션 영상은 그쪽이 이미 깊다** — 내가 붙을 자리는 그 사이 또는 한국어 특화.

> [!action] 당장 할 것
> 1. **갤러리부터 본다**(코드 아님): https://vincentwei1021.github.io/video-shotcraft/ — 214개 모션 프리뷰. 내 reat-catalog 모션 프리셋과 **1:1 대조표**를 만든다.
> 2. `references/workbench.md`(Integration contract)를 읽고 **"납품 후 편집" 계약**을 내 파이프라인에 도입할지 판단.
> 3. **`t` 기반 결정적 컴포넌트 규약**을 내 Remotion 씬에 적용 — 렌더/프리뷰 불일치 문제의 근본 해법.

> [!warning] 주의
> 워크벤치 가이드(`workbench/GUIDE.md`)는 **중국어**다. Apache-2.0 이라 라이선스는 문제 없음.

## 관련 페이지
- [[Remotion]]  *(09-22 연결)*
- [[AI-영상-생성-2026]]
- [[에이전트-스킬]]
- [[Claude-Code-워크플로우]]
- [[claude-video]]
- [[OpenMontage]]

## 원본
- 출처: https://github.com/Vincentwei1021/video-shotcraft
- 실측(2026-09-09): ⭐7,860 · fork 707 · TypeScript · Apache-2.0 · created 2026-07-19 · pushed 2026-09-09 · archived=False
- raw 대비 드리프트: **완전 일치**(스타)
- 갤러리: https://vincentwei1021.github.io/video-shotcraft/
- 신뢰도: ⭐⭐⭐
