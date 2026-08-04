---
title: OpenManus — 초대코드 없는 오픈 범용 자율 에이전트
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-framework, autonomous-agent, mcp, browser-automation, open-source]
created: 2026-07-12
updated: 2026-07-14
sources: []
reliability: high
---

# FoundationAgents/OpenManus (GitHub ⭐57,404)

> [!note] 2026-07-14 갱신
> 스타 57,200→**57,404**(2일 +204, 당일 +126)로 완만 유지. 범용 자율 에이전트 오픈 구현 앵커로 안정. 아래 본문 수치(⭐57,200)는 최초 인제스트 시점 기준.

> [!insight] 핵심 인사이트
> Manus류 **범용 자율 에이전트를 초대코드·특수권한 없이** 오픈소스로 구현한 프레임워크. ⭐57,200(당일 +226). 터미널에 아이디어를 입력하면 에이전트가 **계획 수립 → 도구 호출 → 다단계 실행**으로 목표를 스스로 완수한다. 핵심 구성은 **[[MCP]] 도구 통합 + Playwright 브라우저 자동화 + 비전(이미지 이해) + DataAnalysis 전문 에이전트 + 멀티에이전트 워크플로우** — 즉 "LLM + 도구 + 브라우저 + 실행 루프"를 한 패키지로 묶은 자율 실행 하네스. MetaGPT 기여자(Xinbin Liang·Jinyu Xiang) 주도로, 상용 Manus의 폐쇄성을 오픈으로 되받아친 대표 사례.

**GitHub**: https://github.com/FoundationAgents/OpenManus
**스타**: ⭐57,200 (2026-07-12, 당일 +226)
**신뢰도**: ⭐⭐⭐⭐ (5.7만 스타·Python 97.8%·MIT)

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 5.7만 스타·MIT·MetaGPT 계보. 다국어 README(중·한·일)·Discord 활성으로 커뮤니티 성숙.
- **즉시 활용**: 부분 YES — 브라우저 자동화(Playwright)+[[MCP]] 도구 통합 구조는 위키 자동수집 파이프의 "웹 조사→구조화" 단계에 직접 후보. 단 자율 실행은 스케줄/무인 환경에서 blocklist·격리 전제.
- **6개월 영향력**: "초대코드 없는 Manus"라는 접근성 프레임이 범용 에이전트의 오픈 표준화를 가속. [[deer-flow]]·[[agentscope]]와 함께 "오케스트레이션 하네스" 경쟁의 한 축.
- **대체 관계**: [[deer-flow]](ByteDance 슈퍼에이전트)·[[agentscope]](관측·권한 프레임워크)와 층위 경쟁 — OpenManus는 "범용 태스크 자동 완수"에 더 가깝고, 관측·권한 성숙도는 [[agentscope]]가 우위.
- **허와 실**: "범용 자율"은 데모에서 강하나 실제 롱호라이즌 신뢰성은 [[UniClawBench]]가 지적한 pass<50% 벽에 부딪힐 가능성. 브라우저·MCP 도구 조합 자체는 실용적.
- **액션**: Playwright+MCP 도구 파이프만 떼어 위키 웹 조사 보조로 격리 실험.

> [!action] 당장 할 것
> OpenManus의 브라우저 자동화+[[MCP]] 도구 통합 구조를 격리 환경에서 1회 실행해, 위키 자동수집의 "웹 조사→구조화" 단계 오케스트레이터 후보로서 [[deer-flow]]와 대조 평가.

## 관련 페이지
- [[AI-에이전트-프레임워크]]
- [[deer-flow]]
- [[agentscope]]
- [[OpenViking]]
- [[UniClawBench]]
- [[ai-news]]

## 원본
- 출처: https://github.com/FoundationAgents/OpenManus
- 스타: ⭐57,200 (2026-07-12, 당일 +226), MIT, Python 97.8%
- 제작: MetaGPT 기여자 (Xinbin Liang, Jinyu Xiang)
- 신뢰도: ⭐⭐⭐⭐ (5.7만 스타·MIT·활성 커뮤니티, README 실측)
