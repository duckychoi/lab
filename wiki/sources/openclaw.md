---
title: openclaw — 크로스 OS 개인 AI 어시스턴트 (★391,087 · 볼트 최대 누락)
type: source
domain: ai-news
tags: [ai-news, github-trending, assistant, own-your-data, cross-platform, 선발창-누락, mit]
created: 2026-10-01
updated: 2026-10-01
sources: []
reliability: high
---

# openclaw/openclaw

> [!insight] 핵심 인사이트
> **★391,087 · fork 82,233 인 저장소가 볼트 1,191개 소스 페이지 어디에도 없었다.** 이것이 이 항목의 가장 중요한 사실이며, 소프트웨어에 관한 사실이 아니라 **볼트 선발 파이프라인에 관한 사실**이다. 09-27 에 기록한 [[tensorflow]] ★200,524 누락보다 **1.95배 크다** → [[선발창-누락]] **최대 사례로 확정**.
> 🎯 **왜 놓쳤는지가 명확하다: 볼트는 "당일 증분" 과 "트렌딩 랭크" 로만 선발해 왔다.** openclaw 의 당일 증분은 **+136**(오늘 5건 중 최저)이고 트렌딩 7위다. **증분 기준으로는 영원히 선발되지 않는 종류의 거대 저장소**다 — 이미 커서 하루 증가율이 0.03%에 불과하기 때문이다.

> [!note] 배경 정보
> 설명문: *"The AI that really does things. Any OS. Any Platform. The lobster way. 🦞"*. topics 7종 = `ai` · `assistant` · `crustacean` · `molty` · `openclaw` · `own-your-data` · `personal`. 생성 2025-11-24 → 약 10개월에 ★391K. 데이터 소유권을 사용자 기기에 두는 범용 어시스턴트 포지셔닝.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — GitHub API 직접 실측(★391,087 · fork 82,233 · 생성일 · topics · 라이선스 전문). 단 **기능 주장은 README 미열람**이라 설명문·topics 수준까지만.
- **즉시 활용**: NO (현 시점) — 볼트의 당면 병목은 [[Hermes]] 메모리와 렌더 파이프라인이고 범용 어시스턴트는 그 축이 아니다. 🔴 **단 이 "NO" 는 10개월간 검토조차 안 한 뒤의 NO 라서 신뢰도가 낮다.**
- **6개월 영향력**: ★391K · fork 82K 규모는 **생태계 기본값(default)을 정의하는 급**이다. fork/star 비 **21.0%** 는 오늘 5건 중 최고(openrig 6.8% · VoiceStudio 11.1%)로, **읽히는 저장소가 아니라 가져가 고치는 저장소**임을 시사.
- **대체 관계**: 미판정 — [[openrig]]·[[jcode]] 류 로컬 하네스와 겹치는지 README 없이 단정 불가.
- **허와 실**: 🔴 **"Any OS. Any Platform." 은 설명문 주장이며 볼트 검증 0.** 이슈 5,857건(순수)의 성격도 미조회.
- **액션**: README 열람 + [[openrig]] 와의 기능 중첩 판정 → actionable 최우선 등록([[유예-은폐]] 규칙 3 적용).

## 🔓 라이선스 봉인 해제 — 수집기 "실제 라이선스 미확인" 을 1회 조회로 해소

> [!warning] 수집기: *"라이선스가 `NOASSERTION`(SPDX 미인식)이라 **실제 라이선스 미확인**"*
> ✅ **볼트 실측 — LICENSE 전문 1,170B 확보: 1행이 문자 그대로 `MIT License`, 3행 `Copyright (c) 2026 OpenClaw Foundation`, 표준 MIT 전문 그대로.**
> 🔴 `NOASSERTION` 의 원인은 **말미 추가 2행**이다: *"Third-party notices for incorporated or adapted code are recorded in THIRD_PARTY_NOTICES.md."* 표준 문구 이탈 → GitHub `licensee` 탐지기가 `Other` 로 분류.
> ⚖️ **판정: 실질 MIT + 제3자 고지 참조 1문단.** 수집기의 *"미확인"* 은 **탐지기 라벨을 세계에 대한 사실로 승격**한 것 → [[메타데이터-부재-추론]] · [[유예-은폐]].

## 지표 분해 (2026-10-01 09:21 UTC 실측)

- ★ **391,087** (수집기 09:0x 391,078 → 드리프트 **+9**) · fork **82,233**(완전 일치) · 생성 2025-11-24 · 당일 푸시
- `open_issues_count` **9,146** → 🔴 **분해 실측: 순수 이슈 5,857 + PR 3,289**([[복합지표-분해]])
  - 수집기식 비율 2.34% → **순수 이슈 비율 1.50%** · PR 비중 36.0%
- topics **7종** — ★391K 규모에서 7종은 빈약하나 0종은 아님([[메타데이터-부재-추론]] 중간값)

## 관련 페이지
- [[선발창-누락]] ← **최대 사례**
- [[복합지표-분해]] · [[유예-은폐]] · [[메타데이터-부재-추론]]
- [[openrig]] · [[paperclip]] · [[tensorflow]]
- [[OpenClaw-Foundation]] · [[ai-news]]

## 원본
- 출처: https://github.com/openclaw/openclaw
- 실측(2026-10-01 09:21 UTC): ★391,087 · fork 82,233 · issue 5,857 + PR 3,289 · 생성 2025-11-24
- 라이선스: **실질 MIT**(전문 확인) · GitHub 탐지 `NOASSERTION`
- 신뢰도: ⭐⭐⭐ (수치·라이선스 직접 실측) / 🔴 기능 주장은 README 미열람
