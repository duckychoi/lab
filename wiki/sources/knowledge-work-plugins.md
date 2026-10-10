---
title: anthropics/knowledge-work-plugins — Anthropic 지식 노동자용 Claude Code 플러그인
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, plugins, anthropic, knowledge-work, research, workflow, plugin, connector, cowork, 하네스-설계]
created: 2026-05-25
updated: 2026-10-10
sources: []
reliability: high
---

# anthropics/knowledge-work-plugins — Anthropic 지식 노동자용 Claude Code 플러그인

> [!update] 2026-10-10 갱신 — ⭐**28,497**(05-25 대비 **+14,050 · +97.2%** · **138일 만의 첫 재관측**) · 🏆 **"지식 노동자용"에서 "직무별 플러그인 11종"으로 재포지셔닝됐다**
> **2026-10-10 실측**: ★**28,497** · 당일 +709 · **트렌딩 6위** · fork **3,258** · **open_issues 140 = 순수이슈 79 + PR 61**(PR 비중 **43.6%**) · Apache-2.0 · Python · created 2026-01-23 · pushed 2026-10-10 · watchers 186.
> 📈 **05-25 14,447 → 28,497 = +14,050(+97.2% · 일평균 약 102).**
> 🔴 **이 페이지가 2026-05-25 이후 138일간 미갱신이었다** ⇒ 📌 **[[캐시된-지표-신선도]] 의 볼트 내부 버전** — 같은 배치 [[claude-mem]](약 6개월 공백 · ★+60.1%)과 **동일 유형이고 금일 2건째**다. **볼트 자기 기록의 나이도 지표다.**
>
> 🏆 **새 정보 1 — 성격이 바뀌었다.** 05-25 기록은 *"개발자가 아닌 지식 노동자용 · 문서 요약·리서치·워크플로우 자동화 특화"* 였다. 금일 확인되는 것은 **스킬·커넥터·슬래시커맨드·서브에이전트를 직무 단위로 묶은 플러그인 11종**(productivity · sales · customer-support · product-management · marketing 등)이고 **Claude Cowork 용**으로 공개하며 **Claude Code 호환**도 명시한다.
> ⇒ ⚖️ **"기능별 도구 모음"에서 "직무별 묶음"으로 조직 단위가 올라갔다.** 05-25 판정(*"리서치 도구를 Claude 생태계로 흡수"*)은 **방향은 맞았고 단위를 못 잡았다.**
>
> 🎯 **새 정보 2 — 묶음 계층이 공식 공급자 쪽에서 나왔다.** 금일 배치에서 3개 층이 동시에 관측됐다:
> - **스킬 단위**: [[mattpocock-skills]] · [[diagram-design]] · [[rea]]
> - **하네스 제어면**: [[t3code]]
> - **직무 묶음**: 본 레포 ← **최상층**
>
> ⇒ ⚖️ 10-06 *"하네스 생태계가 층으로 쌓인다"* 가설의 **보강 증거이고 반증이 아니다** → [[하네스-설계-축]].
> ⚖️ **단 [[mattpocock-skills]] 와 방향이 반대다** — 그쪽은 *"프레임워크가 프로세스를 소유하면 통제를 빼앗는다"* 며 **작게 쪼개라**고 하고, 본 레포는 **직무로 묶는다** ⇒ 📌 **같은 날 두 반대 처방이 공식·개인 양쪽에서 도착했다** → [[대립레시피-동시도착]] 후보.
>
> 🔴 **측정 수치 0개** — 플러그인이 업무 품질·시간을 얼마나 바꾸는지 측정이 **전혀 없다**(05-25 에도 없었고 138일 후에도 없다). `topics` **0개** · `description` **1줄** → [[메타데이터-부재-추론]] 누적(금일 2건: 본 레포 · [[mattpocock-skills]]).
> ⚠️ **커넥터 의존이 크다** — 실행에 외부 SaaS 계정이 필요하다(Slack · Notion · Asana · Linear · Jira · HubSpot · Intercom · Figma · Amplitude · Microsoft 365 등을 표로 열거) ⇒ 🔴 **볼트 환경에서는 대부분 돌지 않는다**(Gmail·Drive·Calendar **미인증**). 📌 **금일 실행 문턱의 최고값이고 최저값은 [[laya]]**(`pip install laya`).
> 📌 *"11개를 오픈소스로 공개한다"* 는 **개수 선언**이고 **각 플러그인 내부 스킬 수는 미집계**다(볼트가 확인 가능 · 05-25 액션 *"플러그인 목록 확인"* 이 138일째 미이행).
> 🔗 [[Anthropic]] · [[하네스-설계-축]] · [[대립레시피-동시도착]] · [[t3code]] · [[laya]] · [[캐시된-지표-신선도]] · [[에이전트-스킬]]


> [!insight] 핵심 인사이트
> Anthropic이 개발자가 아닌 "지식 노동자"를 위한 Claude Code 플러그인을 별도 레포로 공개. 문서 요약·리서치·워크플로우 자동화 특화. [[claude-plugins-official]]과 다른 타겟 시장.

## 도메인별 추출

- **신뢰도**: GitHub ⭐14,447 (오늘 +550), Anthropic 공식
- **즉시 활용**: YES — 리서치 자동화, 문서 요약에 즉시 적용
- **6개월 영향력**: AI 코딩 → AI 지식 작업으로 Claude Code 사용 범위 확장
- **대체 관계**: 기존 노션 AI, Perplexity 등 리서치 도구를 Claude 생태계로 흡수
- **액션**: 플러그인 목록 확인, wiki 인제스트 파이프라인에 활용 가능한 것 탐색

> [!action] 당장 할 것
> 리서치 자동화 플러그인이 있다면 현재 [[LLM-Wiki]] 워크플로우에 통합 검토.

## 관련 페이지
- [[claude-plugins-official]]
- [[Claude-Code-워크플로우]]
- [[LLM-Wiki]]

## 원본
- 출처: https://github.com/anthropics/knowledge-work-plugins
- 신뢰도: ⭐⭐⭐⭐ (Anthropic 공식, 14.4K 스타)
