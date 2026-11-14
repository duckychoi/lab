---
title: "Actor, Judge, or Teacher? — 행동은 못해도 사후 평가는 잘하는 결정 모델 (ALFWorld 72.8→82.9% · arXiv 2611.17167)"
type: source
domain: ai-news
tags: [ai-news, decision-model, system-one, agent, reinforcement-learning, judge, credit-assignment]
created: 2026-11-14
updated: 2026-11-14
sources: [https://huggingface.co/papers/2611.17167]
reliability: medium
---

**논문**: [arXiv 2611.17167](https://huggingface.co/papers/2611.17167) *Actor, Judge, or Teacher? Understanding Decision Models in Long-Horizon Agents* · 업보트 **30** · 저자 10명(Haochen Liu … Yongliang Shen) · 발행 2026-11-12 · 코드 ZJU-REAL/decision-agents ★42 (HF papers API 볼트 실측 — 수집기와 일치)

## 핵심 인사이트
> [!insight] "과제가 성공할까"를 묻지 말고 "이 행동이 도움이 됐나"를 물어라
> 결정 모델(선택지별 확률을 내는 타입 출력 모델 — [[System-One-모델]])을 세 역할로 비교: 행위자(actor) · 심판(judge) · 교사(teacher).
> - **행위자**: ALFWorld 에서 결정 모델 3종 + 범용 LLM 3종 **6개 전부**가 먼저 해야 할 하위목표 대신 더 쉬운 하위목표로 끌려간다.
> - **심판**: 궤적 전체를 본 같은 모델들은 그 하위목표로 향한 단계에 제대로 점수를 준다. 질문 형식이 갈랐다 — *과제 성공 여부*가 아니라 *각 행동이 도움이 됐는가*를 물을 때 유용/무용 행동이 분리된다.
> - **교사**: JEV 를 교사로 쓰면 Qwen2.5-1.5B 정책이 GRPO 대비 **ALFWorld 72.8% → 82.9% · WebShop 56.8% → 71.4%**.
> - 결론: *"a poor actor can still teach well, because judging an action after the episode ends reveals the consequences that acting must anticipate."*
>
> ⇒ 볼트 규약 [[요약자와-판정자-분리]]의 실험적 근거 하나. 같은 모델도 "사후에 전체를 보고 판정"하는 자리에서는 더 낫다 — 수집기(요약) → 볼트(판정) 구조가 기대는 비대칭과 같다.

> [!warning] 범위
> 환경 2종(ALFWorld · WebShop) · 정책 1종(Qwen2.5-1.5B) · 교사 실험은 JEV 1종. "결정 모델 3종"의 이름은 초록에 없다. 심판 정확도의 수치도 초록에 없다.

## 도메인별 추출 (ai-news)
- **신뢰도**: 업보트 30 · 코드 공개 · 초록에 핵심 수치 4개.
- **즉시 활용**: 설계 차용 YES — 에이전트 실행 로그를 평가할 때 "전체 성공?"이 아니라 **단계별 "이 행동이 목표에 기여했나?"** 로 묻는다. 볼트의 수집기 판정에도 같은 질문 형식을 쓸 수 있다.
- **6개월 영향력**: 결정 모델의 용도가 "빠른 행위자"에서 "값싼 보상 모델"로 옮겨 갈 수 있다.
- **대체 관계**: LLM-as-judge 의 저비용 대안(단일 forward 확률).
- **허와 실**: 소규모 환경, 그러나 대조가 깨끗하다(같은 6개 모델을 두 역할에).
- **액션**: 아래.

> [!action] 당장 할 것
> 수집기 판정 프롬프트 · 에이전트 사후 평가에 "행동 단위 기여 질문" 형식을 1회 적용해 본다(낮음 · 설계 메모).

## 관련 페이지
- [[System-One-모델]] · [[SO-Arena]] · [[AutoTrust-JEV-27B]] · [[Jeva]] · [[요약자와-판정자-분리]] · [[하네스형-에이전틱-RL]] · [[온폴리시-증류]]

## 원본
- 출처: https://huggingface.co/papers/2611.17167
- 확인 범위: HF papers API 초록 전문 · 저자 · 🔴 본문 · 코드 미열람 · 저자 소속 미확인(레포 조직명은 ZJU-REAL)
- 신뢰도: ⭐⭐ (업보트 30 · 코드 공개)
