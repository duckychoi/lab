---
title: "PartAgent — 학습 없이 3D 전문가 + 2D 전문가 + VLM 검증 루프로 3D 부품 분할 (arXiv 2611.32554)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, 3d-segmentation, agent, training-free, verification-loop, vlm, part-mesh]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.32554]
reliability: medium
---

**논문**: arXiv 2611.32554 · 업보트 **29**(수집기 11-25 — Self-Evolving Evaluation Environments와 동률, 목록 API 순서로 선택) → **29**(볼트 API 11-25 일치) · 소속 The Hong Kong University of Science and Technology · 저자 7명 · 코드 https://github.com/yangcaoai/PartAgent_Agent_for_3D_Part_Seg (★24 · **라이선스 없음**)

## 핵심 인사이트
> [!insight] 동결된 전문가 두 개 + 검증 VLM 루프 — 학습 0으로 학습형 SOTA를 넘는다
> 3D 전문가(**동결 P3-SAM**)의 영역 제안과 2D 전문가(**GPT-Image-2.5**)의 다시점 의미 단서를 합쳐 다중 입도 분할을 만들고, VLM(**gpt-6.1-sol**)이 관찰 → 검사 · 증거 보수 · 합성 · 재선택 행동을 반복하며 검증. 표 1 PartObjaverse-Tiny-WT Mask mIoU **68.41**(차순위 PartField 59.88, +8.53), 8개 범주 전부 1위. 표 2 4개 데이터셋 평균 69.36(PartField 62.08, +7.28). **학습 0 + 동결 전문가 + VLM 검증 루프** — [[TAISR]] 가 SR에서 한 것의 3D 버전이자 [[동결-교정층]] 의 표본(전 파이프라인이 교정층).

> [!warning] 유료 폐쇄 API 2종 의존 + 레포 라이선스 없음
> 비교 대상은 학습형 분할기인데 PartAgent는 **유료 폐쇄 API(GPT-Image-2.5 · gpt-6.1-sol)에 의존** — 객체당 비용 · 시간은 본문에 없다(볼트 미확인 항목 유지). 근소 행: Part-T 65.76 vs PartSAM 65.58(+0.18). 의존성 분석: 2D 전문가를 GPT-Image-2로 바꾸면 −2.24/−2.70점, SAM3로 바꾸면 −0.36/−1.50점, 검증 VLM 교체 시 GPT-5.6 · GPT-6과의 차이는 0.04–0.15점 수준 — **검증 VLM은 아무거나 써도 되고 2D 전문가가 병목**.

## 도메인별 추출 (slam-3dgs)
- **응용 가능성**: 3D 에셋 리깅 · 편집 전처리로 품질 최고 수준 — [[3AGameFactory-Motion]] 의 리깅 단계와 연결 가능한 부품.
- **설계 교훈**: "검증 VLM 교체 영향 0.04–0.15점" — 검증층은 약한 모델로도 충분하고 병목은 제안/단서층에 있다. 교정층 설계 시 비용 배분 근거.
- **액션**: 없음(관찰 — API 비용 미공개 · 라이선스 없음).

## 관련 페이지
- [[TAISR]] · [[동결-교정층]] · [[3AGameFactory-Motion]] · [[sam3]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.32554
- 확인 범위: HF papers API(볼트 11-25 — 업보트 29 · HKUST · githubRepo 일치) · 본문 표 1 · 2 및 의존성 분석(수집기 11-25 판독) · 실행 0
- 신뢰도: ⭐⭐ (품질 수치는 강력 · 유료 API 의존 + 비용 미공개 + 라이선스 없음)
