---
title: CineMobile — 온디바이스 이미지→영상 시네마틱 카메라 무빙
type: source
domain: video-saas
tags: [video-saas, on-device, image-to-video, diffusion, mobile, quantization, distillation, huggingface-paper]
created: 2026-07-12
updated: 2026-07-12
sources: []
reliability: medium
---

# CineMobile: On-Device Image-to-Video Diffusion for Cinematic Camera Motion (HF ↑12)

> [!insight] 핵심 인사이트
> **이미지→영상 확산(DiT)을 모바일에서 직접 구동**하는 압축 파이프라인 — 시네마틱 카메라 무빙(불릿타임·달리줌·슬로모)을 온디바이스로 생성한다. 큰 파라미터와 다단계 디노이징이 모바일 배포의 벽인데, CineMobile은 3종 최적화로 **생성 40× 가속·모델 1GB 미만**을 달성: ①**구조적 깊이 프루닝**(PPCL 변형, hidden dim 유지로 시간표현·인물 디테일 보존), ②**스텝 증류**(SFT→적대적 증류로 4-step 생성기 + RL 보정), ③**하이브리드 양자화**(FFN 4bit·나머지 8bit). 결과는 49프레임 480p를 **H200 0.6s/step·MediaTek Dimensity 8400 20s**, VBench 교사 대비 0.92점 이내. [[Higgsfield]]류 클라우드 카메라무빙을 *엣지로 내리는* 방향.

**HF 논문**: https://huggingface.co/papers/2607.03803 (업보트 ↑12)
**신뢰도**: ⭐⭐⭐ (초록 검증, 자체발표 벤치)

## 도메인별 추출 (video-saas)

- **기능 벤치마킹**: 온디바이스 i2v는 내 SaaS에 "클라우드 비용 없는 카메라무빙 프리셋"을 줄 여지. 난이도 높음(프루닝+증류+양자화 3단 스택 필요), 필요 스택은 DiT 압축 파이프라인.
- **크리에이터 인사이트**: 사용자는 "불릿타임/달리줌 같은 시네마틱 무빙"을 원하지만 클라우드 대기·비용이 갭. 온디바이스 4-step은 그 갭을 지연·비용 양면에서 좁힘.
- **프롬프트 패턴**: 3종 카메라 이펙트(bullet time·dolly zoom·slow motion)를 명시적 조건으로 제어 — 프리셋화하기 좋은 구조.
- **워크플로우**: 이미지 1장 → 온디바이스 4-step 확산 → 49프레임 480p 시네마틱 클립. 모바일 로컬 완결.
- **디자인 레퍼런스**: 카메라 무빙을 "이펙트 프리셋"으로 노출하는 UX는 [[Higgsfield]] 벤치마킹과 겹침.
- **경쟁 우위 빈틈**: 클라우드 i2v 대비 "오프라인·무과금·저지연" 차별화. 단 480p·49프레임 한계.

> [!warning] 검증 범위
> HF 논문 초록만 검증(reliability: medium). arXiv ID 2607.03803은 미래형이라 원문·코드·가중치 및 벤치 독립검증 불가. 40× 가속·VBench 수치는 저자 발표 기준.

## 관련 페이지
- [[Higgsfield]] — 클라우드 시네마틱 카메라무빙 (엣지 대조)
- [[AI-영상-생성-2026]] — 영상 생성 지형도
- [[Vidu-S1]] — 실시간 인터랙티브 비디오 생성(소비자 GPU)
- [[Seedance]] — VFX 특화 영상 AI
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2607.03803 (↑12)
- 방법: 구조적 깊이 프루닝 + 4-step 스텝 증류(+RL) + 하이브리드 양자화(FFN 4bit/8bit), 1.2B·<1GB
- 성능: 49프레임 480p, H200 0.6s/step·Dimensity 8400 20s, VBench 교사 대비 0.92점 이내
- 신뢰도: ⭐⭐⭐ (초록 검증, 자체발표 벤치 — 원문/코드 미검증)
