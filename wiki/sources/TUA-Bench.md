---
title: TUA-Bench — 터미널 사용 에이전트(Terminal-Use Agent) 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, terminal-agent, cli, ai-agent, evaluation]
created: 2026-06-30
updated: 2026-06-30
sources: []
reliability: medium
---

# TUA-Bench: Benchmark for Terminal-Use Agents

> [!insight] 핵심 인사이트
> HF 데일리 upvote 33 (2026-06-30). **터미널/CLI를 다루는 범용 에이전트의 능력을 측정하는 벤치마크.** 셸 조작·명령 수행 능력을 표준화해 평가한다. [[Claude-Code-워크플로우]]처럼 *에이전트가 터미널에서 직접 작업*하는 시대에, "어떤 에이전트가 셸을 더 잘 다루는가"를 정량화하는 인프라. [[CLI-Universe]](터미널 에이전트용 검증 태스크 자동 합성)와 짝을 이루며 — CLI-Universe가 *태스크 생성*이라면 TUA-Bench는 *능력 측정* — 터미널 에이전트 평가 생태계가 형성되고 있음을 보여준다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — HF upvote 33. 벤치마크는 채택·인용으로 가치가 결정되므로 초기 단계. 평가 항목 설계의 타당성 확인 필요.
- **즉시 활용**: MAYBE — 내가 쓰는 [[Claude-Code-워크플로우]]·터미널 에이전트의 신뢰성을 객관 비교할 때 참조 지표. 직접 실행보다 결과 해석용.
- **6개월 영향력**: 터미널 에이전트(Claude Code, 코딩 CLI 등)가 늘면서 "셸 조작 능력 리더보드"가 모델 선택 기준이 될 수 있음.
- **대체 관계**: [[EnterpriseClawBench]]·[[NatureBench]]·[[PlanBench-XL]] 같은 에이전트 벤치마크 군에 *터미널 특화* 축을 추가.
- **허와 실**: 정적 벤치마크의 한계([[Beyond-Static-Leaderboards]] 경고) — 벤치 점수가 실제 워크플로 성능을 보장하지 않음.
- **액션**: 벤치 항목 구성 확인 → 내 터미널 에이전트 신뢰성 평가의 체크리스트로 차용.

## 관련 페이지
- [[CLI-Universe]]
- [[EnterpriseClawBench]]
- [[PlanBench-XL]]
- [[NatureBench]]
- [[Beyond-Static-Leaderboards]]
- [[AI-에이전트-프레임워크]]
- [[Claude-Code-워크플로우]]

## 원본
- 출처: https://huggingface.co/papers/2606.28480
- HF 데일리 upvote: 33 (2026-06-30)
- 신뢰도: ⭐⭐ (신규 벤치마크, 채택·타당성 미검증)
