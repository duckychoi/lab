---
title: iFixAi — AI 에이전트 독립 감사(크로스벤더 심판) CLI
type: source
domain: ai-news
tags: [ai-news, agent-audit, ai-governance, eu-ai-act, iso-42001, nist-ai-rmf, owasp-llm, 요약자와-판정자-분리, 문서내-값충돌, 측정도구-먼저-반증]
created: 2026-10-15
updated: 2026-10-15
sources: []
reliability: medium
---

# ifixai-ai/iFixAi — 에이전트가 지시받은 일을 실제로 하는지 **다른 벤더 모델로** 채점한다

> [!insight] 🏆🏆 핵심 인사이트 — **"판정자를 벤더째로 분리한다"가 설계 원칙으로 박혀 있다**
> README 원문: *"running them as a **pair** still comes in under a single Sonnet run and adds **cross-vendor robustness, so no one model or vendor decides your grade** (ties break conservatively, `fail > partial > pass`)."*
> 🎯 ⇒ **심판을 2개 벤더로 두고, 동점은 보수적으로 깬다**(`fail` 우선). 📌 **볼트 [[요약자와-판정자-분리]] 를 제품이 구현한 형태다.**
> 🏆🏆 **그리고 금일 같은 배치의 [[CriticOPD]] 가 *정반대 경로로 같은 결론* 에 도달했다** — 그쪽은 증류 이론에서 *"교사가 오류를 알아보면서도 이어쓰기에서는 따라간다"* 를 측정해 **역할 분리**를 도출했고, 이쪽은 감사 도구로 **벤더 분리**를 구현했다. ⇒ 📌 **[[대립레시피-동시도착]] 의 변형: 대립이 아니라 *동일 결론* 이 이론·제품 양쪽에서 같은 날 도착했다.**

**GitHub**: https://github.com/ifixai-ai/iFixAi
**스타**: ★**27,995**(볼트 API 실측 2026-10-15 · 수집기 27,986 → **+9**) · 포크 **1,523** · watchers **410** · `open_issues` **8**
**언어/라이선스**: Python · **Apache-2.0** · created **2026-04-27** · pushed **2026-10-15T07:45:19Z** · 28,343 KB
**신뢰도**: ⭐⭐⭐ (지표·README 수치는 1차 확인 / 🔴 **README 내부 모순 2건 적발 · 코드 미실행**)

## ✅ 볼트 독립 검증 — 수집기 README 수치 4종 전건 확증

> [!note] 수집기 주장 ↔ 볼트 원문 대조 (README 27,625 B 전문 수신 · HTTP 200)
> | 수집기 주장 | README 원문 위치 | 판정 |
> |---|---|---|
> | 기본 **10개 검사** | *"`ifixai run` runs **10 inspections** unless you ask for more. They are the `essential` suite: **six high-impact** checks plus **four medium-impact**"* | ✅ **정확** |
> | 기본 실행 약 **850 콜** | *"a default run makes about **850 calls to your agent** and about **820 judge calls**"* | ✅ **정확** (🏆 **단 850 은 *에이전트* 콜이고 심판 콜은 별도 820 이다** — 수집기는 850 만 적었다) |
> | **"약 6배 적은 작업"** | *"**About 6x less work.**"* · `--full-run` 은 *"about **5,500** and **4,700**"* | ✅ **정확** (볼트 환산: 5,500/850 = **6.47배** · 4,700/820 = **5.73배**) |
> | **120초 이내** | *"iFixAi gives you this answer in **less than 120 seconds**"* | ✅ **정확** |
> | 기본 픽스처 **의도적 결함**(B01·P01 FAIL 정상) | *"Expect a **FAILING** scorecard (**B01 and P01** fail) — the bundled default fixture ships **seeded defects on purpose**"* | ✅ **정확** |
>
> 🏆 **수집기 5/5 전건 정확하다. 금일 GitHub 신규 1건의 보고 품질은 높다.**

## 🔴🔴 볼트 신규 — **README 내부 값 충돌 2건 (수집기 미적발)**

