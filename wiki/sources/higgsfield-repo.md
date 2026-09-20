---
title: "higgsfield(레포) — 볼트가 8개월 추적해 온 영상 회사의 버려진 첫 제품이었다"
type: source
domain: ai-news
tags: [ai-news, github, higgsfield, gpu-orchestration, 트렌딩-노이즈, 피벗, 스킬-배급]
created: 2026-09-20
updated: 2026-09-20
sources: []
reliability: medium
---

# higgsfield (higgsfield-ai/higgsfield)

> [!warning] 🔴 수집기 가설 기각 — **"동명의 다른 회사"가 아니다. 같은 회사다.**
> 수집기 raw: *"**동명의** AI 영상 회사(Higgsfield AI) 인지도 유입으로 의심되며, 코드 자체의 신규성 근거는 찾지 못했다."*
> 🔴 **볼트 실측(GitHub org API): `higgsfield-ai` 의 `name` = "Higgsfield Inc." · `blog` = **higgsfield.ai** · `description` = "AI lab" · location = United States of America.**
> ✅ **볼트가 2026-04-10부터 추적해 온 [[Higgsfield]](Cinema Studio) 와 동일 법인이다.** 동명이인 혼동이 아니라 **같은 회사의 폐기된 첫 제품**이다.
> 🎯 **가설의 방향이 반대였다**: "외부 인지도가 무관한 레포로 흘러들었다"가 아니라 **"회사의 현재 인지도가 자사의 옛 레포로 돌아왔다"** 이다.

> [!insight] 🎯 그래서 진짜 발견은 트렌딩이 아니라 **볼트 [[Higgsfield]] 페이지의 공백**이다
> org 레포 **9개**를 전수 열람한 결과, 볼트가 8개월간 "영상 SaaS"로만 기록해 온 회사가 **에이전트 표면을 갖추고 있었다**:
> - **`skills` ★1,070**(MIT · created 2026-04-09 · pushed 2026-09-14) — `.claude-plugin` · `.codex-plugin` · `.cursor-plugin` **3종 하네스 동시 지원**, `CLAUDE.md` · `COOKBOOK.md` · `INSTALL_FOR_AGENTS.md`, 그리고 🎯 **`evals/` 디렉터리**
> - **`cli` ★555**(pushed 2026-09-18) · `homebrew-tap` · `higgsfield-js`(Node/TS SDK) · `higgsfield-client`(Python SDK) · `fnf-local-pluging-bridge-mcp`(MCP 브리지)
>
> 📌 **볼트 [[Higgsfield]] 엔티티는 `updated: 2026-04-10` 에서 멈춰 있고 CLI·SDK·skills·MCP 를 한 줄도 담고 있지 않다.** 이번 배치가 준 것은 트렌딩 레포가 아니라 **그 공백의 발견**이다.
> 🎯 **그리고 이건 [[Vercel]] 과 같은 자리다** — 자기 제품을 에이전트에서 호출 가능하게 만들고 스킬로 배급한다. [[mem0]]·[[Vercel]]·[[SnailSploit]] 에 이은 **스킬 배급 축 5번째**이고, ✅ **`evals/` 를 함께 낸 것은 이 축에서 드물다**([[vercel-skills]] 배지 자기보고 · [[CloddsBot]] 검증 불가와 대비) → [[검사가능성-공사]].

> [!note] 📌 레포 자체 — 정지 상태는 맞다
> ★**5,089**(raw 5,087 → **+2**) · fork **926** · **Apache-2.0** · Jupyter Notebook · created **2018-05-26** · **open issues 13**(수집기 분해 이슈 6 / PR 7 **합계 일치**)
> **기본 브랜치 최종 커밋 = 2024-02-13T18:45:37Z**(`Update llama.py`) — 볼트가 커밋 API로 직접 확인. **2년 7개월 정지** ✅ 수집기 정확.
> ⚠️ **다만 `pushed_at` 은 2026-09-14T02:46:36Z 다** — 즉 **비기본 브랜치/태그 쪽에 최근 푸시가 있다.** `pushed_at` 을 활동 지표로 쓰면 이 레포는 "이번 주에 작업 중"으로 보인다. 🔴 **`pushed_at` ≠ 기본 브랜치 커밋.** 볼트 규칙으로 승격할 것.
> 내용: ZeRO-3 DeepSpeed API · PyTorch FSDP · 노드 할당/큐잉 · GitHub Actions 연동. `topics` 9개가 전부 학습 인프라 계열(`llama2` · `mlops` · `cluster-management`) — **영상과 한 글자도 겹치지 않는다.** 피벗의 화석.

