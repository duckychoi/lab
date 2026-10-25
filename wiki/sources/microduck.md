---
title: "microduck — 25cm·800g 이족보행 로봇의 온보드 SW. 50Hz · 서보 15개 · ONNX 정책. 🔴 '하드웨어 필요'는 틀렸다 — MuJoCo 시뮬로 그대로 돈다"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, sim2real, rl, ppo, mujoco, onnx, rk3566, legged, github-trending, rust]
created: 2026-10-25
updated: 2026-10-25
sources: []
reliability: medium
---

# microduck

**GitHub**: https://github.com/pollen-robotics/microduck (정책 학습: `pollen-robotics/microduck_rl`)
**실측(2026-10-25 KST)**: ★ **11,211**(수집기 11,208 · +3) · Apache-2.0 · `language: Rust` · created **2026-07-29** · pushed 2026-10-24 · 제작사 [[Pollen-Robotics]]
**도메인 재분류**: 수집기 `ai-news` → **`slam-3dgs`**(로봇 제어 · 볼트 10-17~10-24 slam-3dgs 0건 지속의 해소분)
**신뢰도**: ⭐⭐⭐ (3개월 1.1만 ★ · 오픈 하드웨어 제작사 · 정량 성능 주장 없음)

> [!insight] 핵심 인사이트 — **저가 로봇 RL 의 전체 파이프라인(학습→ONNX→온보드 50Hz)이 두 레포로 닫혀 있다**
> README: *"Rockchip RK3566: a 50 Hz control loop driving fifteen servos from neural policies"* · 학습은 `microduck_rl`(*"MuJoCo and PPO, domain randomisation, and the ONNX export this repo loads"*).
> 🎯 **[[VLA]] 휴머노이드 노트(크론 10-25)가 말한 "느린 추론(1~10Hz) + 빠른 제어(100~1000Hz)" 2계층에서, 이 레포는 '빠른 층'만을 신경망으로 대체한 최소 사례다** — LLM/VLA 없이 RL 정책만으로 50Hz.

> [!warning] 🔴 수집기 정정 — *"하드웨어 구매 필요"* 는 과장이다
> README: *"**No robot on the desk?** `scripts/duck-sim` runs the real daemons against a body in MuJoCo — one duck in a window, or four as machines you log into"* ⇒ **실제 데몬을 시뮬 몸체에 붙여 돌린다.** 하드웨어 없이 파이프라인 전체를 실험할 수 있다. (수집기 요약은 *"참고 가치 높음(하드웨어 구매 필요)"*)

## 도메인별 추출 (slam-3dgs)
- **현재 SOTA**: 해당 없음(SLAM/3DGS 아님 · 소형 이족보행 제어). 벤치 수치 0건(README 전문 기준)
- **실시간 가능성**: **50Hz 제어 루프** · RK3566(저가 ARM SoC) — 로봇 제어 하한선으로는 낮은 편이나 소형·저관성 몸체에 맞춘 값
- **카메라 파이프라인**: README 에 카메라 언급 없음 — **고유수용 감각(proprioception) 기반 정책**으로 판단(추정)
- **응용 가능성**: 🎯 sim2real 학습 → ONNX → 임베디드 추론 흐름은 [[임바디드-AI]] 실험의 최저비용 입문로
- **필수 레퍼런스**: `microduck_rl` (PPO · domain randomisation)

## 관련 페이지
- [[Pollen-Robotics]] · [[임바디드-AI]] · [[VLA]] · [[월드모델]]
- 같은 배치 로봇 계열: [[FRED]] · [[LaLa-World]] · [[Physical-RSI]]
- [[리서치-휴머노이드-로봇의-VLASLAM로컬LLM-통합-제어-2026-최신-동향]] — 2계층 아키텍처 서술
- [[slam-3dgs]]

## 원본
- 출처: https://github.com/pollen-robotics/microduck
- 신뢰도: ⭐⭐⭐ (GitHub 스타 11,211)
