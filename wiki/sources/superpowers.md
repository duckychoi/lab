---
title: obra/superpowers — 에이전트 스킬·소프트웨어 개발 방법론 프레임워크
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-framework, skills, open-source, software-methodology, claude-code, 오픈코어, 런타임-이식]
created: 2026-04-11
updated: 2026-10-31
sources: []
reliability: high
---

# obra/superpowers

## 🔄 2026-10-28 갱신 (인제스트 2026-10-28) — ★306,797 · **v7 두 번의 릴리스 · 릴리스 노트가 스스로 밝힌 실패율 24/24 · 기본값 ON 텔레메트리**

**GitHub API 실측(2026-10-28T09:10Z)**: ★**306,797**(수집기 306,792 · **+5**) · fork **27,309**(10-03 26,330 → +979) · open issues **365**(298 → +67) · **MIT** ✅ · created 2025-10-09 · pushed **2026-10-23T03:48:57Z** ✅(수집기 일치)
- 볼트 기준선 ★294,627(10-03) → **+12,170 / 25일 ≈ 487/일**. 10-03 구간(≈405/일)보다 **빨라졌다**. 수집기 당일 +617도 25일 평균보다 높다.
- 🔴 **수집기 해석 정정**: *"마지막 push가 10-23이라 당일증분이 낮다(위치는 크고 속도는 느림)"* 는 근거가 없다. ① 레포 자신의 최근 평균보다 오늘이 빠르다 ② push 날짜와 별 증분의 인과는 볼트 기록에서 이미 두 번 깨졌다(09-26 "정체" 판정 만료). "속도가 느리다"는 ★30만 대비 비율일 뿐이다. 📌 main 최신 커밋은 10-21 v7.0.1이다. 10-23 push는 다른 브랜치(`dev`, Contributing 절이 dev 브랜치 작업을 지시)로 보인다(미확인).

**🆕 10-03 이후 새로 생긴 것 (릴리스 API 원문)**
- **v7.0.0 (10-10)**: brainstorming을 처음부터 다시 만들었다. 작업 크기를 먼저 판정해 *"quick, clear task right away / small change agreed in chat / design document for a project"* 로 나눈다. 스펙 문서 리뷰어를 **"builder check"**(새 서브에이전트가 구현자 입장에서 남은 질문을 뽑는 방식)로 교체했다. Antigravity Marketplace 매니페스트를 추가했다. 동기 사례: *"a session designed an iOS app, never asked about platform, and built a web app."*
- **v7.0.1 (10-21)**: 🔴 **부정적 결과를 릴리스 노트가 직접 적었다.** *"Many of you told us, rightly, that the new default questions **got annoying fast and felt formulaic**."* 그리고 *"in one of our test scenarios, it **skipped the doc without asking in 24 of 24 runs** before this change and **3 of 24 after**."* ⇒ v7.0.0 brainstorming은 한 시나리오에서 설계 문서 단계를 **100% 건너뛰었다.** 수정 후에도 12.5%가 남는다. 세 개의 긴 스킬을 *"better survive compaction on Claude Code"* 하도록 줄였다.
- README에 **`diagnosing-superpowers`** 스킬(세션 트랜스크립트를 읽고 줄 단위 근거로 무엇이 잘못됐는지 보고·익명화 번들 생성)과 **`executing-plans`**(서브에이전트 없이 인라인 실행 + 마지막 1회 리뷰, *"cheapest"*)가 명시됐다. ⇒ 서브에이전트 주도 개발이 **유일 경로가 아니게 됐다.**
- 평가 하네스: *"Skill-behavior tests use the drill eval harness from `prime-radiant-inc/superpowers-evals`"*(★139, 볼트 확인). ⚖️ 07-26 이래 미해소였던 *"that works" 정량 근거 미제시*에 대해 **평가 도구의 존재는 확인됐다.** 결과 수치 공개는 위 24/24·3/24 한 건뿐이다.

