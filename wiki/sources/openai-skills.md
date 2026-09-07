---
title: openai/skills — ⭐25,754짜리 벤더 스킬 카탈로그가 폐기됐다 (3층 재편의 첫 실측)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, openai, codex, deprecated, plugins, 3층-규격]
created: 2026-09-07
updated: 2026-09-07
sources: []
reliability: high
---

# openai/skills — Codex 스킬 카탈로그 (**deprecated**)

**GitHub**: https://github.com/openai/skills
**스타수**: **25,754** (2026-09-07 API 실측 · raw 표기 25,751 대비 **+3**)
**포크 1,734 · 이슈 292 · 워치 147 · 생성 2025-11-25 · 최종 push 2026-07-14 · 주 언어 Python**
**라이선스**: ⚠️ **없음(API `license: null`)** · `archived: false` — **아카이브되지 않은 채 deprecated**

> [!warning] README 최상단이 스스로 폐기를 선언한다 (원문 대조 완료)
> ```
> > [!IMPORTANT]
> > This repository is deprecated. For current Codex skill and plugin examples,
> > use the OpenAI Plugins repository (github.com/openai/plugins). If you want to
> > add your own skills to Codex, follow the Build plugins guide, which includes
> > instructions for creating a skill-only plugin.
> ```
> raw의 *"deprecated 명시"* 기재는 **정확**하다. 2026-09-07 raw README 원문으로 재확인했다.

> [!insight] 핵심 인사이트 — **"스킬 레포"라는 배포 단위가 벤더 층에서 폐기됐다**
> 볼트는 [[에이전트-스킬]] **3층(규격·배포)** 에서 *"벤더가 계약을 정의한다"* 고 정리했고, [[claude-plugins-official]]·[[cursor-plugins]] 를 그 사례로 뒀다. 이번 건은 그 층에서 **처음 관측된 폐기(retirement)** 다.
> 이동 방향이 명확하다 — **스킬 카탈로그 레포 → 플러그인 레포**. OpenAI의 안내는 *"스킬을 추가하려면 **skill-only plugin** 을 만들라"* 이다. 즉 **스킬이 사라진 게 아니라 플러그인 안으로 들어갔다.**
> **플러그인이 상위 배포 단위가 되고 스킬은 그 내용물이 된다.** [[claude-plugins-official]] 이 마켓플레이스를 연 것과 **같은 방향의 두 번째 벤더 사례**이며, 이로써 3층의 수렴 방향이 2개 벤더에서 일치한다.

> [!insight] 볼트의 "스타 수 ≠ 영향력" 규칙이 가장 선명하게 성립한 사례
> ⭐**25,754** 는 볼트가 추적하는 스킬 레포 상위권이다. 그런데 **신규 채택 대상이 아니다.**
> - 최종 push **2026-07-14** → **약 2개월 정체**(09-07 기준)
> - 그럼에도 스타는 raw 수집(09-07 09:00 KST) 대비 **+3** 계속 증가
> → **스타는 폐기 이후에도 붙는다.** 볼트가 [[anthropics-skills]] 에서 세운 *"스타는 사용자 기반의 크기를 잰다"* 를 넘어, **"스타는 과거의 크기를 잰다"** 로 강화해야 한다. 볼트는 이미 3층에서 *"스타 수는 영향력의 대리 변수가 아니다"* 라고 적었는데, 이번 건이 그 문장의 **가장 강한 실증**이다.

> [!warning] `archived: false` — 폐기 신호가 기계 판독 가능한 곳에 없다
> API의 `archived` 는 **false** 다. **README 본문을 읽어야만 폐기를 안다.**
> → 볼트의 자동수집기는 **GitHub 지표(스타·포크·push)만으로는 이 레포를 걸러낼 수 없다.** 실제로 09-07 배치가 이걸 *"스타 25,751 신규 소스"* 로 올렸다. **수집기 개선 항목**이며, [[actionable]] 에 반영한다.
> 판별 가능한 대리 신호는 **push 정체(2개월)** 뿐이다.

## 폐기 전 구조 (README 실측 · 기록 목적)

- **`skills/.system`** — Codex 최신 버전에 **자동 설치**되는 시스템 스킬
- **`skills/.curated`** — 큐레이션 스킬. `$skill-installer <이름>` 으로 설치
- **`skills/.experimental`** — 실험 스킬. 폴더 지정 또는 GitHub 디렉터리 URL로 설치
- 설치 후 **Codex 재시작 필요**

> [!note] 폐기됐어도 이 레포가 남긴 관측 하나
> README가 [[agentskills]](`agentskills.io`)를 **"Agent Skills open standard"** 로 명시 링크한다. [[anthropics-skills]] 가 *"표준은 밖에 있다"* 고 선언한 것과 **동일한 참조**다. → **경쟁 벤더 둘이 같은 외부 표준을 가리킨다**는 09-04 관측이 재확인됐고, **벤더 레포가 폐기돼도 표준 참조는 유지된다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ (사실 확인 기준) — 벤더 공식, README 원문 대조 완료. **단 소스로서의 유효기간은 종료.**
- **즉시 활용**: **NO.** 신규 채택 금지. 유일한 용도는 **마이그레이션 확인** — Codex 스킬을 쓰고 있었다면 `openai/plugins` 로 옮겨야 한다.
- **6개월 영향력**: 볼트가 추적하는 **스킬 레포 21건+ 중 몇 개가 같은 경로로 폐기될지**의 선행 지표. 벤더 레포부터 먼저 접힌다면 커뮤니티 자산 레포도 뒤따를 수 있다.
- **대체 관계**: **`openai/plugins` 로 대체됨.** 볼트에 해당 페이지가 **없다** → 추적 공백.
- **허와 실**: ⭐25.7K가 곧 현재 가치라는 해석이 **틀렸음이 입증된 사례**. 이 페이지의 존재 이유 자체가 그 반례를 남기는 것.
- **액션**: 아래.

> [!action] 당장 할 것
> 1. **`openai/plugins` 를 다음 배치 수집 대상으로 등록** — 3층의 현행 벤더 규격이 그쪽으로 옮겨갔다.
> 2. **수집기에 "폐기 탐지" 추가** — `archived` 플래그로는 부족하다. **README 상단 200자에서 `deprecated`/`no longer maintained`/`moved to` 문자열 검사** + **push 60일 초과 정체 플래그**. → `actionable.md` 반영.

> [!question] 미해결
> **`openai/plugins` 도 [[agentskills]] 표준을 따르는가.** 배포 단위가 플러그인으로 올라갔을 때 **스킬 명세가 그대로 보존되는지**가 크로스벤더 호환의 관건이다. 09-04에 [[anthropics-skills]] 에서 남긴 *"spec과 agentskills.io 버전 일치"* 질문과 **같은 뿌리**이며 여전히 미해소.

## 관련 페이지
- [[에이전트-스킬]] · [[agentskills]] · [[anthropics-skills]] · [[claude-plugins-official]] · [[cursor-plugins]] · [[OpenAI]] · [[marketingskills]] · [[humanlayer-skills]] · [[google-skills]] · [[vercel-skills]]

## 원본
- 출처: https://github.com/openai/skills
- 후속: https://github.com/openai/plugins (**미인제스트 — 추적 공백**)
- 수집: 2026-09-07 자동수집 (ai-news)
- 검증: GitHub API 실측 + README 원문 대조 (2026-09-07)
- 신뢰도: ⭐⭐⭐⭐⭐ (사실) / **소스 유효성: 폐기**
