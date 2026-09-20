---
title: VectifyAI
type: entity
domain: ai-news
tags: [rag, retrieval, benchmark, 오픈소스]
created: 2026-09-20
updated: 2026-09-20
sources: [PageIndex.md]
reliability: high
---

# VectifyAI

GitHub `VectifyAI` · pageindex.ai. **벡터DB 없는 추론 기반 검색을 미는 조직.**

> [!insight] 자리의 성격 — **엔진·벤치·데이터셋을 세 레포로 나눠 낸다**
> - [[PageIndex]] — 본체(★**35,766** · MIT)
> - `VectifyAI/PageIndex-OSS-Benchmark` — 평가 러너·결과
> - `VectifyAI/MMLongBench-Doc-V2` — 평가 데이터셋
> 🎯 **[[k2-fsa]] 가 *"논문+코드+가중치+데모 네 표면을 세트로 내는 조직"* 이었다면, VectifyAI는 *"엔진+러너+데이터 세 표면"* 이다.** 검색 쪽에서는 가중치 대신 **데이터셋**이 그 자리에 온다.

> [!note] ✅ 벤치 설계에 규율이 있다
> *"Every question's answer is a fact stated in running text, so a wrong answer is a **retrieval or reading failure, not a reasoning one**."* — **실패 모드를 격리하려고 데이터를 골랐다.** 62문항 · 34 PDF · 1,945쪽.
> ✅ 비용을 **텍스트 수치**로 공개: 색인 $0.001/page · 13초~4.5분 · 원문 투입 대비 52쪽 2.1배 / 420쪽 **16.6배** / 805쪽 미적재.

> [!warning] ⚠️ 자기 벤치·자기 데이터셋이다
> MMLongBench-Doc-V2 도 VectifyAI 소유다. [[m-a-p]] 가 [[YuE2-3B]] 를 자기 WildSongBench로 잰 것과 **형태가 같다**.
> 🎯 **단 성격이 낫다** — m-a-p는 비교군을 골라 보였고, 여기는 **러너·데이터·결과를 전부 열어 뒀다**. *닫힌 자기평가*가 아니라 *열린 자기평가*.
> 🔴 **정확도 수치가 그림 안에만 있다**(`results-light.png`). 비용은 텍스트, 정확도는 차트 — 볼트가 전사하지 못했다.

## 관련 페이지
- [[PageIndex]] · [[관련성-판단-주체]] · [[m-a-p]] · [[k2-fsa]] · [[docling]] · [[ai-news]]
