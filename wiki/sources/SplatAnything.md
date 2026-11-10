---
title: "SplatAnything (GSNorm) — feed-forward 3DGS 의 스케일 흔들림을 '가우시안 간격 정규화'로 잡는다. 초록에 정량 수치 없음"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-paper, 3dgs, feed-forward, zju3dv, normalization]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/papers/2611.08264]
reliability: medium
---

**논문**: [2611.08264](https://huggingface.co/papers/2611.08264) · Zhejiang University(zju3dv) · 업보트 **65** · 코드 [zju3dv/SplatAnything](https://github.com/zju3dv/SplatAnything) ★123(수집 시 116) · **레포 생성 2026-11-08** · license 필드 NOASSERTION

## 핵심 인사이트
> [!insight] 정규화 기준을 "장면 반경"에서 "이웃 간격"으로 바꾼다
> 기존 feed-forward 3DGS 는 재구성 기하의 전역 반경 통계로 정규화한 공간에서 가우시안 속성을 예측한다. 그런데 이웃 가우시안 중심 간 **간격**은 장면 스케일·카메라 배치에 따라 여전히 크게 달라 가우시안 크기 타깃이 체계적으로 어긋난다(모호한 감독). **GSNorm** 은 장면 수준 간격의 강건 통계로 정규화한다. 데이터셋 · 입력 희소도 · 외삽 시점을 아우르는 벤치마크도 함께 낸다.

> [!warning] 수치 0 — "SOTA"는 초록의 문장뿐이다
> 초록 전문(볼트 papers API 확인)에 정량 수치가 없다. *"particularly strong gains under substantial variations in scene scale and viewpoint"* 는 격차 미제시. 벤치마크도 저자가 새로 만든 것이라 기존 표와 직접 비교되는지 본문 확인이 필요하다. 레포는 생성 이틀째 — 가중치 공개 여부 볼트 미확인.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 주장만 있음(수치 본문).
- **실시간 가능성**: feed-forward(장면별 최적화 없음) 계열이라 구조상 빠르나 FPS 수치 없음.
- **카메라 파이프라인**: 희소 다시점 입력 → 가우시안 직접 예측. 포즈 요구 조건은 초록에 없음.
- **응용 가능성**: 스케일이 제각각인 사용자 촬영 영상에서 [[3DGS]] 를 뽑을 때 실패 원인 후보를 하나 더 준다.
- **필수 레퍼런스**: [[GlobalSplat]] 과 같은 "범용 feed-forward" 축.

## 관련 페이지
- [[3DGS]] · [[GlobalSplat]] · [[EDGAR]] · [[Open-HumanScale]]

## 원본
- 출처: https://huggingface.co/papers/2611.08264
- 확인 범위: HF papers API 초록 전문 · GitHub API 메타 · 🔴 본문 · README · 코드 미열람
- 신뢰도: ⭐⭐ (업보트 65 · ★123 · 수치 미제시)
