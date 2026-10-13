---
title: "open-webui — '오픈소스 챗 UI'가 아니다: BSD-3 + 브랜딩 제거 금지(50명 임계)"
type: source
domain: ai-news
tags: [ai-news, local-llm, ollama, openai-api, chatui, self-hosted, rag, mcp, 라이선스-비표준, noassertion, 브랜딩-조항]
created: 2026-04-23
updated: 2026-10-13
sources: []
reliability: high
---

# open-webui/open-webui

> [!insight] 핵심 인사이트
> Ollama·OpenAI API 등 다양한 LLM 백엔드를 통합하는 사실상의 오픈소스 AI 채팅 UI 표준. 133K 스타는 "로컬 LLM 사용자의 UI 선택지" 중 압도적 1위를 의미한다.

**GitHub**: https://github.com/open-webui/open-webui  
**스타**: ⭐134,166 (+636 최근)  
**신뢰도**: ⭐⭐⭐⭐⭐

## 도메인별 추출

- **신뢰도**: 13만+ 스타, 매일 수백 스타 추가 — 로컬 LLM 생태계 핵심 인프라로 완전 안착
- **즉시 활용**: Ollama + open-webui 조합으로 자체 ChatGPT 구축 가능 (10분 설치)
- **6개월 영향력**: 기업 내부 LLM 배포의 UI 레이어 표준. 플러그인 생태계 확장 중
- **대체 관계**: ChatGPT UI 완전 대체. [[cognee]] 메모리 레이어와 통합 가능
- **액션**: 로컬 LLM 테스트 환경 구축 시 첫 번째 선택지

## 관련 페이지
- [[에이전트-메모리-레이어]]
- [[Qwen3.6-35B-A3B]]
- [[GLM-5.1]]

## 원본
- 출처: https://github.com/open-webui/open-webui

---

## 🔄 2026-10-13 갱신 (인제스트 2026-10-13) — 🏆🏆 **`NOASSERTION` 을 열었더니 "오픈소스 챗 UI"가 아니었다**

**GitHub API 실측(2026-10-13)**: ★**155,432**(수집기 155,426 → **+6**) · 포크 **22,666** · watchers **676** · open_issues **197** · Python · created 2023-10-06T22:08:27Z · pushed 2026-10-12T22:13:08Z · 476,043 KB
🔴 **볼트 기재값이 173일 묵었다**: 이 페이지 `updated` 는 **2026-04-23** 이었다.

> [!warning] 🏆🏆 **최대 발견 — `NOASSERTION` 의 정체는 "Open WebUI License" = BSD-3-Clause + 브랜딩 제거 금지 조항**
> ✅ **볼트가 `api.github.com/repos/open-webui/open-webui/license` 로 원문을 직접 받았다(HTTP 200 · 2,819자).**
> **라이선스명**: `Open WebUI License` · **Copyright (c) 2023- Open WebUI Inc.** [Created by Timothy Jaeryang Baek]
> 1~3항은 **BSD 3-Clause 와 동일**하다. 🔴 **4항이 추가돼 있고 이것이 성격을 바꾼다**(원문):
> > *"licensees are **strictly prohibited from altering, removing, obscuring, or replacing any "Open WebUI" branding**, including … name, logo, or any visual, textual, or symbolic identifiers … **except**: (i) deployments where the total number of end users … **does not exceed fifty (50) within any rolling thirty (30) day period**; (ii) **specific prior written permission**; or (iii) a **duly executed enterprise license**."*
> 🎯 ⇒ **화이트라벨링이 50명 초과 시점부터 "material breach"(중대한 계약 위반)가 된다.**
> 📌 **실무 함의가 크다**: 사내 배포·SaaS 재판매에서 로고/이름을 지우는 순간 **50명이 임계선**이다. ⚖️ **소프트웨어 사용 자체는 자유롭다 — 제한되는 것은 "브랜딩 제거"뿐이다**(이 구분을 흐리면 틀린다).
> 🔴 **추가 조건 2건도 초록에 안 드러난다**: ① *"Materials governed by **prior licenses** retain those original license terms, as specified in **LICENSE_HISTORY**"* ⇒ **파일별로 라이선스가 다를 수 있다** ② 기여 시 **CLA 동의 필수**.

> [!insight] 🏆 **볼트 10-11 규약이 2배치 만에 2번째로 적중했다 — 그리고 금일 배치에서 2/5 가 비표준 라이선스다**
> 10-11 에 볼트가 세운 규약: *"`NOASSERTION` 은 '라이선스 없음'으로 적으면 틀린다 — 반드시 `/license` 엔드포인트로 원문을 1회 확인한다."*(→ [[context-mode]] 에서 ELv2 확정)
> ✅ **금일 그 규약을 [[open-webui]] 에 적용해 2번째 적중을 얻었다.**
> | 레포 | GitHub 표기 | 원문 실체 | 핵심 제약 |
> |---|---|---|---|
> | [[context-mode]] | `NOASSERTION` | **Elastic License 2.0** | 호스팅/관리형 서비스 제공 금지 |
> | **open-webui** | `NOASSERTION` | **Open WebUI License**(BSD-3 + 4항) | 50명 초과 시 브랜딩 제거 금지 |
> 🎯 ⇒ **금일 GitHub 5건 중 2건(40%)이 `NOASSERTION` 이고, 열어 보니 둘 다 상업적 제약이 있는 비-OSI 라이선스다.**
> 🆕 **규약 승격 제안: `NOASSERTION` 은 "미확인"이 아니라 "비표준 라이선스 경보"로 취급한다.** n=2 로는 이르지만 **두 건 모두 제약이 있었다**는 사실은 적어 둔다. → [[메타데이터-부재-추론]]

