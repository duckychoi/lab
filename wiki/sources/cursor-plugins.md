---
title: cursor/plugins — Cursor 플러그인 규격 및 공식 플러그인 저장소
type: source
domain: ai-news
tags: [ai-news, github-trending, cursor, plugin, agent-skills, typescript, vendor-official]
created: 2026-08-22
updated: 2026-08-22
sources: []
reliability: high
---

# cursor/plugins — 벤더가 직접 규격을 못박는 쪽으로

**리포**: https://github.com/cursor/plugins
**지표(2026-08-22 GitHub API 실호출)**: ⭐**4,496** · 포크 **369** · 이슈 **52** · **TypeScript** · 생성 2026-01-23 · 최종 푸시 2026-08-21 · 트렌딩 데일리 **8위** (raw 표기 당일 +388)
**설명(원문)**: "Cursor plugin specification and official plugins"
**라이선스**: **명시 없음(GitHub API `license: null`)**

> [!insight] 핵심 인사이트 — 스킬 생태계가 "커뮤니티 수집"에서 "벤더 규격"으로 넘어가는 지점
> 오늘 배치에서 스킬·확장 관련 리포가 셋([[mattpocock-skills]] ⭐23.0만·[[superpowers]] ⭐27.6만·본 리포 ⭐4,496) 동시에 트렌딩에 올랐는데, 앞의 둘이 **개인·커뮤니티가 모은 프롬프트·절차 자산**인 반면 이것은 **툴 벤더가 직접 규격(specification)을 정의하고 공식 플러그인을 배포**하는 리포다. 별 수는 두 자릿수 배 차이지만 **성격이 다르다** — 커뮤니티 컬렉션은 스타가 곧 채택이지만, 벤더 규격 리포는 스타가 아니라 **에디터에 내장되어 강제 배포**되므로 실제 영향력이 스타 수로 측정되지 않는다.
>
> 볼트 맥락에서 이는 [[claude-plugins-official]](Anthropic 공식 마켓플레이스)과 **동형 사건**이다: Anthropic이 [[superpowers]]를 공식 마켓플레이스에 얹었듯, Cursor도 자체 플러그인 규격을 세운다. 즉 **"스킬=배포 단위"가 커뮤니티 관행에서 벤더 계약(contract)으로 굳는 국면**.

> [!warning] 초기 단계 신호가 뚜렷 — 규격 안정성을 신뢰하기 이르다
> ① **라이선스 미명시**(API `license: null`) — 규격을 구현하는 서드파티 입장에서 법적 지위가 불명확. ② 생성 2026-01-23으로 약 7개월, ⭐4,496·포크 369는 이번 배치 GitHub 항목 중 **최소 규모**. ③ 미해결 이슈 52건. 규격은 **파괴적 변경(breaking change)** 가능성이 남아 있다고 보는 편이 안전하다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — **벤더 공식 리포**라는 점에서 출처 신뢰도는 최상급이고 수치는 **GitHub API 실호출로 검증**. 다만 *규격의 성숙도*는 별개이며 초기.
- **즉시 활용**: **NO(현재 워크플로우 기준)** — 내 작업은 [[Claude-Code-워크플로우]] 기반이라 Cursor 플러그인 규격은 직접 접점이 없다. Cursor를 병행 사용할 경우에만 의미.
- **6개월 영향력**: 중간 — 다만 **관전 가치는 높다**. 하니스별 플러그인 규격이 난립하면([[claude-plugins-official]] vs cursor/plugins vs …) 스킬 자산의 **이식성**이 다음 문제로 떠오른다. [[superpowers]]가 이미 멀티 하니스(Claude Code·Cursor·Copilot·Kimi Code) 지원을 내세운 것이 이 압력의 방증.
- **대체 관계**: [[claude-plugins-official]]과 **경쟁 규격**. [[mattpocock-skills]]·[[superpowers]] 같은 자산 컬렉션과는 경쟁이 아니라 **적재 대상 계약**.
- **허와 실**: "official"이라는 단어가 성숙을 뜻하지 않는다 — 라이선스 미명시·7개월 업력·⭐4.5천은 **규격 초안 단계**에 가깝다. 서드파티 생태계 규모는 리포만으로 확인 불가.
- **액션**: 관망. Cursor를 실제 도입하게 되면 규격 문서만 1회 통독해 [[claude-plugins-official]]과의 개념 매핑을 기록.

> [!question] 미해결 질문
> 라이선스 미명시는 의도인가 누락인가? 규격 버전 정책(semver·deprecation)은 있는가? [[superpowers]] 같은 기존 멀티 하니스 스킬이 이 규격을 어떻게 충족하는가?

## 관련 페이지
- [[에이전트-스킬]] — 스킬=배포 단위 개념 축
- [[claude-plugins-official]] — 경쟁 규격(Anthropic 공식 마켓플레이스)
- [[mattpocock-skills]] · [[superpowers]] — 같은 배치 스킬 자산(적재 대상)
- [[SkillEvo]] — 같은 배치, 스킬 유지·진화 상류
- [[Claude-Code-워크플로우]] · [[바이브코딩]]
- [[ai-news]]

## 원본
- 출처: https://github.com/cursor/plugins
- 스타: ⭐4,496 (2026-08-22 GitHub API 실호출·트렌딩 데일리 8위·raw 표기 당일 +388) — 볼트 첫 편입
- 언어: TypeScript · 포크 369 · 이슈 52 · 라이선스 미명시 · 생성 2026-01-23 · 최종 푸시 2026-08-21
- 신뢰도: ⭐⭐⭐⭐ (벤더 공식 리포·수치 API 실검증 — 단 규격 안정성·서드파티 생태계 규모 미검증, 라이선스 미명시)
- 수집: 2026-08-22 아침 자동수집 (GitHub 트렌딩 데일리 8위)
