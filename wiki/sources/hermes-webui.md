---
title: nesquena/hermes-webui — Hermes Agent 웹 UI 프론트엔드
type: source
domain: ai-news
tags: [ai-news, github-trending, hermes-agent, webui, frontend, self-hosted, agent]
created: 2026-06-02
updated: 2026-06-04
sources: []
reliability: high
---

# nesquena/hermes-webui — Hermes Agent 웹 UI

**GitHub**: https://github.com/nesquena/hermes-webui  
**스타**: ⭐12,806 (+1,722 당일, 2026-06-03 기준, prev 11,945)  
**신뢰도**: ⭐⭐⭐⭐

## 핵심 인사이트

> [!insight] 핵심 인사이트
> [[hermes-agent]]를 브라우저에서 쓸 수 있게 해주는 경량 셀프호스팅 웹 UI. 빌드 스텝 없음, 순수 Python + 바닐라 JS — 설치 후 `python3 bootstrap.py` 한 줄로 기동. CLI 완전 동등 기능을 웹/모바일에서 접근. hermes-agent가 터미널 밖으로 나왔다는 신호.

> [!action] 당장 할 것
> hermes-agent 설치 후 `./start.sh`로 port 8787 기동, Docker Compose 대안 테스트. 멀티 프로파일 + WebAuthn 인증 적용 가능성 확인.

## 도메인별 추출 (ai-news)

**즉시 활용**: YES — [[hermes-agent]] 설치되어 있다면 추가 설정 없이 바로 기동 가능  
**신뢰도**: ⭐11,945 오늘 +945 (급상승), NousResearch 공식 연계 프로젝트  
**대체 관계**: OpenWebUI, AnythingLLM 대체 (단, hermes-agent 전용)

**주요 기능:**
- 멀티 프로바이더 지원 (OpenAI, Anthropic, Google, DeepSeek 등)
- 스트리밍 응답 + 도구 호출 카드 시각화
- 파일 첨부, 인라인 코드 실행
- 세션 관리: 영구 기록, 검색, 태그, 아카이브
- 워크스페이스 브라우저: 파일 트리, 인라인 편집, Git 연동
- 음성 입력 (Web Speech API)
- 9+ 테마, 모바일 반응형

**배포:**
```bash
python3 bootstrap.py  # 또는
./start.sh            # port 8787
docker compose up -d  # Docker 단일 컨테이너
```

**철학**: No build step, no framework, no bundler — 순수 Python + vanilla JS

> [!note] 배경 정보
> [[NousResearch]]의 [[hermes-agent]]가 CLI 기반이라 진입 장벽이 있었는데, 이 WebUI로 비개발자도 접근 가능. 오픈소스 에이전트 프론트엔드 표준이 될 가능성.

## 관련 페이지
- [[hermes-agent]]
- [[NousResearch]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/nesquena/hermes-webui
- 신뢰도: ⭐⭐⭐⭐ (⭐11,945, 오늘 +945)
