---
title: hyperresearch — Claude Code용 16단계 딥리서치 파이프라인 + 영속 볼트
type: source
domain: ai-news
tags: [ai-news, github-trending, deep-research, claude-code, agent-skills, llm-wiki, verification, citation-audit]
created: 2026-09-12
updated: 2026-09-12
sources: []
reliability: high
---

# hyperresearch (jordan-gibbs/hyperresearch)

> [!insight] 핵심 인사이트 — **이건 리서치 도구가 아니라 이 볼트와 같은 종(種)이다**
> ⭐**2,858**(2026-09-12 API 실호출 · raw 2,855 대비 **+3**) · fork **272** · Python · **MIT** · created **2026-04-09** · pushed 2026-09-11 · 이슈 14 · topics `agents, agentskills, claude-code, deep-research, deep-research-agent`.
> GitHub **description 원문**: *"Agent-driven research knowledge base. Agents collect, search, and synthesize web research into a **persistent, searchable wiki**."*
> → 🎯 raw는 이것을 *"딥리서치 파이프라인"* 으로 요약했지만, **레포 자기소개의 주어는 파이프라인이 아니라 wiki 다.** README 14행도 같다: *"Every source it reads lands in a **persistent, searchable vault**, so each session starts smarter than the last."*
> **즉 [[LLM-Wiki]] 패턴의 세 번째 완제품 구현체다** — 계보: 프롬프트 규약([[llm-wiki-karpathy-2026]]) → 패키지([[claude-obsidian]]) → 앱([[llm_wiki]]) → **파이프라인 결합형(hyperresearch)**.

> [!warning] 🔴 **raw가 인용한 면책이 실제 면책보다 약하다** — 같은 문서 6행 아래에 더 센 문장이 있다
> raw 기록: *"README의 'DeepResearch-Bench RACE 리더보드 1위'는 본인들이 자체 측정한 수치(README에 `benchmarked internally` 명기) — 외부 검증 아님."*
> **볼트 원문 실측 — 두 문장이 따로 있다:**
> - README **14행**(굵은 헤드라인 안 괄호): *"currently leads the DeepResearch-Bench RACE leaderboard **(benchmarked internally)**"*
> - README **20행**(차트 바로 아래 `<sub>` 캡션): *"**Forward-looking projection from a stratified pilot** against the DeepResearch-Bench leaderboard snapshot... **Third party validation is pending.**"*
>
> → raw는 **14행만 읽었다.** 그런데 두 문장은 강도가 다르다:
> - *"자체 측정"* = **측정은 했고 검증자만 자신**이다
> - *"stratified pilot 에서의 forward-looking projection"* = **전체 벤치를 돌린 게 아니라 층화 표본 파일럿에서 외삽한 추정치**다
> → 🎯 **"우리가 쟀다"와 "우리가 일부만 재고 나머지를 추정했다"는 다른 주장이다.** 후자는 리더보드 순위를 주장할 근거로 훨씬 약하다.
> → 이 실패는 [[한정어-탈락]] 의 전형이다 — 원문을 정확히 인용했는데 **그 주장을 한정하는 문장이 3~6행 옆에 있었고 그걸 안 가져왔다.** [[파생표기-함정]] 과 다르다(파생물을 읽은 게 아니라 **같은 원문의 덜 정확한 절반**을 읽었다).
> **다만 raw를 과하게 깎을 일은 아니다** — raw는 면책 존재 자체는 잡았고, 이건 09-11 [[vercel-skills]] 의 *"산문 요약 vs 표 실측"* 과 같은 계열의 **문서 내부 강도 차이** 문제다.

> [!insight] 🪞 볼트가 없는 것을 **정확히 갖고 있다 — 기계 검사 가능한 검증 배터리**
> README 228행 원문, 출고 전 자동 실행:
> - **quote-integrity** — *"every quoted span must exist verbatim in a vault note"* (인용문이 볼트 노트에 **글자 그대로** 존재해야 함)
> - **retracted-citations** — 철회된 논문을 인지 없이 인용하면 **출고 차단**
> - **numeric-consistency** — 증거로 추적되지 않는 숫자는 **플래그**
> - **cite-check** — 인용별 결속 감사
> - **locus coverage**(235행) — step 4의 모든 논점에 step 5 중간 노트가 없으면 **에러**
> - **patch-only**(115·236행) — step 14~16은 툴 권한이 `[Read, Edit]` 로 **잠겨 있어 물리적으로 재생성 불가**
>
> 🎯 **볼트의 만성 결함이 정확히 이 자리다.** [[검사가능성-공사]] 가 지적한 *"외부 정답 고정 없음"*, [[llm_wiki]] 갱신이 지적한 *"그래프를 측정하지 않는다"*, [[i-have-adhd]] 가 지적한 *"쓰기만 하고 자기 산출물을 검사하지 않는다"* — **세 지적이 전부 '출고 전 자동 검사가 0개'라는 한 문장으로 합쳐진다.**
> 그리고 hyperresearch의 검사 항목은 **볼트에 그대로 이식 가능하다**. 볼트도 인용문을 쓰고, 숫자를 쓰고, 소스를 링크한다. 재료가 같다.

