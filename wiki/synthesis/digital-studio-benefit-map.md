---
title: "디지털 스튜디오 수혜 AI 모델 전수 예측 + 하위과제 맵 (#43 → #44–#57)"
created: 2026-11-23
author: fryday
tags: [synthesis, data-engine, task-map, synthetic-data, 3d-vision, film-production, ledger-43]
parent: 43
purpose: 전방향 조명·카메라뷰 디지털 스튜디오가 공짜 GT로 성능을 끌어올릴 AI 모델 분야를 전수 예측하고, 각각을 개별 연구번호로 등재
---

# 디지털 스튜디오 수혜 AI 모델 전수 예측 + 하위과제 맵

> 전제: 교수님의 AI 영상제작 툴 = **전방향 조명·카메라뷰를 제어하는 디지털 스튜디오**. 같은 장면을 **임의의 조명 × 시점 × 시간**으로 렌더하며, 픽셀/프레임마다 **정확한 GT를 공짜로** 얻는다.
> 모든 하위과제의 공통 신규성 = 각 태스크에 **#42/#43 필터‑지배 자기교정 루프**(합성=예측 · 실촬영=보정 · 태스크 일관성=공짜 관측 · 수축=붕괴방지)를 적용 → 샘플효율·강건성·붕괴내성.

## 🎁 스튜디오가 '공짜로' 주는 감독신호
기하(depth·normal·3D좌표) · 모션(optical/scene flow·궤적) · 카메라(pose·intrinsics) · 조명(HDR env·광원파라미터·그림자) · 재질(albedo·BRDF·roughness/metal) · 의미(instance/class/part/amodal 마스크·matting α) · 휴먼(SMPL·관절·손/얼굴 메쉬). **핵심 초능력 = 방해인자(조명·시점·모션블러·날씨)를 가로지르는 '쌍(paired)' 데이터.**

