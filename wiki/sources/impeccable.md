---
title: impeccable — AI 하네스 디자인 언어 (pbakaus)
type: source
domain: ai-news
tags: [ai-news, github-trending, design-system, ai-harness, frontend, claude-code, agent-skills, design-tokens]
created: 2026-07-27
updated: 2026-10-28
sources: []
reliability: high
---

# impeccable (pbakaus/impeccable, ⭐51,000)

> [!update] 2026-10-04 갱신 — ★75,664 (볼트 실측 · **관측 2026-10-04T09:12:13Z**) · 🏆 **size 384MB 발견** · 🔴 **어제 "진단과 증거가 만났다"는 기록의 독립성을 철회한다**
> **볼트 독립 실측 ★75,664** ↔ 수집기 ★75,655 = **드리프트 +9**. 어제 볼트 실측 ★74,563 → **구간 증분 +1,101**(⚠️ 어제 기록에 관측 시각이 없어 구간 길이 미확정 — [[ponytail]] 과 같은 결함).
> ✅ **일치**: open_issues **57** · **Apache-2.0** · created 2025-11-16 · 주언어 **JavaScript**. 🔵 fork **4,531** ↔ 수집기 4,530 = **+1**.
> 🏆 **`pushed` 2026-10-04T09:04:31Z = 볼트 관측 시각보다 8분 앞이다.** 배치 5건 중 **가장 활발**하다([[caveman]] 07:51Z · [[ponytail]] 어제 · [[ECC]] 10-02 · [[Agent-Reach]] 09-15). 📌 *"관측 시각 병기"* 가 왜 필요한지 보여주는 사례 — **8분 차이는 시각 없이는 표현 자체가 불가능하다.**
>
> 🔴 **`topics` 0 — 2일 연속 확증. 10-02 가설 기각이 유지된다(n=2).**
> 10-02 가설: *"topics 는 규모가 아니라 배포 의도를 반영한다"*. impeccable 은 ★75,664 · `npx impeccable install` 1줄 배포인데 **topics 0** 이다. 📌 오늘 같은 배치 비교: [[Agent-Reach]] **17** · [[ponytail]] **10** · [[caveman]] **10** · 🆕 [[ECC]] **8** · **impeccable 0**. ⇒ ⚖️ **★27만([[ECC]])도 ★7.5만(impeccable)도 topics 를 안 채우거나 적게 채운다. `topics` 는 메인테이너가 그 칸을 채웠는지만 반영한다**(10-03 결론 유지) → [[메타데이터-부재-추론]].
>
> 🏆🏆 **볼트 신규 발견 — `size` 384,342KB ≈ **375MiB**. 배치 최대이고 2위([[ECC]] 54,908KB)의 7배, [[ponytail]] 의 **142배**다.**
> 🎯 **이 수치가 레포의 자기 서술과 긴장 관계에 있다.** 수집기가 전한 핵심 주장은 *"**LLM 호출과 API 키 없이** 결정론적 검출 규칙 61개를 실행한다"* 이고, 그 그림대로면 **규칙은 텍스트**이므로 레포가 클 이유가 없다([[ponytail]] 의 규범 텍스트 자산이 2.7MB다).
> 🔴 **384MB 의 내용은 조회하지 않았다.** 가능한 설명이 최소 3개이고 **구분할 근거가 없다**: ① 브라우저 확장 번들 · ② 비주얼 회귀 테스트의 스크린샷 픽스처 · ③ 폰트·에셋 동봉. ⚖️ **"규칙이 무겁다"고 적지 않는다 — "레포가 무겁고 이유를 모른다"가 현재 상태다.** → actionable 등록(`GET /contents/` 1회로 상위 디렉터리 크기 분포 확인 가능).
>
> 🔴🔴 **10-03 기록의 지위를 정정한다 — 그것은 독립 관측이 아니었다.**
> 어제 볼트는 *"🏆 오늘 이 레포의 진단이 같은 배치에서 실물로 확인됐다"* 며, impeccable README 가 지목한 *"전부 Inter 폰트"* 를 [[HC-DLM]] 프로젝트 페이지에서 **1건 확인**했다고 적었다. 수집기가 오늘 **그 출처가 이 README 임을 확인**했다고 전한다.
> ⇒ ⚖️ **순서가 중요하다: 볼트는 README 의 진단을 먼저 읽고 나서 폰트를 찾았다. 즉 탐색이 가설에 의해 지시됐다(directed search).** 🔴 **이것은 독립 확증이 아니라 확증 편향에 열린 n=1 이다** — 반증을 찾으려면 **Inter 가 아닌 AI 생성 프런트엔드를 세어야** 하고, 그 작업은 하지 않았다.
> 📌 **따라서 10-03 의 *"진단과 증거가 만났다"* 는 *"진단을 읽고 한 건을 찾았다"* 로 약화해 보존한다.** [[관심-검증-역상관]] · [[측정도구-먼저-반증]] 에 **"도구의 진단을 읽은 뒤의 관측은 그 도구의 검증이 아니다"** 로 등재.
> ⚖️ **이 레포 자체가 반증 수단을 제공한다** — 규칙 61개가 **결정론적**이고 **LLM 없이** 돌므로, 임의 표본에 CLI 를 돌리면 Inter 가설을 **정량 검증**할 수 있다. 🏆 **즉 `npx impeccable` 은 디자인 도구가 아니라 볼트에게는 측정 도구다.** → actionable 최우선.
>
> ✅ **확증된 자기 서술**: 스킬 **1** + 커맨드 **24** + 결정론적 규칙 **61**(LLM 비평 체크는 별도 층) · Anthropic `frontend-design` 스킬 **파생 자체 명시** · 설치 1줄 `npx impeccable install`.
> 📌 watchers **207**. 🔴 **규칙 61개의 목록은 여전히 미열람**(3배치 연속) — 개수만 알고 내용을 모른다 → [[표-부분인용]] 경계.

