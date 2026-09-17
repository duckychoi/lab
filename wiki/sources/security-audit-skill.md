---
title: cloudflare/security-audit-skill — 심각도를 붙일 수 없는 칸을 설계의 중심에 둔 스킬 묶음
type: source
domain: ai-news
tags: [ai-news, github, agent-skills, security, verification, evidence-gate, self-limitation]
created: 2026-09-17
updated: 2026-09-17
sources: []
reliability: high
---

# GitHub: cloudflare/security-audit-skill — ★8,529

**URL**: https://github.com/cloudflare/security-audit-skill
**지표(2026-09-17 볼트 API 실측)**: ★ **8,529** · fork **474** · MIT · 생성 **2026-06-18** / 푸시 **2026-09-14** · `topics` **0개**
**드리프트**: raw ★8,506 → 볼트 **8,529 (+23)** · fork 472 → **474 (+2)**
🏗️ **신규 릴리스** (생성 3개월) · 트렌딩 daily 2위 · 당일 +927 = **상대속도 10.90%**

> [!insight] 🎯 **이 배치의 척추 — "확인되지 않음"을 위한 전용 칸**
> 이 스킬의 중심은 6단계 절차가 아니라 **판정 3분류를 스키마로 강제하는 것**이다. 볼트 README 20행 **문자 일치 확인**:
> > *"The verdicts are distinct: `confirmed` has a complete source trace and bounded observed result, `needs_validation` has **an exact unresolved fact and no severity**, and `rejected` records a disproved candidate."*
>
> 🎯 **`no severity` 가 설계의 핵이다.** 심각도를 붙일 수 있는 칸과 **붙일 수 없는 칸을 물리적으로 분리**했다. 확인되지 않은 후보는 "낮은 심각도"가 아니라 **심각도 자체가 없는 상태**로 남는다 — 등급이 아니라 **범주**로 갈랐다.
> 🔗 **같은 배치 [[oh-my-hermes]] 가 완전히 다른 생태계에서 같은 것을 만들었다** → [[검사가능성-공사]] 갱신 근거.

> [!insight] 🔴 **볼트 추가 — 수집기가 놓친 자기제한 조항 (README 90행)**
> 수집기 보고: *"탐지율 수치가 README에 없다 → 확인 불가."* **사실이다.** 그러나 **더 중요한 조항이 90행에 있다**:
> > *"An OS-enforced sandbox for target-controlled builds, tests, processes, browsers, emulators, fuzzers, and fixtures... **Without these controls, the workflow keeps the lead as `needs_validation` instead of executing target code.**"*
>
> 🎯 **도구가 자기 실행 조건이 미충족일 때 무엇을 하는지 미리 적어 뒀다** — 샌드박스가 없으면 **확인을 포기하고 `needs_validation` 에 남긴다.** 조건 미달 시 **조용히 낮은 신뢰도로 진행하지 않는다.**
> 📌 이것이 *"탐지율 수치가 없다"* 보다 **검증가능성에 대해 더 많은 것을 말한다** — 수치는 성능의 약속이고, 이 조항은 **실패 모드의 약속**이다. → [[자기제한-명시]]

> [!note] 설계 원칙 3개 — 전부 "누가 판정하는가"에 대한 것 (README 92~96행)
> - *"**Only confirm established boundary failures.** Keep a source-grounded blocked lead as `needs_validation` with its exact unresolved fact."*
> - *"**Adversarial validation.** The agent that checks a finding is never the agent that found it."*
> - *"**Severity requires impact.** Likelihood x impact, not deviation from a checklist."*
>
> 🎯 두 번째가 [[요약자와-판정자-분리]] 의 **보안 도메인 판본**이다 — 찾은 에이전트와 검증하는 에이전트를 **강제로 분리**한다.
> 세 번째는 체크리스트 이탈을 취약점으로 세지 않는다 — **[[측정도구-먼저-반증]] 과 같은 동작**(관행 지표를 먼저 부정).

