---
title: "KKKKhazix/agent-autoloop — CLI 에이전트를 이벤트로 깨워 한 라운드 돌리고 종료, 애매하면 메신저 카드로 묻는다. 대기 중 토큰 0"
type: source
domain: local-llm
tags: [local-llm, github-trending, agent-orchestration, cron, human-in-the-loop, claude-code, codex, typescript, mit]
created: 2026-11-09
updated: 2026-11-09
sources: [https://github.com/KKKKhazix/agent-autoloop]
reliability: medium
---

**GitHub**: [KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop) · ★**4,204**(볼트 11-09 API · 수집기 4,022 → +182/1일) · 포크 764 · 이슈 3 · MIT · TypeScript · created 2026-11-03(6일차) · Node 24+

## 핵심 인사이트
> [!insight] "에이전트 상주"가 아니라 "이벤트 → 1라운드 → 종료 → 승인 대기(프로세스 0) → 세션 재개"
> 의존성 없는 스케줄링 커널 + 플러그인(이벤트 소스·에이전트·알림 채널·배포). 크론·GitHub 이슈·에러 보고를 규칙대로 배정, 데이터 삭제·재시작·결제·외부 발송 같은 판단만 Slack·Discord·Feishu 등 카드로 사람에게 확인. **대기 중엔 프로세스·토큰을 쓰지 않는다.** 프롬프트를 받아 마지막 답을 출력하는 CLI 면 SDK 없이 연결.

> [!note] 이 볼트 자체의 운영 구조와 같은 모양
> 이 위키 인제스트도 크론이 CLI 에이전트를 깨워 한 라운드 처리하고 Telegram 으로 보고하는 구조다. 차이는 autoloop 의 **"애매할 때만 묻는 카드 + 원래 세션 재개"** — 지금 볼트 루프엔 중간 승인 경로가 없다.

## 도메인별 추출 (local-llm)
- **실용성**: 로컬 PC 한 대(클라우드·공인 포트 불필요). 지연시간 수치 없음
- **Hermes 적용**: YES 후보 — ChinameBot 의 장시간 작업을 "이벤트 → 1라운드 → 승인 카드" 로 돌리는 패턴 참고. 단 문서 중국어 중심, 6일차 레포
- **트레이드오프**: 무인 운영 ↔ 승인 규칙을 잘못 쓰면 위험 행동이 카드 없이 실행될 수 있음(규칙 품질 의존)
- **오픈소스 구현체**: YES (MIT)

## 관련 페이지
- [[AI-에이전트-프레임워크]] · [[하네스-설계-축]] · [[Paradev]](11-08 — CLI 에이전트 병렬) · [[Mika]]

## 원본
- 출처: https://github.com/KKKKhazix/agent-autoloop
- 확인 범위: GitHub API(볼트 11-09) · README 미정독 · 실행 0회
- 신뢰도: ⭐⭐ (★4.2K · 6일차 · 수치 0)
