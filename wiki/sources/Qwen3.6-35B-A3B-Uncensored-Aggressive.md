---
title: Qwen3.6-35B-A3B-Uncensored-Aggressive — 무검열 MoE 멀티모달 GGUF
type: source
domain: ai-news
tags: [ai-news, huggingface, model, uncensored, moe, multimodal, gguf, local-llm]
created: 2026-07-09
updated: 2026-07-09
sources: []
reliability: medium
---

# HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive (HF DL 2.72M)

**HuggingFace**: https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
**다운로드**: 2,716,428 (2026-07-09) · **likes**: 2,580
**베이스**: Qwen/Qwen3.6-35B-A3B · **언어**: 영·중·다국어

> [!warning] 무검열·거부율 클레임 검증 한계
> "0/465 Refusals"(465개 커뮤니티 테스트 전부 거부 없음)는 **제작자 자가 측정** 수치. 안전장치 제거형(abliterated) 모델로 유해 출력 위험이 있으며, 벤치·안전성 재현은 미실측. DL/아키텍처/GGUF 라인업만 WebFetch 실측 채택.

> [!insight] 핵심 인사이트
> **[[Qwen3.6-35B-A3B]] 베이스의 무검열 파인튜닝 + GGUF 양자화판**이 HF 다운로드 **2.72M**(likes 2,580)로 급등. WebFetch 실측 아키텍처: 35B 총 / **~3B 활성 MoE(256 전문가 중 8 라우팅)**, **262K 네이티브 컨텍스트**, **멀티모달(text·image·video)**. GGUF는 IQ2_M(11GB)~Q8_K_P(44GB)로 importance matrix 최적화 → llama.cpp·LM Studio 즉시 구동. 주목점은 절대 성능이 아니라 **"무검열 + 로컬 실행 가능 경량 MoE + 멀티모달"의 결합 수요가 200만+ DL로 실증**됐다는 것 — [[Qwen3.6-35B-Uncensored]] 계열(어제까지 Aggressive 변형 언급)의 채택이 여전히 최상위권. 로컬 LLM 실수요가 "검열 없는 자유도"를 강하게 원한다는 신호(단 안전 리스크는 사용자 책임).

## 도메인별 추출 (local-llm / ai-news 교차)

- **신뢰도**: ⭐⭐⭐ (HF DL 2.72M·likes 2,580 실측 / 무검열·거부율 자가 측정 → medium)
- **즉시 활용**: 조건부 — 3B 활성 MoE라 소비자 GPU/맥에서 262K 컨텍스트·멀티모달 로컬 구동 가능. 단 무검열 특성상 프로덕션·공개 서비스엔 부적합, 개인 실험 한정.
- **6개월 영향력**: 로컬 오픈모델 채택에서 "경량 MoE + 멀티모달 + 무검열"이 뚜렷한 수요층. 커뮤니티 파인튜닝이 플래그십 못지않은 DL을 견인.
- **대체 관계**: 상용 API의 검열·과금을 로컬 무검열로 대체하려는 사용자층. [[Qwen3.6-35B-A3B]] 원본·[[Ornith-1.0-35B]] 등과 경쟁.
- **허와 실**: "0/465 거부"는 판매 포인트지 안전 보증이 아님. 무검열 = 정렬 제거 = 유해·환각 리스크 증가. 벤치 우위 주장은 원문 미검증.
- **액션**: 필요 시 IQ4 양자화로 로컬 멀티모달(image-text) 태스크 1건만 개인 환경서 실측, 원본 Qwen3.6-35B-A3B와 품질·거부 성향 비교.

## 관련 페이지
- [[Qwen3.6-35B-A3B]] — 베이스 모델
- [[Qwen3.6-35B-Uncensored]] — 무검열 계열 선행
- [[Ornith-1.0-35B]] · [[Agents-A1]] — 35B급 오픈 경쟁 모델
- [[Alibaba]] — Qwen 원 제작사
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/HauhauCS/Qwen3.6-35B-A3B-Uncensored-HauhauCS-Aggressive
- HF DL: 2,716,428 (2026-07-09), likes 2,580
- 아키텍처: 35B/~3B 활성 MoE(256e top-8), 262K 컨텍스트, 멀티모달, GGUF IQ2_M~Q8_K_P
- 신뢰도: ⭐⭐⭐ (DL·아키텍처 실측 / 무검열·벤치 자가 측정)
