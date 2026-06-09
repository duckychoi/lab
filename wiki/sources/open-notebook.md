---
title: lfnovo/open-notebook — 오픈소스 NotebookLM 대체재
type: source
domain: ai-news
tags: [ai-news, github-trending, notebooklm, open-source, podcast, rag, local-llm, multi-provider]
created: 2026-06-06
updated: 2026-06-06
sources: []
reliability: high
---

# open-notebook — 구글 NotebookLM의 오픈소스 대체재

**GitHub**: https://github.com/lfnovo/open-notebook  
**스타**: ⭐26,200 (2026-06-06 기준)  
**라이선스**: 오픈소스

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 구글 NotebookLM의 오픈소스 대체재로, 18개 AI 제공사 선택(OpenAI·Anthropic·Google·Ollama 등), PDF·영상·오디오 복합 소스, **멀티스피커 팟캐스트 자동 생성**, 완전 로컬 배포 지원. ⭐26,200 — NotebookLM의 종속성·프라이버시 문제를 자체 인프라로 해결하려는 수요 반영.

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐26,200, 활발한 커뮤니티, 다양한 소스 타입 지원 검증됨
- **즉시 활용**: YES — Docker 또는 pip로 로컬 배포, Ollama와 결합해 완전 오프라인 지식 관리 가능
- **6개월 영향력**: [[LLM-Wiki]] 패턴과 결합 시 강력한 시너지 — 소스 인제스트·팟캐스트 생성·질문 응답을 단일 파이프라인으로. [[project-nomad]]식 오프라인 지식 시스템과 직접 연결
- **대체 관계**: Google NotebookLM 직접 대체. 차이점: 모델 선택 자유, 로컬 배포, 팟캐스트 커스터마이징
- **허와 실**: NotebookLM의 팟캐스트 품질을 그대로 재현할 수 있는지 TTS 품질이 관건

> [!action] 당장 할 것
> Ollama + open-notebook 결합으로 완전 오프라인 지식 관리 시스템 테스트. PDF/YouTube → 팟캐스트 파이프라인 구현.

## 주요 기능

- **멀티소스**: PDF, YouTube, URL, 오디오, 텍스트 복합 인제스트
- **18개 AI 제공사**: OpenAI, Anthropic, Google, Groq, Ollama 등 자유 선택
- **팟캐스트 생성**: 멀티스피커 오디오 자동 생성 (NotebookLM 시그니처 기능 재현)
- **로컬 배포**: Docker compose 단일 명령, 완전 오프라인 가능

## 관련 페이지

- [[LLM-Wiki]] — 유사한 지식 관리 패턴
- [[project-nomad]] — 오프라인 AI 자급자족 시스템
- [[VoxCPM]] — 오픈소스 TTS (팟캐스트 생성 결합 가능)
- [[VibeVoice]] — Microsoft 오픈소스 STT/TTS

## 원본

- 출처: https://github.com/lfnovo/open-notebook
- 스타: ⭐26,200 (2026-06-06 기준)
- 신뢰도: ⭐⭐⭐⭐⭐
