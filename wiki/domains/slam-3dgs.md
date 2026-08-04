---
title: 로봇 SLAM / 3DGS / 카메라 누적 인사이트
type: domain
domain: slam-3dgs
tags: [slam, 3dgs, gaussian-splatting, camera, robotics, nerf]
created: 2026-04-09
updated: 2026-04-09
sources: []
---

# 로봇 SLAM / 3DGS / 카메라 누적 인사이트

목표: SLAM 기술 이해 + 3DGS 렌더링 + 카메라 파이프라인

---

## 현재 SOTA 및 오픈소스 구현체
_소스 ingest 시 자동 누적_

## 실시간 동작 가능 조건
_소스 ingest 시 자동 누적_

## 카메라 파이프라인 구조
_소스 ingest 시 자동 누적_

## 응용 가능한 것
_소스 ingest 시 자동 누적_

## 반드시 읽어야 할 논문/레포
_소스 ingest 시 자동 누적_

## 관련 페이지

---

## 월드모델 × 엣지 로보틱스 (2026-07-12 synthesis)
> [!insight] slam-3dgs ↔ world-model 접점
> [[JEPA효율화-로컬추론]]에서 도출 — **SLAM/3DGS = "지금 어디에 무엇이 있나"(명시적 기하·현재)**, **[[월드모델]] = "다음에 무엇이 일어날까"(암묵적 예측·미래)**. 엣지 로봇(Jetson)엔 둘 다 필요하며 같은 하드웨어 예산 안에서 경쟁·협력.
> - 가능한 합성: 3DGS를 [[월드모델]]의 렌더러/타깃으로, 또는 [[JEPA]] 월드모델을 SLAM의 예측 사전(prior)으로.
> - 연결: [[임바디드-AI]] · [[Embodied-cpp]](온디바이스 런타임) · [[RoboDojo]](sim-and-real 평가) · [[JEPA]] · [[Mamba4]](선형 롤아웃)
