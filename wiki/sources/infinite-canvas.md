---
title: "infinite-canvas(无限画布) — 노드형 무한 캔버스 AI 이미지·영상 작업대 + MCP 캔버스 에이전트. 스폰서 8곳 대부분이 API 중계상이라 '비즈니스 모델'이 README 첫 화면에 있다"
type: source
domain: video-saas
tags: [video-saas, ai-news, github-trending, infinite-canvas, node-canvas, mcp, canvas-agent, plugin-sdk, api-relay, 기능벤치마킹]
created: 2026-10-26
updated: 2026-10-26
sources: [https://github.com/basketikun/infinite-canvas]
reliability: low
---

# basketikun/infinite-canvas — ★9,165 · TypeScript · MIT · 개발 단계

> [!note] 도메인 판단 — `video-saas`
> README 본문은 *"面向图片创作的开源工作台"*(이미지 창작 중심)이지만 레포 설명·기능에 **영상 생성**이 포함되고, 이 레포의 가치는 개발 도구가 아니라 **크리에이터용 제작 UI(노드 캔버스)의 벤치마크**다. 볼트에서 같은 성격인 [[ComfyUI]]·[[artcraft]]가 `video-saas`로 분류되어 있어 일관성을 맞췄다.

> [!insight] 핵심 인사이트 — **"캔버스 + 외부 코딩 에이전트가 MCP로 캔버스를 조작"이 오픈소스로 내려왔다**
> 무한 캔버스(노드 드래그·연결선·미니맵·undo)에 텍스트→이미지, 이미지→이미지, 참조 편집, 오디오·영상 생성 노드를 올리고, 로컬 **Canvas Agent**(`canvas-agent/` 실재 확인)가 Codex/Claude Code를 MCP로 연결해 **에이전트가 현재 캔버스를 직접 편집**한다. Codex app 플러그인(`plugins/`)은 MCP 자동 등록까지 한다. 원격 URL로 설치하는 노드 플러그인 + TypeScript SDK도 있다. ⇒ 영상 SaaS 관점에서 "프롬프트 창"이 아니라 **에이전트가 조작 가능한 노드 그래프**가 제작 UI의 다음 형태라는 신호.
> 동시에 이 레포는 **모델을 하나도 제공하지 않는다** — 브라우저가 사용자가 넣은 OpenAI 호환 Base URL/키로 직접 호출. 그 Base URL을 채워주는 쪽이 README 최상단 스폰서들이다.

> [!warning] 리스크 / 자기보고
> - **스폰서 8곳 중 대부분이 API 중계(中转)·저가 리셀러**(APIMart, 88API, Infistar "공식가 1할", PackyCode "Claude Code·Codex 중계", HeyRoute 등)이고 다수가 **aff 추적 링크**. 제공자 약관 위반 소지가 있는 경로를 사실상 권장.
> - 레포 설명이 *"chatgpt2api、grok2api、flow2api"* 채널 접속을 명시하고, README가 저자의 `chatgpt2api`(무료 생이미지)를 홍보 — 웹 구독을 API로 바꾸는 계열로 보이며(추정, 미열람) 약관 회색지대.
> - README `[!CAUTION]`: *"개발 단계, 과거 데이터 호환 보장 안 함, 로컬 저장 형식이 직접 바뀔 수 있음"*. API 키·캔버스·생성기록은 **브라우저 로컬 저장**.
> - 성능·사용자 수치는 README에 없음(효과 이미지 8장뿐). 수집기 "mostly Chinese README, sponsor ads" 확인.

## 도메인별 추출

### ai-news 템플릿
- **신뢰도**: ★9,165 · fork **2,144**(23%, 매우 높음 — 2차 개발·자체 배포용 포크 많음) · open issues 19 · created 2026-05-18(5개월) · pushed 10-25 · 논문·벤치 없음 · 커뮤니티 Linux.do/QQ.
- **즉시 활용**: **NO(실서비스) / YES(UI 벤치마킹)** — 데이터 호환 미보장·중계 채널 의존이라 제작 파이프라인에 넣을 수 없음. Docker(`docker compose up -d`, :3000)로 띄워 UI만 보는 것은 가능하나 다운로드 코드 실행이므로 [[sandbox-runtime]]이나 격리 VM에서.
- **6개월 영향력**: 중간 — 중국권에서 "무한 캔버스 + MCP 에이전트"가 오픈소스 표준 UI로 굳으면 상용 캔버스형 툴(이미지/영상)의 기능 하한선이 올라감.
- **대체 관계**: [[ComfyUI]](노드 그래프, 로컬 모델 실행)의 **API 소비형·브라우저형** 대안. [[artcraft]](입력 통제 IDE)와 같은 "프롬프트 너머 제작 UI" 계열.
- **허와 실**: 실 = 캔버스 편집기 + 커스텀 호출 스크립트(중계상별 API 차이 흡수) + 프롬프트 라이브러리 7개 소스 + MCP 에이전트 브리지. 허 = 품질은 전적으로 연결한 외부 모델 몫, 프로젝트 자체 가치는 UI·오케스트레이션.
- **액션**: star만 + 문서 `docs/content/docs/canvas/canvas-node-manual.mdx`·`canvas-agent/agent-instructions.md` 열람(실행 없이)으로 **에이전트가 캔버스를 조작하는 MCP 툴 표면**을 영상 SaaS 설계 레퍼런스로 수집.

### video-saas 템플릿 (요약)
- **기능 벤치마킹**: 노드 캔버스 + "선택 노드·상위 노드 맥락으로 대화/생성 후 결과를 캔버스에 되삽입"하는 캔버스 어시스턴트가 핵심 UX. 구현 스택은 Vite 7 + React Router 7 + Bun, 저장은 IndexedDB.
- **경쟁 우위 빈틈**: 모델 무관·중계 의존 구조라 **결과 품질·일관성 보장**이 비어 있음 — 영상 SaaS가 메울 자리.

## 관련 페이지
- [[ComfyUI]] · [[artcraft]] · [[video-saas]]
- [[에이전트-스킬]] · [[Claude-Code-워크플로우]] · [[openai-codex]]
- 같은 배치: [[experiential]] · [[sandbox-runtime]] · [[claude-seo]] · [[gstack]]
- 중계/라우터 층 비교: [[freellmapi]] · [[OmniRoute]]
- [[ai-news]]

## 원본
- 출처: https://github.com/basketikun/infinite-canvas · README raw 14,662 B · homepage canvas.best
- 볼트 실측(GitHub API, 2026-10-26T09:07Z): ★9,165(수집기 9,164, +1) · fork 2,144 · open issues 19 · MIT · TypeScript · created 2026-05-18 · pushed 2026-10-25T11:21Z · `canvas-agent/`·`plugins/`·`canvas-proxy/` 디렉터리 실재
- 신뢰도: ⭐ (개발 단계 · 수치 근거 0 · 스폰서/중계 의존)
