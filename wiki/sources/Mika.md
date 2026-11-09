---
title: "wangzan101/Mika — 숨은 가상 화면에서 앱을 직접 탭·입력하는 안드로이드 에이전트. \"온디바이스\"는 조작 위치이고 두뇌는 클라우드 API"
type: source
domain: ai-news
tags: [ai-news, github-trending, android, phone-agent, gui-agent, kotlin, apache-2.0, on-device]
created: 2026-11-09
updated: 2026-11-09
sources: [https://github.com/wangzan101/Mika]
reliability: medium
---

**GitHub**: [wangzan101/Mika](https://github.com/wangzan101/Mika) · ★**7,830**(볼트 11-09 09:04Z API · 수집기 7,663 → +167/1일) · 포크 1,790 · 이슈 131 · Apache-2.0 · Kotlin · created 2026-10-29(11일차) · pushed 11-09

## 핵심 인사이트
> [!insight] 앱 API 대신 "화면을 보고 누르는" GUI 에이전트를 사용자 폰의 별도 가상 디스플레이에서 돌린다
> 사용자는 그동안 폰을 계속 쓴다. 무선 디버깅 페어링 1회로 루팅 없이 동작 → 국내 앱처럼 API 가 없는 대상도 원리상 자동화 가능. 완료 작업을 스킬로 저장해 재사용([[에이전트-스킬]]), PC 에이전트가 CLI+Skill/MCP 로 작업을 폰에 위임.

> [!warning] "온디바이스"의 범위
> 조작·샌드박스(arm64 Linux)는 폰 안이지만 **판단 모델은 본인 API 키 / ChatGPT·xAI·OpenRouter 로그인** = 클라우드. 화면 내용이 모델 제공자로 간다. 데모 다수가 WeChat·샤오훙슈 기준 — 국내 앱 동작은 미확인.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★7.8K / 11일 · 포크 비율 23%(정상 범위) · 성공률·벤치 수치 0건
- **즉시 활용**: 부분 YES — 개인 폰 자동화 실험용. 결제·주문 전 확인하는 Ask 모드가 기본, 로그인·인증·결제는 사람에게 넘김
- **대체 관계**: Tasker·자동화 앱 + 접근성 서비스 조합을 LLM GUI 조작으로 대체
- **허와 실**: "아무 앱에나 동작"은 원리 주장, 정확도 측정 없음
- **액션**: star · 여분 폰에서만 시험(본 폰 X)

## 관련 페이지
- [[에이전트-스킬]] · [[PrivateLM]](같은 안드로이드 축, 11-08) · [[agent-autoloop]](같은 배치 — 무인 에이전트 운영)

## 원본
- 출처: https://github.com/wangzan101/Mika
- 확인 범위: GitHub API(볼트 11-09) · README 미정독(수집기 요약 기준) · 실행 0회
- 신뢰도: ⭐⭐ (★7.8K · 수치 0)
