---
title: 3DGS — 3D 가우시안 스플래팅 (3D Gaussian Splatting)
type: concept
domain: slam-3dgs
tags: [slam-3dgs, 3dgs, gaussian-splatting, concept]
created: 2026-11-09
updated: 2026-11-09
sources: [EDGAR.md, idol.md, ME-World.md, OuroWorld.md, WorldSculpt.md, Introduction-to-Autonomous-Robots.md]
reliability: medium
---

# 3DGS — 3D 가우시안 스플래팅

장면을 수많은 3D 가우시안(위치·공분산·색·불투명도)으로 표현하고 래스터화로 실시간 렌더하는 표현 방식. NeRF 대비 렌더 속도가 압도적이라 아바타·SLAM·월드모델 출력 포맷으로 확산 중.

> [!insight] 볼트에서 반복되는 패턴: "무거운 생성/보정은 한 번, 결과는 가우시안에 굽는다"
> [[EDGAR]](디퓨전 보정 → 아바타 재최적화, 추론 시 디퓨전 0회) · [[idol]](단일 이미지 → 최대 104만 가우시안 .ply). 생성 모델은 오프라인 교사, 3DGS 는 실시간 배포 포맷이라는 분업.

> [!note] 2026-11-09 신설 — `[[3DGS]]` 링크가 6개 소스에 쌓였는데 페이지가 없었다(스키마: 3개+ 소스 등장 시 개념 페이지 필수). 이전 표기 [[가우시안 스플래팅]] · [[Gaussian-Splatting]] · [[3DGS-SLAM]] 도 이 개념을 가리킨다.

## 관련 소스
- [[EDGAR]] · [[idol]] · [[ME-World]] · [[OuroWorld]] · [[WorldSculpt]] · [[Introduction-to-Autonomous-Robots]]
- [[월드모델]] · [[slam-3dgs]]
