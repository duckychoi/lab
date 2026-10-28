---
title: "nightly-labs/openbot — 7개 코딩 에이전트 CLI를 '팀원'으로 묶는 데스크톱 앱. 무승인 전권 실행 + 공개 8일 만에 비상업 라이선스로 전환"
type: source
domain: ai-news
tags: [ai-news, github-trending, multi-agent, agent-orchestration, desktop-app, claude-code, codex, computer-use, 라이선스-전환, source-available, 권한]
created: 2026-10-28
updated: 2026-10-28
sources: []
reliability: medium
---

# nightly-labs/openbot (OpenBot)

**GitHub**: https://github.com/nightly-labs/openbot · ★**2,787** · fork 279 · open issues(PR 포함) **247** · created 2026-08-12 · pushed 2026-10-28T09:01:05Z · 최신 릴리스 **v0.52.1**(10-27) · 볼트 관측 2026-10-28T09:10Z
**라이선스**: README·LICENSE = **PolyForm Noncommercial 1.0.0** · GitHub API `license.spdx_id` = **NOASSERTION**(SPDX 자동판별 실패. 수집기는 README 표기를 옮겼고 그 자체는 맞다)
**저작권자**: Synthetify Labs sp. z o.o.(폴란드 유한회사) · 외부 기여자는 **저작권 양도 계약(CLA)** 서명 필요
**신뢰도**: ⭐⭐ medium

> [!insight] 🏆 핵심 인사이트: **"로컬 우선 AI 팀원" 앱인데 실제 구조는 '무승인 전권 에이전트 + 클라우드 계정/결제 + 저작권 집중'이다**
> 1. **경고는 수집기도 전했다**: *"Agents currently run with `danger-full-access` and `approvalPolicy: never`… without per-action confirmations after the explicit first-launch consent."* README Security 절은 한 발 더 나간다: *"Full local access is an explicit current product decision, **not a security boundary**."* 즉 격리는 제품 목표가 아니라고 스스로 밝힌다 → [[자기제한-명시]].
> 2. 🔴 **수집기가 빠뜨린 것 1: 라이선스는 처음부터 비상업이 아니었다.** LICENSE 커밋 이력: 08-12 *"Prepare repository for public release"* → **08-20 "Change license to PolyForm Noncommercial"**(공개 **8일 후**) → 10-16 *"Name Synthetify Labs as the licensor and add a commercial contact"*. README: *"Versions up to and including **0.1.11** remain available under **Apache-2.0**."* ⇒ 0.1.11 이하 코드는 지금도 Apache-2.0로 포크할 수 있다.
> 3. 🔴 **수집기가 빠뜨린 것 2: 상용화 배관이 이미 깔려 있다.** 명령표에 `api:stripe:bootstrap`(Stripe 요금제 카탈로그·Customer Portal) · `hosting:setup`(호스팅 서버) · Cloudflare Workers + D1 계정 API · 모바일 앱(Expo) · WebRTC 팀 공유(coturn 릴레이)가 있다. 비상업 라이선스 + CLA(저작권 양도) + Stripe ⇒ **오픈코어/듀얼 라이선스 판매 구조**다. [[Prime-Radiant]]([[superpowers]])의 "MIT + 기업 지원"과는 반대 방향이다. 코드를 닫고 상용 라이선스를 판다.
> 4. 📌 **"local-first, not offline-only"**: 채팅·파일·명령은 로컬(Cloudflare가 *"does not carry chats, files, commands, or remote desktop media"*)이지만 계정·설정·멤버십·초대·세션 기록은 Cloudflare에 저장된다. 모바일 분석(OpenPanel)도 있다.

