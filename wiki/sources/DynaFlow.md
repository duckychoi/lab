---
title: "DynaFlow — 메인 에이전트만 학습해 서브에이전트 조율 코드를 직접 쓴다. 88.08%(+10.90%p)는 'Forced 모드' 수치다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, multi-agent, orchestration, workflow-synthesis, sft, qwen3.5]
created: 2026-10-27
updated: 2026-10-27
sources: [https://huggingface.co/papers/2610.34467, https://github.com/amiya-special/Dynaflow]
reliability: medium
---

# DynaFlow: Learning Free-Form Multi-Agent Orchestration

**HF**: https://huggingface.co/papers/2610.34467 · published **2026-10-25** · **National University of Singapore**(Ruhao Liu · Xinchao Wang 외 4인) · upvote **96**(수집기 90 · +6)
**코드**: https://github.com/amiya-special/Dynaflow — ★8 · MIT · Python 113KB + TS 40KB · `workflow_runtime/` `tool_runtime/` `src/` 실재 ✅
**신뢰도**: ⭐⭐ medium

> [!insight] 핵심 인사이트 — **"협업 구조"를 설계하지 말고 행동 공간에 넣어라**
> 기존 멀티에이전트는 고정 협업 구조(역할·순서)를 쓴다 — 같은 배치의 [[TradingAgents]](애널리스트→리서처→트레이더→리스크)가 전형. DynaFlow 는 메인 에이전트가 **언제 협업할지 판단하고, 순차/병렬 실행·정보 교환·검증을 담은 실행 가능한 프로그램을 매번 생성**한다.
> 🎯 **학습 분리**: 메인만 SFT, **서브에이전트는 전부 고정** ⇒ "조율 능력"과 "실행자 능력"의 기여를 분리해 잰다. 개선이 오케스트레이션에서 왔다는 주장이 이 설계 덕에 성립한다.
> 📌 사후 분석: 학습 후 **상류 출력을 명시적으로 사용·검증·정제**하는 빈도가 늘었다 ⇒ 저자 결론 *"cross-stage information flow"* 가 핵심 차원.

> [!warning] 주의
> - ⚖️ **88.08% 는 "Forced 모드"** — 협업을 강제한 설정. 에이전트가 협업 여부를 스스로 고르는 기본 모드 수치는 초록에 없다(수집기는 모드 표기 보존 ✅).
> - ⚖️ +10.90%p 는 **"strongest evaluated baseline"** 대비 · 같은 Qwen3.5-27B 백본 — 백본 통제는 좋으나 베이스라인 목록은 미열람.
> - 📌 학습 데이터: 증류 궤적 → **근거 없는 전제·편향 검증·정보흐름 결함** 필터 후 정제 — [[Trajectory2Gym]] 의 근거성 필터와 같은 처방.

## 도메인별 추출 (ai-news)
- **즉시 활용**: 부분 — 학습 없이도 **"오케스트레이터가 워크플로 코드를 쓰게 한다"** 패턴은 Claude Code 서브에이전트 운용에 그대로 이식 가능(프롬프트 수준).
- **대체 관계**: 고정 파이프라인형([[TradingAgents]]) ↔ 자유형. 볼트 [[AI-에이전트-프레임워크]] 의 "역할 사전정의" 가정에 대한 반례.

## 관련 페이지
- [[AI-에이전트-프레임워크]] · [[하네스-설계-축]] · [[에이전트축-분기]] · [[Qwen]]
- 같은 배치: [[TradingAgents]] · [[Trajectory2Gym]] · [[Trial-by-Trace]]
- [[ai-news]]

## 원본
- https://huggingface.co/papers/2610.34467 · 볼트 실측(2026-10-27): upvote 96 · ★8 · contents 14항목
