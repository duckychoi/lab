---
title: Zhipu AI (Z.AI)
type: entity
domain: ai-news
tags: [entity, zhipu-ai, zai, GLM, chinese-llm, MoE, bilingual, monday-ai]
created: 2026-04-10
updated: 2026-08-28
sources: [GLM-5.1.md, GLM-5.2.md, GLM-5.3-Flash.md]
reliability: high
---

# Zhipu AI (Z.AI)

중국 베이징 기반 AI 연구 기업. GLM(General Language Model) 시리즈 개발사. 글로벌 브랜드명은 **Z.AI**.

## 주요 모델

- **GLM-5-Turbo**: 이 위키 어시스턴트 Monday의 기반 모델
- **GLM-5.1**: 753B MoE 아키텍처, 한국어+영어 이중 언어, MIT 라이선스 (2026-04-08 출시)
- **[[GLM-5.2]]**: 753B·MIT 플래그십, 1M 컨텍스트(IndexShare 아키텍처). GPQA-Diamond 91.2·AIME 2026 99.2·SWE-Bench Pro 62.1·Terminal Bench 2.1 81.0 (HF 191k DL, likes 3.29k, 2026-07-03) — 단 자체 모델카드가 SWE-Bench Pro·Terminal Bench에서 Claude Opus 4.8 상회를 인정
- GLM 시리즈: arXiv 2602.15763 기반, `glm_moe_dsa` 아키텍처 (Dynamic Sparse Attention)

> [!insight] 핵심 인사이트
> 오픈소스(MIT) + 한국어 강점 + MoE 효율 세 가지를 모두 갖춘 드문 케이스. 중국 오픈소스 LLM의 글로벌 경쟁력 입증.

> [!note] Monday 연관성
> **Monday(이 AI 어시스턴트)는 GLM-5-Turbo 기반**으로 구동된다. GLM-5.1은 동일 계열 최신 MoE 버전.

## 인퍼런스 서비스

- HuggingFace: https://huggingface.co/zai-org
- Together AI, Fireworks AI 파트너십

## 2026-08-28 — `glm5_next` 실험 계열을 **MIT로** 공개

**[[GLM-5.3-Flash]]** (HF 트렌딩 **2위** · 생성 2026-08-25 · **MIT** · **fp8**). 아키텍처 태그는 **`glm5_next`**.

> [!insight] MIT 개방 노선이 차세대 실험판에서도 유지된다
> 같은 배치의 경쟁 모델 [[Qwen3.8-Flash-Next]]는 라이선스가 **`other`** 다. **[[Zhipu-AI]]만 MIT** 로, 볼트가 [[GLM-5]]·[[GLM-5.1]]·[[GLM-5.2]]에서 추적해 온 개방 노선이 **차세대 실험 계열에서도 깨지지 않았다.**
> **fp8 원본 배포**도 주목할 선택이다 — [[unsloth]] 같은 제3자 양자화 재배포를 거치지 않고 **원본이 곧 저정밀 실행본**이다. 볼트가 관측해 온 *"원본 ≫ 양자화 재배포"* 2단 구조를 **1단으로 접는 시도**다.

> [!warning] 다운로드 34건 — 볼트 사상 가장 극단적인 지표 분리
> DL **34** · 좋아요 **1,393** → **좋아요가 다운로드의 41배**. [[Qwen3.8-27B]](DL/좋아요 **264.5**) 대비 **약 11,000배 낮다.**
> **트렌딩 2위가 여기서는 사실상 아무것도 뜻하지 않는다.** 34건은 개발자 본인들과 호기심 몇 명 수준이다.
> 단 **공개 3일차**라 "안 쓰인다"의 증거는 아니다 — 다음 회차 DL 추이가 *관심 선행 → 사용 후행* 가설을 판정한다. 같은 날의 [[Qwen3.8-Flash-Next]](DL 4,810)와 **자연 대조 실험**이 세팅됐다.
> ⚠️ **`arxiv:2602.15763` 태그가 API에 있다**(raw 미기재) — 벤치·아키텍처를 확인할 유일한 공개 경로이나 **미확인**. 크기·컨텍스트·MoE 여부 전량 미확인.

## 관련 페이지
- [[GLM-5.3-Flash]] — `glm5_next`·MIT·fp8 *(NEW 2026-08-28)* · [[Qwen3.8-Flash-Next]] — 같은 주 경쟁 실험판(라이선스 대비)

- [[GLM-5.2]] — 최신 753B 플래그십(1M 컨텍스트, MIT)
- [[GLM-5.1]] — MoE 모델
- [[GLM-5]] — 에이전틱 엔지니어링 전환판
- [[Qwythos-9B]] — 같은 배치 트렌딩 오픈 모델
- [[local-llm]]
