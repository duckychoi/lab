---
title: "tradermonty/claude-trading-skills — 매매 신호가 아니라 "결정 절차"를 스킬 74개로 묶은 툴킷"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, claude-skills, finance, trading, 금융-ai]
created: 2026-11-14
updated: 2026-11-14
sources: [https://github.com/tradermonty/claude-trading-skills]
reliability: medium
---

**레포**: [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) · ★**4,352** · fork 883 · MIT · Python · repo id 1079356098 · created 2025-10-19 · pushed 2026-11-14T08:58Z (GitHub API 볼트 실측). `skills/` 디렉터리 항목 **74개**(GitHub contents API 볼트 재확인 — 수집기와 일치).

## 핵심 인사이트
> [!insight] AI 에게 "무엇을 살까"가 아니라 "내 절차를 지켰나"를 묻게 한다
> 시장 폭 · 상승추세 분석, 노출 한도 코치, VCP 스크리너, 배당 포트폴리오 점검, 매매일지 · 사후 분석, 월간 성과 리뷰 등을 YAML 워크플로 매니페스트로 엮는다(일일 15분 시황 점검 `market-regime-daily` · 매매 기록 루프 `trade-memory-loop` · 월간 리뷰 등 — README 45–49행). 일일 워크플로의 끝은 주문이 아니라 *"an Exposure Coach posture for human review, not an order"*(67행).
> API 키 없는 시작 경로가 있다 — 공개 CSV 만 쓰는 `market-breadth-analyzer` · `uptrend-analyzer` 등(86–91행). FMP · FINVIZ Elite · Alpaca 는 선택(수집기 판독).

> [!note] 범위를 스스로 자른다 — README 11 · 23 · 37행 (볼트 직접 판독)
> *"This is not a signal service or a promise of profitability."* · *"not financial advice … a signal service, or a broker execution platform"* · *"not designed for fully automated trading, signal outsourcing, or short-term scalping."*
> → [[자기제한-명시]]. 같은 날 재배달된 [[daily_stock_analysis]](저자 논문이 "수익을 입증하지 않는다"고 명시)와 같은 방향 — [[금융-AI]] 레포 두 곳이 모두 "판단은 사람"으로 선을 긋는다.

> [!warning] 성과 검증 수치 없음
> 예시 출력은 가상 데이터(수집기 판독). 스킬이 내는 점수 · 스크리닝 결과의 예측력은 측정되지 않았다.

## 도메인별 추출 (ai-news · 교차 금융-AI)
- **신뢰도**: ★4,352 · 13개월 차 · 측정 0.
- **즉시 활용**: 패턴만 YES — "기록 → 사후 분석 → 월간 규칙 조정" 루프(`trade-memory-loop`)는 볼트의 actionable 관리에도 옮길 수 있는 구조다. 투자 용도는 판단하지 않는다.
- **6개월 영향력**: [[에이전트-스킬]]이 코딩 밖 개인 업무 영역(투자 루틴)으로 넓어지는 사례.
- **대체 관계**: [[daily_stock_analysis]](자동 푸시형)와 달리 사용자가 호출하는 절차형.
- **허와 실**: 주장 자체가 절제돼 있다. 근거도 없다.
- **액션**: 없음.

## 관련 페이지
- [[에이전트-스킬]] · [[금융-AI]] · [[daily_stock_analysis]] · [[자기제한-명시]] · [[anthropics-skills]]

## 원본
- 출처: https://github.com/tradermonty/claude-trading-skills
- 확인 범위: GitHub API 메타 · contents API(skills 74) · README 11 · 23 · 37 · 45–49 · 67 · 86–91행 직접 판독 · 🔴 스킬 본문 미열람 · 실행 미확인
- 신뢰도: ⭐⭐ (★4,352 · 측정 0)
