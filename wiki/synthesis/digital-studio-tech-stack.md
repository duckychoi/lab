---
title: "디지털 스튜디오 테크스택 — 파이프라인 단계별 SOTA/오픈소스 (2026-11)"
created: 2026-11-23
author: fryday
tags: [synthesis, tech-stack, tooling, digital-studio, data-engine, sota, 2026]
parent: 43
purpose: 전방향 조명·카메라뷰 디지털 스튜디오(실내·실외) 구축/고도화에 쓰는 모델·오픈소스를 단계별로 모으고, 우리 연구번호(#43~#62)와 필터 루프 위치에 매핑
note: 빠르게 변하는 분야 — 각 항목은 "최신 태그/라이선스 직접 확인" 전제. 날짜 2026-11-23 스냅샷.
---

# 디지털 스튜디오 테크스택 (2026-11 스냅샷)

> 설계 원칙: **기하(geometry)는 정확한 3D 재구성·depth로, 외관·시점은 생성(Qwen/비디오/리라이팅)으로, 둘을 #42/#43 필터 루프로 보정.** 생성뷰는 기하 부정확 → 반드시 실측·교차일관성으로 교정(garbage-in 차단).

## 파이프라인 위치 ↔ 필터 루프
- **예측(prediction)** = 합성 생성: 렌더러/시뮬·생성모델·리라이팅·Qwen 다각도.
- **관측(observation·보정)** = 실촬영 + 교차태스크/교차뷰 일관성: depth·3D 재구성·RGB mocap·세그.
- **라벨/큐레이션** = VLM(Qwen3-VL)·SAM3·Sapiens2.

---

## 1. 캡처 → 3D 기하 (스튜디오 뼈대) — #43·#58
- **VGGT** (Meta/Oxford) — 한 패스로 카메라·depth·pointmap·트랙. 현 피드포워드 3D 중심. ★
- **MASt3R / DUSt3R / Fast3R / MapAnything** — pointmap 재구성(쌍→다뷰).
- **3DGS**: `gsplat`(nerfstudio) 백본 · 피드포워드 GS **MVSplat·pixelSplat·Uni3R(VGGT 기반)·AVSplat·GeoForward·2Xplat**.
- **동적 4D**: Deformable-3DGS·4DGS(#48). **SfM**: COLMAP·GLOMAP(초기화·검증).
- 실내외: 실내=소수뷰 GS 바로, 실외=다뷰/스테레오 보강.

## 2. depth / normal 기하 프라이어 — #44·#45
- **Depth Anything 3 (Metric-L)** — 빠름(~33ms)·정확, 범용 1픽. ★
- **Depth Pro** (Apple) — intrinsics 없이 metric·경계 선명(느림 ~0.8s).
- **MoGe-2** (MS) — 스케일 알 때 최고 정밀 · **UniDepth v2·Metric3D v2** — 실외 스케일.
- normal/휴먼 기하: **Sapiens2**. 정밀 실외 metric은 스테레오 고려(2026 Jetson 벤치).

## 3. 카메라컨트롤 비디오 생성 (외관·모션·시점증강) — #46·#49
- 오픈 베이스: **Wan 2.x**(Alibaba) ★ · CogVideoX · HunyuanVideo · LTX-Video.
- **ReCamMaster**(KwaiVGI) — 기존 영상 새 카메라 경로 리렌더 = '가상 카메라' 핵심. ★
- CameraCtrl · MotionCtrl · RealCam-I2V · CamCloneMaster · CameraAnything.
- ⚠️ 전부 기하 부정확 → 증강/예측용, 실측·일관성 보정 필수.

## 4. 조명 / 리라이팅 ("조명 달기") — #50·#51
- **IC-Light (v2)** — 인물·오브젝트 리라이팅, 대중적(복잡장면 약함). ★
- **Neural Gaffer** — 환경맵(HDR) 조건 리라이팅 · **relightable 3DGS** — 장면 재조명 재구성.
- 2026: **PI-Light**(물리기반 2단계, ICLR'26)·**TokenLight**(조명 토큰)·**LightCtrl**(희소 물리단서). 대부분 합성지도 학습=스튜디오와 동결.

## 5. 세그 / 매팅 (컴포지팅·마스크) — #53
- **SAM 3 / 3.1** (Meta) — 텍스트·예시 프롬프트 검출+세그+트래킹 통합, 체크포인트·FT 코드 공개. ★
- **SAM 3D (Objects/Body)** — 단일영상 3D.
- **BiRefNet**(MIT, 고해상 매팅)·Matte-Anything·RMBG — 그린스크린 없는 합성.

## 6. 휴먼 / 포즈 / 모캡 — #54 (세 갈래)
**(a) 합성 생성 GT (스튜디오 내부, RGB mocap 불필요 — 렌더가 더 정확):**
- **BEDLAM 2.0** (SMPL-X GT, 카메라모션·초점 다양) ★ · SynBody · AGORA(평가용).
**(b) 실영상 보정 관측(= #42/#43 관측):**
- **GVHMR**(월드그라운드, 드리프트↓) ★ · WHAM(온라인·SLAM, 연구용) · TRAM/OnlineHMR(스트리밍) · 전신+손+얼굴 **SMPLest-X** · 밀집 **Sapiens2** · 다중카메라 마커리스 **EasyMoCap**.
**(c) 실제 사람 → 4D 자산(아바타):**
- **LHM**(단일이미지 초단위) · AniGS · **AHOY**(가림 강건 모노) · F3G-Avatar(멀티뷰) · 4DHumanDiff(텍스트→4DGS). 영상구동 리타겟(Animate Anyone/Champ/MimicMotion)=외관증강용(기하 부정확).

## 7. 합성데이터 시뮬레이터 / 월드모델 (진짜 '스튜디오' 엔진) — #43·#57
- **Infinigen** (Princeton) — 절차생성 포토리얼 **실내+자연(실외)**, depth·normal·세그·flow GT 공짜. 오픈소스 코어 1순위. ★
- **Kubric**(Google) · **BlenderProc** · **NVIDIA Isaac Sim / Omniverse Replicator**.
- **NVIDIA Cosmos**(월드 파운데이션, 물리 AI 합성데이터) · **Genie·Yume(인터랙티브 월드)·WorldCast(월드일관 카메라)** — 생성형 스튜디오 프런티어(세부 별도 확인).

## 8. VLM 자동 라벨·오케스트레이션 ("Qwen layer") — #43 큐레이션
- **Qwen3-VL** — 캡션·그라운딩·품질태그 자동부여(스튜디오 데이터 라벨링). ★
- **Qwen-Image-Edit (Multi-Angle)** — 궤도 ±90°·틸트 다각도 **이미지 편집**(키프레임/증강). ⚠️ 2D편집=metric 기하 아님.

## 9. 오디오 스튜디오 — #59~#62 (별도 모달)
- RIR 시뮬(공짜 음향 GT): **pyroomacoustics · gpuRIR**(건조↔잔향 쌍).
- 향상/분리: DeepFilterNet·음원분리(오픈) · 빔포밍 MVDR/GSC(+적응보정) · AEC(Kalman/NLMS).
- 오디오-비주얼(입모양↔소리 일관성)=교차모달 공짜 관측(#60).

---

## 실내 vs 실외 요약
- **실내**: 스케일·조명 제어 쉬움 → Infinigen Indoors + 3DGS + IC-Light 바로.
- **실외**: 하늘·날씨·대스케일 → metric depth 어려움(UniDepth/Metric3D), 스테레오/다뷰 보강, HDR env 조명 추정 중요.

## 우리 연구 매핑 (핵심)
기하진실원(VGGT/splatting+depth) = #43/#58 보정 관측 · 생성증강(Qwen/ReCamMaster/리라이팅) = 예측 · 라벨(Qwen3-VL/SAM3/Sapiens2) = 큐레이션. **생성뷰가 3D 재구성 품질을 올리나 vs 일관성 보정 없으면 망치나** = #58 toy의 실증 축.

## 연결
[[selfcorrecting-studio-engine]] #43 · [[digital-studio-benefit-map]](#44–#62) · [[filtering-synthetic-robust]] #42 · [[research-topics-ledger]] · [[research-genesis-34-43]] · 🧭 나침반.
