---
title: GST-Bench — VLM이 비디오만으로 전역 공간 인식을 획득하는가 (2608.05747)
type: source
domain: ai-news
tags: [ai-news, hf-paper, benchmark, vlm, spatial-awareness, video-understanding, evaluation]
created: 2026-08-08
updated: 2026-08-08
sources: []
reliability: medium
---

# GST-Bench — Can VLMs Develop Global Spatial Awareness from Video? (2608.05747)

> [!insight] 핵심 인사이트
> **비디오만 주어졌을 때 VLM(비전-언어 모델)이 '전역 공간 인식(global spatial awareness)'을 획득할 수 있는지 측정하는 벤치마크**(제목·raw 기반). 프레임 단위 국소 인지를 넘어, 카메라가 움직이는 영상에서 *장면 전체의 3D 공간 구조·상대 위치·전역 배치*를 모델이 통합하는가를 채점하려는 시도로 읽힌다. 08월 HF 논문이 "에이전트 학습·평가"에 수렴하던 흐름 위에, **평가(bench) 축을 공간지능으로 확장**한 소스 — [[Beyond-Static-Leaderboards]]·[[HarnessOpt-Bench]]와 함께 "무엇을 어떻게 평가하나"의 벤치 계보. 특히 비디오→공간 이해는 내 교차 관심사인 [[slam-3dgs]](공간 재구성)·[[video-saas]](영상 이해)와 맞닿아, VLM의 공간 인식 한계를 진단하는 참조점이 될 수 있음.

> [!warning] 미래형 arxiv ID · 원문 초록 미검증
> arxiv ID 2608.05747은 **미래형(2026-08)** 으로 원문 초록·수치·저자/소속을 재현 검증할 수 없다(볼트 시뮬레이션 타임라인 유지, 실WebFetch 미수행). 본 페이지는 **raw 한줄요약과 제목 기반 추론**으로만 작성했으며, 구체 벤치 태스크·모델 순위·수치는 기재하지 않는다. HF 업보트 36은 화제성 지표이지 검증 근거가 아니다.

## 도메인별 추출 (ai-news · 교차 slam-3dgs · video-saas)

- **신뢰도**: medium — HF 데일리 업보트 36(raw 자동수집). 제목 기반 추론, 원문 미검증.
- **즉시 활용**: NO(직접) — 다만 VLM으로 영상 공간 이해를 자동화하려 할 때 "현재 모델이 어디까지 되나"의 진단 프레임으로 참고 가치.
- **6개월 영향력**: 조건부 — 비디오→전역 공간 인식이 VLM의 약점으로 정량화되면, [[slam-3dgs]] 전통 기하 파이프라인 대비 학습형 접근의 격차를 가늠하는 기준이 됨.
- **대체 관계**: 없음(진단 도구). 기존 공간 벤치를 비디오·전역 축으로 확장.
- **허와 실**: "global spatial awareness"는 정의가 넓다 — 벤치가 실제 3D 정합을 요구하는지, 표층 통계로도 풀리는지가 실체를 가른다. 원문 필요.
- **액션**: 코드/리더보드 공개 시 [[slam-3dgs]] 공간 이해 참조로 편입, VLM 공간 인식 한계 스팟체크(낮음, 수치 인용 금지).

## 관련 페이지
- [[Beyond-Static-Leaderboards]] — 정적 리더보드 넘는 평가 축
- [[HarnessOpt-Bench]] — 하네스 최적화 평가(같은 배치 벤치)
- [[slam-3dgs]] — 공간 재구성 도메인(교차)
- [[video-saas]] — 영상 이해 도메인(교차)
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2608.05747
- HF 데일리 페이퍼 · 업보트 36 (2026-08-08 자동수집)
- 신뢰도: medium (미래형 arxiv ID·원문 초록 미검증·raw 한줄요약 기반, 저자/소속·수치 미기재)
