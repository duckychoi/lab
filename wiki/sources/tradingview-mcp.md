---
title: "tradingview-mcp — Claude Code를 TradingView 데스크톱에 CDP로 붙이는 MCP. 도구는 78개가 아니라 84개이고, 열린 PR이 195건 쌓여 있다"
type: source
domain: ai-news
tags: [ai-news, github-trending, mcp, tool, finance-ai, trading, pine-script, cdp, electron, context-management, maintenance-risk]
created: 2026-09-19
updated: 2026-09-19
sources: [instagram-저장-2026-02-2026-04.md]
reliability: medium
---

# tradingview-mcp (tradesdontlie/tradingview-mcp)

> [!insight] 핵심 인사이트 — **"공식 API가 없는 데스크톱 앱을 에이전트에게 열어주는" 일반 패턴의 교과서다. 그리고 그 패턴의 대가를 저자가 스스로 전부 적었다**
> 구조: `Claude Code ←→ MCP 서버(stdio) ←→ CDP(localhost:9222) ←→ TradingView Desktop(Electron)`. TradingView 서버에 붙지 않고, **사용자가 `--remote-debugging-port=9222` 로 직접 연 로컬 앱의 디버그 인터페이스**만 쓴다. 실거래 실행은 하지 않는다(*"chart interaction only"*).
> 🎯 **이 패턴은 TradingView에 국한되지 않는다** — VS Code·Slack·Discord 등 모든 Electron 앱이 같은 CDP 포트를 가진다(README가 직접 예로 듦). **"API 없는 GUI 앱 → MCP 도구화"의 재사용 가능한 설계도**다.
> 🔴 **대가 4개를 저자가 README 최상단과 Disclaimer에 적었다** — 수집기가 전부 옮겼고 ✅ 원문 대조 일치: ① **유료 구독 필수**(실시간 데이터) ② *"accesses **undocumented internal** TradingView APIs … can change or break **without notice**"* — *"Pin your TradingView Desktop version"* 권고 ③ TradingView 약관이 자동 수집·비표시(non-display) 사용을 제한하며 이 도구가 *"**may conflict** with those terms"* · 계정 정지 등 결과는 사용자 부담 ④ TradingView와 **무관**(비공식). 추가로 Disclaimer 4항이 **"자동매매·알고리즘 의사결정에 추출 데이터 사용 금지"** 를 명시한다.
> → [[자기제한-명시]] 의 **양성 사례**. 단 🔴 **자기제한을 명시했다고 위험이 줄지는 않는다** — 명시는 책임 이전이다.

> [!warning] 🔴 정정 1 — **도구는 78개가 아니라 84개다**
> - 볼트가 `src/tools/*.js` 14개 파일의 `server.tool(` 등록 호출을 셌다: alerts 3 · batch 1 · capture 1 · chart 10 · data 12 · drawing 5 · health 5 · indicators 4 · pane 4 · pine 12 · replay 6 · tab 5 · ui 12 · watchlist 4 = **84**.
> - README 안에서도 불일치: 섹션 제목 *"Tool Reference (**78** MCP tools)"* vs 같은 README Architecture 절 *"MCP over stdio (**84** tools)"* · `RESEARCH.md` 도 *"84 granular tools"*.
> - 🎯 원인 추적: 2026-07-21 커밋 *"docs: **reconcile tool count to 84** across all docs"* 가 있었는데 **섹션 제목 하나를 놓쳤다.** 수집기는 그 제목을 옮겼다.
> - 🔴 **CLI는 "동일"하지 않다**: README 원문 *"CLI (`tv` command, **30 commands with 66 subcommands**)"* — MCP 도구와 1:1이 아니다(수집기 "동일 `tv` CLI" 표현 정정).
> → [[측정도구-먼저-반증]]: **문서 안의 개수는 코드로 세기 전까지 주장이다.**

> [!warning] 🔴 정정 2 — 유지보수 신호의 실체: **open_issues 256 중 195건이 열린 PR이다**
> ```
> 볼트 실측 (2026-09-19, GitHub search API)
>   open_issues_count  256  = 열린 이슈 61 + 열린 PR 195
>   pushed_at          2026-07-28T17:28:37Z  ✅ (수집기 일치)
>   forks_count        2,719  / stars 6,540 = 41.6%
> 최근 커밋 (commits API)
>   2026-07-28  Merge #403  "Add MCP Toplist rank badge"   ← 마지막 push = 배지 추가
>   2026-07-21  Merge #377  "reconcile tool count to 84"
>   2026-07-06  Merge #335  "Add tv_update tool"
> ```
> 🎯 수집기의 *"7주 무변경"* ✅ — 볼트가 **왜 문제인지**를 수치로 보강한다: **기여자들이 PR을 195건 보냈는데 7주째 병합이 없다.** 마지막 push조차 기능이 아니라 **배지**다. 그리고 **포크/스타 41.6%** 는 이 배치 4개 레포 중 압도적 최고(agent-lightning 8.8% · gitdiagram 7.6% · marin 8.0%) — 🔴 (추정) **사용자가 업스트림 대신 자기 포크에서 고쳐 쓰고 있을 가능성.** 내부 API 의존 도구에서 TradingView 앱 업데이트가 오면 **수정은 업스트림이 아니라 195개 PR·2,719개 포크 어딘가에** 흩어진다.
> → open_issues 비율 3.91%는 **대부분 PR 적체**다. 같은 필드가 [[marin]] 에선 실험 장부를, 여기선 병합 병목을 잰다 → [[측정도구-먼저-반증]]

