---
title: "sam-3d-body-dinov3 — 단일 이미지 전신 3D 인체 메시 복원(SAM 3D Body)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-model, 3d-human, mesh-recovery, pose-estimation, mhr, sam-license, meta]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/facebook/sam-3d-body-dinov3]
reliability: medium
---

**모델**: facebook/sam-3d-body-dinov3 · 다운로드 30일 **20,355**(볼트 API 11-25 — 수집기 값과 정확 일치) · 누적 92,553(일치) · 좋아요 1,941 → **1,942** · trendingScore 119(트렌딩 18위) · HF 내부 ID `691b6d08…` · license other(**SAM License**) · gated(**수동 승인 — 생년월일 · 국가 · 소속 입력**) · 생성 2025-11-17

## 핵심 인사이트
> [!insight] 몸 · 발 · 손 포즈와 체형을 새 파라메트릭 리그 MHR로 — 골격과 표면 형상을 분리한 표현
> Meta Superintelligence Labs. 사진 한 장에서 몸 · 발 · 손 포즈와 체형을 새 파라메트릭 리그 **MHR(Momentum Human Rig — 골격과 표면 형상 분리)** 로 추정. 2D 키포인트 · 마스크를 보조 프롬프트로 받는 SAM식 인코더-디코더. 출력: 3D 정점 · 3D/2D 키포인트 · 카메라 이동 · 초점거리 · 몸/손 포즈 · 체형 파라미터. 파인튜닝 6 · 양자화 4 · Space 30개(MCP 래퍼 포함). 2025-11 모델의 재트렌딩(신규 아님). 볼트 [[digital-studio-tech-stack]] 에 "SAM 3D (Objects/Body)"로 언급만 있었다가 이번에 독립 등록 — [[Meta]] 의 SAM 계열([[sam3]]) 확장.

> [!warning] 벤치 수치 0 + SAM License 상업 조건 미확인 + 수동 게이트
> 카드에 정량 벤치 수치 없음("state-of-the-art" 서술뿐, 논문 링크 위임). **SAM License 상업 이용 조건은 볼트 미확인**. gated 수동 승인이라 원본 README도 막혀 카드 본문 HTML 판독(수집기).

## 도메인별 추출 (slam-3dgs)
- **응용 가능성**: 영상 속 인물 포즈 → 3D 캐릭터 리깅 · 모션 참조 추출에 바로 쓸 수 있는 후보 — video-saas 축(캐릭터 모션)과의 다리. MHR의 골격/표면 분리는 리깅 파이프라인 입력으로 적합한 형태.
- **경쟁 우위 관점**: 단일 이미지 → 전신(손 · 발 포함) 3D는 영상 제작 워크플로우의 "실사 참조 → 캐릭터" 단축 경로.
- **액션**: gated 승인 신청 후 실제 출력 품질 1차 확인이 유효한 항목 — 우선순위 낮음(actionable 등록).

## 관련 페이지
- [[Meta]] · [[sam3]] · [[digital-studio-tech-stack]] · [[기준선-재부상]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/facebook/sam-3d-body-dinov3
- 확인 범위: HF API 재확인(볼트 11-25 — dl30 · 누적 · 좋아요 · 내부 ID · 생성일 · gated 수동 일치) · 모델 카드(수집기 11-25 — 수동 게이트라 카드 본문 HTML 판독) · 실행 0
- 신뢰도: ⭐⭐ (벤치 수치 0 · 라이선스 상업 조건 미확인 · Meta 공식)
