---
title: rlaope/oh-my-hermes — 자기 벤치마크 칸에 "아직 측정 안 했다"를 적은 레포
type: source
domain: ai-news
tags: [ai-news, github, agent-harness, hermes, evidence-gate, self-limitation, verification]
created: 2026-09-17
updated: 2026-09-17
sources: []
reliability: high
---

# GitHub: rlaope/oh-my-hermes — ★2,657

**URL**: https://github.com/rlaope/oh-my-hermes
**지표(2026-09-17 볼트 API 실측)**: ★ **2,657** · fork **189** · MIT · 생성 **2026-06-03** / 푸시 **2026-09-17** · `topics` **9개**
**드리프트**: raw ★2,653 → 볼트 **2,657 (+4)** · fork **189 완전일치**
🏗️ **신규 릴리스** (생성 3.5개월) · 트렌딩 daily 15위·python-daily 3위 · 당일 +80 = **상대속도 3.02%**

> [!insight] 🔴 **볼트 최대 정정 — 수집기가 "별도 문서 확인 필요"라 한 것이 같은 파일 586행에 있었다**
> 수집기 자기 한계 1번: *"`evidence boundaries` 가 실제로 무엇을 강제하는지는 README 상단 48행에 정의가 없다(docs/README.md 별도 확인 필요). **주장만 확인, 구현 미확인.**"*
> → 🔴 **README는 660행이고, 정의는 586행 `## Evidence Before Claims` 에 표로 있다.** 별도 문서가 아니라 **같은 파일 538행 아래**였다.
>
> **볼트가 읽은 4상태 어휘(586~596행 문자 일치)**:
> | 표시 | 의미 |
> |---|---|
> | `Plan · not run` | 프롬프트·계획이 준비됨. **아직 아무것도 실행되지 않았다.** |
> | `Code · running` | 실행자가 지금 돌고 있고 OMH가 보고 있다. |
> | `Code · reported done` | **실행자가 끝났다고 말했다. 아무도 결과를 확인하지 않았다.** |
> | `Test · verified` | 테스트·리뷰·CI 게이트가 **실제로 통과했다.** |
>
> 🎯 **설계 이유를 README가 직접 적는다**: *"an executor saying it is done is not the same as anything having been checked, and **most tools spell both "complete"**."*
> 📌 **"완료"라는 한 단어가 두 상태를 덮는다는 진단** — 이것이 `evidence boundaries` 의 실체다. 주장이 아니라 **어휘를 나눈 구현**이다.

> [!insight] 🎯 **그리고 이 레포는 자기 기준을 자기에게 적용했다 — 배치 최고의 자기제한**
> README 604행 `### Measured: Hermes alone vs Hermes through OMH` 는 A/B 벤치 레인을 정의한다(자기 레포의 머지된 PR을 코퍼스로, 그 PR의 테스트로 채점, **4지표**: pass rate · cost per passed task · wall clock per goal · **false-completion rate**).
> 그 다음 줄이 결정적이다 — 볼트 문자 일치:
> > *"**No measured run has been published yet.** The lane, its corpus, and its offline pilot are in place; this section carries the table once a run exists whose records the repository can point at."*
>
> 🎯 **벤치마크 섹션을 지우지도, 미검증 수치로 채우지도 않았다.** 섹션을 남겨 두고 **"아직 측정 안 됨"** 을 적었다 — 즉 **자기 4상태 어휘의 `Plan · not run` 을 자기 벤치마크에 적용한 것**이다.
> 📌 **볼트가 지금까지 본 [[자기제한-명시]] 사례 중 가장 강한 형태**다. [[earendil-works]](경계·무모순·대안 3칸) 는 *제품의* 한계를 적었고, 이쪽은 **자기 증거 기준을 자기 주장에 재귀 적용**했다.
> 🔴 **따라서 수집기의 "구현 미확인" 판정은 결론은 맞았지만 이유가 틀렸다** — 수치가 멀리 있어서가 아니라 **수치가 존재하지 않고 레포가 그렇게 적었기 때문**이다.

> [!insight] 🔗 같은 배치 교차 — 두 독립 생태계가 같은 것을 발명했다
> [[security-audit-skill]](Cloudflare·보안) 의 `needs_validation` = *"an exact unresolved fact and **no severity**"*
> 이 레포(Hermes·에이전트 운영) 의 `Code · reported done` = *"실행자가 끝났다고 말했다. **아무도 확인하지 않았다**"*
> 🎯 **둘 다 "주장됨"이 "확인됨"으로 승격되지 못하게 막는 전용 칸을 만들었다.** 도메인·생태계·저자 무관하게 **같은 해법**에 도달했다 → [[검사가능성-공사]] 에 **수렴 증거**로 등재.

