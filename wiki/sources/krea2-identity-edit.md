---
title: conradlocke/krea2-identity-edit — 정체성 유지 이미지 편집 모델
type: source
domain: video-saas
tags: [video-saas, hf-model, image-edit, identity-preservation, face-consistency, krea]
created: 2026-07-14
updated: 2026-07-14
sources: []
reliability: medium
---

# HF모델: conradlocke/krea2-identity-edit (DL 268)

**HuggingFace**: https://huggingface.co/conradlocke/krea2-identity-edit
**다운로드**: 268 (2026-07-14 기준) · **베이스**: Krea2 · **도메인**: video-saas

> [!insight] 핵심 인사이트
> **인물의 정체성(identity)을 유지하면서 이미지를 편집하는 모델 — Krea2 기반 얼굴 일관성 편집.** 배경·의상·포즈·스타일을 바꿔도 **같은 사람으로 보이게** 얼굴 특징을 보존하는 게 목표로, [[AI-3D-생성]]·캐릭터 파이프라인에서 늘 문제였던 "편집하면 사람이 딴 사람 됨"을 정면으로 다룬다. [[video-saas]] 관점에서 **일관된 캐릭터로 여러 컷/씬을 생성**하는 워크플로우(캐릭터+씬+샷 통합, [[Higgsfield]] 계열이 지향)의 부품 후보 — 정체성 고정은 숏폼·시리즈물에서 결정적. 다운로드는 초기(268)지만 문제 정의가 실전적.

> [!warning] 검증 상태
> DL 268의 초기 커뮤니티 모델. 정체성 보존 강도·해상도·라이선스·Krea2 파생 여부는 카드 정밀검증 보류. reliability: medium.

## 도메인별 추출 (video-saas)

- **신뢰도**: ⭐⭐⭐ (HF DL 268, 자동수집·초기 채택)
- **기능 벤치마킹**: 캐릭터 정체성 고정 편집 → 내 SaaS의 "동일 인물 다중 씬" 기능에 직결. 난이도 중(HF 모델 로드+파이프라인 통합).
- **크리에이터 인사이트**: 사용자는 "같은 캐릭터로 시리즈"를 원하는데 대부분 툴이 컷마다 얼굴이 흔들림 — 이 갭을 겨냥.
- **워크플로우**: 원본 얼굴 → 편집 지시(배경/의상/포즈) → 정체성 유지 출력. i2v/캐릭터 시트와 연결.
- **경쟁 우위 빈틈**: 정체성 일관성은 여전히 미해결 영역 — 안정적이면 차별화 포인트.

## 관련 페이지
- [[Higgsfield]] — 캐릭터+씬+샷 통합 파이프라인(정체성 일관성이 관건)
- [[AI-3D-생성]] — 캐릭터/이미지 생성 워크플로우
- [[AI-영상-생성-2026]] — 영상 생성 지형도
- [[video-saas]] — 영상 AI SaaS 도메인

## 원본
- 출처: https://huggingface.co/conradlocke/krea2-identity-edit
- 신뢰도: ⭐⭐⭐ (HF DL 268, 자동수집)
