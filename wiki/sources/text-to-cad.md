---
title: "text-to-cad — CAD/CAE/CAM 에이전트 스킬 라이브러리"
type: source
domain: ai-news
tags: [ai-news, github, agent-skills, cad, robotics, urdf, gcode, 3d-printing]
created: 2026-09-10
updated: 2026-09-10
sources: []
reliability: high
---

# text-to-cad

> [!insight] 핵심 인사이트
> **스킬 11종**으로 로컬 프로젝트 파일에서 CAD·로봇기술파일을 생성/검사/슬라이싱한다. 중요한 건 범위가 **설계에서 끝나지 않는다**는 점 — G-code는 **실제 슬라이서 CLI**로 프린터 프로파일까지 검증하고, Bambu Lab **실기 출력 작업 시작**까지 간다.
> → **에이전트 스킬이 "텍스트 생성"에서 "물리적 결과물"로 넘어간 경계 사례.** 잘못된 출력의 비용이 토큰이 아니라 **필라멘트와 시간**이다.

> [!note] 스킬 11종 (README 표 실측, 69–81행)
> `CAD` · `CAD Viewer` · `step.parts` · `DXF` · `URDF` · `SRDF` · `SDF` · `SendCutSend` · `DfAM Check` · `G-code` · `Bambu Labs`
> - **STEP을 주 출력**으로 STL/3MF/GLB 내보내기
> - **URDF/SRDF/SDF** → MoveIt2·시뮬레이터 연결 (로봇 기술파일 3종 세트)
> - `DfAM Check` — 벽두께·오버행·서포트 부피·빌드 방향으로 **출력 가능성 정량 측정**
> - 각 스킬 `requirements.txt` 가 발행 당시 `cadgen` 릴리스를 **핀 고정**
> → raw의 "11종" 표기 **원문 대조 확인**.

> [!warning] 🔴 설치 함정 — README가 직접 경고하는 조용한 실패 3종
> ① **`npx skills update` 는 락파일에 있는 스킬만 갱신해 신규 스킬을 조용히 누락**한다(103–104행 원문: *"silently misses new ones — which matters here, because releases do add skills"*). 정답은 **`add` 재실행**(overwrite 방식).
> ② **두 명령 모두 상류에서 폐기된 스킬을 제거하지 않는다**(107행). `npx skills remove <skill>` 수동 필요.
> ③ **raw가 놓친 세 번째** — Codex 플러그인은 **0.142.0 이상에서만** 해석된다. 구버전에서는 *"조용히 건너뛰어 `codex plugin list` 에 아예 나타나지 않는다"*(124행).
> → **세 실패가 전부 "조용하다".** 에러가 없으니 사용자는 최신 상태라고 믿는다. → [[측정도구-먼저-반증]] 의 설치 계층 판본.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐**15,249**(실측 2026-09-10, raw 15,244 대비 +5) · 포크 1,570 · 이슈 21 · **MIT** · Python · 생성 2026-04-22 · pushed 2026-09-10. 5개월에 15K — 실사용 견인.
- **즉시 활용**: **NO.** CAD·3D프린팅은 내 도메인이 아니고 장비도 없다. 다만 **스킬 패키징 방식은 즉시 참고 대상**.
- **6개월 영향력**: 직접 영향 낮음. 간접적으로는 **"스킬 라이브러리"라는 배포 단위**가 표준화되는 흐름의 증거 — [[openai-plugins]]·[[teamai-cli]] 와 같은 방향.
- **대체 관계**: 없음(도메인 비중첩).
- **허와 실**: 과장 없음. 오히려 **README가 자기 함정을 먼저 밝히는** 드문 사례로, 신뢰도를 올리는 요소.
- **액션**: 설치 불필요. **`requirements.txt` 릴리스 핀 고정 + 조용한 실패 3종 경고**를 내 스킬 문서 규약에 반영.

> [!action] 당장 할 것
> 내 스킬들에 **버전 핀 고정**이 없다. `cadgen` 식으로 **발행 시점 의존성을 고정**하는 방식 도입 검토 — 지금은 상류가 바뀌면 조용히 깨진다.

## 관련 페이지
- [[에이전트-스킬]]
- [[측정도구-먼저-반증]]
- [[openai-plugins]]
- [[teamai-cli]]
- [[Pascal-Editor]]
- [[AI-3D-생성]]
- [[임바디드-AI]]

## 원본
- 출처: https://github.com/earthtojake/text-to-cad
- 실측(2026-09-10): ⭐**15,249** · 포크 1,570 · 이슈 21 · MIT · pushed 2026-09-10T07:15:08Z · Python
- **README 원문 대조: 스킬 11종 표 확인 · 조용한 실패 3종 확인(raw는 2종만 기재)**
- raw 대비 드리프트: 스타 +5(자연 증가) · **볼트가 실패모드 1건 추가 발견**
- 신뢰도: ⭐⭐⭐ (MIT · 15K · 자기 함정 명시 · 실행 검증까지 포함)
