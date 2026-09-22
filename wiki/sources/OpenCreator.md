---
title: "OpenCreator (구 KrillinAI) — 17일 된 제품이 1년 9개월 된 레포의 별 12k를 물려받았다"
type: source
domain: ai-news
tags: [ai-news, github-trending, video-saas, codex, agent-workspace, video-translation, seedance, whisper, 하네스-설계-축, 수집기-정정]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: medium
---

# OpenCreator

> [!insight] 🎯 핵심 인사이트 — **에이전트 루프를 만들지 않고 빌린다**. 자기 몫은 "상태 기계 + 로컬 런타임"뿐이다
> README 34행: *"Instead of **reimplementing an Agent loop**, it uses **Codex CLI as the execution engine** and adds a stable local Runtime, a visual workspace, and a Desktop host around it."*
> 아키텍처 원칙(README 아키텍처 절): *"The frontend **does not launch Codex directly** and does not depend on raw Codex JSONL event formats"* · *"**Codex remains the execution source of truth** for the Agent loop, Skills, and MCP."*
> 🎯 자체 구현은 **워크플로 상태 기계**다 — 소스 입력·설정·생성·검토·수정·내보내기를 명시적 상태/이벤트로 두고, **시각 워크스페이스와 대화가 같은 상태 기계에 이벤트를 넣는다**(*"without introducing a second source of truth"*). 수정은 덮어쓰지 않고 **새 버전**을 만든다.
> 📌 [[하네스-설계-축]] 의 한 형태 — 모델도, 에이전트 루프도 바꾸지 않고 **감싸는 층만** 제품으로 만들었다. [[openai-codex]] 를 엔진으로 쓰는 제3자 제품의 볼트 첫 사례다.

> [!warning] 🔴 수집기 보강 — 개명 시점은 **2026-09-05**, 그리고 **코드베이스가 교체됐다**
> 수집기: *"개명 시점 미확인"*. 볼트 확인(GitHub API):
> - 릴리스 **v3.0.0 = "KrillinAI v3.0.0"**(2026-09-05T09:00:47Z) → **v3.0.1 = "OpenCreator v3.0.1"**(같은 날 10:34:45Z). **공개 릴리스 명칭**의 전환은 **이 1시간 34분 사이**다. ⚠️ 단 `OpenCreator` 라는 이름은 커밋 `2ea113bf`(2026-08-27, *"add OpenCreator runtime integration"*)에서 이미 내부적으로 쓰였고, **레포 URL 변경 시각 자체는 API로 확인 불가**(⬜).
> - 같은 날 05:37:59Z 커밋 `787dde73` *"Initialize KrillinAI with current project"* — **부모 커밋 0개**(루트), **+309,754줄 / −0줄**, 300파일. 🎯 **새 TypeScript 코드베이스를 루트 커밋으로 심었다.** 이전 이력(`b30c12f9`, 2026-08-20 등)은 조회 가능하지만 현재 제품은 이 루트에서 시작한다.
> - 언어 구성: TypeScript **8.88MB** · Go **0.92MB**. 구 KrillinAI(Go 영상 번역 도구)는 **내장 CLI로 남았다**(`pnpm krillinai:package` · `skills/krillinai-*`).
> - 🔴 **topics 5개가 전부 구 제품 것이다**: `dubbing` · `localization` · `tts` · `video-transcription` · `video-translation`. `codex`·`agent`·`workspace` 는 **없다** — [[메타데이터-부재-추론]] 의 역방향(**메타데이터가 비어서가 아니라 낡아서** 틀리는 경우).

> [!warning] ✅ 수집기의 "스타 상당 부분은 KrillinAI 시기" — **수치로 확인됐다**
> Wayback Machine 2026-03-21 스냅샷(`github.com/krillinai/KrillinAI`): *"**9732** users starred this repository"*, 설명 *"Video translation and dubbing tool powered by LLMs…"*.
> 🎯 현재 ★12,152 중 **최소 80.1%가 개명 5.5개월 전에 이미 있었다.** 현재 제품(Codex 워크스페이스)으로 쌓인 별은 **최대 약 2,420**이다. [[원본-파생-역전]] 과 같은 계열의 착시 — **정렬 키(스타)가 전신의 명성을 현 제품에 귀속시킨다.**

> [!warning] ⚠️ 수집기 부분 정정 — *"Codex 구독/설정 의존"*
> README 원문은 **"구독"이라 하지 않는다**: *"The Desktop package **includes Codex CLI**, but real model tasks require **a valid Codex login**"* · 언어 모델은 *"follows the **Codex model catalog or your OpenAI-compatible provider**"*. 이미지·영상·음성·전사는 별도 **Settings → AI Services** 키.
> 📌 "의존"은 맞고 "구독"은 수집기가 붙인 한정어다. Codex 로그인 방식(구독 vs API 키)별 제약은 README 범위 밖 — ⬜ 미확인.

> [!note] ✅ 수집기가 맞은 것
> - ✅ 도구 12종 중 **10 Available / 2 In development**(Auto Clips · Digital Avatar). README 본문도 *"The current release includes **ten** creator tools"*.
> - ✅ 영상 번역(클라우드/로컬 Whisper → LLM 분절·정렬·번역 → 더빙) · yt-dlp 다운로더 · 썸네일 · **GPT Image** · **[[Seedance]] 영상 생성** · 기사/샤오홍슈/쇼츠 대본 · 막대인간 애니메이션 · 스마트 더빙.
> - ✅ 개인 계정(API owner type **User**) · Apache-2.0 · TypeScript · 생성 2024-12-17.
> - 📌 **볼트 추가**: Auto Clips는 README상 "In development"지만 커밋은 이미 진행 중 — 09-10 *"feat: add video clips workflow"* · 09-11 *"optimize automatic video clipping workflow"* · 09-15 *"default video clips to source format and three outputs"*. 출하 여부는 ⬜ 미확인. [[autoclip]] 과 같은 기능을 향한다.
> - 📌 UI 언어는 **간체 중국어·영어·스웨덴어** 3종(README 65행) — README 번역본(한국어 포함 11개)과 **UI 지원 언어는 다르다.**

