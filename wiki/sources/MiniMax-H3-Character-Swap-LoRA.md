---
title: "akatz-ai/MiniMax-H3-Character-Swap-LoRA — 영상 속 인물을 참조 캐릭터로 교체하는 H3 LoRA (🔴 한국 제외 라이선스)"
type: source
domain: video-saas
tags: [video-saas, minimax, lora, character-swap, license, huggingface]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA]
reliability: low
---

**모델**: [akatz-ai/MiniMax-H3-Character-Swap-LoRA](https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA) · 다운로드 **139,046**(볼트 11-16 · 수집기 141,476 — 30일 창 감소, [[지표-창길이]]) · 좋아요 989 · license `other` · base `Comfy-Org/MiniMax-H3` · 생성 2026-09-25 · 데이터셋 akatz-ai/H3-Character-Swap-v1.

## 핵심 인사이트
> [!insight] 포즈·시선·표정·움직임은 소스, 정체성은 참조 이미지
> Ref2VA 용 어댑터. 권장 V1.5(`h3_character_swap_v1.5.safetensors`, V1 에서 1,000 업데이트 추가 학습), 강도 1.0. 단독 모델이 아니라 Ref2VA INT8 베이스 + 텍스트 인코더 · VAE + 별도 Turbo 8-step LoRA 필요(검증 레시피: 8스텝 · CFG 1 · `er_sde`). 학습 설정 · 해시는 `training/v1.5/run-summary.json` 공개.

> [!warning] 🔴 라이선스 — 한국 사용 불가 (볼트 확인)
> 레포 LICENSE(17,604B)가 [[MiniMax-H3]] 원본 · [[Pika-H3-Flex]] 와 **바이트 동일**(sha256 앞 20자 `59b99642b95ea21630e3` · `cmp` 일치). 10행 *"Excluded Territories" = EU · 영국 · 대한민국 · 미국*, 42행 적용 지역 밖에서 사용 · 복제 · 수정 · 배포 · **출력물 표시** 불가. 수집기가 11-12 요청(파생 모델 base LICENSE 지역 조항)을 이번엔 **이행**해 요약에 명시했다. → [[라이선스-지역-제외]] 파생 5번째.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 캐릭터 교체 = 영상 SaaS 의 고수요 기능. 구현은 베이스 + LoRA 2종 조합으로 공개돼 있어 기술 난이도는 낮지만 **라이선스 때문에 한국 서비스에 쓸 수 없다**.
- **크리에이터 인사이트**: 카드가 스스로 "선별 사례이지 집계 벤치마크가 아니다", "실험적 · 정체성 · 타이밍 · 표정 · 가림 · 컷에서 드리프트 가능", "원본 사운드트랙 유지는 앱 기능이지 립싱크 정확도 근거가 아니다"라고 한정 → [[자기제한-명시]].
- **경쟁 우위 빈틈**: 같은 기능을 지역 제한 없는 베이스(Wan 계열 등)로 재현하는 쪽이 한국 사용자에겐 유일한 경로.
- **액션**: [[MiniMax-H3]] 계열 보류 목록에 추가.

## 관련 페이지
- [[MiniMax-H3]] · [[MiniMax]] · [[Pika-H3-Flex]] · [[Comfy-Org]] · [[Minimax-h3-Turbo-lightx2v]] · [[라이선스-지역-제외]] · [[자기제한-명시]] · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/akatz-ai/MiniMax-H3-Character-Swap-LoRA
- 확인 범위: HF models API 메타 · LICENSE 원문 grep + 11-14 보관 원본과 `cmp`/sha256(볼트) · 🔴 학습 설정 · 레시피 · 카드 한정 문구는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐ low (정량 0 · 한국 사용 불가)
