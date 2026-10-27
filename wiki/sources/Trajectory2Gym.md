---
title: "Trajectory2Gym — '성공 궤적'이 아니라 '결정 시점에 근거가 있는 행동'만 감독 신호로 쓴다. Qwen3 5개 스케일 전부 +16.9~29.8%p"
type: source
domain: ai-news
tags: [ai-news, hf-paper, tool-use, agent-training, sft, synthetic-data, tau-bench, bfcl, qwen3]
created: 2026-10-27
updated: 2026-10-27
sources: [https://huggingface.co/papers/2610.33568, https://github.com/yihaohu0118/Trajectory2Gym]
reliability: medium
---

# Trajectory2Gym: Decision-Grounded Compositional Interaction Synthesis for Tool-Use Agents

**HF**: https://huggingface.co/papers/2610.33568 · published **2026-10-24** · 소속 **ant-international**(Yihao Hu · Wei Wu 외) · upvote **164**(수집기 162 · +2)
**코드**: https://github.com/yihaohu0118/Trajectory2Gym — ★4 · Apache-2.0 · Python 922KB · `trajectory2gym/` `env/` `tests/` `RELEASE_MANIFEST.json` 실재 ✅
**신뢰도**: ⭐⭐ medium (5개 스케일 일관 개선 · 코드 공개 / 수치는 초록 범위값만)

> [!insight] 핵심 인사이트 — **"성공했다"는 것이 "배울 만하다"를 보증하지 않는다**
> 초록 첫 문장: *"Successful tool-use trajectories are not necessarily useful supervision."* 두 조건을 제시한다:
> 1. **조합적 커버리지** — 관측→행동 의존성이 데이터에 표현돼 있어야 한다
> 2. **결정 근거(decision grounding)** — 각 감독 행동이 *그 시점에 학습자에게 보이던 이력*으로 정당화돼야 한다(운 좋게 맞힌 행동 배제)
> ⇒ 궤적 생성을 "성공 수집"에서 **"학습 가능한 상호작용 경험의 의도적 구성"** 으로 재정의. [[Trial-by-Trace]] 의 "성공 ≠ 신뢰" 와 같은 날 같은 방향의 주장이 나왔다 — 하나는 평가, 하나는 학습 데이터에서.

> [!warning] 주의
> - ⚖️ **+16.9~29.8%p 는 "3벤치 등가중 평균"의 스케일별 범위** — 개별 벤치·스케일 수치는 초록에 없다(볼트 본문 미열람).
> - ⚖️ 비교 기준(무엇 대비 +)이 초록상 불명확 — 베이스 모델 대비인지, 기존 궤적 합성법 대비인지 확인 필요 → [[비매칭-비교]] 규약 ㉒.
> - 📌 개선 폭이 가장 큰 곳: **상태 유지·멀티턴**(나중 결정이 앞선 관측에 의존) — Tau2 류.

## 도메인별 추출 (ai-news)
- **즉시 활용**: NO(학습 파이프라인) — 단 **데이터 필터 원칙**은 바로 쓸 수 있다: 에이전트 로그로 파인튜닝할 때 "결과 성공" 필터 대신 "그 시점 정보로 정당화되는 행동" 필터.
- **6개월 영향력**: 도구사용 SFT 데이터의 품질 기준이 성공률 → 근거성으로 이동하는 신호(추정).
- **대체 관계**: 성공 궤적 증류 계열(→ [[DynaFlow]] 도 "distilled trajectories" + 결함 필터를 쓴다 — 같은 날 같은 처방).

## 관련 페이지
- [[하네스형-에이전틱-RL]] · [[AI-에이전트-프레임워크]] · [[Qwen]] · [[비매칭-비교]]
- 같은 배치: [[Trial-by-Trace]] · [[DynaFlow]] · [[StreamVibe]] · [[InteractiveWorld]]
- [[ai-news]]

## 원본
- https://huggingface.co/papers/2610.33568 · 볼트 HF API 실측(2026-10-27): upvote 164 · GitHub ★4 · contents 16항목
