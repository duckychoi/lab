---
title: "OpenMausBot — 로컬 CLI 에이전트를 채팅 연락처로 묶는 데스크톱 앱"
type: source
domain: ai-news
tags: [ai-news, agent, desktop-app, orchestration]
created: 2026-11-01
updated: 2026-11-10
sources: [https://github.com/milind-soni/OpenMausBot]
reliability: medium
---

**GitHub**: https://github.com/milind-soni/OpenMausBot · ★**9,989** · fork 1,385 · Apache-2.0 · 생성 2026-08-11 · 푸시 2026-11-01T09:08Z (GitHub API 2026-11-01)

## 핵심 인사이트
> [!insight] 새 에이전트가 아니라 기존 구독을 묶는 껍데기다
> 봇마다 로컬 `claude`·`codex`·`grok` CLI, 모델, 컴퓨터, 연결 앱을 따로 둔다. 기존 로그인을 그대로 쓰고 중간 프록시가 없다고 밝힌다. 구독료를 새로 내지 않고 Grok Bot 같은 형태를 흉내 내는 것이 판매 논리다.

> [!warning] 권한 범위와 요약 정정
> - 수집기 "Claude 또는 Codex"는 좁다. README는 **Grok CLI와 임의 CLI 바이너리**까지 적는다.
> - 봇에 **자기 컴퓨터 제어**를 줄 수 있고(macOS · Ubuntu Xorg 옵트인, Wayland는 #345로 비활성), Composio 앱 500개 이상이 붙는다. 승인 카드가 있어도 권한 면적은 넓다.
> - `boat.dev`는 README의 sponsors 자산 경로로 보아 후원사로 보인다. 클라우드 컴퓨터와의 관계는 볼트도 확인하지 못했다(추정).
> - 측정 수치는 README에 없다. 생성 약 3개월로 이력이 짧다.

## 도메인별 추출
- **즉시 활용**: 보류. [[Claude-Code-워크플로우]]를 이미 터미널로 쓰고 있어 얻는 것은 UI다.
- **대체 관계**: [[t3code]] · [[thinkrail]] · [[Orkas]]와 같은 "에이전트 GUI" 축이다.
- **액션**: 지금은 없음. 텔레그램으로 이미 같은 형태를 쓰고 있다면 우선순위가 낮다.

## 관련 페이지
- [[Orkas]] · [[t3code]] · [[Claude-Code-워크플로우]] · [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/milind-soni/OpenMausBot
- 확인 범위: GitHub API · README · 🔴 앱 미실행
- 신뢰도: ⭐⭐ (★9,989 · 이력 짧음 · 수치 없음)

## 🔄 2026-11-02 갱신 (인제스트 2026-11-02) — ★10,902 · **클라우드 컴퓨터 = boat.dev 확인(추정 해소) · "no crypto" 경고 · 매일 릴리스**

**GitHub API 실측(11-02 09시대)**: ★**10,902**(수집기 10,901 · +1 드리프트) · fork 1,487 · open_issues **649**(이슈+PR 합산) · Apache-2.0 · TypeScript · created 2026-08-11 ✅ · pushed 2026-11-02T08:45Z · 최신 릴리스 **v0.1.138(11-02)** · v0.1.137(11-01) · v0.1.136(10-31)
- 📈 볼트 마지막 기록 ★9,989(11-01) → **+913 / 1일**(수집기 당일 +922와 근접).
- 저장소 description: *"Open-source Grok Bot alternative with a virtual machine that bots can use"*.
- ✅ 수집기 서술 확인: Electron(README 17·244·260행) · Grok Bot 대안(5·9행) · 봇마다 모델·클라우드 컴퓨터·연결 앱(11~12행) · 중요한 동작 승인(13·138행 "permission broker") · **암호화폐 무관 경고**(69행: 토큰 없음, 동명 코인은 무관, 보증 안 함).
- ⚖️ 수집기 서술 범위: README 11행은 "Claude or Codex"라 쓰지만 78행은 `claude`·`codex`·`grok` CLI를 적는다(11-01 정정 유지). v0.1.138 노트에 "Copilot Auto" 처리 PR(#4044)도 있다 — Copilot 지원 범위는 🔴 미확인.
- 🆕 **11-01 페이지의 "boat.dev 관계 추정" 해소**: README 262행 *"Boat (boat.dev) — Each bot's cloud computer · our sponsor"*, 292행 아키텍처 도식 `server -- "Boat API" --> Cloud computer (boat.dev)`. 즉 **봇의 클라우드 데스크톱은 후원사 boat.dev가 제공**한다. "local-first"(81행: 하네스 서버는 127.0.0.1, 기록·키는 `~/.openmausbot`)와 별개로 클라우드 컴퓨터 경로에서는 작업 내용이 boat.dev로 간다.
- ⚖️ 수집기 누락: 키 관리 — API 키를 앱 설정에 붙여넣으면 로컬에 저장되고 공급자 전체에 핫리로드된다(167~169행). 최근 릴리스는 **비밀값 마스킹 보강**(GitLab 토큰, Authorization Basic 자격증명 — #3926·#3985)이 이어지고 있어, 로그·내보내기에서 비밀 누출 차단이 아직 다듬어지는 단계로 보인다(볼트 해석).

> [!warning] 이력 3개월 · 하루 1회 이상 배포 · 이슈+PR 649
> 자기 컴퓨터 제어(macOS·Ubuntu Xorg 옵트인) + Composio 500+ 앱 + 외부 클라우드 VM이 한 앱에 묶인다. 측정 수치는 여전히 README에 없다. 액션은 11-01과 같이 **보류**.

## 🔄 2026-11-10 갱신 (인제스트 2026-11-10) — ★20,210 · **8일 만에 약 2배** · 이슈+PR 983

**GitHub API 실측(11-10 09:06Z)**: ★**20,210**(수집기 20,204 · +6 드리프트) · fork 2,773 · open_issues **983** · Apache-2.0 · TypeScript · pushed 2026-11-10T09:05Z(조회 1분 전)
- 📈 볼트 마지막 기록 ★10,902(11-02) → **+9,308 / 8일**(일평균 약 1,160 · 수집기 당일 +1,587). fork 1,487 → 2,773.
- 🔴 open_issues **649 → 983(+334 / 8일)** — 스타와 같은 속도로 미해결 표면이 는다. 11-02 경고("이력 3개월 · 하루 1회 이상 배포") 유지.
- 수집기 서술 중 볼트 기존 확인과 겹치는 것: 로컬 CLI(`claude`/`codex`/`grok`) · 승인 카드 · 127.0.0.1 하네스 · `~/.openmausbot` · Wayland 호스트 제어 비활성(#345). **신규 서술**: 격리 로컬 VM 옵션 · 팀 모드 개발 중 — 볼트 README 미재열람(수집기 판독 기준).
- ⚖️ 수집기 "중간 프록시 없음"은 로컬 CLI 경로 한정이다. 11-02 볼트 확인대로 **클라우드 컴퓨터 경로는 후원사 boat.dev 로 작업이 나간다.** 오늘 요약에는 이 구분이 빠졌다.
- 액션: 보류 유지. 이 볼트 사용자는 이미 텔레그램으로 같은 형태를 쓰고 있다.
