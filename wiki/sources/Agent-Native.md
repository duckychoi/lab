---
title: "Agent-Native — 에이전트가 UI를 클릭하지 않고 UI와 같은 액션층을 부른다 (라이선스는 레포 단위로 불명확)"
type: source
domain: ai-news
tags: [ai-news, github-trending, typescript, framework, agent, mcp, a2a, react, builderio, 라이선스-불일치]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# Agent-Native (BuilderIO)

> [!insight] 🎯 핵심 인사이트: "에이전트가 앱을 어떻게 쓰나"에 대한 설계 시점의 답
> README 40행: *"The agent **does not click through the UI**. It works through the same action layer as the UI."*
> `defineAction`(zod 스키마) 하나를 정의하면, 에이전트에게는 tool로, React에게는 `useActionQuery` 로, 외부에는 HTTP·MCP·A2A·CLI로 노출된다(README 50·63행). 검증·권한·구현이 **한 벌**이다.
> 📌 **같은 배치의 [[browser-harness]] 와 정반대다.** harness는 API가 없는 기존 웹을 **사후에** CDP로 뚫는다. Agent-Native는 **처음부터** 에이전트 경로를 UI와 같은 급으로 만든다. [[Electron-CDP-브리지]] 까지 합치면 볼트에 세 가지 노선이 있다. **API가 없으면 화면(CDP)을 뚫고, 앱을 새로 만든다면 액션층을 공유한다.**
> 🎯 셋째 축인 *"shared application state"*(38행, 현재 페이지·선택 레코드·활성 뷰를 에이전트 컨텍스트로 전달)가 있어서 **화면 캡처 없이 "지금 사용자가 보는 것"을 에이전트가 안다.** CDP 노선은 이것을 스크린샷이나 DOM으로 복원해야 한다.

> [!warning] 🔴 라이선스: 수집기 지적은 맞다. 볼트가 한 층 더 찾았다
> 수집기 raw: *"라이선스 3곳 불일치 — API `null` · README MIT · 루트 `package.json` ISC(`private: true`) · `@agent-native/core` MIT(v0.182.1)"*
> ✅ **4개 항목 전부 재현했다**(2026-09-22):
> - GitHub API `license: null`. 루트 contents 38개 항목에 **LICENSE 파일이 없다**
> - README 270~272행 `## License` → `MIT`
> - 루트 `package.json`: `"name": "agentnative"`, `"license": "ISC"`, `"private": true`
> - npm `@agent-native/core`: **0.183.0**(오늘 최신)·0.182.1 모두 `MIT`. `packages/core/package.json` 도 `MIT`
> 🆕 **볼트 추가 1**: 레포 전체(파일 24,223개)에서 MIT 전문이 있는 곳은 **`packages/vscode-extension/LICENSE.md` 단 하나**다(*"Copyright (c) Builder.io"*). 나머지 LICENSE 파일은 폰트 라이선스(Liberation·Noto)뿐이다. → **MIT 전문과 저작권자 표기가 하위 패키지 하나에만 있다.**
> 🆕 **볼트 추가 2**: 루트의 `ISC` 는 `npm init` **기본값**이다. 의도한 선언이라기보다 **방치된 기본값**으로 보인다(⚠️ 추정). `private: true` 라 배포되지 않으므로 실해는 작다.
> 🎯 **판정**: 배포 패키지(`@agent-native/core`)는 MIT로 봐도 된다. 🔴 **템플릿 17종(`templates/`)을 복사해 쓰는 경우는 법적 근거가 README 한 줄뿐이다.** 제품에 템플릿을 가져다 쓸 계획이면 이 점을 확인해야 한다.

> [!note] 📌 볼트 실측: 개발 속도가 비정상적으로 빠르다
> - npm `@agent-native/core` 버전 **1,563개**. 첫 배포 2026-03-12(레포 생성 당일)부터 약 194일이므로 **하루 평균 약 8개**다. `.changeset/` 기반 자동 릴리스로 보인다.
> - npm 주간 다운로드 **43,594**(09-14~09-20). ★6,218 대비 설치 신호가 강하다.
> - `packages/` **21개**(core·desktop-app·mobile-app·agent-chrome-extension·vscode-extension·scheduling·embedding·recap-cli 등). `templates/` **17개**(analytics·assets·brain·calendar·chat·clips·content·crm·design·dispatch·factory·forms·mail·plan·slides·tasks·**videos**). README 표에는 그중 9개만 나온다.
> - 루트에 `.claude/`·`.codex/`·`.gemini/`·`.agents/`·`AGENTS.md`·`CLAUDE.md`·`skills/` 가 있다. **코딩 에이전트로 개발하는 레포**다.

