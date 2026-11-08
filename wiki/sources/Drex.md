---
title: "Drex — 디코딩 없이 선택지 확률분포를 한 번에 내는 오픈 '결정 모델' 4종. 183ms, 단 비교 벤치는 자사 계열로 보인다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, decision-model, classification, routing, low-latency, open-weights, nace-ai]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/papers/2611.07854]
reliability: low
---

**논문**: arXiv 2611.07854 · HF 업보트 **22**(볼트 11-08 · 수집기 19) · Nace.AI · 코드 [nace-ai/drex-decision-models](https://github.com/nace-ai/drex-decision-models) ★**116** · Apache-2.0 · created 2026-10-09

## 핵심 인사이트
> [!insight] "고르기"는 생성할 필요가 없다
> 상태(문서·레코드·에이전트 컨텍스트, 선택적으로 이미지) + 질문 + 선택지 → **옵션별 확률분포**(객관식·예/아니오·서열 점수)를 자기회귀 없이 반환. 일관성 없는 답 · 출력 파싱 · 지연을 동시에 없앤다. 8B(DLM)·9B(v1.5)·35B-A3B(v2.0)·27B(Max, 비전) 4종 공개. 학습 = SFT + RLAF + 옵션 순서 강건성 consistency loss.

> [!warning] 벤치의 독립성이 불투명
> - **Decision Index 0.4.1 Max 67.52 vs Jev 1.14.0 60.70** · Decision Bench v4 에서 d3-turbo·GPT-6 Sol 과 통계적 동률, **Claude Opus 5.5 보다 1.6점 낮음** · DecideBench 결정모델 중 최고. 세 벤치 모두 볼트가 처음 보는 이름이고, 초록은 *"among the decision models **we compare**"* 로 범위를 스스로 한정했다(보존).
> - 지연 **183 ms vs GPT-6 Sol ~2.0 s · Opus 5.5 ~3.5 s** — 생성형 프런티어 모델과의 지연 비교는 *태스크 형식이 다르다*(옵션 확률 1회 vs 자기회귀) → 속도 우위는 구조상 당연하고 **정확도 동률 여부가 실제 쟁점**.

## 도메인별 추출 (ai-news)
- **즉시 활용**: 조건부 YES — 대량 분류·라우팅·심사(정해진 선택지)라면 9B/35B-A3B 를 로컬로 시험할 가치. 봇의 의도 라우팅 후보.
- **대체 관계**: LLM-as-judge · 분류용 프롬프팅을 대체.
- **허와 실**: 벤치 출처 미확인 · 레포 ★116 · 생성형과의 지연 비교는 사과-오렌지.
- **액션**: 낮은 우선순위로 actionable 등록(라우팅 실험).

## 관련 페이지
- [[DPDM]](같은 "생성 없이 판단" 축) · [[비매칭-비교]] · [[Anthropic]]

## 원본
- 출처: https://huggingface.co/papers/2611.07854
- 확인 범위: HF papers API 초록(볼트 11-08) · GitHub API(★116) · 가중치·벤치 정의 미열람
- 신뢰도: ⭐ (벤치 독립성 미확인)
