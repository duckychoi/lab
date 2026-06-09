---
title: Microsoft ONNX Runtime — 크로스플랫폼 ML 추론·학습 가속기 (⭐20,678)
type: source
domain: ai-news
tags: [ai-news, github-trending, local-llm, edge-ai, inference, ONNX, microsoft, NPU, cross-platform, optimization]
created: 2026-05-30
updated: 2026-05-30
sources: []
reliability: high
---

# Microsoft ONNX Runtime — 크로스플랫폼 ML 추론 가속기

## 핵심 인사이트

> [!insight] 핵심 인사이트
> CPU/GPU/NPU 모두에서 ONNX 모델을 고속 추론·학습하는 Microsoft 오픈소스 런타임. ⭐20,678. 엣지 AI 배포의 사실상 표준 — iOS/Android/Windows/Linux/Web 모두 지원. [[MiniCPM5-1B]] 같은 소형 모델을 엣지에 배포할 때 핵심 인프라.

## 도메인별 추출 (local-llm 템플릿)

- **실용성 판단**: 실배포 가능 YES — 프로덕션 검증된 Microsoft 공식 런타임. PyTorch/TF 모델 → ONNX 변환 후 바로 배포
- **하드웨어**: CPU (x86/ARM), CUDA GPU, DirectML (Windows), CoreML (Apple), NNAPI (Android), NPU (Qualcomm, Intel)
- **지연시간**: PyTorch 대비 CPU에서 2~5배, GPU에서 1.2~2배 빠름 (모델/하드웨어 따라 상이)
- **메모리 아키텍처**: 정적 계산 그래프 → 메모리 최적화 용이, 양자화(INT8/INT4) 완전 지원
- **오픈소스 구현체**: https://github.com/microsoft/onnxruntime — pip install onnxruntime-gpu

> [!action] 당장 할 것
> HuggingFace Optimum 라이브러리로 Transformers 모델 → ONNX 변환 자동화. `from optimum.onnxruntime import ORTModelForCausalLM`으로 기존 코드 최소 수정 배포.

## 주요 기능

- **최적화 실행 공급자**: CUDA, TensorRT, DirectML, OpenVINO, CoreML 등 15+ EP
- **학습 가속**: PyTorch ORT (학습 단계 가속화)
- **양자화**: INT8/INT4 정적·동적 양자화, QNN/NNAPI 연동
- **GenAI API**: LLM 특화 추론 API (ONNX Runtime GenAI)
- **웹 지원**: ONNX Runtime Web (WebAssembly + WebGPU)
- **크로스 플랫폼**: Python, C++, C#, Java, JavaScript 바인딩

## 관련 페이지

- [[MiniCPM5-1B]] — ONNX Runtime으로 엣지 배포 가능한 1B 모델
- [[에이전트-메모리-레이어]] — 엣지 에이전트 배포와 추론 최적화
- [[Qwen3.6-35B-Uncensored]] — 대형 모델 양자화 배포

## 원본

- 출처: https://github.com/microsoft/onnxruntime
- 스타: ⭐20,678 (+10, 2026-05-30 기준)
- 신뢰도: ⭐⭐⭐⭐⭐
