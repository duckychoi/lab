---
title: thedotmack/claude-mem — Claude Code 세션 간 컨텍스트 지속 플러그인
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, memory, context, session, plugin, llm-coding, workflow, 캐시된지표신선도, 관심검증역상관]
created: 2026-04-13
updated: 2026-11-04
sources: []
reliability: high
---

# thedotmack/claude-mem

> [!insight] 핵심 인사이트
> Claude Code 세션 종료 시 컨텍스트를 AI로 압축·저장하고, 다음 세션 시작 시 주입하는 플러그인. 스타 **60,473개(+1,897 today)**. "세션 간 기억 단절"이 Claude Code 실무 최대 불만 중 하나 — 이를 해결하는 도구가 이 정도 스타를 받는다는 건 **메모리 연속성**이 LLM 코딩의 핵심 UX 문제임을 입증.

## 핵심 인사이트

> [!action] 당장 할 것
> claude-mem 설치 후 실제 개발 세션에서 컨텍스트 연속성 확인. 특히 장기 프로젝트(wiki 시스템 등)에 유용할 수 있음.

> [!note] 배경 정보
> thedotmack 개발. AI 압축을 활용해 중요한 컨텍스트(파일 구조, 진행 상황, 결정 사항)를 요약 → 다음 세션 CLAUDE.md나 시스템 프롬프트에 자동 주입하는 방식으로 추정.

> [!question] 미해결 질문
> 압축 방식은? 어떤 AI를 압축에 사용? 주입 포인트가 CLAUDE.md인가 시스템 프롬프트인가?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — 스타 60,473개, 커뮤니티 대규모 검증
- **즉시 활용**: YES — Claude Code 설치 후 즉시 사용 가능 (플러그인 형태)
- **6개월 영향력**: 세션 간 기억이 해결되면 Claude Code로 수주/수개월 프로젝트 연속 진행 가능
- **대체 관계**: 수동 CLAUDE.md 관리 대체, 메모리 관련 CLAUDE.md 섹션 자동화
- **허와 실**: 압축 품질에 의존 — 중요 컨텍스트가 누락될 수 있음
- **액션**: 설치 후 wiki 작업 세션에 테스트

## 관련 페이지
- [[Claude-Code-워크플로우]]
- [[claude-code-best-practice]]
- [[andrej-karpathy-skills]]
- [[LLM-Wiki]]

## 원본
- 출처: https://github.com/thedotmack/claude-mem
- 신뢰도: ⭐⭐⭐ (볼트 구기록 ★60,473 → **2026-10-06 실측 ★96,801**)

---

## 🔄 2026-10-06 갱신 (인제스트 2026-10-10)

**★96,801** (당일 +534 · **트렌딩 2위**) · fork 8,537 · watchers 308 · **v13.32.0**
**open_issues 86 = 순수이슈 25 + PR 61** · Apache-2.0 · TypeScript · created 2025-08-31 · pushed 2026-10-06

> [!warning] 🔴 볼트 기록이 크게 낡았다 — [[캐시된-지표-신선도]] 의 볼트 내부 버전
> index.md:1609 는 **★60,473** 이고 2026-10-06 실측은 **96,801 = +36,328(+60.1%)** 이다.
> 📌 **외부 필드 동결만 보지 말고 볼트 자기 기록의 나이도 지표다.** 이 페이지는 2026-04-17 이후 **약 6개월 미갱신**이었다.

> [!insight] 갱신된 기능 서술
> 세션 중 에이전트 활동을 캡처해 **AI 로 압축 저장**하고 다음 세션 시작 시 관련 컨텍스트를 자동 주입한다. 훅이 없는 하네스(Grok Bot)에는 **채팅 로그 파일 감시**로, OpenClaw 게이트웨이에는 설치 스크립트로 **각각 다른 경로**를 쓴다.

> [!insight] 🏆🏆 배치 내부 교차 — 같은 날 트렌딩 4위 [[t3code]] 전용 설치 경로를 명시한다
> `npx claude-mem install --ide t3code` · *"T3 Code 의 활성 provider 를 탐색해 각 provider 홈에 네이티브 플러그인 등록"*
> ⇒ ⚖️ **같은 날 트렌딩 두 레포가 서로를 참조한다 = 하네스 생태계가 층으로 쌓이고 있다는 1차 증거**(t3code = 하네스 제어면 · claude-mem = 그 위 메모리층). 금일(10-10) [[knowledge-work-plugins]] 가 3번째 층이다.

