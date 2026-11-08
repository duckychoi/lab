---
title: "rivet-dev/rivet — 에이전트·세션마다 하나씩 띄우는 상태 보유 Actor. 콜드스타트 4.99ms·72KB 는 측정 조건 없는 자기보고"
type: source
domain: local-llm
tags: [local-llm, agent-memory, github-trending, actor-model, sqlite, websocket, serverless, rust, apache-2.0, 자기보고-수치]
created: 2026-11-08
updated: 2026-11-08
sources: [https://github.com/rivet-dev/rivet]
reliability: medium
---

**GitHub**: [rivet-dev/rivet](https://github.com/rivet-dev/rivet) · ★**6,798**(볼트 11-08 API · 수집기 6,769 → +29) · 포크 311 · 이슈 388 · Apache-2.0 · Rust · created **2023-06-16**(3년차) · pushed 2026-11-08

## 핵심 인사이트
> [!insight] 에이전트 메모리를 "DB에 쓰는 것"이 아니라 "프로세스로 살려두는 것"으로 본다
> Rivet Actor = 장수명 프로세스 + 인메모리 상태 + **액터별 SQLite** + WebSocket + 스케줄링. 유휴 시 S3 로 하이버네이트, 요청 시 복귀. 샌드박스/VM 이 아니라 노드 프로세스를 공유해 액터당 메모리를 줄인다. ⇒ "에이전트 1개 = 액터 1개"로 **세션·기억이 재시작을 견디는 인프라**. [[에이전트-메모리-레이어]] 논의에서 빠져 있던 **런타임 계층** 후보.

> [!warning] 성능 수치 전부 측정 조건 없음
> README 검출: 콜드스타트 **p99 4.99 ms**(4회) · **72 KB/액터**(3회) · S3 기반 SQLite 쓰기 p99 **1.07 ms** / 읽기 **1.36 ms** · 복제 SSD 대비 **10.4× 저렴**. 하드웨어·부하·액터 크기 미기재 → 비교 기준점으로 쓰지 않는다([[비매칭-비교]]).

## 도메인별 추출 (local-llm)
- **메모리 아키텍처**: 외부DB(액터별 SQLite) + 인메모리 상태. RAG 아님.
- **Hermes 적용**: 부분 YES — ChinameBot 이 사용자별 세션 상태를 장기 유지해야 한다면 "사용자 1명 = 액터 1개" 설계가 가능. 단 지금 규모(단일 봇)에선 과잉 인프라. `rivetkit` TS SDK + Vercel AI SDK 예제 있음.
- **트레이드오프**: 셀프호스트 vs Rivet Cloud. LLM 기능 없음(오케스트레이션 계층만).
- **오픈소스 구현체**: YES (Apache-2.0).

## 관련 페이지
- [[에이전트-메모리-레이어]] · [[비매칭-비교]]
- 같은 배치: [[EvoMemState]](메모리 내용 구조) ↔ rivet(메모리 런타임) · [[pipeshub-ai]]

## 원본
- 출처: https://github.com/rivet-dev/rivet
- 확인 범위: GitHub API(볼트 11-08) · README raw grep(4.99ms · 72KB · 1.07/1.36ms · 10.4× 검출) · 실행 0회
- 신뢰도: ⭐⭐ (★6.8K · 3년 운영 · 수치 무조건)