> [!update] 2026-10-03 갱신 — ★74,563 (볼트 실측) · 🏆 **같은 배치 안에서 진단과 증거가 만났다** · 🔴 **topics 가설 반례 확정**
> **볼트 독립 실측 ★74,563** ↔ 수집기 ★74,559 = **드리프트 +4**. 기존 베이스라인 ★51,000(2026-07-27) → **+23,563 / 68일 = 일평균 ≈346**.
> ✅ **전 필드 일치**: fork **4,491** · open_issues **64** · **Apache-2.0**(볼트 기존 기록 일치) · created 2025-11-16 · **pushed 2026-10-03T07:35:50Z = 당일 활성** · 주언어 **JavaScript**(볼트 기존 기록 일치).
> 🔴 **`topics` 0 확증 — 10-02 가설의 반례가 확정됐다.** 10-02 에 볼트는 *"topics 는 규모가 아니라 배포 의도를 반영한다"* 는 가설을 세웠다. impeccable 은 **★74,563 · `npx impeccable install` 1줄 배포 · 스킬 1 + 커맨드 24개**로 **배포 의도가 명백한데 topics 가 0 이다**. ⇒ ⚖️ **가설 기각. `topics` 는 배포 의도도 규모도 반영하지 않는다 — 메인테이너가 그 칸을 채웠는지만 반영한다.** 📌 같은 배치의 [[Agent-Reach]] topics **17** ↔ impeccable **0** 이고 둘 다 ★7만~8만대 배포형이다 → [[메타데이터-부재-추론]] 에 **"칸이 비어 있음은 대상에 대한 정보가 0"** 유형 추가.
> 🏆 **오늘 이 레포의 진단이 같은 배치에서 실물로 확인됐다.** impeccable 의 문제 설정은 *"모든 모델이 같은 SaaS 템플릿으로 학습돼 가이던스 없이는 매 프로젝트에 같은 몇 가지 흔적(**전부 Inter 폰트** 등)이 나온다"* 다. 볼트가 오늘 같은 배치의 [[HC-DLM]] 논문 프로젝트 페이지 `hc-dlm.github.io` 를 열람(HTTP 200 · 34,296B)했더니 **외부 폰트 로드가 `family=Inter`(+Fira Code) 단 하나**였다.
> ⚖️ **그래서 이 주장의 지위가 올라간다**: 마케팅 문구가 아니라 **볼트가 독립 소스에서 1회 관측으로 확인한 패턴**이다. 🔴 **단 n=1 이다. "전부"를 지지하지는 않는다** — 반증 가능한 형태로 적어 둔다(향후 프로젝트 페이지 열람 시 폰트를 기록한다).
> ✅ **구조적 강점 재확인**: *"61개 **결정론적** 검출 규칙"* 은 LLM 판정이 아니라 **검출기**라 재현 가능성이 높은 쪽이다. 🔴 **효과 수치는 여전히 0개** — 규칙 수(61)는 규모이고 성능이 아니다 → [[복합지표-분해]].
> 🎯 **계보 자기신고**: *"Anthropic 의 frontend-design 이 Claude 최초의 범용 디자인 스킬이었고 Impeccable 은 거기서 출발했다"* (README 명시) → [[파생저장소-식별]] **자기신고형**.

