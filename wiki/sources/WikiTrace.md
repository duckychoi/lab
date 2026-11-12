---
title: "WikiTrace — 교훈을 원본 궤적에 연결해 '메모리 유발 성능 저하'를 줄이는 에이전트 메모리 (arXiv 2611.14320)"
type: source
domain: local-llm
tags: [local-llm, agent-memory, memory-degradation, provenance, kaist]
created: 2026-11-12
updated: 2026-11-12
sources: [https://huggingface.co/papers/2611.14320]
reliability: medium
---

**논문**: [arXiv 2611.14320](https://huggingface.co/papers/2611.14320) *Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents* · 업보트 **61** · 저자 4명(Yukyeong Lee · Yumin Choi · Jinheon Baek · **Sung Ju Hwang**) · 코드 github.com/yukyeongleee/wikitrace (HF papers API 볼트 실측)

> [!note] 계수기 차이
> 수집기: 같은 시각 `api/papers` 61 ↔ `api/daily_papers` 57. 볼트 재조회도 61. → [[계수기-배수]] 계열의 "같은 지표, 다른 엔드포인트" 사례.

## 핵심 인사이트
> [!insight] 메모리는 해가 될 수 있다 — 그리고 해결책은 "출처를 붙여 두는 것"이다
> **메모리 유발 성능 저하**: 메모리 없이는 풀던 과제를 메모리 때문에 틀린다. 원인 진단 — 교훈이 **성공/실패 라벨만으로 추론**되고 **원본 궤적 없이** 제공돼 검증할 길이 없다. WikiTrace 는 각 교훈을 [간결한 인사이트 → 성공/실패 이유 요약 → 원본 궤적] 링크로 저장하고, 인사이트가 ① 세부 부족 ② 다른 인사이트와 충돌 ③ **실패 과제 유래**일 때만 터미널 도구로 링크를 내려가 확인·수정한다. 에이전트 벤치 5종에서 기존 메모리 방식과 **"같은 인사이트만 준 기준선"** 을 일관되게 상회하고 저하도 줄였다(초록).
> ⇒ 🎯 **이 볼트 자체가 이 구조다** — wiki 페이지(인사이트) → source 페이지(요약) → 원본 URL(궤적), 그리고 "출처를 연다"는 검증 하강. 같은 날 크론 메모리 노트가 인용 논문의 반대 결론을 놓친 것([[인용-부호]])이 정확히 "링크를 내려가지 않은" 사례다.

> [!warning] 수치 0
> 초록에 성공률·저하율·토큰 비용·지연이 없다. 링크 하강의 추가 비용은 본문 확인 필요. "같은 인사이트만 준 기준선"을 이긴다는 것이 이 논문의 핵심 통제 실험이다(링크의 효과를 분리) — 폭은 미상.

## 도메인별 추출 (local-llm · 에이전트 메모리)
- **메모리 아키텍처**: 외부 텍스트 메모리 + **증거 링크(provenance)** + 조건부 하강. RAG/KV/압축 중에서는 "구조화 외부 DB"에 해당하되 핵심은 검색이 아니라 **검증 경로**.
- **Hermes 적용**: YES(설계 차용) — 에이전트 메모리에 저장하는 교훈마다 원본 대화/로그 경로를 같이 저장하고, 실패 유래 교훈은 사용 전 원본 확인을 강제.
- **트레이드오프**: 정확도 ↑ · 저하 ↓ vs 하강 시 토큰·지연 ↑(수치 미상).
- **오픈소스 구현체**: yukyeongleee/wikitrace(★7, 수집기).

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[LLM-Wiki]] · [[인용-부호]] · [[mem0]] · [[리서치-LLM-에이전트-메모리-아키텍처-최신-동향-2026]] · [[계수기-배수]]

## 원본
- 출처: https://huggingface.co/papers/2611.14320
- 확인 범위: HF papers API 초록 전문 · 저자 목록 · 🔴 본문·코드 미열람
- 신뢰도: ⭐⭐ (업보트 61 · 코드 공개)
