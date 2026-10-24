---
title: OpenBMB/VoxCPM — 토크나이저 없는 오픈소스 TTS 모델
type: source
domain: ai-news
tags: [ai-news, github-trending, tts, voice-cloning, multilingual, tokenizer-free, openBMB]
created: 2026-04-10
updated: 2026-10-24
sources: []
reliability: high
---

# OpenBMB/VoxCPM

> [!insight] 핵심 인사이트
> 토크나이저(Tokenizer) 없이 직접 음성을 처리하는 새로운 TTS 아키텍처. 다국어 합성 + 스타일 전이 + 실제 음성 클로닝까지 하나의 모델로 처리. 스타 30,552개(2026-06-17, +418 당일, prev 25,364). 30개 언어 지원·48kHz 품질·RTF 0.13 실시간 처리. Apache-2.0.

## 핵심 인사이트

> [!action] 당장 할 것
> `/reat-voice` 스킬의 ElevenLabs 대체 오픈소스 후보로 검토. 로컬 배포 가능 여부 확인.

> [!note] 배경 정보
> OpenBMB(Open Big Model Benchmark)는 CPM 시리즈(Chinese Pretrained Model)로 유명. VoxCPM은 텍스트 도메인의 CPM 철학을 음성으로 확장한 것.

> [!question] 미해결 질문
> 한국어 지원 수준? 실시간(스트리밍) TTS 가능? GPU 요구사항? ElevenLabs 대비 음질?

## 도메인별 추출 (ai-news 템플릿)

- **신뢰도**: ⭐⭐⭐ — 스타 24,625개, OpenBMB 연구팀 신뢰도 높음
- **즉시 활용**: YES — reat-voice 파이프라인 ElevenLabs 비용 절감 후보
- **6개월 영향력**: TTS API 비용 0으로 만드는 경쟁 압력. ElevenLabs 포지셔닝 위협
- **대체 관계**: ElevenLabs / OpenAI TTS 대체 오픈소스 후보
- **허와 실**: "토크나이저 없음"이 실제 음질·속도 이점으로 이어지는지 검증 필요
- **액션**: 로컬 설치 + 한국어 음성 품질 테스트

## 관련 페이지

- [[TTS-오픈소스]]
- [[reat-voice]]

## 원본

- 출처: https://github.com/OpenBMB/VoxCPM
- 스타: 30,552 (2026-06-17 기준, +418 당일) ← 25,364 (2026-06-03)
- 신뢰도: ⭐⭐⭐

---

## 🔄 2026-10-24 재수집 업데이트 — 벤치 수치 전수 대조 + 3대 미해결 질문(한국어·스트리밍·GPU) 해소

**관측 시각**: 2026-10-24 09:06 UTC (18:06 KST) · GitHub API + README 실열람

- 실측: ⭐ **40,427** · fork **4,591** · open_issues 155 · Python · Apache-2.0 · created **2025-09-16** · pushed **2026-10-08** · subscribers 170 · topics 14개(`tts·voice-cloning·multilingual` 등)
- 수집기 대조: ★40,426→**40,427 (+1 드리프트)** · fork **4,591 완전일치** · #7 · 당일 +150 · 라이선스 일치.
- 📈 직전 추적치(log.md) **2026-06-17경 ⭐30,552** → 오늘 **40,427**, 약 128일간 **+9,875**(1.32배, 일평균 약 +77).

> [!warning] 🔧 볼트 자기정정 2건
> 1. **생성일**: 본 레포 `created_at` 은 **2025-09-16** — 1년 넘은 레포다. 기존 페이지는 2026년 프로젝트처럼 서술했다.
> 2. **RTF 수치**: 기존 페이지 *"RTF 0.13 실시간"* 은 **가속 구현(Nano-vLLM) 수치**였다. README 표 기준 **표준 PyTorch RTF ~0.30 (RTX 4090)**, Nano-vLLM ~0.13. 수집기 *"RTF 4090 ~0.30"* 이 **표준값으로 정확**하다. VRAM ~8GB.

