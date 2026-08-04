---
title: SkillSpector — AI 에이전트 스킬 보안 정적 분석 스캐너
type: source
domain: ai-news
tags: [ai-news, security, agent-skills, static-analysis, nvidia, vulnerability]
created: 2026-06-14
updated: 2026-06-16
sources: []
reliability: high
---

# NVIDIA/SkillSpector

> [!insight] 핵심 인사이트
> NVIDIA가 공개한 AI 에이전트 스킬 전용 보안 스캐너. ⭐6,679 (+1,079 today, 2026-06-16). [[agent-skills]] 생태계가 급성장하는 가운데 "스킬 배포 전 보안 검증"이라는 새로운 필수 인프라 레이어가 등장. 에이전트 스킬 큐레이션 붐의 이면에서 **보안 감사 도구 수요가 동시에 폭발**하는 패턴 확인.

**GitHub**: https://github.com/NVIDIA/SkillSpector  
**스타**: ⭐6,679 (+1,079 today, 2026-06-16)  
**신뢰도**: ⭐⭐⭐⭐ (NVIDIA 공식, 당일 급상승)

## 도메인별 추출

- **신뢰도**: NVIDIA 공식 레포, 당일 +804 급상승 — 신뢰도 높음
- **즉시 활용**: YES — 에이전트 스킬 배포 전 보안 스캔 파이프라인에 통합 가능. .claude/skills/ 폴더 스킬 검증에 직접 적용
- **6개월 영향력**: 에이전트 스킬 마켓플레이스 확산과 함께 "스킬 보안 감사"가 표준 워크플로우로 자리잡을 가능성. CI/CD 파이프라인 통합 수요 증가 예상
- **대체 관계**: 기존 코드 정적 분석(Bandit, Semgrep) 대비 에이전트 스킬 특화 패턴(프롬프트 인젝션, 권한 탈취, 악성 도구 호출 등) 탐지에 특화
- **허와 실**: 오픈소스 초기 단계, 탐지 패턴 커버리지는 확인 필요. NVIDIA 내부 스킬 생태계 기준으로 설계되었을 가능성

> [!action] 당장 할 것
> SkillSpector로 .claude/skills/ 내 커스텀 스킬 스캔 실행. 악성 패턴 탐지 룰셋 검토 → 자체 스킬 작성 시 보안 체크리스트 추가.

> [!note] 배경 정보
> [[agent-skills]](⭐58,861), [[awesome-agent-skills]] 등 에이전트 스킬 큐레이션 급성장 흐름 속에서 보안 감사 도구 수요 동시 폭발. [[Claude-Code-워크플로우]]에서 스킬 관리가 핵심이 된 만큼 보안 레이어 필수화.

## 관련 페이지
- [[agent-skills]]
- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[awesome-agent-skills]]

## 원본
- 출처: https://github.com/NVIDIA/SkillSpector
- 신뢰도: ⭐⭐⭐⭐ (6.7K 스타, NVIDIA 공식)
