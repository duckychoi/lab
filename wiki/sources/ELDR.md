---
title: ELDR — PD 분리형 MoE 서빙의 expert-locality 인지 디코드 라우팅
type: source
domain: ai-news
tags: [ai-news, hf-paper, moe, inference, serving, routing, efficiency]
created: 2026-07-02
updated: 2026-07-02
sources: []
reliability: low
---

# ELDR (Expert-Locality-aware Decode Routing, HF papers 2607.00466)

> [!insight] 핵심 인사이트
> **PD 분리형(Prefill-Decode disaggregation) MoE 서빙**에서 **expert-locality를 인지한 디코드 라우팅** 기법. MoE(Mixture-of-Experts) 추론은 토큰마다 다른 전문가(expert)를 호출해 메모리·통신 비용이 크고, 특히 프리필과 디코드를 다른 하드웨어로 분리한 최신 서빙 구조에서 expert 위치(locality)를 무시하면 통신이 폭증한다. ELDR은 디코드 단계 라우팅을 expert가 실제 어디 있는지에 맞춰 정렬해 **MoE 추론 효율을 최적화**한다. [[BlockPilot]]·[[JetSpec]]가 디코딩 속도(추측 디코딩)를 밀었다면, ELDR은 *MoE 특유의 서빙 토폴로지* 최적화 — [[OmniRoute]] 같은 게이트웨이 아래에서 대형 MoE를 싸게 굴리는 인프라 축.

## 도메인별 추출 (ai-news / local-llm 교차)

- **신뢰도**: ⭐ — HF 자동수집. 저자·처리량/지연 개선치·대상 모델(GLM/Qwen MoE 등) 미확인.
- **즉시 활용**: NO — 대규모 MoE 서빙 인프라 기법으로 개인 로컬 규모엔 직접 무관. 클라우드 MoE 서빙 원가 이해용.
- **6개월 영향력**: 중간 — [[GLM-5.1]](753B MoE) 등 초대형 MoE가 주류가 될수록 PD 분리 + expert-locality 라우팅이 서빙 표준 최적화로 편입. 대형 모델 API 단가에 간접 영향.
- **대체 관계**: 순진한 MoE 디코드 라우팅을 locality 인지 방식으로 대체.
- **허와 실**: 서빙 최적화는 클러스터 구성·통신 대역에 극도로 의존. 논문 세팅 밖 일반화 여부가 관건.
- **액션**: 별도 개인 액션 없음. MoE 서빙 원가 논의 시 [[OmniRoute]]·[[GLM-5.1]] 맥락 참고 링크로 보관.

> [!question] 미해결 질문
> 대상 MoE 모델·규모? 처리량/지연/통신량 개선 수치? 오픈 구현 존재?

## 관련 페이지
- [[BlockPilot]]
- [[JetSpec]]
- [[OmniRoute]]
- [[GLM-5.1]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.00466
- 신뢰도: ⭐ (HF 자동수집 — 원문·수치 미검증)
