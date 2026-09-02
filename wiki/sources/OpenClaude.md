---
title: OpenClaude — 임의 LLM 백엔드용 코딩 에이전트 CLI (Claude Code 파생·무허가 자체 고지)
type: source
domain: ai-news
tags: [ai-news, github, cli, coding-agent, mcp, license-risk, derivative-work]
created: 2026-09-02
updated: 2026-09-02
sources: []
reliability: high
---

# Gitlawb/openclaude — "runs anywhere. uses anything"

**URL**: https://github.com/Gitlawb/openclaude
**지표(2026-09-02)**: ⭐**31,655** · 포크 **8,975** · 이슈 **73** · 워치 **223** · **TypeScript** · SPDX **NOASSERTION** · 생성 **2026-04-01** · **당일 푸시(00:15Z)** — GitHub REST 실호출 검증
**드리프트**: raw 절대값 31,650 대비 API **+5** (±10 이내 → **API값 채택**)
**추가 검증**: `raw.githubusercontent` README 원문 + **LICENSE 파일 전문 직접 확인**

> [!warning] 🚨 이 배치 최대 발견 — 배지는 MIT, LICENSE 파일은 "우리는 배포 권한이 없다"
> raw는 이 레포를 *"라이선스가 SPDX 미식별(NOASSERTION)이라 재배포 조건 확인 필요"* 라고만 적었다. **LICENSE 파일을 직접 열어보니 훨씬 구체적인 자기 고지가 들어 있다.**
>
> README 상단에는 파란 **`license-MIT`** 배지가 걸려 있다. 그런데 그 배지가 가리키는 `LICENSE` 파일의 제목은 `LICENSE`가 아니라 **`NOTICE`** 로 시작하며, 내용은 다음과 같다(원문 인용):
> - *"This repository contains code derived from **Anthropic's Claude Code CLI**."*
> - *"The original Claude Code source is **proprietary software**: Copyright (c) Anthropic PBC. All rights reserved. Subject to Anthropic's Commercial Terms of Service."*
> - MIT 적용 범위는 **"modifications only"** 이며 그마저 **"where legally permissible"**(법적으로 허용되는 범위에서)라는 조건부다.
> - 그리고 결정적으로: *"This project **does not have Anthropic's authorization to distribute their proprietary source**. Users and contributors should evaluate their own legal position."*
>
> **즉 유지관리자 스스로가 "권한 없음"을 문서에 적어두었다.** SPDX가 NOASSERTION으로 뜨는 것은 메타데이터 누락이 아니라 **이 구조를 SPDX 식별자 하나로 표현할 수 없기 때문**이다. ⭐31,655·**포크 8,975**는 그 상태로 약 9천 벌의 사본이 이미 존재한다는 뜻이다.

> [!insight] 핵심 인사이트 — "하네스와 모델의 분리"가 법적 층위에서 먼저 파열했다
> 기능 서술은 명확하다(README 원문): OpenAI 호환 API · **Gemini** · **GitHub Models** · **Codex OAuth** · Codex · **Ollama** · Atomic Chat 등 백엔드를 바꿔 끼우면서 **프롬프트·툴·에이전트·MCP·슬래시 커맨드·스트리밍이라는 하나의 터미널 워크플로**를 유지한다. 모델은 제공하지 않고 **하네스 계층만** 제공한다.
> 볼트가 [[JIT-Agent]]·[[claude-plugins-official]] 계열에서 계속 관측해 온 명제 — **"에이전트의 가치는 모델이 아니라 하네스에 있다"** — 가 여기서 극단까지 간다. 하네스가 모델과 분리 가능하다면, **특정 벤더의 하네스를 떼어내 다른 모델에 붙이는 것**도 가능하다. OpenClaude가 실제로 한 일이 그것이고, 그 결과가 **원 벤더의 독점 코드 파생**이라는 형태로 나타났다.
> 이것은 기술적 성취인 동시에, **하네스가 실질 자산이 되는 순간 그 하네스의 소유권이 쟁점이 된다**는 것을 보여주는 첫 대형 사례다. 이름 자체가 `OpenClaude`인 것이 이 긴장을 압축한다.

