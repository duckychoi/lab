---
title: Fish Audio — 오픈 웨이트 TTS 개발사 (fish-speech · S2 · Drama 3)
type: entity
domain: ai-news
tags: [ai-news, entity, tts, voice-cloning, fish-audio, 오픈웨이트]
created: 2026-10-24
updated: 2026-10-24
sources: [drama-3.md]
reliability: medium
---

# Fish Audio

> [!insight] 한 줄
> **오픈 웨이트 TTS 를 내면서 상업 호스팅은 별도 계약으로 묶는 회사.** 최신작 [[drama-3]] 은 표준 정확도 지표(WER·SIM)를 RL 보상에서 의도적으로 빼고 "연출 가능한 연기"를 내세웠다 — 그 결과 Seed-TTS-Eval 에서 **전작 S2 보다 수치가 나쁘다**(볼트 대조 · 2026-10-24).

## 확인된 것 (2026-10-24 · 1차 자료)
- HF 조직 `fishaudio` · GitHub `fishaudio/fish-speech`(카드 링크 — 레포 자체는 볼트 미열람) · 플레이그라운드 fish.audio
- 모델 계보(문서에 나온 이름만): **OpenAudio-s1-mini**(0.5B · [[VoxCPM]] README 표에 등장) → **Fish Audio S2**(4B · 같은 표 Seed-TTS-Eval en WER 0.99 / zh CER 0.54) · **S2-Pro**(VoxCPM README 다국어표) → **[[drama-3]]**(35B 총 / 3B 활성 MoE · 2026-10)
- 라이선스: **Fish Audio Community License v1.0**(2026-10-13) — 연구·비상업 무료 · **연매출 USD 500,000 미만** 상업 허용 · **Hosted Service(TTS·보이스클로닝을 제3자에게 API/앱으로 제공)는 매출과 무관하게 별도 계약** · 자기 콘텐츠 내레이션·더빙 및 결과물만 납품하는 대행은 Hosted Service 아님
- 🔴 HF 메타데이터는 같은 모델에 `fish-audio-research-license` 로 표기(간판 불일치) → [[간판-지체]]

⬜ 미확인: 법인 소재·규모·투자, S2 기술보고서 원문(볼트 미보유), fish-speech GitHub 스타 수

## 관련 페이지
- [[drama-3]] · [[VoxCPM]] · [[OmniVoice]] · [[higgs-audio-v3-tts]] · [[pocket-tts]]
- [[Qwen]] ← Drama 3 백본 초기화 출처
- [[간판-지체]] · [[벤치마크-외부축]]

## 원본
- https://huggingface.co/fishaudio · https://huggingface.co/fishaudio/drama-3/blob/main/LICENSE · arXiv 2610.18010
- 신뢰도: ⭐⭐ (단일 모델 기준 · 회사 정보 전무)
