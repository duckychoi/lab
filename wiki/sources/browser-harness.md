---
title: "browser-harness — '쓸수록 느는 하네스'의 비용은 PR 큐에 쌓인다"
type: source
domain: ai-news
tags: [ai-news, github-trending, browser-automation, cdp, agent, mcp, 에이전트-스킬, 하네스-설계-축, 에이전트-웹접근]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: high
---

# browser-harness

> [!insight] 🎯 핵심 인사이트: 스킬은 에이전트가 만들고, 병목은 사람의 머지로 옮겨 갔다
> README 5행: *"Connect an LLM directly to your real browser through **one editable CDP websocket**. The agent **writes missing helpers as it works**, so the harness improves with every task."*
> 에이전트가 없는 기능을 `agent-workspace/agent_helpers.py` 에 직접 쓰고, 사이트별 지식은 `domain-skills/<site>/` 로 쌓는다. 🎯 **CONTRIBUTING.md는 이것을 정책으로 적어 두었다.** *"Agent-generated skills reflect what actually works in the browser; **do not hand-author them.**"* 사람이 쓴 스킬은 받지 않겠다는 뜻이다.
> 📌 **그 결과는 PR 큐에서 보인다.** 열린 PR **333**, 열린 이슈 **41**. 볼트 실측으로 열린 PR의 **50%(165/333)** 에 에이전트 생성 흔적(`Generated with Claude Code`·`Co-Authored-By: Claude`·🤖·`codex/` 브랜치)이 명시돼 있고, 제목에 "skill"이 들어간 PR 126건 중에서는 **70%(88건)** 다.
> 🔴 **그런데 main 브랜치는 2026-09-07 이후 머지가 0건이다**(마지막 커밋 #757 머지, Magnus Müller). 그 뒤 새로 열린 PR이 **42건**이다. 🎯 에이전트는 스킬을 싸게 찍어 내고, 검수는 여전히 사람이 한다. [[에이전트-스킬]] 이 09-14에 연 질문(*"어느 스킬이 값을 하나"*, [[COBRA-Skills]])이 **연구가 아니라 운영 문제로 먼저 터진 사례**다.

> [!warning] 🔴 수집기 정정: "가능성(미확인)"이 아니었다. 확인되는 사실이고, 설계 의도이기도 하다
> 수집기 raw: *"README가 'agent-generated domain skills are welcome' 이라 **에이전트 생성 PR 누적 가능성**(미확인)."*
> ✅ **추정 방향은 맞았다.** 🔴 **다만 "가능성"으로 둘 일이 아니었다.** CONTRIBUTING.md가 에이전트 생성을 **요구**하고, PR 본문·브랜치명에서 **165건이 직접 확인된다.** README 59행만 읽고 CONTRIBUTING은 열지 않은 것으로 보인다.
> ⚠️ 볼트 측정의 한계도 적어 둔다. 165는 **명시 흔적만 센 하한**이다. 흔적을 지운 에이전트 PR은 잡히지 않는다. 반대로 🤖 이모지를 사람이 쓴 경우는 과대 계산될 수 있다(표본 수동 확인은 하지 않았다).

> [!note] 📌 PR 큐 실측 (2026-09-22, GitHub API 열린 PR 333건 전수)
> - **고유 작성자 202명**, 1인 최다 11건(`MagMueller`·`gregpr07`·`harrisboatworks`). 소수 봇이 도배한 구조가 아니라 **다수가 조금씩 기여**하는 구조다.
> - 제목 키워드: `skill` 126 · `domain` 100 · `fix` 69 · `docs` 66 · `feat` 24
> - 열린 PR의 생성월 분포: 04월 31 → 05월 42 → 06월 47 → 07월 65 → 08월 67 → **09월 81**(22일 기준). **안 닫힌 PR이 매달 더 많이 생긴다.**
> - 누적: 머지 **278** · 머지 없이 닫힘 **123** · draft 23. 머지 PR 중 제목에 `domain-skill` 이 들어간 것은 55건이다.
> - 레포 트리: `agent-workspace/domain-skills/` 아래 `.md` **107개**, `interaction-skills/` 19개(쿠키·iframe·shadow DOM·업로드 등).
> 🎯 샘플 12건 제목(#819~#831)이 성격을 보여 준다. *"Add Furnished Finder and Airbnb monthly-search domain skills"* · *"domain-skills: Bilbasen.dk search extraction via `__NEXT_DATA__`"* · *"domain-skill: google-flights — deep-link any search via tfs"* · *"Add SF Assessor-Recorder domain skill"* 같은 **사이트별 스킬**과 `fix(helpers)` 계열 코어 수정이 섞여 있다.

> [!warning] ⚠️ README는 짧고 수치가 없다(수집기 ✅)
> ✅ **README 63행**: 볼트 실측과 완전히 일치한다.
> ✅ **정량 성능 수치 0개**: 수치는 예시 과제의 *"latest 20 video posts"* 와 `Python 3.12` 뿐이다. 성공률·지연·비용은 **없다.**
> ✅ 19행 *"**You will never use the browser again.**"* 은 마케팅 문구다.
> ✅ 48행: 병렬·프록시·스텔스·CAPTCHA는 **Browser Use Cloud(유료)** 로 유도한다. 로컬은 *"logged-in, personal work"* 용이다.
> 📌 수치 대신 블로그 두 편(63행: *"The Bitter Lesson of Agent Harnesses"* · *"Web Agents That Actually Learn"*)으로 설계 철학을 대신 설명한다. 볼트는 이 두 글을 **열람하지 않았다**.

> [!note] 🎯 같은 문제에 반대로 답한 두 설계: [[BrowserSkill]] 과의 대조
> [[BrowserSkill]](09-18)은 *"에이전트에게 브라우저를 주지 않고 **탭만 빌려준다**"* 였다. 에이전트는 자기 창에 격리된다.
> browser-harness는 정반대다. `chrome://inspect/#remote-debugging` 체크박스 하나로 **로그인된 사용자 Chrome 전체**를 CDP로 넘긴다.
> → [[에이전트-웹접근]] 의 접근 층에 **"진짜 세션 전체 위임"** 이라는 네 번째 노선이 생겼다. 편의성은 최대이고 격리는 없다. ⚠️ README에는 권한 범위·보호 장치 설명이 **없다**.
> 📌 [[Electron-CDP-브리지]](API 없는 데스크톱 앱을 CDP 포트로 도구화)와 **같은 CDP 경로**를 웹 브라우저 본체에 쓴 것이다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ ★**18,007** · MIT · [[browser-use]] 조직 공식 · 5개월 만의 규모. 🔴 감점 요인: README 성능 수치 0, **main 머지 15일 정지**, PR 333 적체.
- **즉시 활용**: **YES, 조건부.** Claude Code에 셋업 프롬프트 한 줄이면 설치된다(uv·Python 3.12). `browser-harness-mcp` 로 MCP 도구로도 붙일 수 있다. 🔴 **단 로그인된 실사용 Chrome 전체를 넘긴다.** 개인 계정 작업용 **별도 Chrome 프로필**을 만든 뒤 붙여야 한다.
- **6개월 영향력**: 🎯 **"브라우저 자동화 스크립트를 짠다"가 "에이전트가 쌓아 둔 스킬 폴더를 공유한다"로 바뀐다.** 사이트별 셀렉터·함정을 사람이 문서화하지 않고, 에이전트가 성공한 경로를 남긴다. 병목은 그 스킬의 **검수와 노후화**(사이트가 바뀌면 스킬도 낡는다)로 이동한다.
- **대체 관계**: [[browser-use]] 본체(113k, 조작 논리 + 자체 루프)와 층이 다르다. harness는 **루프를 외부 코딩 에이전트(Claude Code·Codex)에 맡기고 도구만 준다.** [[camofox-browser]]·[[CloakBrowser]] 의 지문 위조는 필요 없다. 진짜 세션이기 때문이다.
- **허와 실**: 걷어내면 남는 것은 **CDP 헬퍼 + 스킬 폴더 규약 + MCP 래퍼**다. 🔴 "매 작업마다 나아진다"는 주장은 **측정된 적이 없다**. 스킬 107개가 쌓였다는 것은 사실이지만, 스킬이 성공률을 올린다는 수치는 없다.
- **액션**: 아래.

> [!action] 당장 할 것
> 별도 Chrome 프로필에 붙여 **같은 과제를 `BH_DOMAIN_SKILLS=1` 켠 상태와 끈 상태로 각 3회** 돌린다(예: 볼트 운영자가 자주 쓰는 사이트 1곳). **스킬이 실제로 값을 하는지**를 README가 주지 않는 수치로 직접 잰다.

## 관련 페이지
- [[BuilderIO]]  *(09-22 연결)*
- [[browser-use]]: 같은 조직의 본체
- [[BrowserSkill]]: 🎯 반대 노선(탭 대여·격리)
- [[에이전트-웹접근]] · [[Electron-CDP-브리지]] · [[camofox-browser]] · [[CloakBrowser]]
- [[에이전트-스킬]] · [[COBRA-Skills]]: 스킬 가치 평가 문제
- [[하네스-설계-축]] · [[검사가능성-공사]]
- [[Agent-Native]]: 같은 배치. **UI를 클릭하지 않는** 반대 설계
- [[ai-news]]

## 원본
- 출처: https://github.com/browser-use/browser-harness
- 볼트 실측(2026-09-22, GitHub API): ★**18,007**(raw 17,911 대비 +96) · fork 1,758 · **MIT** · Python · open issues **374** = PR **333** + 이슈 **41**(search API, raw 329/41, 하루 새 PR +4) · created 2026-04-17T01:56:15Z ✅ · pushed 2026-09-12T08:30:02Z ✅ · **main 마지막 커밋 2026-09-07T20:13:31Z** · topics 14 · homepage browser-harness.com
- 수치 출처: README 5·12·19·29·48·59·63행, CONTRIBUTING.md "Domain skills" 절 **원문 실열람**, 열린 PR 333건 전수(pulls API 4페이지), search API(merged 278 / closed-unmerged 123 / `merged:>2026-09-07` 0 / `created:>2026-09-07` open 42)
- raw 대비: 볼트 추가 = 🔴 **"에이전트 PR 가능성(미확인)" → CONTRIBUTING이 요구하는 설계이고, 열린 PR 50%에서 흔적 직접 확인** · 🔴 **main 머지 15일 정지(raw 미기재)** · ✅ README 63행·수치 0·유료 Cloud 유도 전부 확인 · 🎯 **[[BrowserSkill]] 과의 반대 노선 대조**
- 신뢰도: ⭐⭐⭐ (지표·라이선스 확인 / 성능 수치 0 · 머지 정지 · 권한 범위 미기재)
