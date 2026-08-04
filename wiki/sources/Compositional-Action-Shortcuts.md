---
title: RCORE — 제로샷 조합 행동 인식의 객체 지름길 완화
type: source
domain: ai-news
tags: [ai-news, huggingface, paper, video-understanding, action-recognition, naver, shortcut-bias]
created: 2026-07-10
updated: 2026-07-10
sources: []
reliability: medium
---

# HF논문: Why Can't I Open My Drawer? — Mitigating Object-Driven Shortcuts (arXiv 2601.16211)

**HuggingFace**: https://huggingface.co/papers/2601.16211
**기관**: 경희대(Kyung Hee U, Jinwoo Choi 외) + [[NAVER]] Cloud(Inwoong Lee·Taeoh Kim·Minho Shim·Dongyoon Wee) · **기법명**: RCORE

> [!insight] 핵심 인사이트
> **제로샷 조합 행동 인식(ZS-CAR) 모델이 시간적 증거 대신 "객체 지름길(object-driven shortcut)"에 의존하는 문제를 진단·완화.** WebFetch로 초록 실측: 모델이 동작을 시간 패턴이 아니라 **인식된 객체로 동사를 추측**해, 특히 시간 순서가 반대인 동작(서랍 열기 vs 닫기)을 혼동. 해법 RCORE는 두 축: ①**CPR(Co-occurrence Prior Regularization)** — 새 동사-객체 조합을 합성하고 자주 본 쌍을 hard negative로, ②**TORC(Temporal Order Regularization)** — 시간 역전·셔플에 대한 불변성을 페널티로 시간 민감성 강제. 결과: 미관측 조합 정확도 Sth-com +3.8~4.5, 신규 EK100-com +6.9~7.0, 베이스라인이 음수인 compositional gap을 양수로 전환. 이것은 내 [[down-analysis]] 영상 이해와 직결 — "**객체만 보고 동작을 단정하지 말고 시간 순서를 봐라**"는 원칙이 영상 장면 분석 프롬프트 설계에 그대로 이식됨.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐⭐ (arXiv 2601.16211 초록 WebFetch 검증 — CPR/TORC·정량 개선폭·EK100-com 신설 확인. 재현 미실측 → medium)
- **즉시 활용**: 간접 — 학습 기법이라 코드 직접 투입은 아니나, [[down-analysis]] 장면 설명 시 "객체=동작 단정" 편향 경계 프롬프트로 활용.
- **6개월 영향력**: 비디오 이해 평가·학습이 "객체 상관"이 아닌 "시간적 인과"를 요구하는 방향으로. 같은 [[NAVER]]의 [[Video-Oasis]]와 함께 "지름길 없는 영상 이해" 흐름 형성.
- **대체 관계**: 기존 ZS-CAR 베이스라인의 shortcut 문제를 정규화로 교정 — 백본 교체 아닌 학습 규제 추가.
- **허와 실**: "compositional gap 음수→양수"는 초록 명시. 단 벤치 2종(Sth-com·EK100-com) 한정, 일반 영상 이해로의 전이는 미검증.
- **액션**: down-analysis 장면 분석 시 "동사는 프레임 시간 순서에서 추론" 규칙 명시화(서랍 열기/닫기류 역전 케이스 방지).

## 관련 페이지
- [[Video-Oasis]] — 같은 [[NAVER]] 팀, "지름길 없는 영상 이해" 평가 (강한 공명)
- [[Video-MME-Logical]] — 영상 시간적·논리적 추론 벤치
- [[down-analysis]] — 영상 장면 분석 스킬(원칙 이식 대상)
- [[NAVER]] — 제작 기관
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2601.16211
- arXiv: 2601.16211, RCORE (경희대 + NAVER Cloud)
- 성과: Sth-com +3.8~4.5 / EK100-com +6.9~7.0 / compositional gap 음수→양수
- 신뢰도: ⭐⭐⭐ (초록 원문 검증 / 재현 미실측)
