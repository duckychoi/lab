---
title: "Zyphra/ZONOS3-Mini — 총 800M · 활성 약 100M 다국어 TTS · 음성 복제 (43개 언어 · 한국어 포함 · Apache-2.0 · WER/유사도 수치는 카드에 없음)"
type: source
domain: local-llm
tags: [local-llm, hf-model, tts, voice-cloning, korean, latent-moe, on-device, apache-2.0]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/Zyphra/ZONOS3-Mini]
reliability: medium
---

**HF**: dl30 154,251(볼트 API 11-22 · 수집기 11-21 142,778) · 좋아요 **574**(수집기 622 — 🟡 불일치, 아래) · 생성 2026-11-09 · 내부 ID `6af1543d…` · apache-2.0

## 핵심 인사이트
> [!insight] 한국어 + Apache-2.0 + 온디바이스 런타임 — 쇼츠 음성 파이프라인의 로컬 후보
> 총 800M · 토큰당 활성 약 100M([[latent-MoE]] 64 experts top-2, GDN 9층 + 전역 어텐션 2층). 15Hz 듀얼 코덱 프레임(코드북 10 × 4,096)을 자기회귀 생성해 44.1kHz 스트리밍 렌더. 샘플 음성 복제, 나이 · 억양 · 음색 설계, 단어 단위 감정 · 속도 조절. 브라우저 WebGPU · CUDA · MLX · C++/ggml(CPU/Vulkan), 기본 음성 27종, OpenAI 호환 `/v1/audio/speech` 서빙.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 🟡 시험 가치 있음. **한국어는 카드 103행(언어 표 East Asia: Mandarin · Japanese · Korean)과 153행(NeMo 텍스트 정규화 9개 언어)에 명시**(볼트 확인).
- **트레이드오프**: 🔴 **카드에 WER · 화자 유사도 수치 없음** — 184 · 186행은 "H100 80GB 1대에서 품질-속도 그림"의 설명(품질 = ½ z(유사도) − ½ z(WER), ZTTS2-Eval 55개 언어 서브셋)뿐이고 값은 그림 안에 있다([[벤치마크-이미지-봉인]]). 상세는 블로그 · arXiv 2611.16525(미확인). "폰 · 노트북 실시간"은 자칭.
- **Hermes 적용**: ChinameBot 음성 응답 · 쇼츠 내레이션(현재 클라우드 TTS)의 로컬 대체 후보 — 한국어 발음 · 숫자 읽기를 직접 들어 봐야 한다.
- **메모리 아키텍처**: 해당 없음.
- **오픈소스 구현체**: 본 레포 + ggml 런타임.

> [!warning] 🟡 좋아요 수 불일치
> 수집기 11-21 622 → 볼트 11-22 574. 다운로드는 늘었는데 좋아요가 48 줄었다. 좋아요 취소가 하루에 48건 생기는 것은 흔치 않아 수집기 판독 오류일 가능성이 있으나 볼트는 11-21 값을 재현할 수 없다 — 판정 보류.

## 관련 페이지
- [[latent-MoE]] · [[파라미터-다중표기]] · [[OmniVoice]] · [[pocket-tts]] · [[higgs-audio-v3-tts]] · [[VibeVoice]] · [[sherpa-onnx]] · [[벤치마크-이미지-봉인]] · [[local-llm]]

## 원본
- 출처: https://huggingface.co/Zyphra/ZONOS3-Mini
- 확인 범위: HF models API · 카드 README 원문(8,699B · Korean 2행 · WER 2행 · Apache) · 🔴 arXiv 2611.16525 · 블로그 미열람 · 음성 청취 0
- 신뢰도: ⭐⭐⭐
