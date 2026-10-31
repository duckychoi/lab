---
title: "Intrinsic Distribution Matching (IDM) — 외부 인코더 없는 소수 스텝 이미지 증류"
type: source
domain: video-saas
tags: [ai-news, video-saas, image-generation, distillation, dmd]
created: 2026-10-31
updated: 2026-10-31
sources: [https://huggingface.co/papers/2610.39633]
reliability: medium
---

**HF**: published 2026-10-29 · upvote 239 · 저자 10(Deyuan Liu 외) · arXiv 2610.39633

## 핵심 인사이트
> [!insight] 영어 쪽 우위는 0.32점이다
> 헤드라인 "2 NFE LongText-Bench 중국어 94.25% · 영어 90.20%, 비교군 최고"는 사실이지만, 차점 Z-Image-Turbo++ 대비 격차는 **중국어 +2.63 · 영어 +0.32점**이다(본문 Table 5). 초록의 "최고"만 보면 영어 렌더링도 크게 앞선 것처럼 읽힌다 → [[한정어-탈락]].

- **새로운 점**: DMD 보정은 그대로 두고 특징의 평균·좌표별 표준편차 제약을 더했다. 특징 추출기로 **생성기 자신의 EMA 복사본**을 쓴다.
- **외부 인코더 대체의 근거**: 같은 대조군에서 GenEval이 DINOv2 +0.29 · EMA +0.35, LongText-CN은 94.13 · 94.25로 비슷하다. DINOv2를 뗄 수 있다는 주장은 이 수치 범위에서 지지된다.
- **비용 범위**: Qwen-Image 20B, 2 NFE에서 APEX 대비 GenEval 0.91 vs 0.90 · FID 6.34 vs 6.44 · 지연 0.44 vs 0.45초. 품질 차이가 크지 않고 지연은 거의 같다.

## 도메인별 추출
- **기능 벤치마킹**: 텍스트가 들어간 이미지(자막 카드·썸네일)를 1~2스텝으로 뽑는 파이프라인 후보. 다만 직접 쓰려면 증류 학습을 돌리거나 체크포인트 공개 범위를 확인해야 한다(🔴 볼트 미확인).
- **즉시 활용**: NO — 코드 ★63 · 미실행. **액션**: star만.
- **허와 실**: LongText는 글자 렌더링 전용 벤치다. 일반 품질은 APEX와 박빙이므로 "텍스트가 필요한 경우"로 한정해 읽어야 한다.

## 관련 페이지
- [[Qwen]] · [[한정어-탈락]] · [[천장-기준선]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2610.39633 · 코드 https://github.com/inclusionAI/IDM (★63 · Apache-2.0 · 볼트 실측)
- 확인 범위: HF `api/papers` · arXiv HTML 본문 열람(2026-10-31) · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐ (저자 자기 측정 · 볼트 재현 없음)