**GitHub**: https://github.com/pbakaus/impeccable
**스타수**: ⭐51,000 (2026-07-27, 당일 +413) / JavaScript·TypeScript / Apache 2.0

> [!insight] 핵심 인사이트
> "AI 하네스를 디자인에 더 능숙하게 만드는 **디자인 언어**." AI 코딩 에이전트가 만들어내는 프런트엔드의 고질적 약점(밋밋한 UI·안티패턴)을 **프롬프트가 아니라 검증 가능한 룰셋**으로 잡는다. 핵심은 두 축: ①`/impeccable audit`·`/impeccable polish`·`/impeccable critique` 등 **23개 슬래시 커맨드**(스킬), ②**60개 결정론적(deterministic) 디텍터 룰**로 흔한 디자인 안티패턴을 API 키 없이 파일·URL 스캔으로 잡아냄. [[Google-Labs]]의 [[design.md]]가 "에이전트에 주입하는 디자인 명세"였다면, impeccable은 거기에 **결정론 검출기 + 라이브 브라우저 이터레이션**을 붙여 "명세→자동 감사→수정" 루프로 발전시킨 형태 — 즉 [[SWE-Pruner-Pro]]·[[open-code-review]]가 코드에서 한 "LLM 판단을 결정론 룰로 보강" 패턴의 **디자인판**.

## 핵심 인사이트

> [!note] 구조 (README 실측)
> - **23개 커맨드**: audit(감사)·polish(다듬기)·critique(비평) 등 — [[agent-skills]] 형태로 하네스에 설치
> - **60개 결정론 디텍터 룰**: 대비 부족·간격 불일치·타이포 위계 붕괴 등 안티패턴을 규칙으로 검출 (LLM 호출 없이 확정적)
> - **CLI**: API 키 불필요, 로컬 파일·라이브 URL 스캔
> - **멀티 플랫폼**: 여러 AI 코딩 도구(Claude Code·기타 하네스) 지원, 라이브 브라우저 이터레이션 포함

> [!action] tools-frontend / reat 계열에 직접 참고
> 내 [[tools-frontend]]·[[reat-layout]]·[[reat-analyze]]가 "AI로 프런트/레이아웃 생성"을 하는데, 결과물 디자인 품질은 항상 약점. impeccable의 **60개 결정론 룰 + audit 커맨드 구조**를 참고해, 생성된 레이아웃/슬라이드에 "결정론 디자인 게이트"를 붙이는 실험 가치 큼. Apache 2.0이라 룰셋 차용 가능.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐51,000(당일 +413), Apache 2.0. GitHub API 실검증. "디자인 완성도 향상" 효과 주장은 산출물 재현으로 확인 필요하나 룰셋·CLI 존재는 확정.
- **즉시 활용**: YES — CLI가 API 키 없이 파일·URL 스캔이라 즉시 시험 가능. 내 프런트 산출물에 audit 돌려 안티패턴 목록만 뽑아도 가치.
- **6개월 영향력**: "에이전트에 디자인 감각을 코드로 주입" 흐름의 대표 사례. [[design.md]]·[[Impeccable]]류가 표준화되면 AI 생성 UI의 하한선이 올라감 — 순수 프롬프트로 디자인 품질을 올리려던 접근을 **결정론 룰 게이트**가 대체·보강.
- **대체 관계**: 디자인 시스템 문서(피그마·스토리북)를 대체하진 않지만, **AI 산출물 품질 게이트**로서 수작업 디자인 리뷰의 1차 필터를 대체.
- **허와 실**: "디자인을 잘하게 만든다"는 결국 룰 커버리지에 달림 — 60개 룰이 잡는 건 안티패턴 회피이지 창의적 디자인은 아님. 하한선 상승 도구로 이해.
- **액션**: CLI 설치 → 내 프런트 산출물(reat 슬라이드·tools-frontend)에 audit 실행, 결정론 룰 60개 중 이식 가능 항목 추출.

## 관련 페이지
- [[design.md]] — 에이전트용 디자인 명세 (impeccable의 선행 계보)
- [[Google-Labs]] — design.md 배포처
- [[agent-skills]] — 23개 커맨드의 배포 단위
- [[open-code-review]] — 코드판 "결정론 룰 + LLM" 하이브리드
- [[SWE-Pruner-Pro]] — "모델 판단을 결정론 신호로 보강" 계보
- [[tools-frontend]] — 내 프런트 개발 오버레이 (적용 대상)
- [[reat-analyze]] — 내 디자인 토큰 추출 스킬 (연결점)

## 원본
- 출처: https://github.com/pbakaus/impeccable
- GitHub: ⭐51,000 (2026-07-27, 당일 +413), JavaScript·TypeScript, Apache 2.0
- 구성: 23 커맨드 + 60 결정론 디텍터 룰 + 키 불필요 CLI + 라이브 브라우저 이터레이션
- 신뢰도: ⭐⭐⭐⭐⭐ (GitHub API 실검증, 대규모 스타·명확한 구조. 디자인 향상 "효과"는 산출물 재현 전 잠정)

---

## 📥 2026-10-05 재관측 (자동수집 10-05 배치 · 갱신)

**볼트 독립 실측 2026-10-05**: ★**76,638** · fork **4,573** · open_issues **60** · **Apache-2.0** · pushed **2026-10-05**
**드리프트**: 수집기 ★76,634 → 볼트 **+4** · fork·issue·라이선스·pushed **전건 일치**
**수집기 보고**: 당일 **+1,171** · 트렌딩 **2위**(배치 최고 순위) · 생성 2025-11-16

> [!warning] 🔴 규칙 61개 목록 미열람 — **4배치 연속**
> 10-02·10-03·10-04 에 이어 또 열지 않았다. 🎯 **이 레포가 볼트에게 디자인 도구가 아니라 측정 도구인 이유는 그대로다** — 규칙 61개가 **결정적이고 LLM 없이 돌며 API 키가 필요 없다**. ⇒ **`npx impeccable` 은 볼트가 지금 당장 실행 가능한 유일한 외부 검증기다.**
> 🔴 **384MB 레포 크기 내용도 4배치째 미조회**(10-04 실측 `size` 384,342KB = ponytail 의 142배). *"LLM 없이 도는 결정적 규칙 61개"* 라는 자기 서술과의 긴장은 미해소다.

