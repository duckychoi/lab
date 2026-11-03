---
title: "t3code — 로컬 코딩 에이전트 6종을 모바일·웹에서 제어하는 하네스 제어면"
type: source
domain: ai-news
tags: [ai-news, github-trending, harness, control-plane, 자기제한, 메타데이터부재, mobile]
created: 2026-10-10
updated: 2026-11-03
sources: []
reliability: medium
---

# t3code — 자기를 "agent harness control surface"로 규정한다

**GitHub**: https://github.com/pingdotgg/t3code
**★25,745** (당일 +485 · **트렌딩 4위**) · fork 6,628 · watchers 68
**open_issues 2,499 = 순수이슈 1,162 + PR 1,337**(배치 최대) · MIT · TypeScript · created 2026-02-08 · pushed 2026-10-06
**수집일**: 2026-10-06 · 인제스트 2026-10-10

> [!insight] 핵심 인사이트
> 자신을 *"agent harness control surface"* 로 **직접 규정하고**, 사용자 머신에 이미 설치·인증된 **Claude Code · Codex · Cursor · Grok Build · OpenCode · Google Antigravity** 를 iOS/Android 앱·웹앱·Electron 데스크톱에서 원격 제어한다. **별도 모델 구독을 팔지 않고 기존 구독을 그대로 쓴다**고 명시한다.
> 🎯 **[[하네스-설계-축]] 에 "제어면"이라는 층 이름이 공급자 쪽에서 붙은 사례다.** 금일(10-10) [[knowledge-work-plugins]] 의 직무 묶음과 [[mattpocock-skills]] 의 스킬 단위 사이에 **이 층이 들어간다.**

> [!warning] 🔴 [[메타데이터-부재-추론]] 신규 유형 — 설명 필드 자체의 부재
> API `description` 이 **`null`** 이고 `topics` 가 **0개**다. 레포 성격은 **README 첫 문단에서만** 얻었다.
> 📌 같은 배치 [[e2e]] 는 **필드가 있고 부정확**했으나 t3code 는 **비어 있다** — **두 유형이 동시에 나왔다.** 금일 [[mattpocock-skills]] · [[knowledge-work-plugins]] 가 같은 유형으로 누적된다.

> [!warning] 🔴🔴 open_issues 2,499 가 ★의 9.7% 다
> **PR 1,337 이 순수이슈 1,162 보다 많다.**
> ⚖️ **해석을 단정하지 않는다**: 활발한 외부 기여일 수도, 미처리 적체일 수도 있으며 **PR 의 생성일 분포를 보지 않았다**(볼트 확인 필요).
> 📌 대조: 금일 [[open-code-review]] 는 `open_issues` 286 = ★의 **0.63%** = 본 레포의 **1/15**.

> [!insight] ✅ `open_issues_count` 분해 규약이 확립된 배치다
> 10-06 5개 레포 전부 `open_issues_count == 순수이슈 + PR` 검산 통과(50=13+37 · 86=25+61 · 35=0+35 · 2,499 · 213=97+116).
> ⇒ 🆕 **규약: `open_issues_count` 는 이슈+PR 합계이며 GitHub Search API `is:issue`/`is:pr` 로 분해 가능하다.** 볼트 4배치 연속 요청 항목이고 **금일(10-10)도 5/5 이행됐다.**

