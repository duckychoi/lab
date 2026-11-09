---
title: "haydenschmitty/floorplan — 코드베이스를 화면·파일·API·외부 서비스의 줌 가능한 지도로, 노드 설명은 평이한 말로. 헬스 체크(키 노출·무인증 엔드포인트) 포함"
type: source
domain: ai-news
tags: [ai-news, github-trending, codebase-visualization, claude-code, codex, security-check, javascript, mit]
created: 2026-11-09
updated: 2026-11-09
sources: [https://github.com/haydenschmitty/floorplan]
reliability: medium
---

**GitHub**: [haydenschmitty/floorplan](https://github.com/haydenschmitty/floorplan) · ★**3,285**(볼트 11-09 API · 수집기 3,200 → +85) · 포크 258 · 이슈 **59** · MIT · JavaScript · created 2026-10-27 · 🔴 pushed **11-02**(7일 정지)

## 핵심 인사이트
> [!insight] "AI 가 만든 앱을 코드 안 읽고 이해하기" — 대상 사용자가 비개발자
> 앱→파트→파일 그룹→파일→엔드포인트 줌, "Stripe API wrapper" 대신 "결제를 받는 곳". 프런트 요청을 서버 엔드포인트에 **레포를 넘어** 매칭, "환불이 카드까지 어떻게 가나?" 질문에 미니맵으로 답. **헬스 체크**: 코드 내 키 · 열린 Supabase 테이블/Firebase 규칙 · 위조 가능한 Stripe 웹훅 · 무인증 엔드포인트 · AI 가 방금 바꾼 부분.

> [!warning] 정적 분석 정확도 수치 없음 · 대형 코드베이스는 README 스스로 [[Understand-Anything]] 을 권함. 이슈 59 / 푸시 7일 정지.

## 도메인별 추출 (ai-news)
- **즉시 활용**: YES(소규모) — 바이브코딩한 사이드 프로젝트 보안 1차 점검용
- **대체 관계**: [[Understand-Anything]] 의 비개발자판
- **액션**: 내 Next.js 프로젝트 하나에 1회 실행해 헬스 체크 결과만 확인

## 관련 페이지
- [[Understand-Anything]] · [[stack-diagram]](같은 배치 — 구조 시각화)

## 원본
- 출처: https://github.com/haydenschmitty/floorplan
- 확인 범위: GitHub API(볼트 11-09) · README 미정독 · 실행 0회
- 신뢰도: ⭐⭐