> [!note] 📌 라이선스 재확인 — **두 표기 모두 사실이고, 원인은 LICENSE 파일의 덧붙인 문단이다**
> - GitHub API `license.spdx_id`: **`NOASSERTION`** (`key: other`)
> - `LICENSE` 파일 원문: **MIT 전문 + 그 뒤에 `ADDITIONAL NOTICE:` 문단**(TradingView와 무관 · 약관 준수는 사용자 책임 · 라이선스는 이 소스코드에만 적용) · README도 *"MIT"* + 같은 취지 단서
> - 🎯 (추정) GitHub의 라이선스 자동 판별기가 **MIT 표준문에 추가 문단이 붙은 파일을 MIT로 일치시키지 못해** NOASSERTION을 돌려준 것. **코드에 대한 권리는 MIT와 실질 동일**하게 읽히나, 🔴 **API 필드만 보는 자동 필터(라이선스 = MIT인 것만 채택 등)에서는 탈락한다.** → [[메타데이터-부재-추론]]: 필드의 "판별 불가"를 "라이선스 없음"으로 읽으면 안 된다.

## 도메인별 추출 (ai-news)

- **신뢰도**: GitHub **★6,540** · 포크 2,719 · 2026-03-29 생성(약 6개월) · 개인 계정 · 평가 체계 **없음** — 저자 스스로 `RESEARCH.md` 한계 절에 *"**No formal evaluation framework** — findings are observational"*. → reliability **medium**(★·포크 높음, 🔴 유지보수 병목 + 비공식 내부 API 의존).
- **즉시 활용**: **조건부 NO.** 유료 TradingView 구독 + 데스크톱 앱이 없으면 쓸 수 없고, 나는 트레이딩 워크플로가 없다. 🎯 **패턴으로는 YES** — "Electron 앱 + CDP + MCP" 설계와 **컨텍스트 절감 기법**(아래)은 다른 GUI 앱 자동화에 그대로 옮길 수 있다.
- **6개월 영향력**: **낮음(이 레포)** · **중간(패턴)**. 레포 자체는 앱 업데이트 한 번에 깨질 수 있고 병합이 멈췄다.
- **대체 관계**: 볼트의 [[금융-AI]] 계열과 달리 **예측·매매 모델이 아니라 인터페이스 층**이다(*"This is not a trading bot"*). 볼트 [[After-Effects-MCP]] 와 **같은 부류**(데스크톱 전문 앱을 MCP로 여는 것).
- **허와 실**: 🔴 **"~5-10KB instead of ~80KB"** 는 저자 관찰이며 측정 조건 미기재(수집기 ✅). `RESEARCH.md` 가 근거 수치를 더 준다: **Pine 스크립트 원본 200KB+ · OHLCV 500봉 ≈ 40KB** · 도구별 페이로드(`data_get_ohlcv` 요약 500B / 100봉 8KB). 🔴 *"**Tool Count Does Not Confuse the Agent** … Claude consistently selects the right tools"* — **도구 84개가 선택 오류를 일으키지 않는다는 주장에 측정이 없다.** 저자는 해법을 "도구 수 축소"가 아니라 **서술적 도구 이름 + MCP 서버 instructions + 레포 `CLAUDE.md` 결정 트리**로 제시한다.
- **액션**: star/설치 불필요. 🎯 **`src/tools/_format.js` 와 `data_get_ohlcv` 의 `summary: true` 구현을 읽는다** — "기본값은 압축, 상세는 opt-in"을 도구 설계 수준에서 구현한 예시다.