> [!insight] 자기제한 서술 보유
> *"우리가 잘못된 방향으로 가면 포크해서 원하는 에디터를 만들 수 있게 전부 공개한다"*
> ⇒ [[자기제한-명시]] **2번째 사례**(10-04 [[ponytail]] 에 이어). 금일 [[mattpocock-skills]] 가 3번째다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — API 실측 · MIT. 🔴 **성능 수치 0개.**
- **즉시 활용**: **조건부 — 볼트 운영과 직접 관련이 있다.** 볼트는 Telegram 경유로 에이전트를 돌리고 있고, t3code 는 **같은 문제(원격 제어면)를 앱·웹으로 푼다.** ⚠️ **설치가 파이프-투-셸이다**(`curl -fsSL https://t3.codes/install.sh | sh` · Windows `irm … | iex`) ⇒ 설치 보류, 설계만 참조.
- **6개월 영향력**: 코딩 에이전트의 **실행 위치와 제어 위치가 분리**되면 "어디서 돌리나"가 선택 축이 된다. 볼트의 Telegram 경로는 이미 이 축에 있다.
- **대체 관계**: 터미널 고정 사용을 대체한다. 모델 구독은 대체하지 않는다(명시).
- **허와 실**: 🏆 **"기존 구독을 쓴다"는 비즈니스 모델 서술이 정직하다** — 모델 마진을 취하지 않는다고 적는다. 🔴 단 **호스팅·동기화 비용 구조는 미확인.**
- **액션**: 10-06 [[claude-mem]] 이 `--ide t3code` 전용 경로를 가진 점과 교차해 **하네스 층 지도**를 그린다.

> [!insight] 🏆🏆 배치 내부 교차 — 같은 날 트렌딩 두 레포가 서로를 참조한다
> [[claude-mem]] 이 **t3code 전용 설치 경로를 명시한다**: `npx claude-mem install --ide t3code` · *"T3 Code 의 활성 provider 를 탐색해 각 provider 홈에 네이티브 플러그인 등록"*.
> ⇒ ⚖️ **하네스 생태계가 층으로 쌓이고 있다는 1차 증거**(t3code = 제어면 · claude-mem = 그 위 메모리층). 금일 [[knowledge-work-plugins]] 가 **3번째 층**으로 이 가설을 보강한다.

> [!question] 미해결
> - **PR 1,337 의 생성일 분포** 미확인 ⇒ 기여 활발 vs 적체 판정 불가.
> - 호스팅·동기화 **비용 구조** 미확인.
> - 제어 대상 6종 중 **실제 동작 검증** 0건.

## 관련 페이지
- [[하네스-설계-축]] — "제어면" 층 이름
- [[메타데이터-부재-추론]] — 신규 유형(필드 부재)
- [[자기제한-명시]] — 2번째 사례
- [[claude-mem]] — 상호 참조하는 상위 메모리층
- [[e2e]] — 같은 배치, 메타데이터 다른 유형
- [[knowledge-work-plugins]] · [[mattpocock-skills]] — 금일 층 지도
- [[지표-창길이]] · [[pingdotgg]] · [[ai-news]]

## 원본
- 출처: https://github.com/pingdotgg/t3code
- 수집: 2026-10-06 자동수집 (ai-news) · 인제스트 2026-10-10
- 검증: GitHub API 실측 · `open_issues` 분해 2,499 = 1,162 + 1,337
- 신뢰도: ⭐⭐⭐

## 🔄 2026-10-31 갱신 (인제스트 2026-10-31) — ★33,204 · **"에이전트 하네스 제어면"으로 자기 규정 · 아직 0.1.x nightly**

**GitHub API 실측(10-31)**: ★**33,204**(수집기 33,195 · +9) · fork **8,694**(별 대비 26%) · MIT ✅ · pushed 2026-10-31T09:06Z · 릴리스 `v0.1.6-nightly.20261031.*` (하루 2회 이상)
- 📈 볼트 마지막 기록 ★25,745(10-10 페이지) → +7,459.
- ✅ 수집기 서술 확인: 지원 6종(Codex·Claude·Cursor·Grok Build·OpenCode·Antigravity, README 5·16행) · 자체 판매 없음(9행) · 각 CLI 사전 설치·로그인(18~23행). Antigravity는 예외적으로 CLI 불요(23행) — 수집기 "각 CLI 사전 설치"의 작은 예외.
- ⚖️ 수집기 누락: 설치가 `curl -fsSL https://t3.codes/install.sh | sh` 이고 버전이 **0.1.x nightly** 다. 원격 조작 도구인 만큼 노출 범위(인증·포트)를 먼저 확인해야 한다 — 🔴 README에서 보안 모델은 확인 못 함.
- 🔗 [[claude-mem]] 이 T3 Code 네이티브 플러그인을 지원한다(claude-mem README 171행) — 두 도구의 결합 경로가 실재한다.

