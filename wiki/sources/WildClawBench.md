---
title: WildClawBench — 실세계 복잡·장기 태스크 AI 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, benchmark, agent, long-horizon, real-world, internlm, evaluation]
created: 2026-05-17
updated: 2026-05-17
sources: []
reliability: high
---

# WildClawBench (arXiv 2605.10912)

> [!insight] 핵심 인사이트
> 실세계 복잡·장기(long-horizon) 태스크에서 AI 에이전트 성능을 측정하는 **InternLM 기반 평가 벤치마크**. 371회 인용으로 이미 커뮤니티에서 유효성을 인정받은 에이전트 벤치마크. "Claw" 계열 벤치마크([[ClawBench]], [[ClawGUI]], [[Claw-Eval-Live]])의 "Wild" 버전으로 실환경 난이도 적용.

**arXiv**: https://huggingface.co/papers/2605.10912
**신뢰도**: ⭐⭐⭐⭐

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 371 citations, InternLM(Shanghai AI Lab) 발표, 이미 커뮤니티 검증 완료
- **즉시 활용**: YES — 에이전트 성능 평가 시 이 벤치마크 기준 사용 가능
- **6개월 영향력**: "장기 태스크"는 AI 에이전트의 가장 어려운 문제 — 이 벤치마크가 표준화되면 에이전트 프레임워크 선택 기준으로 활용. [[ClawBench]](단기), WildClawBench(장기) 이분법 정착 가능
- **"Wild" 의미**: 실제 사용자 행동 패턴에서 추출한 태스크 — 인공적 벤치마크 대비 현실 밀착성 높음
- **대체 관계**: [[ClawBench]], [[gameworld]], [[WindowsWorld]] 등 에이전트 벤치마크 생태계에서 장기 실세계 태스크 특화
- **허와 실**: "Wild" = 실세계이지만 특정 플랫폼·언어에 편향 가능. 한국어/한국 사용자 태스크 포함 여부 확인 필요

> [!question] 미해결 질문
> WildClawBench에서 최고 성능 에이전트 모델은? 인간 베이스라인은?

## 관련 페이지
- [[ClawBench]] — AI 에이전트 일상 온라인 태스크 벤치마크 (단기 버전)
- [[ClawGUI]] — GUI 에이전트 학습·평가 프레임워크
- [[Claw-Eval-Live]] — 워크플로우 에이전트 라이브 벤치마크
- [[gameworld]] — 게임 에이전트 표준 평가 벤치마크
- [[AI-에이전트-프레임워크]] — 에이전트 프레임워크 전체 지형도

## 원본
- 출처: https://huggingface.co/papers/2605.10912
- arXiv: 2605.10912
- Citations: 371 (2026-05-17)
- 신뢰도: ⭐⭐⭐⭐ (InternLM/Shanghai AI Lab, 371 citations)
