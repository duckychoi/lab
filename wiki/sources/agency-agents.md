---
title: agency-agents — 역할별 전문 서브에이전트 프리셋 집합(AI 에이전시)
type: source
domain: ai-news
tags: [ai-news, github-trending, multi-agent, agency, automation, roles, process, claude-code]
created: 2026-05-07
updated: 2026-07-21
sources: []
reliability: high
---

# msitarzewski/agency-agents

> [!update] 2026-07-21 갱신 — WebFetch 실검증
> GitHub ⭐**135,000**(WebFetch 실확인, raw ⭐135,081·+862/일과 일치) ← ⭐126,006(07-03). 18일간 +9천으로 13.5만 돌파, "230+ 역할별 서브에이전트" 규모도 실확인. 12만 후 유입은 완만해졌으나 여전히 성장 — "AI 에이전시 역할 카탈로그" 수요가 장기 트렌드로 굳어짐. 같은 07-21 배치의 [[ai-agent-book]](설계 원리 책)·[[ai-engineering-from-scratch]](구현 커리큘럼)과 함께 "에이전트를 **페르소나·원리·구현** 세 층에서 조립하는 재료" 계열을 형성.

> [!insight] 핵심 인사이트
> 프론트엔드·리서치·QA 등 **역할별 전문 서브에이전트 프리셋 모음**. 각 에이전트는 페르소나(personality)·프로세스(workflow)·산출물(deliverable) 템플릿이 사전 정의돼 있어, [[Claude-Code-워크플로우]]나 Cursor·Codex·Gemini 등 코딩 에이전트에 "역할을 꽂아" 쓰는 방식이다. ⭐126,006(2026-07-03, 당일 +3,032)로 12만 돌파 후에도 일 유입이 +1.8천→+3.0천으로 재가속 — "AI 에이전시" 구성 템플릿 수요가 단발 트렌드가 아님을 재확인. [[superpowers]]가 "방법론+스킬 체계"라면 agency-agents는 "역할 페르소나 카탈로그"로, 같은 배치의 [[superpowers]]·[[strix]]·[[video-use]]와 함께 *에이전트를 조립하는 재료* 계열에 속한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐126K, 커뮤니티 검증 완료. Reddit 스레드 발원 → 수개월 반복으로 다듬어진 로스터. 네이티브 앱(agencyagents.app, macOS·Linux·Windows)까지 출시돼 배포 성숙도 높음.
- **즉시 활용**: YES — `./scripts/install.sh --tool claude-code` 또는 `cp engineering/*.md ~/.claude/agents/` 후 "activate Frontend Developer mode"로 즉시 사용. 진입장벽 낮음.
- **6개월 영향력**: 높음 — 에이전시 패턴이 개인 워크플로우 → 팀 업무 자동화로 확장. "역할 카탈로그"가 코딩 에이전트의 기본 부속이 되는 흐름.
- **대체 관계**: [[superpowers]](방법론+스킬), [[swarms]](엔터프라이즈), [[hermes-agent]](오픈소스 프레임워크), [[multica]](매니지드) 대비 **역할 페르소나·산출물 명세화**에 특화. 프레임워크 대체가 아니라 그 위에 얹는 프리셋.
- **허와 실**: 사전 정의된 역할 구조가 강점이자 제한 — 창의적·비정형 태스크엔 유연성 부족 가능. 상당수는 "정교한 프롬프트 템플릿" 성격이라 실제 산출물 품질은 역할별 편차.
- **액션**: star + engineering/ 카테고리 몇 개를 설치해 산출물 품질 체감 → 좋은 역할 명세는 내 자동화 스키마로 흡수.

> [!action] 당장 할 것
> Frontend/QA/Research 역할 3종을 Claude Code에 설치해 동일 태스크로 품질 비교 → 역할(Role)/프로세스(Process)/산출물(Deliverable) 정의 포맷을 [[superpowers]] 스킬 구조와 대조해 내 워크플로우용 템플릿으로 정리.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]
- [[superpowers]]
- [[strix]]
- [[video-use]]
- [[caveman]]
- [[hermes-agent]]
- [[swarms]]
- [[multica]]

## 원본
- 출처: https://github.com/msitarzewski/agency-agents
- 스타: ⭐126,006 (2026-07-03, 당일 +3,032) ← ⭐121,603 (07-01, +1,791) ← ⭐119,654 (06-30) ← ⭐111,911 (06-13) ← ⭐94,058 (05-06)
- 신뢰도: ⭐⭐⭐⭐⭐ (12만+ 스타, 일 유입 재가속 +3.0천, 네이티브 앱 출시)
