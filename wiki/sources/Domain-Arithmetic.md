---
title: Domain Arithmetic — 산술 연산으로 VLA 모델을 신규 환경에 원샷 적응
type: source
domain: ai-news
tags: [ai-news, hf-paper, vla, robotics, domain-adaptation, one-shot, model-arithmetic]
created: 2026-07-02
updated: 2026-07-02
sources: []
reliability: low
---

# Domain Arithmetic (HF papers 2607.00666)

> [!insight] 핵심 인사이트
> **산술 연산 기반으로 VLA(비전-언어-행동) 모델을 환경 변화에 원샷 적응**시키는 방법. 태스크 벡터(task arithmetic) 계열의 아이디어를 VLA에 적용해, 재학습 없이 **모델 파라미터/표현의 덧셈·뺄셈으로 신규 환경에 최소 데이터로 대응**하려는 접근으로 읽힌다. [[In-Context-World-Modeling]](시스템 식별을 인컨텍스트 적응으로)·[[Translation-as-Bridging-Action]](신체 갭 흡수)가 던진 **"VLA를 새 환경에 값싸게 일반화"** 흐름의 또 다른 갈래 — 인컨텍스트 적응이 *추론 시*라면 Domain Arithmetic은 *파라미터 산술*로 접근. slam-3dgs/로보틱스 축과 직접 교차.

## 도메인별 추출 (ai-news / slam-3dgs 교차)

- **신뢰도**: ⭐ — HF 자동수집. 저자·성공률·적응 대상 환경/로봇·baseline 미확인.
- **즉시 활용**: NO — 로봇 VLA 연구로 당장 붙일 오픈 구현·하드웨어 없음. 개념적 방향성 참고.
- **6개월 영향력**: 중간 — "재학습 없이 산술로 환경 적응"이 검증되면 VLA 배포 비용이 크게 낮아짐. [[Orca]] 같은 월드 파운데이션 모델 위에 올리는 경량 적응 레이어로 결합 가능성.
- **대체 관계**: 환경별 파인튜닝을 파라미터 산술 원샷 적응으로 대체 시도.
- **허와 실**: 태스크 벡터 산술은 태스크 간 간섭·비선형성에서 자주 깨진다. "원샷 적응"의 실제 성공률과 실패 모드가 핵심인데 미확인.
- **액션**: 원문 fetch로 적응 성공률·실패 모드·오픈 코드 확인 → [[In-Context-World-Modeling]]와 비교해 "추론시 vs 파라미터 산술" 적응 계보 [[synthesis]] 후보로 검토.

> [!question] 미해결 질문
> 어떤 VLA 백본·로봇 태스크? 원샷 적응 성공률과 실패 모드? task arithmetic의 간섭 문제 처리 방식?

## 관련 페이지
- [[In-Context-World-Modeling]]
- [[Translation-as-Bridging-Action]]
- [[Orca]]
- [[slam-3dgs]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.00666
- 신뢰도: ⭐ (HF 자동수집 — 원문·수치 미검증)