> [!insight] 🎯 10-05 배치와의 연결 — "결정적 검사"가 두 층에서 같이 나왔다
> [[SimuVerity]] 가 **게이트 3단**(제출 94.72% → 실행 86.47% → 공학자격 76.90%)을 **결정적 검사**로 돌린 뒤 **다차원 점수**를 따로 낸다.
> 📌 **impeccable 의 구조와 같다**: 결정적 룰 61개(게이트) + `DESIGN.md` 시각 방향(판단). ⚖️ **서로 인용하지 않는 두 프로젝트가 "먼저 결정적으로 걸러라"에 도달했다** → [[검사가능성-공사]].

**검증**: `api.github.com/repos/pbakaus/impeccable` 실측
**관련 추가**: [[SimuVerity]] · [[검사가능성-공사]] · [[표본순위-전수순위]]

---

## 🔄 2026-10-28 갱신 (인제스트 2026-10-28) — ★91,124 · 🏆 **규칙 목록을 5배치 만에 열었다(62개)** · 🔴 **주언어가 JavaScript → Rust로 바뀌었고, 볼트의 'topics 0' 기록 2건이 만료됐다**

**GitHub API 실측(2026-10-28T09:10Z)**: ★**91,124**(수집기 91,116 · **+8**) · fork **5,399** · open issues **46** · **Apache-2.0** ✅ · created 2025-11-16 · pushed **2026-10-28T08:57:03Z**(관측 13분 전) · 주언어 🔴 **Rust** · topics 🔴 **5** · size **888,336KB** · watchers 200
- 볼트 기준선 ★76,638(10-05) → **+14,486 / 23일 ≈ 630/일**(10-03 구간 ≈346/일의 1.8배).
- 🔴 **만료 1 — "topics 0"(10-03·10-04 두 번 확증)**: 지금 `agent-skills, ai, anti-slop, design, slop` **5개**다. 10-03 결론 *"topics는 메인테이너가 그 칸을 채웠는지만 반영한다"* 는 오히려 강화된다. 메인테이너가 칸을 채우자 값이 바뀌었다. 다만 "impeccable은 topics 0"이라는 **사례 서술은 만료** → [[메타데이터-부재-추론]]에 시점 표기 필요.
- 🔴 **만료 2 — 주언어 JavaScript**: GitHub languages API 바이트 기준 Rust 11.07MB · JavaScript 3.06MB · TypeScript 0.26MB. README: *"Every skill copy ships a small launcher… that runs the Impeccable engine, **a self-contained binary** that either sits next to the launcher or is **downloaded once on first run into `~/.impeccable/bin/`**. Node is only involved if you use the `npx impeccable` installer."* ⇒ **JS 스킬에서 Rust 엔진 + 런처 구조로 바뀌었다.** 릴리스도 `skill-v4.8.0` · `cli-v4.8.0` · `engine-v0.1.18`(10-26) 세 갈래로 나뉜다.

> [!insight] 🏆 규칙 62개 목록 — 10-02부터 5배치 연속 "미열람"이던 항목 해소
> 출처: `crates/live/assets/antipatterns.json`(23,755B, 데이터로만 읽음). **62개 = `slop` 31 + `quality` 31.** severity: 기본 44 · `advisory` 16 · **`error` 2**(`script-error`, `content-hidden-at-rest`).
> - 📌 **error 2개는 둘 다 "취향"이 아니라 "깨짐"이다**: 스크립트 예외, 리빌 실패로 텍스트가 opacity 0에 남는 것. 슬롭 31개는 전부 기본 또는 advisory다. ⇒ impeccable도 hallmark Floor/Reflex처럼 **"깨짐은 차단, 취향은 권고"** 2층 구조다.
> - 🎯 **벤더 이름이 붙은 규칙이 있다**: `gpt-thin-border-wide-shadow`(헤어라인 테두리 + 넓은 그림자 카드 행) · `codex-grid-background`(장식용 격자선 배경). 특정 모델/하니스의 생성 습관을 규칙 ID로 박제했다. 🔴 귀속 근거(정말 그 모델에서 더 자주 나오는지)는 파일에 없다.
> - `overused-font` 대상: *"Inter, Roboto, Fraunces, **Geist**, Plus Jakarta Sans, Space Grotesk"*. ⇒ 10-03/10-04의 "Inter 가설"을 볼트가 검증하려면 이 6종을 세면 된다.
> - 문구 규칙도 있다: `em-dash-overuse` · `marketing-buzzword` · `aphoristic-cadence` · `theater-slop-phrase`(*"Dismissing something as 'theater' is a recurring generated-copy tic"*). 시각 규칙만 있는 게 아니다.
> - 🔴 **같은 배치 충돌**: [[ai-design-skills]] `landing-page-design`은 Geist를 **권장 폰트 1순위**로, 히어로 그라디언트 텍스트를 **필수**로 지시한다. 둘 다 이 규칙 세트에서 슬롭이다. [[hallmark]]의 tell 목록과는 `kicker-above-heading`·`hero-eyebrow-chip`·`wide-tracking`이 겹친다.

