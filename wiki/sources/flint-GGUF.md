---
title: "unsloth/flint-GGUF — 39.8B/활성 ~2.5B 코딩 에이전트 MoE. 양자화본이 원본의 16.5배 다운로드, 그리고 비교표는 PNG 에만 있다"
type: source
domain: local-llm
tags: [local-llm, hf-model, gguf, moe, coding-agent, unsloth, 원본-파생-역전, 벤치마크-이미지-봉인, swe-bench, terminal-bench]
created: 2026-10-25
updated: 2026-10-25
sources: [unsloth.md]
reliability: medium
---

# unsloth/flint-GGUF (원본 RecursiveSI/flint)

**HF**: https://huggingface.co/unsloth/flint-GGUF · 양자화 [[unsloth]] · 원본 https://huggingface.co/RecursiveSI/flint ([[RecursiveSI]])
**실측(2026-10-25 KST · HF API)**: GGUF downloads **78,891** · likes 231 · createdAt 2026-10-20 · apache-2.0 ‖ 원본 downloads **4,795** · likes **796** · createdAt 2026-10-21 · `library_name: transformers`
**신뢰도**: ⭐⭐ (수치 전부 자기보고 · 비교표 이미지 봉인)

> [!insight] 핵심 인사이트 — **원본보다 하루 먼저 생성된 파생본이 16.5배 다운로드됐다**
> - GGUF createdAt **10-20T03:26Z** < 원본 createdAt **10-21T14:20Z** ⇒ 🎯 **양자화본이 원본 공개 전에 준비됐다**(사전 협업 · [[원본-파생-역전]] 09-22 "설계된 역전" 유형).
> - 다운로드 **78,891 vs 4,795 = 16.5배** · 좋아요 **231 vs 796 = 0.29배** ⇒ **다운로드는 파생으로, 평판은 원본으로** — 09-20 관측 패턴 재현.
> - ⚖️ 규약 ⑰: GGUF 는 파일당 계수가 아니다(`library_name` None · gguf 레포 계수 규칙은 확인 필요) — 이번엔 배수 보정 근거 없음, 원값 인용.

> [!warning] 🔴 비교표가 이미지에만 있다 → [[벤치마크-이미지-봉인]] ①형
> 원본 카드 Evaluation 섹션 = `assets/flint_benchmarks_nvfp4.png` 1장. 텍스트 수치는 22행 한 문장뿐: *"54.9% on Terminal-Bench 2.1, 89.7% on SWE-bench Pro v2, and 74.2% on SWE-bench Verified"*. **경쟁 모델 수치는 그림 밖에서 인용 불가.**
> ✅ 측정 조건은 텍스트로 적었다: temp 1.0 · top-p 0.95 · top-k 20 · TB = Terminus 2 · SWE = mini-swe-agent · pass@1 ≥5회 평균 · *"† marks scores measured by Recursive; other comparison scores are developer-reported"* ⇒ 그림 속 비교는 **자기측정 vs 남의 자기보고 혼합** → [[비매칭-비교]].
> 🏆 **자기에게 불리한 조정을 먼저 적는다**: *"Flint's Terminal-Bench score counts solutions obtained through **web retrieval as unsuccessful**; developer-reported scores may not apply the same adjustment"* → [[측정도구-먼저-반증]] 계열의 정직성.

> [!question] 미해결 — SWE-bench Pro v2 89.7% > Verified 74.2%
> 일반적으로 Pro 계열이 Verified 보다 어렵다고 알려져 있는데(볼트 기억 · 미검증) 점수가 **15.5p 높다.** "Pro v2" 가 다른 과제 분포인지, 오기인지 카드로 판별 불가. 인용 시 이 역전을 병기한다.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 총 39.8B · 활성 ~2.5B(256 전문가 중 6 + 공유 1) · 262K 컨텍스트 · 원본 BF16 ~80GB(B300/H200 1장) ⇒ **GGUF 로 소비자 GPU/맥 실행 가능 범주**(활성 2.5B 라 토큰 속도 유리 — 추정)
- **메모리 아키텍처**: 해당 없음(일반 LLM)
- **Hermes 적용**: 🎯 **후보** — ChinameBot 의 툴콜 백엔드로 OpenAI 호환 tool call 지원(원본 카드 92행). 단 *"preserve returned `reasoning_content`"* 요구
- **트레이드오프**: 카드 자신이 *"Long reasoning can increase latency and exhaust the output budget"* 경고
- **오픈소스 구현체**: GGUF(llama.cpp 계열) · 원본에 SGLang 서빙 킷

## 관련 페이지
- [[unsloth]] · [[RecursiveSI]] · [[원본-파생-역전]] · [[벤치마크-이미지-봉인]] · [[비매칭-비교]] · [[측정도구-먼저-반증]] · [[RSI-프레이밍]](제작사명)
- 같은 배치 GGUF: [[DeepSeek-V4.1-Flash-1017-GSQ-RCO-GGUF]]
- [[local-llm]]

## 원본
- 출처: https://huggingface.co/unsloth/flint-GGUF · https://huggingface.co/RecursiveSI/flint
- 신뢰도: ⭐⭐ (HF 다운로드 78,891 · 자기보고)
