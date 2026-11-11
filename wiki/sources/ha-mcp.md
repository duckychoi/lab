---
title: "ha-mcp — MCP 클라이언트가 Home Assistant 설정·자동화를 직접 고치게 하는 87-툴 MCP 서버 (관리자 토큰으로 동작)"
type: source
domain: ai-news
tags: [ai-news, github-trending, mcp, home-assistant, smart-home, tool-search]
created: 2026-11-11
updated: 2026-11-11
sources: [https://github.com/homeassistant-ai/ha-mcp]
reliability: medium
---

**레포**: [homeassistant-ai/ha-mcp](https://github.com/homeassistant-ai/ha-mcp) · ★**6,887** · fork 441 · open_issues 21(이슈+PR) · MIT · Python · created 2025-09-14 · pushed 2026-11-11T08:58Z (GitHub API 볼트 실측 — 수집기 수치와 전건 일치)

## 핵심 인사이트
> [!insight] 툴이 87개면 "툴을 찾는 툴"이 필요해진다
> README 배지·목록 기준 **87개 툴**. 일부 클라이언트의 툴 수 상한 때문에 `ha_search_tools`(BM25 영어 키워드 검색)로 숨긴 툴을 필요할 때만 꺼내는 모드를 둔다(README 361행 볼트 확인). MCP 서버가 커질수록 툴 선택 자체가 하나의 과제가 된다 — 같은 날 입고된 [[MMDM]] 이 재는 "툴·스킬 선택" 능력과 같은 문제다.

> [!warning] 권한 표면이 넓다
> - 서버는 **관리자 토큰**으로 동작한다(README 36·44행 "admin token" 볼트 확인). 원격 접속 기본값은 HA 웹훅 URL(README 56행) — 수집기 판독으로는 "비밀 URL = 자격증명" 방식이며 `ha_auth`·OIDC 는 옵션.
> - 조직명은 `homeassistant-ai` 로 공식 `home-assistant` 조직이 아니다(수집기 판독 · 볼트는 README 에서 "community" 표기만 확인, 공식 여부 자체는 미확인).
> - stdio 전송은 연결 문제가 있어 HTTP 권장(README 95행 · 이슈 #1713 볼트 확인).

## 도메인별 추출 (ai-news)
- **신뢰도**: ★6,887 · 당일 +790(수집기) · 릴리스 v9.1.2(11-08, 수집기) · 정량 벤치 없음(MCP 서버).
- **즉시 활용**: Home Assistant 를 쓰는 경우에만 YES. 이 볼트 사용자의 HA 사용 여부는 볼트에 기록 없음 → 판단 보류.
- **6개월 영향력**: "자연어로 자동화 YAML 수정"이 스마트홈 기본 인터페이스가 될 수 있다. 다만 관리자 권한을 LLM 에 넘기는 구조라 오조작 비용이 크다.
- **대체 관계**: HA 내장 대화 에이전트·수동 YAML 편집을 보강.
- **허와 실**: 기능 목록은 README 로 확인되나 성공률·오조작률 같은 측정값은 없다.
- **액션**: 보류(star 수준). 요구 버전은 in-process 통합 기준 **HA 2026.8.0 이상**(README 46·318행).

## 관련 페이지
- [[MMDM]] · [[에이전트-스킬]] · [[Viggle-Remake]](MCP 로 도구를 묶는 같은 구조)

## 원본
- 출처: https://github.com/homeassistant-ai/ha-mcp
- 확인 범위: GitHub API 메타 · README 패턴 검색(87 · ha_search_tools · 2026.8.0 · #1713 · admin token · webhook) · 🔴 코드·실행 미확인
- 신뢰도: ⭐⭐ (★6,887 · 벤치 없음)