> [!action] 🔴 최우선 — **quote-integrity 1개만** 이식한다
> [[AgentGrad]] 원칙(한 번에 하나, 효과 측정)에 따라 **6개 중 1개만** 고른다. 고른 것은 **quote-integrity**다. 이유:
> - 볼트가 매 배치 *"원문 대조"* 를 주장하는데 **그 주장 자체가 검사된 적이 없다**
> - 구현이 가장 싸다 — 소스 페이지의 인용 문자열이 실제 원문에 있는지 `grep` 한 번
> - **오늘 배치가 즉시 반례를 만들었다**: raw의 hyperresearch 인용은 원문에 **존재하지만 불완전**했다. 존재 검사만으로는 못 잡고, **"인용 주변 N행에 한정어가 있는가"** 까지 봐야 한다 → 검사 규격을 이 사례로 정한다
>
> 판정 기준(다음 배치에서 확인): **소스 페이지에 쓴 직접 인용 중 원문 미검증 건이 0인가.**

> [!note] 파이프라인 실측 사양 (README 원문)
> - **16단계**, 티어별 라우팅: `light`(5단계: 1→2→10→15→16, ~30~40분) · `full`(기본, 16단계 전체 + cite-check, `full` 기어에서 ~1.5~2.5시간) · `dissertation`(옵트인 전용, **25K~80K 단어 · 300~450 소스**)
> - **250+ 소스/회** — raw 표현 정확. 원문 24행: `premier` 프로파일이 폭 스윕만으로 100~130 목표, 인용 추적·갭필이 그 두 배 이상
> - **독립성 감사**(26행): *"five reprints of one press release argue with the weight of one source"* — raw가 짚은 재판 클러스터링, **원문 일치**
> - **크래시 복구**(31행): 매 실행이 매니페스트를 남겨 `run resume` 가 죽은 단계에서 정확히 재개
> - **예산 상한**: `run init --budget 50` 초과 시 조용히 부풀지 않고 **실행을 차단**
> - **소스 백엔드**: OpenAlex(~250M works) · Crossref(~160M) 등, STEM 밖에서 강한 기본값
> - **버전 함정 명시**(340행): Unpaywall이 accepted/submitted 원고를 반환할 수 있어 `oa_version` 기록 + 본문 배너 경고 → **도구가 스스로 [[단위-불일치]] 를 방어한다**
> - 로컬 웹 UI(197행): stdlib HTTP 서버, 포트 8080, 노트 브라우징·태그 페이지·검색·**인터랙티브 링크 그래프**, 빌드 스텝·JS 의존성 없음
> - `hyperresearch link --note <id> --dry-run`(175행) — **wikilink 를 기계가 제안**한다

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 스타·라이선스·생성일 API 실호출, README 32,398B **원문 직접 대조**(인용 6개소 행번호 기록). 성능 순위 주장만 자체 파일럿 추정치로 **분리 격하**. 구조·기능 서술은 실행 가능한 CLI 명세라 검증 용이 → **high**(성능 주장 제외).
- **즉시 활용**: **YES, 단 도구가 아니라 규격으로.** 이 볼트는 이미 Obsidian 마크다운 + Claude Code라 앱을 갈아탈 이유가 없다([[llm_wiki]] 때와 같은 판단). 가져올 것은 **검증 배터리 6종의 명세**이고, 그중 **quote-integrity 1개만** 먼저.
- **6개월 영향력**: 딥리서치 경쟁의 축이 *"소스를 얼마나 많이 모으나"* 에서 **"모은 것이 실제로 주장을 뒷받침하는가를 기계가 검사하나"** 로 이동한다. 같은 배치 [[SWE-Bench-Pro-Verified]](벤치 자체의 신뢰성 교정)와 **동형**이다 — 두 소스가 같은 날 같은 말을 한다: **산출물의 존재는 산출물의 정당성이 아니다.**
- **대체 관계**: [[claude-obsidian]]·[[llm_wiki]] 와 같은 층. 차이는 **저 둘은 인제스트를 자동화했고, 이건 인제스트에 감사(audit)를 붙였다.**
- **허와 실**: 걷어낼 것은 **리더보드 1위 주장 하나뿐**이다(위 경고 참조). 나머지 — 티어/기어 라우팅, 툴 권한 잠금, 매니페스트 재개, 예산 차단 — 는 **전부 확인 가능한 구현 명세**이고 마케팅 형용사가 거의 없다. 이 비율(주장 1 : 명세 다수)이 이 레포의 실질이다.
- **액션**: ① quote-integrity 이식(위 action) ② `--dry-run` wikilink 제안 방식이 [[LLM-Wiki]] 갱신에서 미해결로 남긴 *"신규 페이지 vs 기존 갱신 판정 자동화"* 에 답을 주는지 소스 확인.

## 관련 페이지
- [[LLM-Wiki]]
- [[llm_wiki]]
- [[claude-obsidian]]
- [[WeKnora]]
- [[검사가능성-공사]]
- [[한정어-탈락]]
- [[파생표기-함정]]
- [[AgentGrad]]
- [[i-have-adhd]]
- [[SWE-Bench-Pro-Verified]]
- [[에이전트-스킬]]
- [[ai-news]]

## 원본
- 출처: https://github.com/jordan-gibbs/hyperresearch
- GitHub API 실호출(2026-09-12): ⭐**2,858** · fork **272** · Python · **MIT** · created 2026-04-09 · pushed 2026-09-11 · open_issues 14
- README 원문 실측: **32,398B**, 인용 행번호 14 · 20 · 24 · 26 · 31 · 32 · 115 · 175 · 197 · 228 · 235 · 236 · 303 · 340
- raw 대비: 스타 **+3 드리프트** / 🔴 **면책 인용 대상 오선택**(14행 인용, 20행 미인용)
- 신뢰도: ⭐⭐⭐ (구조·기능 high · 성능 순위 주장은 자체 파일럿 외삽으로 격하)