> [!insight] 포크/스타 비율 0.284 — 이 배치 최고이며 성격이 다르다
> 포크 **8,975** ÷ 스타 **31,655** = **0.284**. 같은 배치 비교: [[OpenMAIC]] 0.167 · [[minimind]] 0.130 · [[video-use]] 0.122 · [[academic-research-skills]] 0.079. **OpenClaude가 2위의 1.7배**다.
> 볼트는 그간 포크를 *"직접 고쳐 쓰려는 의지"* 의 대리 지표로 읽어 왔다. CLI 도구는 보통 `npm i`로 설치하지 포크하지 않는다(README에 npm 배포 배지 `@gitlawb/openclaude` 존재). 그럼에도 포크가 스타의 28%라는 것은 **설치가 아니라 사본 보유가 일어나고 있다**는 뜻이며, 위 라이선스 고지를 함께 놓으면 해석이 갈린다 — *백엔드 커스터마이즈 목적*인지, *소실 대비 아카이빙*인지 **현재 데이터로는 판별 불가**.
> 반면 이슈는 **73건**뿐이라 **이슈/포크 0.0081**로 매우 낮다. 포크는 많은데 이슈 유입은 적다 = **가져가되 돌려주지 않는다.**

> [!question] 미해결 질문
> - 포크 8,975의 성격(커스터마이즈 vs 아카이빙)은 API 메타데이터로 판별되지 않는다. **포크 중 실제 커밋이 있는 비율**을 봐야 하나 현재 수집 파이프라인에 그 필드가 없다.
> - 백엔드별 **기능 동등성**(어느 백엔드에서 MCP·툴콜이 실제로 되는지)은 README에 표가 없다 → **미검증**.
> - 이 레포의 존속 리스크(테이크다운 가능성)는 관측 대상이 아니라 **추측**이다. 단정하지 않는다.

## 도메인별 추출 (ai-news)

- **신뢰도**: **high** — 지표는 GitHub REST 실호출, 라이선스 서술은 **LICENSE 원문 직접 인용**. 다만 high는 *문서에 그렇게 적혀 있다*에 대한 등급이지, **법적 유효성 판단이 아니다**(나는 법률 판단을 하지 않는다).
- **즉시 활용**: **아니오 — 실무 도입 보류 권고.** 기능이 매력적이어도 유지관리자가 스스로 "권한 없음"을 적은 코드를 **업무 파이프라인에 넣는 것은 별개 문제**다. 백엔드 전환이 목적이라면 라이선스가 깨끗한 대안(예: 자체 MCP 클라이언트 구성)을 먼저 검토.
- **6개월 영향력**: **중~높음(불확실성 큼)**. 기술 흐름으로는 "하네스 이식"의 대표 사례로 계속 인용될 것. 다만 존속 자체가 외부 요인에 걸려 있어 **레포 생존을 전제로 한 의존은 위험**.
- **대체 관계**: [[claude-plugins-official]](공식 인덱스)과 **정면 대비**된다. 공식 경로는 성장률 최저(+1.03%/일)인데, 무허가 파생은 ⭐31,655에 포크 8,975. **사람들은 라이선스가 아니라 편의를 따라간다**는 것을 수치로 보여준다.
- **허와 실**: 마케팅 문구 *"runs anywhere. uses anything"* 을 걷어내면 = **Claude Code CLI의 백엔드 추상화 파생본**. "anything"의 실제 경계(백엔드별 지원 범위)는 **미검증**.
- **액션**: [[actionable]]에 **① 도입 보류 판정** 등재 · **② 포크 활성도 필드 수집 검토**(포크의 성격 판별 지표 부재가 이번에 드러남).

## 관련 페이지
- [[claude-plugins-official]] — 같은 층위의 **공식** 경로. 성장률 대비 극명한 대조군
- [[JIT-Agent]] — "하네스가 실질 자산" 명제의 논문 측 근거
- [[Anthropic]] — 원저작권자
- [[에이전트-스킬]] — 하네스/스킬 층위 분류
- [[academic-research-skills]] — 같은 배치의 또 다른 NOASSERTION 건(이쪽은 **CC BY-NC**)
- [[ai-news]]
