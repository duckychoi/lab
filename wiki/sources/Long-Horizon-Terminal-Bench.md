---
title: Long-Horizon-Terminal-Bench — 밀집 보상 기반 장기 터미널 에이전트 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, terminal-agent, long-horizon, dense-reward, agent-eval]
created: 2026-07-13
updated: 2026-07-13
sources: []
reliability: medium
---

# Long-Horizon-Terminal-Bench (HF 2607.08964)

> [!insight] 핵심 인사이트
> **밀집 보상(dense reward) 채점으로 장기(long-horizon) 터미널 작업에서 에이전트의 한계를 측정**하는 벤치마크. 기존 성공/실패 이분 채점이 놓치는 *"어디서부터 무너지는가"*를 단계별 보상으로 드러낸다. [[TUA-Bench]]·[[CLI-Universe]](터미널 에이전트 평가)와 같은 계보이며, 밀집 보상이라는 점에서 단순 pass@k보다 진단력이 높다 — 에이전트가 긴 작업에서 궤도를 이탈하는 지점을 정밀 지목.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ (HF 데일리 페이퍼 · 초록 기반). 미래형 ID(2607)로 원문 정밀검증 보류.
- **즉시 활용**: MAYBE — 내가 돌리는 자동화 에이전트(크론·셸 작업)의 장기 안정성 진단 프레임으로 참고 가치. 밀집 보상 아이디어는 자체 태스크 채점에 차용 가능.
- **6개월 영향력**: 에이전트 평가가 "성공률"에서 "궤적 품질·이탈 지점"으로 이동하는 흐름. [[UniClawBench]]·[[Long-Horizon-Terminal-Bench]]가 장기 에이전트의 진짜 실력을 노출.
- **대체 관계**: 이분 채점 벤치([[TUA-Bench]])를 밀집 보상으로 정밀화. [[EvoPolicyGym]](궤적 단위 진단)과 문제의식 공유.
- **허와 실**: 밀집 보상 설계 자체의 편향 가능. 채점 룰이 특정 해법을 우대하지 않는지 확인 필요.
- **액션**: 원문 공개 시 SOTA 모델의 장기 터미널 통과율·이탈 패턴 확인. 밀집 보상 채점법을 내 에이전트 자가진단에 적용 검토.

## 관련 페이지
- [[TUA-Bench]]
- [[CLI-Universe]]
- [[UniClawBench]]
- [[EvoPolicyGym]]

## 원본
- 출처: https://huggingface.co/papers/2607.08964
- 신뢰도: ⭐⭐ (HF 데일리 페이퍼 · 초록 검증 · 미래형 ID로 원문 정밀검증 보류)
