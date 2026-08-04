---
title: agent-governance-toolkit — 자율 에이전트 통제(정책·제로트러스트·샌드박스·감사)
type: source
domain: ai-news
tags: [ai-news, agent-security, governance, zero-trust, sandbox, owasp, microsoft, mcp]
created: 2026-07-29
updated: 2026-07-29
sources: []
reliability: high
---

# agent-governance-toolkit (microsoft/agent-governance-toolkit · GitHub ⭐5.4k)

> [!insight] 핵심 인사이트
> [[Microsoft]]의 **"자율 AI 에이전트를 위한 정책 강제·제로트러스트 신원·실행 샌드박싱·신뢰성 엔지니어링"** 툴킷. 구성: **정책 엔진(YAML/OPA/Cedar) + 제로트러스트 신원·신뢰점수(SPIFFE/DID/mTLS) + 권한 링 샌드박싱 + 변조증거 감사로그 + MCP 보안 게이트웨이(툴 포이즈닝 탐지) + SRE(킬스위치·SLO 모니터링)**, 멀티프레임워크(Semantic Kernel·AutoGen·LangChain·CrewAI) + Python/TS/.NET/Rust/Go SDK. **OWASP Agentic Top 10을 10/10 커버**(ASI 리스크 전 범주를 결정론 통제에 매핑)를 명시 주장. [[StateAct]]·[[impeccable]]·[[open-code-review]]의 **"순수 LLM 판단을 결정론/구조로 게이트"** 흐름을 **보안·거버넌스**로 확장한 항. MIT.

> [!warning] 10/10 커버는 자체 주장 — MCP 보안 게이트웨이는 실효 검증 필요
> "OWASP Agentic Top 10 10/10 커버"는 **저장소 자체 표기**로 WebFetch에서 서브타이틀·매핑 문서 존재는 확인했으나 실제 방어 효과는 독립 검증 전. 다만 **MCP 보안 게이트웨이(툴 포이즈닝 탐지)**는 MCP 도구를 다수 쓰는 내 환경에 직결되는 부품이라 개념적으로 주목.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — 스타 5.4k·MIT·MS 공식·기능 WebFetch 실확인. OWASP 10/10은 자체 주장.
- **즉시 활용**: 조건부 — **MCP 보안 게이트웨이·킬스위치·권한 링**은 내가 MCP·브라우저 자동화(lightpanda)·studio 도구를 쓰는 환경의 안전장치로 참고. 통째 도입보단 **정책 게이트·감사로그 패턴**만 선별.
- **6개월 영향력**: 에이전트가 실행 권한을 갖는 흐름이 커질수록 **거버넌스가 필수 레이어**로 부상. [[ECC]] AgentShield(보안스캔)와 함께 "에이전트 운영 = 보안 포함" 표준화 신호.
- **대체 관계**: [[ECC]]의 보안 부분(AgentShield)을 전용·심화한 것. 실행 샌드박싱은 이전 위키 [[CubeSandbox]]([[Tencent]])와 계보.
- **허와 실**: "제로트러스트·10/10"은 강한 프레이밍 — 실질은 **정책 강제 + 신원 + 샌드박스 + 감사**의 조합 프레임워크. 방어 완전성 보장 아님.
- **액션**: MCP 보안 게이트웨이의 툴 포이즈닝 탐지 규칙을 코드로 확인 → 내 MCP 도구 사용에 최소 정책 게이트 적용 여부 판단.

## 관련 페이지
- [[Microsoft]]
- [[ECC]]
- [[StateAct]]
- [[impeccable]]
- [[open-code-review]]
- [[CubeSandbox]]
- [[Tencent]]
- [[AI-에이전트-프레임워크]]
- [[ai-news]]

## 원본
- 출처: https://github.com/microsoft/agent-governance-toolkit
- 스타: ⭐5.4k (2026-07-29, 당일 +46 — raw 5,379와 일치), MIT
- 기능: 정책엔진(YAML/OPA/Cedar)·제로트러스트 신원(SPIFFE/DID/mTLS)·권한 링 샌드박스·변조증거 감사·MCP 보안 게이트웨이·킬스위치/SLO·멀티프레임워크·5언어 SDK
- 주장: OWASP Agentic Top 10 10/10 커버(자체 표기)
- 신뢰도: ⭐⭐⭐ (스타·라이선스·MS 공식·기능 WebFetch 실확인, 커버리지 주장 자체표기 medium)
