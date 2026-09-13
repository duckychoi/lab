---
title: vxcontrol
type: entity
domain: ai-news
tags: [ai-news, security, offensive-security, 조직]
created: 2026-09-13
updated: 2026-09-13
sources: [pentagi.md]
reliability: high
identifiers: [vxcontrol]
---

# vxcontrol

**GitHub**: `vxcontrol` · 대표 배포물 [[pentagi]](⭐23,624 · Go · MIT)

> [!insight] 노선 — **자율 에이전트를 보안 실행기로 내리되, 경계를 문서화한다**
> [[pentagi]] 는 Docker 샌드박스 안에서 nmap·metasploit·sqlmap 등 20+ 툴을 LLM 에이전트가 위임 호출하는 자가호스팅 플랫폼이다. LLM 공급자 10종+ 교체 가능.
> 🎯 주목할 점은 기술이 아니라 **문서 습관**이다 — README에 `### Current Capability Boundaries` 섹션을 따로 두고 *"autonomous **and assistant-guided**"* · *"**not** a CALDERA-style BAS"* · *"conceptual or future work, **not** a feature that is implemented today"* 를 직접 적는다.
> ⚠️ 다만 **같은 README 63행은 여전히 "Fully Autonomous"** 이고 GitHub description도 그렇다. **경계를 적는 습관과 헤드라인을 고치는 습관은 별개다** → [[한정어-탈락]]

> [!note] 사용 조건 명시
> README 1067행 *"Only test systems you own or are **explicitly authorized** to assess"* + 별도 `EULA.md`.
> 공격 도구를 배포하면서 **허가 요건을 문서 본문에 박아 둔** 형태.

**운영 이력**: 2025-01-06 생성 · 2026-09-10 푸시 — **8개월 지속 운영**. 이슈 60개 관리 중.

## 관련 페이지
- [[pentagi]] · [[Claude-Red]] — 같은 도메인, 다른 형식(실행기 vs 방법론 문서)
- [[자기제한-명시]] · [[한정어-탈락]] · [[검사가능성-공사]]
