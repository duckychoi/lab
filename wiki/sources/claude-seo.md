---
title: "claude-seo — 26 스킬·19 에이전트 SEO 감사 플러그인. 유일한 성과 근거는 '자기 이름을 딴 사이트'의 12주 트래픽이라 효과와 레포 인기가 분리되지 않는다"
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code-plugin, agent-skills, seo, geo, multi-agent, self-reported, 오픈코어]
created: 2026-10-26
updated: 2026-10-26
sources: [https://github.com/AgriciDaniel/claude-seo]
reliability: medium
---

# AgriciDaniel/claude-seo — ★21,523 · Python · MIT

> [!insight] 핵심 인사이트 — **[[에이전트-스킬]]이 "직군 전체 패키지"로 팔리는 형태의 완성형, 그리고 그 증거 구조의 약점**
> 구성 수치는 실측으로 맞다: `skills/` 26개, `agents/` 19개(GitHub contents API). `/seo audit` 하나가 최대 17개 에이전트를 병렬로 펼쳐 기술 SEO·E-E-A-T·Schema·GEO(AI 검색 인용)·로컬·이커머스를 훑고 우선순위 액션 플랜(Markdown/PDF)을 낸다. [[marketingskills]]가 보여준 "스킬 1층이 비코딩 직군으로 넘어감"의 SEO 단일 직군 심화판.
> 그러나 **성과 근거가 단 하나**이고 교란되어 있다: *"The project's own site, claude-seo.md … 10.8K Search Console clicks in its first 12 weeks"*. 그 사이트는 ★2만 레포의 공식 랜딩이므로 클릭이 **SEO 작업 덕인지 GitHub 인기 덕인지 분리 불가**. 대조군 없음, 제3자 사이트 사례 없음 → [[스타-근거-비동행]]·[[관심-검증-역상관]].

> [!warning] 자기보고 수치 / 빠진 맥락
> - 10.8K clicks에 붙은 원문 맥락: **324K impressions, 2026-03-23~06-12**, 모바일 PageSpeed 99(SVG 이미지로 제시, 원 데이터 링크 없음). 수집기 요약은 기간·노출수 누락.
> - README 배지 `tests-1077 passing`은 CI 연동 배지가 아니라 **정적 shields.io 배지**(값이 하드코딩) — CI 배지는 별도로 존재.
> - 가격 비교의 "에이전시 1년 $106,500"은 README 스스로 *"Illustrative pricing"*.
> - **두 버전**: 공개판 MIT 외에 유료 커뮤니티(Skool "AI Marketing Hub Pro") 회원용 **비공개판(신기능 조기 접근)** 이 있음 → 오픈코어형 퍼널. 레포 homepage도 skool 링크.
> - 비용: 5개 에이전트는 Opus, 나머지 Sonnet → 전체 감사는 Claude 플랜 사용량이 큼(README 명시). 분석 대상 페이지는 Claude로 전송됨(README FAQ).

## 도메인별 추출 (ai-news)

- **신뢰도**: ★21,523 · fork **2,979**(13.8%, 높음 = 실제 설치·개조 많음) · open issues 52 · created 2026-02-07 · pushed 10-22 · 논문·제3자 벤치 없음.
- **즉시 활용**: **조건부 YES** — 볼트 자체엔 SEO 대상이 없음. 영상 SaaS 랜딩/블로그를 운영할 때 `/seo audit`·`/seo geo` 1회 실행 가치는 있음(MIT, 로컬 실행). 단 결과는 "체크리스트 자동화"로 받고 순위 효과 기대는 금물.
- **6개월 영향력**: 중간 — 이 레포보다 **구조**(직군=스킬 묶음+역할 에이전트+단일 슬래시 진입점)가 확산 패턴. [[gstack]]의 엔지니어링판과 같은 설계.
- **대체 관계**: Screaming Frog·SaaS 감사툴의 "설명·우선순위" 부분만 대체(README 스스로 크롤 속도·백링크 DB는 기존 툴이 낫다고 인정). [[everything-claude-code]]·[[claude-howto]]와 같은 Claude Code 확장 묶음 층.
- **허와 실**: 실 = 26/19 구성, 헤드리스 브라우저 렌더링, Google API(GSC·CrUX·PSI) BYOK 연동, drift 모니터링(SQLite 스냅샷). 허 = "Rank in Google, get cited by AI"라는 결과 약속의 증거가 자기 사이트 1건.
- **액션**: star 보류. 필요 시 `skills/seo-geo` SKILL.md만 읽어 GEO 체크리스트를 참고 — 플러그인 전체 설치는 영상 SaaS 랜딩 공개 시점에.

## 관련 페이지
- [[에이전트-스킬]] · [[Claude-Code-워크플로우]] · [[스타-근거-비동행]] · [[관심-검증-역상관]]
- 유사: [[marketingskills]] · [[everything-claude-code]] · [[claude-howto]]
- 같은 배치: [[experiential]] · [[sandbox-runtime]] · [[gstack]] · [[infinite-canvas]]
- [[ai-news]]

## 원본
- 출처: https://github.com/AgriciDaniel/claude-seo · README raw 22,871 B
- 볼트 실측(GitHub API, 2026-10-26T09:07Z): ★21,523(수집기 21,511, +12) · fork 2,979 · open issues 52 · MIT · Python · created 2026-02-07 · pushed 2026-10-22T16:47Z · skills/ 26 · agents/ 19
- 신뢰도: ⭐⭐ (★2.1만 · 성과 근거는 교란된 자기보고 1건)