> [!warning] 🔴 **"당일 급상승"이 아니다 — 수집기도 같은 판정, 2배치 연속 구조**
> 당일 **+157**(볼트 간격 델타 **+6** = 금일 5건 중 최하위 타이). ★155,432 로 **"스타 1000개 이상" 기준만** 충족한다.
> ✅ **수집기 한계보고 9번 *"기준이 OR 조건이어서 통과했을 뿐"* 이 정확하다.** 📌 **10-12 `pytorch/pytorch`(+315) 와 동일한 구조가 2배치 연속**이고, 원인도 같다 — **트렌딩 모집단이 9개로 축소돼 선별 여유가 없었다.**

> [!insight] 📌 **그래도 이 소스는 가치가 있다 — 라이선스 때문이다**
> ⚖️ 급상승 신호로는 약하지만, **본 인제스트의 최대 산출물이 이 레포에서 나왔다.** 🎯 **"상위 5건 선별 규칙이 약한 항목을 넣었는데, 그 약한 항목이 배치 최대 발견을 만들었다"** 는 점을 적어 둔다 — ⚠️ **수집 규칙의 품질을 "급상승 정확도"로만 평가하면 틀린다.**

## 도메인별 추출 (ai-news · 10-13 재작성)
- **신뢰도**: ⭐⭐⭐⭐ — GitHub API + `/license` 원문 2,819자 **직접 수신**. 라이선스 판정은 1차 문서 기반이라 확실하다.
- **즉시 활용**: 🟢 **YES, 단 조건부.** Ollama/OpenAI 호환 API 프런트로 지금 쓸 수 있다. 🔴 **브랜딩 제거 + 50명 초과 배포는 안 된다.**
- **6개월 영향력**: 🟡 셀프호스팅 LLM UI 의 사실상 표준(★15.5만 · 포크 2.27만). 🔴 **단 라이선스가 BSD 가 아니라는 사실이 알려질수록 기업 채택에서 법무 검토가 붙는다.**
- **대체 관계**: 자체 챗 UI 개발을 대체한다. ⚖️ **화이트라벨 제품을 만들 거라면 대체가 안 된다**(4항).
- **허와 실**: 🔴 **"오픈소스 셀프호스팅"이라는 일반 인식과 실제 라이선스가 다르다.** GitHub 가 `NOASSERTION`(= Other)으로 표기하는데 **대부분의 소비자는 이것을 확인하지 않는다.**
- **액션**: 아래.

> [!action] 🔴 **즉시 확인 — 이미 쓰고 있다면**
> ① 배포 인원이 30일 롤링 **50명**을 넘는가 ② 로고/이름을 바꿨는가 — **둘 다 YES 면 라이선스 위반이다.** ③ `LICENSE_HISTORY` 를 열어 **파일별 선행 라이선스**를 확인한다(볼트 미열람).

> [!question] 미해결
> - `LICENSE_HISTORY` 내용 — **미열람**(경로 확보: 레포 루트). 파일별로 어떤 선행 라이선스가 남아 있는지 미상.
> - 4항의 *"end users … direct access"* 정의 — 사내 SSO 뒤 계정 수 기준인지 동시접속 기준인지 원문이 모호하다.
> - `rag`·`mcp`·`openapi` 토픽의 **실제 구현 깊이** 미검증(기능 실행 안 함).

## 관련 페이지 (10-13 추가)
- [[context-mode]] — 🏆 같은 배치 `NOASSERTION` 2건 중 1건(ELv2)
- [[메타데이터-부재-추론]] — `NOASSERTION` 은 부재가 아니라 비표준 경보
- [[배포출처-봉인]] · [[검사가능성-공사]] — 라이선스가 채택 비용을 바꾼다
- [[rea]] · [[artcraft]] · [[diagram-design]] — 금일 동일 배치
- [[에이전트-메모리-레이어]] — RAG/MCP 를 UI 층에서 제공
- [[ai-news]]

## 원본 (10-13 갱신)
- 수집: 2026-10-13 자동수집(ai-news) · 인제스트 2026-10-13
- 볼트 실측: GitHub API HTTP 200(★155,432 · 포크 22,666 · issues 197) + 🏆 **`/license` 원문 HTTP 200 · 2,819자 수신**
- raw 대비: ✅ 스타·포크·생성일 **일치**(+6) · ✅ *"당일 급상승 아님"* 판정 **동의** · 🏆 **볼트 신규 최대 발견: `NOASSERTION` = Open WebUI License(BSD-3 + 브랜딩 4항 · 50명 임계)** · 🔴 **볼트 기재값 173일 체납 해소**
- 신뢰도: ⭐⭐⭐⭐
