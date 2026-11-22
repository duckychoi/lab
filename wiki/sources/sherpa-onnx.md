---
title: "k2-fsa/sherpa-onnx — 오프라인 음성 처리 종합 툴킷 (ASR · TTS · 화자분리 · VAD · 12개 언어 바인딩 · NPU 지원)"
type: source
domain: local-llm
tags: [local-llm, github-trending, asr, tts, diarization, vad, onnx, on-device, embedded]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/k2-fsa/sherpa-onnx]
reliability: high
---

**GitHub**: ★16,087(볼트 API 11-22 · 수집기 일치) · C++ · Apache-2.0 · 생성 2022-09-01 · push 2026-11-21

## 핵심 인사이트
> [!insight] 모델이 아니라 "음성 기능을 기기에 싣는 배관"
> ONNX Runtime 기반으로 인터넷 없이 음성 인식 · 합성 · 음원 분리 · 화자 식별/검증/분리 · 언어 식별 · 오디오 태깅 · VAD · 키워드 스포팅 · 구두점 복원 · 음성 향상 · 강제 정렬. Android · iOS · Windows · macOS · Linux · HarmonyOS(x64/x86/arm64/arm32/riscv64) + WebAssembly, 바인딩 12종, Rockchip · Qualcomm · Ascend NPU. [[k2-fsa]] 의 [[OmniVoice]] 가 모델 쪽이라면 이쪽은 런타임 쪽이다. 볼트의 [[openwhispr]] 가 이미 이를 구성요소로 쓴다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 임베디드 · 모바일 실배포 가능(4년 된 프로젝트). 품질은 붙이는 모델에 좌우 — README 상단에 정확도 수치 없음.
- **메모리 아키텍처**: 해당 없음.
- **Hermes 적용**: ChinameBot 음성 입력(VAD + ASR)과 강제 정렬(자막 타이밍)에 후보. 쇼츠 파이프라인의 SRT 정렬에도 쓸 수 있는지 시험 가치.
- **트레이드오프**: 범용 런타임이라 최신 대형 음성 모델은 ONNX 변환 지원을 기다려야 한다.
- **오픈소스 구현체**: 본 레포.

## 관련 페이지
- [[k2-fsa]] · [[OmniVoice]] · [[openwhispr]] · [[ZONOS3-Mini]] · [[openvino]] · [[local-llm]]

## 원본
- 출처: https://github.com/k2-fsa/sherpa-onnx
- 확인 범위: GitHub API(스타 · 언어 · Apache-2.0 · 생성일 · push) · 🔴 README 기능 목록은 수집기 판독
- 신뢰도: ⭐⭐⭐⭐
