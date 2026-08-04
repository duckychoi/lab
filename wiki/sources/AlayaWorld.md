---
title: AlayaWorld — 장시간·플레이 가능한 비디오 월드 생성
type: source
domain: ai-news
tags: [ai-news, world-model, video-generation, interactive, long-horizon]
created: 2026-07-08
updated: 2026-07-22
sources: []
reliability: medium
---

# AlayaWorld: Long-Horizon and Playable Video World Generation

**HuggingFace Papers**: https://huggingface.co/papers/2607.06291 (v1, 2026-07-08) · https://huggingface.co/papers/2607.18367 (후속판, 2026-07-22)
**업보트**: 49 (v1, 데일리 1위 2026-07-08) → **556 (후속판, 데일리 1위 2026-07-22)**

> [!update] 2026-07-22 갱신 — 후속 논문(2607.18367 "Interactive Long-Horizon World Modeling") 초록 실검증, reliability low→medium
> HF 데일리 1위 재등판(**↑556**)한 후속판을 **초록 WebFetch로 실확인** — 07-08 "원문 미검증 low"에서 구체 스펙 확보로 상향. **15B 비디오 확산 트랜스포머**(LTX-2.3 백본, 원본 22B 멀티모달에서 오디오 모듈 제거), 텍스트/이미지/영상 입력에서 **540p·720p 24fps 자기회귀 청크 생성(4스텝, ~1초/청크)**. 4대 능력(카메라 상호작용·지속 시공 일관성·안정적 장기생성·빠른 응답)을 **①시간 메모리(6프레임 슬라이딩 히스토리 압축) ②공간 메모리(깊이+카메라포즈 지오메트리 정렬 캐시, 최대커버리지 검색·오클루전 처리) ③sink frame(전역 정체성 앵커) ④안티드리프트 학습(Helios 드리프트 시뮬+에러뱅크 리플레이)** 로 구현. **iWorld-Bench**: 궤적정확도 0.7985·모션평활 0.9924·밝기일관 0.9492·메모리대칭 0.8871 등 대부분 지표 1위(480p 평가). **같은 팀의 실시간 렌더러 → [[Generative-World-Renderer]](AlayaRenderer-Flash)** 와 짝을 이룸(생성 vs 렌더). reliability low→**medium**(초록 검증, 원문·가중치·재현 미검증).

> [!insight] 핵심 인사이트
> **장시간(long-horizon)·상호작용(playable) 가능한 비디오 월드 생성** 모델. 단발 클립이 아니라 사용자가 개입할 수 있는 **긴 시퀀스 영상을 일관성 있게 생성**하는 것을 목표. [[WorldDirector]](지속 메모리 월드 시뮬)의 계보를 잇는 "월드 모델 as 게임 엔진" 흐름 — 영상 생성이 "예쁜 클립"에서 "탐험 가능한 세계"로 이동하는 신호. [[video-saas]] 관점에서는 인터랙티브 콘텐츠·게임 프리비주얼라이제이션의 잠재 입력.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐ (HF 데일리 1위 ↑49 / 원문 미검증 — arXiv 2607.06291 미래형 ID)
- **즉시 활용**: NO — 연구 단계. 코드/가중치 공개 여부·실행 요건 미확인.
- **6개월 영향력**: 월드 모델이 "긴 시간축 + 플레이 가능"으로 성숙하면 인터랙티브 영상·게임 생성 시장 개화. 단 계산 비용·일관성 유지가 관건.
- **대체 관계**: 기존 단발 T2V(텍스트→비디오)를 "지속 가능한 세계"로 확장. Genie 계열 플레이어블 월드모델 흐름.
- **허와 실**: "playable/long-horizon"은 데모 조건에서만 성립할 가능성. 실제 상호작용 지연·드리프트는 미검증.
- **액션**: 코드·데모 공개 시 [[WorldDirector]]와 지속성·상호작용 품질 대조 관찰. 현재는 트렌드 기록만.

## 관련 페이지
- [[Generative-World-Renderer]] — 같은 팀 실시간 렌더러(AlayaRenderer-Flash), 생성↔렌더 짝
- [[WorldDirector]] — 지속 메모리 월드 시뮬 (직접 계보)
- [[월드모델]]
- [[video-saas]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.06291 (v1) · https://huggingface.co/papers/2607.18367 (후속판, 초록 WebFetch 실검증)
- HF 업보트: 49(v1, 2026-07-08) → 556(후속판, 2026-07-22, 데일리 1위)
- 스펙(후속판): 15B 비디오 DiT(LTX-2.3 백본), 540p/720p 24fps 4스텝 자기회귀, 시간/공간 메모리+sink frame+안티드리프트, iWorld-Bench 궤적정확도 0.7985
- 신뢰도: ⭐⭐⭐ (후속판 초록 검증 / 원문·가중치·재현 미검증)
