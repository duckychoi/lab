---
title: BAAI (Beijing Academy of AI) — 임베딩 바닥 인프라를 MIT로 푸는 조직
type: entity
domain: ai-news
tags: [entity, huggingface, embedding, retrieval, china, open-source, infrastructure]
created: 2026-09-16
updated: 2026-09-16
sources: [bge-small-en-v1.5.md]
reliability: medium
---

# BAAI (Beijing Academy of Artificial Intelligence)

**대표 산출물**: [[bge-small-en-v1.5]] (DL **64,638,739**/월 · ♥582 · **MIT**) · BGE 패밀리(small/base/large · en/zh) · FlagEmbedding

> [!insight] 이 조직의 위치 — **모델이 아니라 바닥을 깐다**
> 🎯 **BGE는 RAG 파이프라인 1단계(후보 생성)의 사실상 표준 중 하나다.** 월 6,464만 다운로드는 **사람이 고르는 숫자가 아니라 파이프라인에 박혀 자동으로 받아지는 숫자**다.
> 📌 **라이선스가 MIT다.** 같은 배치 [[ms-marco-MiniLM-L6-v2]](Apache-2.0)와 함께 **RAG 2단 파이프라인 전체가 허용적 라이선스로 구성 가능**하다 — 이것이 채택률의 구조적 이유 중 하나다.

> [!note] 문서화 습관 — 방대하고, 그래서 검증 가능하다
> [[bge-small-en-v1.5]] 모델카드는 **3,074행**이다. `model-index` 에 **68개 벤치 결과**를 통째로 싣고 **변경 이력까지 날짜별로** 남긴다.
> 🎯 **볼트가 수집기 요약의 오류(v1.5가 프리픽스 의존을 *줄인* 것)를 잡아낼 수 있었던 것은 이 카드가 변경 이력을 적었기 때문이다.** **수치를 다 공개하는 카드는 반박도 가능하게 만든다.**

> [!warning] ⚠️ 2년 7개월 미수정
> `bge-small-en-v1.5` 최종 수정 **2024-02-22**. 🎯 **"수정이 없다"는 완성과 방치를 구분하지 못한다** — 다만 현재도 월 6,464만 DL이 나오므로 **실사용은 계속되고 있다.**

> [!note] 볼트 내 중국 오픈 축
> [[Alibaba]](Qwen) · [[DeepSeek]] · [[MiniMax]] · [[Moonshot AI]] · [[SenseTime]] · [[m-a-p]] · **BAAI**
> 📌 다른 조직들이 **생성 모델**을 낼 때 BAAI는 **검색 인프라**를 낸다 — **경쟁 축이 다르다.**

## 관련 페이지
- [[bge-small-en-v1.5]] — 대표 산출물
- [[ms-marco-MiniLM-L6-v2]] — RAG 2단계 직렬 파트너
- [[HuggingFace]] · [[측정도구-먼저-반증]]
- [[ai-news]]
