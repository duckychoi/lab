---
title: android/skills — 안드로이드 공식 에이전트 스킬 (선정 근거를 적고 근거의 근거는 안 적었다)
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, android, google, skill-md, 벤더공식, 선정근거]
created: 2026-10-17
updated: 2026-10-17
sources: []
reliability: high
---

# android/skills

**GitHub**: https://github.com/android/skills
**스타**: ⭐8,191 (2026-10-17T09:12Z / 18:12 KST 실측 · 수집기 8,188 대비 +3)
**증분**: **+36 today = 금일 수집분 최저 증분**
**제원**: fork 540 · Kotlin · Apache-2.0 · open_issues 37 · created 2026-03-16 · pushed 2026-10-16T10:07Z
**신뢰도**: ⭐⭐⭐

> [!insight] 핵심 인사이트 — **스킬 선정 기준을 명문화한 첫 벤더 공식 레포**
> README 원문(검증 완료, 2,994 B 전문 열람):
> *"Our Android skill development focuses on **use cases and workflows where evaluations show LLMs underperform**. We aren't prioritizing well-established areas where LLMs are already proficient, such as basic Jetpack Compose best practices."*
> ⇒ 🏆 **"무엇을 스킬로 만들 것인가"에 답을 적었다** — 커버리지가 아니라 **모델 약점**이 선정 축이다. 기본 Compose 처럼 모델이 이미 잘하는 영역은 **의도적으로 뺐다**고 명시한다.
> ⇒ 📌 이것은 스킬 설계 일반론으로 이전 가능하다: **스킬의 가치는 문서의 품질이 아니라 모델 성능의 결손 위치에서 나온다.**

> [!warning] 🔴 그러나 근거의 근거가 없다 — *"evaluations show"* 의 그 evaluation 이 공시되지 않았다
> README 는 선정 기준으로 **평가 결과**를 지목하는데, **평가 하네스·점수·대상 모델·링크가 전부 없다.**
> ⇒ ⚖️ **"기준을 적었다"와 "기준의 근거를 적었다"는 다르다.** 전자는 이 레포가 금일 수집분 중 유일하게 했고, 후자는 하지 않았다.
> ⇒ 🔴 규약 ⑨ 적용(`GET /contents/`): 루트에 `BENCHMARK.md`·`EVAL.md`·`RESULTS.md` **없음**. 24개 디렉터리는 전부 스킬 도메인(`camera/`·`performance/`·`testing/`·`security/`·`wear/`·`xr/`·`device-ai/` 등)이고 **평가 산출물 디렉터리가 아니다** ⇒ **"열어서 없음"이지 "열지 않아 모름"이 아니다.**

> [!note] 배경 — 증분 +36 의 의미
> 트렌딩 7위로 선발됐으나 당일 증분 **+36** 은 금일 수집분 최저이고 1위 `xerj`(+1,648)의 **1/46** 이다.
> ⇒ ⚖️ **수집 기준 "스타 1000+ **또는** 당일 급상승" 중 전자만 통과**했다. **"당일 급상승"에는 해당하지 않는다**(수집기도 숨기지 않고 적었고, 볼트도 유지한다).

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — ★8,191 · **구글 공식**(`android` org) · Apache-2.0 · 24 스킬 도메인. 🔴 단 *"Public contributions are **not accepted** at this time"* — 8,191★ / 540 fork 규모에서 **외부 기여를 받지 않는 단방향 배포**다.
- **즉시 활용**: **YES** — 벤더 중립 설치 경로를 제공한다. `android skills add --all` · Claude Code `/plugin install android-skills --marketplace android/skills` · Codex `codex plugin add android-skills@android-skills`. 🔴 **기본 설치 경로는 `~/.gemini/antigravity/skills`**(에이전트 미지정 시) = **구글 자사 우선, 타사 지원**.
- **6개월 영향력**: `SKILL.md` **open-standard agent skills**(agentskills.io) 를 구글이 공식 채택했다 ⇒ **스킬 포맷이 벤더 간 공통 규격으로 굳는 신호**다. 같은 날 `anthropics/claude-plugins-official`(트렌딩 1위 · +1,552) · `cursor/plugins`(9위) 가 **동시 급상승**한 것과 묶어 읽어야 한다 → [[벤더-디렉토리-동시급상승]]
- **대체 관계**: 안드로이드 개발 시 에이전트에 수동으로 붙이던 developer.android.com 문서 복붙을 대체. 🔴 대체 대상이 **도구가 아니라 사람의 복붙 습관**이다.
- **허와 실**: 과장 문구가 **없다** — 수치 주장을 아예 하지 않는다. 🏆 **금일 수집분 중 "수치 0건"이 결함이 아닌 유일 항목**(규격·문서 레포는 수치가 가치 축이 아니다). 단 위 warning 의 평가 미공시는 실재하는 공백이다.
- **액션**: `android skills add r8-analyzer` 1건 설치해 **SKILL.md 구조만 확인**(볼트 스킬 작성 레퍼런스로 쓸 수 있는지) · 우선순위 중간.

## 관련 페이지
- [[cursor-plugins]] ← 같은 날 같은 범주 벤더 공식 디렉토리
- [[claude-plugins-official]] ← 트렌딩 1위 · 동일 범주
- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[간판-지체]] ← 반대 사례(간판에 과장이 없다)

## 원본
- 출처: https://github.com/android/skills
- 열어 본 것: `GET /repos` · `GET /contents/` · `raw/main/README.md`(2,994 B 전문)
- 관측: 2026-10-17T09:12Z (18:12 KST)
- 신뢰도: ⭐⭐⭐
