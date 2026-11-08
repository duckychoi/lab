---
title: "orailnoor/cross-platform-llm-client (PrivateLM) — 안드로이드 GGUF 온디바이스(Vulkan)와 클라우드 API 전환 Flutter 클라이언트. 정량 수치 0, Firebase 내장"
type: source
domain: local-llm
tags: [local-llm, on-device, edge-ai, android, flutter, gguf, vulkan, github-trending, mit]
created: 2026-11-08
updated: 2026-11-08
sources: [https://github.com/orailnoor/cross-platform-llm-client]
reliability: low
---

**GitHub**: [orailnoor/cross-platform-llm-client](https://github.com/orailnoor/cross-platform-llm-client) · ★**1,680**(볼트 11-08 API · 수집기 1,602 → **+78/1일**) · 포크 347 · 이슈 27 · MIT · C++ · created 2026-04-25 · pushed 11-04

## 핵심 인사이트
> [!insight] "온디바이스"와 "클라우드"를 앱 하나의 토글로
> GGUF 를 폰에 내려받아 **Vulkan GPU 가속**으로 오프라인 추론, 필요하면 OpenAI·Anthropic·Gemini·Kimi API 로 전환. 첫 실행 시 기기 RAM 을 감지해 컨텍스트·토큰 한도를 추천하는 점이 비개발자 친화적. 로컬 비전(Qwen2-VL) 지원. 멀티스텝 태스크는 *"개발 중·미제공"* 이라고 README 가 직접 적는다.

> [!warning] "Private"인데 Firebase Cloud Messaging 내장
> README: *"Firebase Cloud Messaging integration for push updates and background task handling"* · *"Firebase Core + Firebase Messaging"*(볼트 grep 검출). 이름이 PrivateLM 이어도 **푸시 채널이 Google 서버를 경유**한다 — 완전 무전송을 원하면 빌드에서 제거 필요. 토큰/초 등 **정량 수치 0건**.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 안드로이드 실기기(Pixel 6A·S23 등 시연 이미지). 속도 수치 없음.
- **Hermes 적용**: NO — 클라이언트 앱이지 서버 구성요소가 아님.
- **트레이드오프**: 편의성↑ / 프라이버시 주장과 FCM 의존이 충돌.
- **오픈소스 구현체**: YES(MIT) — Flutter + llama.cpp 계열 Vulkan 백엔드 참고용.

## 관련 페이지
- 온디바이스 AI
- 같은 배치 크론: [[리서치-온디바이스-AI엣지-추론모델-경량화-기술의-2026년-최신-동향]]

## 원본
- 출처: https://github.com/orailnoor/cross-platform-llm-client
- 확인 범위: GitHub API(볼트 11-08) · README raw grep(Vulkan · Firebase 검출) · 실행 0회
- 신뢰도: ⭐ (★1.7K · 수치 없음)