> [!warning] 🔴 공급망 주의 (README 원문 기준)
> - 앱이 각 공급자 CLI를 **직접 다운로드해 고정(pin)** 하고 *"checks for a newer provider CLI release at startup and every hour… Updates install the latest upstream release"* 한다. `native-runtime.lock.json` 버전은 *"only the first-install fallback"* 이다. ⇒ **고정 버전은 첫 설치용일 뿐이고, 이후에는 매시간 최신 업스트림을 받는다.** 무승인 실행과 겹치면 업스트림 CLI 변경이 확인 없이 전권으로 돈다.
> - Computer Use는 릴리스에 포함된 `cua-driver` 바이너리를 자식 프로세스로 띄워 **모든 공급자에게** 준다(볼트 [[trycua-cua]] 계열로 보이나 동일 프로젝트인지 미확인). 이쪽은 SHA-256 검증(`prepare:cua-driver`)이 명시돼 있다.
> - 릴리스 속도: v0.50.0(10-25) → v0.52.1(10-27), **사흘 동안 4개**. 공개 2.5개월에 0.52까지 왔다. 개발 프리뷰라는 자기 규정과 맞는다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — ★2,787(당일 +777 수집기) · 이슈 247 · CI 배지 · 서명된 macOS/Windows 빌드. 활동은 매우 활발하다. 실사용 후기·벤치마크는 없다.
- **지원 하니스**: Codex(App Server) · Claude Code · Grok CLI · OpenCode · Gemini(Antigravity ACP 서버, 구글 라이선스 때문에 앱이 대신 다운로드) · Cursor CLI · Cline CLI(ACP) + 사용자 정의 OpenAI 호환 엔드포인트(Ollama·LM Studio 감지). 수집기 목록 일치 ✅.
- **즉시 활용**: **NO.** ① 무승인 전권 실행 ② 비상업 라이선스(내 SaaS·업무 사용이 "noncommercial"에 해당하는지 불명확) ③ Claude 구독 사용에 대해 README가 별도 `docs/provider-terms.md`를 가리킨다(구독 약관 문제가 있다는 신호로 보이나 **문서 미열람**).
- **6개월 영향력**: 중간. "에이전트마다 독립 워크스페이스(`~/OpenBot/Agents/<id>`) + 공유 폴더 + 해시 매니페스트가 붙은 파일 전송 + FIFO 큐 + 채널에서 작업 소유자 1명·명시적 위임" 설계는 멀티 에이전트 조정의 참고 모델이다. [[paperclip]](회사 모델)·[[multica]](매니지드 플랫폼)과 같은 층이다. 차이점은 **기존 벤더 CLI를 그대로 프로세스로 띄우고 자격증명을 복사하지 않는다**는 것(*"uses the existing local CLI login. It does not copy provider credentials"*)이다.
- **대체 관계**: [[hermes-agent]]처럼 자체 에이전트를 만드는 대신 **기존 CLI 위의 관리 계층**이다. [[하네스-설계-축]] 관점에서는 하네스 바깥의 "하네스 묶음(meta-harness)" 층이다.
- **허와 실**: "persistent AI teammates"의 실체는 **장기 세션 + 자동 컨텍스트 압축 + 큐**다. 수집기 요약은 기능 목록과 위험 경고를 정확히 옮겼다. 빠진 것은 라이선스 전환 이력·CLA·Stripe 상용 배관·매시간 자동 업데이트 네 가지다. 이 네 가지가 "써도 되나"를 판단할 때 더 중요하다.
- **액션**: 설치하지 않는다. 설계 문서만 읽을 가치가 있다: `docs/architecture/`(공급자 어댑터) · 메시징·전송 매니페스트 포맷. 꼭 실험해야 한다면 Apache-2.0인 **v0.1.11 태그**를 기준으로 하고, [[sandbox-runtime]] 같은 OS 격리 안에서 돌린다.

> [!question] 미해결
> - `docs/provider-terms.md`(Claude 구독 관련) 내용 미열람.
> - `cua-driver`가 [[trycua-cua]]의 산출물인지 미확인.
> - open issues 247은 PR 포함 수치다. 이슈/PR 비율은 세지 않았다.

## 관련 페이지
- [[paperclip]] · [[multica]] · [[hermes-agent]] · [[opencode]] · [[cline]] · [[trycua-cua]] · [[sandbox-runtime]]
- [[하네스-설계-축]] · [[자기제한-명시]] · [[AI-에이전트-프레임워크]] · [[Claude-Code-워크플로우]]
- [[Anthropic]] · [[OpenAI]] · [[Prime-Radiant]] (상용화 방향 대비)
- 같은 배치: [[superpowers]] · [[ai-design-skills]] · [[hallmark]] · [[impeccable]]
- [[ai-news]]

## 원본
- 출처: https://github.com/nightly-labs/openbot
- 볼트 실측(GitHub API, 2026-10-28T09:10Z): ★2,787 (수집기 2,780 → **드리프트 +7**) · fork 279 · issues 247 · license API NOASSERTION / README PolyForm-NC-1.0.0 · created 2026-08-12 ✅ · pushed 2026-10-28T09:01:05Z
- 확인 범위: README 55,726B 중 개요·What works·Agent setup·로컬 데이터·Security·Releases·Contributing·License 절, LICENSE 커밋 3건, 릴리스 5건. 🔴 코드 미독 · 🔴 미실행.
- 신뢰도: ⭐⭐