> [!warning] 🔴🔴 **충돌 1 — 같은 `--full-run` 의 심판 콜 수가 2,000 과 4,700 으로 둘 다 적혀 있다**
> **비용 각주(README 218행 부근)**: *"Rough total for one **full-suite** run at OpenRouter list prices (mid-2026), based on the **~2,000 judge calls** a full run makes"*
> **기본실행 설명(251행)**: *"`--full-run` makes about **5,500** [agent] and **4,700** [judge]"*
> 🔴 **같은 문서가 같은 대상(full-run 심판 콜)에 2,000 과 4,700 을 준다 — 2.35배 차이다.**
> 📌 **그리고 "기본은 전체의 약 1/6"(224행)과도 안 맞는다**: 2,000/6 = **333** 인데 기본 심판 콜은 **820** 이라고 적혀 있다(2.46배). ⚖️ **4,700/6 = 783 ≈ 820 이므로 *4,700 쪽이 내부 일관성이 있다* 고 추정되나, 🔴 어느 쪽이 참인지 볼트는 확정하지 않는다.**
> 🎯 ⇒ **비용 각주의 가격 추정이 2,000 콜 기준이라면, 실제 비용은 README 가 말한 값의 2.35배일 수 있다.** 📌 **이것이 이 모순의 실질 피해다 — 사용자가 과금 규모를 오판한다.**

> [!warning] 🔴 **충돌 2 — 전체 스위트 규모가 50 과 60 으로 둘 다 적혀 있다**
> **"50"**: 비용 각주 *"the suite generates far more probes than its **50-test count**"*
> **"60"**: ① *"10 inspections by default; `--full-run` for **all 60**"*(82행) ② *"Add **`--full-run`** to run **all 60**"*(229행) ③ *"`ifixai run --provider openai --full-run`  # **all 60**"*(256행)
> 🔴 **60 이 3곳, 50 이 1곳이다.** ⚖️ **다수는 60 이나 "다수결이 참"은 근거가 아니다 — 볼트는 둘 중 하나를 고르지 않는다.**
> 📌 **주목할 점: 두 모순이 *같은 각주 한 문장* 안에 함께 있다**(2,000 과 50). 🎯 ⇒ **비용 각주 1문장이 문서의 다른 부분과 체계적으로 어긋난다** — 단발 오타가 아니라 **갱신 누락으로 보이는 패턴**이다(스위트가 50→60 으로 늘고 콜 수가 2,000→4,700 으로 늘었는데 각주만 옛 값에 남은 형태). ⚖️ **이 해석은 추정이고, 커밋 이력으로 확인하지 않았다.**
> 🆕 ⇒ **[[문서내-값충돌]] 신설 — 본 건이 1호 사례다.**

> [!insight] 🏆 볼트 신규 2 — **"6배 적은 작업"은 품질 할인을 동반하고, 레포가 그걸 먼저 적는다**
> README 가 기본 10검사의 한계를 **스스로 명시한다**:
> - *"The three **mandatory minimums** are always included (**a run without them has its overall score withheld**)"* ⇒ 📌 B01·B08·P01 이 빠지면 **총점이 보류된다** — 점수 산출에 조건이 걸려 있다.
> - *"**Eight of the ten** only need your agent to answer chat messages. **B01 and P01 read its tool-authorization layer instead**; what they report **when none is exposed**: docs/scoring.md"* ⇒ 🔴 **툴 권한 계층을 노출하지 않는 에이전트에서는 필수 2개가 정상 측정되지 않는다.**
> 🎯 ⇒ **즉 "어떤 에이전트에도 돌아간다"와 "필수 최소 3종이 항상 포함된다"가 긴장 관계다.** ⚖️ **레포가 이 긴장을 숨기지 않고 문서 링크까지 달았다** → [[측정도구-먼저-반증]] 계열. 🏆 **금일 2번째 사례다**(10-14 [[context-mode]] 가 자기 열등 구간 13% 를 공개한 것과 같은 성격).

