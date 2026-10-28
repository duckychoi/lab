---
title: Nutlope/hallmark — 안티-AI슬롭 디자인 스킬 (에이전트 UI 품질 개선)
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, agent-skills, design, frontend, anti-ai-slop, css]
created: 2026-07-16
updated: 2026-10-28
sources: []
reliability: high
---

# hallmark (Nutlope/hallmark)

> [!insight] 핵심 인사이트
> ⭐**9,734 (2026-07-16, 당일 +1,277 — 신규 급상승)**. Claude Code·Cursor·Codex 같은 코딩 에이전트에 주입하는 **"안티-AI슬롭(anti-AI-slop) 디자인 스킬"**. AI가 UI를 생성할 때 나오는 획일적·조잡한 결과물(보라 그라디언트, 과한 그림자, 무의미한 이모지, 뻔한 레이아웃)을 억제하고 절제된 디자인 규칙(주로 CSS·디자인 토큰 가이드)으로 유도한다. Vercel 계열 개발자([Hassan/Nutlope](https://github.com/Nutlope), llama-ocr·roomGPT 제작자)의 브랜드 파워 + 에이전트 스킬 생태계 폭발이 만난 사례. [[mattpocock-skills]]·[[agent-skills]]가 *작업 절차*를 표준화한다면 hallmark는 *미적 산출물의 하한선*을 규정하는 스킬 — 스킬이 "무엇을 하는가"에서 "얼마나 잘 보이게 하는가"로 확장됐다.

> [!action] 당장 할 것
> reat-* 슬라이드·[[tools-frontend]] 오버레이·pptx 생성 등 내가 만드는 프론트엔드 산출물의 디자인 품질에 직접 이식 후보. hallmark 규칙 세트를 스킬로 편입해 AI 생성 UI의 "슬롭" 억제 효과를 스팟체크.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐9.7K·당일 +1,277로 급상승, 제작자 salience 높음. 다만 "디자인 품질 개선"은 주관적 평가라 실효는 직접 적용 후 판단 필요.
- **즉시 활용**: YES(후보) — 내 프론트엔드 산출물(슬라이드·오버레이·랜딩)이 정확히 "AI 슬롭" 위험군. CSS/디자인 규칙 스킬은 도메인 무관 재사용 가능.
- **6개월 영향력**: 에이전트 코딩이 늘수록 "결과물이 다 똑같다"는 슬롭 문제가 부각 → 디자인 가드레일 스킬이 절차 스킬만큼 중요해지는 흐름.
- **대체 관계**: [[hallmark]]는 [[stitch-skills]]·[[google-skills]] 같은 UI 생성 스킬과 상보 — 생성이 아니라 *억제/정제* 측. shadcn/ui·Tailwind 기본 프리셋의 한계를 규칙으로 보완.
- **허와 실**: "안티 슬롭"은 결국 취향의 코드화. 규칙이 또 다른 획일성(hallmark 룩)을 낳을 위험도 있어 맹신은 금물.
- **액션**: 규칙 세트 클론 → reat 슬라이드/tools-frontend에 1개 화면 적용 A/B로 슬롭 억제 효과 확인.

## 관련 페이지
- [[mattpocock-skills]]
- [[agent-skills]]
- [[stitch-skills]]
- [[tools-frontend]]
- [[Claude-Code-워크플로우]]
- [[ai-news]]

## 원본
- 출처: https://github.com/Nutlope/hallmark
- 신뢰도: ⭐⭐⭐ (GitHub ⭐9,734, 당일 +1,277 — raw 자동수집 수치)

## 🔄 2026-10-27 갱신 (인제스트 2026-10-27) — **103일에 ★3.85배. 수집기 요약의 '48테마·3단 게이트'는 README 원문과 일치**

**GitHub API 실측(2026-10-27T09:05Z)**: ★ **37,498**(수집기 37,485 · +13) · fork 1,953 · open issues 64 · **MIT** · 주언어 CSS · created 2026-04-27 · 🔴 pushed **10-22**(5일 전)
- 볼트 기준선 ★9,734(07-16) → **+27,764 / 103일 ≈ 270/일** · 금일 트렌딩 +2,244(수집기) — 장기 평균의 8배가 하루에 들어왔다(재점화).
- ✅ README 원문 대조(8,121B): *"Made by **Together AI**"* · *"forty-eight themes"* · *"deals **three themes** from a catalog of forty-eight"* · *"lints the result in a **real browser**"* · 게이트 3단 **Floor**(대비·포커스·reduced motion·**지어낸 사실**·모바일 깨짐 — *never ships*) / **Reflex**(모델이 빠지는 기본값 — 근거 있으면 기록 후 무시 가능) / **Finish** — 수집기 서술 **전건 일치**.
- 🆕 07-16 판에 없던 것: **제작 주체가 Together AI** 로 명시(개인 레포 → 기업 산출물) · 실제 브라우저 린트 단계.

> [!insight] Floor 게이트에 *"invented facts"* 가 들어 있다 — 디자인 스킬이 **허위 수치(가짜 고객 수·통계)를 출하 차단 사유**로 둔다. 볼트 [[인용-부호]]·[[비매칭-비교]] 계열 규약이 UI 층에서도 같은 형태로 나타났다.
> 📌 같은 배치 [[Trial-by-Trace]]: 하네스 부가 스킬도 "과제 성공 vs 기준 위반" 2층으로 볼 수 있다 — hallmark 의 Floor/Reflex 구분이 바로 그 2층(절대 기준 vs 근거 있으면 예외).

## 🔄 2026-10-28 갱신 (인제스트 2026-10-28) — **48→50 테마는 어제 관측 2시간 뒤에 들어왔다. 'v2 신기능'은 대부분 어제 README에 이미 있었다**

**GitHub API 실측(2026-10-28T09:10Z)**: ★ **39,652**(수집기 39,645 · **+7**) · fork 2,074 · open issues 64 · **MIT** ✅ · 주언어 CSS · topics 0 · pushed **2026-10-28T08:48:31Z**(관측 22분 전, 커밋 *"Add third-party notices"*)
- 볼트 기준선 ★37,498(10-27T09:05Z) → **+2,154 / 약 24시간**. 수집기 "당일 +2,830"과는 집계 창이 다르다(트렌딩 창 ≠ 볼트 관측 간격).
- 🔴 **어제 기록 "pushed 10-22(5일 전)"은 관측 시점에는 맞았지만 2시간 만에 만료됐다**: 10-27 10:35Z~15:05Z 커밋 6건(PR #96 *"fifty-themes"*: Refract·Vantage 테마 추가 + #84·#89 수정). 볼트 관측 09:05Z 직후다. "정체" 판정에는 관측 시각을 붙여야 한다는 [[superpowers]] 09-26 교훈의 재현이다.
- ✅ **README 원문 대조(8,125B, 어제 8,121B)**: *"fifty themes"* · *"755 openly licensed photos"* · `/hallmark redesign <path>` · `/hallmark audit <path>` · *"`scripts/sloplint.mjs --render` checks the page at **eight widths**, then a subagent reviews it with fresh eyes"* · *"needs `npm i -g puppeteer-core` and Chrome; without them the static checks still run"* — 수집기 서술 **전건 일치**.
- ⚖️ **"v2 신기능"이라는 표현의 지위**: README 크기가 어제와 4바이트 차이이고 오늘 바뀐 것은 테마 수(48→50)와 표기뿐이다. 즉 `## New in v2` 절(사진 755장·redesign/audit·Custom 모드·URL/dev server 스크린샷 캡처)은 **어제 볼트가 읽은 README에도 있었을 가능성이 높다.** 어제 볼트 기록은 게이트 3단만 적고 이 절을 옮기지 않았다(볼트 쪽 누락).

> [!warning] 🔴 수집기 요약이 빠뜨리거나 뭉갠 것
> 1. **"라이선스 사진 755장"은 레포에 사진이 들어 있다는 뜻이 아니다.** README: *"The photo library (`photos.json`) lists photographs hosted on **Wikimedia Commons** and **holds no image files**. Each keeps its own licence (CC0, public domain, **CC BY or CC BY-SA**)."* ⇒ 산출물이 외부 URL을 참조하고, **CC BY-SA 사진이 섞이면 동일조건 변경허락 의무**가 생긴다. "MIT라서 상업 사용 자유"는 코드에만 해당한다.
> 2. 스톡 사이트를 안 쓰는 이유가 적혀 있다: *"It does not use stock sites (Unsplash, Pexels, Pixabay), **whose terms bar AI tools from picking their images**."* 내 reat-*·pptx 파이프라인이 Unsplash를 자동 선택한다면 같은 약관 문제가 있다(볼트 확인 필요).
> 3. **redesign 안전장치**: `sloplint --before`가 모든 링크·필드·핸들러·제목을 먼저 기록하고 `sloplint --kept`는 *"fails the redesign if one went missing"*. 재디자인이 기능을 지우는 것을 결정론적으로 막는 장치다. 수집기는 명령 이름만 적었다.
> 4. Claude Code용 **편집 시점 Floor 훅**(`install-hook.mjs`)이 있다. 스킬이 생성 시점이 아니라 **편집할 때마다** 검사할 수 있다.

> [!insight] 🎯 같은 배치 대조 — hallmark의 "기계 티" 목록이 [[impeccable]] 규칙 ID와 1:1로 겹친다
> hallmark README의 tell 목록 *"the eyebrow above every heading, tracked-capital labels, one coloured word in a headline…"* ↔ impeccable `antipatterns.json`의 `kicker-above-heading` · `hero-eyebrow-chip` · `wide-tracking` · `gradient-text`. 서로 인용하지 않는 두 프로젝트(Together AI / pbakaus)가 **같은 증상 목록**에 도달했다 → [[검사가능성-공사]]. 🔴 반대로 [[ai-design-skills]]는 impeccable이 슬롭으로 보는 Geist 폰트·그라디언트 텍스트를 **필수로 지시**한다. 안티 슬롭 도구끼리도 합의가 없는 항목이 있다.

**관련 추가**: [[impeccable]] · [[ai-design-skills]] · [[taste-skill]] · [[검사가능성-공사]]