> [!note] Hermes를 대체하지 않는다 — 위에 얹는 운영 계층
> README 43행(수집기 인용 문자 일치): *"frames the problem, picks the workflow and evidence gates, and runs native skills as capabilities inside that governed path"*
> 🎯 볼트에 이미 [[agent-skills]]·[[ECC]]·[[superpowers]] 같은 **Claude Code 계열 하네스** 페이지가 있는데, 이건 **[[NousResearch]] Hermes 계열**이다 — 같은 패턴의 **다른 생태계 표본**. 계층화가 특정 하네스의 특성이 아니라 **에이전트 운영의 일반 요구**라는 증거.
> 구성(섹션 헤딩 18개 실측): per-model tuning · 카테고리 소유 · 모델 패밀리별 프롬프팅 · 안전한 병렬화 + 타입 반환 · Ultra-Skills · 장기 메모리.

> [!warning] 미확인 항목
> - **코드를 읽지 않았다.** 4상태 어휘가 런타임에서 실제로 강제되는지(=상태 전이 검사가 코드에 있는지)는 **README 진술 확인까지**다
> - `docs/CAPABILITY_IMPACT.md` · `benchmarks/product-ab/v1/README.md` **미확인** — README가 가리키는 1차 출처를 볼트도 따라가지 않았다
> - ★2,657 · 생성 3.5개월 · **제3자 검증 이력 없음**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ high. 🎯 **수치가 없는데 high다** — 이유는 **없는 것을 없다고 적었기 때문**이다. [[한정어-탈락]] 의 완전한 반대 사례. 볼트 09-16 관찰(*"한정어를 지킨 건은 high, 떨어뜨린 건은 low/medium"*)의 **가장 깨끗한 확증**
- **즉시 활용**: **조건부 NO** — Hermes 계열 스택이 전제다. 🎯 **그러나 4상태 어휘는 스택 무관하게 즉시 쓸 수 있다**
- **6개월 영향력**: 중간. 레포 자체보다 **어휘의 전파력**이 크다 — `reported done ≠ verified` 구분은 어떤 에이전트 운영에도 적용된다
- **대체 관계**: Hermes Agent를 **대체하지 않고 감싼다**. 볼트의 Claude Code 계열 하네스와 **경쟁이 아니라 평행 진화**
- **허와 실**: 🎯 **허가 거의 없다.** *"honest record of what actually happened"*(38행) 같은 문구가 있지만 **같은 README가 그 honest record의 빈 칸까지 보여준다**
- **액션**: 4상태 어휘를 **볼트 log.md 기록 형식에 이식 검토** — 현재 볼트는 `✓확인/🔴확인 불가` 2값이다. **`보고됨(미확인)` 칸이 없다**

> [!action] 🎯 볼트 규칙 후보 — 60행 제한의 오적용
> **"README 60행 인용" 규칙은 *제외 판정*을 위해 만들어졌는데, *채택 건*의 독해 상한으로 오적용되고 있다.**
> 이번 배치에서 **두 번 대가를 치렀다**: 이 레포(정의가 586행) · [[cline]](헤드리스 전용 섹션이 219행).
> → 다음 배치 요청: **채택 건은 섹션 헤딩을 전수 스캔한 뒤 관련 섹션을 읽을 것.** 비용은 `grep "^##"` 한 번이다.

## 관련 페이지
- [[security-audit-skill]] — 🎯 **같은 배치·다른 생태계·같은 발명**
- [[자기제한-명시]] — **최강 사례**(자기 기준의 재귀 적용) · [[검사가능성-공사]] — 수렴 증거
- [[NousResearch]] · [[agent-skills]] · [[ECC]] · [[superpowers]] · [[wshobson-agents]]
- [[한정어-탈락]] — 완전한 반대 사례 · [[cline]] — 같은 독해 누락 패턴
- [[ai-news]]

## 원본
- 출처: https://github.com/rlaope/oh-my-hermes
- 검증: GitHub API 실호출(2026-09-17) · **README 660행 중 섹션 헤딩 18개 전수 + 586~618행 전문 대조** — 수집기 인용(43행) **문자 일치**, 🔴 **수집기 "미확인" 항목을 볼트가 같은 파일에서 발견**
- 신뢰도: ⭐⭐⭐
