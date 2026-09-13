---
title: PentAGI — 자율 침투테스트 에이전트 시스템
type: source
domain: ai-news
tags: [ai-news, github-trending, security, offensive-security, agent, sandbox, go, 한정어-탈락]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [vxcontrol/pentagi]
---

# PentAGI — 자율 침투테스트 에이전트 시스템

**GitHub**: https://github.com/vxcontrol/pentagi · `vxcontrol/pentagi`
**지표(2026-09-13 API 실호출)**: ⭐**23,624** · fork **3,076** · 이슈 **60** · **Go** · **MIT**
**생성 2025-01-06 · 최종 푸시 2026-09-10** — 8개월 된 레포다(신생 아님)
**드리프트**: raw ⭐23,621 vs API **23,624**(+3) → API값 채택. fork·이슈·언어·라이선스 **전건 일치**

> [!insight] 핵심 인사이트 — **레포가 자기 설명을 19행 뒤에서 스스로 부인한다**
> GitHub description과 README 63행은 *"**Fully Autonomous**"* 다. 그런데 **82행 `### Current Capability Boundaries`** 섹션이 이렇게 적는다(원문 84~85행 실측):
> - *"PentAGI today is an autonomous **and assistant-guided** penetration testing platform, **not** a CALDERA-style Breach and Attack Simulation (BAS) or adversary emulation product with predefined campaigns or attack plans."*
> - *"BAS-like agent-authored attack scripts should be treated as **conceptual or future work, not as a feature that is implemented today**."*
>
> 🎯 **"완전 자율"을 부인하는 주체가 경쟁자도 리뷰어도 아니라 레포 자신이다.** 그리고 그 부인은 **주장으로부터 19행 거리**에 있다. 헤드라인만 읽는 독자와 한 화면 더 내린 독자가 **다른 제품을 보게 된다** → [[한정어-탈락]]의 구조적 사례.

> [!note] 실제 구조 — 샌드박스 + 툴 위임
> Docker 샌드박스 안에서 nmap·metasploit·sqlmap 등 **20+ 보안 툴**을 LLM 에이전트가 위임 구조로 호출하는 자가호스팅 플랫폼. LLM 공급자 **10종+ 교체 가능**. 실행 모니터링과 태스크 플래닝은 *optional*(63행)로 표기된다.

> [!warning] 사용 조건이 명시되어 있다
> README **1067행**: *"Only test systems you own or are **explicitly authorized** to assess."* 별도 `EULA.md` 존재.
> → 이 레포는 **허가된 대상 한정** 도구다. 볼트는 이 조건을 페이지에 고정해 둔다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐23,624 · MIT 본문 확인 · 8개월 운영 · 푸시 3일 전 → **high**
- **즉시 활용**: **NO.** 허가된 침투테스트 대상이 없으면 실행 자체가 규약 위반이다. 구조 참고만.
- **6개월 영향력**: 툴 위임 + 샌드박스 격리 패턴은 보안 외 도메인(데이터 파이프라인)에도 이식 가능한 형태다.
- **허와 실**: *"Fully autonomous"* 는 **레포 자신이 부인한다.** 실제는 **자율 + 어시스트 혼합**이고 BAS는 미구현.
- **액션**: 아키텍처(에이전트↔툴 위임 경계) 읽기. 실행 금지.

> [!question] 미해결
> 20+ 툴의 실제 목록과 위임 프로토콜은 README 밖(소스)에 있다. "어떤 단위로 에이전트에 권한을 주는가"가 [[검사가능성-공사]] 관점의 핵심인데 미확인.

## 관련 페이지
- [[Claude-Red]] — 같은 배치 공격보안. **둘의 차이: PentAGI는 실행기, Claude-Red는 방법론 문서다**
- [[한정어-탈락]] · [[자기제한-명시]] · [[검사가능성-공사]]
- [[에이전트-스킬]]

## 원본
- 출처: https://github.com/vxcontrol/pentagi
- 신뢰도: ⭐⭐⭐ (API 실호출 + README 63/82/84/85/1067행 원문 대조)