> [!insight] 재실행이 가산적(additive)이다 — 볼트 22행 확인
> > *"Multiple runs against the same repo are additive. The skill uses prior ledgers and findings to target gaps, revalidate changed source, and carry forward current-source evidence **without treating stale or unresolved work as covered**."*
>
> 🎯 **마지막 절이 핵심이다** — 이전 실행의 미해결 항목을 "처리됨"으로 넘기지 않는다. 커버리지 원장(`validate-coverage-ledger.cjs`)이 **빈 구멍을 상태로 보존**한다. [[국소-수리-원리]] 와 같은 구조.

> [!warning] 🔴 성능 수치가 레포에 없다 — 확인 불가
> 탐지율·재현율·오탐률 **일절 없음**(README 106행 전수 확인). Cloudflare 블로그(`build-your-own-vulnerability-harness`) 링크만 있고 **레포 자체에 벤치가 없다.**
> ⚠️ **볼트도 블로그를 읽지 않았다** — 볼트가 추가한 것은 **"어디로 가면 있는지"** 까지다. [[메타데이터-부재-추론]] 원칙대로 *"성능이 없다"* 가 아니라 **"레포에서 확인 불가"** 로 기록한다.
> ⚠️ `topics` **0개** — [[메타데이터-부재-추론]] 포화도 사례에 추가(0개인데 실재 AI 스킬).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ high. Cloudflare 공식 · MIT · ★8,529 · **README 조항이 구체적이고 반증 가능**(샌드박스 조건·판정 3분류·검증자 분리). 성능 수치 부재는 감점이나 **주장 자체를 안 한 것**이므로 [[한정어-탈락]] 해당 없음
- **즉시 활용**: **YES.** 모델이 아니라 마크다운+JS 검증기라 **어떤 코딩 에이전트에도 붙는다**(요구사항: 도구 사용 + 병렬 서브에이전트 + Node.js). 의존성 0
- **6개월 영향력**: 🎯 **높음 — 단 보안 도구로서가 아니라 판정 스키마로서.** `confirmed/needs_validation/rejected` 3분류는 **도메인 무관**이다. 볼트 자체의 수집기↔볼트 프로토콜이 같은 일을 하고 있다(주장/구현 구분·확인 불가 표기)
- **대체 관계**: 기존 SAST 도구를 대체하지 않는다. **에이전트가 이미 찾은 후보를 승격시킬지 판정하는 층**이다
- **허와 실**: 🎯 **과장이 거의 없다.** *"AI가 취약점을 찾는다"* 류 문구 없고, 대신 **확인 못 한 것을 확인 못 했다고 남기는 장치**를 판다. AI를 빼면 마크다운 문서만 남으므로 **AI 네이티브** 판정 유지
- **액션**: 판정 3분류 스키마를 **볼트 ingest 절차에 이식 검토** — 현재 볼트는 `🔴 확인 불가` 표기를 쓰지만 **스키마 강제는 없다**

> [!action] 볼트 자체 적용 후보
> `needs_validation = "정확한 미해결 사실 + 심각도 없음"` 을 볼트 규칙으로 승격할 것인가.
> 현재 볼트는 `🔴 확인 불가` 를 **서술로** 적는다. 이 스킬은 **심각도 필드를 비울 수 없게** 만들었다 — 서술과 스키마의 차이.

## 관련 페이지
- [[oh-my-hermes]] — 🎯 **같은 배치·다른 생태계·같은 발명**(`Code · reported done` vs `Test · verified`)
- [[검사가능성-공사]] · [[자기제한-명시]] · [[요약자와-판정자-분리]] · [[국소-수리-원리]]
- [[agent-skills]] · [[superpowers]] · [[ECC]] · [[wshobson-agents]] — 하네스/스킬 계층
- [[Cloudflare]] · [[메타데이터-부재-추론]] · [[ai-news]]

## 원본
- 출처: https://github.com/cloudflare/security-audit-skill
- 검증: GitHub API 실호출(2026-09-17) · **README 106행 전문 대조** — 수집기 인용(20행) **문자 일치** · 볼트 추가 인용 3건(22·90·92~96행)
- 신뢰도: ⭐⭐⭐