## 🗺 수혜 분야 전수 (9 군)
- **A. 기하/카메라**: 단안 metric/상대 depth · MVS/스테레오 · optical flow · scene flow · surface normal · SfM/SLAM/VO · 카메라 relocalization · intrinsics 캘리브레이션 · depth completion/super-res.
- **B. 재구성**: NeRF · 3DGS · 4DGS/동적 · SDF/occupancy · mesh recon · point-cloud completion · novel-view synthesis.
- **C. 역렌더링/외관**: intrinsic 분해(albedo/shading) · 재질/BRDF · 조명(HDR env) 추정 · relighting · 그림자 검출/제거 · 반사/스펙큘러 분리 · de-light.
- **D. 저수준 복원**: denoise · deblur · dehaze · 저조도 향상 · super-resolution · HDR 복원 · demosaic · 롤링셔터 보정.
- **E. 의미/검출**: semantic/instance/panoptic/amodal 세그 · object detection · 6DoF 포즈 · **matting/α(그린스크린 없는 합성)** · edge/boundary.
- **F. 휴먼중심**: 3D human pose/SMPL · 모캡 · 손 메쉬 · 얼굴 메쉬/랜드마크 · gaze · 파트 세그 · 의상/cloth · re-ID.
- **G. 시간/비디오**: video object seg · MOT 추적 · video depth · 시간 일관성 · action recognition · event-camera.
- **H. 생성/세계/체화**: 비디오 생성 **물리 일관성** · 월드모델 · sim2real 로보틱스 · VLA 정책 · 자율주행 지각 · 카메라컨트롤 생성.
- **I. 영화 특화 킬러앱**: match-moving(카메라 트래킹) · 로토/매팅 · 합성용 relighting · depth 기반 DOF/안개 · 버추얼 프로덕션(LED 볼륨) 캘리브 · 얼굴/바디 교체 리얼리즘 · 그림자/접촉 그럴듯함.
- **J. 음향(오디오)**: 음성 향상/잡음제거 · 음원 분리 · 오디오-비주얼 분리 · 음원 위치추정(DOA)/마이크 어레이 빔포밍 · 잔향제거/에코제거(AEC) · 공간오디오/HRTF · ASR 강건성 · 더빙/립싱크. ★칼만·적응필터가 **이미 고전 백본**(Wiener/Kalman 향상, RLS/NLMS·Kalman AEC, MVDR 빔포밍) → #42 루프 네이티브. "음향 스튜디오"(방·음원·마이크·RIR 제어 → clean·방향·위치 GT 공짜)=디지털 스튜디오의 오디오 쌍둥이.
- **뷰 중첩(view-overlap)**: SfM/MVS/3DGS의 고중첩(60~80%) 요구 → 저중첩/희소뷰 실패. 가상 카메라로 중첩률 제어 + **교차뷰 reprojection 일관성(=#43 공짜 관측)** 으로 저중첩 재구성. = #43 을 중첩 축에 적용.

## 🔢 하위과제 등재 (#44–#57) — 각 = 스튜디오 공짜GT + 필터‑지배 루프
> 표기: **난이도** / **붐빔**(기존연구 밀집도) / **영화툴 직결도**. 공통 신규성은 "루프 적용"이므로 아래는 태스크별 특이점만.

### 기하·카메라
- **#44 조명·시점 불변 metric depth** — 같은 기하에 조명×뷰 랜덤화, depth GT 고정 → 조명 불변 강건 metric depth. 특이점: depth는 조명 불변(기하 안 변함)이라 **domain randomization의 정석 수혜**. 붐빔↑(PNDR·RaSim), 신규=가이드 랜덤화+실보정 게인. [난이도 하 / 붐빔 상 / 영화 상] ★최우선 toy 후보
- **#45 표면 법선 + 역렌더링(albedo/shading)** — 다조명 쌍으로 normal·albedo·shading 동시 분해(inverse rendering). [중/중/상]
- **#46 스플랫 뷰합성 카메라 포즈/relocalization** — 실 카메라 리그 없이 가상 뷰 렌더로 포즈 학습. 근접 2412.00138(적대적 sim2real) → 신규=일관성 루프+수축. [중/중/상] ★toy 후보
- **#47 optical/scene flow** — 공짜 모션 GT(픽셀 대응). 합성 flow의 정석(FlyingThings 계보), 신규=실보정 루프. [중/상/중]

### 재구성
- **#48 3DGS/4DGS 동적 재구성 + GS 시간추적** — 멀티뷰+시간 GT. 가우시안의 시간추이 추적·보정(이전 'GS temporal tracking' 문의 흡수). [상/중/상] ★toy 후보
- **#49 novel-view synthesis / 비디오 물리 일관성** — 월드·비디오 모델용 물리consistent 멀티뷰 데이터 생성. [상/상/상]

### 역렌더링·외관
- **#50 조명(HDR env-map) 추정** — 공짜 라이팅 GT로 단일영상 HDR 환경광 추정. [중/중/상]
- **#51 relighting + 그림자/반사 제거(de-light)** — 임의 재조명·그림자 제거. 영화 컴포지팅 핵심. [상/중/최상] ★영화 킬러앱
- **#52 저조도·dehaze·deblur·SR 복원 강건성** — 제어된 degradation 쌍(깨끗↔열화). RaSim식 실열화 모델 결합. [하/상/중]

### 의미·휴먼
- **#53 세그/인스턴스/amodal + 매팅(그린스크린 없는 합성)** — 임의 조명·뷰에서 공짜 마스크·α. **영화 컴포지팅 킬러앱**. [중/상/최상] ★toy 후보(영화 직결)
- **#54 3D 휴먼 모캡/SMPL + 손·얼굴 메쉬** — 멀티뷰 스튜디오=가상 모캡 스테이지, 공짜 3D 관절 GT. [상/상/상]
- **#55 6DoF 물체 포즈** — 공짜 포즈 GT, 조명·오클루전 강건. [중/상/중]

### 시간·체화
- **#56 비디오 추적/VOS 시간 일관성** — 공짜 트랙 GT + 일관성 루프로 시간 flicker 억제. [중/중/상]
- **#57 sim2real 체화/VLA/자율주행 지각** — 스튜디오→정책/지각, 물리+보정 루프로 sim2real 갭 축소. [상/상/중]

### 뷰 중첩·희소뷰
- **#58 희소·저중첩 멀티뷰 재구성 강건성** — 가상 카메라로 중첩률 제어 + 교차뷰 reprojection 일관성(#43 관측)으로 저중첩/희소뷰에서도 재구성. 근접: 희소뷰 재구성(pixelSplat/MVSplat 계보) 핫·붐빔, 신규=스튜디오 중첩 커리큘럼 + 일관성 루프. [상/붐빔상/상] = #43 의 중첩 축.

### 음향(오디오) 스튜디오 — 섹션 Q
> 칼만·적응필터가 오디오의 고전 백본 → #42 루프가 비전보다 더 native. "음향 스튜디오"=방·음원·마이크 위치·잡음·RIR 제어로 clean 신호·방향·위치 GT 공짜. 공통 신규성=필터 루프 + 교차(오디오-비주얼) 일관성 관측.
- **#59 음성 향상·잡음제거(speech enhancement)** — Kalman/Wiener 향상 고전 백본, 합성 잡음·RIR 쌍 + 실측 보정 루프. [중/붐빔상/상]
- **#60 음원 분리 + 오디오-비주얼 분리** — 영화툴 대사/배경 분리. AV 일관성(입모양↔소리)=교차모달 공짜 관측. [상/상/최상] ★영화 직결
- **#61 음원 위치추정(DOA)·마이크 어레이 빔포밍** — 공간오디오, 카메라포즈의 음향 아날로그. MVDR/GSC 빔포밍+적응보정. 이전 빔포밍 연구(neuralbeamforming) 연결. [중/중/상]
- **#62 잔향제거·에코제거(AEC)** — RIR 제어로 건조↔잔향 공짜 쌍, Kalman-AEC 루프. [중/붐빔상/상]

## 우선순위 제안 (toy 착수 순)
1. **#44 조명불변 metric depth** — 가장 깨끗·빠른 실증, Depth Pro 계기와 직결.
2. **#53 매팅/세그** — 영화툴 즉시 가치(그린스크린 제거).
3. **#46 스플랫 뷰합성 포즈** · **#48 4DGS 시간추적** — 3D 재구성 축.
4. **#51 relighting/de-light** — 영화 VFX 고가치·고난도.

## 정직한 총평
- 개별 태스크의 "합성데이터 학습"은 **대부분 레드오션**. 우리 방어 가능한 신규성은 **태스크 전반을 하나의 필터‑지배 자기교정 데이터엔진(#42/#43)으로 묶고, 태스크 간 일관성을 공짜 관측으로 써 실데이터 예산을 접는 것** + 수축 붕괴보증.
- 리스크: 학습된 스튜디오(생성뷰)에서 데이터 생성 시 그 오차 상속(garbage-in) → 실관측 보정이 차단기. sim2real 갭은 태스크마다 크기 다름(depth·matting 큼).

## 연결
[[selfcorrecting-studio-engine]] #43(부모) · [[filtering-synthetic-robust]] #42 · [[digital-studio-tech-stack]](구현 테크스택) · [[research-topics-ledger]] · [[research-genesis-34-43]] · 🧭 나침반.
