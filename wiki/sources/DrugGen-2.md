---
title: DrugGen 2 — 질병 인지형 언어모델 신약 후보 생성
type: source
domain: ai-news
tags: [ai-news, drug-discovery, generative, grpo, smiles, biotech]
created: 2026-07-11
updated: 2026-07-11
sources: []
reliability: medium
---

# DrugGen 2 (HF papers 2607.08404)

> [!insight] 핵심 인사이트
> **질병 맥락 + 표적 단백질**을 함께 조건으로 받아 신약 후보 분자(SMILES)를 생성하는 모델. "같은 표적도 질병 상태에 따라 다르게 행동한다"는 관찰을 반영한 **최초의 질병 조건부 분자 생성**. GPT-2를 2단계 학습 — SFT(승인 약물 13,908건)로 disease-target-drug 관계 학습 후 **GRPO 강화학습**(유효성·신규성·다양성·결합친화도 보상). 표적당 고유 분자 409-444개(경쟁 50-219), 유효성 99-100%, 결합친화도 중앙값 9.26-9.97.

**HF Papers**: https://huggingface.co/papers/2607.08404 (upvote 3)  
**신뢰도**: ⭐⭐⭐ (초록 원문 검증 / 재현·수치 미실측)

## 도메인별 추출

- **신뢰도**: 초록 원문 WebFetch 검증. 도킹 검증(ACE·PPARγ) 수치는 미재현 → medium
- **즉시 활용**: 없음(바이오 도메인, 내 4대 도메인 밖). 기록·트렌드 관측용
- **6개월 영향력**: **GRPO(그룹 상대 정책 최적화)가 분자 생성에도** 적용 — [[UP-Asymmetric-Optimization]]·[[온폴리시-증류]]와 같은 RL 계보가 도메인 특화 생성에 확산되는 사례
- **허와 실**: GPT-2 기반(소형)이라 규모보다 **질병 온톨로지(MeSH) 조건화 + RL 보상 설계**가 성능 원천. 실제 신약 가치는 wet-lab 검증 전까지 미확정
- **대체 관계**: DrugGPT·DrugGen 대비 고유 생성 수·drug similarity·binding affinity 전면 우위(자가 평가)
- **액션**: 없음 — "RL 보상 설계로 도메인 특화 생성을 끌어올린 패턴"만 참고 노트

> [!note] 배경 정보
> 입력: 질병 식별자(MeSH 계층) + 표적 단백질 서열 → 출력 SMILES. 도메인 지식(온톨로지)을 조건으로 넣어 표적-only 접근을 넘어선 것이 핵심 기여.

## 관련 페이지
- [[UP-Asymmetric-Optimization]]
- [[온폴리시-증류]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.08404
- 신뢰도: ⭐⭐⭐ (초록 검증)
