---
title: alphaXiv
type: entity
domain: ai-news
tags: [ai-news, research-tools, arxiv, open-source, rust]
created: 2026-09-12
updated: 2026-09-12
sources: [OpenResearch.md]
reliability: high
---

# alphaXiv

> [!insight] 한 줄
> **arXiv 논문 위에 토론·리뷰 층을 얹는 서비스**로 출발해, 2026년 리서치 에이전트 워크스페이스 [[OpenResearch]] 를 공개했다.

## 왜 기록하는가
[[OpenResearch]] 를 평가할 때 **제작 주체가 정보**다. 리서치 에이전트 도구는 오늘 배치에만 세 개가 걸렸는데([[hyperresearch]]·[[OpenResearch]]·[[WeKnora]]), 그중 **논문 유통을 실제로 운영해 본 팀이 만든 것은 이것뿐**이다.

## 산출물
- **[[OpenResearch]]** (2026-09-12 인제스트) — ⭐1,469 · fork 105 · **Rust** · MIT · created 2026-06-07.
  로컬 우선 병렬 리서치 워크스페이스. **모델뿐 아니라 하네스까지 세션 단위 교체**(Claude Code / Codex / OpenCode / Cursor). 로컬 · SSH · Slurm 동일 실행.
- 관리형 컴퓨트를 `openresearch.sh` 에서 제공 — **오픈소스 + 호스팅 병행 모델**.

> [!note] 관측
> 도구가 **Rust** 다. 같은 주에 [[llm_wiki]](Rust 백엔드)도 나왔다 → **로컬 우선 에이전트 도구가 Python을 벗어나는 흐름**의 두 번째 사례. 단일 바이너리 배포·낮은 기동 비용이 로컬 우선 설계와 직결된다.

> [!question] 미확인
> 법인 실체·규모·자금 조달 **미조사**. 서비스(alphaxiv.org)는 공개적으로 존재하나 **볼트가 직접 확인한 것은 GitHub 조직과 레포까지**다.

## 관련 페이지
- [[OpenResearch]]
- [[hyperresearch]]
- [[에이전트축-분기]]
- [[ai-news]]