> [!insight] 🏆 볼트 신규 3 — **topics 가 이것을 개발도구가 아니라 *규제 대응 도구* 로 분류한다**
> GitHub topics(볼트 API 실측 20개): `eu-ai-act` · `iso-42001` · `nist-ai-rmf` · `owasp-llm` · `ai-governance` · `ai-alignment` · `risk-assessment` · `risk-management` · `responsible-ai` · `hallucination-detection` · `prompt-injection` · `llm-security`
> 🎯 ⇒ **EU AI Act · ISO 42001 · NIST AI RMF · OWASP LLM — 4개 규제/표준 프레임워크를 명시적으로 겨냥한다.** 📌 **볼트 ai-news 도메인에서 이런 조합은 드물다**(대부분 개발 생산성 도구다).
> 📌 **`open_issues` 8 은 금일 GitHub 5건 중 압도적 최저다**([[context-mode]] 359 의 **1/45** · [[rea]] 911 의 **1/114**). ⚖️ **해석 2가지**: ① 신생(5.5개월)이고 사용자가 적다 ② 감사 도구라 사용자층이 좁고 숙련됐다. 🔴 **포크 1,523 / 이슈 8 = 이슈·포크비 0.005 로 볼트 추적 중 최저급** — 🔴 **이슈/PR 분해 미실행**(볼트 연속 누락 항목) → [[복합지표-분해]].

## 도메인별 추출 (ai-news)

- **신뢰도**: ★**27,995**(볼트 실측 · 당일 +2,109 로 수집기 ①선발 근거) · **Apache-2.0**(제약 없음 · 금일 [[context-mode]] ELv2 와 대비) · **README 수치 5종 전건 확인** · 🔴 **그러나 문서 내부 값 충돌 2건.**
- **즉시 활용**: ⚖️ **조건부 YES — 금일 GitHub 5건 중 볼트 축에 가장 직접적이다.** 📌 **볼트 자신이 "에이전트가 지시받은 일을 하는지"를 매 배치 판정하는 주체다**(수집기 ↔ 볼트 구조). 🎯 **iFixAi 의 B16**(*"reports a failure instead of pretending it worked"*)·**B06**(*"says when it is unsure instead of guessing"*)**은 볼트 `CLAUDE.md` 의 사실확인 원칙과 1:1 대응한다.**
- **6개월 영향력**: 규제 프레임워크(EU AI Act 등) 대응이 의무화되면 **감사 도구가 선택이 아니라 요건**이 된다. ⚖️ **단 볼트 소유자는 규제 대상 사업자가 아니므로 영향은 간접적이다.**
- **대체 관계**: 🔴 **볼트 보유 도구 중 직접 대체 대상 없음** — 에이전트 *감사* 범주 자체가 볼트 신규다. ⚖️ 성격상 [[context-mode]](컨텍스트 최적화)·[[claude-mem]](메모리)와 **경쟁이 아니라 보완**이다.
- **허와 실**: ✅ **실**: 검사 ID·영향도·필수 최소 구조가 표로 공개 · 비용·콜 수 명시 · **의도적 결함 픽스처로 "첫 실행 FAIL 이 정상"임을 미리 알린다**(사용자 오해 방지 설계). 🔴 **허에 가까운 것**: *"120초 이내"* 는 **기본 10검사 기준**이고 full-run 은 6배이므로 **12분 급**이 된다(단순 환산 · 🔴 **README 에 full-run 시간 미제시**). 🔴 **그리고 비용 각주가 2.35배 어긋나 있다.**
- **액션**: 아래 action 참조.

