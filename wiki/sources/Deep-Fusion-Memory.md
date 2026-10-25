---
title: "Deep Fusion Memory (DFM) — 백본을 얼린 채 청크 단위 메모리를 예측해 은닉상태에 게이트 크로스어텐션으로 융합. 추론 시 검색 0회"
type: source
domain: local-llm
tags: [local-llm, agent-memory, parametric-memory, cross-attention, frozen-backbone, rag-대안, hf-paper, 코드없음]
created: 2026-10-25
updated: 2026-10-25
sources: [MemAdapter.md]
reliability: medium
---

# Deep Fusion Memory: A Chunk-Level Parametric Memory for LLMs

**HF**: https://huggingface.co/papers/2610.25100 · published 2026-10-18
**실측(2026-10-25 KST)**: upvote **48**(수집기 일치 · 10-23 목록 7위) · 저자 Rubin Wei · Siyuan Sun · Hao Sun 외 · 소속 표기 없음 · `githubRepo` **None**(🔴 코드 미공개)
**도메인 재분류**: 수집기 `ai-news` → **`local-llm`**(에이전트 메모리 아키텍처 템플릿 해당)
**신뢰도**: ⭐⭐ (초록 수치 있음 · 코드 없음 · 재현 불가)

> [!insight] 핵심 인사이트 — **메모리의 "구축 비용"을 1급 지표로 올렸다 — 검색 쿼리 32배 · 검색 항목 2048배 감소**
> 초록: *"Compared with existing parametric memory approaches, which often construct **token-level** memory targets, DFM requires **32× fewer retrieval queries and 2048× fewer retrieved items**"* ⇒ 🎯 배수의 출처가 구조적이다 — **토큰 단위 → 청크 단위**로 바꾸면 청크 길이만큼 쿼리가 준다(32 = 청크 길이로 추정). 2048 은 쿼리당 항목 수 감소까지 곱한 값으로 보인다(추정 · 본문 미확인).
> 📌 **[[local-llm]] 메모리 분류(RAG/KV/압축/외부DB)에서 위치**: 외부DB 를 **학습 시에만** 쓰고 추론 시엔 **파라미터(크로스어텐션 모듈)** 에 둔다 ⇒ RAG 와 파인튜닝 사이의 **"증류된 검색"**. [[MemAdapter]](10-06) 와 같은 계열(얼린 백본 + 부착 메모리).

> [!warning] 🔴 수치 단위가 섞여 있다
> QA 6과제: *"performs better over the strongest baseline by **12.71%**"* — 상대(%)인지 절대(%p)인지 초록이 밝히지 않음. 도메인 적응: *"average gains of 6.51 and 4.38 **points**"* — 이쪽은 절대 점수. ⇒ 한 초록 안에서 두 단위 → [[단위-불일치]]. 볼트는 12.71 을 **"12.71%(단위 미확정)"** 로만 인용한다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 백본 동결 + 부착 모듈이라 7B~8B(Mistral-7B-v0.3 · Qwen3-8B-Base) 에서 실험됨 ⇒ 로컬 GPU 1장 범위. 지연시간 수치 없음(🔴 "검색 불필요" 이득을 시간으로 안 적었다)
- **메모리 아키텍처**: 파라메트릭 메모리 · 청크 단위 · 게이트 크로스어텐션 · 추론 시 검색 없음
- **Hermes 적용**: **NO(지금)** — 코드 미공개. 개념만 차용 가능: 자주 묻는 코퍼스는 검색 대신 어댑터로 굽는다
- **트레이드오프**: 코퍼스가 바뀌면 재학습 필요(검색 대비 갱신성 열위) — 초록에 언급 없음
- **오픈소스 구현체**: 없음

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[MemAdapter]] · [[RAG vs LLM-Wiki]] · [[단위-불일치]]
- [[리서치-LLM-장기기억에이전트-메모리-아키텍처-SOTA-2026]] — 같은 날 크론 메모리 노트
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/papers/2610.25100
- 신뢰도: ⭐⭐ (HF upvote 48 · 코드 없음)
