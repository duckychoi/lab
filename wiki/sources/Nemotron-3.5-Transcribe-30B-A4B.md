---
title: "NVIDIA Nemotron-3.5-Transcribe-30B-A4B — 1시간 녹음을 한 번에 받는 40개 언어 ASR·번역·화자분리. 비교 대상 상당수가 수십 배 작은 모델"
type: source
domain: local-llm
tags: [local-llm, hf-model, asr, speech, diarization, speech-translation, moe, mamba, nvidia, openmdw]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B, Nemotron-3-Diarization.md]
reliability: high
---

**HF**: [nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B](https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B) · 다운로드 **63,798(30일)** / 누적 63,846(볼트 11-08 API · 수집기 61,049 → +2,749/1일) · ♥3,102 · trendingScore 288(수집기 303.5) · license **OpenMDW-1.1** · base Nemotron-3.5-Lightning-30B-A3B · 34B(활성 4.3B) · created **2026-10-07** · sha `c1766764`(lastModified 10-29)

## 핵심 인사이트
> [!insight] "청크로 자르고 이어붙이기"를 없앤 롱폼 ASR
> Mamba-2–Transformer 하이브리드 MoE LLM + 병렬 전문가 인코더(ASR 인코더 · 화자 인코더 = [[Nemotron-3-Diarization]], 카드 링크로 볼트 확인 — **11-07 볼트 미대조 항목 해소**). 65,536 토큰 컨텍스트로 **최대 1시간 오디오를 한 번에**: 축자/정서체 전사 · 문맥 전사 · 화자 귀속 · 음성번역 · 언어식별 · 오디오 QA · 단어 타임스탬프. 회의록 파이프라인에서 분할·화자 정합 후처리가 통째로 빠진다.

> [!warning] 비교의 체급 차이
> 카드(볼트 grep 전건 검출, 2026-10-12 측정, WER 낮을수록 좋음): Open ASR 9세트 **4.71** vs Qwen3-ASR-1.7B 4.94 · 롱폼 **10.98** vs Parakeet-TDT-0.6B-v3 13.37 · 다국어 7개 **4.62** vs Qwen3-ASR-1.7B 6.49 · 다화자 cpWER **15.80** vs DiCoW v3.3+DiariZen 16.83. ⇒ **활성 4.3B / 총 34B 가 1.7B·0.6B 를 이긴 것**이고 격차는 0.23~2.4 포인트. 체급을 지우면 압승처럼 읽힌다 → [[비매칭-비교]]. 처리량 *초당 최대 2,238초 오디오* 는 RTX PRO 6000 · NVFP4 + DFlash2 조건.

## 도메인별 추출 (local-llm)
- **실용성 판단**: H100 80GB 1장(BF16/FP8, vLLM). FP8·NVFP4 변형 있음 — 소비자 GPU 는 확인 필요.
- **Hermes 적용**: 조건부 — 장시간 음성(회의·인터뷰·강의) 로컬 전사가 필요할 때 1순위 후보. 현재 봇엔 음성 입력 경로 없음.
- **트레이드오프**: 품질·롱폼 vs 80GB VRAM. 짧은 클립이면 1.7B 급이 비용 대비 합리적.
- **오픈소스 구현체**: 가중치 공개 · OpenMDW-1.1(상업 사용 가능 명시).

## 관련 페이지
- [[NVIDIA]] · [[Nemotron-3-Diarization]] · [[비매칭-비교]] · [[Qwen]]

## 원본
- 출처: https://huggingface.co/nvidia/NVIDIA-Nemotron-3.5-Transcribe-30B-A4B
- 확인 범위: HF API expand(볼트 11-08) · 카드 raw 130,543B grep(4.71·10.98·4.62·15.80·4.94·13.37·6.49·16.83·2,238·OpenMDW·65,536·40 languages·Nemotron-3-Diarization 검출) · 추론 실행 0회
- 신뢰도: ⭐⭐⭐ (NVIDIA 공식 · 카드 수치 일치 · 독립 재현 없음)
