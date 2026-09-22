---
title: TaichuAI
type: entity
domain: ai-news
tags: [ai-news, vlm, spatial-reasoning, china, derivative]
created: 2026-09-22
updated: 2026-09-22
sources: [ZDTaichu5.0-9B.md]
reliability: low
---

# TaichuAI

HF `TaichuAI`. [[ZDTaichu5.0-9B]] 제작(Qwen3.5-9B 디코더 + C-RADIOv4-H 비전 인코더 교체형 VLM). ⬜ 법인 실체·국적은 볼트가 확인하지 않았다(이름상 중국 '자동화연구소 紫东太初' 계열로 보이나 **추정**).

> [!insight] 🎯 파생 식별의 새 사례 — **기계판독 필드 0, 산문만 부모를 밝힌다**
> `base_model` · `base_model_relation` **둘 다 미설정**. README 산문만 *"Qwen3.5-9B LLM Decoder"* 를 적는다. 원본 `Qwen/Qwen3.5-9B` = DL **9,307,599** · 좋아요 2,010 · Apache-2.0(09-22 실측). → [[파생저장소-식별]] 에 **"인코더 교체형 + 필드 미설정"** 탐지 사례.

> [!warning] 🔴 카드가 자기 표를 반증한다
> 카드 문장 *"no trading"* ↔ 볼트 재집계: 공간 **8승 1패** · 일반 시각 **2승 5패** · 지식·추론 8승 3패(총 18승 9패). TAU2 87.7 은 **다른 시뮬레이터/심판**(DeepSeek-V4-Flash) 조건 — [[비매칭-비교]]. 컨텍스트도 128K / 262,144 / 220,000 **세 값**. 서빙은 **vLLM 포크 필수**.

## 관련 페이지
- [[ZDTaichu5.0-9B]] · [[파생저장소-식별]] · [[비매칭-비교]] · [[NVIDIA]]
- [[ai-news]]
