---
title: obra/superpowers — 에이전트 스킬·소프트웨어 개발 방법론 프레임워크
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-framework, skills, open-source, software-methodology, claude-code]
created: 2026-04-11
updated: 2026-08-08
sources: []
reliability: high
---

# obra/superpowers

> [!update] 2026-08-08 갱신 — ⭐268,947 (당일 +782)
> ⭐**268,947** (2026-08-08 자동수집, 당일 **+782**) ← ⭐268,380 (08-07). 에이전트 스킬 카테고리 압도적 1위·27만 근접 유지, 하루 +수백대 안정 유입. 같은 08-08 배치의 [[mattpocock-skills]](⭐209,271)와 스킬 상단 2강 그대로. Anthropic 공식 마켓플레이스 등재·방법론 수준 인정 유지 → reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-08-07 갱신 — DL 26.8만 (당일 +858)
> ⭐**268,380** (2026-08-07 자동수집, 당일 **+858**) ← ⭐261,293 (07-26). 2주 새 +7,087로 에이전트 스킬 카테고리 압도적 1위 유지. 같은 08-07 배치의 [[mattpocock-skills]](⭐207,870·20만 돌파)와 함께 스킬 상단 2강. Anthropic 공식 마켓플레이스 등재·방법론 수준 인정 유지 → reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-07-26 갱신 — 26만 돌파 (WebFetch 실검증)
> ⭐**261,293** (2026-07-26 WebFetch 실검증) ← ⭐252,676 (07-12). 2주 새 +8,617로 에이전트 스킬 카테고리 압도적 1위·26만 돌파 유지. 같은 배치에서 스킬 발견 레이어([[awesome-claude-skills]])와 벤더 호환 레이어([[open-code-review]]·[[claude-cookbooks]])가 함께 성장 — 스킬=배포 단위 트렌드 지속. reliability high 유지.

> [!insight] 핵심 인사이트
> 코딩 에이전트를 위한 **완결된 소프트웨어 개발 방법론** — 조합 가능한 스킬(composable skills) 세트와 이를 자동으로 발동시키는 초기 지침으로 구성된다. ⭐261,293 (2026-07-26 실검증) ← ⭐252,676 (07-12) ← ⭐244,962 (07-03)로 에이전트 스킬 카테고리 압도적 1위, 급상승 최상위 유지. Claude Code·Cursor·Copilot·Kimi Code 등 멀티 하니스 지원 명시. 핵심은 "에이전트가 코드부터 짜지 않는다" — 먼저 스펙을 캐묻고(spec), 읽을 만한 크기로 쪼개 승인받고, 주니어도 따를 수준의 구현 계획을 세운 뒤, **서브에이전트 주도 개발(subagent-driven development)**로 태스크별 검수·리뷰하며 진행한다. 진짜 red/green TDD·YAGNI·DRY를 강제. 스킬이 자동 트리거되므로 사용자가 특별히 조작할 필요가 없다. 같은 배치의 [[agency-agents]](역할 페르소나 카탈로그)가 "누가 일하나"를 정의한다면, superpowers는 "어떻게 일하나"(프로세스·스킬 체계)를 정의한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐244,962, 단순 AI 도구가 아닌 개발 방법론 수준의 커뮤니티 인정. Anthropic 공식 플러그인 마켓플레이스(`/plugin install superpowers@claude-plugins-official`)에 등재, obra(Jesse Vincent) 주도로 전임 커뮤니티 엔지니어까지 채용 중 — 지속성 높음.
- **즉시 활용**: YES — Claude Code·Codex·Cursor·OpenCode·Copilot 등 다수 하니스에 플러그인으로 설치. 설치 즉시 스킬 자동 발동.
- **6개월 영향력**: 높음 — 에이전트 스킬·워크플로우 설계의 표준 참조. "스펙 → 계획 → 서브에이전트 실행 → 리뷰" 루프가 [[Claude-Code-워크플로우]]의 사실상 레퍼런스가 될 가능성.
- **대체 관계**: [[hermes-agent]]·LangChain 같은 프레임워크 대비 "코딩 에이전트 개발 프로세스"에 특화. [[agency-agents]]와는 경쟁이 아니라 상보(방법론 vs 역할 카탈로그) — 함께 쓰기 좋음.
- **허와 실**: "완결된 방법론"은 강력하지만 그만큼 **에이전트를 특정 프로세스에 강하게 구속**한다. 빠른 단발 태스크엔 오버헤드일 수 있고, 자동 트리거가 의도치 않게 개입할 여지. TDD·리뷰 강제가 맞지 않는 워크플로우도 존재.
- **액션**: 공식 마켓플레이스에서 설치 → 서브에이전트 주도 개발 루프를 내 실제 태스크에 1회 돌려보고 [[agency-agents]] 역할 프리셋과 조합 가능성 검증.

> [!question] 미해결 질문
> Monday 스킬 시스템([[Claude-Code-워크플로우]])과 자동 트리거가 충돌하지 않는가? 스킬 발동 조건을 세밀히 통제할 수 있는지 확인 필요.

> [!action] 당장 할 것
> `/plugin install superpowers@claude-plugins-official`로 설치 → 스킬 정의·조합 구조 분석 → [[agency-agents]] 역할 프리셋과 [[caveman]] 출력 압축을 얹은 조합 워크플로우 실험.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]
- [[agency-agents]]
- [[strix]]
- [[video-use]]
- [[caveman]]
- [[hermes-agent]]
- [[multica]]

## 원본
- 출처: https://github.com/obra/superpowers
- 스타: ⭐268,947 (2026-08-08 자동수집, 당일 +782) ← ⭐268,380 (08-07, +858) ← ⭐261,293 (07-26 WebFetch 실검증) ← ⭐252,676 (07-12) ← ⭐244,962 (07-03) ← ⭐225,402 (06-13) ← ⭐224,143 (06-11) ← ⭐193,260 (05-16) ← ⭐174,963 (04-30)
- 신뢰도: ⭐⭐⭐⭐⭐ (24만+ 스타, Anthropic 공식 마켓플레이스 등재, 전임 커뮤니티 엔지니어 채용 — 방법론 수준 인정)