> [!warning] ⚠️ 트렌딩 +196의 원인은 여전히 미확정
> ★ 당일 **+196 / 5,087 = 3.85% — 배치 상대속도 1위**이고 2위([[docling]] 0.013%)의 **약 300배**다.
> 🔴 볼트가 확인한 것: **같은 회사다 · 기본 브랜치는 2년 7개월 정지다 · 비기본 브랜치 푸시가 있다.**
> 🔴 볼트가 **확인하지 못한 것**: 그 푸시의 내용, 그리고 ★+196 이 **회사 인지도 유입인지 · 최근 푸시 때문인지 · 외부 언급 때문인지**. **원인은 모른다.** 수집기의 "노이즈" 판정도, 그 반대도 지금은 근거가 없다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ — org 정체·커밋 이력·레포 목록은 **API 실측**. 트렌딩 원인은 **미확인**.
- **즉시 활용**: 🔴 **이 레포는 NO**(2년 7개월 정지 · PyPI 0.0.3). ✅ **`higgsfield-ai/skills`·`cli` 는 YES 후보** — 볼트가 [[Higgsfield]] 를 실제로 쓰는 워크플로가 있다면 **CLI/SDK/MCP 브리지가 자동화 경로**다. 09-18 배치의 [[하네스-설계-축]] 과 직결.
- **6개월 영향력**: 🎯 **영상 SaaS가 "웹 UI 제품"에서 "에이전트가 호출하는 API + 스킬"로 이동 중**이라는 신호. 볼트 [[Higgsfield-벤치마킹]] 이 UI 기능을 벤치마킹해 왔는데, **벤치마킹 대상 자체가 UI 밖으로 나가고 있다.**
- **대체 관계**: 학습 오케스트레이터로서는 이미 대체됨(DeepSpeed·FSDP 직접 사용 · Ray 등).
- **허와 실**: 🔴 **"트렌딩 = 신규성"이 아니다**가 이번 건의 교훈이고, **"트렌딩 = 노이즈"도 아니다.** 둘 다 원인 주장이며 볼트는 원인을 못 봤다.
- **액션**: `higgsfield-ai/skills` 의 `evals/` 를 열어 **영상 SaaS가 자기 스킬을 무엇으로 검증하는지** 본다. 이 축에서 evals를 낸 사례가 거의 없다.

> [!action] 당장 할 것
> **[[Higgsfield]] 엔티티를 갱신한다**(5개월 정지 중이었다) — CLI ★555 · skills ★1,070 · JS/Python SDK · MCP 브리지. → 이번 인제스트에서 반영 완료.

> [!question] 미해결 질문
> 1. ★+196 의 **원인** — 미확인.
> 2. `pushed_at` 2026-09-14 의 **푸시 내용** — 비기본 브랜치 미열람.
> 3. `skills` 레포의 `evals/` **내용과 규모** — 목록만 봤다.

## 관련 페이지
- [[Higgsfield]]
- [[Higgsfield-벤치마킹]]
- [[Vercel]]
- [[mem0]]
- [[검사가능성-공사]]
- [[하네스-설계-축]]
- [[상대속도-가림]]
- [[ai-news]]

## 원본
- 출처: https://github.com/higgsfield-ai/higgsfield
- 볼트 실측(2026-09-20, GitHub API): ★**5,089**(raw 5,087, +2) · fork 926 · **Apache-2.0** · Jupyter Notebook · open issues **13**(이슈 6/PR 7 합계 일치) · created 2018-05-26T22:47:43Z · **pushed 2026-09-14T02:46:36Z** · **기본 브랜치 최종 커밋 2024-02-13T18:45:37Z** · topics 9
- org 실측: `higgsfield-ai` → name **"Higgsfield Inc."** · blog **higgsfield.ai** · description "AI lab" · US · **public_repos 9**(cli ★555 · skills ★1,070 · higgsfield ★5,089 · higgsfield-client ★103 · higgsfield-js ★54 · cursor-plugin ★18 · fnf-local-pluging-bridge-mcp ★7 · omagotchi ★6 · homebrew-tap ★1)
- raw 대비: 🔴 **"동명의 다른 회사" 가설 기각 — 동일 법인 확인** · **볼트 [[Higgsfield]] 페이지의 5개월 공백 발견(CLI/SDK/skills/MCP)** · **`pushed_at` ≠ 기본 브랜치 커밋 규칙화** · ⚠️ **★+196 원인은 볼트도 모름**
- 신뢰도: ⭐⭐ (정체·이력 실확인 / 트렌딩 원인 미확정)
