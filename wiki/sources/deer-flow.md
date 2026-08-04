---
title: bytedance/deer-flow
type: source
domain: ai-news
tags: [ai-news, agent, superagent, bytedance, web-research, coding, sandbox]
created: 2026-04-20
updated: 2026-08-02
sources: []
reliability: high
---

# bytedance/deer-flow

> [!update] 2026-08-02 갱신 — ⭐78,859 (당일 +209)
> ⭐**78,859**(2026-08-02 자동수집, 당일 +209) ← 76,695(07-10). 3주 새 +약2,160으로 7만대 후반 진입, 일 +200대 안정 성장 지속 — DeerFlow 2.0(멀티에이전트·지속메모리·샌드박스·Telegram/Slack 연동) 슈퍼에이전트 하네스로서 기업급 표준 후보 지위 유지. 구성 동일. reliability high 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(볼트 시뮬레이션 타임라인 유지).*

> [!insight] 핵심 인사이트
> ByteDance가 공개한 장기 작업 수행 SuperAgent — 웹 리서치·코딩·콘텐츠 생성을 샌드박스 환경에서 자율 처리. ⭐74,211 (2026-06-24, 당일 +739; ⭐65,770→74,211 누적 +13%)로 deer-flow는 OpenAI의 Swarm, Anthropic의 Claude Code와 동급 공식 에이전트 프레임워크로 포지셔닝. 7만대 스타에서 일 +700대 안정 성장 — 기업급 SuperAgent 표준 후보 지위 굳힘.

> [!note] 2026-07-10 갱신 — ⭐76,695 (당일 +136), 제작 [[ByteDance]]
> WebFetch README 실측: **DeerFlow 2.0**은 기존 딥리서치 프레임워크를 **바닥부터 재작성**해 "리서치 툴 → 범용 슈퍼에이전트 하네스"로 전환됨을 확인. 실측 스펙: ①**멀티에이전트 오케스트레이션**(병렬 서브에이전트 스폰), ②세션 간 **지속 장기 메모리**, ③파일시스템 접근 격리 **샌드박스 실행**, ④태스크별 **스킬 시스템**(점진적 스킬 로딩), ⑤OpenAI 호환 다중 LLM, ⑥Web UI + 터미널 워크벤치(TUI) + 임베디드 Python 클라이언트, ⑦**Telegram·Slack·Feishu·WeChat** 등 메신저 연동, MIT·Python 77%/TS 16%. → "분·시간 단위 롱호라이즌 태스크를 분해·협조"라는 방향이 내 위키 자동수집 오케스트레이터 후보로 격상(⑦ Telegram 연동은 내 스케줄 실행 환경과 직접 접점).

## 도메인별 추출

**신뢰도**: ⭐⭐⭐⭐⭐ (ByteDance 공식 레포, ⭐65,770, 오늘 +190)
**즉시 활용**: YES — 웹 리서치 자동화, 장기 코딩 태스크에 즉시 투입 가능
**6개월 영향력**: SuperAgent 패러다임(단일 에이전트→복합 에이전트 루프)의 기업급 구현체 표준 후보
**대체 관계**: perplexity-deep-research, OpenAI Deep Research의 오픈소스 대안
**허와 실**: 62K 스타는 확실히 주목도 높음. 실제 성능은 오픈소스 특성상 클로즈드 대비 차이 있을 수 있음
**액션**: GitHub 클론 후 웹 리서치 에이전트 테스트

## 주요 기능

- 웹 검색 + 콘텐츠 수집 자동화
- Python 코딩 작업 샌드박스 실행
- 장기 멀티스텝 태스크 지속 수행
- 콘텐츠 생성 파이프라인 내장

> [!action] 당장 할 것
> deer-flow 로컬 설치 후 "AI 뉴스 자동 요약 + 위키 인제스트" 파이프라인에 연결 가능성 검토

## 관련 페이지

- [[ByteDance]] — 제작사
- [[AI-에이전트-프레임워크]]
- [[herdr]] · [[orca]] — 에이전트 오케스트레이션/병렬 관제(비교군)
- [[openai-agents-python]]
- [[hermes-agent]]

## 원본

- 출처: https://github.com/bytedance/deer-flow
- 스타: ⭐78,859 (2026-08-02 자동수집, 당일 +209) ← ⭐76,695 (2026-07-10, 당일 +136) ← ⭐74,211 (2026-06-24) ← ⭐65,770 (2026-04-20)
- 제작: [[ByteDance]] · 라이선스 MIT · Python 77%/TS 16%
- 신뢰도: ⭐⭐⭐⭐⭐ (README WebFetch 실측)
