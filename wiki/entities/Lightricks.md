---
title: Lightricks
type: entity
domain: video-saas
tags: [기업, HuggingFace, 영상생성, 오디오생성, gated, 이스라엘]
created: 2026-09-29
updated: 2026-09-29
sources: [LTX-2.5.md, LTX-2.md]
reliability: medium
---

# Lightricks

> [!note] 정체
> [[LTX-2.5]]·[[LTX-2]] 영상/오디오 생성 모델을 배포하는 **HuggingFace 조직 계정**. arXiv 2601.03233 의 저자 **29인** 규모로 보아 **개인이 아닌 연구팀을 갖춘 조직**이다(제1저자 Yoav HaCohen).

## 볼트가 아는 것

- [[LTX-2.5]] — `Lightricks/LTX-2.5` · **DL 1,595,377**(30일 · 볼트 실측 2026-09-29) · ♥5,465 · **`gated: auto`** · license **`other`** · created 2026-07-23
- [[LTX-2]] — 논문 **arXiv 2601.03233** *"LTX-2: Efficient Joint Audio-Visual Foundation Model"*(2026-01-06 · 저자 29인) · **영상 14B + 오디오 5B 비대칭 듀얼 스트림**
- 제품 포지션: **오디오까지 같은 모델이 생성**하는 통합 영상 모델. *"state-of-the-art ... among open-source systems"*(자기보고)

## 🎯 볼트가 주목하는 것 — **공개 태도가 엇갈린다**

| 채널 | 개방도 |
|---|---|
| 논문(arXiv) | ✅ **완전 공개** — 구조·설계의도·한계까지 초록에 명시 |
| 모델카드(HF) | 🔴 **`gated: auto`** — 볼트 3회 연속 401(08-25 · 08-31 · 09-29) |
| 라이선스 | 🟡 **`other`** — Apache/MIT 아님, 상업적 사용 조건 미확인 |

🔴 **논문 마지막 문장은 *"All model weights and code are publicly released"* 다.** 게이트·비표준 라이선스와 긴장 관계에 있다.
📌 **단정하지 않는다** — 논문은 **LTX-2**, 게이트는 **LTX-2.5** 에 걸려 있다(6.5개월 차이의 다른 버전). `gated: auto` 는 거절이 아니라 자동 승인 절차일 수 있다. **`Lightricks/LTX-2` 저장소의 `gated` 값 조회로 검정 가능**하다.

🎯 **볼트 실무 결론**: 이 조직의 **스펙 정보는 HF 가 아니라 arXiv 에서 온다.** 카드가 막혀도 논문 경로가 열려 있다 → [[벤치마크-이미지-봉인]](채널 봉인) · [[무응답-오귀속]].

> [!warning] ⬜ 볼트가 확인하지 않은 것
> **조직의 다른 모델·회사 정보·소속 국가·상업 제품 라인을 조회하지 않았다.** 모델카드 전문을 **한 번도 읽지 못했다**(35일째). LTX-2 저장소의 게이트 여부 미확인.

## 관련 페이지
- [[LTX-2.5]] · [[LTX-2]] · [[벤치마크-이미지-봉인]] · [[무응답-오귀속]] · [[한정어-탈락]]
- [[YuE2]] — 오디오 생성 통합 계열(학계) · [[debpalash]] — 분리형 로컬 대비축 · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/Lightricks · 논문 https://arxiv.org/abs/2601.03233
- 볼트 실측: HF API `models/Lightricks/LTX-2.5` + README 401(126B) + arXiv API (2026-09-29 09:08~09:09 UTC)
- 신뢰도: ⭐⭐⭐ (모델 메타·논문 서지 실검증 · 조직 정보 자체는 미조회)