> [!warning] ⚠️ 스타 수치 불일치
> raw ★5,496(*"당일 +98"*) → 볼트 실측 ★**6,218**, 하루 사이 **+722**다. raw의 당일 증가폭과 맞지 않는다. 급등 중인지 raw 스냅샷이 오래된 것인지 **확인하지 못했다**(stargazers 타임스탬프 조회는 API 한도로 실패).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ ★6,218 · fork 560 · npm 주 43.6k · Builder.io 조직. 🔴 **레포 단위 라이선스 불명확**과 **정량 수치 0**(프레임워크라 성능 벤치가 없는 것은 자연스럽다)으로 medium.
- **즉시 활용**: **YES, 부분적으로.** `npx @agent-native/core create --template chat` 한 줄로 시작한다. 🎯 볼트 운영자의 영상 SaaS에 가장 직접 가져올 것은 프레임워크가 아니라 **패턴**이다. **액션 1개 = UI 버튼 + 에이전트 tool + MCP** 를 동시에 만드는 규약이다. `templates/videos`·`clips` 가 있다는 점도 확인할 가치가 있다(⚠️ 내용은 미열람).
- **6개월 영향력**: 🎯 **"MCP 서버를 따로 만든다"가 "앱의 액션을 정의하면 MCP가 따라 나온다"로 바뀐다.** 에이전트 접근을 사후 래퍼(tradingview-mcp류)가 아니라 **앱 설계의 부산물**로 얻는다.
- **대체 관계**: [[CopilotKit]](AG-UI, 프론트엔드에 에이전트 삽입)과 가장 가깝다. 차이는 Agent-Native가 **인증·DB(PostgreSQL/PGlite)·스케줄·에이전트 팀까지 풀스택**이라는 점이다. [[browser-harness]] 류 CDP 자동화는 **자기 앱에 대해서는** 대체한다(자기 앱을 CDP로 조작할 이유가 없어진다).
- **허와 실**: 걷어내면 **zod 스키마 기반 RPC + 어댑터 6종**이다. 새로운 원리가 아니라 **규약의 번들**이다. 🔴 하루 8릴리스 속도는 **API 안정성과 반비례**할 수 있다(버전 고정 필수).
- **액션**: 아래.

> [!action] 당장 할 것
> `templates/videos` 를 열어 **영상 작업이 액션 몇 개로 쪼개졌는지** 본다. 볼트 운영자의 영상 파이프라인 단계(대본→음성→장면→렌더)를 같은 `defineAction` 단위로 나누면 **에이전트 tool과 UI 버튼이 한 벌**이 되는지 판정한다.

## 관련 페이지
- [[BuilderIO]]  *(09-22 연결)*
- [[browser-harness]]: 🎯 같은 배치, 반대 노선(UI를 CDP로 조작)
- [[Electron-CDP-브리지]] · [[tradingview-mcp]]: API 없는 앱의 사후 도구화
- [[CopilotKit]]: 가장 가까운 비교군
- [[에이전트-스킬]] · [[에이전트-메모리-레이어]]: README "Skills and memory"
- [[검사가능성-공사]]: UI가 에이전트 작업을 검사 가능하게 만든다는 README 32행 논지
- [[ai-news]]

## 원본
- 출처: https://github.com/BuilderIO/agent-native
- 볼트 실측(2026-09-22, GitHub API): ★**6,218**(raw 5,496, +722 ⚠️) · fork 560(raw 508) · **license null** · TypeScript · open issues **78** = PR **62** + 이슈 **16**(search API, raw 59/18) · created 2026-03-12T14:57:10Z ✅ · pushed 2026-09-22T09:05:44Z · topics 5 · homepage agent-native.com
- npm 실측: `@agent-native/core` latest **0.183.0 MIT** · 버전 1,563개 · 첫 배포 2026-03-12T15:22 · 주간 DL 43,594
- 수치 출처: README(272행) 18·38·40·50·63·270~272행 **원문 실열람**, 루트·`packages/core` `package.json`, 재귀 트리 24,223개 파일 중 LICENSE 전수
- raw 대비: 볼트 추가 = ✅ **라이선스 4항목 전부 재현** · 🆕 **MIT 전문은 vscode-extension 하위에만 있음** · 🆕 **루트 ISC는 npm 기본값으로 추정** · 🆕 **npm 1,563버전/주 43.6k** · 🎯 **[[browser-harness]] 와의 반대 노선 대조** · ⚠️ 스타 +722 불일치
- 신뢰도: ⭐⭐ (지표·npm 확인 / 레포 단위 라이선스 불명확 · 정량 수치 0)
