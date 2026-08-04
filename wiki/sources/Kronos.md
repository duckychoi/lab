---
title: shiyu-coder/Kronos — 금융 시장 특화 파운데이션 모델
type: source
domain: ai-news
tags: [ai-news, github-trending, finance-ai, time-series, financial-llm, trading]
created: 2026-04-10
updated: 2026-07-28
sources: []
reliability: medium
---

# shiyu-coder/Kronos

> [!update] 2026-07-28 갱신 — ⭐34,707 (+441/일)
> ⭐**34,707**(2026-07-28, 당일 +441, WebFetch "34.7k" 일치) ← ⭐33,610(07-25). 완만한 지속 성장 유지. WebFetch 재확인: **45+ 글로벌 거래소** 학습·2단계(계층 이산토큰화 → decoder-only AR)·mini/small/base/large 변종·KronosPredictor·Qlib 파인튜닝·BTC/USDT 24h 데모. 금융 예측 특성상 백테스트↔라이브 괴리 검증 필수라 reliability **medium 유지**.

> [!update] 2026-07-25 갱신 — ⭐33,610 + 구조 재확인
> ⭐**33,610**(2026-07-25, GitHub API 실측 · WebFetch "33.6k" 일치) ← ⭐30,432(06-16). 완만한 지속 성장. WebFetch로 구조 재확인: **금융 캔들스틱(K-line) 최초 오픈 파운데이션 모델**을 표방, 45+ 글로벌 거래소 학습, **2단계**(OHLCV를 계층적 이산토큰으로 만드는 토크나이저 → decoder-only 오토리그레시브 트랜스포머), 파라미터 **4.1M~499.2M** 변종. 여전히 금융 예측 특성상 백테스트↔라이브 괴리 검증 필수라 reliability medium 유지.

> [!insight] 핵심 인사이트
> 금융 시장 데이터(시계열, 가격, 지표)를 언어 모델 방식으로 이해·예측하는 파운데이션 모델. 스타 **30,432개(2026-06-16)**. 7,045 → 30,432로 급등 (+332%) — 금융 AI 관심 폭증 신호. "금융 언어 모델링"이라는 니치 도메인에서의 특화 모델 트렌드 반영.

## 핵심 인사이트

> [!warning] 주의 / 신뢰도 낮음
> 금융 예측 모델은 과대평가 경향 강함. 백테스트 결과와 실제 라이브 성능 간 괴리 검증 필수. 과거 데이터에만 유효할 수 있음.

> [!note] 배경 정보
> 개인 연구자(shiyu-coder) 프로젝트. 대형 연구소 아님. 스타 수 대비 논문/검증 자료 확인 필요.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐ — 개인 연구자, 독립 검증 자료 부족
- **즉시 활용**: NO — 금융 AI는 실제 배포 전 충분한 검증 필요
- **6개월 영향력**: 금융 AI 특화 모델 증가 트렌드의 데이터 포인트
- **대체 관계**: Bloomberg GPT / FinGPT 계열과 경쟁
- **허와 실**: 마케팅 vs 실제 알파 생성 능력 별개. 관심 수준 유지
- **액션**: 논문/벤치마크 확인 후 star 결정

## 관련 페이지

- [[금융-AI]]

## 원본

- GitHub: https://github.com/shiyu-coder/Kronos — 스타 7,045 (2026-04-10)
- arXiv 논문: https://arxiv.org/abs/2508.02739 — 45개 글로벌 거래소 120억 K-line 학습, 가격예측 RankIC +93%, 변동성 예측 MAE -9%
- 신뢰도: ⭐⭐⭐ (논문 출판으로 상향, 벤치마크 수치 공개)
