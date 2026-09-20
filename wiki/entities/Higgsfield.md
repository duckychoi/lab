---
title: Higgsfield
type: entity
domain: video-saas
tags: [video-generation, higgsfield, cinema-studio, ai-video, 영상자동화]
created: 2026-04-10
updated: 2026-09-20
sources: [instagram-저장-2026-02-2026-04.md, AI영상자동화-SaaS-Higgsfield-2026.md]
reliability: high
---


> [!update] 2026-09-20 — **이 페이지는 5개월간 회사의 절반만 담고 있었다**
> 2026-09-20 배치로 `higgsfield-ai/higgsfield` 레포가 도착했고, 볼트가 GitHub org API 로 정체를 확인했다: **`higgsfield-ai` 의 `name` = "Higgsfield Inc." · `blog` = higgsfield.ai · `description` = "AI lab" · US.** 🎯 **이 페이지의 회사와 동일 법인이다**(수집기는 *"동명의 다른 회사"* 로 의심했고 **기각됐다**).
> 🔴 **그 org의 레포 9개를 보고 나서야 이 페이지의 공백이 드러났다** — 이 페이지는 **웹 UI 기능만** 기록해 왔다:
> - **`skills` ★1,070**(MIT · 2026-04-09 생성 · 2026-09-14 푸시) — `.claude-plugin` · `.codex-plugin` · `.cursor-plugin` **3종 하네스**, `CLAUDE.md` · `COOKBOOK.md` · `INSTALL_FOR_AGENTS.md`, 🎯 **`evals/` 디렉터리**
> - **`cli` ★555** · `homebrew-tap` · **`higgsfield-js`**(Node/TS SDK ★54) · **`higgsfield-client`**(Python SDK ★103) · **`fnf-local-pluging-bridge-mcp`**(MCP 브리지) · `cursor-plugin` ★18 · `omagotchi` ★6
> - `higgsfield` ★5,089 — **2018년 시작한 GPU 학습 오케스트레이터. 기본 브랜치 최종 커밋 2024-02-13.** 피벗 이전의 화석이다.
>
> 🎯 **해석**: 이 회사는 **웹 스튜디오 제품 + 에이전트가 호출하는 API/CLI/스킬** 두 표면을 동시에 갖고 있다. [[Vercel]] 이 *"자기 에이전트를 만들지 않고 배급 층을 가져갔다"* 와 **같은 자리**이며, ✅ **`evals/` 를 함께 낸 것은 이 축에서 드물다** → [[검사가능성-공사]].
> 📌 **볼트 [[Higgsfield-벤치마킹]] 이 UI 기능을 벤치마킹해 왔는데, 벤치마킹 대상이 UI 밖으로 나가는 중이다.**
> 상세: [[higgsfield-repo]]

# Higgsfield

AI 기반 영상 생성 스튜디오 플랫폼. 2026년 현재 **Cinema Studio 2.5**가 최신 버전. 캐릭터, 씬, 샷을 통합된 워크플로우에서 생성해 영화 제작 파이프라인 전체를 AI로 대체하는 것을 목표로 한다.

---

## 핵심 인사이트

> [!insight] 영화 제작 파이프라인 전체를 단일 도구로
> "Higgsfield Cinema Studio 2.5 creates characters, scenes, and shots — ready to turn into a film." 캐릭터 생성부터 샷 구성까지 하나의 인터페이스에서 처리. 기존엔 여러 툴을 연결해야 했던 파이프라인이 단일화됨.

> [!insight] Claude Code와 결합 시 완전 자동화 가능
> 개발자가 Claude Code + Higgsfield 조합으로 "노트북 안 건드리고 모든 것을 자동화"하는 워크플로우 구현. 콘텐츠 기획~제작~퍼블리싱 파이프라인 자동화의 최전선.

---

## 주요 기능 (Cinema Studio 2.5)

- **캐릭터 생성**: 일관된 외모의 AI 캐릭터를 프롬프트로 생성
- **씬 빌딩**: 배경, 조명, 분위기 설정
- **샷 디자인**: 카메라 앵글, 무브먼트, 트랜지션
- **시네마틱 품질**: 실제 영화 제작사 수준의 조명/구도 처리

---

## 오픈소스 대안

> [!note] 오픈소스 Higgsfield 대안 등장 (2026-04-09)
> @appinventiv4ai: "Someone just built an open-source alternative to Higgsfield. It delivers similar capabilities for generating cinematic AI videos, but without paywall." → [[오픈소스-AI-영상-도구]] 추적 필요.

---

## Claude Code + Higgsfield 자동화 워크플로우

```
Claude Code (기획/스크립트 생성)
    ↓
Higgsfield (영상 생성)
    ↓
자동 커밋 + 퍼블리시
```

포인트:
- "I'm not touching my laptop. Everything is automated."
- Claude Code가 트렌드 레이더로 콘텐츠 기획 → Higgsfield가 영상 생성 → 자동 배포
- 참고: [[Claude-Code-워크플로우]]

---

## 경쟁 포지셔닝

- [[Seedance]] — VFX 특화, 비용 경쟁력
- [[Kling]] — 캐릭터 일관성
- [[invideo AI]] — 편집 워크플로우 통합
- Runway — 전통적 AI 영상 편집

---

## 관련 페이지

- [[AI-영상-생성-2026]] — 전체 AI 영상 도구 지형도
- [[Seedance]] — 경쟁 VFX 도구
- [[Claude-Code-워크플로우]] — 자동화 파이프라인
- [[AI영상자동화-SaaS-Higgsfield-2026]] — 블로그 글 (상세 분석)

## 원본

- https://www.instagram.com/p/DW6wCibsGrA/ (@sferro21, 2026-04-09)
- https://www.instagram.com/p/DWa7efhEU4p/ (@storyboard.co.th, 2026-03-28)
- https://www.instagram.com/p/DWbk-jnE725/ (@ashoksangireddyy, 2026-03-28)
- https://www.instagram.com/p/DW6JsxriGLE/ (@appinventiv4ai, 오픈소스 대안)
- 신뢰도: ⭐⭐⭐ (공식 계정 + 다수 독립 사용자 후기)
