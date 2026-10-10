---
title: "text-to-cad — CAD/CAE/CAM 에이전트 스킬 라이브러리"
type: source
domain: ai-news
tags: [ai-news, github, agent-skills, cad, robotics, urdf, gcode, 3d-printing]
created: 2026-09-10
updated: 2026-10-10
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

---

## 📥 2026-10-05 재관측 (자동수집 10-05 배치 · 갱신)

**볼트 독립 실측 2026-10-05**: ★**17,036** · fork **1,754** · open_issues **34** · **MIT** · pushed **2026-10-05**
**드리프트**: 수집기 ★17,034 → 볼트 **+2** · fork·issue·라이선스·pushed **전건 일치**
**수집기 보고**: 당일 **+83** · 트렌딩 5위 · 생성 2026-04-22

> [!insight] 🎯 배치에서 **검증 가능성이 가장 높은 항목**이다
> 의존 스택이 전부 공개된다: **build123d 0.11 · Open CASCADE 7.9 · Python 3.11+ · PyPI `cadgen`**. 출력이 **STEP·GLB·STL·3MF** 실제 제조 포맷이고 **DFM 검사·도면 생성**까지 한다.
> 📌 **이 배치 13건 중 "주장이 맞는지 10분 안에 확인 가능한" 유일한 항목이다** — `pip install cadgen` → 1개 생성 → STEP 파일을 열면 끝난다. ⚖️ **[[ponytail]]·[[impeccable]] 은 효과를 재려면 비교 실험이 필요하고, 이것은 산출물 존재만 보면 된다.**

> [!insight] 🏆 [[SimuVerity]] 와 같은 문제를 반대쪽에서 다룬다
> SimuVerity(같은 배치)는 **Simulink 모델이 "실행되지만 공학적으로 부적격"** 한 비율을 쟀다(실행 86.47% → 자격 **76.90%** → 최종 **42.86**).
> 🎯 **text-to-cad 의 DFM 검사가 바로 그 ③ 자격 게이트다** — *"파일이 나왔다"*(①) 와 *"제조 가능하다"*(③)를 분리한다. ⚖️ **벤치마크 논문이 필요하다고 결론 낸 층을 이 레포는 제품 기능으로 갖고 있다.**
> 🔴 **그러나 DFM 검사의 정확도 수치는 README 에 없다**(수집기 미보고 · 볼트 미확인) ⇒ **검사기를 검사할 수단이 없다** → [[측정도구-먼저-반증]].

> [!action] 당장 할 것 (우선순위 **높음** — 배치 최저 문턱)
> `pip install cadgen` 후 **STEP 1건 생성 + DFM 검사 1회**. 🎯 **볼트 코드 실행 0건이 17배치 연속인데, 이 배치에서 가장 싼 깨기 수단이다**(로봇 불필요 · GPU 불필요 · API 키 불필요).

**검증**: `api.github.com/repos/earthtojake/text-to-cad` 실측
**관련 추가**: [[SimuVerity]] · [[측정도구-먼저-반증]] · [[검사가능성-공사]]

---

## 🔄 2026-10-06 갱신 (인제스트 2026-10-10)

**★17,630** (볼트 구기록 **★17,036** → **+594**) · 당일 +437 · **트렌딩 3위** · fork 1,779 · watchers 92
**open_issues 35 = 순수이슈 0 + PR 35** · MIT · Python · created 2026-04-22 · pushed 2026-10-06

> [!insight] 🏆🏆 볼트 ★최우선 actionable 1건이 해소됐다 — `cadgen` 은 실존한다
> **PyPI API 직접 조회(HTTP 200)**:
> - `cadgen` **0.7.15** · 릴리스 **53개** · wheel **11,547,471B** · sdist **11,320,523B**
> - 업로드 **2026-10-06**(수집 당일) · MIT · `requires_python >=3.11`
> - summary: *"STEP-first CAD artifact generation runtime: build123d STEP/GLB/topology generation, validation, and inspection for CAD agent skills."*
> - 의존성: **build123d >=0.11.1,<0.12 · cadquery-ocp-novtk >=7.9,<8 · ezdxf · shapely · playwright==1.63.0**
>
> ⇒ ⚖️ **"선언된 구현체 실존"은 확정이고 "실행 성공"은 아니다.** 볼트가 10-05 에 *"산출물 존재만 확인하면 끝"* 이라 적은 **그 범위까지만 해소됐다.**
> 📌 [[선언된-구현체-공백]] **반례** — 빈 레포형이 아니다.

> [!insight] 기능 서술 (갱신)
> 평문/이미지 요청에서 **STEP 을 주 출력**으로 3D 모델을 만들고(STL·3MF·GLB 내보내기), 치수 기입 도면 **PDF·DXF** · **URDF/SRDF/SDF** 로봇 기술 파일 생성과 판금·CNC·사출 **DFM 검토** · OrcaSlicer **G-code** · Bambu 전송까지 **스킬 12종**으로 나눠 제공한다.

> [!warning] 🔴 `has_issues: true` 인데 순수 이슈 0 · PR 35 = open_issues 의 100% 가 PR 이다
> ⇒ 🆕 **[[지표-창길이]] 와 별개 축: `open_issues_count` 는 두 모집단의 합이고 비율이 레포 운영 방식을 드러낸다.**
> 10-06 배치 5건 PR 비중: **100% / 71% / 74% / 54% / 54%** — **text-to-cad 가 극단값**이다.
> 📌 금일(10-10) 배치 분포는 **8.6% / 28.7% / 43.6% / 59.4% / 75.3%** 로 **100% 는 재현되지 않았다.**

> [!warning] 성능·정확도 수치 0개
> 스킬 표는 **기능 서술만**이고 **CAD 생성 성공률·DFM 검출률 측정이 없다.** ★17,630 에 능력 근거 0.

> [!note] 📌 `skills.sh` 배지 보유 = 배포 경로가 수렴한다
> 10-05 기록 때와 동일한 스킬 프레임워크 배포 경로이고, **금일(10-10) 트렌딩 AI 5건 중 3건이 같은 경로**다([[rea]] · [[mattpocock-skills]] · [[diagram-design]]).
> ⇒ ⚖️ **"스킬"이 레포 단위 배포 포맷으로 굳어가는 중이라는 관측의 가장 이른 사례 중 하나.** → [[에이전트-스킬]]

> [!question] 미해결
> - `cadgen` **실행 성공 미확인** — 실존만 확정됐다(`pip install cadgen` 미시도 · `playwright==1.63.0` 핀이 환경 충돌 가능).
> - CAD 생성 **성공률·DFM 검출률** 미측정.
> - 스킬 12종의 **개별 동작 검증** 0건.

## 관련 페이지 (갱신 추가)
- [[선언된-구현체-공백]] — 반례(PyPI 실존 확정)
- [[지표-창길이]] — PR 비중 극단값 100%
- [[에이전트-스킬]] · [[rea]] · [[mattpocock-skills]] · [[diagram-design]] — `skills.sh` 경로
- [[t3code]] · [[knowledge-work-plugins]]

## 원본 (갱신)
- 수집: 2026-10-06 자동수집 (ai-news) · 인제스트 2026-10-10
- 검증: GitHub API 실측 · `open_issues` 분해 35=0+35 검산 통과 · **PyPI API `cadgen` 0.7.15 실존 확정(HTTP 200)**
- 신뢰도: ⭐⭐⭐⭐ (구현체 실존 확정 · 능력 측정 0)
