---
title: InvokeAI — Stable Diffusion 크리에이티브 엔진 + 노드 파이프라인 (⭐27,287)
type: source
domain: ai-news
tags: [ai-news, github-trending, stable-diffusion, image-generation, video-generation, node-editor, WebUI, creative-tool]
created: 2026-05-30
updated: 2026-05-30
sources: []
reliability: high
---

# InvokeAI — Stable Diffusion 기반 크리에이티브 생성 엔진

## 핵심 인사이트

> [!insight] 핵심 인사이트
> Stable Diffusion 기반 이미지/영상 생성 WebUI 중 노드 에디터가 가장 성숙한 구현체. ⭐27,287. 복잡한 생성 파이프라인(컨트롤넷 + LoRA + 인페인팅 조합 등)을 시각적으로 구성 가능. [[AI-영상-생성-2026]] 맥락에서 로컬 SD 워크플로우의 사실상 표준.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — GitHub ⭐27,287, 수년간 활발한 유지보수, 커뮤니티 규모 큼
- **즉시 활용**: YES — GPU 있으면 로컬 설치 후 바로 이미지/영상 생성 가능
- **6개월 영향력**: SD3.5, FLUX 등 신규 모델 지속 통합. 노드 파이프라인으로 자동화 워크플로우 구성 시 creative AI 파이프라인의 핵심 도구
- **대체 관계**: ComfyUI(노드 에디터 강점) vs InvokeAI(UX+API 강점) 양대 진영. A1111(WebUI) 대비 더 현대적인 아키텍처
- **허와 실**: 로컬 GPU 메모리 8GB+ 권장. 최신 FLUX 모델은 16GB+. 클라우드 배포는 별도 설정 필요
- **액션**: GitHub README의 설치 가이드 따라 로컬 설치 후 노드 에디터 탐색

> [!note] 배경 정보
> InvokeAI는 단순 WebUI가 아니라 REST API를 기본 제공해 외부 서비스와 프로그래매틱 연동 가능. n8n ([[n8n]]) 같은 워크플로우 도구와 조합하면 완전 자동화된 이미지 생성 파이프라인 구성 가능.

## 주요 기능

- **노드 에디터**: 시각적 파이프라인 구성 (ComfyUI 스타일)
- **WebUI**: 직관적 인터페이스로 즉시 사용 가능
- **REST API**: 외부 앱 연동, 배치 처리, 자동화
- **컨트롤넷/LoRA**: 다양한 어댑터 지원
- **인페인팅/아웃페인팅**: 부분 편집 워크플로우
- **영상 생성**: 이미지-to-비디오, 텍스트-to-비디오 지원

## 관련 페이지

- [[AI-영상-생성-2026]] — 영상 생성 도구 전체 지형도
- [[CollectionLoRA]] — LoRA 증류 기술, InvokeAI에서 활용 가능
- [[n8n]] — 워크플로우 자동화와 InvokeAI API 연동

## 원본

- 출처: https://github.com/invoke-ai/InvokeAI
- 스타: ⭐27,287 (+12, 2026-05-30 기준)
- 신뢰도: ⭐⭐⭐⭐⭐
