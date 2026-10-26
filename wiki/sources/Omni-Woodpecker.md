---
title: "Omni-Woodpecker — 학습 없이 은닉상태를 직교분해해 오디오-비주얼 환각을 고친다. Qwen2.5-Omni-7B CMM 73.2→86.1, 대가는 지연 1.71배"
type: source
domain: ai-news
tags: [ai-news, hf-paper, hallucination, omni-llm, audio-visual, training-free, representation-editing, qwen2.5-omni, nanjing-university]
created: 2026-10-26
updated: 2026-10-26
sources: [2610.27103]
reliability: high
---

# Omni-Woodpecker: Hallucination Correction via Evidence-Prior Rebalancing for Omni LLMs (HF 2610.27103)

**HF**: https://huggingface.co/papers/2610.27103 · org **Nanjing University** · 저자 5명(Zijian Liu · Chaoyou Fu · Yan Yang · Caifeng Shan · Ran He) · published 2026-10-19 · 코드 `ZiiJianLiu/Omni-Woodpecker`
**실측(2026-10-26 09:08 UTC)**: upvote **21**(수집기 20 → +1) · ★**97**(수집기 94 → +3) · MIT · 레포 생성 2026-09-01(논문보다 먼저) · push 10-26 · `owp/ · configs/ · results/ · tests/ · run_smoke.sh · sample_data/` 실재
**도메인 판정**: **`ai-news`** — 7B 백본에 붙는 추론 시 기법이라 local-llm 과도 접점이 있으나, 주제는 온디바이스/메모리가 아니라 **멀티모달 환각 교정**.
**신뢰도**: ⭐⭐⭐⭐ (코드·결과 디렉터리 실재 · 지연 비용과 대조 통제까지 보고)

> [!insight] 핵심 인사이트 — **"출력 단계 조작"에서 "융합 표현 재균형"으로: 그리고 단순 "No 편향"이 아님을 직접 통제했다**
> 방법: 모달리티별 뷰로 교차모달 충돌 감지 → 은닉상태를 **근거(evidence) 성분 vs 사전지식(prior) 성분으로 직교분해** → 디코딩 전에 오도하는 prior 억제·무시된 evidence 복원. 학습 없음.
> 🎯 환각 벤치 개선은 흔히 "예(yes)라고 덜 말하게" 만든 효과일 수 있다. 저자는 이를 통제했다 — **"No 쪽으로 yes-rate 를 맞춘 상수 이동"** 대조군:
> ```
>                         Qwen2.5-Omni-7B   VideoLLaMA2-AV   (진단 셋, 백본 대비 %p)
> Shift toward "No"(matched)   +0.60            +0.67
> + OWP                        +2.85            +2.14
> ```
> ⇒ 이득의 대부분은 yes-bias 이동으로 설명되지 않는다. 이 한 줄이 "환각 감소" 류 논문에서 가장 먼저 찾아볼 대조군이다.

> [!warning] 수치 성격 (수집기 대비)
> - **모두 절대 점수차(%p)**: CMM **73.2→86.1 (+12.9)** · AVHBench **75.1→83.7 (+8.6)** · VideoLLaMA2-AV CMM **76.2→80.8 (+4.6)** · AVHBench **70.2→74.1 (+3.9)** — 수집기 수치 전부 일치.
> - 기여 문단 표현은 *"improves the original OLLMs by **up to** 12.9 points"* — 12.9 는 최대치. **가장 강한 기존 기법 대비 격차는 +4.9 / +7.7**(본문).
> - 일반 벤치 +0.67~2.25: OmniBench 45.36→47.29 · WorldSense 45.21→47.46 · MUSIC-AVQA 85.08→86.08 · AVQA 91.83→92.50. AVQA 는 이미 91.8% 라 +0.67 은 [[천장-기준선]] 영역.
> - **트레이드오프 존재**: CMM 표에서 PA 열 89.5→86.7 하락 · HR 열 57.0→85.5 상승(열 정의는 본문 표 헤더 기준, 세부 의미는 미대조) — 모든 하위지표가 오르는 것은 아님.
> - **"training-free" ≠ "설정 없이"**: VideoLLaMA2-AV 는 *"evidence layers (16, 20, 24) and the residual gains (α_R=0.20, β_R=1.20) are adapted to the backbone"* — 백본별 층·계수 튜닝 필요.
> - **비용**: RTX A6000 기준 지연 3.54s→6.05s(**1.71×**), VideoLLaMA2-AV 1.77× · 전방 호출 ≤5회. 비교 기법 MAD 2.81× · HulluEdit 3.68× 보다는 싸다.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★97 · upvote 21 · 난징대 · MIT · 결과/테스트 디렉터리 존재. 볼트 기준 스타 1000 미달이나 논문 내 통제가 촘촘함.
- **즉시 활용**: **조건부 YES** — Qwen2.5-Omni-7B 로 오디오+영상 질의를 돌리는 파이프라인(예: down-analysis 의 영상 내용 판정)이 있다면 학습 없이 붙일 수 있는 후보. 단 지연 1.7배 · 백본별 튜닝. 지금 볼트 워크플로우는 Omni 모델을 쓰지 않으므로 실험은 보류.
- **6개월 영향력**: 중간 — 오디오-비주얼 환각은 Omni 모델이 늘수록 커지는 문제. "출력 대조 디코딩(AVCD·MAD)" → "표현 편집" 이동의 사례.
- **대체 관계**: AVCD(대조 디코딩) · MAD(모달리티 적응 디코딩) · HulluEdit(표현 편집)를 같은 프로토콜에서 상회하고 더 빠름. 이미지 VLM 쪽 학습 없는 환각 억제 [[Online-Self-Calibration-VLMs]] 의 오디오-비주얼판.
- **허와 실**: 과장 적음. 핵심 리스크는 ① 백본별 하이퍼파라미터, ② 일반 벤치 이득이 작고 일부는 천장 근처, ③ OWP 적용 백본은 2종뿐 — 본표 "External omni backbones" 행(VITA-1.5 · OmniVinci · Qwen3-Omni)은 OWP 미적용 참고치. [[Qwen3.5-Omni]] 등 최신 Omni 적용은 미검증.
- **액션**: ★ 정도. Omni 모델 도입 시 1순위 후보로 메모.

## 관련 페이지
- [[Qwen]] · [[Qwen3.5-Omni]] · [[Audio-Visual-Intelligence-Foundation-Models]] · [[OmniAssistBench]]
- [[Online-Self-Calibration-VLMs]] · [[Enoki]] (환각 탐지) · [[천장-기준선]] · [[한정어-탈락]]
- 같은 배치: [[UserArena]] · [[RSIHub]] · [[HiSTEVE]] · [[RynnUnify]]

## 원본
- 출처: https://huggingface.co/papers/2610.27103 · https://arxiv.org/html/2610.27103 · https://github.com/ZiiJianLiu/Omni-Woodpecker
- 볼트 실측: upvote 21 · ★97 (2026-10-26 09:08 UTC)
- 신뢰도: ⭐⭐⭐⭐ (코드 실재 · 대조군·비용 보고 / 백본별 튜닝)