> [!warning] 🔴 수집기 요약이 빠뜨린 것
> 1. **텔레메트리가 기본값 ON이다.** README `## Visual companion telemetry`: brainstorming 비주얼 컴패니언의 Prime Radiant 로고가 *"loaded from our website. It includes the version of Superpowers in use."* 프로젝트·프롬프트 내용은 보내지 않는다고 적혀 있다. 끄기: `SUPERPOWERS_DISABLE_TELEMETRY` 또는 Claude Code의 `DISABLE_TELEMETRY` / `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`.
> 2. **v7.0.1의 24/24 실패 수치**(위). 수집기의 "검증된 워크플로 템플릿이라 실용성이 높다"는 평가와 정면으로 긴장하는 1차 자료인데 요약에서 빠졌다 → [[인용-부호]] 계열 "부정적 결론 누락" 사례.
> 3. 기여 정책: *"we don't generally accept contributions of new skills"* · *"We also don't accept agent-written PRs that fix issues filed by someone else unless a maintainer asked"* · PR 템플릿에 *"the summary a human writes in their own words"* 필수(10-20 커밋). 에이전트 스킬 레포가 **에이전트가 쓴 PR을 막는** 정책이다.
> 4. 🔴 **볼트 자체 기록 정정**: 아래 「도메인별 추출」의 *"전임 커뮤니티 엔지니어까지 채용 중"* 은 **만료**됐다. 07-27 커밋 *"docs: remove the "We're Hiring" section from the README"*. 3개월 동안 볼트가 낡은 주장을 유지했다.
> 5. ✅ 볼트 미해결 해소: README `## Community`에 *"Superpowers is built by Jesse Vincent and the rest of the folks at **Prime Radiant**"*. obra와 [[Prime-Radiant]]의 관계가 README 원문으로 확인됐다(GitHub org `prime-radiant-inc` 2026-01-07 생성·공개 레포 57개).

- ✅ 런타임 목록은 10-03과 같은 **16종**(수집기 "16종 이상" 일치). Muse 설치 절이 가장 길다.
- 🔵 [[openbot]](같은 배치)이 Claude Code·Codex·OpenCode 등 7개 CLI를 묶는 관리 계층이라면, superpowers는 각 CLI **안에서** 프로세스를 강제하는 층이다. 둘은 겹치지 않는다.

**관련 추가**: [[Prime-Radiant]] · [[openbot]] · [[인용-부호]] · [[에이전트-스킬]]

> [!update] 2026-10-03 갱신 — ★294,627 (볼트 실측) · 🎯 **"명시"와 "유지"의 차이가 같은 배치에서 드러났다**
> **볼트 독립 실측 ★294,627** ↔ 수집기 ★294,623 = **드리프트 +4**. 볼트 베이스라인 ★291,794(2026-09-26 실측) → **+2,833 / 7일 = 일평균 ≈405**.
> ✅ **전 필드 일치**: fork **26,330** · open_issues **298** · **MIT** · topics **8** · created 2025-10-09 · pushed 2026-09-27T02:37:47Z · 주언어 **Shell**.
> ✅ **09-26 "−1 음수 드리프트" 이상은 재발하지 않았다** — 이번 7일 구간은 단조 증가다. ⚖️ 그때의 −1 은 **일회성 관측 잡음**으로 판정한다(원인은 여전히 미확인이므로 "해소"가 아니라 "재발 없음"으로만 적는다).
> 🔴 **일평균 ≈405가 [[reverse-skill]] 의 405와 같은 자릿수인 것은 우연이다. 무관한 두 레포이며 해석을 금지한다**(수집기 경고 수용).
> 🏆 **오늘 배치가 이 레포의 자기 규정을 시험했다** — superpowers 는 **15종 이상 에이전트 설치 경로를 개별 명시**하는 것으로 [[하네스-설계-축]] 의 이식성 극단 사례였다. 그런데 같은 배치의 [[ponytail]] 커밋 로그를 볼트가 열어 보니 **9개 플러그인 매니페스트**(`.claude-plugin`·`.codex-plugin`·`.devin-plugin`·`.github/plugin`·`.qoder-plugin`·`gemini-extension.json`·`package.json`·`plugin.yaml`·`ponytail-mcp/package.json`)를 **릴리스 1건에서 동시 버전업**했다.
> ⚖️ **그래서 이식성은 두 층으로 분해된다**: ① **문서가 설치 경로를 열거하는 것**(superpowers 15종) ② **매니페스트를 실제로 유지보수하는 것**(ponytail 9종, 커밋으로 증명). **둘은 같은 지표가 아니다.** 📌 superpowers 쪽은 ②의 증거를 볼트가 아직 확인하지 않았다 → **README 열거 수 ≠ 유지되는 매니페스트 수** → [[암묵을-명시로]].
> 🔴 **미해결 유지(2배치 연속)**: `## Commercial Services` 섹션 **내용 미열람**. MIT 레포에 상용 서비스 유입 경로가 있다는 사실만 확인됐고 조건·범위를 모른다.