> [!warning] 💰 무료가 아니다 — 2026-04 기록에 없던 사실
> 기본값이 **CMEM Pro(호스팅 메모리)** 이고 *"최대 14일 무료"* 후 Anthropic 플랜으로 폴백하거나 구독한다. **로컬 observer 는 opt-in**(`--provider host`).
> ⚠️ **파이프-투-셸 설치 경로 보유**: `curl -fsSL https://install.cmem.ai/openclaw.sh | bash`

> [!warning] 🔴 측정 수치 0개 — ★96,801 에 검증 0
> 메모리 품질·검색 정확도·토큰 절감에 대한 벤치가 README 에 없다. 유일한 정량 표현은 *"up to 100% more usage from your plan"* 이라는 **플랜 소비 관련 마케팅 문구**이고 **능력 측정이 아니다.**
> ⇒ 📌 [[관심-검증-역상관]] 후보(★96,801 · 검증 0).

> [!warning] 🔴🔴 두 방향에서 전제가 압박받는다 — 볼트가 이번 배치에서 얻은 핵심
> ① **[[MemAdapter]](같은 10-06 배치)**: *"올바른 메모리조차 아첨을 유발한다"* 를 측정했다 — 아첨 실패율 80.00 → 53.50 으로 줄이는 도구를 내면서 **claude-mem 의 "주입은 좋다" 전제를 측정 대상으로 만든다.**
> ② **[[Learn2Play]](10-10 배치)**: **행동·피드백 전체 기록 보존이 규칙·전략으로 요약하는 것보다 효과적**이라고 측정했다 — claude-mem 의 **AI 압축** 설계와 **정면 충돌한다.**
> ⇒ ⚖️ **즉 "압축 형태"와 "메모리 신뢰도" 두 축에서 동시에 반대 증거가 도착했다.** ★는 6개월간 +60% 늘었고 **검증은 여전히 0이다.**
> 📌 [[대립레시피-동시도착]] · [[에이전트-메모리-레이어]] **"메모리 신뢰도" 축 신설 후보.**

> [!question] 미해결
> - 압축 품질 측정 **여전히 없음**(2026-04 기록의 *"압축 품질에 의존"* 우려가 6개월 후에도 미해소).
> - CMEM Pro **가격·데이터 보존 정책** 미확인.
> - 로컬 observer 모드의 **기능 동등성** 미확인.
> - PR 61 / 순수이슈 25 = **PR 비중 71%** 의 의미 미확정.

## 관련 페이지 (갱신 추가)
- [[t3code]] — 상호 참조하는 하네스 제어면
- [[MemAdapter]] — 전제를 측정 대상으로 만든 논문
- [[Learn2Play]] — 압축 vs 원본 보존을 측정한 논문
- [[캐시된-지표-신선도]] · [[관심-검증-역상관]] · [[대립레시피-동시도착]]
- [[에이전트-메모리-레이어]] · [[knowledge-work-plugins]]

## 원본 (갱신)
- 수집: 2026-10-06 자동수집 (ai-news) · 인제스트 2026-10-10
- 검증: GitHub API 실측 · `open_issues` 분해 86=25+61 검산 통과 · README i18n **26개 언어 이상**(한국어 `docs/i18n/README.ko.md`) — 10-04 [[ECC]] 14개 언어를 넘는다
- 신뢰도: ⭐⭐⭐ (★96,801 · **능력 측정 0**)

## 🔄 2026-10-31 갱신 (인제스트 2026-10-31) — ★106,828 · 🔴 **릴리스 노트가 밝힌 사고: 숨은 `codex exec` 약 230회 · "10배 절감"의 정체**

**GitHub API 실측(10-31)**: ★**106,828**(수집기 106,816 · +12) · fork 9,396 · Apache-2.0 ✅ · pushed 2026-10-31T08:56Z · 최신 릴리스 **v15.7.0(10-30)** · v15.6.0(10-29)
- 📈 볼트 마지막 기록 ★96,801(10-10 페이지) → +10,027. 릴리스가 매일 나오는 상태.

