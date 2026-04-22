---
title: TixiaoShan/LIO-SAM — 라이다-IMU 긴밀 결합 SLAM 프레임워크
type: source
domain: slam-3dgs
tags: [slam, lidar, imu, 3d-mapping, real-time, robotics, ros, localization, outdoor]
created: 2026-04-12
updated: 2026-04-12
sources: []
reliability: high
---

# TixiaoShan/LIO-SAM

> [!insight] 핵심 인사이트
> 라이다(LiDAR)와 IMU를 긴밀 결합(tightly-coupled)한 실시간 3D 지도 생성·위치추정 SLAM 시스템. ⭐4,676. ROS 기반, 실외 대규모 환경에서 검증. 현재 슬램 도메인의 핵심 레퍼런스 레포 중 하나.

## 핵심 인사이트

> [!action] 당장 할 것
> slam-3dgs 도메인 파이프라인 설계 시 LIO-SAM을 기준 SLAM 구현체로 참조. ROS 환경 구성 및 Velodyne LiDAR 데이터로 재현 실험 검토.

> [!note] 배경 정보
> Tixiao Shan (MIT → Nvidia)의 연구. LIO-SAM은 LeGO-LOAM의 후속작으로 IMU preintegration 추가. 루프 클로징, GPS 통합 지원. KITTI·MulRan 등 공개 데이터셋 검증 완료. Livox LiDAR도 지원.

> [!note] SLAM 도메인 현황 연결
> 기존 wiki slam-3dgs 도메인 소스 없던 상태 → LIO-SAM이 첫 SLAM 핵심 소스. 향후 3DGS(Gaussian Splatting)와 SLAM 결합 파이프라인 탐색 시 기준점.

## 도메인별 추출 (slam-3dgs 템플릿)

- **현재 SOTA**: LiDAR SLAM 실용 구현체 중 최다 인용·사용. KISS-ICP, FastLIO2와 함께 3대 실용 SLAM
- **실시간 가능성**: YES — 30Hz LiDAR 입력 실시간 처리 가능 (ROS 환경)
- **카메라 파이프라인**: LiDAR 포인트 클라우드 + IMU 입력. 카메라 없이 동작. Visual-SLAM과 별개 트랙
- **응용 가능성**: 드론·자율주행·로봇 네비게이션. 3DGS 입력용 정밀 포즈 추정에 활용 가능
- **필수 레퍼런스**: 원 논문 "LIO-SAM: Tightly-coupled Lidar Inertial Odometry via Smoothing and Mapping" (IROS 2020)

## 관련 페이지

- [[slam-3dgs]] — 도메인 허브 페이지
- [[anomalib]] — 로봇 비전 파이프라인 이상 탐지 레이어

## 원본

- 출처: https://github.com/TixiaoShan/LIO-SAM
- 스타: 4,676 (2026-04-12 기준)
- 논문: IROS 2020
- 신뢰도: ⭐⭐⭐⭐
