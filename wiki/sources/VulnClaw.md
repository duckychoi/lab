---
title: Unclecheng-li/VulnClaw — MCP+침투 스킬 결합 자율 보안 에이전트
type: source
domain: ai-news
tags: [ai-news, github-trending, security, pentest, ai-agent, mcp, ctf]
created: 2026-07-02
updated: 2026-07-02
sources: []
reliability: medium
---

# VulnClaw (Unclecheng-li/VulnClaw)

> [!insight] 핵심 인사이트
> ⭐1,692 (2026-07-02, 당일 +132). **LLM + MCP 툴체인 + 구조화된 침투 스킬**을 결합해 보안 평가를 자동화하는 자율 침투 테스트 에이전트. 자연어 지시 하나로 *정보수집 → 취약점 발견 → 취약점 이용 → 리포트 생성* 전 과정을 오케스트레이션한다. 설계상 두 가지가 눈에 띈다 — ①**목표 지향 solving 엔진**(고정 반복 횟수가 아니라 초기 상태→목표를 향해 탐색), ②**증거 기반 환각 게이트**(주장한 취약점을 실제 툴 출력과 대조 검증). CTF·OSINT 정찰·고급 웹 보안 등 **21개 내장 스킬**, 13개 LLM 프로바이더 + Chrome DevTools·Burp Suite MCP 연동, CLI/TUI/REPL/웹 대시보드 인터페이스. **MIT**. [[strix]](자율 보안·침투 에이전트)와 같은 계보의 후발 주자.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ⭐1.7K로 [[strix]](⭐28K+)보다 초기 단계. 단 "증거 기반 환각 게이트"는 에이전트 신뢰성의 핵심 설계로 [[Dockerless]]의 "증거로 판정" 철학과 공명, 개념적 가치는 큼.
- **즉시 활용**: MAYBE(방어·학습) — **인가된 환경 한정**. 내 서비스의 자체 취약점 스캔·CTF 학습·MCP 오케스트레이션 구조 참고용. 무단 타깃 사용 금지(레포도 명시).
- **6개월 영향력**: 중간 — "AI 에이전트가 침투 테스트 전 과정을 수행"하는 DevSecOps 흐름을 [[strix]]와 함께 밀어올림. MCP(Burp/Chrome) 연동은 실무 도구 통합의 좋은 레퍼런스.
- **대체 관계**: 수동 침투 테스트 워크플로 일부를 에이전트로 대체·보조. [[strix]]와 직접 경쟁.
- **허와 실**: 자율 익스플로잇은 오탐·과신 위험이 크다. "증거 게이트"가 있어도 실제 익스플로잇 성공률·오탐률은 미검증. 21개 스킬의 깊이도 확인 필요.
- **액션**: MCP(Burp Suite·Chrome DevTools) + 목표지향 solving + 증거 게이트의 **아키텍처 3요소만 추출** → 자체 방어용 에이전트 설계에 참고. 실행은 반드시 인가된 자체 자산에서만.

> [!warning] 신뢰도·안전 주의
> 자율 침투 에이전트는 **인가된 보안 테스트·CTF·연구 목적에 한정**. 무단 시스템 침투는 불법(레포도 명시). 자율 익스플로잇의 오탐·부작용 위험을 감안해 격리 환경에서만 실험할 것.

## 관련 페이지
- [[strix]]
- [[Dockerless]]
- [[ai-news]]

## 원본
- 출처: https://github.com/Unclecheng-li/VulnClaw
- 스타: ⭐1,692 (2026-07-02, 당일 +132)
- 구성: 21 침투 스킬 · 13 LLM 프로바이더 · MCP(Burp/Chrome) 연동 · CLI/TUI/REPL/웹 · MIT
- 신뢰도: ⭐⭐ (초기 단계, 증거 기반 게이트 설계는 유의미 — 익스플로잇 성능 미검증)
