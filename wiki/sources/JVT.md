---
title: "JVT (Just Video Transformer) — 오토인코더 없이 큰 패치 DiT 하나로 픽셀 공간 영상 확산"
type: source
domain: video-saas
tags: [video-saas, video-diffusion, dit, pixel-space, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.18549]
reliability: medium
---

**논문**: arXiv 2611.18549 · 업보트 13 · 코드 [ZhouTimeMachine/JVT](https://github.com/ZhouTimeMachine/JVT) ★4.

## 핵심 인사이트
> [!insight] VAE 를 빼면 "픽셀 정렬 모달리티"를 공짜로 같이 생성한다
> 사전학습 오토인코더 · 디테일러 · 캐스케이드 · U-Net 스킵 없이 **16×16 큰 패치 DiT** 하나로 픽셀 공간 영상 확산. 패치 임베딩 · 레지스터 토큰 · AdaLN 을 체계 비교. 픽셀 공간이라 **RGB + 디스패리티**를 동시 생성 → 카메라 조건 생성에서 카메라 추종 향상 + 추론 시 별도 복원 모델 없이 장면 기하 획득 → [[3DGS]] · 기하 쪽과 연결.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹 (본문 표 1 · 256² · FVD@2048, 수집기 판독)**: 클래스 조건 UCF-101 **136.5** vs Latte 477.97 · 무조건 FaceForensics 32.86 · SkyTimelapse 46.58 · Taichi-HD 119.1.
- **경쟁 우위 빈틈**: 상용 영상 생성 대비 해상도(256²) · 규모가 연구 단계.

> [!warning] 초록 "competitive" vs 본문 "능가" — 부록이 반박 (수집기 판독)
> 초록은 *"competitive with latent diffusion baselines"*(볼트 확인)로 절제했는데, 본문 표 1 의 우위는 표 범위 한정: 부록에서 Latte+IMG(FF 27.08 · Sky 42.67 · Taichi 97.1) · FrameDiT+IMG(16.6 · 39.5 · 95.5)가 JVT 보다 낫고, UCF-101 에서도 ACDiT-XL 111 · FAR-XL 108 이 136.5 보다 낮다 → [[표-부분인용]] · [[한정어-탈락]](본문이 초록보다 강하게 말하는 역방향).

## 관련 페이지
- [[AI-영상-생성-2026]] · [[3DGS]] · [[표-부분인용]] · [[한정어-탈락]] · [[VibePrevisBench]](같은 날 · 기하 조건 영상)

## 원본
- 출처: https://huggingface.co/papers/2611.18549
- 확인 범위: HF papers API 초록 전문(볼트) · 🔴 본문 · 부록 표 수치는 수집기 판독
- 신뢰도: ⭐⭐
