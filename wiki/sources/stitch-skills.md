---
title: stitch-skills — Stitch MCP 연동 에이전트 스킬 라이브러리 (Google Labs)
type: source
domain: ai-news
tags: [ai-news, agent-skills, mcp, google-labs, design, claude-code, video-saas]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: high
---

# google-labs-code/stitch-skills

> [!insight] 핵심 인사이트
> [[Google-Labs]]가 **Agent Skills 오픈 표준**을 따라 만든 스킬 라이브러리. ⭐6,863. **Stitch MCP 서버**와 연동되며 [[Claude-Code-워크플로우]]·Cursor·Gemini CLI에서 동작. 3대 플러그인 스위트 — **Design**(코드↔디자인 변환·화면 생성·디자인 시스템·스펙 추출)·**Build**(코드 생성·React/React Native/**Remotion 영상 생성**/shadcn)·**Utilities**(디자인 분석·프롬프트 강화·멀티페이지 웹 생성).

**GitHub**: https://github.com/google-labs-code/stitch-skills  
**스타**: ⭐6,863 (당일 +117)  
**신뢰도**: ⭐⭐⭐⭐ (Google 공식 조직·Apache 2.0)

## 도메인별 추출

- **신뢰도**: ⭐⭐⭐⭐ — [[Google-Labs]] 공식·Apache 2.0. [[design-md]]에 이은 두 번째 에이전트 코딩 표준화 산출물
- **즉시 활용**: YES — Claude Code에서 바로 스킬로 로드. 특히 **Build 플러그인의 Remotion 영상 생성**은 내 [[reat-render]]·[[reat-slides]] 파이프와 직접 겹침 → 레이아웃/스킬 패턴 추출 대상
- **6개월 영향력**: "MCP 서버 + 스킬 라이브러리" 조합이 표준 배포 형태로 굳음. Design→Build→Utilities의 3단 구성은 디자인→코드→영상 end-to-end를 한 벤더가 커버
- **대체 관계**: [[claude-skills]]·[[agent-skills]]·[[mattpocock-skills]] 계열과 경쟁하되, **Stitch MCP 종속**이 차별점(자유 스킬이 아니라 서버 연동 전제)
- **허와 실**: Stitch MCP 서버가 없으면 반쪽 — 스킬 자체는 오픈이나 실효는 Stitch 생태계에 묶임. 순수 이식 시 MCP 부분 대체 필요
- **액션**: Build 플러그인의 Remotion·shadcn 스킬 정의를 뜯어 내 영상 자동화 스킬 구조와 대조

> [!action] 당장 할 것
> stitch-skills의 Build(Remotion) 플러그인 스킬 정의를 읽고, [[reat-render]]/[[reat-slides]]가 참고할 레이아웃·컴포지션 패턴을 추출한다.

## 관련 페이지
- [[Google-Labs]]
- [[design-md]]
- [[Claude-Code-워크플로우]]
- [[claude-skills]]
- [[reat-render]]

## 원본
- 출처: https://github.com/google-labs-code/stitch-skills
- 신뢰도: ⭐⭐⭐⭐ (Google 공식·Apache 2.0)
