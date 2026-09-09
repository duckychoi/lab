---
title: "Comp AI CRM — 에이전트가 1차 사용자인 오픈소스 CRM"
type: source
domain: ai-news
tags: [ai-news, github, agentic-first, crm, evidence, eve, durable-agent, tool-design]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# Comp AI CRM

> [!insight] 핵심 인사이트 — 이 배치에서 가장 훔칠 게 많은 설계
> raw는 *"툴 스키마/권한 모델은 원문 재확인 필요"* 라고 유보했다. 확인 결과 **README가 그 답을 수치로 다 적어 놨다**: **18 authored tools · 4 skills(마크다운 산문) · 1 schedule · `deny-all` egress 샌드박스**.
> 그리고 진짜 핵심은 CRM이 아니라 **하나의 설계 규칙**이다:
> > **"No tool accepts a confidence score, because a model asked to grade its own certainty will, and it will be wrong in the direction that makes it look useful."**
> 툴은 **관찰한 것**(`crm.signature-block`, `github.account-identity`)만 보고하고, **증거 원장(ledger)이 가격을 매긴다.** 강한 증거는 레코드에 쓰고, **약한 증거는 사람이 판정할 제안으로 격하**된다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐10,122 · fork 1,340 · TypeScript · MIT · 생성 2026-07-31 · pushed 2026-09-02(**6일 전**, 정체 아님).
- **즉시 활용**: CRM으로는 **NO**(영업 조직용). 그러나 **설계 규칙 3개는 오늘 바로 이식 가능** — ①자기보고 신뢰도 금지 ②증거 등급별 쓰기/제안 분기 ③"왜 다시 볼 것인지"를 말하지 못하면 재방문 일정을 잡지 못하게 하는 강제.
- **6개월 영향력**: "agentic-first"가 마케팅 구호에서 **검증 가능한 아키텍처 주장**으로 내려오는 사례. *"The agent is not a feature of the CRM; the CRM is where the agent keeps its notes."*
- **대체 관계**: 대체 아님. 다만 **[[에이전트-메모리-레이어]]** 를 "DB에 노트를 남기는 에이전트" 형태로 구현한 실물 참조.
- **허와 실**: **허가 거의 없다** — 주장마다 파일/함수 이름을 댄다. 다만 ①**Context**(link.context.dev) 상업 서비스가 브랜드·LinkedIn 데이터의 단일 키로 걸려 있어 **완전 무키 운용 시 기능이 줄어든다**(README도 인정) ②18 tools/4 skills는 **저자 집계**이며 볼트가 파일 수를 직접 세지는 않았다.

> [!insight] 볼트 자신에게 꽂히는 규칙
> 이 볼트가 2026-09-07·09-08 배치에서 반복해 배운 교훈 — *"raw의 한줄요약은 수집기의 요약이지 소스가 아니다"* — 은 Comp AI의 규칙과 **같은 명제**다.
> **요약(자기보고)을 증거(관찰)로 취급하지 말 것.** raw는 신뢰도 점수를 스스로 매기는 툴이고, 예상대로 **"쓸모 있어 보이는 방향"으로 틀린다**(과대 열거·범위 확대). → [[측정도구-먼저-반증]]

> [!note] 런타임 설계 — 훔칠 만한 구현 디테일
> - **eve**([Vercel] filesystem-first durable agent 프레임워크): **툴 = 파일, 스킬 = 마크다운 파일, 스케줄 = 파일.** 재배포를 견디는 세션.
> - 작업 큐 `lib/tasks.ts`: `claimDue` 가 **`FOR UPDATE SKIP LOCKED`** 로 행을 리스한다 → 디스패처 둘이 **겹치지 않는 일**을 집고, **죽은 실행은 리스 만료로 행이 풀린다.**
> - *"'N분마다 오래된 10명' 같은 것은 cron 표현식이 아니라 태스크의 `dueAt` 에 속한다."* — **스케줄을 데이터로 옮기는** 명확한 입장.
> - 세션 시작 시 **사용 가능한 키 목록을 출력**해 에이전트가 *가진 것 기준으로 계획*하게 한다(실패 호출로 결핍을 발견하지 않게).

> [!action] 당장 할 것
> `apps/agent` 의 **4개 스킬 마크다운**(`evidence.md` · `identity-matching.md` · `data-boundaries.md` · `writing-a-brief.md`)을 읽는다. 특히 `evidence.md` — 증거 등급 체계를 [[검사가능성-공사]] 의 4단 관문과 대조할 것.

## 관련 페이지
- [[검사가능성-공사]]
- [[측정도구-먼저-반증]]
- [[에이전트-메모리-레이어]]
- [[에이전트-스킬]]
- [[qm]]
- [[open-agents-vercel]]

## 원본
- 출처: https://github.com/trycompai/crm
- 실측(2026-09-09): ⭐10,122 · fork 1,340 · TypeScript · MIT · created 2026-07-31 · pushed 2026-09-02 · archived=False
- raw 대비 드리프트: **완전 일치**
- 신뢰도: ⭐⭐⭐
