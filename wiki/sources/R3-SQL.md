---
title: R³-SQL — Text-to-SQL 랭킹 보상·리샘플링 RLVR 프레임워크
type: source
domain: ai-news
tags: [ai-news, hf-paper, text-to-sql, rlvr, ranking-reward, resampling, bird-benchmark, sota]
created: 2026-05-11
updated: 2026-05-11
sources: []
reliability: high
---

# R³-SQL: Text-to-SQL 랭킹 보상 및 리샘플링

> [!insight] 핵심 인사이트
> SQL 생성 후보군의 **랭킹 일관성 문제**(같은 점수인데 다른 SQL)와 **정답 부재 문제**(정답 데이터 없는 쿼리)를 동시에 해결. BIRD-dev에서 **75.03% 실행 정확도** — 공개 모델(오픈웨이트) 중 SOTA. Text-to-SQL이 실용적 엔터프라이즈 도구로 진입했음을 확인하는 벤치마크.

## 도메인별 추출 (ai-news)

- **신뢰도**: arXiv 2604.25325 — 동료 심사 전이나 벤치마크 수치 구체적
- **즉시 활용**: 중간 — RLVR Text-to-SQL 파이프라인 구축에 참조 가능. 금융 데이터 쿼리 자동화 관심 있으면 직접 적용 검토
- **6개월 영향력**: "AI가 자연어로 DB 쿼리"가 SaaS 기능으로 실용화 가속. [[금융-AI]]와 결합 시 재무 분석 자동화에 직접 응용
- **대체 관계**: 기존 Text-to-SQL(fine-tuning 위주)에서 RLVR 방식으로 패러다임 전환

## 핵심 내용

### 해결한 두 가지 문제
1. **랭킹 일관성 문제**: 동일 실행 결과를 내는 여러 SQL 후보 사이의 점수 동점 처리
2. **정답 부재 문제**: 훈련 데이터에 정답 SQL이 없는 쿼리에 대한 보상 계산

### 방법론
- Ranking-based Reward: 후보 SQL 실행 결과를 서로 비교하는 상대적 랭킹 보상
- Resampling: 정답 없는 쿼리에 대해 고품질 후보를 재샘플링하여 학습 신호 생성

### 성능
- BIRD-dev: **75.03% 실행 정확도** (공개 모델 SOTA)

> [!note] 배경 정보
> BIRD Benchmark: 복잡한 실세계 DB 기반 Text-to-SQL 평가 표준. 기업 데이터 분석 시나리오 포함.

## 관련 페이지
- [[금융-AI]]
- [[TradingAgents]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://arxiv.org/abs/2604.25325
- 신뢰도: ⭐⭐ (arXiv 논문, 동료 심사 전)
