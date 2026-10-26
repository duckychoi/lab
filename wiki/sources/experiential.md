---
title: "experiential — BYOK·로컬·호스티드 모델을 OpenAI 호환 게이트웨이 하나로 묶고, 트래픽으로 '내 라우터'를 학습시킨다는 약속. 라우터 효과 수치는 README에 0개"
type: source
domain: ai-news
tags: [ai-news, github-trending, llm-gateway, llm-router, openai-compatible, budget-control, telemetry, traffic-capture, 오픈코어]
created: 2026-10-26
updated: 2026-10-26
sources: [https://github.com/experientiallabs/experiential]
reliability: medium
---

# experientiallabs/experiential — ★13,040 · Python · Apache-2.0 · 생성 4개월

> [!insight] 핵심 인사이트 — **게이트웨이는 미끼, 상품은 "당신의 트래픽"이다**
> README의 세 기둥 중 1·2(단일 OpenAI 호환 API, 사용자/에이전트별 모델·예산 통제)는 [[litellm]]·[[OmniRoute]]·[[9router]]가 이미 하는 일이다. 차별점은 3번 *"Turn production traffic into a custom router or model"* 하나뿐이고, 이를 위해 README가 사용자에게 요구하는 것은 **트레이스 업로드(telemetry), 데스크톱 앱 트래픽 캡처, 호스티드 플랫폼 가입**이다. ⇒ 이 레포의 구조적 의미는 "라우터"가 아니라 **에이전트 트래픽을 학습 데이터로 수집하는 파이프라인의 입구**다. [[freellmapi]]가 "카탈로그 신선도"를 팔았다면, 여기서는 "트래픽 → 라우터/파인튜닝 모델"을 판다.
> 핵심 약속(비용 절감·품질 향상)을 뒷받침하는 **라우터 효과 수치는 README에 하나도 없다**(수집기 주장 확인). 유일한 숫자는 자체 CI 배지 `gateway latency 30.9 ms`(측정 방법·부하 조건 미기재)와 셋업 기본값 `$50.00` 예산뿐 → [[스타-근거-비동행]].

> [!warning] 검증 안 됨 / 수집기 요약에서 빠진 한정어
> - **"OpenAI·Anthropic 호환"** → [[한정어-탈락]]: 로컬 `exp` 게이트웨이는 README상 *"one OpenAI-compatible API"*. *"(and Anthropic Messages) API"* 는 **호스티드 플랫폼**(`api.experientiallabs.ai/v1`) 설명에만 붙어 있다.
> - **"Claude Code/Codex 트래픽 캡처"** → 원문은 *"Codex and Claude Code **desktop apps** using your existing ChatGPT or Claude **subscription**"*, 요구사항은 macOS + **Python 3.13+** + **확장·인증서 승인**(=TLS 가로채기 구조로 보임, 추정), *"macOS network reliability is still under investigation"*. 구독 트래픽을 제3자 플랫폼 텔레메트리로 보내는 것이 각 구독 약관과 맞는지는 README에 언급 없음.
> - **텔레메트리 기본 ON**: *"Anonymous aggregate PostHog product telemetry is enabled by default"* — 수집기 요약에 없음. 프롬프트·트레이스는 제외한다고 명시. `exp config telemetry disable`.
> - 레포 설명의 *"zero markup"*, *"1000+ marketplace models"* 는 자기 주장, 열람 범위(README)에서 근거 없음 → [[카탈로그-등가가정]].
> - 파인튜닝(`exp optimize model`)은 자체 기능이 아니라 외부 **Tinker**(Thinking Machines) 경유.

## 도메인별 추출 (ai-news)

- **신뢰도**: ★13,040 · fork 267 · open issues 149 · 생성 2026-06-24(4개월) · 논문 없음 · 효과 벤치 0건. fork/★ 비율 2.0%로 낮음 — 써보는 사람보다 저장하는 사람이 많은 패턴.
- **즉시 활용**: **NO(보류)** — 볼트 크론은 Linux 서버인데 차별 기능(캡처)은 macOS 전용·실험적. 게이트웨이·예산 기능만 필요하면 이미 검증된 [[litellm]]으로 충분. 텔레메트리 기본 ON도 무검토 설치를 막는 이유.
- **6개월 영향력**: 중간 — "에이전트별 예산 + 트래픽 기반 라우터 학습"이 실제 절감 수치를 공개하면 게이트웨이 층의 새 기준이 될 수 있음. 공개 전까지는 약속.
- **대체 관계**: [[litellm]]·[[OmniRoute]]·[[9router]]·[[freellmapi]]와 같은 층(모델 게이트웨이/라우터). [[cindy]]·[[openclaw]]는 한 층 위(하네스) → [[하네스-설계-축]]의 "모델 선택" 축을 외부화하는 시도.
- **허와 실**: 실 = OpenAI 호환 로컬 게이트웨이 + 별칭(`opus-5` 등) + identity별 예산 + OTLP 트레이스 기반 `exp build` 시뮬레이션. 허 = "비용 절감·더 나은 모델 추천"의 정량 근거 부재, 공개 데이터셋(HF `wmo-terminal-tasks-traces`)은 데모용.
- **액션**: star만. 라우터 효과 수치(전/후 비용·품질)가 docs나 릴리스에 올라오면 재검토. 설치 시 `exp config telemetry disable` 먼저.

## 관련 페이지
- 같은 층: [[litellm]] · [[OmniRoute]] · [[9router]] · [[freellmapi]]
- 개념: [[하네스-설계-축]] · [[스타-근거-비동행]] · [[한정어-탈락]] · [[카탈로그-등가가정]]
- 같은 배치: [[sandbox-runtime]] · [[claude-seo]] · [[gstack]] · [[infinite-canvas]]
- [[Claude-Code-워크플로우]] · [[ai-news]]

## 원본
- 출처: https://github.com/experientiallabs/experiential · README raw 5,590 B
- 볼트 실측(GitHub API, 2026-10-26T09:07Z): ★13,040(수집기 13,038, +2) · fork 267 · open issues 149 · Apache-2.0 · Python · created 2026-06-24 · pushed 2026-10-25T17:19Z
- 신뢰도: ⭐⭐ (★1.3만이나 핵심 약속의 근거 수치 0)