## 🔄 2026-11-02 갱신 (인제스트 2026-11-02) — ★39,168 · **이틀 새 +5,964, 트렌딩 1위 · 지원 대상 7종(fx 추가) · LAN 모드는 페어링 코드가 유일한 문**

**GitHub API 실측(11-02 09시대)**: ★**39,168**(수집기 39,150 · +18 드리프트) · fork **8,975** · open_issues **4,051**(이슈+PR 합산, 10-10 2,499에서 1.6배) · MIT ✅ · description **null** ✅(수집기 "설명 비어 있음" 일치) · pushed 2026-11-02T08:48Z · 릴리스 `v0.1.7-nightly.20261102.4066`(11-02 하루에만 nightly 2개)
- 📈 볼트 마지막 기록 ★33,204(10-31) → **+5,964 / 2일**. 수집기 당일 +3,094 · 트렌딩 1위는 트렌딩 페이지 값이라 API로 재현하지 못했다(미검증).
- ✅ 수집기 서술 확인: "agent harness control surface" · iOS/Android/웹/Electron(README 3행) · 기존 구독 사용(5행) · 판매 없음(9행).
- ⚖️ 수집기 누락 ① **지원 대상이 7종이다.** README 5·16·24행에 **fx**가 추가됐다(`fx login`, T3 Code 서버 머신에서). 수집기의 6종 목록은 10-31 시점 기준이다.
- ⚖️ 수집기 누락 ② **원격 노출 모델**(10-31에 🔴 미확인으로 남긴 항목, `docs/user/remote-access.md` 확인):
  - **T3 Connect**: 호스팅 계정 로그인으로 포트 포워딩 없이 다른 기기에서 접속(6~10행). 즉 제3자(T3) 중계 계정이 경로에 들어간다.
  - **LAN 모드** `t3 up --lan` / `t3 serve --lan`: 로컬망과 tailnet 연결을 받으며 문서가 직접 *"a pairing code is all that keeps other devices on them out"* 이라고 쓴다(81~83행). 페어링은 이후 접속까지 영구 인가한다(104행).
  - Linux/macOS에서는 백그라운드 서비스로 상주한다(20행).
- ⚖️ 수집기 누락 ③ 설치는 여전히 `curl -fsSL https://t3.codes/install.sh | sh`(README 29행) · Windows `irm … | iex`(35행). README 100행 *"We are very very early in this project. Expect bugs."*
- 📝 최신 nightly 노트(4066): 모델·effort 변경 이력 표시, Antigravity 서브에이전트 작업 표시, Codex의 T3 MCP 서버 직접 호출 등 기능·버그 수정. 사고 공지는 없다.

> [!warning] 권한 면적
> 로컬에 로그인된 에이전트 7종을 휴대폰에서 원격 구동하는 도구다. LAN 모드에서는 페어링 코드 하나가 경계다. 0.1.x nightly · 이슈+PR 4천 건 · 하루 복수 배포 상태에서 상주 서비스로 띄우는 것은 신중히. 🔴 실제 앱 동작·인증 구현은 볼트가 검증하지 않았다(문서 서술만).

## 🔄 2026-11-03 갱신 (인제스트 2026-11-03) — ★42,780 · **하루 +3,612 · 11-03 나이틀리 2회에 Kiro(beta) 8번째 제공자 · README 목록은 아직 7종**

