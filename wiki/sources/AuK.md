---
title: AuK — 음성 생성·편집 통합 파운데이션 모델 (Tencent)
type: source
domain: ai-news
tags: [ai-news, tts, speech, diffusion, tencent, 단위-불일치, no-numbers]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: medium
identifiers: [tencent/AuK, arXiv:2609.08936]
---

# AuK — 음성 생성·편집 통합 파운데이션 모델

**HF**: https://huggingface.co/tencent/AuK · `tencent/AuK`
**지표(2026-09-13 API 실호출)**: 다운로드 **1,202**(30일) · ♥**157** · **MIT** · `pipeline_tag: text-to-speech` · 논문 arXiv:2609.08936
**🔴 드리프트 2건 — 이 배치 최대**:
- **다운로드**: raw **907** vs API **1,202** → **+295(+32.5%)**. 이 배치 유일한 두 자릿수 % 드리프트
- **생성일**: raw *"2026-09-09 오픈소스"* vs API `createdAt` **2026-08-18** → **22일 차이**. `lastModified` 2026-09-10
> raw의 09-09는 **레포 생성일이 아니라 공개 공지일**로 보인다. 둘을 구분해 적어야 한다.

> [!insight] 핵심 인사이트 — **16개 태스크를 자연어 지시 하나로 통합한다**
> 제로샷/지시 TTS · 발화 **내용 편집** · 피치/속도/음량 편집 · 감정/음색/억양/비언어음/속삭임 변환 · 잡음제거 · 화자분리 · 음원분리를 **한 인터페이스**로 처리한다.
> ✅ **실카운트(카드 표)**: **5개 범주 16개 태스크** — 생성 2 · 내용편집 2 · 음향편집 3 · 준언어편집 5 · 향상분리 4. **합이 맞는다**(2+2+3+5+4=16).
> 🎯 음성 도메인은 보통 태스크마다 별도 모델을 쓴다. **"무엇을 할지"를 가중치가 아니라 지시문으로 옮긴 것**이 이 모델의 주장이다.

> [!warning] 🔴 **"1.5B"의 실제 실행 규모는 1.5B가 아니다**
> `config.yaml` 실조회 결과: `text_encoder_path: **ckpts/Qwen2.5-Omni-3B**`
> → **3B 텍스트 인코더가 하드 의존**이고 **별도 다운로드**다. 이 레포에 들어 있지 않다.
>
> **레포 파일 실측(HF API blobs)**:
> | 파일 | 바이트 |
> |---|---:|
> | `auk_base.safetensors` | 6,122,209,092 |
> | `vae.safetensors` | 637,322,604 |
> | `assets/performance.png` | 2,249,748 |
> | **총계** | **6,762,657,404 = 6.76 GB** |
>
> → **디스크 6.76GB + Qwen2.5-Omni-3B 별도.** 카드의 "1.5B"는 **확산 트랜스포머 본체만 센 값**이다. 실제 배치 규모는 그 몇 배다 → [[단위-불일치]]

> [!warning] 🔴 **카드에 수치 벤치마크가 없다 — 성능 인용 불가**
> `## Performance` 절의 내용은 **이미지 1장**(`assets/performance.png`, 2,249,748B)이 **전부**다. 표도 숫자도 텍스트도 없다.
> → **성능 수치를 인용할 수 없다.** 논문 arXiv:2609.08936 확인 필요.
> 📌 09-12 [[VibeVoice-ASR-Streaming-7B]] 에서 볼트가 기록한 *"Evaluation = 이미지 1장"* 패턴의 **재현**이다. 음성 도메인에서 반복해서 나타난다 → **벤더 무관 도메인 관행**으로 격상 검토.

> [!note] 아키텍처 실측 (`config.yaml` 전문 조회)
> - backbone **`Flux2Edit`** · cfm_class `CFMEdit` (확산/CFM 계열)
> - dim **1536** · heads **24** · ff_mult 2 · **num_layers 10 + num_single_layers 20**
> - VAE **`BigVGANFlowVAE`** · latent_dim 64 · downsample_rate 480 · **target_sample_rate 24000 (24kHz)**
> - ⚠️ 같은 배치 [[YuE]] 는 **48kHz** 출력이다. **AuK는 24kHz** — 음악용이 아니라 **음성용** 샘플레이트다. 용도가 다르다
> - ⚠️ 주석 *"gradient checkpointing: peak ~91G→~75G"* 는 **학습 VRAM**이지 추론이 아니다. **추론 VRAM 수치는 카드에 없다**
> - `attn_backend: flash_attn`, 주석에 *"CLI overrides to `torch` for inference (no flash_attn dep)"*

> [!warning] base 전용 레포다
> 이 레포는 **base 전용**. 4스텝 증류판 **`tencent/AuK-Flash` 는 별도 레포**(HTTP **200** 확인).
> → **속도 수치를 이 레포의 성질로 쓰면 안 된다.** 두 레포를 섞어 인용하는 것이 [[파생표기-함정]] 의 전형.

## 도메인별 추출 (ai-news)

- **신뢰도**: 다운로드 1,202 · MIT(cardData·License절 일치) · [[Tencent]] · 구조는 config로 전부 검증됨. **그러나 성능 수치 0개** → **medium**
- **즉시 활용**: ⚠️ **조건부.** 16개 태스크 통합은 매력적이나 ① 성능 미검증 ② Qwen2.5-Omni-3B 별도 확보 ③ 추론 VRAM 미기재. **PoC 전 실측 필수.**
- **6개월 영향력**: *"태스크별 모델 → 지시 기반 단일 모델"* 흐름이 음성에도 도달. 영상 SaaS의 음성 트랙 처리에 직접 해당.
- **대체 관계**: 편집 기능(내용 편집·준언어 변환)은 기존 TTS가 못 하던 축이라 **대체가 아니라 추가**다.
- **액션**: 논문 2609.08936에서 수치 확보 → 그 전까지 성능 주장 인용 금지.

> [!question] 미해결
> ① 추론 VRAM ② 24kHz 출력 품질이 실사용에 충분한가 ③ AuK-Flash와의 품질 격차. **셋 다 카드 밖.**

## 관련 페이지
- [[Tencent]] — 제작사. NOASSERTION 관행(09-12 [[WeKnora]])과 달리 **여기는 MIT가 cardData·본문 양쪽 일치**
- [[VibeVoice-ASR-Streaming-7B]] — *"Evaluation = 이미지 1장"* 패턴의 선례
- [[YuE]] — 같은 배치 오디오. **48kHz 음악 vs 24kHz 음성**
- [[단위-불일치]] · [[파생표기-함정]] · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/tencent/AuK
- 신뢰도: ⭐⭐ (HF API + blobs 파일 전수 실측 + `config.yaml` 전문 조회. **성능 근거 부재로 medium**)
