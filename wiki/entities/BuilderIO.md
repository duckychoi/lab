---
title: Builder.io (BuilderIO)
type: entity
domain: ai-news
tags: [ai-news, agent-framework, visual-cms, typescript, license]
created: 2026-09-22
updated: 2026-09-22
sources: [Agent-Native.md]
reliability: medium
---

# Builder.io

GitHub `BuilderIO`. 비주얼 CMS/디자인-투-코드 회사. 볼트 첫 소스는 [[Agent-Native]].

> [!insight] 🎯 자리 — **에이전트가 UI를 클릭하지 않게** 만드는 쪽
> [[Agent-Native]] 의 `defineAction` 하나가 에이전트 tool · React 훅 · HTTP · MCP · A2A · CLI로 **동시에** 노출된다. 같은 배치 [[browser-harness]]([[browser-use]] 계열)가 **이미 있는 웹을 CDP로 사후에 뚫는** 것과 정반대 노선 — **앱을 처음부터 에이전트 친화적으로 짓는다.**

> [!warning] 🔴 라이선스 표기 4곳 불일치 (09-22 재현)
> GitHub API `null` · README `MIT` · 루트 `package.json` `ISC`(`private: true`, npm 기본값으로 추정) · npm `@agent-native/core` `MIT`. MIT 전문은 `packages/vscode-extension/LICENSE.md` 에만 있다. **배포 패키지 기준 MIT로 보이나 레포 단위 법적 라이선스는 불명확.**
> 출하 속도: npm 버전 **1,563개(하루 약 8개)** · 주간 다운로드 43,594.

## 관련 페이지
- [[Agent-Native]] · [[browser-harness]] · [[하네스-설계-축]]
- [[ai-news]]
