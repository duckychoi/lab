---
title: "Orkas — Commander가 내장 전문가와 외부 CLI를 조율하는 데스크톱 앱"
type: source
domain: ai-news
tags: [ai-news, agent, desktop-app, orchestration, multi-agent]
created: 2026-11-01
updated: 2026-11-01
sources: [https://github.com/Orkas-AI/Orkas]
reliability: medium
---

**GitHub**: https://github.com/Orkas-AI/Orkas · ★**7,018** · fork 441 · MIT · 생성 2026-04-29 · 푸시 2026-11-01T01:24Z

## 핵심 인사이트
> [!insight] "로컬 우선 오픈소스"에는 두 제품이 들어 있다
> 패키지 앱과 소스 빌드의 기능이 다르다. 공유 프로젝트 · 클라우드 동기화 · 앱 게시는 **패키지 앱 전용**이고 로그인이 필요하다. 소스 빌드는 계정 없이 자체 키나 로컬 엔드포인트로 돈다. 내장 모델은 Orkas 관리형 서비스를 거치며, 음성 입력도 Orkas로 전송된다. MIT 라이선스가 곧 전 기능 공개를 뜻하지는 않는다.

- **구성**: Commander + 내장 전문가 16개 + 마켓 30개 이상 + Claude Code · Codex · OpenCode · OpenClaw · Hermes-Agent.
- **자동 진행**: 프로젝트 메모리, 다음 할 일 자동 진행, 시간~월 단위 자동화. 유휴 시 백그라운드 리뷰로 스킬을 다듬는다. 🔴 이 자기 수정의 품질 수치는 README에 없다.

## 도메인별 추출
- **즉시 활용**: 보류. 측정 수치가 없고, 크론과 위임 체계가 이미 있다.
- **Hermes 적용**: README가 [[hermes-agent]]를 "조율 대상 중 하나"로 위치시킨다. 경쟁이 아니라 상위 조율층이라는 주장이다.
- **대체 관계**: [[OpenMausBot]] · [[t3code]]와 같은 GUI 축.

## 관련 페이지
- [[OpenMausBot]] · [[hermes-agent]] · [[t3code]] · [[AI-에이전트-프레임워크]] · [[에이전트-메모리-레이어]]

## 원본
- 출처: https://github.com/Orkas-AI/Orkas
- 확인 범위: GitHub API · README · 🔴 앱 미실행 · 코드 미검토
- 신뢰도: ⭐⭐ (★7,018 · 수치 없음)
