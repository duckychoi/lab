---
title: openbmb/MiniCPM5-1B — 초소형 1B 파라미터 강력 텍스트 생성 모델
type: source
domain: ai-news
tags: [ai-news, local-llm, edge-ai, slm, openbmb, text-generation, on-device, 1B]
created: 2026-05-28
updated: 2026-07-15
sources: []
reliability: high
---

# openbmb/MiniCPM5-1B — 초소형 1B 파라미터 고성능 텍스트 모델

## 핵심 인사이트

> [!insight] 핵심 인사이트
> MiniCPM 시리즈의 최신작. SFT+RL+OPD 학습, Think/No-Think 모드 전환 지원. 1B 초소형 파라미터로 강력한 텍스트 생성 — 동급 1B 모델 중 도구 사용·코드·추론 SOTA 주장. HF 다운로드 68,494 (2026-06-03, prev 45,700).

> [!note] 2026-07-15 — 커뮤니티 GGUF 변종 유입 (GnLOLot/MiniCPM5-1B-...-Thinking-GGUF, DL 89.9k)
> 자동수집에 `GnLOLot/MiniCPM5-1B-Claude-Opus-Fable5-Thinking-GGUF`(HF DL 89.9k, likes 239)가 별도 트렌딩으로 등장. **베이스 [[OpenBMB]] MiniCPM5-1B의 커뮤니티 추론(thinking) 특화 GGUF 양자화·머지판** — 원본/양자화 관계라 별도 페이지 대신 여기에 통합. 이름의 상표성 표기(Claude/Opus/Fable5)는 [[Qwythos-9B]]·비-공식 GGUF들과 같은 커뮤니티 명명 관행으로, **실제 성능·학습 데이터는 별도 검증 필요**(reliability low). 초경량 로컬 추론용 GGUF 수요가 1B 급에도 형성됨을 보여주는 신호 — 베이스가 이미 fast/think 2모드를 내장하므로 변종의 실효 이득(추가 thinking 튜닝)은 미검증.

> [!note] 2026-07-10 갱신 — DL 363k (한 달 +295k 급증), 제작 [[OpenBMB]]
> WebFetch 모델카드 실측: DL 68k→**362,863**로 5배 이상 급증(온디바이스 SLM 실수요 확인). 스펙 정정·보강 — 총 **1,080,632,832 파라미터**(비임베딩 679,552,512), LlamaForCausalLM 24층·16 Q헤드·2 KV헤드(GQA), **컨텍스트 131,072**. 기능: 내장 `<think>` 템플릿으로 **fast(빠른 응답) ↔ think(추론) 2모드 토글**, XML 스타일 **도구 호출**(SGLang 파서 호환), FlagOS로 다칩 지원. 학습 **RL + 온폴리시 증류([[온폴리시-증류]])**로 수학·코드 평균 **+16점**, 최대토큰 초과 응답 **-29%p**. 포맷 BF16/GGUF/MLX, Apache 2.0. → 1B로 "도구+추론"까지 넣은 온디바이스 에이전트 백엔드 실체.

## 도메인별 추출 (local-llm 템플릿)

- **실용성 판단**: YES — 1B은 CPU 전용 환경, 스마트폰, 임베디드 시스템에서도 실행 가능. 최소 RAM ~2GB
- **메모리 아키텍처**: 표준 디코더 트랜스포머, 고밀도 파라미터 효율화 적용
- **Hermes 적용**: 가능 — 단순 명령 수행·요약·분류 태스크에 로컬 추론 레이어로 투입. 복잡한 멀티스텝 추론은 어려울 수 있음
- **트레이드오프**: 1B → 초저지연·초저메모리 but 복잡 추론 한계. 코딩/수학보다 대화·분류·요약 특화
- **오픈소스 구현체**: https://huggingface.co/openbmb/MiniCPM5-1B — 직접 다운로드·llama.cpp 변환 가능

## 실용성 평가

> [!action] 당장 할 것
> llama.cpp GGUF 변환 또는 Ollama 통해 로컬 실행 테스트. 한국어 성능 확인 (MiniCPM 시리즈 한국어 지원 수준).

> [!question] 미해결 질문
> MiniCPM5 vs MiniCPM-V-4.6 (멀티모달): 순수 텍스트에선 어느 게 더 강한가? 한국어 지원 수준?

## 관련 페이지

- [[MiniCPM-V-4.6]] — OpenBMB 멀티모달 VLM 버전 (1B 동일 스케일)
- [[Qwen3-0.6B]] — 경쟁 초소형 모델 (0.6B)
- [[Qwen3.6-35B-A3B-GGUF]] — GGUF 양자화 실용 사례
- [[시계열-예측-파운데이션-모델]] — 소형 특화 모델의 파운데이션 접근
- [[에이전트-메모리-레이어]] — 경량 에이전트 백엔드 후보

## 원본

- 출처: https://huggingface.co/openbmb/MiniCPM5-1B
- 다운로드: 362,863 (2026-07-10) ← 68,494 (2026-06-03) ← 45,700
- 파라미터: 1.08B(비임베딩 0.68B) / 24층 GQA / 131K 컨텍스트 / Apache 2.0
- 제작: [[OpenBMB]] · 태스크: Text Generation(think·fast 2모드, 도구호출)
- 신뢰도: ⭐⭐⭐⭐ (모델카드 WebFetch 실측 / 벤치 자가측정)
