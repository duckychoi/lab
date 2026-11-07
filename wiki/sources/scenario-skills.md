---
title: "scenario-labs/skills — Scenario MCP 경유 이미지·영상·3D 생성 스킬 175개. 핵심은 '생성 전 견적(dry-run)'"
type: source
domain: video-saas
tags: [video-saas, ai-news, github-trending, agent-skills, mcp, scenario, image-generation, video-generation, 3d, cost-control]
created: 2026-11-07
updated: 2026-11-07
sources: [https://github.com/scenario-labs/skills]
reliability: medium
---

**GitHub**: [scenario-labs/skills](https://github.com/scenario-labs/skills) **★3,462 · 포크 299 · 오픈이슈 34**(볼트 11-07 실측 · 수집기 11-06 ★3,281 → +181/1일) · MIT · Python · created 2026-08-12 · pushed 2026-11-07T00:49Z · 최신 릴리스 `skills-v0.60.1`(10-29) · daily 트렌딩 11위(11-06)

## 핵심 인사이트
> [!insight] 모델 지식(멤버·사이즈·가격 사다리)을 스킬로 쪼개고, "돈 쓰기 전에 판정"을 별도 스킬로 둔다
> 기본 트리의 `SKILL.md` 는 **175개**(볼트 11-07 git tree API 실측 · 수집기 11-06 은 174 → 하루 +1). 모델별 스킬(GPT Image · Seedream · Gemini image · Ideogram · Veo · Seedance · MiniMax Hailuo 등)이 **어떤 변형을 고르고, 어떤 크기로, 얼마에** 돌릴지를 담는다. 여기에 비용 통제 스킬이 붙는다: `scenario-quality-gate`(pass/warn/fail + dry-run 견적) · `scenario-model-comparison`(사전등록 기준 · dry-run 비용 행렬) · `scenario-seedance-drafts`(**480p 초안 → 선별분만 1080p**). 영상 SaaS 관점에서 가장 쓸모 있는 아이디어는 **"초안은 싸게, 확정만 비싸게"** 를 에이전트 규칙으로 고정한 것이다.

> [!warning] 상용 과금 전제
> 핵심 스킬은 **Scenario 계정(OAuth) 또는 API 키 = Creative Unit 과금**이 전제다. README 스스로 `main` 대신 **릴리스 태그 고정 설치**를 권한다(빈번한 변경). 로컬 DCC 툴(ZBrush·Blender·Maya·Unreal·Unity·Godot·Roblox Studio)을 구동하는 "Expert tools" 패밀리는 MCP 불필요하나, 패밀리별 검증 수준이 다르다고 README 가 적는다(볼트 미열람).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: "생성 요청 → dry-run 견적 → 품질 게이트 → 확정 렌더" 흐름은 사용자의 reat-*/Vibecasting 파이프라인에 그대로 이식 가능한 **비용 통제 UX**다. 구현 난이도 낮음(모델별 단가 테이블 + 사전 견적 함수).
- **프롬프트 패턴**: Seedance 480p 초안 선별 → 1080p 업스케일 렌더는 영상 생성 비용을 크게 줄이는 표준 패턴으로 보인다(정량 비교 수치는 README 에 없음).
- **크리에이터 인사이트**: 사용자는 "어떤 모델이 이 컷에 맞나"를 모른다 → 모델 선택을 스킬(사전 지식)로 넘긴 설계가 답이다.
- **경쟁 우위 빈틈**: 스킬이 Scenario 플랫폼 종속. 멀티 프로바이더 직접 호출형으로 같은 구조를 만들면 차별화 여지.
- **즉시 활용(ai-news)**: 부분 YES — `scenario-quality-gate` · `scenario-seedance-drafts` 의 SKILL.md 를 **읽고 규칙만 차용**(계정 불필요). 실제 호출은 과금.

## 관련 페이지
- [[에이전트-스킬]] · [[AI-영상-생성-2026]] · [[AI-3D-생성]] · [[Seedance]] · [[MiniMax]]
- [[garden-skills]] (같은 날 · 영상 제작 스킬 큐레이션) · [[mattpocock-skills]] · [[google-skills]] · [[anthropics-skills]]
- [[auto-ontology]] · [[agent-switch]] · [[pr-agent]] (같은 날 GitHub)

## 원본
- 출처: https://github.com/scenario-labs/skills
- 확인 범위: GitHub API·git tree API(볼트 11-07, SKILL.md 175) · README 는 수집기 기준(상단 약 70행 + grep) · 패밀리 README·SKILL.md 본문 미열람 · 실행 0회
- 신뢰도: ⭐⭐ (★3.5k · 상용 서비스 연동 스킬 · 벤치 해당 없음)
