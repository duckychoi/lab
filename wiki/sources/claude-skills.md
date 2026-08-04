---
title: claude-skills — 13개 코딩 에이전트용 통합 스킬·플러그인 저장소
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, claude-code, plugins, marketplace]
created: 2026-07-06
updated: 2026-07-06
sources: []
reliability: high
---

# alirezarezvani/claude-skills (GitHub ⭐20,831)

**GitHub**: https://github.com/alirezarezvani/claude-skills
**스타수**: 20,831 (2026-07-06 기준, 당일 +392)

> [!insight] 핵심 인사이트
> Claude Code·Codex·Gemini CLI·Cursor 등 **13개 코딩 에이전트**에서 쓰는 스킬·플러그인·페르소나 355종을 한 레포에 모은 통합 마켓플레이스. 핵심 차별점은 "**하나의 레포, 13개 플랫폼**" — 602개 Python 도구가 전부 stdlib-only(pip 설치 0)라 어디서든 돌아가고, `scripts/convert.sh`로 벤더 포맷 변환. [[agentskills]] 규격·[[mattpocock-skills]] 개인 배포·[[superpowers]] 방법론에 이은 "스킬을 **크로스벤더 배포 단위**로 굳히는" 흐름의 결정판.

## 핵심 인사이트

> [!note] 구성 (README 실측)
> - **Skills 355** — SKILL.md(워크플로우·결정 프레임워크) + Python 도구 602개(stdlib-only) + 레퍼런스 문서 711종
> - **Agents 97 / Personas 7 / Commands 103** — 스킬(어떻게 실행)·에이전트(무엇을)·페르소나(누가 사고)를 3층으로 분리, [[SkillCoach]]식 "실제 잘 쓰이는가" 관점과 공명
> - 커버리지: 엔지니어링·DevOps·마케팅(AEO)·보안(PreToolUse 훅)·컴플라이언스·C레벨 자문·학술 리서치 스택
> - 라이선스 **MIT**, SkillCheck 검증 배지

> [!warning] 수치 불일치 (실측 검증 원칙)
> README 자체 배지는 "5,200+ stars / 355 skills"로 표기되나 자동수집 라이브 스타는 **20,831**(당일 +392) — README 배지가 낡았거나 다른 지표. "가장 포괄적"·"production-ready"는 자가 홍보 문구이므로 스킬 품질은 개별 확인 필요. 스킬 **개수 자체가 품질을 보증하지 않음** — [[caveman]]식 자가제출 수치 노이즈와 같은 계열.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ (⭐20,831 당일 급상승, MIT, 실측 fetch로 구성 확인)
- **즉시 활용**: 부분 YES — stdlib-only Python 도구라 의존성 지옥 없이 발췌 이식 가능. 단 355종 전부가 아니라 내 도메인(영상/로컬LLM/위키)에 맞는 소수만 선별해야 스킬 남발 방지.
- **6개월 영향력**: 스킬이 벤더별 포맷을 넘어 `convert.sh`로 이식되는 "스킬 패키지 매니저" 패턴이 정착하면, 내 `.claude/skills`도 크로스벤더 호환 포맷 정렬 압력.
- **대체 관계**: [[mattpocock-skills]](개인 TS 편향)보다 도메인 폭이 넓고, [[agentskills]](규격만)보다 실물 스킬이 많음 — "규격+실물"의 중간.
- **허와 실**: 마케팅 걷어내면 = 잘 정리된 대형 스킬 카탈로그. 진짜 가치는 "stdlib-only + 13플랫폼 변환"이라는 이식성 설계.
- **액션**: 클론 후 보안(PreToolUse 훅)·리서치 스택 스킬 2~3개만 발췌 검토.

## 관련 페이지
- [[agentskills]] — 벤더 간 스킬 규격
- [[mattpocock-skills]] — 개인 스킬 배포 레포
- [[superpowers]] — Claude 공식 방법론 스킬
- [[SkillCoach]] — 스킬 사용 능력 평가
- [[caveman]] — 자가제출 수치 노이즈 사례
- [[Claude-Code-워크플로우]]
- [[ai-news]]

## 원본
- 출처: https://github.com/alirezarezvani/claude-skills
- GitHub: ⭐20,831 (2026-07-06, 당일 +392), MIT
- 구성(README): Skills 355 · Agents 97 · Personas 7 · Commands 103 · Python 도구 602(stdlib-only)
- 신뢰도: ⭐⭐⭐⭐ (라이브 스타 급상승, 구성 실측 확인 / 품질·README 배지 수치는 개별 검증)
