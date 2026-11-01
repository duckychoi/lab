---
title: "Platonic Representation JEPA — 다음 토큰 예측은 정렬에 비효율적이라는 증명과 그 조건"
type: source
domain: ai-news
tags: [ai-news, jepa, representation-learning, prh]
created: 2026-11-01
updated: 2026-11-01
sources: [https://huggingface.co/papers/2610.39302]
reliability: medium
---

**HF**: published 2026-10-29 · upvote 58 · 저자 2(Randall Balestriero · Yann LeCun) · arXiv 2610.39302 · 코드 [galilai-group/prh-proof](https://github.com/galilai-group/prh-proof)

## 핵심 인사이트
> [!insight] 스케일이 아니라 양성 쌍의 설계가 정렬을 만든다
> 한 장면의 두 관측(good view)을 양성 쌍으로 쓰면 모달리티별로 따로 학습한 [[JEPA]]가 회전 하나 차이의 같은 표현을 학습한다는 정리다. 다음 토큰 예측은 한 문서의 조각을 쌍으로 쓰는 bad-view JEPA로 재해석된다. 언어 모델이 규모로만 비전과 정렬되는 이유를 설명한다.

> [!warning] 헤드라인 세 숫자의 조건 (수집기 요약에 없음)
> - **42배**: 21.6M 샘플(.109)과 900M 샘플(.111)의 비교인데, 저자는 **next-token의 더 이른 체크포인트를 재지 않았다**고 적었다. 같은 샘플 수 비교는 .108 대 .071, 토큰 기준은 14배다.
> - **.184 > Qwen2.5-72B .154**: 네 번째 시드는 **.121**로 72B보다 낮다. 그 뒤 첫 시드의 가중치로 고정했다. 4시드 평균 .168은 여전히 전 언어 모델 위다.
> - **"픽셀을 본 적 없다"**: 학습 텍스트 대부분을 쓴 리캡셔너가 CLIP ViT-L/14로 이미지를 본다. 저자 스스로 밝힌 단서다. WIT 캡션 1,024개 중 최소 43개가 학습 대체 텍스트에 포함되지만, 제거해도 변화는 .002 이하다.
> - **CIDEr .838은 쌍 없는 결과가 아니다**: 네트워크는 쌍 없이 학습했지만 선형 사상 하나를 Flickr **30k 쌍**으로 맞췄다. 쌍이 전혀 없는 결과는 ImageNet-100 top-5 64%(언어 모델 최대 8B 대비 최대 56%) 쪽이다.

## 도메인별 추출
- **신뢰도**: 정리와 증명 + 저자 측정 · 코드 공개 · 볼트 재현 없음.
- **즉시 활용**: NO(수억 건 텍스트 학습 전제). **6개월 영향력**: 크로스모달 임베딩을 만들 때 모델 크기보다 양성 쌍 설계를 먼저 볼 근거다.
- **대체 관계**: [[Sensorimotor-Alignment]]의 PRH 로봇 확장과 같은 축이다. 후자는 평가 지표, 이 논문은 이론과 학습법이다.
- **허와 실**: "1.09억 파라미터가 72B를 이긴다"는 **정렬 지표**에 한한 말이다. 언어 능력 비교가 아니다.

## 관련 페이지
- [[JEPA]] · [[월드모델]] · [[Sensorimotor-Alignment]] · [[JEPA-vs-Diffusion-월드모델]] · [[한정어-탈락]]

## 원본
- 출처: https://huggingface.co/papers/2610.39302
- 확인 범위: HF `api/papers` · arXiv HTML 본문(2026-11-01) · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐⭐ (코드 공개 · 저자가 단서 공개 · 볼트 재현 없음)