> [!update] 2026-09-26 갱신 — ★**291,794** · 🔴 **08-23 판정 2건이 만료됐다** · 🆕 **16개 런타임 이식 + 상업 지원 발견**
> ★**291,794**(2026-09-26 GitHub API 실검증) ← 276,399(08-23). **34일간 +15,395 · 일평균 약 453**(당일 +468과 정합).
> 🔴 **만료 1 — "나흘째 정체"가 사라졌다.** 08-23에 *"최종 푸시 2026-08-19 — 나흘째 정체"* 로 적었으나 오늘 **`pushed_at` = 2026-09-25T18:08:16Z(어제)** 다.
> 🔴 **만료 2 — 그래서 "커밋 없이 스타만 늘고 있어 트렌딩 노출의 자기강화 루프"라는 해석의 전제가 무너졌다.** 🎯 09-24 [[TradingAgents]](*"5주 정체"* → 당일 푸시)에 이은 **시점의존 주장 만료 2번째**이고, 같은 배치 [[mattpocock-skills]] 까지 합치면 **3번째**다. 📌 **볼트가 "정체"라고 적은 것들이 예외 없이 되살아났다 — 정체 판정에는 관측 창을 함께 적어야 한다.**
> 🆕 **볼트 신규 발견 1 — 16개 런타임에 이식된다.** README 399행의 `###` 헤딩 17개 중 16개가 설치 대상 런타임이다: Claude Code · Antigravity · Codex App · Codex CLI · Cursor · Devin CLI · Factory Droid · Gemini CLI · GitHub Copilot CLI · Grok Build CLI · Kimi Code · OpenCode · Pi · Qwen Code · **Hermes Agent** · Muse (+ Skills Library).
> 🎯 **`Hermes Agent` 가 공식 설치 대상에 들어 있다** — 사용자 [[hermes-agent]] 축에 **직접 적용 가능한 경로**이고, 볼트가 07-03 이래 *"멀티 하니스 지원"* 이라고만 적어 온 것의 **실제 목록을 오늘 처음 확정**했다. 같은 배치 [[hindsight]](MCP 경로)와 함께 **두 건이 같은 날 Hermes 를 가리킨다.**
> 🆕 **볼트 신규 발견 2 — 상업 지원 창구가 있다.** README 48행 `## Commercial Services`: *"If you're using Superpowers in enterprise … drop us a line at **sales@primeradiant.com**."* → **MIT 오픈소스 + 기업 유료 지원** 구조이고, 볼트 [[mem0ai]](오픈코어 3경로)에 이은 **두 번째 상용 퍼널**이다. [[Prime-Radiant]] 엔티티 신설.
> 부가 실측: 포크 **26,114**(24,726→+1,388) · 오픈이슈 **404** · watchers **1,082** · MIT · Shell · topics **8개**(`ai,brainstorming,coding,obra,sdlc,skills,subagent-driven-development,superpowers` — 08-23에는 미기록).
> 🔴 **드리프트가 음수다**: 수집기 ★291,795 → 볼트 **291,794(−1)**. 09-17 [[cline]] 이후 볼트 **2번째 음수 드리프트**이고, 같은 배치 [[claude-plugins-official]] 도 −1이라 **한 배치에 2건**이다 → [[상대속도-가림]] 보강.
> ⚠️ *"that works"* 정량 근거 미제시는 **여전히 미해소**(07-26 최초 지적 이후 2개월). reliability high 유지(수치 신뢰도).

