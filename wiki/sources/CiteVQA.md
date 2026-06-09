---
title: CiteVQA — 문서 VQA 증거 귀속 능력 벤치마크
type: source
domain: ai-news
tags: [ai-news, document-ai, vqa, benchmark, evidence-attribution, trustworthy-ai]
created: 2026-05-19
updated: 2026-05-19
sources: []
reliability: medium
---

# CiteVQA — 문서 VQA 증거 귀속 능력 벤치마크

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 문서 이해 AI(VQA)가 답변의 근거가 되는 증거를 얼마나 정확히 인용·귀속할 수 있는지 평가하는 벤치마크. "답이 맞는가"에서 "왜 이 답이 맞는지 근거를 댈 수 있는가"로 문서 AI 평가 기준을 격상한다. 신뢰 가능한 엔터프라이즈 문서 AI에 핵심 요구사항.

## 도메인별 추출 (ai-news)

- **신뢰도**: HF 업보트 76 (2026-05-18), arXiv 2605.12882, 학술 벤치마크로 중상위 관심
- **즉시 활용**: NO — 벤치마크 논문. 직접 활용보다는 문서 AI 시스템 선택 기준으로 참조
- **6개월 영향력**: 문서 처리 AI 솔루션 평가 시 표준 벤치마크가 될 가능성. [[MinerU2.5]], [[markitdown]] 같은 문서 파싱 도구 평가에 연결 가능
- **대체 관계**: 기존 VQA 벤치마크(DocVQA 등)의 한계 보완 — 정답률 외 근거 인용력 추가
- **허와 실**: 벤치마크 논문은 현실 적용 성능과 괴리 있을 수 있음. 실 문서 다양성 커버리지 확인 필요
- **액션**: 문서 AI 파이프라인 구축 시 CiteVQA 점수를 모델 선택 기준에 포함

## 관련 페이지

- [[MinerU2.5]] — 문서 파싱 SOTA VLM
- [[markitdown]] — 문서→마크다운 변환기
- [[UniDoc-RL]] — RL 기반 문서 이해 RAG 훈련

## 원본

- 출처: https://huggingface.co/papers/2605.12882
- 신뢰도: ⭐⭐ (업보트 76, arXiv 2605.12882, 2026-05-18)
