---
title: LibreChat — 모델을 만들지 않고 접근 계층만 통합하는 셀프호스트 채팅 플랫폼
type: source
domain: ai-news
tags: [ai-news, github, self-hosted, multi-provider, chat-ui, mcp, agents, access-layer]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: high
---

# GitHub: danny-avila/LibreChat — ★44,019

**URL**: https://github.com/danny-avila/LibreChat
**지표(2026-09-16 API 실측)**: ★ **44,019** (raw 44,017 · 드리프트 **+2**) · fork **9,038** (**raw와 완전 일치**) · TypeScript
생성 **2023-02-12**(3년 7개월) · 최종 push **2026-09-16** · 현재 **v0.8.8-rc3 = 정식 릴리스 아님**

> [!insight] 핵심 인사이트 — **fork 비율이 제품 유형을 드러낸다**
> 볼트가 이 배치 GitHub 5건의 **★:fork 비율**을 계산했다:
>
> - **LibreChat 4.9:1** (44,019 / 9,038)
> - **[[9router]] 5.5:1** (28,983 / 5,318)
> - **[[pi-agent-harness]] 7.9:1** (106,058 / 13,340)
> - **[[atlas-source-control]] 16.6:1** (4,761 / 286)
> - **[[worktrunk]] 29:1** (7,876 / 272)
>
> 🎯 **셀프호스트·프록시류(LibreChat·9router)는 fork 비율이 3~6배 높다.** fork가 "기여"가 아니라 **배포 단위**이기 때문이다 — 자기 인스턴스를 띄우려면 fork한다. 반면 CLI 도구(worktrunk·atlas)는 **설치해서 쓸 뿐 fork하지 않는다.**
> 📌 **즉 fork 수는 인기 지표가 아니라 배포 모델 지표다.** ★만 보면 worktrunk(7,876)와 atlas(4,761)가 작아 보이지만, **사용 형태가 달라서 fork가 안 생기는 것**이다.

> [!note] 이 제품이 하는 일 — 만들지 않고 묶는다
> Anthropic · OpenAI · Azure · Bedrock · Mistral · OpenRouter · Vertex 등 **여러 프로바이더를 하나의 셀프호스트 채팅 UI**로 묶고 에이전트 · MCP · 스킬 · 아티팩트를 붙인다.
> **모델을 만들지 않는다. 접근 계층만 통합한다.** [[HuggingFace]] 가 모델 *정의*의 공통 기반이라면, LibreChat은 모델 *접근*의 공통 기반을 노린다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ ★44,019 · 3년 7개월 · 당일 push. ⚠️ 단 **v0.8.8-rc3(release candidate)** — 1.0 이전이며 정식 릴리스 아님
- **즉시 활용**: **YES.** 멀티 프로바이더 키를 한 UI에서 쓰려는 경우 즉시 배포 가능. `topics` 20개가 실제 지원 프로바이더와 일치(anthropic·claude·deepseek·gemini·gpt-5·mcp·openai 등) — **이 레포는 topics가 정확한 편이다.**
- **대체 관계**: 상용 ChatGPT/Claude 웹 UI 대체. 단 **모델 성능은 그대로**이고 바뀌는 건 **통제권과 데이터 위치**다.
- **허와 실**: *"Enhanced ChatGPT Clone"* 이라는 자기 규정이 정확하다 — **과장이 없다.** 3년 넘게 rc를 못 벗어난 것은 **범위가 계속 늘어나기 때문**으로 보이나, 이는 볼트 추정이지 저자 진술이 아니다.

> [!action] 실행 항목
> 멀티 프로바이더 라우팅이 필요하면 **[[9router]] 보다 먼저 검토할 것.** 9router는 프록시 계층이고 LibreChat은 UI+백엔드 통합이라 **목적이 다르다** — 9router는 기존 코딩 CLI를 가로채고, LibreChat은 자체 UI를 준다.

## 관련 페이지
- [[9router]] — 같은 "멀티 프로바이더" 축, 다른 계층(프록시 vs UI)
- [[pi-agent-harness]] · [[worktrunk]] · [[atlas-source-control]] — 같은 배치
- [[HuggingFace]] — 모델 정의의 공통 기반 (접근 계층과 대비)
- [[ai-news]]

## 원본
- 출처: https://github.com/danny-avila/LibreChat
- 검증: GitHub API 실호출(2026-09-16). ★+2 · **fork 9,038 완전 일치** · topics 20개 대조
- 신뢰도: ⭐⭐⭐
