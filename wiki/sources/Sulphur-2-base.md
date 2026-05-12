---
title: Sulphur-2-base — 텍스트→비디오 확산 모델 (Diffusers 기반)
type: source
domain: ai-news
tags: [ai-news, video-saas, text-to-video, diffusion, gguf, local-llm, sulphurai]
created: 2026-05-07
updated: 2026-05-08
sources: []
reliability: medium
---

# SulphurAI/Sulphur-2-base

> [!insight] 핵심 인사이트
> Diffusers 기반 텍스트→비디오 확산 모델. **GGUF 양자화 지원**으로 로컬 비디오 생성 가능. ⬇️55,500 다운로드 — 텍스트→비디오를 로컬에서 실행하려는 수요가 존재함을 확인. video-saas × local-llm 교차 도메인 항목.

**HuggingFace**: https://huggingface.co/SulphurAI/Sulphur-2-base  
**다운로드**: 144,000 (2026-05-10 기준, 이전 93,000)  
**신뢰도**: ⭐⭐⭐

## 도메인별 추출 (video-saas 관점)

- **신뢰도**: 55K 다운로드 — 중간. SulphurAI 신생 조직, 검증 필요
- **즉시 활용**: GGUF 지원 = llama.cpp 계열 툴로 로컬 실행 가능. Diffusers 통합 = HF 파이프라인 표준 방식으로 실험 용이
- **6개월 영향력**: 텍스트→비디오 생성이 LLM처럼 로컬 실행 가능해지면 SaaS 구독 없이 콘텐츠 파이프라인 자체 구성 가능
- **대체 관계**: [[Pixelle-Video]](파이프라인 오케스트레이션) 대비 기반 모델 제공. [[Seedance]](SaaS), [[Higgsfield]](SaaS) 대비 로컬 오픈소스 대안
- **local-llm 연결**: GGUF 양자화 = [[Qwen3.6-35B-A3B-GGUF]] 패턴과 동일. 소비자 GPU에서 실행 가능성 확인 필요
- **기능 벤치마킹**: 실제 생성 품질이 상용 T2V 모델 대비 어느 수준인지 테스트 필요

> [!question] 미해결 질문
> RTX 4090 단일 GPU에서 어느 해상도/길이까지 실시간에 가깝게 생성 가능한가?

## 관련 페이지
- [[Pixelle-Video]]
- [[AI-영상-생성-2026]]
- [[Seedance]]
- [[Qwen3.6-35B-A3B-GGUF]]

## 원본
- 출처: https://huggingface.co/SulphurAI/Sulphur-2-base
- 신뢰도: ⭐⭐⭐ (55K DL, 신생 조직)
