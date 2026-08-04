---
title: upstage/Solar-Open2-250B — Upstage 오픈 250B/15B 하이브리드-어텐션 MoE
type: source
domain: local-llm
tags: [ai-news, local-llm, hf-model, moe, korean-llm, upstage, hybrid-attention, agentic, text-generation]
created: 2026-07-25
updated: 2026-07-29
sources: []
reliability: medium
---

# Solar-Open2-250B (upstage/Solar-Open2-250B)

> [!insight] 핵심 인사이트
> 한국 [[Upstage]]가 공개한 **오픈 웨이트 250B 총/15B 활성 MoE**. HF 다운로드 4,804월·좋아요 682(2026-07-29 갱신, 2,784→4,804·546→682). NVIDIA B200 2M GPU시간·12조 토큰 학습, 위치인코딩 제거(선형 어텐션이 순서를 recurrent state로 내재) 추가 확인. 모델카드 WebFetch 확인 결과 단순 대형 MoE가 아니라 **하이브리드-어텐션**(48레이어에 softmax+linear 어텐션 혼합) + **321 전문가(320 라우팅 + 1 공유)** + **1M 컨텍스트** 구조로, "긴 컨텍스트에서도 효율적 추론"을 설계 목표로 내세운다. 자체 벤치는 **MMLU-Pro 86.2 · GPQA-Diamond 86.3 · SWE-Bench Verified 70.4 · AIME 2026 95.7 · LiveCodeBench 92.4** — 사실이라면 오픈 플래그십급. 무엇보다 **한국어·일본어·영어 다국어**를 명시한 국산 오픈 모델이라는 점에서 [[GLM-5.2]]·[[LongCat-2.0]] 중국발 대형 MoE 계보에 **한국 진영**이 합류하는 사건.

> [!note] 배경 정보
> Upstage는 Solar LLM 계열로 알려진 한국 AI 기업. 이번 Open2는 "Solar License"(파생물에 "Solar" 접두·"Built with Solar" 표기 요구) 하의 오픈 웨이트로, 완전 자유는 아니지만 가중치 공개. 15B 활성이라 250B 총량 대비 추론 비용은 중형급 — 단 250B 웨이트 저장·서빙은 여전히 서버 인프라 필요(소비자 로컬 불가).

## 도메인별 추출 (local-llm / ai-news 교차)

- **실용성 판단**: 부분적 YES — 15B 활성이라 서빙 효율은 좋으나 250B 웨이트라 다중 GPU 서버 필요. 소비자 온디바이스는 불가, **자체 호스팅 API급**. 한국어 성능이 자체벤치대로면 국산 에이전트 백본 후보.
- **메모리 아키텍처**: 하이브리드 어텐션(softmax+linear 혼합)으로 1M 컨텍스트를 노림 — [[Mamba4]]식 선형 어텐션을 소프트맥스와 레이어 단위로 섞는 접근. 131K까지 추론 트레이스(reasoning trace) 지원.
- **Hermes/ChinameBot 적용**: 한국어 다국어 오픈 웨이트라 국산 봇 백본으로 GLM 계열 대안 검토 가치. OpenAI 호환 툴콜 지원으로 에이전트 연동 용이.
- **트레이드오프**: 250B 총량(서빙 인프라 부담) ↔ 15B 활성(추론 효율) + 1M 컨텍스트. 벤치가 사실이면 SWE 70.4·AIME 95.7로 준프론티어.
- **오픈소스 구현체**: HF 가중치 공개(Solar License), OpenAI 호환 인터페이스. 신규라 커뮤니티 양자화(GGUF 등)는 아직 미형성.

> [!warning] 자체 벤치 — 독립검증 전 잠정
> MMLU-Pro 86.2·SWE 70.4·AIME 95.7 등은 Upstage 자체 발표. 신규 공개(DL 2,784)로 독립 재현·리더보드 교차검증 전이라 reliability medium. Solar License의 상업 사용 조건(접두·표기 의무)도 도입 전 확인 필요.

## 관련 페이지
- [[Upstage]]
- [[GLM-5.2]]
- [[LongCat-2.0]]
- [[Inkling]]
- [[Laguna-S-2.1]]
- [[Mamba4]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/upstage/Solar-Open2-250B
- HuggingFace: 다운로드 4,804월 / 좋아요 682 (2026-07-29 갱신, 2,784→4,804·546→682, WebFetch 실측)
- 아키텍처: 250B 총 / 15B 활성 MoE, 48레이어 하이브리드-어텐션(softmax+linear), 321 전문가(320+1 공유), 1M 컨텍스트, ~131K reasoning trace
- 라이선스: Upstage Solar License (파생물 "Solar" 접두·"Built with Solar" 표기)
- 자체 벤치: MMLU-Pro 86.2 · GPQA-Diamond 86.3 · SWE-Bench Verified 70.4 · AIME 2026 95.7 · LiveCodeBench 92.4
- 신뢰도: ⭐⭐⭐ (Upstage 공식 + 모델카드 WebFetch 실확인, 자체벤치·신규라 medium)