### 저자가 발견했다고 적은 것 (RESEARCH.md "Findings So Far", 전부 관찰 수준)
1. **컨텍스트 관리가 1차 제약** — 모든 도구의 **압축 출력 기본값**이 가장 영향이 큰 설계 결정. → [[하네스-설계-축]] 의 SoL-Pi·Harness-Design-Empirical 결론(*컨텍스트 관리가 가장 중요*)과 **같은 방향의 도구 층 사례**. 🔴 단 이쪽은 **대조 실험 없음**.
2. 도구 수는 에이전트를 혼란시키지 않는다(위 🔴).
3. **Pine Script 개발이 가장 강한 사용처** — `pine_set_source → pine_smart_compile → pine_get_errors` 컴파일-오류-수정 루프.
4. **스트리밍은 에이전트용이 아니다** — 데이터가 에이전트 응답보다 빨리 바뀌면 추론이 낡는다 → 스트리밍은 **사람 대시보드용**으로 돌렸다. 🎯 **요청–응답형 LLM의 실시간 한계를 저자가 설계로 인정한 사례.**
- 🔴 휴먼인더루프 미결: *"all chart mutations … are executed **immediately**"* — 심볼 변경·지표 추가·드로잉에 **사용자 확인 단계가 없다**(저자가 열린 질문으로 명시).

> [!warning] 🔴 보안 관점 — 볼트 추가 관찰
> - **`tv_update` 도구**: *"git fast-forward of origin/main + npm ci"* 로 **MCP 서버가 자기 코드를 스스로 업데이트**한다(비-git 설치·dirty 트리·비-main 브랜치·분기 이력에선 거부하도록 설계). 🎯 **에이전트가 호출 가능한 도구로 공급망 갱신이 열려 있다** — 업스트림 main에 들어간 것이 에이전트 호출 한 번으로 로컬에서 실행된다.
> - **CDP 디버그 포트**: 저자는 "사용자가 명시적으로 열어야 한다"를 안전 근거로 든다. (일반 지식, 이 레포에서 검증 안 함) CDP 포트가 열리면 **같은 머신의 다른 로컬 프로세스도 그 앱을 제어**할 수 있다 — README는 이 점을 다루지 않는다.

> [!action] 당장 할 것
> **볼트의 기존 기록 "거래 분석 | Claude + TradingView MCP | 참고용"([[instagram-저장-2026-02-2026-04]] post 39 · ai-news 도메인 표)이 이 레포를 가리키는지 확인하고, 맞으면 그 행에 [[tradingview-mcp]] 링크와 "🔴 PR 195건 적체 · 7주 무병합(2026-09-19)" 상태를 붙인다.** 🎯 볼트는 이 도구를 **이미 한 번 봤다** — 수집기 보고에는 그 사실이 없다(볼트 0히트 판정 대상이 아니었음).

> [!question] 미해결 질문
> - 07-28 이후 **TradingView Desktop 업데이트가 있었고 그로 인해 깨진 도구가 있는가?** 열린 이슈 61건의 내용은 미열람.
> - 열린 PR 195건 중 **내부 API 변경 대응 수정**이 몇 건인가? — 그 수가 "업스트림 방치 비용"의 직접 지표다.
> - "도구 84개가 혼란을 주지 않는다"를 **다른 모델(비-Claude)** 에서도 관측했는가? *"Agent performance varies significantly by model"* 는 한계 절에 있다.

## 관련 페이지
- [[금융-AI]]
- [[After-Effects-MCP]]
- [[instagram-저장-2026-02-2026-04]]
- [[하네스-설계-축]]
- [[SoL-Pi]]
- [[Harness-Design-Empirical]]
- [[Claude-Code-워크플로우]]
- [[자기제한-명시]]
- [[측정도구-먼저-반증]]
- [[메타데이터-부재-추론]]
- [[marin]]
- [[Electron-CDP-브리지]] *(신설 제안)*

## 원본
- 출처: https://github.com/tradesdontlie/tradingview-mcp · `README.md`(396행) · `RESEARCH.md`(83행) · `LICENSE` · `src/tools/*.js`(14개 파일)
- 볼트 실측(2026-09-19, GitHub API): `stargazers_count` **6,540** ✅ · `forks_count` **2,719** · `open_issues_count` **256** ✅ = 이슈 61 + PR **195** · `created_at` 2026-03-29 ✅ · `pushed_at` **2026-07-28T17:28:37Z** ✅ · `license.spdx_id` **NOASSERTION** ✅ (LICENSE 파일 = MIT + ADDITIONAL NOTICE) · 트렌딩 전체 데일리 `79 stars today` ✅
- 수집기 대조: 9222 포트 ✅ · 실거래 미실행 ✅ · 5~10KB vs 80KB ✅ · 저자 명시 위험 4개 ✅ · 7주 무변경 ✅ · README 396행 ✅ · 🔴 도구 **78 → 84**(코드 계수) · 🔴 "동일 CLI" → **30 명령 / 66 하위명령** · 🔴 open_issues 대부분이 **PR(195/256)**
- 볼트 추가: LICENSE NOASSERTION 원인 · 포크비 41.6% · 마지막 push가 배지 커밋 · `tv_update` 자기갱신 도구 · RESEARCH.md 발견 4개와 한계 · 볼트 기존 언급(instagram post 39) 발견
- 신뢰도: ⭐⭐ (★·포크 높음 · 저자 위험 공시 성실 · 🔴 평가 없음 · 비공식 내부 API · 병합 정지)
