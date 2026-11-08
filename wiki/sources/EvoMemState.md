---
title: "EvoMemState — 사실 나열형 메모리에 '관계 상태'와 RL 로 만든 '추론 상태'를 더한 개인 에이전트 기억. 평균 1위, 안전 점수는 Mem0 보다 낮다"
type: source
domain: local-llm
tags: [local-llm, agent-memory, personal-agent, long-term-memory, rl, ontology, mem0, a-mem, hf-paper, xmu]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/papers/2611.03743]
reliability: medium
---

**논문**: arXiv 2611.03743 · HF 업보트 **32**(볼트 11-08 · 수집기 21) · XMU · 코드 [XMUDeepLIT/EvoMemState](https://github.com/XMUDeepLIT/EvoMemState) ★26 · 🔴 **라이선스 미지정**(API `license: null`)

## 핵심 인사이트
> [!insight] 메모리의 단위를 "사실"에서 "사실 간 관계 + 지금 요청에서의 우선순위"로
> [[mem0]]·A-MEM 류는 사실을 독립 항목으로 저장해 *"새 사실이 옛 사실을 갱신·제약·충돌시키는 관계"*를 놓친다. EvoMemState 는 ① 온톨로지 기반으로 영속 사실 + **Relational State**(유효성·범위·관계) ② **RL 로 메모리 사용 경험을 정책에 내재화**해 요청별 Reasoning State 생성 ③ 둘을 합쳐 응답. ⇒ "언제 어떤 기억을 적용하나"를 학습 대상으로 만든 것.

> [!warning] 평균 1위 ≠ 전 항목 1위
> 수집기 README 판독(응답모델 Qwen3-8B): Overall **59.9** vs SimpleMem 53.6 · MemoryBank 49.9 · A-MEM 49.6 · Mem0 39.2. 그러나 **MemTrapBench Safety 62.3 < Mem0 69.3 · LightMem 69.9** — 수집기가 ⚠️ 로 보존했다(✅ 유지 요청 이행). 기억을 더 적극적으로 적용할수록 함정 질문에 더 걸리는 트레이드오프로 읽힌다(볼트 추론). 볼트는 README 표를 재열람하지 않았다.

## 도메인별 추출 (local-llm)
- **메모리 아키텍처**: 구조화 외부 메모리(온톨로지) + RL 정책. RAG 단독 아님.
- **Hermes 적용**: 아이디어 차용 YES — 볼트/봇 기억에 "이 사실은 언제까지 유효한가·무엇을 대체했나" 필드를 두는 것만으로 Relational State 의 핵심 효과를 근사할 수 있다. 코드 재사용은 라이선스 미지정이라 보류.
- **트레이드오프**: 평균 +6.3 vs 안전 −7.
- **오픈소스 구현체**: 있으나 라이선스 없음.

## 관련 페이지
- [[mem0]] · [[에이전트-메모리-레이어]]
- 같은 배치: [[rivet]](런타임) · [[pipeshub-ai]](사내 RAG)
- 같은 날 크론: [[리서치-LLM-장기기억에이전트-메모리-아키텍처-SOTA-2026년-최신]]

## 원본
- 출처: https://huggingface.co/papers/2611.03743
- 확인 범위: HF papers API 초록(볼트 11-08) · GitHub API · README 결과표는 수집기 판독만
- 신뢰도: ⭐⭐
