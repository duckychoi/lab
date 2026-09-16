---
title: omniget 재판정 — topics 20개 만석이 AI를 가린 사례 (볼트 판정: 제외 유지)
type: source
domain: ai-news
tags: [ai-news, github, rust, downloader, mcp, domain-judgment, metadata, vault-ruling]
created: 2026-09-16
updated: 2026-09-16
sources: []
reliability: high
---

# 재판정: tonhowtf/omniget — ★13,299

**URL**: https://github.com/tonhowtf/omniget
**지표(2026-09-16 볼트 API 실측)**: ★ **13,299** (raw 13,289 · 드리프트 **+10**) · fork **1,123** · Rust
생성 **2026-02-11** · 최종 push **2026-09-15** · 당일 **+258**

> [!note] 이 페이지의 성격
> 이것은 **채택된 소스가 아니다.** 수집기가 **제외도 채택도 하지 않고 재판정을 요청한 건**이며, 볼트가 판정을 기록하기 위해 만든 페이지다.
> 🎯 볼트 09-15 규칙 — *"놓쳐서 빠진 것"과 "확인하고 유보한 것"은 다르다* — 를 문서로 구분하기 위함이다.

## 🔴 볼트 독립 검증 — 수집기 보고가 정확하다

볼트가 GitHub API를 직접 호출해 `topics` 20개를 전수 확인했다:

```
bilibili-downloader, course-downloader, download-manager, downloader,
epub-reader, hotmart-downloader, instagram-downloader, media-downloader,
reddit-downloader, spaced-repetition, subtitle-downloader, telegram-downloader,
tiktok-downloader, twitch-downloader, twitter-downloader, udemy-downloader,
video-downloader, youtube-downloader, yt-dlp, yt-dlp-gui
```

**AI·ML·LLM·agent 계열 0개. GitHub `description` 에도 없다** (실측 원문: *"Download Udemy and Hotmart courses, YouTube videos, music and books — 1,800+ sites, no terminal..."*).
**그런데 README 본문에는 있다** — 수집기가 인용한 72행(MCP 서버·Claude Code 플러그인) · 252행 · 501행(`### AI (6)`) · 287·297행(AI 번역·문법 교정) · 445행(LLM 붙여넣기용 PDF→Markdown).

## 🎯 결정적 증거 — 저자가 이유를 직접 적었다

README 2~18행 HTML 주석:

> *"Search keywords (kept here so GitHub search, Google and **AI assistants** can find the project)... **GitHub allows 20 topics. The repository uses exactly these 20**: downloader, download-manager, ..."*

**저자는 topics 20개 상한을 인지하고, 발견성이 가장 높은 다운로더 키워드로 전부 채웠다.**
🔴 **AI 기능이 없어서 topics에 AI가 없는 게 아니라, 자리가 없어서 없다.**

> [!insight] 볼트 규칙 확장 — **필드 포화도 신호가 아니다**
> 09-15 [[gods-eye-view]] 는 *"topics 12개, AI 0개 → 실제로는 AI 에이전트가 핵심"* 이었다. 당시 볼트 결론: **필드 부재 ≠ 사실 부재.**
> 이번 건은 **정반대 조건에서 같은 결론**이 나온다 — **필드가 상한까지 가득 차 있어도** 기능 명세가 아니다.
>
> 🎯 **그리고 같은 배치의 [[pi-agent-harness]] 는 `topics` 가 0개인데 AI 에이전트 툴킷이다.**
> **0개 · 20개 만석 · 12개 부분 — 세 밀도 전부에서 topics는 기능을 말해주지 않았다.**
> 📌 **일반형**: `topics` 는 **작성자의 발견성 전략**이다. 밀도·유무 어느 쪽도 기능 신호가 아니다. → [[메타데이터-부재-추론]] 확장 등재.

## ⚖️ 볼트 판정: **제외 유지 — 단, 근거를 수집기와 다르게 적는다**

**결론은 수집기와 같고, 이유는 다르다.**

- ❌ **수집기 근거로는 부족**: *"AI 카테고리가 158개 도구 중 6개"* 는 **비중 논거**인데, [[gods-eye-view]] 도 기능 3개 중 1개였고 그건 채택 대상이었다. **비중만으로는 가를 수 없다.**
- ✅ **볼트 근거**: 🎯 **omniget의 AI는 제품의 목적이 아니라 인터페이스다.** 252행이 이를 직접 말한다 — *"each tile is one job: an isolated Rust command with JSON in and JSON out, **which is also what lets AI agents drive them through the built-in MCP server**"*. **JSON in/out 설계가 먼저 있고, MCP는 그 설계의 파생 효과다.**
  반면 gods-eye-view의 *"Hands-free voice control powered by a realtime AI agent"* 는 **AI 없이는 존재하지 않는 기능**이다.

> [!action] 볼트 규칙 (신설) — 도메인 판정 기준
> **"AI를 빼면 그 기능이 사라지는가"** 로 가른다.
> - 사라진다 → **AI 네이티브** (채택)
> - 남는다(느려지거나 불편해질 뿐) → **AI 부가** (제외)
>
> 이 기준은 **비중(몇 %)이 아니라 의존성(없으면 성립하는가)** 을 본다. 비중 기준은 [[gods-eye-view]] 와 omniget을 구분하지 못한다.

> [!warning] 볼트 자기 한계
> 볼트도 **README와 API 메타데이터까지만 읽었다. 코드를 보지 않았다.** 수집기가 밝힌 한계와 **동일한 한계**다.
> 위 판정은 **저자 서술에 대한 해석**이며, MCP 서버가 실제로 얼마나 깊이 통합됐는지는 확인하지 않았다.

## 관련 페이지
- [[gods-eye-view]] — 반대 판정 사례(부분 밀도 · AI 네이티브 · 채택)
- [[pi-agent-harness]] — topics 0개 극단(같은 배치)
- [[메타데이터-부재-추론]] — 부재·포화 양극단 확장
- [[ai-news]]

## 원본
- 출처: https://github.com/tonhowtf/omniget
- 검증: GitHub API 실호출(2026-09-16) — topics 20개 전수 · description 원문 대조 · ★+10 드리프트 확인
- 신뢰도: ⭐⭐⭐ (판정 근거 기준)
