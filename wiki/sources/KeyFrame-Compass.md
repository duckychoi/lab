---
title: KeyFrame-Compass — Keyframe-Conditioned Video Generation 평가 벤치
type: source
domain: ai-news
tags: [ai-news, hf-paper, video-generation, benchmark, keyframe, evaluation, video-saas]
created: 2026-07-17
updated: 2026-07-17
sources: [2607.14202]
reliability: medium
---

# KeyFrame-Compass — Keyframe-Conditioned Video Gen 평가 (HF 2607.14202)

> [!insight] 핵심 인사이트
> **HF 데일리(upvote 28)**. **키프레임 조건부 비디오 생성(keyframe-conditioned video generation)의 종합 평가 벤치마크**. "키프레임 몇 장을 주고 그 사이를 채우게" 만드는 생성 방식이 실제로 키프레임을 얼마나 충실히 따르고 중간을 자연스럽게 잇는지를 표준 축으로 측정한다. 이는 내 영상 자동화([[reat-render]]·[[AI-영상-생성-2026]])에서 **"원하는 구도의 앵커 프레임을 지정하고 그 사이를 AI가 보간"하는 워크플로우의 평가 기준**을 제공 — 상용 툴(Higgsfield·Kling 등)이 내세우는 "캐릭터·구도 일관성"을 정량화하는 잣대. [[DomainShuttle]](주제 일관 T2V)·[[krea2-identity-edit]](정체성 유지)가 노리는 "일관성"의 측정 인프라 쪽 짝.

> [!warning] 신뢰도 medium — 원문 미검증
> 미래형 arXiv ID(2607.14202) 기반 자동수집으로 **초록·제목 수준만 확인**. 평가 지표·데이터셋 구성은 원문 확인 필요.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐ — HF upvote 28. 벤치 설계의 타당성·채택도는 미검증.
- **즉시 활용**: MAYBE — 키프레임→보간 방식의 영상 생성 도구를 고를 때 평가 관점으로 참고. reat-* 렌더 결과의 "구도 충실도" 자기점검 축으로 응용 여지.
- **6개월 영향력**: 키프레임 조건 생성이 "우연히 예쁜 결과"에서 "지정한 앵커를 지키는 통제 가능한 생성"으로 성숙하는 데 필요한 평가 표준. 크리에이터가 원하는 통제력의 척도.
- **대체 관계**: 자유 T2V 평가의 보완 — 키프레임 통제라는 실무 시나리오를 격리 측정. [[KeyFrame-Compass]]↔[[DomainShuttle]]/[[krea2-identity-edit]](일관성 생성)와 짝.
- **허와 실**: 벤치가 측정하는 "충실도"가 인간 지각과 어긋날 수 있음([[PerceptionRubrics]] 문제). 지표 정의를 원문에서 확인해야.
- **액션**: 원문 공개 시 평가 축을 정리해 [[AI-영상-생성-2026]]의 "통제 가능성" 섹션에 반영.

## 관련 페이지
- [[AI-영상-생성-2026]]
- [[reat-render]]
- [[DomainShuttle]]
- [[krea2-identity-edit]]
- [[PerceptionRubrics]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.14202
- HF 데일리 upvote 28 (2026-07-17)
- 신뢰도: ⭐⭐ (미래형 ID·초록 수준 자동수집, 원문 미검증)