> [!update] 2026-08-23 갱신 — ⭐276,399 (**API 실검증**·이틀 +587·성장률 역전 고착)
> GitHub ⭐**276,399** (2026-08-23 **GitHub API 실호출 검증**) ← 275,812(08-22). 이틀 **+587**로 **절대 스타 1위는 유지하나 증분은 하루 300선**까지 내려앉았다. 같은 기간 [[mattpocock-skills]]는 +2,473 — **성장률 역전이 08-22 관측에 이어 이틀째 고착**되며 격차가 약 4.2배로 벌어졌다.
> 부가 실측(API): 포크 **24,726**·이슈 **308**·**MIT**·Shell·생성 2025-10-09·최종 푸시 **2026-08-19**(**나흘째 정체**). mattpocock(푸시 08-21 정체)과 달리 이쪽은 정체가 더 길다 — 두 레포 모두 **커밋 없이 스타만 늘고 있어**, 현재 스킬 생태계 상위 스타 유입은 콘텐츠 갱신이 아닌 **트렌딩 노출의 자기강화 루프**로 해석하는 편이 사실에 가깝다.
> 해석 유의: 방법론 레포는 자산 레포보다 **한 번 정착하면 추가 유입이 느린 것이 정상**일 수 있다(방법론은 채택 후 반복 소비되지 않음). 따라서 증분 둔화를 곧 쇠퇴로 읽지 않는다. ⚠️"that works" 정량 근거 미제시 상태는 변함없음. reliability high 유지.

> [!update] 2026-08-22 갱신 — ⭐275,812 (**API 실검증**·27.5만 돌파·약 2주 만 +6,865)
> GitHub ⭐**275,812** (2026-08-22 **GitHub API 실호출 검증**) ← 268,947(08-08). 약 2주 만 **+6,865**로 **27.5만 돌파**, 이번 배치 **최대 절대 스타수**이자 에이전트 스킬 카테고리 1위 유지. 트렌딩 데일리 **6위**(raw 표기 당일 +790·raw 절대값 275,811과 API 275,812 일치 수준). 부가 실측: 포크 **24,660**·이슈 **300**·**MIT**·생성 2025-10-09·최종 푸시 2026-08-19. 원문 설명 *"An agentic skills framework & software development methodology that works."*
> 이날 신설한 [[에이전트-스킬]] 개념 페이지에서 본 리포는 **2층(방법론)** 대표. 같은 배치 [[Repo0]](Dual-DAG로 요구사항↔컴포넌트 구조를 자료구조화 후 TDD 생성)가 **동일 신념의 알고리즘판**으로 짝을 이룸 — superpowers가 *프롬프트 규율*로 "코드부터 짜지 마라"를 강제한다면 Repo0는 같은 규율을 **모듈성 지표로 수렴 판정하는 기계 절차**로 옮긴다.
> ⚠️설명문의 **"that works"에 대한 정량 근거는 리포에 미제시**(재현성·성공률 벤치 없음). 이 공백은 [[에이전트-스킬]] 개념 페이지에 구조적 약점으로 기록. reliability high 유지.

> [!update] 2026-08-08 갱신 — ⭐268,947 (당일 +782)
> ⭐**268,947** (2026-08-08 자동수집, 당일 **+782**) ← ⭐268,380 (08-07). 에이전트 스킬 카테고리 압도적 1위·27만 근접 유지, 하루 +수백대 안정 유입. 같은 08-08 배치의 [[mattpocock-skills]](⭐209,271)와 스킬 상단 2강 그대로. Anthropic 공식 마켓플레이스 등재·방법론 수준 인정 유지 → reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-08-07 갱신 — DL 26.8만 (당일 +858)
> ⭐**268,380** (2026-08-07 자동수집, 당일 **+858**) ← ⭐261,293 (07-26). 2주 새 +7,087로 에이전트 스킬 카테고리 압도적 1위 유지. 같은 08-07 배치의 [[mattpocock-skills]](⭐207,870·20만 돌파)와 함께 스킬 상단 2강. Anthropic 공식 마켓플레이스 등재·방법론 수준 인정 유지 → reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!update] 2026-07-26 갱신 — 26만 돌파 (WebFetch 실검증)
> ⭐**261,293** (2026-07-26 WebFetch 실검증) ← ⭐252,676 (07-12). 2주 새 +8,617로 에이전트 스킬 카테고리 압도적 1위·26만 돌파 유지. 같은 배치에서 스킬 발견 레이어([[awesome-claude-skills]])와 벤더 호환 레이어([[open-code-review]]·[[claude-cookbooks]])가 함께 성장 — 스킬=배포 단위 트렌드 지속. reliability high 유지.

