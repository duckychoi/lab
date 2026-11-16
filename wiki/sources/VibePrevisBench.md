---
title: "VibePrevisBench — 코딩 에이전트가 Blender 4D 씬을 만들어 영상 생성용 프록시 영상을 렌더하는 능력 벤치"
type: source
domain: video-saas
tags: [video-saas, benchmark, blender, coding-agent, previs, paper]
created: 2026-11-16
updated: 2026-11-16
sources: [https://huggingface.co/papers/2611.15789]
reliability: high
---

**논문**: arXiv 2611.15789 · HF Daily 11-16 3위 · 업보트 **58**(볼트 · 수집기 46) · HF 조직 `Kling-Keye` · 코드 vibeprevisbench/vibeprevisbench · 242과제.

## 핵심 인사이트
> [!insight] 제어 가능한 영상 생성의 입력을 에이전트가 만든다 — "그레이박스 프리비즈"
> 영상 생성 모델은 레이아웃 · 움직임 · 카메라를 고정한 **그레이박스 프록시 영상**을 조건으로 받을 수 있다. 코딩 에이전트가 브리프(대본 · 사진 · 이어찍기 · 참조 영상)로 Blender 4D 씬을 만들고 그 영상을 렌더. 채점: 코드 재실행 후 숨은 정답 사실과 9차원 대조하는 **Scene Check** + VLM 판정자가 프록시 영상에서 그 사실을 알아보는지 보는 **Screen Check**. → 영상 SaaS 의 "프롬프트 → 영상" 사이에 **편집 가능한 3D 중간 표현**을 넣는 워크플로.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹 (arXiv HTML 표 2 · 볼트 확인)**: Overall **GPT-6 Astra 77.7 · GPT-6.1 Sol 76.1 · Gemini 4 Argon 75.0 · Opus 5.5 74.1** … 사진 입력 Scene 점수 최고 Opus 5.5 **59.8**(모든 에이전트 40–60점대 — 가장 어려운 입력). 사람 선호와 판정자 상관 Spearman **0.90–0.94**.
- **크리에이터 인사이트**: 기본 카메라 · 배치는 모두 해내지만 어려운 요청에서 실패, **자기 렌더를 확인하고도 오류를 고치지 못함**, 최상위도 영상 과제의 **55%** 에서 참조보다 컷을 더 넣음.
- **워크플로**: 대본 → 에이전트 Blender 프리비즈 → 프록시 영상 → 제어형 영상 생성. 볼트 Remotion 파이프라인의 3D 버전.
- **경쟁 우위 빈틈**: "렌더를 브리프와 항목별 대조"하는 검증 단계 — 현 에이전트가 못 하는 부분.

> [!warning] 하네스가 다르다
> *"The GPT models run in the Codex CLI and all other models in Claude Code"*(볼트 확인) — 모델 순위에 하네스 차이가 섞였다 → [[하네스-설계-축]] · [[비매칭-비교]]. 상위 4개 격차 3.6점.

## 관련 페이지
- [[하네스-설계-축]] · [[비매칭-비교]] · [[AI-영상-생성-2026]] · [[AI-3D-생성]] · [[Remotion]] · [[ffmpeg-skill]] · [[After-Effects-MCP]]

## 원본
- 출처: https://huggingface.co/papers/2611.15789 · https://arxiv.org/html/2611.15789
- 확인 범위: HF papers API 초록 · arXiv HTML 표 2 행 · 하네스 문장 · 55% · 상관 표(볼트) · 🔴 코드 미실행
- 신뢰도: ⭐⭐⭐ (242과제 · 사람 상관 검증 · 코드 공개)