> [!insight] 🏆 수집기 벤치 수치가 README 표와 **완전 일치** — 드리프트 0
> Seed-TTS-eval(README 실열람): **VoxCPM2(2B) test-EN WER 1.84 / SIM 75.3 · test-ZH CER 0.97 / SIM 79.5 · test-Hard CER 8.13.** 🎯 **수집기가 보고한 세 수치(EN WER 1.84/SIM 75.3, ZH CER 0.97/SIM 79.5, Hard CER 8.13)가 표와 글자 단위로 일치.** 수집기 사양(VoxCPM2 2B · 30langs · 48kHz)도 전부 확인.
> ⚖️ **단 해석 주의**: 표에서 VoxCPM2 는 **최저 WER/CER 이 아니다** — EN WER 은 FishAudio S2(0.99)·Qwen3-TTS(1.23)가 더 낮고, test-Hard CER 8.13 은 비교군 중 **최악**(VibeVoice·CosyVoice3 등이 5~7). 즉 *"오픈소스 2B 다국어 올라운더"* 이지 *"단일 지표 SOTA"* 는 아니다. [[측정도구-먼저-반증]] 식으로 보면 **마케팅 걷어낸 실체 = 30언어 범용성이 강점, 영어 난이도 세트는 약점.**

> [!insight] ✅ 2026-04 이후 미해결 3질문이 README 로 해소됐다
> 기존 페이지 [!question]: *"한국어 지원 수준? 스트리밍 가능? GPU 요구?"*
> - **한국어**: 30개 공식 언어 목록에 **Korean 포함**. 내부 30언어 ASR 벤치 **한국어 CER 0.95%**(VoxCPM2). Minimax-MLS 한국어는 WER 1.962(중위권)·**SIM 83.3(비교군 최고)** → **명료도 중상, 화자 유사도 최상.** ⇒ [[reat-voice]] 한국어 더빙 후보로 **실측 근거 확보.**
> - **스트리밍**: `model.generate_streaming()` API 존재 → **YES.** FastAPI HTTP 서버·배치 동시요청 지원.
> - **GPU**: **~8GB VRAM / RTX 4090 기준 RTF 0.30**(가속 0.13). 로컬 배포 현실적.
> - 아키텍처: tokenizer-free diffusion-AR, AudioVAE V2, `LocEnc→TSLM→RALM→LocDiT`, arXiv 2606.06928.

> [!action] 당장 할 것 (갱신)
> [[reat-voice]] ElevenLabs 대체 후보로 **한국어 실측**: SIM 최상(83.3)이 음성 복제 용도에 유리. Apache-2.0 상업 이용 가능. 로컬 8GB GPU 설치 → 한국어 자연성·안정성 직접 테스트(README 경고: Voice Design/Controllable Cloning 은 run 간 변동 있어 1~3회 재생성 권장).

### 원본 갱신
- 검증: 2026-10-24 09:06 UTC GitHub API + **README 실열람(Seed-TTS-eval·Minimax-MLS·내부30언어 표 대조)** — ★+1 드리프트 · fork 완전일치 · **벤치 3수치 표와 일치** · 생성일/RTF 자기정정
- 신뢰도: ⭐⭐⭐ (⭐40,427 · Apache-2.0 · OpenBMB 공식 · 벤치 논문 arXiv) / ⚠️ 단일지표 SOTA 아님 · 한국어 자연성 직접 테스트 미실시

- 🔄 **2026-10-24 (교차 참조)**: VoxCPM GitHub README 의 Seed-TTS-eval 표가 **Fish Audio S2(4B) en WER 0.99 / zh CER 0.54 / hard 5.99** 를 싣는다(VoxCPM2 2B = 1.84 / 0.97 / 8.13). 같은 날 [[drama-3]](Fish Audio 후속작) 논문의 Seed-TTS-Eval 최종값은 **1.54 / 0.83** ⇒ 후속작이 전작보다 표준 지표가 나쁘다(단 S2 값은 VoxCPM 측 인용이라 채점 조건 미확인). 첫 테이크 기준 Drama 3 en **2.20** 은 VoxCPM2 1.84 보다도 나쁘고, 재생성 후 최종 1.54 는 낫다 → [[비매칭-비교]]. 🎯 **한국어 로컬 TTS 기본값으로는 VoxCPM2(Apache-2.0·2B) 유지**가 타당 — Drama 3 는 FP8 35.9B 로 소비자 GPU 불가 · 라이선스 Hosted Service 제한.