> [!insight] 핵심 인사이트
> 코딩 에이전트를 위한 **완결된 소프트웨어 개발 방법론** — 조합 가능한 스킬(composable skills) 세트와 이를 자동으로 발동시키는 초기 지침으로 구성된다. ⭐261,293 (2026-07-26 실검증) ← ⭐252,676 (07-12) ← ⭐244,962 (07-03)로 에이전트 스킬 카테고리 압도적 1위, 급상승 최상위 유지. Claude Code·Cursor·Copilot·Kimi Code 등 멀티 하니스 지원 명시. 핵심은 "에이전트가 코드부터 짜지 않는다" — 먼저 스펙을 캐묻고(spec), 읽을 만한 크기로 쪼개 승인받고, 주니어도 따를 수준의 구현 계획을 세운 뒤, **서브에이전트 주도 개발(subagent-driven development)**로 태스크별 검수·리뷰하며 진행한다. 진짜 red/green TDD·YAGNI·DRY를 강제. 스킬이 자동 트리거되므로 사용자가 특별히 조작할 필요가 없다. 같은 배치의 [[agency-agents]](역할 페르소나 카탈로그)가 "누가 일하나"를 정의한다면, superpowers는 "어떻게 일하나"(프로세스·스킬 체계)를 정의한다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐244,962, 단순 AI 도구가 아닌 개발 방법론 수준의 커뮤니티 인정. Anthropic 공식 플러그인 마켓플레이스(`/plugin install superpowers@claude-plugins-official`)에 등재, obra(Jesse Vincent) 주도로 전임 커뮤니티 엔지니어까지 채용 중 — 지속성 높음.
- **즉시 활용**: YES — Claude Code·Codex·Cursor·OpenCode·Copilot 등 다수 하니스에 플러그인으로 설치. 설치 즉시 스킬 자동 발동.
- **6개월 영향력**: 높음 — 에이전트 스킬·워크플로우 설계의 표준 참조. "스펙 → 계획 → 서브에이전트 실행 → 리뷰" 루프가 [[Claude-Code-워크플로우]]의 사실상 레퍼런스가 될 가능성.
- **대체 관계**: [[hermes-agent]]·LangChain 같은 프레임워크 대비 "코딩 에이전트 개발 프로세스"에 특화. [[agency-agents]]와는 경쟁이 아니라 상보(방법론 vs 역할 카탈로그) — 함께 쓰기 좋음.
- **허와 실**: "완결된 방법론"은 강력하지만 그만큼 **에이전트를 특정 프로세스에 강하게 구속**한다. 빠른 단발 태스크엔 오버헤드일 수 있고, 자동 트리거가 의도치 않게 개입할 여지. TDD·리뷰 강제가 맞지 않는 워크플로우도 존재.
- **액션**: 공식 마켓플레이스에서 설치 → 서브에이전트 주도 개발 루프를 내 실제 태스크에 1회 돌려보고 [[agency-agents]] 역할 프리셋과 조합 가능성 검증.

> [!question] 미해결 질문
> Monday 스킬 시스템([[Claude-Code-워크플로우]])과 자동 트리거가 충돌하지 않는가? 스킬 발동 조건을 세밀히 통제할 수 있는지 확인 필요.

> [!action] 당장 할 것
> `/plugin install superpowers@claude-plugins-official`로 설치 → 스킬 정의·조합 구조 분석 → [[agency-agents]] 역할 프리셋과 [[caveman]] 출력 압축을 얹은 조합 워크플로우 실험.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]
- [[agency-agents]]
- [[strix]]
- [[video-use]]
- [[caveman]]
- [[hermes-agent]]
- [[multica]]

