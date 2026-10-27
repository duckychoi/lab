---
title: "Trial by Trace (TraceTrial-Bench) — 하네스 4종 중 '전 기준 통과(Clean)'는 최대 11.7%다. 과제 성공의 31.1%가 하네스 결함을 덮고 있었다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent-harness, benchmark, failure-attribution, claude-code, codex, openclaw, reliability]
created: 2026-10-27
updated: 2026-10-27
sources: [https://huggingface.co/papers/2610.32285, https://github.com/TraceLite-AI/TraceTrial-Bench]
reliability: medium
---

# Trial by Trace: Benchmarking AI Agent Harnesses for Reliability and Failure Attribution

**HF**: https://huggingface.co/papers/2610.32285 · arXiv 2610.32285 · published **2026-10-23** · 제작 **TraceLite AI**(Zhiyong Cao 외) · upvote **123**(볼트 HF API 실측 · 수집기 일치)
**코드**: https://github.com/TraceLite-AI/TraceTrial-Bench — ★13 · MIT · Python 5.2MB · `Task/` `harness_tracer/` `verifier/` `docker/` 실재 ✅ ([[선언된-구현체-공백]] 아님)
**도메인**: `ai-news` · **신뢰도**: ⭐⭐ medium (실행 가능한 코드·Docker 제공 / 단 제작사가 트레이싱 제품사 — 이해관계 아래 참조)

> [!insight] 🏆 핵심 인사이트 ① — **"과제 성공"과 "하네스 신뢰성"은 다른 축이다**
> 초록: *"**31.1% of runs achieve task success despite failing at least one harness criterion**."* README 추가 수치(수집기 미전달): *"Only **8.4%** pass every criterion in both layers."*
> ⇒ 지금까지 볼트가 하네스를 비교할 때 쓴 신호(SWE-bench 류 통과율·★)는 **에이전트 층만 잰다.** 오류를 조용히 삼키고도 결과물이 맞으면 성공으로 집계된다 → [[하네스-설계-축]] 에 **"관측 가능한 실패" 축**이 빠져 있었다.

> [!insight] 🏆 핵심 인사이트 ② — **1위가 축마다 다르다** (README 표 · 9모델×95과제 평균 · 하네스당 855셀)
>
> | 하네스 | Agent Pass | Agent Score | Harness Macro | **Clean** | Overall |
> |---|--:|--:|--:|--:|--:|
> | [[anthropic-claude-code\|Claude Code]] | **44.0** | **75.9** | 71.2 | 9.1 | **73.5** |
> | [[openai-codex\|Codex]] | 35.8 | 70.7 | 🔴 **59.8** | 🔴 **2.8** | 65.2 |
> | DeepSeek Harness | 40.0 | 73.3 | 68.8 | 9.8 | 71.0 |
> | [[openclaw\|OpenClaw]] | 38.2 | 71.7 | **72.0** | **11.7** | 71.8 |
>
> ⇒ 과제 성공은 Claude Code, 하네스 신뢰성은 OpenClaw. **Codex 는 Clean 2.8% — 36칸 중 최저.** Harness Macro 범위 12.2%p 가 수집기 "59.8~72.0%" 의 정체다.

> [!warning] 주의
> - 🔴 **이해관계**: 제작사 TraceLite AI 는 실행 트레이스 도구 회사(`tracelite.ai` 리더보드 운영). "트레이스를 봐야 실패가 보인다"는 결론이 **자사 제품 범주를 정당화**하는 구조 → [[인용-부호]] 처럼 결론 부호를 따로 의심할 것. 다만 코드·과제 공개로 재현 가능성은 열려 있다.
> - ⚖️ 하네스 판정에 **LLM 평가자**(MEA 모듈 증거 제공) 사용 — 평가자 모델·일치도는 초록 미기재.
> - ⚖️ 95과제는 **"mechanism-oriented"**(하네스 기제 겨냥) — 일반 코딩 작업 분포가 아니다. Clean 비율을 실사용 신뢰도로 직역 금지.
> - 📌 9개 모델 명단·모델별 수치는 기술보고서(tracelite.ai) 에만 있음 — 볼트 미열람.

## 도메인별 추출 (ai-news)
- **신뢰도**: upvote 123 · ★13 · 코드/Docker 공개 · 제3자 재현 없음
- **즉시 활용**: **YES(조건부)** — 사용자가 Claude Code 를 주력으로 쓰므로 "Agent 1위·Clean 9.1%" 는 곧 **작업 10건 중 9건은 어딘가에서 하네스 기준을 어긴다**는 뜻. 장시간 자동 작업(크론 리서치 에이전트 등)의 로그 감사 필요성 근거.
- **6개월 영향력**: 하네스 비교가 ★·통과율 → **트레이스 기반 2층 평가**로 이동하는 첫 공개 벤치. [[ECC]]·[[hallmark]]·[[cindy]]·[[thinkrail]] 같은 하네스 부가물도 같은 잣대에 올라갈 수 있다(추정).
- **허와 실**: "31.1% 숨은 결함"은 실측 · "어느 하네스가 낫다"는 축 선택에 따라 뒤집힘.
- **액션**: 볼트 크론 에이전트의 덮어쓰기 사고([[크론-덮어쓰기-소실]])는 정확히 "과제 성공(노트 생성) + 하네스 결함(기존 파일 파괴)" 유형 — TraceTrial 의 *lifecycle/verification* 축으로 분류 가능.

## 관련 페이지
- [[하네스-설계-축]] · [[하네스형-에이전틱-RL]] · [[AI-에이전트-프레임워크]] · [[에이전트-스킬]]
- [[anthropic-claude-code]] · [[openai-codex]] · [[openclaw]] · [[pi-agent-harness]]
- 같은 배치: [[DynaFlow]] · [[Trajectory2Gym]] · [[ECC]] · [[cindy]] · [[thinkrail]]
- [[인용-부호]] · [[크론-덮어쓰기-소실]] · [[ai-news]]

## 원본
- https://huggingface.co/papers/2610.32285 · README https://github.com/TraceLite-AI/TraceTrial-Bench (볼트 열람 · 표 전사)
- 볼트 실측(2026-10-27T09:0xZ): HF upvote 123 · GitHub ★13 · contents 13항목 · languages Python 5,235,308B
