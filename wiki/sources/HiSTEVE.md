---
title: "HiSTEVE 1.0 — 키보드·마우스만 쓰는 Minecraft 계층형 VLA. OpenHA 'SOTA' 37.4% 는 기준선 대비 +0.6%p, 하네스는 원자과제가 아니라 장기과제에서 효과"
type: source
domain: ai-news
tags: [ai-news, hf-paper, vla, game-agent, minecraft, agent-harness, embodied-ai, tencent, gui-agent]
created: 2026-10-26
updated: 2026-10-26
sources: [2610.31162]
reliability: medium
---

# HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games (HF 2610.31162)

**HF**: https://huggingface.co/papers/2610.31162 · org **Tencent** · 저자 6명(Zecong Tang · Zian Guan · Yuncheng Guo · Zhanqiu Zhang · Yiwen Guo · Bo Dai) · published 2026-10-22
**실측(2026-10-26 09:08 UTC)**: upvote **29**(수집기 일치) · HF `githubRepo` = 없음 · 본문 Project Page 표기 `github.com/Andytonglove/HiSTEVE-1.0` → **GitHub API 404**(수집기 "code unreleased" 와 일치, 단 링크 자체는 논문에 있음)
**도메인 판정**: **`ai-news`** — 가상 게임 에이전트(물리 로봇·카메라 파이프라인 없음). 볼트가 slam-3dgs 로 재분류한 [[FRED]] 는 실로봇 매니퓰레이션이었다. HiSTEVE 의 핵심 기여는 **하네스(메모리·플래너·완료 감지기) + GUI/비GUI 표현 분리**로, [[하네스-설계-축]] 계열에 더 가깝다.
**신뢰도**: ⭐⭐ (구체적 표·ablation 있음 · 코드 404 · 표본 작음)

> [!insight] 핵심 인사이트 — **"SOTA" 두 개의 무게가 전혀 다르다**
> 본문 원문: *"HiSTEVE improves average success by **20.0** percentage points on MineStudio Bench and **0.6** points on OpenHA"* (기준선 = OpenHA Text/CoA).
> - **MineStudio 85.0%** (기준선 65.0%) — 의미 있는 격차. 단 **20과제 × 3시행**, 패밀리당 15시행이라 1회 실패 = 6.7%p.
> - **OpenHA 37.4%** (기준선 36.8%) — **+0.6%p**. 본문: *"GUI and Combat remain **slightly below** the corresponding baseline scores"* — 이득은 Embodied 한 패밀리(37.0→46.0)에 몰려 있다. 반복 시행 분산 미보고 ⇒ "SOTA" 는 사실상 **동률**.
> 🎯 그리고 ablation 이 더 흥미롭다: **완전 하네스는 원자과제 점수를 거의 바꾸지 않는다** — *"MineStudio All 81.2%→85.0%, OpenHA Avg 37.8%→**37.4%**"*(오히려 하락), 반면 *"LongBench Goal SR **10.7%→25.0%**"*. ⇒ 하네스는 **장기 과제용 장치**이고, 원자 과제 SOTA 는 VLA 학습(세계지식 주입 → 모방 → 환경 RL)의 몫이다. [[하네스-설계-축]] 에 "하네스 이득이 나타나는 과제 지평" 사례로 추가할 만함.

> [!warning] 미검증·주의
> - **코드 404** (Project Page 링크는 있으나 레포 미공개 또는 비공개) ⇒ [[선언된-구현체-공백]].
> - LongBench 는 저자 신설 벤치. 본표 패밀리 값이 42.9 / 28.6 / 14.3 / 14.3 — 14.3 = 1/7 단위로 보여 **패밀리당 과제 수가 매우 작을 가능성**(추정, 본문 과제 수 미대조). 25.0% Goal SR 의 신뢰구간은 넓다.
> - "iron pickaxe from scratch" 는 정성 시연 — 성공률 미제시.
> - 저수준 VLA 는 **Qwen2.5-VL-7B** 기반(본문). 플래너는 별도 VLM.

## 도메인별 추출 (ai-news)
- **신뢰도**: upvote 29 · Tencent · 코드 없음 · 수치는 표 단위로 구체적.
- **즉시 활용**: NO — Minecraft 전용 · 코드 미공개. 다만 **"GUI 조작과 비GUI(월드) 조작의 표현 간섭"** 이라는 진단 + 해법(regime-specific RMSNorm 분기 · 마우스 이동 토큰 임베딩 분리)은 데스크톱/브라우저 GUI 에이전트에도 전이 가능한 아이디어. ablation: 공유 표현 대비 두 장치 결합 시 MineStudio 80.7%, OpenHA 26.6→37.7%.
- **6개월 영향력**: 중간 — "API/스킬 호출이 아니라 **사람과 같은 키보드·마우스**"로 장기 과제를 푸는 흐름. 게임 = 컴퓨터 사용 에이전트의 시험장.
- **대체 관계**: OpenHA(계층형 오픈소스 Minecraft 에이전트)를 원자과제에서 동률~우위, 장기과제에서 대체 시도. [[ForgeWM]] 은 같은 Minecraft 를 **월드모델** 쪽에서 다룬다(행동 vs 예측).
- **허와 실**: MineStudio +20%p 는 실재. OpenHA SOTA 는 +0.6%p · 두 패밀리 열세. 하네스 효과는 장기과제에서만 — 초록은 이 구분을 하지 않는다.
- **액션**: 레포 공개 여부 1주 후 재확인(낮음).

## 관련 페이지
- [[VLA]] · [[임바디드-AI]] · [[하네스-설계-축]] · [[에이전트-스킬]]
- [[Tencent]] · [[Qwen]]
- [[ForgeWM]] (Minecraft 월드모델) · [[월드모델]]
- [[선언된-구현체-공백]] · [[비매칭-비교]]
- 같은 배치: [[RynnUnify]] · [[RSIHub]] · [[UserArena]] · [[Omni-Woodpecker]]

## 원본
- 출처: https://huggingface.co/papers/2610.31162 · https://arxiv.org/html/2610.31162
- 볼트 실측: upvote 29 · 코드 레포 404 (2026-10-26 09:08 UTC)
- 신뢰도: ⭐⭐ (구체적 ablation / 코드 없음 · 소표본)
