---
title: AOHP — OS 레벨 에이전트 하네스 오픈소스 프레임워크
type: source
domain: ai-news
tags: [ai-news, hf-paper, agent-harness, os-level, open-source, security, personalization]
created: 2026-06-24
updated: 2026-06-24
sources: []
reliability: medium
---

# AOHP: An Open-Source OS-Level Agent Harness

> [!insight] 핵심 인사이트
> HF 데일리 22 upvotes. **개인화·효율·보안**을 설계 목표로 내건 OS 레벨 에이전트 하네스 오픈소스. 에이전트를 앱 안이 아니라 *운영체제 레이어*에서 돌려 파일·프로세스·입출력 전반을 다루게 하는 방향 — [[hermes-agent]]·[[OpenComputer]]·[[trycua-cua]]가 보여준 "에이전트가 컴퓨터를 통째로 쓴다" 흐름의 *하네스(실행 골격) 표준화* 시도. 보안을 1급 설계 목표로 명시한 점이 [[SkillSpector]]·[[Anthropic-Cybersecurity-Skills]] 류의 에이전트 보안 의식과 합류.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — HF 추천 22, arXiv 2606.23449. 오픈소스라면 코드 검증 가능하나 "보안" 클레임의 위협 모델 범위 확인 필요.
- **즉시 활용**: MAYBE — OS 레벨 에이전트 하네스는 내 Telegram/크론 자동화 스택과 구조적으로 유사. 개인화·보안 레이어 설계를 참고할 여지.
- **6개월 영향력**: 에이전트가 OS 권한을 갖는 순간 보안이 핵심 — "효율 + 보안 동시 설계" 하네스가 표준화되면 데스크톱 에이전트 채택의 신뢰 장벽이 낮아짐.
- **대체 관계**: [[hermes-agent]](메신저 게이트웨이형), [[trycua-cua]](컴퓨터 사용)와 경쟁/보완. AOHP는 *OS 레벨 + 보안 우선* 포지션.
- **허와 실**: "보안 갖춘 OS 에이전트"는 양날의 검 — 권한이 클수록 사고 피해도 큼. 샌드박싱·권한 최소화 실제 구현 수준이 진짜 가치.
- **액션**: 레포 존재 시 보안 아키텍처(권한 모델, 샌드박스) 분석 → 내 자동화 스택 보안 강화에 차용.

> [!warning] 보안 주의
> OS 레벨 에이전트는 파일 삭제·자격증명 접근 등 고위험 행동 가능. 권한 격리·승인 게이트 없는 운용 금지.

## 관련 페이지

- [[hermes-agent]]
- [[OpenComputer]]
- [[trycua-cua]]
- [[SkillSpector]]
- [[Anthropic-Cybersecurity-Skills]]
- [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://huggingface.co/papers/2606.23449
- HF 추천: 22 upvotes (2026-06-24)
- 신뢰도: ⭐⭐⭐ (HF 추천, 프리프린트 — 보안 위협모델 검증 필요)
