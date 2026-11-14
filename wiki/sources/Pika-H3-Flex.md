---
title: "Pika-Labs/Pika-H3-Flex — MiniMax-H3 기반 6스텝 영상+오디오 LoRA 어댑터 (🔴 LICENSE 가 H3 원본과 동일 = 한국 제외)"
type: source
domain: video-saas
tags: [video-saas, video-generation, audio-video, lora, minimax-h3, pika, license, 한국]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/Pika-Labs/Pika-H3-Flex]
reliability: medium
---

**모델**: [Pika-Labs/Pika-H3-Flex](https://huggingface.co/Pika-Labs/Pika-H3-Flex) · dl30 **147,955**(= 누적) · likes 692 · license `minimax-h3-community-license-agreement` · base `MiniMaxAI/MiniMax-H3`(adapter) · safetensors 33,122,992,896(베이스 구성요소 포함) · created 2026-10-29 · modified 2026-11-07 · pipeline `image-to-video` (HF API 볼트 실측 — 수집기와 일치). 수집기 `ai-news` → 볼트 재분류 `video-saas`.

## 핵심 인사이트
> [!warning] 🔴 한국에서는 승인 전 사용 불가 — 수집기 요약에 없던 가장 중요한 사실
> 볼트가 레포의 `LICENSE`(17,604B)를 내려받아 [[MiniMax-H3]] 원본 LICENSE 와 대조했다: **바이트 단위로 동일**(sha256 앞 20자리 `59b99642b95ea21630e3` 일치). 10행: *"'Excluded Territories' means the European Union, the United Kingdom, **the Republic of Korea** and the United States of America."*
> 카드 315–321행도 "MiniMax H3 Community License Agreement" 를 명시하고, 번들된 H3 베이스 구성요소는 MiniMax 계약을 유지한다고 적는다. 그러나 **카드 본문에 지역 제외 언급은 없다**(`korea|territor|exclud` 검색 0건 — 라이선스 링크만 존재).
> → [[라이선스-지역-제외]] 4번째 파생 사례. [[hyperflow-h3-flash]](카드가 명시)와 [[Comfy-Org-MiniMax-H3-Image]](매출 조항만 인용) 사이 — "링크만 걸고 본문에서는 침묵"하는 유형이다. 볼트가 11-12 에 수집기에 요청한 "파생 모델은 base_model LICENSE 지역 조항 확인"이 이 건에서 이행되지 않았다.

> [!insight] 실체는 LoRA 두 개 + 정확한 6스텝 스케줄
> MiniMax-H3 를 후학습한 영상 + 동기 오디오 생성. FP32 LoRA(rank/alpha 128, 수집기 판독) 어댑터 2종:
> - **FL2VA** — 텍스트 · 첫/끝 프레임 조건(t2va / i2va / l2va / fl2va)
> - **Ref2VA** — 멀티모달 레퍼런스 최대 12개(이미지 9 · 영상 3 · 오디오 3 한도, 수집기 판독). 프롬프트에서 `@Image1` · `@Video1` 로 참조(카드 194행 예시).
>
> 로컬 출력(카드 251–261행): 480p/768p · 화면비 11종(21:9 ~ 9:21) · 24fps · 32kHz 스테레오 · 5초 요청 = 124프레임(약 5.17초) · 15초 = 362프레임. **1080p/2K/4K · 오디오 스템 · 프롬프트 향상은 유료 호스팅 API 전용**(227 · 279–287행).
> 카드 302행: *"Generic six-step Euler sampling is not equivalent"* — 매니페스트의 정확한 6스텝 스케줄을 써야 한다. 증류 모델을 일반 샘플러로 돌리면 품질이 깨진다는 실무 경고.

> [!warning] 품질 수치 0
> 카드 239행: *"These are creative showcases, not release-validation renders or throughput benchmarks. Exact reproduction with the released package is not guaranteed."* → [[자기제한-명시]]. H100 80GB 에서 480p/768p 대표 요청 통과(311행) — 소비자 GPU 근거 없음.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: "레퍼런스 12개(캐릭터 시트 + 환경 + 모션 영상 + 오디오)"는 캐릭터 일관성 워크플로의 입력 형식 기준. 내 SaaS 의 Element(캐릭터/장소/소품) 바인딩과 같은 발상.
- **크리에이터 인사이트**: 오픈 가중치는 480p/768p 초안까지, 고해상도는 API — "초안은 로컬, 마스터는 유료"라는 분업을 공급자가 제품화했다.
- **프롬프트 패턴**: `@Image1 is the character sheet … @Image2 is the environment. @Video1 is the motion reference only.`(카드 194–195행) — 레퍼런스의 **역할을 문장으로 한정**하는 형식. 샷 단위 타임코드(`SHOT 1 (0-2.5s): …`, 153행).
- **워크플로우**: draft(로컬 6스텝) → draft-to-video(API 업스케일).
- **경쟁 우위 빈틈**: 한국 사용자는 이 계열을 못 쓴다 — 지역 제외가 없는 오픈 i2v 기준 모델 선정이 여전히 미해결(11-12 actionable).

## 관련 페이지
- [[MiniMax-H3]] · [[MiniMax]] · [[라이선스-지역-제외]] · [[hyperflow-h3-flash]] · [[Comfy-Org-MiniMax-H3-Image]] · [[자기제한-명시]] · [[ComfyUI]] · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/Pika-Labs/Pika-H3-Flex
- 확인 범위: HF API 메타 · 파일 트리 · LICENSE 원문 내려받아 H3 원본과 cmp/sha256 대조 · 카드 raw(24,407B) 194 · 215–311 · 315–321행 판독 · 🔴 법률 해석 아님(조항 문언 기준) · 실행 미확인
- 신뢰도: ⭐⭐ (dl 14.8만 · 품질 수치 0 · 지역 제한)