## 도메인별 추출 (ai-news)

> [!note] 도메인 판정
> 크리에이터 도구 10종 대부분이 영상이라 [[video-saas]] 태그를 붙이되, 제품의 새로움은 **Codex를 엔진으로 빌린 에이전트 워크스페이스 구조**(기사·샤오홍슈 작성, 개발 작업, 스케줄, 메모리 포함)에 있으므로 `ai-news` 유지. 볼트 선례([[MoneyPrinterTurbo]] · [[video-use]] = ai-news + video-saas 태그)와 같다.

- **신뢰도**: ⭐⭐ — ★12,152 · Apache-2.0 · 문서·보안 경계 서술이 구체적(daemon `127.0.0.1` 전용 + Bearer 토큰, 진단 로그 마스킹, ASAR 무결성). 🔴 단 **현 제품은 17일(v3.0.1, 09-05 이후)** 이고 별의 **80% 이상이 전신 것**이다. 예시 영상도 README가 스스로 *"produced while OpenCreator still used the KrillinAI name"* 이라 밝힌다(정직한 한정어 ✅).
- **즉시 활용**: **MAYBE** — Codex CLI 로그인이 전제. 볼트 운영자가 Claude Code 중심이면 **엔진을 갈아끼울 수 없다**(Codex가 *"source of truth"*). 개별 부품(영상 번역 파이프라인 = 구 KrillinAI CLI, `skills/krillinai-*` SKILL.md 7종)은 독립 차용 가능.
- **6개월 영향력**: 🎯 "에이전트 루프는 벤더 CLI에 맡기고, 제품은 **도메인 상태 기계 + 버전 관리**만 만든다"는 패턴이 크리에이터 도구로 내려왔다. 스케줄마다 **전용 대화 스레드**를 두고 50회 Run마다 Codex 스레드를 **로테이션**(`OPENCREATOR_CODEX_THREAD_ROTATION_RUN_THRESHOLD=50`)하는 설계는 장기 실행 에이전트의 컨텍스트 관리 실례다.
- **대체 관계**: [[MoneyPrinterTurbo]](쇼츠 자동 생성) · [[autoclip]](하이라이트 클리핑, 개발 중)과 겹친다. 반대로 Codex에 **종속**되므로 [[openai-codex]] 를 대체하지 않고 그 위에 앉는다.
- **허와 실**: 실 = 상태 기계 기반 대화/GUI 동기화 · 버전 보존 · 로컬 우선 보안 경계. 허 = **"12k 스타 = 현 제품 인기"** 라는 인상(80%+ 전신 몫) · 지원 모델 로고 표는 README 스스로 *"examples; actual availability depends on your credentials"* 라 한정.
- **액션**: 아래.

> [!action] 당장 할 것
> 전체 설치 대신 `skills/krillinai-subtitle/SKILL.md` · `krillinai-pipeline/SKILL.md` 2개만 읽고, **"dry-run으로 다단계 계획을 검증한 뒤 단계별 스킬로 실행"**(Pipeline Plan 설명) 구조가 [[reat]] 스킬군의 `reat-new → reat-chunk → reat-scene` 체인에 이식 가능한지 판단한다.

## 관련 페이지
- [[KrillinAI]]  *(09-22 연결)*
- [[openai-codex]]
- [[openai-whisper]]
- [[Seedance]]
- [[autoclip]]
- [[MoneyPrinterTurbo]]
- [[video-use]]
- [[reat]]
- [[하네스-설계-축]]
- [[에이전트-스킬]]
- [[메타데이터-부재-추론]]
- [[원본-파생-역전]]
- [[video-saas]]
- [[ai-news]]

## 원본
- 출처: https://github.com/krillinai/OpenCreator (구 URL `krillinai/KrillinAI` → 301 리다이렉트, repository id 904490600) · homepage open-creator.ai
- 볼트 실측(2026-09-22, GitHub API): ★**12,152**(raw 11,999 → +153) · fork **1,233**(raw 1,200) · **Apache-2.0** · TypeScript · owner **User** · open issues **31**(raw 완전일치) · created 2024-12-17T01:59:22Z · pushed 2026-09-22T07:11:30Z · default branch `master` · topics 5(전부 구 제품)
- 릴리스: v2.1.0(2026-06-17) → **v3.0.0 "KrillinAI"(09-05 09:00Z)** → **v3.0.1 "OpenCreator"(09-05 10:34Z)** → … → v3.2.2(09-21)
- 과거 스타: Wayback 2026-03-21 스냅샷 **9,732**
- 수치 출처: README 전문 616행 · 커밋 `787dde73`(루트, parents 0) · `/languages` · `/releases` · Wayback CDX
- raw 대비: 볼트 추가 = 🎯 **개명 시점 확정(2026-09-05, 1시간 34분 창)** · 🎯 **루트 커밋으로 코드베이스 교체** · ✅ **"스타 대부분 전신" 수치 확인(≥80.1%)** · 🔴 **topics 전부 구 제품** · ⚠️ **"구독" 한정어는 README에 없음** · 📌 Auto Clips 코드 진행 중
- 신뢰도: ⭐⭐ (문서 구체적·한정어 정직 / 현 제품 17일 · 별 귀속 착시 · Codex 종속)
