---
title: "ethanplusai/sellbird — 구독 플랜(Claude Code · Codex)으로 돌리는 콜드메일 영업 에이전트 (구 Harvey)"
type: source
domain: ai-news
tags: [ai-news, github-trending, sales-agent, cold-email, claude-code, agpl]
created: 2026-11-19
updated: 2026-11-19
sources: [https://github.com/ethanplusai/sellbird]
reliability: medium
---

**GitHub**: ★6,580(볼트 API 11-19 · 수집기 6,579 · Python 일간 +237) · **AGPL-3.0** · Python · 생성 2026-03-12 · HEAD b212385(11-18)

## 핵심 인사이트
> [!insight] "API 키 없이" = 구독 플랜을 자동화 엔진으로 쓴다
> 회사 탐색(OpenStreetMap) → 웹사이트 구매 신호 추출(모델 호출 없음) → 의사결정자 · 이메일 패턴 추정 + 1건 검증 → 개인화 시퀀스 → Gmail/M365/SMTP 발송 → 답장 분류. LLM 호출은 **Claude Code CLI(Pro/Max) 또는 Codex(ChatGPT 플랜)**. 비용 구조가 매력이지만 **구독 플랜의 자동화 사용이 각 사 약관에 맞는지는 확인되지 않았다**(수집기 · 볼트 모두 미확인).

> [!warning] 책임이 사용자에게 있는 부분
> - 스팸 규제(한국 정보통신망법 영리 광고성 정보 사전 동의 포함)는 도구가 해결하지 않는다. README 는 수신거부 처리를 명시(수집기 판독).
> - 기본값은 사람 승인 전 발송 안 함 — 이 기본값을 유지할 것.
> - AGPL-3.0: 수정해 SaaS 로 제공하면 소스 공개 의무.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐ — 개인 레포 · 효과 수치(응답률 등) 0.
- **즉시 활용**: NO — 볼트 사용자 업무에 B2B 아웃바운드가 없다. 구조(신호 추출은 규칙, 작문만 LLM)는 참고 가치.
- **대체 관계**: 유료 세일즈 SaaS(Apollo 류)의 셀프호스트 대안.
- **허와 실**: "에이전트"의 실체는 파이프라인 + 승인 게이트.

## 관련 페이지
- [[Claude-Code-워크플로우]] · [[AI-에이전트-프레임워크]] · [[openworker]] (승인 사다리 비교)

## 원본
- 출처: https://github.com/ethanplusai/sellbird
- 확인 범위: GitHub API(스타 · 라이선스 · 생성일 · push) · 🔴 README 파이프라인 · 승인 기본값은 수집기 판독
- 신뢰도: ⭐⭐
