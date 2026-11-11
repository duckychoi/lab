---
title: "MMDM — 한 번의 forward 로 선택지 확률을 내는 'System-1 결정 모델' 벤치: 16범주 5,448문항, 최고 Hard 다중선택 정확도 36.81%"
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, decision-model, tool-selection, reranker]
created: 2026-11-11
updated: 2026-11-11
sources: [https://huggingface.co/papers/2611.14309]
reliability: medium
---

**논문**: [2611.14309](https://huggingface.co/papers/2611.14309) · CUHK Database Group · 업보트 **23** · 코드 [mmdm-benchmark/mmdm](https://github.com/mmdm-benchmark/mmdm) ★**8**(GitHub API 볼트 실측 · HF 캐시 값은 1) · MIT

## 핵심 인사이트
> [!insight] 상식은 잘 맞히고, 서로 얽힌 선택지에서 무너진다
> 추론 문장을 생성하지 않고 선택지 확률만 내는 결정 모델 28개를 평가. 예시로 Perplexity Decider-V1.2 의 Hard 단일선택 정확도는 세계지식 **78.75%** 인데 선택지 논리 **53.95%** · 제약 계획 **47.95%** 로 떨어진다. **전 모델 최고 Hard 다중선택 정확도는 36.81%**. 문항 5,448개 · 16범주 · 선택지 2~1,024개 · 입력 최대 64,817 토큰(초록 전문 일치).

> [!note] 왜 이 볼트에 관련 있나
> 평가 시나리오가 **에이전트 상태 추적 · 툴/스킬 선택 · 선호 판정 · 루브릭 채점**이다. 같은 날 [[ha-mcp]](툴 87개)와 [[mattpocock-skills]](스킬 39개) · [[agent-skills]](25개)가 입고됐다 — 툴·스킬이 늘수록 "무엇을 부를지 고르는" 단계가 병목이 되고, 그 단계의 현재 수준이 다중선택 36.81% 라는 뜻이다.

> [!warning] 한정
> 수치는 초록의 "예시" 한 모델과 최고값뿐이다. 28개 모델 전체 표 · 일반 생성형 LLM 과의 비교는 본문. Hard 가 아닌 구간 점수는 초록에 없다.

## 도메인별 추출 (ai-news)
- **신뢰도**: 업보트 23 · 코드 공개(★8) · 벤치 신규 구성·재작성 문항(유출 회피 목적, 초록).
- **즉시 활용**: 조건부 — 에이전트의 툴 라우터·리랭커를 고를 때 평가셋으로.
- **6개월 영향력**: 스킬·MCP 툴 수가 늘어나는 흐름에서 "선택 정확도"가 별도 지표로 자리 잡을 수 있다.
- **허와 실**: 벤치 자체의 난이도 주장은 수치로 뒷받침되나 ★8 로 채택은 아직 없다.
- **액션**: 읽기(본문 표).

## 관련 페이지
- [[ha-mcp]] · [[에이전트-스킬]] · [[mattpocock-skills]] · [[agent-skills]]

## 원본
- 출처: https://huggingface.co/papers/2611.14309
- 확인 범위: HF papers API 초록 전문 · GitHub API 메타 · 🔴 본문 미열람
- 신뢰도: ⭐⭐ (업보트 23 · ★8)