> [!action] 당장 할 것
> ⬜ 🔴 **값 충돌 2건 해소** — `docs/scoring.md` 와 `ifixai/fixtures/default/README.md` 를 1회 열어 전체 스위트 규모(50 vs 60)와 심판 콜 수(2,000 vs 4,700)를 확정한다. 📌 **비용은 요청 2회다.** ⚖️ **금일 미실행 — 명시적 이월 1건으로 기록한다.**
> ⬜ 🏆 **볼트 자기감사 설계에 B06·B16 채택(무비용 · 즉시)** — *"모르면 모른다고 한다"*(B06)·*"실패를 성공으로 포장하지 않는다"*(B16)는 이미 볼트 `CLAUDE.md` 원칙이다. 📌 **금일부터 배치 보고에 이 2항목의 자기판정을 명시한다.**
> ⬜ ⚖️ **설치·실행은 보류 판정한다.** 🔴 **이유를 적는다**: 기본 실행이 **에이전트 콜 850 + 심판 콜 820**(총 1,670 콜)이고 **심판은 유료 API**다 ⇒ **볼트의 "외부 코드 실행 0건" 적자를 해소할 후보로는 비용이 과하다.** 📌 **더 싼 후보는 여전히 [[context-mode]] 로컬 기동이다**(무료 · MCP 서버 · 비교 수치 13~100% 확보됨).

> [!question] 미해결 질문
> - 🔴 **전체 스위트가 50 인가 60 인가** — README 내부 충돌(미해소 · 이월)
> - 🔴 **full-run 심판 콜이 2,000 인가 4,700 인가** — README 내부 충돌(미해소 · 이월) · **비용 추정의 근거**
> - **full-run 소요 시간** — 미제시(기본 120초의 6배로 추정되나 확인 안 함)
> - **툴 권한 계층 미노출 에이전트에서 B01·P01 이 무엇을 보고하는가** — `docs/scoring.md` 로 넘겨져 있음
> - **60개 검사 전체 목록** — README 는 기본 10개만 표로 제시

## 관련 페이지
- [[요약자와-판정자-분리]] — 🏆 **제품이 구현한 형태**(크로스벤더 심판 2개 · 동점은 `fail` 우선)
- [[CriticOPD]] — 🏆🏆 **금일 같은 배치 · 정반대 경로(증류 이론) · 같은 결론(역할/벤더 분리)**
- [[문서내-값충돌]] — 🆕 **본 건이 1호 사례**(2,000↔4,700 · 50↔60)
- [[단위-불일치]] — 형제 개념(그쪽은 단위·지시대상 불일치 · 이쪽은 **같은 단위 값 충돌**)
- [[측정도구-먼저-반증]] — 🏆 레포가 자기 측정의 조건부 한계(총점 보류·툴계층 미노출)를 먼저 적는다
- [[복합지표-분해]] — 🔴 `open_issues` 8 미분해
- [[임계-의존-성공률]] — "필수 최소 3종 없으면 총점 보류" = 점수의 임계 의존
- [[ifixai-ai]] — 저작 조직(엔티티)
- [[rea]] · [[VoiceStudio]] · [[pentagi]] · [[context-mode]] — 금일 GitHub 동일 배치
- [[ai-news]]

## 원본
- 출처: https://github.com/ifixai-ai/iFixAi
- 수집: 2026-10-15 자동수집(ai-news) · **볼트 신규**(금일 GitHub 5건 중 유일 신규) · 인제스트 2026-10-15
- 볼트 실측 **2건**: GitHub API `/repos`(HTTP **200** · ★27,995 · 포크 1,523 · watchers 410 · issues 8 · Apache-2.0 · topics 20개) · **README 전문**(`raw.githubusercontent.com` HTTP **200** · **27,625 B**)
- raw 대비: ✅ 스타(+9)·포크·언어·라이선스·생성일 **일치** · ✅ **수집기 README 수치 5/5 전건 정확** · 🏆 **볼트 신규 4건**: **README 내부 값 충돌 2건 적발**(2,000↔4,700 심판콜 · 50↔60 스위트) · 850 은 에이전트 콜이고 심판 콜 820 이 별도임을 분리 · 기본 10검사의 조건부 한계(총점 보류·툴계층 의존) 발굴 · topics 로 **규제 대응 도구** 성격 특정
- 신뢰도: ⭐⭐⭐ (지표·README 1차 확인 / 🔴 **문서 내부 모순 2건 미해소 · 외부 코드 실행 0건 · 60개 검사 목록 미확인**)
