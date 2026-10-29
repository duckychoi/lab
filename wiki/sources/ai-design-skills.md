---
title: "elayadesign/ai-design-skills — ★1만인데 스킬 1개. 급등 구간에 있던 2번째 스킬은 하루 전에 레포를 떠났다"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, design, landing-page, claude-code, cursor, codex, anti-ai-slop, 파생]
created: 2026-10-28
updated: 2026-10-29
sources: []
reliability: medium
---

# elayadesign/ai-design-skills

**GitHub**: https://github.com/elayadesign/ai-design-skills · ★**10,275** · fork 739 · open issues 7 · **MIT** · created 2026-07-29 · pushed 2026-10-27T16:02:10Z · 볼트 관측 2026-10-28T09:10Z
**신뢰도**: ⭐⭐ medium (★는 1만이지만 실체는 SKILL.md 1개 18.8KB. 레포 전체 파일이 5개다)

> [!insight] 🏆 핵심 인사이트: **★1만의 실체는 18.8KB 마크다운 1개이고, 급등을 설명할 수 있는 다른 후보는 이미 빠져 있다**
> - git tree 실측: `README.md`(2.4KB) · `LICENSE` · `.gitignore` · `skills/landing-page-design/SKILL.md`(**18,801B**). 이게 레포의 전부다. 수집기의 "현재 스킬 1개"는 맞다.
> - 🔴 **수집기가 빠뜨린 것은 커밋 로그다.** 07-29 첫 업로드 이후 3개월 동안 커밋이 없다가 **10-25에 `design-to-motion` 스킬이 추가됐다**(정적 디자인을 픽셀 단위 애니메이션 쇼케이스로 바꾸고 X용 MP4·800×500 GIF로 내보내는 스킬). 그리고 **10-27 15:57Z에 "Move design-to-motion to its own repo"로 제거됐다.** 커밋 메시지가 가리키는 `elayadesign/Design-to-motion`은 API에서 **404**다(비공개거나 아직 안 만들어진 것으로 보인다. 확인하지 못했다). 계정의 공개 레포는 3개뿐이다(`ai-design-skills` · `redesign-skill` ★409 · `skills` ★4).
> - ⇒ ⚖️ 트렌딩 당일 +1,395(수집기)가 쌓인 구간은 **스킬이 2개였던 사흘(10-25~10-27)과 겹친다.** 지금 별을 누르는 사람이 받는 것은 그중 1개뿐이다. 인과는 증명할 수 없다(별 시계열 미보유). "이 레포의 무엇이 별을 모았나"에 대한 답이 **이미 레포에 없는 물건일 수 있다**는 점만 적어 둔다 → [[선발창-누락]].
> - 📌 **파생 관계도 있다**: README·SKILL.md Credits에 *"adapts content realism and motion ideas from [[taste-skill]] by Leon Lin, MIT"* 라고 적혀 있다. 10-26 커밋은 *"Rewrite the motion/navigation and content realism sections in original wording, and remove the upgrade techniques list"* 다. 원본 taste-skill은 지금 **★103,923**(볼트 05-29 기록 27,221)이다. 파생이 원본의 1/10 규모로 따라붙은 사례다 → [[파생저장소-식별]].
> - 📌 커밋 5건 전부 `Co-Authored-By: Claude Opus 5.5` 트레일러가 달려 있다. Claude Code로 작성·관리되는 디자인 스킬이다.

