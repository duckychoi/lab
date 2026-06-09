---
title: DRIFT — 딥리서치 에이전트 궤적 오류 구간 탐지 (NJU-LINK Lab)
type: source
domain: ai-news
tags: [ai-news, hf-paper, deep-research-agent, error-detection, fact-checking, hallucination, span-level]
created: 2026-06-04
updated: 2026-06-04
sources: []
reliability: high
---

# DRIFT — 장문 에이전트 궤적 근거 없는 주장·충돌 클레임 자동 탐지

**논문**: https://huggingface.co/papers/2606.02060  
**저자**: NJU-LINK Lab (난징대)

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 딥리서치 에이전트의 장문 궤적(trajectory)에서 **근거 없는 주장(unsupported claims)·충돌 클레임(conflicting claims)**을 자동으로 span-level로 탐지. 탐지 정확도 최대 **+30%p 향상**. "에이전트가 뭘 잘못 알고 있는가"를 자동으로 짚어내는 검증 레이어.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐ — NJU-LINK Lab, arXiv, HF Papers 수록
- **즉시 활용**: YES (개념으로) — 딥리서치 에이전트 출력의 사후 검증 파이프라인으로 즉시 적용 가능. 구현체 공개 여부 확인 필요
- **6개월 영향력**: AI 에이전트 신뢰성 인프라의 핵심. [[AutoMedBench]]에서 Validate 단계 강화에 직접 활용 가능. 규제 환경에서 AI 출력 감사(audit) 도구로 중요
- **대체 관계**: 단순 사실확인(fact-checking) vs DRIFT의 궤적 내 내부 모순 탐지
- **허와 실**: span-level 탐지가 실제 오류와 일치하는가? 탐지된 "충돌"이 실제로 틀린 것인가 아닌 것인가?

## 기술 요약

- **입력**: 에이전트 추론 궤적 (장문 텍스트)
- **탐지 대상**:
  1. **Unsupported Claims**: 출처·증거 없이 단정된 주장
  2. **Conflicting Claims**: 동일 궤적 내 서로 모순되는 주장
- **출력**: 오류 구간(span) 위치 + 유형 레이블
- **성능**: span-level 탐지 정확도 최대 +30%p

> [!action] 당장 할 것
> auto-research 스킬 출력에 DRIFT 스타일 검증 레이어 추가. 장문 리서치 결과의 내부 모순 자동 플래그 시스템 검토.

## 관련 페이지

- [[AutoMedBench]] — 에이전트 파이프라인 Validate 단계 취약성 (직접 연결)
- [[AutoResearchClaw]] — 자율 연구 에이전트
- [[DR3-Eval]] — AI 딥리서치 에이전트 평가 프레임워크

## 원본

- 출처: https://huggingface.co/papers/2606.02060
- arXiv: 2606.02060
- 저자: NJU-LINK Lab
- 신뢰도: ⭐⭐⭐⭐