> [!warning] 🔴 수집기 요약에 없는 사고 (v15.7.0 릴리스 노트 원문)
> My Work 자동 새로고침에서 Claude Code 응답을 거부하면 로그인된 **다음 에이전트로 넘어갔고**, Codex가 깔린 기기에서는 *"hidden `codex exec --ephemeral` runs on the owner's ChatGPT account, even with `CLAUDE_MEM_PROVIDER=claude`"* 가 발생했다(#5189: **4일에 약 230회**). 사용자가 지정한 공급자 설정을 넘어 **다른 계정의 구독을 소모**한 사례다. v15.7.0에서 현재 에이전트에 머물도록 고쳤다. ⇒ **v15.7.0 미만이면 올린다.** 수집기의 "백그라운드 워커 상시 운용" 경고는 맞지만 위험의 실체는 이쪽이다.

> [!insight] "약 10배 토큰 절감"은 측정값이 아니라 설계 비율이다
> README 287·289·296행: 검색 색인 **~50-100 토큰/결과** vs 상세 조회 **~500-1,000 토큰/결과** → *"~10x token savings by filtering before fetching details"*. 즉 **결과 하나당 크기 비율**이고, 실사용 세션 전체의 절감을 잰 값이 아니다. 수집기가 "상세 조회 전 필터링 기준의 자체 수치"로 적은 것은 ✅ 정확하다. 볼트의 "능력 측정 0" 판정은 유지 → [[스타-근거-비동행]].

- ✅ 수집기 서술 확인: SQLite FTS5(255행) · Chroma 하이브리드(256·275행) · MCP 도구 4종(283행) · 워커 서비스(254·272행). 🆕 [[t3code]] 에 네이티브 플러그인 등록 지원(171행) · npm 전역 설치는 SDK만 깔고 훅을 등록하지 않음(204행 주의).

## 🔄 2026-11-02 갱신 (인제스트 2026-11-02) — ★110,000 · 🔴 **설치 직후 최근 30일 프롬프트를 cmem.ai에 무동의 업로드(v15.2.0~v15.8.2) — v15.8.3에서 수정, 이미 올라간 것은 안 지워짐**

**GitHub API 실측(11-02 09시대)**: ★**110,000**(수집기 109,992 · +8 드리프트) · fork 9,602 · Apache-2.0 ✅ · pushed 2026-11-02T08:57Z · 최신 릴리스 **v15.8.3(11-02 06:26Z)** · v15.8.2(11-02) · v15.8.1(11-01) · v15.8.0(11-01)
- 📈 볼트 마지막 기록 ★106,828(10-31) → **+3,172 / 2일**.
- ✅ 수집기 서술 확인: 캡처→AI 압축→주입(저장소 description) · SQLite(README 251·269행) · Chroma 하이브리드 검색(252·271행). 지원 목록은 description 기준 **Claude Code · OpenClaw · Codex · Gemini · Hermes · Copilot · OpenCode + More** — 수집기 5종 목록은 OpenClaw·Hermes를 뺐다. README 설치 절에는 Grok Bot(136)·T3 Code(164)·Antigravity(172)·OMP(178)·Pi/DeepSeek Harness(184~185)도 있다.

> [!warning] 🔴 수집기 요약에 없는 프라이버시 사고 (v15.8.3 릴리스 노트 · issue #5176)
> v15.2.0(2026-10-25)에서 도입된 브라우저 설치 흐름(#5031)이 로컬 에이전트 기록을 스캔한 뒤 **최근 30일 프롬프트 전문을 세션 ID·프로젝트명·폴더 경로·타임스탬프와 함께 cmem.ai로 묻지 않고 업로드**했다. 이슈 #5176 제목: *"Installing claude-mem uploads your last 30 days of prompts to cmem.ai, no opt-in"*(10-29 등록, API 조회 시점 **open**).
> - v15.8.3(#5220): 스캔 후 멈추고 동의 패널을 띄운다. 도구별 체크한 것만 업로드, "Keep everything local" 선택 시 0건. 분석(analytics) 체크박스는 별도이며 기본 off.
> - 릴리스 노트가 스스로 밝힌 한계: **이전 버전이 이미 올린 프롬프트는 이 업데이트로 삭제되지 않는다.** cmem.ai 서버 측 처리와 개인정보 정책 문구는 이 변경 범위 밖이다.
> - 노출 범위 추정: v15.2.0 노트는 이 흐름이 **신규 설치**에서 열린다고 적는다(기존 설치는 My Work를 그대로 연다). 즉 10-25~11-02 사이 새로 `npx claude-mem install` 한 사용자가 대상이다 — 기존 설치 사용자의 노출 여부는 🔴 미확인.
> ⇒ 10-31 갱신의 숨은 `codex exec` 사고에 이어 **일주일 안에 두 번째 "사용자 동의 범위 밖" 사고**다.

- ⚖️ 수집기 누락 ② **호스팅 쪽으로 기울고 있다.** 설치기가 브라우저 로그인(이메일 매직링크)으로 **claude-mem observer 30일 무료 체험**을 열고, 체험 종료 후에는 Anthropic 플랜으로 되돌아간다(README 149행). Grok Bot 경로는 기본값이 **CMEM Pro(호스팅 메모리)**, 로컬 observer는 옵트인(139행). 로그인 회피: `--provider` 지정 또는 `CLAUDE_MEM_ONLINE_OPTIN=false`(151행).
- ⚖️ 수집기 누락 ③ **텔레메트리 존재.** v15.8.2가 "telemetry volume cuts"(설치당 일별 롤업 이벤트)로 이벤트 양을 줄였다 — 텔레메트리 자체를 끄는 방법은 README에서 확인하지 못했다(🔴 미확인).
- ⚖️ 수집기 누락 ④ OpenClaw 경로는 `curl -fsSL https://install.cmem.ai/openclaw.sh | bash`(README 207행) 파이프 설치다.
- 📌 볼트 환경: `~/.claude-mem` 및 플러그인 설치 흔적은 이 머신에서 발견되지 않았다(11-02 확인) — 직접 노출 없음.

> [!action] 당장 할 것
> 도입 검토를 다시 한다면 **v15.8.3 이상 + `--provider` 지정(또는 `CLAUDE_MEM_ONLINE_OPTIN=false`)** 으로만 설치. 10-25 이후 이미 설치했다면 cmem.ai에 업로드된 데이터 삭제 요청 경로를 먼저 확인(🔴 릴리스 노트에 삭제 절차 없음). ★11만은 신뢰 근거가 아니다 → [[스타-근거-비동행]].

## 🔄 2026-11-03 갱신 (인제스트 2026-11-03) — ★111,159 · 🔴 **#5176 재오픈 상태 · 업로드된 프롬프트는 cmem.ai→OpenRouter→DeepSeek로 전달(ZDR 미설정) · v15.9.0은 localhost 쓰기 차단 등 보안 수정**

**GitHub API 실측(11-03 09시대)**: ★**111,159**(수집기 111,157 · +2) · fork **9,688**(수집기 9,687) · open_issues **135** · Apache-2.0 ✅ · pushed 2026-11-03T03:52Z · 최신 릴리스 **v15.9.0(11-02 18:03Z)** · v15.8.3(11-02 06:26Z) · v15.8.2 · v15.8.1 · v15.8.0
- 📈 볼트 마지막 기록 ★110,000 · fork 9,602(11-02) → **★ +1,159 · fork +86 / 1일**.

> [!warning] 🔴 수집기 오류 — "기존 업로드분 처리 여부는 릴리스 노트에 없음(미확인)" 은 틀렸다
> v15.8.3 노트 원문 **"Not covered by this release — Prompts already uploaded by earlier versions are not removed by this update. Server-side handling at cmem.ai and privacy-policy wording are outside this change."** 릴리스 노트에 **명시돼 있다**(삭제하지 않는다고). 볼트 11-02 갱신은 이미 이 문장을 인용했다 — 수집기가 볼트보다 하루 뒤처진 판정을 냈다.

- ✅ 수집기 서술 확인: v15.8.3 "Privacy fix" — v15.2.0부터 브라우저 셋업이 **최근 30일 프롬프트 전문 + 세션ID·프로젝트명·폴더경로·타임스탬프**를 묻지 않고 업로드, 이제 스캔 후 동의 패널에서 체크한 도구만 전송 · "Keep everything local" = 0건 · analytics 별도·기본 off · 신규 `POST /api/setup/scan/consent`(loopback 전용·origin 가드). v15.9.0 Devin CLI/Desktop 지원(#5172·#5276) · 원격 워커 `CLAUDE_MEM_WORKER_URL`(비로컬은 https 강제, #5285) ✅.
- 📌 **이슈/PR 상태(API 실측)**:
  - **#5176(issue) = `open` · state_reason `reopened`** — 10-29 등록, 11-02 06:12:21Z 메인테이너가 close 후 **9초 뒤 06:12:30Z 직접 reopen**. 즉 "수정됨"이 아니라 **미해결로 남겨 둔 상태**다.
  - **#5220(PR) = closed · merged 2026-11-02T06:12:18Z** — 수정 본체.
- ⚖️ **수집기·볼트 모두 누락 ① — 업로드된 데이터의 행선지(#5176 본문, 보고자가 cmem.ai 회신으로 확인했다고 서술)**:
  - cmem.ai가 프롬프트를 **`deepseek/deepseek-v4-flash-0731` 로 OpenRouter 글로벌 엔드포인트**에 보냈고(최저가 공급자 우선 라우팅), 요청에 **zero data retention도 `data_collection: "deny"` 도 설정하지 않았다.** cmem.ai는 어느 공급자가 받았는지 기록이 없다고 했다.
  - cmem.ai는 요청 시 **자사 DB 레코드는 삭제**했으나 **OpenRouter·하위 공급자 사본은 범위 밖**.
  - 개인정보처리방침 *"Nothing leaves your device unless you explicitly turn on cloud sync"* 와 충돌한다고 보고자가 지적. 10-30 댓글: 계정 수준 OpenRouter 설정(학습 opt-out·로깅·ZDR) 확인 중.
  - ⚠️ 이는 **이슈 작성자의 서술**이며 볼트가 cmem.ai·OpenRouter 측을 독립 검증하지 않았다.
  - 노출 경로: Claude Code `~/.claude/projects/*/*.jsonl`(서브에이전트 포함) · Codex `~/.codex/sessions/…` · Gemini CLI · Antigravity · OpenCode DB(이슈 표). 설치기에서 고른 도구와 무관하게 읽었다고 서술.
- ⚖️ 누락 ② **#5255(open, 11-01)**: 호스팅 셋업이 HTTP 503 "daily budget for anonymous hosted setup"으로 실패해도 **프롬프트 본문은 이미 `POST /api/pro/intent` 로 나간 뒤**라는 보고(로그상 6분에 3회 재시도). v15.8.3 이전 동작 기준 — 실패 = 미전송이 아니었다.
- ⚖️ 누락 ③ **v15.9.0 "Privacy and security" 절(수집기는 Devin·원격워커만 언급)**:
  - **#5200**: localhost의 **다른 웹사이트가 worker의 work-state·dedup·corpus·advisor 라우트로 쓰기 요청을 보낼 수 있었다** → 외부 origin 차단(11-02 merged). 브라우저 경유 로컬 서비스 공격면이 실재했다는 뜻.
  - **#5272**: 오류 보고를 꺼도 **디스크에 저장된 오류는 전송되던** 문제 수정 — 11-02 볼트의 "텔레메트리 끄는 법 미확인"에 대한 부분 답(오류 보고 opt-out 존재, 이전엔 완전히 지켜지지 않음).
  - 비밀값 마스킹 확대(Slack/Discord webhook·Stripe·PyPI·GitLab 토큰·`--auth-token` 등) · Kimi 설정 백업 권한 축소(#5290).
  - 기존 업로드분 삭제·통지에 관한 문장은 **v15.9.0 노트에 0건**(전문 확인).
- 📝 README(raw 461행): `CLAUDE_MEM_ONLINE_OPTIN=false` 로그인 회피(151행) 유지 · Devin은 README에 아직 0건(grep `devin`).

> [!insight] 일주일에 세 번째 "동의 범위 밖" 사고 축이 열렸다
> 10-31 숨은 `codex exec`(타 계정 구독 소모) → 11-02 무동의 프롬프트 업로드 → 11-03 확인된 **localhost 교차 origin 쓰기 허용(#5200)**. 앞의 둘은 "도구가 사용자 몰래 밖으로 보냄", 셋째는 "밖에서 도구로 들어옴"이다. 수정 속도는 빠르지만(모두 1~4일 내 패치) **수정 = 피해 회복이 아니다** — 업로드분은 제3자 LLM 경로까지 퍼졌고 삭제 경로는 cmem.ai DB에 한정된다. ★11만·하루 +1천은 이 신호와 무관하게 오른다 → [[스타-근거-비동행]] · [[관심-검증-역상관]] · [[에이전트-메모리-레이어]] "메모리 신뢰도" 축.

- **수집기 평가**: 사고 포착은 정확하고 전일 볼트 지적을 반영했다. 그러나 ① 삭제 여부를 "릴리스 노트에 없음"으로 잘못 적었고 ② #5176이 재오픈 상태라는 점 ③ OpenRouter/DeepSeek 2차 전달 ④ v15.9.0 보안 절을 놓쳤다.
- **실용성**: 볼트 머신 미설치(11-02 확인) 유지. 도입 재검토 조건에 **v15.9.0 이상**(localhost 쓰기 차단) 추가.

## 🔄 2026-11-04 갱신 (인제스트 2026-11-04) — ★112,311 · 🔴 **동의 패널 고친 지 14시간 만에 "건너뛰기"를 작은 텍스트 링크로 낮췄다(#5270, 미릴리스 main) · #5176 여전히 reopened·무응답**

**GitHub API 실측(11-04 09시대)**: ★**112,311**(수집기 112,309 · +2) · fork **9,764** · open_issues **133** · Apache-2.0 ✅ · 소유 `thedotmack`(User) · pushed 2026-11-04T08:19Z · 최신 릴리스 **여전히 v15.9.0(11-02 18:03Z)** — v15.9.0 이후 새 릴리스 **0건**(`/releases?per_page=5` 상위 = v15.9.0·15.8.3·15.8.2·15.8.1·15.8.0). main은 v15.9.0보다 **38커밋 앞**(`/compare/v15.9.0...main`).
- 📈 볼트 직전 ★111,159 · fork 9,688(11-03) → **★ +1,152 · fork +76 · 릴리스 +0 / 1일.** 수집기 "트렌딩 +1,139 today"와 같은 크기.
- 🔒 공개 보안 권고(GHSA) **0건**(`/security-advisories` 빈 배열) — 업로드 사고는 권고가 아니라 릴리스 노트·이슈로만 공개됐다.

> [!warning] 🔴 수집기·볼트 모두 누락 — 동의 화면이 "업로드 쪽"으로 다시 기울었다 (PR #5270, 11-02 20:37Z merged, 작성자 thedotmack)
> v15.8.3(06:26Z)이 무동의 업로드를 막으려 넣은 동의 패널을 **같은 날 밤 재설계**했다. PR 본문(+Cursor Bugbot 요약) 원문 기준:
> - 기존 **대등한 두 버튼 "Keep everything local" / 업로드** → 전폭 주 버튼 **"Discover My Work, Rules & Focus"** + 그 아래 밑줄 텍스트 **"Skip this step"**.
> - **30일 범위·전문(full-text) 설명·메타데이터 목록**을 접힌 "What gets uploaded?" 상세로 이동. 화면에 남는 건 "선택한 메시지가 cmem.ai와 AI 공급자로 간다"는 짧은 고지.
> - 용어 **prompts → messages**, 단계 제목 "Pick up where you left off".
> - PR 스스로 *"copy and presentation change; it makes no new data-retention promises"* — 도구별 체크박스·명시 동의·analytics 별도는 유지.
> - v15.9.0(18:03Z) **이후** 머지라 아직 릴리스에 없다 → 다음 릴리스부터 사용자에게 간다.
> ⇒ 기능적 동의 장치는 그대로지만, **선택지의 시각적 무게를 비대칭으로 바꾼 것**이 사고 수습 하루 안에 일어났다. 볼트는 이를 "동의 범위 밖" 축의 네 번째 사건이 아니라 **"동의는 있으나 기본 경로를 업로드로 유도"** 하는 별도 유형으로 기록한다(⚖️ 해석, 사용자 전환율 데이터 없음).

- 📌 **#5176 상태(API 실측)**: `open` · state_reason `reopened` · updated_at **2026-11-02T06:12:30Z 그대로**(11-03 이후 갱신·댓글 0) · 댓글 총 2건. → 메인테이너 측 공개 답변·삭제 절차 공지 **여전히 없음**.
  - ⚖️ 볼트 11-03 누락: 댓글 2(webpony2016, 11-01) — v15.7.0 커밋 70aa400 소스 리뷰로 *"CMEM 계정 없이도 업로드가 진행되고 `improveProduct=false` 로도 막히지 않는다"* (`src/services/work-view/hosted-intent.ts` L137-174 지목). ⚠️ 작성자 스스로 "소스 수준 발견, 내 기기 업로드 캡처 아님"이라 적음 — 볼트 미검증.
- 📌 **#5255(503 실패해도 프롬프트는 이미 전송)** = 여전히 `open`, 메인테이너 응답 없음(본문은 15.8.0 기준).
- 📌 **업로드분 처리**: v15.9.0 노트·main 커밋 메시지(38개 중 privacy/consent/upload 키워드 grep) 어디에도 **기존 업로드분 삭제·통지 문장 0건**. v15.8.3의 "not removed" 가 현재까지 유일한 공식 문장.
- 🆕 미릴리스 main 수정: **#5348**(11-04 03:03Z merged) — observer가 `CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS` 옵트아웃을 **환경 정리 과정에서 떨궈** 사용자가 끈 베타가 백그라운드 observer에선 꺼지지 않던 문제(#5346, 11-02 Anthropic Messages API threads 공지 관련). 사용자 설정이 백그라운드 프로세스에 전파되지 않은 **같은 모양의 결함 세 번째**(10-31 `CLAUDE_MEM_PROVIDER=claude` 무시(#5189) → 11-03 오류보고 꺼도 디스크 오류 전송(#5272) → 11-04 베타 옵트아웃 미전파(#5348)). 리댁션 확대 PR 다수(Groq·xAI·NVIDIA NIM·Google OAuth `ya29.`·Linear·Notion·Supabase·Sentry). **#5353 "capture disable setting"** 은 아직 open PR — 즉 캡처 자체를 끄는 설정은 현재 없다(PR 제목 기준 추정).
- 📝 README(raw 464행): `CLAUDE_MEM_ONLINE_OPTIN=false`(151행) 유지 · 스크린샷 업로드는 opt-in·Cloud Sync 시에만(221행) · Devin은 README **0건**(grep `devin`) — 수집기 "Devin 지원"은 v15.9.0 노트 기준으로만 참.

> [!insight] 고친 것을 하루 만에 다시 기울였다 — "수정 = 방향 전환"이 아니다
> 11-02 아침 무동의 업로드를 동의제로 바꾸고, 같은 날 밤 **동의 화면의 기본 경로를 업로드로** 되돌렸다. 체크박스는 남았으니 규칙 위반은 아니지만, **제품 인센티브(호스팅 전환)는 사고 전과 같은 쪽을 가리킨다.** 볼트가 이 레포를 판정할 때 릴리스 노트("Privacy fix")만 읽으면 놓친다 — 다음 릴리스 노트에 #5270이 어떻게 서술되는지가 관찰 포인트. → [[스타-근거-비동행]] · [[에이전트-메모리-레이어]] "메모리 신뢰도" 축.

- **수집기 평가**: v15.8.3 "not removed" 인용·v15.9.0 요약 정확(전일 오류 수정됨). 누락 = ① 새 릴리스 0건이라는 사실(요약이 v15.9.0을 신규처럼 서술) ② #5176 무응답 지속 ③ **#5270 동의 화면 재설계** ④ #5348 옵트아웃 전파 결함 ⑤ "설치 전 동의 패널 확인 필수" 권고가 곧 바뀔 패널을 전제로 함.
- **실용성**: 볼트 머신 미설치 유지. 도입 재검토 조건 유지(v15.9.0+·`--provider`/`CLAUDE_MEM_ONLINE_OPTIN=false`) + **다음 릴리스부터는 설치 화면에서 "Skip this step" 텍스트 링크를 찾아야 한다.**
