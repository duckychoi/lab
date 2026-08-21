---
title: WithEveryone — 그룹 이미지 생성의 계획·정체성 그라운딩 통합
type: source
domain: video-saas
tags: [ai-news, hf-paper, image-generation, group-image, identity-grounding, planning, video-saas]
created: 2026-08-21
updated: 2026-08-21
sources: []
reliability: medium
---

# WithEveryone — Unified Planning and Identity Grounding for Group Image Generation (HF 데일리 5위·업31)

**HF Papers**: https://huggingface.co/papers/2608.20336
**지표**: 업보트 **31** (HF 데일리 **5위**) · arxiv **2608.20336**(미래형 ID) · **도메인**: video-saas (교차 image-gen)

> [!insight] 핵심 인사이트
> **다인원(여러 사람) 그룹 이미지 생성에서 "계획 수립(planning)"과 "인물 정체성 그라운딩(identity grounding)"을 하나로 통합** — 여러 인물을 한 장면에 넣을 때 구도·배치를 계획하는 것과, 각 인물의 정체성(얼굴·특징)이 뭉개지지 않게 고정하는 것을 분리된 단계가 아니라 통합 파이프라인으로 다룬다. 단일 인물·객체 편집을 넘어 **"여러 정체성을 한 프레임에 일관되게"**가 생성형 이미지의 다음 난제임을 보여주는 항목으로, [[video-saas]]([[reat-scene]]) 다인물 씬·캐릭터 일관성 요구와 직결. 4D 인물 재구성 [[4DAnyone]](단안→개인 4D)과 함께 "**인물(정체성) 중심 생성·재구성**"이 이 배치의 비전 축을 이룸 — 전자는 재구성, 후자는 다인물 생성 계획.

> [!warning] 신뢰도 — 미래형 arxiv ID·원문 미검증 (medium)
> 업보트 31·데일리 5위는 raw 자동수집 신호이며 arxiv **2608.20336은 미래형 ID로 원문 초록·방법·수치 재현 불가**([[CLAUDE.md]] 사실확인 원칙). "계획·정체성 그라운딩 통합"의 **구체 아키텍처·정체성 보존율·인원 확장성·벤치·소속은 raw 미기재 → 원문 대조 전 미검증**. 제목·한줄요약 기반 medium(수치 인용 금지).

## 도메인별 추출 (video-saas · 교차 image-gen)

- **기능 벤치마킹**: 다인물 씬 생성 시 "구도 계획 + 각 인물 정체성 고정"을 통합 처리 — 내 [[video-saas]] 캐릭터 일관성 파이프라인의 참조 각도.
- **크리에이터 인사이트**: 여러 인물이 등장하는 컷에서 정체성 붕괴(얼굴 뒤섞임)가 실사용 갭 — 이를 계획 단계에서 잡으려는 접근.
- **프롬프트 패턴**: 미기재 — 통합 계획·그라운딩 프롬프트 구조는 원문 대조 전 미확정.
- **디자인 레퍼런스**: 다인물 배치·정체성 앵커링을 [[reat-scene]] 다캐릭터 씬 설계에 개념 참고.
- **경쟁 우위 빈틈**: 단일 정체성 편집은 성숙, **다인물 동시 정체성 일관성**은 아직 빈틈 — 차별화 포인트 후보.

## 관련 페이지
- [[4DAnyone]] — 단안 비디오 개인 4D 재구성(같은 배치 인물 중심 비전 축·재구성 쪽)
- [[video-saas]] — 영상 AI SaaS 도메인(다인물 씬 활용처)
- [[reat-scene]] — 씬·캐릭터 배치 설계(다캐릭터 일관성 접목)
- [[AI-3D-생성]] · [[ERNIE-Image]] — 이미지 생성·에셋 축
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2608.20336 (arxiv 2608.20336·미래형 ID)
- 지표: 업보트 31 (2026-08-21, HF 데일리 5위)
- 신뢰도: medium (미래형 arxiv ID·원문 미검증·아키텍처/정체성 보존율/소속 미기재·raw 자동수집)
- 수집: 2026-08-21 아침 자동수집 (HF 논문)
