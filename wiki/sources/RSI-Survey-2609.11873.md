---
title: "RSI 서베이 — The Last AI Built by Humans (arXiv 2609.11873)"
created: 2026-11-24
author: fryday
tags: [source, recursive-self-improvement, survey, evaluation, agents, ledger-65]
---

# The Last AI Built by Humans: Toward Genuine Recursive Self-Improvement

- 원문: [arXiv 2609.11873](https://arxiv.org/abs/2609.11873) v3(2026-09-22), 저자 35명. 계기: Threads @conanssam
- 코드 수준 분석·골격: note 레포 `rsi-survey-2609.11873` 브랜치 (`docs/ANALYSIS.md`, `src/rsi_core.py`, 테스트 11/11) · 원장 #65

## 요지
분석 단위를 '개선 루프'(시스템·상태·경험·대상·개선기·전략·검증기·개선·후계자)로 두고, AI가 넘겨받은 책임으로 단계화: **B0** 과제 내 출력 개선(비-RSI) → **L1** 사람이 정한 절차 실행·결과 보존 → **L2** 개입 전략 선택 → **L3** 다음 학습 경험 선택 → **L4** 배포 상호작용으로 지속 적응 → **L5** 이후 개선을 지배하는 메커니즘(개선기·평가기·연구정책) 자체를 고치고 상속. L5는 구조적(상속·호출) vs 효과적(같은 예산·독립 평가에서 더 나은 후계자)로 구분. 높은 단계 ≠ 더 좋은 개선.

## 수식이 있는 유일한 부분: HCI
H = 100·(s̄ − F₀)/(100 − F₀) (F₀=진입년 90백분위), 출처 가중 합의(3/2.5/2/1, 1자 ×0.75), 영역 궤적 √n 가중. 2026: 수학 86.4·과학 85.8 vs SWE 52.6·도구 에이전트 39.9 → 긴 상호작용 워크플로에 RSI 가치 집중(R_d=100−0.22(100−T)는 예시 가정).

## 평가 원칙 (우리 검증 12규칙과 거의 일치)
예산 일치(생성·평가·메커니즘 개발·검토 비용 포함), 보호 평가(적응 질의된 벤치는 최적화 대상이 됨), L3는 학습자 입력 동결/무관 스케줄 대조, L5는 메커니즘 감사 + 같은 예산 비교 + 전이 시 메커니즘 고정.

## 주의
서베이: 새 방법·통제 실험 없음. 산업 사례(Theseus·Lark·Xiaohongshu·Humanlaya·ModelBest·Hyra·ARA·Frontis)는 전부 회사 자체 보고. 효과적 L5의 통계적 증거는 사실상 없음.
