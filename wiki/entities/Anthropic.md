---
title: Anthropic
type: entity
domain: ai-news
tags: [entity, anthropic, claude, api, agent-skills, bigtech, llm-vendor]
created: 2026-07-12
updated: 2026-10-10
sources: [claude-cookbooks.md]
reliability: high
---

# Anthropic

> [!insight] 2026-08-26 — 벤더 공식 **플러그인 레지스트리** 운영 확인 ([[claude-plugins-community]])
> `anthropics/claude-plugins-community` (⭐**1,957**·포크 181·이슈 42·Python·**Apache-2.0**·생성 2026-03-20·푸시 2026-08-25·**GitHub API 실검증**)가 트렌딩 **2위**로 관측됐다. Claude Code/Cowork용 **커뮤니티 플러그인 마켓플레이스의 read-only 미러**이며, 등록은 레포 PR이 아니라 **외부 제출 폼**으로만 이뤄진다(raw 메모 기준·README 미실측).
> **의미**: Anthropic이 **규격 제공자를 넘어 유통 채널 운영자**로 움직였다. [[에이전트-스킬]] 생태계에서 이는 **배포/레지스트리 층의 첫 벤더 사례**이며, 경쟁 축으로 [[cursor-plugins]](벤더 **규격** 배포)와 대비된다 — 한쪽은 규격, 한쪽은 목록.
> ⚠️ **스타 1,957은 이번 배치 GitHub 5건 중 최하위**인데 트렌딩 2위(당일 +351 = 절대값의 18%). *"트렌딩은 절대 스타가 아니라 증분 속도"*([[free-claude-code]] 선례)의 재확인. **심사 기준 공개 여부 미확인**이며 **등재 = 품질 보증이 아니다**.

> [!insight] 핵심 인사이트
> Claude 모델 계열(Opus·Sonnet·Haiku·Fable)과 Claude Code·Agent Skills·MCP 생태계의 개발사. 이 위키에는 그동안 **제품·생태계**([[Claude-Code-워크플로우]]·[[agent-skills]]·[[stitch-skills]]·[[superpowers]]·[[awesome-claude-code]])로 곳곳에 등장했으나 엔티티 페이지는 2026-07-12 [[claude-cookbooks]] 인제스트에서 처음 독립. Anthropic은 "모델 → Claude Code(하니스) → Agent Skills(재사용 스킬) → **cookbooks(API 실전 코드)**"로 이어지는 *풀스택 에이전트 개발 레이어*를 공식 제공하는 포지션.

## 대표 산출물 (위키 등장)
- **[[claude-cookbooks]]** — 공식 Claude API 실전 레시피 노트북(⭐48,084, MIT) *(2026-07-12 신규)*
- **[[Claude-Code-워크플로우]]** — .claude/ 설정·스킬·MCP 기반 에이전트 코딩 환경
- **[[agent-skills]]·[[stitch-skills]]·[[superpowers]]** — Agent Skills 표준·라이브러리·방법론(커뮤니티/공식 마켓플레이스)
- **[[Anthropic-Cybersecurity-Skills]]** — 보안 도메인 공식 스킬

## 관련 페이지
- [[claude-cookbooks]]
- [[Claude-Code-워크플로우]]
- [[AI-에이전트-프레임워크]]
- [[OpenAI]] — 경쟁 벤더(codex-plugin-cc로 상호운용)
- [[Zhipu AI]] · [[Alibaba]] — 오픈가중치 경쟁 진영
- [[ai-news]]

## 원본
- 조직: Anthropic (Claude 개발사)
- 대표 공식 레포: [[claude-cookbooks]](⭐48,084, MIT)
- 신뢰도: ⭐⭐⭐⭐⭐ (LLM 1차 벤더, 공식 자료)

---

## 🔄 2026-10-10 갱신 — 공식 직무별 플러그인 11종 공개

> [!insight] 산출물 갱신 — [[knowledge-work-plugins]](볼트 2026-05-25 보유 · ★14,447 → **+14,050 · +97.2% · 138일 만의 첫 재관측**)
> **★28,497**(당일 +709 · 트렌딩 6위) · fork 3,258 · Apache-2.0 · Python · created 2026-01-23 · pushed 2026-10-10
> 스킬·커넥터·슬래시커맨드·서브에이전트를 **직무 단위로 묶은 플러그인 11종**(productivity · sales · customer-support · product-management · marketing 등)을 Claude Cowork 용으로 공개하고 **Claude Code 호환**도 명시한다.
>
> 🎯 **"스킬 → 플러그인 → 직무"로 묶음 계층이 공식 공급자 쪽에서 나왔다.** 볼트 관측에서 이 층은 **3개 중 최상층**이다:
> - 스킬 단위: [[mattpocock-skills]] · [[diagram-design]] · [[rea]]
> - 하네스 제어면: [[t3code]]
> - **직무 묶음: [[knowledge-work-plugins]]** ← 본 조직
>
> ⇒ ⚖️ 10-06 *"하네스 생태계가 층으로 쌓인다"* 가설의 **보강 증거이고 반증이 아니다.** → [[하네스-설계-축]]

> [!warning] 🔴 공식 조직인데 측정이 없다
> **플러그인이 업무 품질·시간을 얼마나 바꾸는지 측정이 전혀 없다.** `topics` **0개** · `description` **1줄** → [[메타데이터-부재-추론]].
> ⚠️ **커넥터 의존이 크다** — 실행에 외부 SaaS 계정 필요(Slack · Notion · Asana · Linear · Jira · HubSpot · Intercom · Figma · Amplitude · Microsoft 365 등) ⇒ **볼트 환경에서는 대부분 돌지 않는다**(Gmail·Drive·Calendar 미인증).

> [!note] 📌 볼트 관련 모델 계보 (이번 배치 교차 확인)
> [[Learn2Play]] Table 1 에서 **Claude Opus 5.5 + OpenCode 가 최고 에이전트(Max 80.1 / Mean 61.0)** 로 측정됐고 **Claude Opus 5 는 74.5 / 53.8** 이다. 평가 모델 11종 중 이 조직 모델이 **4종**(Opus 5.5 / Opus 5 / Sonnet 5)이다.
> 🔴 단 **인간 Top-1 이 Max 에서는 더 높다**(84.3) ⇒ 지표 선택으로 순위가 뒤집힌다 → [[복합지표-분해]]

## 관련 페이지 (갱신 추가)
- [[knowledge-work-plugins]] — 신규 산출물
- [[하네스-설계-축]] — 3개 층의 최상층
- [[Learn2Play]] — 모델 성능 외부 측정
- [[에이전트-스킬]] · [[메타데이터-부재-추론]] · [[mattpocock-skills]]