## 원본
- 출처: https://github.com/obra/superpowers
- 실측(2026-09-26 GitHub API): ★**291,794** · 포크 26,114 · 오픈이슈 404 · watchers 1,082 · MIT · Shell · 생성 2025-10-09 · 푸시 **2026-09-25T18:08:16Z** · topics 8개 · repo id 1073224795
- 확인 범위: **README 399행 전문 열람**(16런타임·Commercial Services 확인). 🔴 스킬 코드 미독 · 🔴 미실행
- 스타: ⭐291,794 (2026-09-26 API) ← ⭐276,399 (08-23) ← ⭐275,812 (2026-08-22 **GitHub API 실호출 검증**·트렌딩 데일리 6위·27.5만 돌파·raw 표기 275,811/당일 +790) ← ⭐268,947 (08-08, +782) ← ⭐268,380 (08-07) ← ⭐261,293 (07-26 WebFetch 실검증) ← ⭐252,676 (07-12) ← ⭐244,962 (07-03) ← ⭐225,402 (06-13) ← ⭐224,143 (06-11) ← ⭐193,260 (05-16) ← ⭐174,963 (04-30)
- 부가 실측(2026-08-22 API): 포크 24,660 · 이슈 300 · 언어 Shell · 라이선스 MIT · 생성 2025-10-09 · 최종 푸시 2026-08-19
- 신뢰도: ⭐⭐⭐⭐⭐ (27.5만 스타·Anthropic 공식 마켓플레이스 등재·수치 API 실검증 — 단 "that works" 정량 근거는 리포 미제시)

## 🔄 2026-10-29 갱신 (인제스트 2026-10-29) — **★+991/일 · 6일째 푸시 없음 · 지원 하네스 16종 실측**

**GitHub API 실측(2026-10-29T09:06Z)**: ★ **307,788**(수집기 307,783 · **+5**) · MIT ✅ · pushed **2026-10-23T03:48:57Z**(10-28 과 동일 · 6일 무푸시) · 최신 릴리스 **v7.0.1**(10-21) — 10-28 기록 이후 신규 릴리스 없음
- 📈 10-28 ★306,797 → **+991/일**(수집기 당일 +1,095 · 트렌딩 창 차이).
- ✅ README(14,847 B)에서 하네스 이름 **16종** 확인(볼트 사전 기준 grep — 실제 목록과 1:1 대조는 아님) ⇒ 수집기 "15개 이상" 일치. Claude Code 공식 마켓플레이스 등재 서술 일치.
- ⚖️ 수집기 요약은 10-28 볼트가 기록한 **릴리스 노트 자백 실패율(24/24 → 3/24)과 기본값 ON 텔레메트리**를 다시 언급하지 않았다 — "검증된 대형 레포"라는 평가만 남았다 → [[한정어-탈락]] (경미: 매일 반복할 의무는 없지만 "검증됨"의 근거로 쓰기엔 부족).

## 🔄 2026-10-31 갱신 (인제스트 2026-10-31) — ★309,635 · **`pushed_at` 은 움직였는데 기본 브랜치 커밋은 그대로**

**GitHub API 실측(10-31)**: ★**309,635**(수집기 309,631 · +4) · fork 27,550 · MIT ✅ · 최신 릴리스 v7.0.1(10-21) · README 14,847 B(무변경)
- 📈 10-29 ★307,788 → **약 924/일**(10-29 일 증분 991 과 비슷).
- ⚖️ `pushed_at` 이 10-23 → **10-29T23:35Z** 로 바뀌었지만, 커밋 API 기본 응답의 최신은 여전히 **10-21T21:00Z**(v7.0.1). 기본 브랜치 외 push로 보이나 확인은 못 했다(추정). ⇒ `pushed_at` 만으로 "개발 재개"를 판단하면 안 된다.
- 🔴 수집기 "작은 수정에는 절차가 무거울 수 있음(수집자 판단, 정량 근거 없음)" — 추정 표기는 ✅ 정직하다. 다만 **볼트 10-28 기록상 v7.0.0 이 작업 크기를 먼저 판정해 작은 작업은 바로 처리**하도록 바뀌었으므로, 해당 우려는 v7 이후 약해졌다. 반대로 v7.0.1 릴리스 노트의 "문서 건너뜀 24/24 → 3/24"는 3회째 요약에서 빠졌다 → [[한정어-탈락]].
