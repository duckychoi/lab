---
title: SkillCoach
type: source
domain: ai-news
tags: [ai-news, agent-skills, evaluation, self-improving-rubric, benchmark]
created: 2026-07-05
updated: 2026-07-05
sources: [SkillCoach.md]
reliability: low
---

# SkillCoach

시간이 지날수록 스스로 개선되는 **루브릭(rubric)** 으로 에이전트의 스킬 사용 능력을 평가·강화하는 시스템.

## 핵심 인사이트

> [!insight] 스킬 생태계의 "평가·코칭" 레이어 등장
> 스킬 모음([[mattpocock-skills]])과 스킬 표준([[agentskills]])이 폭증한 지금, 다음 필연은 **"스킬을 얼마나 잘 쓰는가"를 측정·개선**하는 층. SkillCoach는 자기개선 루브릭으로 이 평가를 자동화한다. [[EvoPolicyGym]](실행 정책 반복 개선)·[[AgenticDataBench]](스킬 단위 평가)와 함께 "에이전트 스킬 평가" 클러스터를 형성. 2026-07-05 배치의 스킬 3종(모음·표준·평가)이 한 축으로 수렴.

> [!warning] 원문 미검증
> ID 2607.01874, upvotes 14의 자동수집 요약 기반. 자기개선 루브릭의 수렴성·평가 타당성은 원문 확인 필요.

## 도메인별 추출 (ai-news)

- **신뢰도**: HF papers ↑14. 원문 미검증 → low.
- **즉시 활용**: 개념 YES — 내 위키/봇 스킬 사용 품질을 자가 루브릭으로 점검하는 아이디어 이식.
- **6개월 영향력**: 스킬 마켓의 "품질 인증" 기반. 스킬 남발 → 품질 선별로 이동.
- **대체 관계**: 정적 벤치([[AgenticDataBench]]) 대비 자기개선형.
- **허와 실**: "스스로 개선되는 루브릭"의 편향 축적 리스크(→ [[MemSyco-Bench]] 아첨 편향과 유사 경계).
- **액션**: 자가 루브릭 아이디어를 [[SkillOpt]]·내 스킬 점검 루프에 접목 검토.

## 관련 페이지
- [[agentskills]]
- [[mattpocock-skills]]
- [[EvoPolicyGym]]
- [[AgenticDataBench]]
- [[SkillOpt]]

## 원본
- 출처: https://huggingface.co/papers/2607.01874
- 신뢰도: ⭐ (HF ↑14 / 원문 미검증)
