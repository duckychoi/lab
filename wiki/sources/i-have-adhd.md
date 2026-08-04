---
title: i-have-adhd — 코딩 에이전트 응답을 간결·실행중심으로 재구성하는 스킬
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, prompt-engineering, claude-code, ux]
created: 2026-07-22
updated: 2026-07-22
sources: []
reliability: high
---

# i-have-adhd (ayghri/i-have-adhd)

> [!insight] 핵심 인사이트
> ⭐**7,400 (2026-07-22, 당일 +1,866 급상승)**, Python 95.7%. 코딩 에이전트(Claude Code 등)의 응답을 **10개 포맷 규칙**으로 재구성하는 **에이전트 스킬**. "Great question! Let me think…" 같은 서론을 걷어내고 **다음 실행 행동을 맨 앞에**, 멀티스텝은 번호 매김, 리스트는 5개 상한, 불필요한 맺음말 제거. 예: 장황한 설명 대신 `Run npm install jsonwebtoken@latest, then edit src/auth.ts:42`. [[Addy Osmani]]의 [[agent-skills]]·[[Anthropic]] 스킬 계보에서 **"에이전트 출력 UX"** 를 정조준한 축 — 능력이 아니라 **응답 밀도/신호대잡음비**를 개선한다.

> [!note] 배경 정보
> 흥미로운 메타 아이러니: 이 위키를 갱신하는 나(에이전트) 자신이 장황함에 빠지기 쉬운 대상이다. i-have-adhd는 "모델을 바꾸지 않고 **출력 규칙만으로** 실사용 만족도를 올린다"는, 프롬프트/스킬 레이어의 저비용 고효율 개입 사례. 당일 +1,866은 "AI가 말이 너무 많다"는 광범위한 사용자 불만의 실질 신호.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — WebFetch 실확인(⭐7.4k·Python 95.7%, raw 수치와 일치). 스킬 자체는 규칙 텍스트라 실체 검증 용이. reliability **high**.
- **즉시 활용**: YES — 규칙 10개는 [[Claude-Code-워크플로우]]·[[reat-script]]류 생성물 톤 가이드로 즉시 이식 가능. 무인 크론 리포트(예: 이 log/domain 요약)의 **서론 제거·행동 우선** 원칙으로 채택 검토.
- **6개월 영향력**: "에이전트 능력 경쟁"과 별개로 **출력 스타일 스킬** 시장이 형성되는 신호. 모델 무관 규칙 레이어라 어떤 벤더에도 얹힌다.
- **대체 관계**: 커스텀 시스템 프롬프트/스타일 가이드를 재사용 가능한 스킬로 패키징. [[agent-skills]]와 같은 레이어.
- **허와 실**: "ADHD" 네이밍은 마케팅 — 실제는 범용 간결화 규칙. 과도 적용 시 필요한 맥락까지 잘릴 위험(설명이 정말 필요한 경우와의 균형은 사용자 몫).
- **액션**: 규칙 10개를 읽고 이 위키 자동 리포트(log 한 줄·domain 요약)에 "행동 우선·서론 제거" 2~3개만 선별 적용해 가독성 A/B.

## 관련 페이지
- [[agent-skills]]
- [[Addy Osmani]]
- [[Anthropic]]
- [[Claude-Code-워크플로우]]
- [[ai-news]]

## 원본
- 출처: https://github.com/ayghri/i-have-adhd
- GitHub: ⭐7,400 (2026-07-22, 당일 +1,866), Python 95.7% — WebFetch 실확인
- 신뢰도: ⭐⭐⭐ (WebFetch 검증, 스킬 규칙 텍스트로 실체 명확)
