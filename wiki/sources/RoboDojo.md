---
title: RoboDojo — Sim-and-Real 통합 로봇 조작 벤치마크
type: source
domain: ai-news
tags: [ai-news, huggingface, paper, benchmark, robot, sim-and-real, embodied]
created: 2026-07-09
updated: 2026-07-09
sources: []
reliability: medium
---

# HF논문: RoboDojo — Unified Sim-and-Real Benchmark (arXiv 2607.04434)

**HuggingFace**: https://huggingface.co/papers/2607.04434
**게재**: 2026-07

> [!insight] 핵심 인사이트
> **시뮬레이션과 실물 로봇을 통합해 범용(generalist) 로봇 조작 정책을 종합 평가하는 벤치마크.** WebFetch 초록 실측: 일반화·**메모리**·정밀도·**롱호라이즌 실행**·오픈보캐뷸러리 지시 이행 등 "다양·도전적·상보적" 조작 능력 전반을 평가. 파편화된 로봇 벤치를 하나로 묶어 sim↔real 격차까지 본다는 점이 핵심. [[LaMem-VLA]](메모리)·[[LingBot-Video]](사전학습)·[[World-Infinity]](환경 생성)가 "임바디드 모델을 만든다"면 RoboDojo는 **"그걸 어떻게 공정하게 평가하나"**의 축 — [[Beyond-Static-Leaderboards]] "리더보드 ≠ 실제 신뢰성" 원칙의 로봇판 인프라. 임바디드 클러스터가 학습·보정·배포·**평가**까지 4각을 갖춰가는 신호.

## 도메인별 추출 (ai-news / slam-3dgs 교차)

- **신뢰도**: ⭐⭐⭐ (arXiv 2607.04434 초록 WebFetch 검증 — sim-and-real 통합·5+ 능력축 평가 확인. 벤치 상세·리더보드 미실측 → medium)
- **즉시 활용**: NO — 로봇 조작 평가 인프라로 내 워크플로와 직접 접점 없음. "sim↔real + 능력축 분해 평가" 설계는 벤치 방법론으로 참고.
- **6개월 영향력**: 로봇 정책 평가가 단일 태스크에서 **다능력·sim-and-real 통합**으로. 임바디드 모델 비교의 공통 언어 형성.
- **대체 관계**: 파편화된 개별 로봇 벤치를 통합 벤치로 대체 시도.
- **허와 실**: "comprehensive·unified"는 벤치 논문의 상투어 — 실제 채택·재현성이 가치를 결정. 초록 수준만 검증됨.
- **액션**: 없음(도메인 외). "능력축(메모리/정밀/롱호라이즌/오픈보캐)로 분해 평가" 프레임을 내 스킬 평가에 아이디어로 기록.

## 관련 페이지
- [[LaMem-VLA]] · [[LingBot-Video]] · [[World-Infinity]] — 같은 흐름 임바디드 (학습·보정·환경)
- [[Beyond-Static-Leaderboards]] — 리더보드 신뢰성 원칙 (로봇판)
- [[임바디드-AI]] — 상위 개념
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.04434
- arXiv: 2607.04434, RoboDojo
- 평가축: 일반화 / 메모리 / 정밀도 / 롱호라이즌 / 오픈보캐뷸러리 · sim-and-real 통합
- 신뢰도: ⭐⭐⭐ (초록 원문 검증 / 벤치 상세 미실측)