**GitHub API 실측(11-03 09시대)**: ★**42,780**(수집기 42,773 · +7) · fork **9,150**(수집기 9,149) · open_issues **4,499**(이슈+PR 합산) · MIT ✅ · TypeScript ✅ · description **null** ✅ · pushed 2026-11-03T09:02Z · 릴리스 `v0.1.7-nightly.20261103.4119`(08:49Z) · `…20261103.4106`(02:27Z) · 11-02 nightly 3개(4066·4080·4093)
- 📈 볼트 마지막 기록 ★39,168 · fork 8,975 · open_issues 4,051(11-02) → **★ +3,612 · fork +175 · open_issues +448 / 1일.** 수집기 트렌딩 표시 +3,229와 창이 다르다(재현 불가).
- ✅ **Kiro 주장 확인**: nightly **4106** 하이라이트 *"Kiro (beta). Use Kiro as a provider in T3 Code."* · PR #14693 `feat(provider-kiro): add Kiro as an ACP provider`. 4119에 #28253 `fix(provider-acp): Kiro's html_render pages show in the thread` 후속 수정. ⚠️ 단 **README 5·16행의 지원 목록에는 Kiro가 0건**(grep `kiro` · `api.github.com/repos/pingdotgg/t3code/readme` raw 153행) — 릴리스는 8종, 문서는 7종. 수집기 한줄요약의 7종 나열 + "Kiro(beta) 추가" 서술은 이 상태와 정합.
- ✅ 나머지 수집기 서술 확인: 4119 "Imported Claude sessions — Continue an imported Claude Code conversation on the first follow-up" · "Pi messages during compaction … held and delivered instead of lost" ✅ · 11-03 나이틀리 **2회** ✅ · 설치 `curl | sh`(29행)·`irm | iex`(35행) ✅ · README 100행 "very very early … Expect bugs." 유지 · 🔴 성능 수치 0건 ✅.
- ⚖️ 수집기 누락(보안 인접 항목, 노트 전문 grep `secur|auth|pair|secret|token|root|privacy`):
  - 4119 #27961 *"T3 Connect repairs tunnel ingress that drifted from a matching origin"* — 11-02에 기록한 **T3 Connect 중계 터널**의 ingress가 origin과 어긋나는 버그가 있었다. 사고 서술은 없음.
  - 4119 #23804 *"show why Claude refuses full access as root"* — root로 서버를 돌리는 사용자가 있다는 방증.
  - 4106 #28529 Tailscale serve 명령이 멈추면 SIGKILL로 승격 — LAN/tailnet 노출 경로의 안정성 수정.
  - 보안 공지·사고 공개 항목은 **0건**(두 노트 전문 확인).
- 📝 4106 = 78 changes / 17 contributors, 4119 = 39 changes / 3 contributors — 하루 117개 변경. open_issues 하루 +448과 같은 속도감이다.

> [!insight] 제공자 추가 속도가 문서 갱신 속도를 앞질렀다
> 10-10 6종 → 11-02 7종(fx) → 11-03 8종(Kiro, 릴리스 노트에만). 하루 2회 나이틀리에서 기능이 먼저 나오고 README가 뒤따르는 구조라 **"지원 목록"은 README가 아니라 최신 nightly 노트로 판정**해야 한다. 같은 속도로 원격 노출 경로(T3 Connect 터널·Tailscale serve)도 매일 바뀌므로 11-02의 권한 면적 경고는 강화된다 → [[하네스-설계-축]] · [[메타데이터-부재-추론]](description null 지속).

- **수집기 평가**: Kiro·나이틀리·설치 경고 모두 정확. 누락 = README 미반영 상태 명시 · T3 Connect/Tailscale 관련 수정. 
- 🔗 [[claude-mem]] v15.9.0 #5283 *"T3 Code: default Claude and Codex providers are found even when T3 never saved them"* — 메모리층이 제어면의 미저장 기본값까지 탐색한다(두 도구 결합 경로가 계속 정비 중).
