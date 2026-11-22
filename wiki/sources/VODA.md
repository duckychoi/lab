---
title: "VODA — The Mask Is Not the Object: 3DGS 분할에 체적 감독을 넣는 plug-and-play 목적함수 (Yonsei · Removal-3D · RDE 신설)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, 3dgs, segmentation, object-removal, benchmark]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.21383]
reliability: medium
---

**논문**: arXiv 2611.21383 · 업보트 33(볼트 · 수집기 일치) · Yonsei University · 저자 4 · 코드 [jhxcho/voda](https://github.com/jhxcho/voda) ★24

## 핵심 인사이트
> [!insight] 렌더된 마스크가 맞아도 객체는 다 선택되지 않았을 수 있다
> [[3DGS]] 분할이 렌더링 뷰로만 학습 · 평가되어, 렌더 마스크는 정확해도 가려지거나 기여도가 낮은 가우시안이 선택에서 빠진다. VODA 는 국소 깊이 구조로 픽셀별 기여 가우시안을 묶어 **선택된 깊이 클러스터의 모든 가우시안을 직접 감독**하는 plug-and-play 목적함수. 체적 완전성 평가용 합성 객체 제거 벤치 Removal-3D 와 지표 RDE(Removal Depth Error) 신설. 측정 도구(2D 마스크 IoU)가 놓치는 실패를 새 지표로 드러낸 사례 → [[측정도구-먼저-반증]].

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 렌더링 기반 베이스라인 4종에 붙여 Removal-3D 에서 일관 개선. LERF · ScanNet 은 "유지 또는 개선" = 일부는 개선 없음. 초록 수치 0.
- **실시간 가능성**: 학습 목적함수라 추론 속도 영향 없음(추정 아님 — 초록이 plug-and-play objective 로 서술).
- **카메라 파이프라인**: 기존 3DGS 분할 파이프라인 그대로.
- **응용 가능성**: 3DGS 장면에서 객체를 지우거나 떼어 낼 때 남는 잔여 가우시안 문제에 직접 해당 — 장면 편집 · 에셋 추출.
- **필수 레퍼런스**: 본 논문 + 코드.

> [!warning] 단서
> Removal-3D 는 합성 벤치이고 저자가 만든 것이다. 단순 그래디언트 재가중 · 공간 전파로는 같은 효과가 안 난다는 분석은 초록 서술.

## 관련 페이지
- [[3DGS]] · [[측정도구-먼저-반증]] · [[Depth-Pro-2]] (같은 배치 · 깊이) · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.21383
- 확인 범위: HF papers API(초록 전문 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐
