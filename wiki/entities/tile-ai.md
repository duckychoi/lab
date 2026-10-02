---
title: "tile-ai — 커널 DSL 조직"
type: entity
domain: ai-news
tags: [entity, organization, github, kernel, compiler, tvm]
created: 2026-10-02
updated: 2026-10-02
sources: [TileLang.md]
reliability: medium
---

# tile-ai

**GitHub**: https://github.com/tile-ai

> [!insight] 핵심
> [[TileLang]] 의 제공 조직. **GPU/CPU/NPU 커널용 Pythonic DSL** 을 TVM 인프라 위에 만든다.
> 📌 **볼트가 수집한 조직 중 가장 저수준(커널 컴파일러) 축**이다 — 기존 수집은 에이전트 하네스·모델 제공자에 쏠려 있었다.

> [!note] 확인된 것
> - [[TileLang]] created **2024-10-03** — 약 2년 운영(오늘 기준). ★8,185 는 폭발이 아니라 **누적**이다.
> - LICENSE 저작권자 표기: **`Copyright (c) Tile-AI.`**
> - 🎯 LICENSE 에 **2024-12-01 ~ 2025-03-14 기간 한정 Microsoft 협업 조항**이 삽입돼 있다(기간 종료) → [[메타데이터-부재-추론]] `NOASSERTION` 원인
> - 하드웨어별 경로(SM75 · Blackwell SM100 · SM120 · Apple M5 · **화웨이 Ascend 950 NPU**)를 **개별 PR 로 축적**하는 운영 방식

> [!warning] 🔴 미확인
> 조직 실체(기업/연구소/커뮤니티 여부) · 구성원 · 자금 출처 · 다른 저장소 보유 여부 **전부 미조회**. **GitHub org 페이지 미열람.**

## 관련 페이지
- [[TileLang]] — 주 저장소 · [[메타데이터-부재-추론]] · [[하네스-설계-축]] — 최하층
