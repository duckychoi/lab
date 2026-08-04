---
title: Nanbeige4.2-3B — 3B 에이전틱 LLM (자체벤치 SWE 63.6)
type: source
domain: ai-news
tags: [ai-news, hf-model, slm, 3b, agentic-llm, local-llm, edge, text-generation]
created: 2026-07-26
updated: 2026-07-26
sources: []
reliability: medium
---

# Nanbeige4.2-3B (HF DL 14,049)

> [!insight] 핵심 인사이트
> **3B 규모 에이전틱(agentic) LLM** — 작은 파라미터로 도구호출·다단계 태스크를 노리는 온디바이스급 모델. HF 다운로드 **14,049**(좋아요 415, 2026-07-26 WebFetch 실검증, base_model `Nanbeige4.2-3B-Base`, Apache-2.0, en/zh). 모델카드 자체벤치가 공격적이다: **SWE-Bench Verified 63.6·GPQA-Diamond 87.4·Pinch-Bench-V2 74.7** 로 "더 큰 모델을 능가"한다고 주장. 사실이면 [[MiniCPM5-1B]]·[[needle]](26M 함수호출)로 이어지는 **초소형 에이전트 로컬화** 계보에서 3B 상단을 채우지만, 3B가 SWE-Bench 63.6이라는 수치는 프론티어 대형과 비교해 **비현실적으로 높아** 자체벤치 특유의 과장 가능성이 크다.

**HuggingFace**: https://huggingface.co/Nanbeige/Nanbeige4.2-3B
**다운로드**: DL 14,049 (좋아요 415, 2026-07-26 WebFetch 실검증)
**신뢰도**: ⭐⭐⭐ (DL/좋아요 실확인, 벤치는 제작사 자체 수치·독립 재현 전 — 인용 시 "자체벤치" 명시)

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐⭐ — DL 14,049·좋아요 415·pipeline/base_model WebFetch 실확인(medium). 단 **SWE 63.6·GPQA 87.4·Pinch 74.7은 전부 모델카드 자체 수치**로, 3B급으론 이례적으로 높아 독립 재현 전까지 액면 신뢰 금지.
- **즉시 활용**: 조건부 — 3B라 소비자 GPU/CPU에서 가볍게 구동. 에이전트 도구호출·라우팅 로컬 후보이나, 실제 에이전틱 성능은 자체벤치와 괴리 클 수 있어 실태스크 스팟체크 선행 필요.
- **6개월 영향력**: "3B가 대형을 능가"가 부분이라도 사실이면 온디바이스 에이전트 문턱이 급락. 다만 유사 초소형 주장([[Inkling]]·[[Loop-the-Loopies]])이 미검증으로 남은 전례가 있어, 재현 리포트 확보 전엔 트렌드 신호로만 취급.
- **대체 관계**: [[MiniCPM5-1B]](1B 온디바이스)·[[needle]](26M 함수호출) 대비 3B 상단. [[Qwen3.6-27B]]·[[Bonsai-27B]] 같은 중형 양자화판과는 "작지만 온전한 정밀도" vs "크지만 압축" 축에서 상보.
- **허와 실**: 마케팅 걷어내면 **검증된 것은 DL/좋아요뿐**. 벤치 3종 모두 자체 수치이며 특히 SWE 63.6은 3B로는 과장 의심 1순위 — 실사용 코딩/추론 태스크로 반드시 교차 검증.
- **액션**: 로컬로 받아 실제 도구호출·간단 SWE 태스크로 자체벤치 대비 실체감 스팟체크. 재현 안 되면 low로 강등·벤치 인용 금지.

> [!warning] 신뢰도 medium — 자체벤치 과장 의심
> SWE-Bench Verified 63.6·GPQA-Diamond 87.4·Pinch-Bench-V2 74.7은 **제작사 자체 수치**다. 3B 모델의 SWE 63.6은 프론티어 대형과 비교해 비현실적으로 높아 과장 가능성이 크다. 독립 재현 전까지 수치 인용 시 반드시 "자체벤치·미검증" 병기.

## 관련 페이지
- [[MiniCPM5-1B]]
- [[needle]]
- [[Qwen3.6-27B]]
- [[Bonsai-27B]]
- [[Inkling]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/Nanbeige/Nanbeige4.2-3B
- 다운로드: DL 14,049 (좋아요 415, 2026-07-26 WebFetch 실검증), base_model `Nanbeige/Nanbeige4.2-3B-Base`, Apache-2.0, en/zh
- 자체벤치: SWE-Bench Verified 63.6·GPQA-Diamond 87.4·Pinch-Bench-V2 74.7 (모델카드 자체 수치·미검증)
- 신뢰도: ⭐⭐⭐ (DL/좋아요 실확인 medium, 벤치 자체 수치·독립 재현 전)
