---
title: "cathrynlavery — 다이어그램 생성 스킬 제공자"
type: entity
domain: ai-news
tags: [entity, github, agent-skills, diagram, svg, 접근성, 공급망]
created: 2026-10-10
updated: 2026-10-10
sources: [diagram-design.md]
reliability: medium
---

# cathrynlavery

**GitHub**: https://github.com/cathrynlavery

> [!insight] 핵심
> [[diagram-design]] 의 제공자. **44종 다이어그램을 자기완결 `.html` 1개(HTML+SVG)로 출력**하는 에이전트 스킬을 만들고, **출력 크기 프리셋이 viewBox 와 폰트 램프를 함께 바꾸는** 설계를 쓴다(투사 슬라이드 16px · 문서 12px).
> 🎯 **볼트 수집 중 유일한 "출력매체-인식" 제공자다** — 산출물이 어디에 표시되는지가 타이포그래피를 결정한다.

> [!insight] 🏆 두 가지 선제 경고를 README 에 넣었다
> ① **배포 출처 봉인** — *"Official builds come only from this repository… a listing under any other name is an unofficial copy"* → 🆕 [[배포출처-봉인]] **신설 계기**
> ② **프라이버시 분리** — `PRIVACY.md` 로 네트워크 전송 항목을 따로 둔다
> 📌 같은 날 [[mattpocock]] 은 **중복 설치**를 경고했고 이쪽은 **출처 사칭**을 경고했다 ⇒ **두 종류의 선제 경고가 동시에 나왔다.**

> [!note] 확인된 것
> - [[diagram-design]]: ★**48,325** · 당일 **+1,739** · fork 3,057 · MIT · **HTML** · created **2026-04-16** · pushed 2026-10-10
> - `open_issues` 81 = 순수이슈 20 + PR **61** ⇒ PR 비중 **75.3%**(배치 상위값)
> - ✅ **접근성 처리 보유**: 스크린리더 제목·설명 · `prefers-reduced-motion` 정적 프레임
> - 호스트 9종 이상 지원 명시(Cursor·Claude Code·Codex·Copilot·Gemini CLI·Cline·Windsurf·Amp·Zed·Warp·Roo·Kilo) — **미검증**
> - 🔴 **트렌딩 4위인데 당일 증분이 3위보다 크다**(+1,739 > +1,687) ⇒ [[지표-창길이]] 반례 실측

> [!warning] 🔴 미확인
> 개인 실체·직업·소속 **미조회**(GitHub 프로필 미열람).
> 🔴 **다이어그램 품질·정확도 측정 0개** — 44종은 기능 카운트다.
> 🔴 *"No shadows. No Mermaid slop."* 는 **마케팅 문구**이므로 볼트 요약에서 제외했다.

## 관련 페이지
- [[diagram-design]] — 주 저장소
- [[배포출처-봉인]] — 신설 계기를 제공
- [[reat]] — 레이아웃·타이포 램프 적용 대상
- [[지표-창길이]] · [[에이전트-스킬]] · [[mattpocock]] · [[ai-news]]

## 원본
- 대표 산출물: [[diagram-design]] (GitHub ★48,325)
- 신뢰도: ⭐⭐⭐ (저장소 메타 실측 · 제공자 실체 미확인)
