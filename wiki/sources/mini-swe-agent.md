---
title: "SWE-agent/mini-swe-agent — bash 하나만 쓰는 약 100줄 코딩 에이전트 (모델 카드들이 측정 하네스로 쓰는 기준선)"
type: source
domain: ai-news
tags: [ai-news, github-trending, coding-agent, harness, swe-bench, baseline]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/SWE-agent/mini-swe-agent]
reliability: high
---

**GitHub**: ★9,947(볼트 API 11-22 · 수집기 일치) · Python · MIT · 생성 2025-06-28 · push 2026-11-16

## 핵심 인사이트
> [!insight] 하네스를 최소로 줄이면 점수는 "모델의 값"에 가까워진다
> SWE-bench · SWE-agent 팀(Princeton · Stanford, 수집기 판독)의 최소 에이전트. 에이전트 클래스 약 100줄, 도구는 bash 하나(LM 의 tool-calling 인터페이스 불필요), 각 액션은 독립 `subprocess.run` 이라 docker/podman/apptainer 샌드박스 교체가 쉽고, 히스토리가 선형이라 궤적을 그대로 파인튜닝 · RL 데이터로 쓴다. 볼트의 [[하네스-설계-축]] 에서 보면 **"하네스 기여를 0 에 가깝게 고정한 기준점"** 이다 — 같은 배치 [[Inkling-2-Mini-GGUF]] 카드가 DeepSWE · Terminal Bench · SWE-Bench Pro 측정에 이 하네스를 썼고, 볼트 기존 [[DeepSWE]] · [[flint-GGUF]] 도 이를 언급한다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐⭐ — ★9.9k · SWE-bench 팀 · MIT.
- **즉시 활용**: 🟡 일상 코딩 도구가 아니라 **평가 기준선 · 궤적 수집용**. 로컬 모델을 비교할 때 하네스 변수를 없애는 용도로 적합.
- **6개월 영향력**: 모델 카드의 "bash only" 표기가 표준 단위가 되면 카드 간 비교가 쉬워진다.
- **대체 관계**: Claude Code 등 대비 기능이 의도적으로 적다.
- **허와 실**: "SWE-bench Verified 74% 이상"은 붙이는 모델에 따라 달라지는 값이다.
- **액션**: 관찰(로컬 모델 벤치를 직접 돌릴 때 채택).

## 관련 페이지
- [[하네스-설계-축]] · [[DeepSWE]] · [[flint-GGUF]] · [[Inkling-2-Mini-GGUF]] · [[rig]] · [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/SWE-agent/mini-swe-agent
- 확인 범위: GitHub API(스타 · 언어 · MIT · 생성일 · push) · 🔴 README 내용은 수집기 판독
- 신뢰도: ⭐⭐⭐⭐