> [!note] 📦 10-04 "size 384MB, 이유 모름" 중간 해소
> 지금 `size`는 **888,336KB(≈868MiB, 10-04의 2.3배)**다. HEAD 트리 전체 blob 합계(재귀 트리 5,037항목, 잘림 없음)는 **86.4MB**뿐이다. ⇒ **`size`의 대부분은 현재 파일이 아니라 git 이력(팩)이다.** HEAD 기준 상위: `tests/` 16.6MB(2,375파일) · `crates/` 16.1MB(Rust 494파일, 최대 파일 `detect-antipatterns-browser.js` 3.2MB) · 그리고 **하니스별 스킬 복사본 23벌**(`.claude` `.cursor` `.codex`계 `.agents` `.gemini` `.grok` `.hermes` `.kiro` `.trae` `.veto` … 각 ≈2.2MB, `font-index.json` 1.1MB가 23번 중복). 🔴 이력 쪽 무엇이 큰지는 조회하지 않았다. 10-04 가설 ①(브라우저 확장 번들)·②(테스트 픽스처)·③(에셋)이 **모두 HEAD에 일부씩 있다**는 것까지만 확인했다.
> 📌 23벌 복사본은 [[superpowers]] 10-03의 "README 열거 ≠ 유지되는 매니페스트" 구분에서 **②(실제로 파일을 유지)** 쪽 증거다. [[ponytail]] 9종보다 많다 → [[하네스-설계-축]].

> [!warning] 🔴 수집기 요약이 빠뜨린 것
> 1. **바이너리 다운로드**: 첫 실행 때 엔진 바이너리를 `~/.impeccable/bin/`에 내려받는다. "API 키 없이 돈다"는 맞지만 **네이티브 바이너리를 실행한다.** CI에 넣을 때는 버전 고정과 체크섬 확인이 필요하다(README에서 체크섬 언급은 확인하지 못했다).
> 2. **프로젝트에 훅을 설치한다**: *"On Claude Code, Cursor, Codex, GitHub Copilot, and Grok Build, it also installs the provider-native hook manifest for the current project."* Codex는 `/hooks`에서 승인해야 하고 *"updates that change `.codex/hooks.json` can require approval again"*. 스킬 설치가 **편집 시점 훅 설치**까지 포함한다.
> 3. 규칙 62개 중 **error는 2개뿐**이다. "62개 결정론 규칙으로 CI 차단"을 기대하면 안 된다. 대부분은 advisory이거나 severity 미지정이다.
> 4. ✅ 수집기 서술 일치: 커맨드 24 · 규칙 62(10-05의 61에서 +1) · `/impeccable init` → `PRODUCT.md` · Anthropic `frontend-design`에서 출발(README *"Impeccable started from there"*).

**검증**: `api.github.com/repos/pbakaus/impeccable` · `/languages` · `/git/trees/HEAD?recursive=1` · `/releases` · README 30,624B · `antipatterns.json` (전부 데이터로만 읽음, 🔴 미실행)
**관련 추가**: [[ai-design-skills]] · [[hallmark]] · [[하네스-설계-축]] · [[메타데이터-부재-추론]] · [[검사가능성-공사]]
