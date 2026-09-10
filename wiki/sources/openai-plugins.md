---
title: "openai/plugins — Codex 플러그인 공식 예제 모음"
type: source
domain: ai-news
tags: [ai-news, github, codex, plugins, mcp, agent-skills, openai]
created: 2026-09-10
updated: 2026-09-10
sources: []
reliability: low
---

# openai/plugins

> [!insight] 핵심 인사이트
> **프레임워크가 아니라 예제 저장소**다. 값은 코드가 아니라 **매니페스트 규약**에 있다 — 플러그인은 `plugins/<name>/` 에 `.codex-plugin/plugin.json` **필수** + `skills/`·`.app.json`·`.mcp.json`·`agents/`·`commands/`·`hooks.json` **선택** 동반.
> → **한 플러그인이 스킬·MCP·서브에이전트·커맨드·훅을 한 묶음으로 배포**한다. 이게 이 레포의 실제 내용이다.

> [!insight] 놓치기 쉬운 설계 결정 — 마켓플레이스 이원화
> 기본 마켓플레이스는 `.agents/plugins/marketplace.json` 인데, **API 키 로그인 사용자는 `api_marketplace.json` 로 분리**된다.
> → 인증 경로에 따라 **보이는 플러그인 목록이 달라진다.** 구독 사용자와 API 사용자에게 다른 생태계를 노출하겠다는 뜻 — 배포자 입장에서는 **두 곳에 등록해야** 한다는 실무 함정.

> [!note] 수록 예제
> figma(**Code to Canvas · Code Connect**) · notion · build-ios/macos/web-apps · expo · netlify · **remotion** · google-slides.
> → **remotion 예제가 있다.** 내 reat-* 파이프라인이 Remotion 기반이므로 이 항목만은 직접 관련.

> [!warning] 🔴 신뢰도 낮음 — 스타는 코드가 아니라 조직이다
> - **README 1,283바이트**(실측). 이 배치 최소. **벤치마크·성능 수치 전무.**
> - **라이선스 파일 없음** — API `license: None`(실측 확인). **재사용 권리 불명.** 예제를 복사해 쓰는 것이 허용되는지 명시가 없다.
> - 당일 **+498 스타**는 코드 규모와 무관하다. 생성 2026-03-04로 6개월 됐는데 총 6,322 — **급상승분이 최근에 몰렸다**는 것은 `openai` 조직 신규 공개라는 **이벤트 신호**로 해석해야 한다.
> → 볼트 규칙 *"스타는 조직 프리미엄을 반영한다"* 적용. [[teamai-cli]] 와 같은 패턴이나 이쪽이 더 심하다(내용이 더 적다).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐**6,322**(실측 2026-09-10, raw 6,320 대비 +2) · 포크 834 · 이슈 38 · **라이선스 없음** · JavaScript · 생성 2026-03-04 · pushed 2026-09-08. **pushed가 이 배치 GitHub 5건 중 유일하게 09-08** — 나머지 4건은 09-10.
- **즉시 활용**: **부분 YES.** 코드가 아니라 **`plugin.json` 매니페스트 스펙**만 필요. 특히 **remotion 예제**는 내 파이프라인과 직결.
- **6개월 영향력**: 플러그인이 **스킬+MCP+훅의 상위 배포 단위**로 굳는다면 내 reat-* 스킬 묶음도 그 형태로 재포장하는 게 맞다. [[text-to-cad]]·[[teamai-cli]] 와 합쳐 **동일 방향 3건**.
- **대체 관계**: 내 개별 스킬 배포를 **묶음 단위**로 대체 가능.
- **허와 실**: 마케팅을 걷어내면 **예제 몇 개와 매니페스트 규약**이다. "OpenAI Plugins"라는 이름이 주는 무게 대비 실체는 가볍다.
- **액션**: **remotion 예제 1건만** 열어보고 매니페스트 구조 확인. clone 불필요.

> [!action] 당장 할 것
> `plugins/remotion/` 의 `.codex-plugin/plugin.json` 만 확인 — 내 reat-* 를 플러그인 1개로 묶을 수 있는지 판단. **라이선스가 없으므로 코드 복사는 하지 말고 구조만 참고.**

> [!question] 미해결 질문
> 라이선스 부재가 의도인지 누락인지 불명. 예제 코드 재사용 가능 여부를 **가정하면 안 된다**.

## 관련 페이지
- [[OpenAI]]
- [[에이전트-스킬]]
- [[text-to-cad]]
- [[teamai-cli]]
- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]

## 원본
- 출처: https://github.com/openai/plugins
- 실측(2026-09-10): ⭐**6,322** · 포크 834 · 이슈 38 · **license: None** · pushed 2026-09-08T17:57:28Z
- **README 1,283바이트 실측 확인** — raw 표기와 정확히 일치
- raw 대비 드리프트: 스타 +2. **그 외 전 항목 일치**
- 신뢰도: ⭐ (README 극소 · 수치 전무 · 라이선스 부재 · 스타는 조직 이벤트)
