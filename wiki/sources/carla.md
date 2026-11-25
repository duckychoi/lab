---
title: "carla — 자율주행 연구용 오픈 시뮬레이터, 1.0(UE 5.8) 정식 릴리스"
type: source
domain: slam-3dgs
tags: [slam-3dgs, github, autonomous-driving, simulator, unreal-engine, mcp, agentic, robotics]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/carla-simulator/carla]
reliability: high
---

**레포**: carla-simulator/carla · ★ **14,707**(수집기 11-25) → **14,708**(볼트 API 11-25) · C++ 일간 Trending(당일 +8) · MIT(코드) · 생성 2017-10-24 · push 2026-11-25 · **릴리스 1.0(2026-11-17)** — 9년 차 레포의 정식판 전환([[기준선-재부상]] 트리거 유형 — 재등장에 의미 있는 이벤트가 있는 경우)

## 핵심 인사이트
> [!insight] 시뮬레이터에 "에이전트 스킬 + MCP"를 붙였다 — 시뮬레이터가 에이전트의 작업 환경이 되는 전환
> 2017년 레포의 재등장이지만 트리거는 **1.0 정식판**. 릴리스 노트 기준: Unreal Engine 5.8(자체 포크) 이전 — World Partition · Lumen · 하드웨어 레이트레이싱, Ubuntu 24.04 · RTX 50(Blackwell) 지원. **"Agentic CARLA"**: `Skills/` 아래 검증된 절차 64개(설정 · Python API · 빌드 · Scenario Runner · Leaderboard · ROS 2 등) + 에디터 실행 시 **Unreal MCP 서버(`localhost:6256/mcp`)를 띄워 Claude Code 등이 붙게 함**. 센서: NVIDIA NuRec 26.04(실주행 녹화를 시뮬 가능한 장면으로) · Cosmos 2.5/3로 날씨 · 시간대 · 노면 변형 · DLSS 4.5 · 경로추적 렌즈 카메라.

> [!note] 이전 조건
> 권장 사양 **RTX 3070 이상 · VRAM 16GB · RAM 32GB**, Ubuntu 20.04 · Windows 10 미지원. UE 4.26 계열(0.9.16 이하)은 곧 폐기. 성능 수치 없음.

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA 관계**: 자율주행 시뮬레이터 표준의 대규모 버전 전환 — UE 4.26 기반 연구 자산은 마이그레이션 압박.
- **실용성**: 에이전트 스킬 64개 + MCP 서버 조합은 "복잡한 전문 도구를 에이전트에 연결"하는 **설계 참고 사례** — 시뮬레이터 외 도메인에도 복제 가능한 패턴([[Claude-Code-워크플로우]] 축).
- **응용 가능성**: 볼트 로봇/카메라 축에서 실기 없이 센서 · 제어 실험 환경이 필요해지면 후보 — 단 GPU 요구가 높다.
- **액션**: Agentic CARLA의 Skills/ 구성을 열어 볼 — 볼트 스킬 설계 참고(우선순위 낮음, actionable 등록).

## 관련 페이지
- [[Claude-Code-워크플로우]] · [[기준선-재부상]] · [[slam-3dgs]]

## 원본
- 출처: https://github.com/carla-simulator/carla
- 확인 범위: README + 릴리스 노트(수집기 11-25) · GitHub API 재확인(볼트 11-25 — ★ · 라이선스 · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐⭐ (★1.5만 · 9년 공식 프로젝트 · 1.0 릴리스 노트 기준)
