---
title: Canvas360 — 기하 인지 사전학습 기반 인컨텍스트 360도 파노라마 생성
type: source
domain: ai-news
tags: [ai-news, video-saas, slam-3dgs, panorama, flow-matching, rgb-depth]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: medium
---

# Canvas360 (HF papers 2607.08765 — "In-context Panoramic Generation")

> [!insight] 핵심 인사이트
> 360도 파노라마 생성·편집의 2단계 프레임워크. **RGB-Depth 병렬 생성**(latent 연결 후 Flow Transformer가 각자 flow-matching)으로 등장방형(equirectangular) 위경도 왜곡을 극복. 세 장치 — **Velocity Circular Padding**(0°/360° 경계 연속성)·**Similarity Loss 정규화**(RGB·depth 과유사 방지)·**3D RoPE 위치 오프셋**. 파인튜닝 단계에선 depth 감독 없이 **스타일 전이·인페인팅·아웃페인팅·편집을 토큰 연결로 통합**. 100만 쌍 데이터셋(Canvas360Dataset), FAED 지표 선두.

**HF Papers**: https://huggingface.co/papers/2607.08765 (upvote 5)  
**신뢰도**: ⭐⭐⭐ (초록 원문 검증 / 재현·수치 미실측)

## 도메인별 추출

- **신뢰도**: 초록 원문 WebFetch 검증. FAED·유저스터디 수치는 미재현 → medium
- **즉시 활용**: 낮음(360 파노라마 특수 도메인). 다만 **RGB+Depth 동시 생성**은 [[AI-3D-생성]]·3DGS 씬 생성과 연결 — 파노라마+깊이는 3D 재구성 입력으로 바로 쓰임
- **6개월 영향력**: "생성 이미지에 기하(깊이)를 함께 뽑는다"는 흐름 — 2D 생성과 [[slam-3dgs]]/3D 재구성의 경계를 흐림. HunyuanWorld·DiT360 대비 경계 연속성·기하 일관성 우위 주장
- **응용 가능성**: 파노라마+depth → 3DGS 초기화 → 영상용 배경/환경 에셋. [[reat-render]] 배경 생성 파이프에 "360 환경맵" 옵션
- **필수 레퍼런스**: Flow matching·equirectangular projection 왜곡 처리, in-context 멀티태스크(4종) 통합 방식
- **액션**: RGB+Depth 병렬 생성 아이디어를 3D 에셋 파이프 후보로 메모

> [!note] 배경 정보
> Canvas360Dataset = 사전학습용 RGB-depth 파노라마 10만 + 인컨텍스트 4태스크 합성 90만. "지금까지 가장 포괄적" 주장(원문 미검증).

## 관련 페이지
- [[AI-3D-생성]]
- [[AI-영상-생성-2026]]
- [[slam-3dgs]]
- [[World-Infinity]]

## 원본
- 출처: https://huggingface.co/papers/2607.08765
- 신뢰도: ⭐⭐⭐ (초록 검증)
