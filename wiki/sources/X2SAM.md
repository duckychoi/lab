---
title: X2SAM — 이미지·비디오 통합 분할 MLLM
type: source
domain: ai-news
tags: [ai-news, segmentation, multimodal, video, image, open-vocabulary, interactive]
created: 2026-05-07
updated: 2026-05-07
sources: []
reliability: medium
---

# X2SAM: Any Segmentation in Images and Videos

> [!insight] 핵심 인사이트
> 텍스트·시각 프롬프트로 이미지와 비디오 모두에서 오픈보캐뷸러리·추론·인터랙티브 분할을 지원하는 통합 MLLM. SAM(Segment Anything Model) 계보의 멀티모달 확장 — 단일 모델로 모든 분할 유스케이스 커버.

**HuggingFace**: https://huggingface.co/papers/2605.00891  
**업보트**: 14 (2026-05-06 기준)  
**신뢰도**: ⭐⭐⭐

## 도메인별 추출

- **신뢰도**: 업보트 14 — 초기. SAM 계보이므로 기반 기술 신뢰도는 높음
- **즉시 활용**: 영상 편집 파이프라인에서 객체 마스킹·인터랙티브 분할 자동화에 활용 가능. [[Pixelle-Video]] 전처리 레이어로 통합 가능성
- **6개월 영향력**: 텍스트 지시→영상 객체 분할 자동화가 video-saas 도구에 내장될 전망
- **대체 관계**: SAM2(이미지/비디오 분할) 대비 멀티모달(텍스트 프롬프트) 지원 강화
- **slam-3dgs 연결**: 3DGS 재구성 시 객체 분리 마스크 생성에 활용 가능

## 관련 페이지
- [[AI-영상-생성-2026]]
- [[Pixelle-Video]]
- [[VOID-model]]

## 원본
- 출처: https://huggingface.co/papers/2605.00891
- 신뢰도: ⭐⭐⭐ (업보트 14)
