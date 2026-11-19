---
title: "meta-llama/Meta-Llama-3-8B-Instruct — 2024년 기준선 모델의 트렌딩 재부상 (MMLU 68.4 · gated)"
type: source
domain: ai-news
tags: [ai-news, huggingface, model, llama, gated, 8B, instruct, baseline]
created: 2026-11-19
updated: 2026-11-19
sources: [https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct]
reliability: medium
---

**HF**: 다운로드 **423,008**(30일) · 누적 **49,225,973** · ♥6,266 · trendingScore 50.5 · `gated: manual` · license `llama3` · 생성 2024-04-17(볼트 API 11-19 — 수집기 "04-18 공개"는 발표일 기준)

## 핵심 인사이트
> [!insight] 신모델이 아니라 오래된 기준선이 트렌딩 상위에 다시 올라왔다 — 원인은 미확인
> 2년 반 된 모델(컨텍스트 8k · 컷오프 2023-03)이 trendingScore 50.5. 볼트 보유 후속 [[Llama-3.1-8B-Instruct]](09-15, 30일 dl 571만)와 비교하면 30일 다운로드는 1/13 수준. 트렌딩 지표가 **증가율**을 보기 때문에, 논문 · 벤치 재현 실험에서 기준선으로 일괄 호출되는 사건만으로도 올라올 수 있다 — 가설일 뿐 확인 안 됨.

> [!note] gated 카드 처리 (09-15 규약 유지)
> raw README 는 401. 수집기가 **HTML 페이지에서** 표를 확인: MMLU 68.4 · GPQA 34.2 · HumanEval 62.2 · GSM-8K 79.6 · MATH 30.0. 볼트는 재확인하지 않았다(수집기 판독). gated 저장소의 DL 은 승인된 부분집합이라 비게이트 모델과 DL:♥ 직접 비교 금지([[Llama-3.1-8B-Instruct]] 09-15 기록).

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ Meta 공식 · 누적 4,922만.
- **즉시 활용**: NO — 같은 급 최신 대안 다수. 기준선 재현용으로만.
- **6개월 영향력**: 없음. 관측 대상은 "트렌딩 지표가 무엇을 재는가".

## 관련 페이지
- [[Llama-3.1-8B-Instruct]] · [[Meta]] · [[캐시된-지표-신선도]] · [[지표-창길이]]

## 원본
- 출처: https://huggingface.co/meta-llama/Meta-Llama-3-8B-Instruct
- 확인 범위: HF API(expand: dl 30일 · 누적 · ♥ · trendingScore · gated · license · createdAt) · 🔴 카드 벤치 수치는 수집기 HTML 판독
- 신뢰도: ⭐⭐⭐
