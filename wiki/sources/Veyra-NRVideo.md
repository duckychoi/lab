---
title: "Likely7/Veyra-NRVideo — Windows 실시간 GPU 영상 향상 플레이어 (초해상·디노이즈·프레임 생성 호스트)"
type: source
domain: video-saas
tags: [video-saas, github-trending, super-resolution, frame-generation, windows, gpu]
created: 2026-11-16
updated: 2026-11-16
sources: [https://github.com/Likely7/Veyra-NRVideo]
reliability: medium
---

**레포**: [Likely7/Veyra-NRVideo](https://github.com/Likely7/Veyra-NRVideo) · ★**2,900**(볼트 11-16 실측 · 수집기 ★2,466) · fork 228 · C++ · GPL-3.0(+Chiaki 부분 AGPL-3.0) · repo id 1362562155 · 생성 2026-09-09 · 최신 릴리스 **v2.1.9 《迎接GTA6降临》(2026-11-15T15:51Z)** — 수집기 기록 v2.1.6 이후 하루 사이 3개 릴리스.

## 핵심 인사이트
> [!insight] 모델 레포가 아니라 "벤더 런타임을 엮는 호스트"
> RTX Video SR · DLSS/XeSS/FSR · 신경망 디노이즈(최대 4레이어) · RTX Video HDR · 프레임 생성 · 색보정 · 녹화를 로컬 영상 · 캡처카드 · PS5/Xbox/PC 스트리밍 · 화면 캡처 입력에 한 파이프라인으로 건다. 자체 모델은 없고 *"Source Git excludes proprietary runtimes/models"*. AI 생성 영상의 **재생 · 캡처 단계 후처리**라는 별도 층이다.

> [!warning] 간판과 본문의 층 차이 — [[한정어-탈락]]
> 레포 description: *"Bring PS5 GTA6 to 120FPS with DLSS 5."* README 본문은 *"Community runtimes are not vendor certification or a complete official DLSS 5 integration"*, 187행 *"Submitted FPS is not physical display FPS or end-to-end latency"* 로 한정한다. 🟡 수집기 "README 에 GTA 언급 0건"은 **수집 이후 README 가 바뀌어** 현재는 릴리스 코드명(103 · 121행 《迎接GTA6降临》)으로 2건 존재 — 120FPS 주장은 여전히 0건(볼트 grep). 시점 차이라 오류로 세지 않는다.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: README 수치는 **효과 비용뿐** — RTX 5070 4K FXAA ~0.15ms · SMAA/MLAA ~0.30ms · 얼굴 메시 보정 1080p ~0.93ms / 4K ~1.42ms. 화질 정량 지표 없음.
- **크리에이터 인사이트**: 생성 영상 업스케일보다는 게임 · 스트리밍 시청자 대상. 누적 포터블 다운로드 79,332(2026-11-08, "다운로드 이벤트 수이지 고유 사용자 아님" — README 자체 한정).
- **경쟁 우위 빈틈**: 노드 편집기로 효과 체인을 짜는 UX 는 참고 가치. RTX 30/40 커뮤니티 NR/FG · Xbox 장시간 구동은 README 가 "미검증"으로 명시(236행 인근).
- **액션**: 없음(Windows + RTX/RX 전용, 볼트 작업 환경과 무관).

## 관련 페이지
- [[Comfy-Org-RelayVSR]](생성 영상 쪽 초해상) · [[한정어-탈락]] · [[자기제한-명시]] · [[AI-영상-생성-2026]] · [[TNT-Likely]](이름 유사 — 동일인 여부 미확인)

## 원본
- 출처: https://github.com/Likely7/Veyra-NRVideo
- 확인 범위: GitHub API 메타 · releases/latest · README GTA/120fps grep · 187행 · README 커밋 이력(11-15 17:14Z 이후 3회 수정) · 🔴 효과 비용 수치 · 다운로드 수는 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐ (★2,900 · 화질 측정 0)
