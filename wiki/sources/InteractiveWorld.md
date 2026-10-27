---
title: "InteractiveWorld (Meta) — AI가 '사람'에게 지시해 물리 작업을 끝내게 하는 폐루프 환경. 최강 모델(Claude Fable 5.1)도 장기 과제 20%·25%"
type: source
domain: ai-news
tags: [ai-news, hf-paper, egocentric, wearable, mllm-assistant, benchmark, simulation, meta, human-in-the-loop]
created: 2026-10-27
updated: 2026-10-27
sources: [https://huggingface.co/papers/2610.33966, https://github.com/facebookresearch/InteractiveWorld]
reliability: medium
---

# InteractiveWorld: A Verifiable Human-Centric Environment for Building Better Interactive MLLM Assistants

**HF**: https://huggingface.co/papers/2610.33966 · published **2026-10-25** · **Meta**(Qinsi Wang · Zechun Liu 외) · upvote **78**(수집기 일치)
**코드**: https://github.com/facebookresearch/InteractiveWorld — ★9 · license NOASSERTION(🔴 SPDX 미판별 · 상업 이용 전 LICENSE 원문 확인) · Python 6.7MB · `simulator/` `benchmark/` 실재 ✅
**신뢰도**: ⭐⭐ medium

> [!insight] 🏆 핵심 인사이트 — **수집기 요약에서 빠진 것이 이 논문의 결론이다**
> 초록: *"Experiments with 12 frontier MLLMs show they are **still far from reliable assistants**. Even the strongest model, **Claude Fable 5.1**, achieves **at most 20% and 25%** on long-horizon Guidance and Planning tasks."*
> ⇒ 수집기 한줄요약은 환경·벤치 구성(6카테고리 120과제)만 적고 **부정적 결론을 누락**했다 — [[인용-부호]]·10-06 요청 3("유리한 표면만 남기지 않는다")의 위반 사례.
> 🎯 설계 전환: 로봇 중심 시뮬레이터와 달리 **행동 주체가 '시뮬레이션된 인간'** — 어시스턴트는 지시만 하고, 인간 에이전트가 관찰·이해·독립 행동한다. 보상은 **상태 기반·검증 가능**.

> [!warning] 주의
> - ⚖️ "인간"은 **시뮬레이션된 인간 에이전트**(아마 LLM 구동 — 초록 미명시) — 실제 사람의 오해·지연을 재현하는지는 별개 문제 → [[인간-기준선-조건]].
> - ⚖️ "at most" = 상한 표기. 모델별 표는 본문(미열람).
> - 📌 "first verifiable environment" · "first dynamic benchmark" — 최초 주장 2건, 볼트 미검증.

## 도메인별 추출 (ai-news · slam-3dgs 접점)
- **slam-3dgs 연결**: 에고센트릭(1인칭) 장면 이해 → 지시 생성은 웨어러블·휴머노이드 공통 과제. [[리서치-휴머노이드-로봇-SLAMVLA로컬LLM-기반-제어-기술-2026년-최신-동향]] 의 "LLM 은 초 단위 재계획" 층이 바로 이 벤치가 재는 능력.
- **6개월 영향력**: Meta 스마트글라스 어시스턴트 평가 기준으로 쓰일 가능성(추정). 현 수준(장기 과제 ≤25%)은 **상용 "항상 켜진 안내자"가 아직 멀다**는 반증 자료.

## 관련 페이지
- [[Meta]] · [[인간-기준선-조건]] · [[인용-부호]] · [[천장-기준선]]
- 같은 배치: [[StreamVibe]] · [[Trial-by-Trace]]
- [[ai-news]] · [[slam-3dgs]]

## 원본
- https://huggingface.co/papers/2610.33966 · 볼트 실측(2026-10-27): upvote 78 · ★9 · contents 15항목
