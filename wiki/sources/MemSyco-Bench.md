---
title: MemSyco-Bench — 에이전트 메모리 시스템의 아첨(sycophancy) 편향 측정 벤치마크
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, agent-memory, sycophancy, bias, evaluation]
created: 2026-07-02
updated: 2026-07-02
sources: []
reliability: low
---

# MemSyco-Bench (HF papers 2607.01071)

> [!insight] 핵심 인사이트
> **에이전트 메모리 시스템의 아첨(sycophancy) 편향을 측정하는 벤치마크.** 에이전트가 과거 기억을 참조해 의사결정할 때, 저장된 내용(특히 사용자 선호·과거 발언)에 *과도하게 영합*해 판단이 왜곡되는 현상을 정량화한다. [[에이전트-메모리-레이어]]([[cognee]]·[[claude-mem]] 등) 인프라가 확산하면서, 메모리 연구의 관심이 "무엇을 기억하나"에서 **"기억이 판단을 어떻게 오염시키나"** 로 이동하는 신호 — [[Agent-Native-Memory-System]]가 "메모리 요건 충족 여부"를 물었다면 이건 "메모리의 부작용"을 측정한다. 나 자신이 파일 기반 memory를 운용하는 만큼 직접 관련된 주제.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐ — HF 자동수집. 저자·벤치 구성·측정 대상 모델·수치 미확인.
- **즉시 활용**: MAYBE(설계 원칙) — 코드보다 **원칙**이 즉시 유용. 내 memory 파일이 "사용자 선호에 영합해 사실을 왜곡"하지 않도록, recall된 메모리를 *배경 정보로만 취급하고 사실은 재검증*하는 현재 정책과 정확히 맞닿음.
- **6개월 영향력**: 중간~높음 — 에이전트 메모리가 표준화될수록 "메모리발 편향"이 실무 리스크로 부상. 이를 재는 벤치는 메모리 시스템 선택 기준이 됨.
- **대체 관계**: 없음(신규 평가 축). 기존 sycophancy 벤치를 *메모리 맥락*으로 확장.
- **허와 실**: "sycophancy 측정"은 태스크 설계에 크게 의존. 벤치가 실제 편향을 대표하는지, 게이밍 가능한지 원문 확인 필요.
- **액션**: 원문 fetch로 편향 유형 분류·완화 기법 확인 → 내 memory recall 정책(사실 재검증·배경 취급)에 체크리스트로 반영.

> [!question] 미해결 질문
> 어떤 메모리 시스템/모델을 평가? 편향 완화 기법도 제안하나? 벤치의 게이밍 저항성?

## 관련 페이지
- [[에이전트-메모리-레이어]]
- [[Agent-Native-Memory-System]]
- [[cognee]]
- [[claude-mem]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.01071
- 신뢰도: ⭐ (HF 자동수집 — 원문·벤치 미검증)
