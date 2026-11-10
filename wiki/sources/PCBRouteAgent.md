---
title: "PCBRouteAgent — 전역 배선 계획과 KiCad 네이티브 실행을 분리한 멀티모달 PCB 배선 에이전트. clean-pass 100·94.9·100%, 가장 어려운 D3-C 는 40%"
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent, eda, pcb, kicad, multimodal]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/papers/2611.08175]
reliability: medium
---

**논문**: [2611.08175](https://huggingface.co/papers/2611.08175) *How Close Are LLM Agents to Becoming PCB Routing Engineers?* · 업보트 **37** · 코드 [chip-ai-agent/PCBRouteAgent](https://github.com/chip-ai-agent/PCBRouteAgent) ★35(수집 시 31) · BSD-3-Clause · 생성·푸시 2026-11-06

## 핵심 인사이트
> [!insight] 제목의 질문에 초록이 스스로 답한다 — 쉬운 분할은 끝났고 어려운 분할은 40%다
> **Global Routing Planner**(보드 이미지 + 구조화된 전기·기하 정보 → 연결 토폴로지 · 배선 순서 · 통로 · 층 전환)와 **Detailed Routing Executor**(KiCad 네이티브 라우터 + 제한된 국소 복구)를 나눈다. 못 푼 실패는 구조화 피드백으로 돌려 **이미 승인된 배선은 보존한 채 가이드만 수정**한다. PCBWorld-Bench 4개 분할 247개 보드에서 clean-pass D2 **100%** · D3-A **94.9%** · D3-B **100%** · **D3-C 40%**.

> [!warning] 읽는 법
> - 100%가 둘이라는 것은 그 분할이 이 방법에 대해 **포화**됐다는 뜻이다([[천장-기준선]]). 변별력은 D3-C 한 줄에 있다.
> - 실보드 3개 서브셋에서 "최고 베이스라인 대비 +13.9 · +36 · +10%p" — **베이스라인 이름과 절대값이 초록에 없다.** 분할별 보드 수(247 의 분해)도 없어 40%의 분모를 알 수 없다.
> - 수집기 "소속 표기 없음" — 볼트도 papers API 에서 소속을 확인하지 못했다.

## 도메인별 추출 (ai-news)
- **신뢰도**: 업보트 37 · ★35 · 논문 있음 · 자체 벤치 계열(PCBWorld-Bench) 평가.
- **즉시 활용**: NO — PCB 설계 워크플로우가 없다.
- **6개월 영향력**: "계획자는 LLM · 실행자는 도메인 네이티브 도구 · 실패만 되돌림" 구조가 EDA 밖(영상 편집 · 코드 수정)에도 그대로 옮겨진다. 오늘 배치 [[A2-MEAS]] · [[Viggle-Remake]] 의 MCP 컷 단위 자가검수와 같은 골격.
- **허와 실**: 실 = 네이티브 라우터를 써서 설계 규칙 위반 가능성을 도구에 맡김. 허 = 가장 어려운 분할 60% 실패.
- **액션**: 없음.

## 관련 페이지
- [[국소-수리-원리]] · [[천장-기준선]] · [[A2-MEAS]] · [[AI-에이전트-프레임워크]] · [[임계-의존-성공률]]

## 원본
- 출처: https://huggingface.co/papers/2611.08175
- 확인 범위: HF papers API 초록 전문 · GitHub API 메타 · 🔴 본문 · 코드 미열람
- 신뢰도: ⭐⭐ (업보트 37 · ★35)
