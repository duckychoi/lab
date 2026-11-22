---
title: "mjmirza/app-store-compliance — 앱스토어 제출 전 반려 위험을 스캔해 제출 명령을 막는 가드 + 에이전트 스킬 (정확도 수치 0 · 비표준 라이선스)"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, hook, ios, android, compliance]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/mjmirza/app-store-compliance]
reliability: medium
---

**GitHub**: ★3,595(볼트 API 11-22 09:04Z · 수집기 11-21 2,968 → 하루 +627) · Shell · 라이선스 GitHub 표기 NOASSERTION(OpenRoots Agent License 2.3) · 생성 2026-06-06 · 수집기 확인 HEAD `d2156bab9d`

## 핵심 인사이트
> [!insight] 스킬이 "조언"이 아니라 "제출 명령 전 훅"으로 들어간다
> iOS/Android 프로젝트 폴더를 bash 로 스캔해 `BLOCKED / CLEAR / NOT CHECKED` 를 내고, Claude Code · Codex · Gemini CLI · Cursor 등 13개 코딩 에이전트에 훅 + 스킬로 설치(`install.sh --tool all`)해 치명 위험이 있으면 제출 명령을 막는다. [[에이전트-스킬]] 이 지침 문서에서 **차단 게이트**로 옮겨 가는 사례다. `NOT CHECKED` 를 별도 상태로 둔 점(확인 못 한 것을 통과로 치지 않음)은 볼트 규약과 같은 방향.

> [!warning] 측정 없음 · 라이선스 비표준
> - README 자칭 수치는 반려 패턴 117개 · 추적 기한 95건(EU AI Act · DSA · COPPA 등)뿐 — **탐지 정확도 · 오탐률 0건**(수집기 판독).
> - 코드 스캔은 개발자 계정 상태 · 약관 동의를 볼 수 없다고 README 가 명시.
> - **OpenRoots Agent License 2.3**: 연매출 2,000만 달러 이하 · 개인 · 비영리 무료, 초과분 0.5% 로열티(연 25만 달러 상한), **AI 학습 용도는 별도 Compute 라이선스**. OSI 표준 아님.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐ — 1인 유지보수 · 효과 수치 0 · 스타는 하루 +627 로 빠르게 증가.
- **즉시 활용**: 🟡 앱 제출 계획이 있을 때만. 볼트 사용자의 현재 작업(영상 SaaS · 웹)에는 직접 해당 없음.
- **6개월 영향력**: "제출/배포 직전 훅으로 막는 스킬" 양식이 다른 규제 영역(결제 · 개인정보)으로 번질 수 있다.
- **대체 관계**: 수동 체크리스트 대체. 심사 결과 자체는 보증하지 않는다.
- **허와 실**: 패턴 수(117)는 커버리지의 크기이지 정확도가 아니다.
- **액션**: 관찰.

## 관련 페이지
- [[에이전트-스킬]] · [[SkillEvaluator]] · [[Claude-Code-워크플로우]] · [[ai-news]]

## 원본
- 출처: https://github.com/mjmirza/app-store-compliance
- 확인 범위: GitHub API(스타 · 언어 · 라이선스 표기 · 생성일) · 🔴 README 내용 · 라이선스 조항은 수집기 판독, 실행 0
- 신뢰도: ⭐⭐
