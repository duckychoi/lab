---
title: "openai/codex-security — 레포·diff 단위 취약점 탐지·검증·패치 CLI/SDK (OpenAI API 과금)"
type: source
domain: ai-news
tags: [ai-news, github-trending, security, sast, openai, ci]
created: 2026-11-12
updated: 2026-11-12
sources: [https://github.com/openai/codex-security]
reliability: medium
---

**레포**: [openai/codex-security](https://github.com/openai/codex-security) · ★**11,978** · fork 954 · Apache-2.0 · TypeScript · created 2026-07-13 · pushed 2026-11-12T08:23Z (GitHub API 볼트 실측 — 수집기 수치와 일치)

## 핵심 인사이트
> [!insight] "찾기"가 아니라 "검증 + 패치 + 기존 수정 검증"까지 한 루프
> `cs scan .` · `--diff origin/main` 으로 PR 단위 스캔 → 후보 취약점 **검증** → 패치 생성 → **기존 수정이 실제로 막았는지 재검증**, `SECURITY.md`·위협 모델 초안, 타 스캐너 결과 가져오기, SARIF/JSON/CSV, Linear/Jira/GitHub 연동, GitHub Action. Deep 모드 = Standard 스캔 반복 + 중복 제거(수집기 판독). ⇒ 정적 분석기(SAST)의 오탐 문제를 **LLM 재검증 단계**로 푸는 구조이고, 이것은 [[shadcn-improve]] 의 "어드바이저 재확인"과 같은 발상이다.

> [!warning] 성능 수치 0 · 과금 · 접근 제한
> README 에 탐지율·오탐률 없음(수집기 판독). `OPENAI_API_KEY`/`CODEX_API_KEY` 필수 = 과금 대상. 일부 요청은 "Trusted Access for Cyber" 승인 필요. Node 22.13+/24/26 + Python 3.10+. Deep 모드는 스캔을 반복하므로 **비용이 반복 횟수에 비례**한다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★11,978 · 당일 +52 · 벤치 없음 · 공식 [[OpenAI]] 레포.
- **즉시 활용**: 조건부 — OpenAI 키가 있으면 볼트 자동화 스크립트(크론·수집기) 레포 1개에 `--diff` 스캔 1회는 저비용 시험. 키 없으면 NO.
- **6개월 영향력**: PR 단위 LLM 보안 검토가 CI 기본 단계가 될 수 있다. 다만 결과의 신뢰도는 측정되지 않았다.
- **대체 관계**: Semgrep/CodeQL 등 규칙 기반 SAST 를 대체가 아니라 **후단 검증기**로 보강(타 스캐너 결과 가져오기 기능이 그 위치를 말해 준다).
- **허와 실**: 기능 목록은 풍부, 정확도 근거는 없다.
- **액션**: 보류 — 성능 수치나 제3자 평가가 나오면 재판정.

## 관련 페이지
- [[OpenAI]] · [[shadcn-improve]] · [[OpenSandbox]](에이전트 실행 격리 — 보안 축의 반대편)

## 원본
- 출처: https://github.com/openai/codex-security
- 확인 범위: GitHub API 메타 · 🔴 README 본문 수집기 판독 기준 · 실행 미확인
- 신뢰도: ⭐⭐ (★11,978 · 측정 0)
