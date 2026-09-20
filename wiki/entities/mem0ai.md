---
title: mem0ai
type: entity
domain: local-llm
tags: [agent-memory, 오픈코어, 스킬-배급, 벤치마크]
created: 2026-09-20
updated: 2026-09-20
sources: [mem0.md]
reliability: medium
---

# mem0ai

GitHub `mem0ai` · mem0.ai. **에이전트 메모리 레이어의 사실상 기준점.**

> [!warning] 🔴 볼트가 8개월간 자(尺)로만 써 온 조직이다
> [[VoiceMem]] 의 대표 수치(*"top-5로 **Mem0의 top-200** 대비 약 30점 우위"*)와 [[TencentDB-Agent-Memory]] 의 경쟁자 목록에 이름만 있었고, **페이지가 없었다.** → [[mem0]] 참조. [[browser-use]]·[[HuggingFace]] 에 이은 **본체 누락 3번째**.

> [!insight] 자리의 성격 — **오픈코어, 그리고 퍼널을 스킬로 배급한다**
> 3경로 배포(OSS `pip install mem0ai` · 셀프호스트 docker · 매니지드 플랫폼). 🔴 벤치 점수는 **매니지드 플랫폼**의 것이고 README가 그렇게 명시한다(*"proprietary optimizations not available in the open-source SDK"*).
> ✅ **평가 하네스는 별도 오픈소스**(`mem0ai/memory-benchmarks`) — 🎯 **자는 열고 피측정물은 닫았다.**
> 🎯 **스킬 배급**: `npx skills add ... --skill mem0-oss-to-platform` · `/mem0-integrate` · `/mem0-test-integration`. **스킬 하나가 문자 그대로 "오픈소스 → 유료 플랫폼 이전"** — [[Vercel]]·[[higgsfield-repo]]·[[SnailSploit]] 의 스킬 배급 축에서 **상용 퍼널을 스킬로 낸 첫 사례**.

> [!note] 📌 볼트 실측 (2026-09-20)
> [[mem0]] ★**65,688** · fork 7,713 · Apache-2.0 · created **2023-06-20**(3년 3개월) · open issues 759(이슈 322/PR 437) · topics 14.
> 벤치 4행: LoCoMo 71.4→**92.5** · LongMemEval 67.8→**94.4** · BEAM 1M **64.1** · 🔴 **BEAM 10M 48.6(−15.5)**.

## 관련 페이지
- [[mem0]] · [[에이전트-메모리-레이어]] · [[VoiceMem]] · [[표-부분인용]] · [[Vercel]] · [[higgsfield-repo]] · [[검사가능성-공사]] · [[local-llm]]
