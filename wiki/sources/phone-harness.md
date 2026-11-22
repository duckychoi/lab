---
title: "phone-harness/phone-harness — 코딩 에이전트가 실제 폰을 탭 · 스와이프 · 판독하게 하는 CLI (iPhone Mirroring OCR · Android adb)"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent, mobile, harness, mcp, ocr]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/phone-harness/phone-harness]
reliability: medium
---

**GitHub**: ★5,474(볼트 API 11-22 · 수집기 11-21 5,404) · Python · MIT · 생성 2026-08-07

## 핵심 인사이트
> [!insight] 에이전트의 손이 브라우저에서 실기기로 넓어진다 — 단, 눈은 OCR 이다
> `open_app / tap_text / type_text / screen` 헬퍼로 Claude Code · Codex 등이 폰을 조작. iPhone 은 macOS 15+ 의 iPhone Mirroring 창을 캡처해 Apple Vision OCR 로 읽고 입력 이벤트를 보낸다(탈옥 · Xcode · 폰 설치 불필요, iOS 18+). Android 는 adb + 접근성 트리(macOS/Linux/Windows). MCP 엔드포인트와 Hermes · OpenClaw 플러그인 제공.

> [!warning] README 가 스스로 적은 한계
> OCR 은 텍스트만 본다(라벨 없는 아이콘은 스크린샷 + 비전 모델 필요) · 멀티터치 · 카메라 · Face ID 불가 · DRM 영상은 검게 나옴 · 잠금 해제는 사용자 몫. **성공률 등 벤치 수치 0.** README 상당 부분이 유료 호스팅(Phone Harness Cloud, 폰당 보증금 $20) 유도.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ — ★5k · MIT · 한계 자기 명시([[자기제한-명시]]) · 측정 0.
- **즉시 활용**: 🟡 Android + adb 는 리눅스에서도 시험 가능. iPhone 은 Mac 필수.
- **6개월 영향력**: 모바일 앱 QA · 앱 내 반복 작업 자동화가 코딩 에이전트의 도구가 된다.
- **대체 관계**: [[mobile-mcp]] 와 같은 층(모바일 조작 MCP), [[browser-harness]] 의 모바일판.
- **허와 실**: "실제 폰 조작"은 사실이나 텍스트 기반 UI 한정.
- **액션**: 관찰(모바일 QA 필요 시 Android 경로부터).

## 관련 페이지
- [[mobile-mcp]] · [[browser-harness]] · [[hermes-agent]] · [[openclaw]] · [[하네스-설계-축]] · [[자기제한-명시]]

## 원본
- 출처: https://github.com/phone-harness/phone-harness
- 확인 범위: GitHub API(스타 · 언어 · MIT · 생성일) · 🔴 README 내용은 수집기 판독 · 실행 0
- 신뢰도: ⭐⭐⭐