> [!warning] 🔴 같은 날 수집된 디자인 스킬 3종의 규칙이 서로 충돌한다 (볼트 대조)
> `landing-page-design` 규칙을 오늘 볼트가 처음 열어 본 [[impeccable]]의 결정론적 규칙 62개 목록(`crates/live/assets/antipatterns.json`)과 대조했다.
> | landing-page-design 지시 | impeccable 규칙 |
> |---|---|
> | B1 폰트 **"Use: Geist, Manrope, Geist Mono, Poppins"** | `overused-font`: *"Inter, Roboto, Fraunces, **Geist**, Plus Jakarta Sans, Space Grotesk"* 를 슬롭으로 표시 |
> | B5 히어로 제목에 **흑→회색 그라디언트 텍스트**(`#FFFFFF → #9B9B9B`) 필수 | `gradient-text` (slop 카테고리) |
> | A5 예시 문구 *"**Faster iteration** — generate three layout variants…"* (em dash) | `em-dash-overuse` |
> | B7 스크롤 리빌: 섹션이 **opacity 0에서** 페이드인 | `content-hidden-at-rest` (**severity error**, 62개 중 error 2개 중 하나): 리빌이 실패하면 텍스트가 opacity 0에 남는 것을 출하 차단급으로 본다 |
> ⇒ ⚖️ **"안티 슬롭"은 단일 기준이 아니다.** 한 스킬이 권장하는 것이 다른 스킬에서는 슬롭이다. [[hallmark]] 10-27 기록의 *"안티 슬롭은 결국 취향의 코드화"* 우려가 **실제 규칙 수준의 충돌로 확인됐다**(n=1 쌍). 두 스킬을 같은 프로젝트에 같이 깔면 서로의 산출물을 지적하게 된다.
> ✅ 공통점도 있다: `prefers-reduced-motion` 존중(B7)·포커스 링 필수(B9)·Inter 금지·한쪽 테두리 카드 금지(체크리스트 *"No single sided card borders"* ↔ impeccable `side-tab`)는 일치한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ★10,275(볼트 실측) · MIT. 내용은 18.8KB 규칙 문서 1개라 별 수 대비 정보량이 적다. 효과를 보여주는 예시 산출물이나 평가가 레포에 없다.
- **즉시 활용**: **부분 YES**. 랜딩페이지 한 장을 새로 만들 때 Part A(인터뷰 질문 → 섹션 구조 → 전환 카피 → SEO/AEO)는 바로 쓸 수 있다. Part B(시각 규칙)는 위 충돌 때문에 [[impeccable]]·[[hallmark]]와 섞으면 안 되고 하나만 골라야 한다.
- **6개월 영향력**: 낮음~중간. 구조는 "디자인 값이 파일 하단 한 섹션(`Make it yours`)에 모여 있어 포크하면 나머지가 따라온다"는 점이 특징인데, 이건 [[design-md]] 계열의 "토큰 파일 분리"와 같은 생각이다. 컬렉션이 "growing"이라고 하지만 3개월 동안 늘어난 스킬은 0개(+1 추가 후 제거)다.
- **대체 관계**: [[taste-skill]]의 일부를 다시 쓴 파생물이다. [[hallmark]](50 테마 + 브라우저 린트)·[[impeccable]](62 결정론 규칙 + Rust 엔진)과 비교하면 **검사 도구가 없는 순수 지시문**이다. 지시만 있고 검증 단계가 없다.
- **허와 실**: 수집기 평가("기대치를 낮춰야")는 맞다. 다만 이유가 더 있다. ① 급등 구간의 2번째 스킬이 이미 빠졌고 ② 원본(taste-skill)이 10배 크며 ③ 규칙 일부가 다른 안티 슬롭 도구와 정면으로 충돌한다. 규칙 중 "본문에 하이픈 금지"·"이탤릭 전면 금지"·"폰트 1종만"·"태그라인 리빌 섹션 **필수**(B11)"는 근거가 적혀 있지 않은 취향 규칙이다.
- **액션**: star 불필요. 필요할 때 SKILL.md의 **Part A(A1 Intake 질문 목록)만** 발췌해 쓴다. Part B를 쓰려면 [[impeccable]] 규칙 중 `overused-font`·`gradient-text`를 끄거나 둘 중 하나만 설치한다.

> [!question] 미해결
> - `elayadesign/Design-to-motion`이 공개되면 그쪽이 실제 관심의 대상이었는지(별 이동 여부) 확인할 수 있다.
> - 작성자 실체 미확인: GitHub 계정 `elayadesign`(name "Elaya", 팔로워 253, 2025-06 가입)만 확인했다.

## 관련 페이지
- [[taste-skill]] (원본) · [[hallmark]] · [[impeccable]] · [[design-md]] · [[superdesigndev]]
- [[에이전트-스킬]] · [[Claude-Code-워크플로우]] · [[파생저장소-식별]] · [[선발창-누락]]
- 같은 배치: [[superpowers]] · [[openbot]]
- [[ai-news]]

## 원본
- 출처: https://github.com/elayadesign/ai-design-skills
- 볼트 실측(GitHub API, 2026-10-28T09:10Z): ★10,275 (수집기 10,268 → **드리프트 +7**) · fork 739 · issues 7 · MIT ✅ · created 2026-07-29 ✅ · pushed 2026-10-27T16:02:10Z
- 확인 범위: README 2,464B 전문 · SKILL.md 18,801B 섹션 구조와 B1·B5·B7·B8~B11 본문 · git tree 전체(파일 5개) · 커밋 8건 · 계정 공개 레포 목록. 🔴 미실행.
- 신뢰도: ⭐⭐ (★1만이지만 스킬 1개·평가 없음)

## 🔄 2026-10-29 갱신 (인제스트 2026-10-29) — **커밋 없이 하루 ★+1,293. `Design-to-motion` 레포는 여전히 404**

**GitHub API 실측(2026-10-29T09:06Z)**: ★ **11,568**(수집기 11,565 · **+3**) · MIT ✅ · pushed **2026-10-27T16:02:10Z**(10-28 과 동일 — **신규 커밋 0**)
- `skills/` 디렉터리 실측 = **`landing-page-design` 1개** ✅(수집기 "스킬 하나뿐" 일치) · 최근 커밋 3건 모두 10-26~27 의 design-to-motion 추가→이전.
- 🔴 `elayadesign/Design-to-motion` API **404 유지**(10-28 에 이어 2일째) — 커밋 메시지가 가리키는 이전 대상이 아직 공개되지 않았다.
- 📈 10-28 ★10,275 → 10-29 ★11,568 = **+1,293/일**, 코드 변화 없음 ⇒ 급등은 내용이 아니라 노출(트렌딩 2위 자체의 순환 효과)로 보인다 → [[스타-근거-비동행]].
- ✅ 수집기 "스타 수에 비해 내용이 얇음" — 10-28 볼트 판정(18.8KB 1개)과 같은 결론. 이번엔 **유리한 표면만 남기지 않았다** ✅.
