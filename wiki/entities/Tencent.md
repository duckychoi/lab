---
title: Tencent
type: entity
domain: ai-news
tags: [ai-news, tencent, agent-infra, sandbox, hunyuan, entity]
created: 2026-07-04
updated: 2026-07-09
sources: [CubeSandbox.md, Multi-Layer-Agent-Red-Teaming.md, Distribution-wise-Rewards.md, Hy3.md, TencentDB-Agent-Memory.md]
reliability: high
---

# Tencent (텐센트)

> [!insight] 핵심
> Hunyuan(HY) 모델군·클라우드·에이전트 인프라를 보유한 중국 빅테크. 위키 맥락의 신규 신호는 **에이전트용 경량 동시성 샌드박스 [[CubeSandbox]]**(TencentCloud) — "LLM이 생성한 코드를 안전·병렬 실행"이라는 에이전트 스택의 숨은 병목을 겨냥. 앞서 [[HY-Embodied]]·[[HY-World-2.0]]·[[MegaStyle]] 등 모델·데이터 쪽 기여와 함께, 에이전트 **실행 런타임**([[CubeSandbox]])에 이어 **에이전트 보안**([[Multi-Layer-Agent-Red-Teaming]], AI-Infra-Guard)까지 확장 — "코드 실행+공급망 감사"로 에이전트 인프라 양면을 채우는 포지션.

> [!note] 2026-07-09 추가 — Hunyuan 오픈 모델 + 로컬 메모리 동시 배출
> 하루에 모델과 도구를 나란히 공개: **[[Hy3]]**(Hunyuan Hy3, 295B/21B 활성 MoE·256K·Apache 2.0, "스캐폴딩 간 편차 4% 이내" 주장)로 오픈 MoE 플래그십 경쟁에 참전하고, 같은 날 **[[TencentDB-Agent-Memory]]**(완전 로컬 에이전트 장기 메모리, MIT·TypeScript)로 [[에이전트-메모리-레이어]]의 실물 구현체를 냄. 실행 런타임([[CubeSandbox]])·보안([[Multi-Layer-Agent-Red-Teaming]])에 이어 **모델·메모리**까지 = 에이전트 인프라 전방위 커버.

## 관련 페이지
- [[Hy3]] — Hunyuan 295B/21B MoE 오픈 모델 (2026-07-09)
- [[TencentDB-Agent-Memory]] — 완전 로컬 에이전트 장기 메모리 (2026-07-09)
- [[CubeSandbox]] — 에이전트 코드 격리 실행 샌드박스
- [[Multi-Layer-Agent-Red-Teaming]] — 다층 에이전트 레드팀(AI-Infra-Guard)
- [[Distribution-wise-Rewards]] — Hunyuan 분포 보상 시각생성
- [[HY-Embodied]]
- [[HY-World-2.0]]
- [[AI-에이전트-프레임워크]]

## 원본
- 대표 레포: https://github.com/TencentCloud/CubeSandbox
- 신뢰도: ⭐⭐⭐⭐ (빅테크·다수 오픈 릴리스)
