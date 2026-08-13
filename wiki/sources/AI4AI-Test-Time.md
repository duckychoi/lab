---
title: AI4AI at Test-Time — 하네스로 강→약 능력 전이 (2608.12307)
type: source
domain: ai-news
tags: [ai-news, hf-paper, test-time, capability-transfer, harness, agent]
created: 2026-08-13
updated: 2026-08-13
sources: []
reliability: medium
---

# AI4AI at Test-Time: Strong-to-Weak Capability Transfer via Harnesses

**HF 논문**: https://huggingface.co/papers/2608.12307
**지표**: HF 데일리 **2위** · 업보트 71 (2026-08-13 자동수집)

> [!insight] 핵심 인사이트
> **학습(파인튜닝) 없이, 테스트타임에 "하네스(harness)"를 통해 강한 모델의 능력을 약한 모델로 전이(strong-to-weak capability transfer)한다는 접근**(제목·raw 기반). 이는 08월 위키에서 반복된 "무거운 일은 상위, 빈번·정형은 로컬"([[needle]]·[[에이전트-메모리-레이어]]) 분업 사고를, *가중치가 아니라 실행 하네스(스캐폴딩·프롬프트·도구 배선)로* 능력을 이식하는 쪽으로 밀어붙인 것으로 읽힌다 — [[Agent-Memory-Distillation]](대형 교사 메모리→소형 학생, 학습 없이 전이)와 같은 "학습 없는 전이" 계보. 실용적으로는 값비싼 프론티어 모델을 상시 쓰지 않고, 저렴한 약모델 + 잘 짠 하네스로 근접 성능을 뽑으려는 비용 최적화 각도. [[HarnessOpt-Bench]] 등 "하네스가 성능을 좌우한다"는 위키 내 관측과 직결.

> [!warning] 신뢰도 medium — 미래형 arxiv ID, 원문 미재현
> 논문 ID 2608.12307은 **미래형(2026-08) arxiv ID로 원문 초록·수치·방법 재현 불가**. 제목·raw 한줄요약·HF 데일리 순위/업보트만 근거이며, **구체 벤치 수치(전이 후 약모델 성능 향상폭)·저자·소속·하네스 설계 세부는 미기재**([[CLAUDE.md]] 사실확인 원칙).

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐⭐ (medium) — HF 데일리 2위·업보트 71. 원문 미재현.
- **즉시 활용**: 개념 참조 — 저비용 약모델 + 하네스로 프론티어 근접치를 노리는 비용 절감 패턴. 내 봇의 상위 모델 호출 축소 설계에 직접 시사.
- **6개월 영향력**: 중~높음 — "가중치 대신 하네스로 능력 이식"이 검증되면 로컬/저가 모델 활용 저변 확대.
- **대체 관계**: 상시 프론티어 API 호출을 약모델+하네스로 부분 대체.
- **허와 실**: "test-time transfer" 프레이밍 강함 — 어떤 태스크에서 얼마나 좁혀지는지 원문 수치 필수.
- **액션**: 원문 공개 시 하네스 구성 요소 파악, [[HarnessOpt-Bench]]와 대조.

## 관련 페이지
- [[Agent-Memory-Distillation]] — 학습 없는 강→약 전이 계보
- [[needle]] — 상위/로컬 분업의 밑단
- [[HarnessOpt-Bench]] — 하네스가 성능을 좌우한다는 관측
- [[ai-news]] — 도메인 누적 인사이트

## 원본
- 출처: https://huggingface.co/papers/2608.12307
- 신뢰도: ⭐⭐ (HF 데일리 2위·업보트 71, 미래형 ID·원문 미재현)
