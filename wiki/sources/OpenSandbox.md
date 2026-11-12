---
title: "OpenSandbox — 에이전트용 자가 호스팅 샌드박스 런타임(Docker·K8s 동일 API, 구 alibaba/OpenSandbox)"
type: source
domain: ai-news
tags: [ai-news, github-trending, sandbox, agent-infra, kubernetes, firecracker]
created: 2026-11-12
updated: 2026-11-12
sources: [https://github.com/opensandbox-group/OpenSandbox]
reliability: medium
---

**레포**: [opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox) · ★**17,228** · fork 1,633 · Apache-2.0 · Go · created 2025-12-17 · pushed 2026-11-12T08:55Z (GitHub API 볼트 실측 — 수집기 수치와 일치)

> [!note] 🆕 볼트 발견 — 원래 `alibaba/OpenSandbox` 다
> `api.github.com/repos/alibaba/OpenSandbox` 가 **301 → repositories/1118085970** 이고 이 ID 가 opensandbox-group/OpenSandbox 와 같다. 즉 조직 이전(알리바바 → 독립 그룹)된 같은 레포다. 볼트에는 소스 페이지가 없었고 [[agentscope]] 가 샌드박스 백엔드 후보(local/Docker/E2B/OpenSandbox)로 언급만 했다. README 의 "Agentic AI Foundation(AAIF) 프로젝트" 표기는 수집기 판독. → [[정규명-우선-중복검사]]

## 핵심 인사이트
> [!insight] 에이전트 인프라의 병목이 "모델"에서 "격리된 실행 환경을 얼마나 싸고 빠르게 대량 생성하나"로 이동
> 로컬 Docker 와 Kubernetes 에 **같은 API**, 샌드박스별 egress 정책, 통합 ingress, **실제 자격증명을 샌드박스에 노출하지 않는 Credential Vault**, Python·Java/Kotlin·TS·C#·Go SDK, `osb` CLI, MCP. README 수치: Firecracker 샌드박스 생성 **64 ms P50(직렬) / 125.4 ms P99(동시 10개)**, pause/resume 시 메모리·디스크 보존(수집기 판독). RL 학습·에이전트 평가처럼 **샌드박스를 수천 개 찍는** 용도에 맞춘 설계다 — 같은 날 입고된 [[Embodied-First-Exam]](1,156 과제)·[[codex-security]] 같은 워크로드가 이런 런타임 위에서 돈다.

> [!warning] 자체 측정 · 조건 미열람
> 64/125.4 ms 는 프로젝트 자체 측정이고 하드웨어 조건 문서(`docs/architecture/fast-sandbox/performance.md`)는 볼트·수집기 모두 미열람. Firecracker 경로는 Kubernetes(+KVM) 전제라 로컬 Docker 경로의 생성 지연은 다를 것이다.

## 도메인별 추출 (ai-news / local-llm 교차)
- **신뢰도**: ★17,228 · 당일 +97 · 자체 지연 수치만.
- **즉시 활용**: 부분 YES — 이 볼트의 스킬 하네스가 외부 코드를 돌릴 때(실행 0건 21배치+ 이월 문제) **격리 실행 환경**으로 후보. Docker 경로라면 단일 머신에서도 가능.
- **6개월 영향력**: E2B 같은 호스팅 샌드박스의 자가 호스팅 대안. Credential Vault 는 에이전트에 키를 주지 않는 패턴의 참조 구현.
- **대체 관계**: E2B · Daytona · 직접 짠 Docker 래퍼.
- **허와 실**: 기능 범위는 넓고 지연 수치는 자체 측정. 보안 경계(egress 정책 우회 가능성)는 외부 감사 기록 없음.
- **액션**: star · Docker 경로로 샌드박스 1개 생성 시간만 측정(낮음).

## 관련 페이지
- [[agentscope]] · [[codex-security]] · [[Embodied-First-Exam]] · [[정규명-우선-중복검사]] · [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/opensandbox-group/OpenSandbox
- 확인 범위: GitHub API 메타 · `alibaba/OpenSandbox` 301 리다이렉트 ID 대조(볼트) · 🔴 README·성능 문서 미열람 · 실행 미확인
- 신뢰도: ⭐⭐ (★17,228 · 자체 측정)
