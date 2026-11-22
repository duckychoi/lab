---
title: "Depth Pro 2 — 이미지 · 비디오 겸용 미터 단위 단안 깊이 (Apple · 선명도 + 시간 일관성 동시 주장 · 초록 수치 0 · 코드 라이선스에 비상업 문구 없음)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, monocular-depth, metric-depth, video-depth, apple]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.26603]
reliability: medium
---

**논문**: arXiv 2611.26603 · 업보트 31(볼트 · 수집기 일치) · [[Apple]] · 저자 8 · 코드 [apple-aiml-research/ml-depth-pro-2](https://github.com/apple-aiml-research/ml-depth-pro-2) ★382(볼트 GitHub API · HF 필드 354) · 레포 생성 2026-11-03

## 핵심 인사이트
> [!insight] "선명하지만 깜빡인다 / 안정적이지만 뭉갠다"의 양자택일을 하나의 네트워크로
> 단안 깊이에서 다중 프레임 방법은 시간 일관성, 단일 프레임 방법은 경계 선명도를 택해 왔다. Depth Pro 2 는 이미지와 비디오를 모두 처리하고 **원본 해상도에서 미터 단위 절대 깊이**를 낸다. 정확도-선명도-일관성-속도의 새 파레토 프런티어를 이루는 모델 패밀리를 코드 · 가중치와 함께 공개.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: "세 차원 모두에서 선행 연구를 넘는다"는 서술뿐 — **초록에 수치 · 모델 크기 없음**(볼트 확인).
- **실시간 가능성**: 미확인(패밀리 중 빠른 모델의 fps 는 본문 · 레포 몫).
- **카메라 파이프라인**: 단안 RGB(이미지/영상) → 미터 깊이. 카메라 내부 파라미터 요구 여부 미확인.
- **응용 가능성**: 영상 VFX(깊이 기반 합성 · 포커스) · 3DGS 초기화 · 로보틱스 깊이 전처리. 영상 깊이가 프레임 간 흔들리지 않으면 [[3DGS]] 재구성의 깊이 prior 로 쓰기 좋다.
- **필수 레퍼런스**: 본 논문 + 레포.

> [!note] 🆕 라이선스 — 수집기의 "비상업 가능성" 질문에 대한 볼트 확인
> 레포 LICENSE(2,660B, GitHub 표기 NOASSERTION)는 Apple 표준 샘플코드 문언이다: *"to use, reproduce, modify and redistribute the Apple Software, with or without modifications, in source and/or binary forms"*. **`commercial` · `research` 문자열 0건 — 비상업 한정 문구가 없다.** 단 이는 **소프트웨어 LICENSE** 이고 가중치에 별도 조건이 붙는지는 확인하지 못했다(가중치 배포 위치 미열람). 문언 대조이지 법률 해석이 아니다.

## 관련 페이지
- [[Apple]] · [[Marigold-V2]] · [[3DGS]] · [[VODA]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.26603
- 확인 범위: HF papers API(초록 전문) · GitHub API · LICENSE 원문 · 🔴 본문 표 · 가중치 라이선스 미확인 · 실행 0
- 신뢰도: ⭐⭐⭐
