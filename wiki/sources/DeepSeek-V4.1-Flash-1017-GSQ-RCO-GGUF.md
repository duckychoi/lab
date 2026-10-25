---
title: "DeepSeek-V4.1-Flash-1017 GSQ-RCO GGUF — 763B 를 1.75~2.25bpw 로. '100.0% 유지'의 1/3 은 기준선이 이미 만점인 AIME25 이고, 카드엔 TBD 6개가 남아 있다"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, quantization, moe, deepseek, ista-daslab, strata, 천장-기준선, 미완성카드, llama-cpp-미지원]
created: 2026-10-25
updated: 2026-10-25
sources: [DeepSeek-V4.1-Flash-1017.md, Qwen3.8-27B-GSQ-RCO-GGUF.md, Qwen3.8-Flash-Next-GSQ-RCO-GGUF.md]
reliability: medium
---

# ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF

**HF**: https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF · [[ISTA-DASLab]] · 베이스 [[DeepSeek-V4.1-Flash-1017]]
**실측(2026-10-25 KST)**: downloads **32,479**(수집기 일치) · likes 240 · createdAt **2026-10-23** · `library_name: gguf` · MIT
**빌드**: IQ1_M 1.75bpw (백본 120.72GB + Engram 110.60GB = **231.32GB**) · **IQ2_XXS 2.00bpw 248.84GB(권장)** · IQ2_XS 2.25bpw 265.83GB · Engram 룩업테이블(196.6B 파라미터 · IQ4_NL) 공유 파일
**신뢰도**: ⭐⭐ (같은 랩 3번째 GSQ-RCO 릴리스 · 측정 3벤치뿐 · 카드 미완성)

> [!insight] 🏆 핵심 인사이트 — **"100.0% 회복"의 정보량은 3축 중 2축분이다 → 🆕 [[천장-기준선]]**
> 카드 표: Base **AIME25 100.00** · GPQA-D 90.91 · LCB v6 89.71 · 평균 93.54.
> - AIME25 는 기준선이 **만점**이다 ⇒ 양자화가 아무리 손상시켜도 *"위로"* 는 볼 수 없고, 만점 유지는 **30문항 포화 구간의 무변화**일 뿐이다.
> - 🎯 **볼트 재계산 — IQ1_M**: 카드 *"98.7% retains"* (92.32/93.54) ↔ **천장 축 제외 시** (88.38+88.57)/(90.91+89.71) = **97.97%** ⇒ 천장 축이 회복률을 **+0.73%p** 부풀린다. 평균 손실 1.22점은 실제로는 **비천장 2축 평균 1.84점** 손실이다.
> - IQ2_XXS 는 비천장 2축도 기준선과 **소수 둘째 자리까지 동일**(90.91 · 89.71) ⇒ 이쪽은 천장과 무관하게 무손실 주장이 성립한다(자기보고 기준).
> 📌 같은 랩 3릴리스 연속 AIME25 기준선 100.00([[Qwen3.8-27B-GSQ-RCO-GGUF]] · [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] · 본 건) ⇒ **랩의 평가 스위트 자체가 포화 축 1개를 고정 포함한다.**

> [!warning] 🔴 카드가 미완성이다 — HTML 주석 `TBD` **6건**
> ① *"Memory requirements"* 섹션 본문 = `<!-- TBD: confirm how Strata places the model on a 12 GB GPU (which tensors stay in VRAM, how much system RAM it needs) -->` ② IQ2_XS 행 미측정 ③ Strata 실행 명령 ④ llama.cpp 실행 경로 ⑤ 빌드별 전문가 양자화 타입·탐색 텐서 수(방법 섹션) ⑥ 연산 지원 감사문(*"copied from the Flash-Next card"*).
> ⇒ 🎯 **간판 주장 "single GPU with 12 GB of VRAM"(47·72·109행 3회 반복)의 근거 섹션이 비어 있다.** 시스템 RAM 요구량 0건 — 231GB 이상 파일을 12GB GPU 로 돌리면 나머지는 RAM 또는 디스크 mmap 인데 그 양을 안 적었다. → [[선언된-구현체-공백]]
> 🔴 **런타임**: *"As of October 23, 2026, llama.cpp does not support DeepSeek-V4.1"* — 유일 실행 경로는 Strata(`Niko1221/Strata`). llama.cpp PR #30817(draft)은 Engram 을 모델 GGUF 안에 넣는 **다른 포맷**이라 이 파일과 호환 미정(카드 주석).

> [!question] 파라미터 산술
> 백본 **551.9B** + Engram **196.6B** = **748.5B** ↔ 베이스 `safetensors.total` **763.2B**(10-24 실측) ⇒ **14.7B 차이 미설명**(MTP 층 등 제외분 추정 · 카드 미기재) → [[단위-불일치]]

## 도메인별 추출 (local-llm)
- **실용성 판단**: 디스크 231~266GB · GPU 12GB(주장) · RAM 미기재 · llama.cpp 불가 ⇒ **지금 당장 실배포 NO**
- **메모리 아키텍처**: Engram 룩업테이블은 토큰당 1행 희소 접근 → mmap 으로 디스크 상주(카드 82행) — 🎯 **"모델 파라미터의 26%가 VRAM/RAM 불필요"** 는 [[에이전트-메모리-레이어]] 의 외부DB 와 닮은 구조(룩업 = 메모리)
- **Hermes 적용**: NO
- **트레이드오프**: IQ1_M 은 IQ2_XXS 대비 **17.5GB 절약에 비천장 1.84점 손실**
- **오픈소스 구현체**: Strata(단일 경로)

## 관련 페이지
- 🆕 [[천장-기준선]] · [[ISTA-DASLab]] · [[DeepSeek-V4.1-Flash-1017]] · [[DeepSeek]] · [[선언된-구현체-공백]] · [[단위-불일치]]
- [[Qwen3.8-27B-GSQ-RCO-GGUF]] · [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] — 같은 랩 선행 릴리스
- 같은 배치 GGUF: [[flint-GGUF]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/ISTA-DASLab/DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF
- 신뢰도: ⭐⭐ (HF 다운로드 32,479 · 자기보고 · 카드 미완성)
