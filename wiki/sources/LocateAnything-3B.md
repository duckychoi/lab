---
title: nvidia/LocateAnything-3B — NVIDIA 자연어 쿼리 기반 이미지 객체 위치 탐색 VLM
type: source
domain: ai-news
tags: [ai-news, nvidia, VLM, object-detection, localization, vision-language, 3B, grounding]
created: 2026-05-29
updated: 2026-06-08
sources: []
reliability: high
---

# LocateAnything-3B — NVIDIA 정밀 객체 위치 탐색 비전-언어 모델

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 자연어 쿼리("빨간 컵 위의 책")로 이미지 내 객체를 정밀하게 위치 탐색하는 NVIDIA 3B VLM. HF DL 122,000 (2026-06-08, prev 111,000→122,000). 로보틱스·GUI 에이전트·이미지 편집에서 "어디에 있는가" 문제를 직접 해결.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — HF DL 111,000 (2026-06-06, prev 78,925 3일 전), NVIDIA 공식 모델, 트렌딩 등재
- **즉시 활용**: YES — HuggingFace에서 직접 로드. transformers 라이브러리 호환
- **6개월 영향력**: [[ClawGUI]], [[VLAA-GUI]] 같은 GUI 에이전트가 화면 내 UI 요소 위치 파악에 바로 활용. 로봇 조작([[DexJoCo]])에서 "어느 객체를 잡을지" 결정에도 적용 가능
- **대체 관계**: SAM2(세그멘테이션), Grounding DINO(개방형 탐지) 대비 자연어 쿼리 기반 정밀 위치 특화
- **허와 실**: 3B는 실시간 로봇 제어에 충분한 속도? 지연시간 확인 필요

> [!action] 당장 할 것
> GUI 에이전트 파이프라인에서 UI 요소 위치 탐색 테스트. "파란 버튼 클릭" 같은 명령어로 정확도 검증

## 관련 페이지

- [[ClawGUI]] — GUI 자동화 에이전트
- [[VLAA-GUI]] — GUI 에이전트 프레임워크
- [[X2SAM]] — 이미지·비디오 통합 분할 MLLM
- [[WildDet3D]] — 실환경 3D 객체 탐지
- [[DexJoCo]] — 로봇 조작 벤치마크

## 원본

- 출처: https://huggingface.co/nvidia/LocateAnything-3B
- 다운로드: 111,000 (2026-06-06 기준, prev 78,925)
- 태스크: Visual Question Answering / Object Localization
- 신뢰도: ⭐⭐⭐⭐⭐
