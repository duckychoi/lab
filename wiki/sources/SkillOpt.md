---
title: SkillOpt — 프로즌 LLM 에이전트 스킬 텍스트공간 최적화
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skills, skill-evolution, microsoft, text-space-optimization]
created: 2026-05-25
updated: 2026-07-10
sources: []
reliability: high
---

# microsoft/SkillOpt (GitHub ⭐12,019) ← HF논문 arXiv 2605.23904

> [!insight] 핵심 인사이트 (2026-05-25 논문 시점)
> Microsoft Research — 에이전트가 원시 경험에서 스킬을 자율 진화시키는 SkillOpt 프레임워크. 외부 개입 없이 스킬 품질을 점진적으로 개선. [[Skill1-Unified-Evolution]], [[SkillOS]]와 함께 에이전트 자기진화 연구 클러스터 형성.

> [!note] 2026-07-10 갱신 — 논문이 **실제 오픈소스 코드로 공개** (GitHub ⭐12,019, 당일 +276, [[Microsoft]])
> WebFetch README 실측: 개념 논문이었던 SkillOpt가 **동작하는 텍스트공간 옵티마이저**로 릴리스됨(v0.2.0, 2026-07-02). 핵심은 **모델 가중치를 건드리지 않고(frozen) 자연어 스킬을 텍스트 공간에서 최적화·재사용**한다는 것 — ①궤적 기반 편집 + **검증 게이트(validation gate)** 업데이트, epoch·batch·learning rate 같은 학습 하이퍼파라미터를 스킬 텍스트에 적용, ②산출물은 배포 가능한 **`best_skill.md`(보통 300–2,000 토큰)**, ③백엔드 다중 지원(OpenAI·Azure·**Claude**·Qwen·MiniMax·Codex·**Claude Code**), ④내장 벤치 6종 + WebUI 대시보드, ⑤**SkillOpt-Sleep**(야간 오프라인 자가진화 — 경험 리플레이 + 장기 메모리). 결과: 52개 모델-벤치-하니스 조합에서 정확도 **+19.1~+24.8점** 향상 주장(자가 벤치). MIT·Python 87%. → "스킬을 **가중치 대신 텍스트로 학습**한다"는 [[온폴리시-증류]]의 프롬프트판. [[SkillCoach]](스킬 사용 평가)·[[agent-skills]](스킬 배포)와 3층(생성·최적화·평가) 완성.

## 도메인별 추출 (2026-07-10 실측 기준)

- **신뢰도**: ⭐⭐⭐⭐ (GitHub ⭐12,019·당일 +276·MIT·v0.2.0, README WebFetch 실측 — best_skill.md·검증게이트·SkillOpt-Sleep 확인. +19~24점은 자가 벤치)
- **즉시 활용**: YES(후보) — **Claude Code 백엔드 지원**이 결정적. 내 스킬(reat-*·down-analysis 등) 프롬프트를 궤적 기반으로 자동 최적화해 `best_skill.md`로 배포하는 실험 가능.
- **6개월 영향력**: 스킬 개선이 수작업 프롬프트 튜닝→**자동 텍스트공간 최적화 + 검증 게이트**로 이동. "가중치 없는 학습"이 프로즌 프런티어 모델 시대의 현실적 개선 경로.
- **대체 관계**: [[SkillClaw]]·[[SkillOS]] 개념 연구를 **실행 코드로 구현**. 수동 스킬 편집·[[SkillCoach]](평가)와는 상보(최적화 vs 평가).
- **허와 실**: "+19.1~24.8점"은 자가 벤치(52 조합) — 내 태스크 재현 필요. 다만 frozen·텍스트공간·검증게이트 설계 자체는 건전하고 재현 마찰 낮음.
- **액션**: SkillOpt를 Claude Code 백엔드로 붙여 down-analysis 스킬 1개를 궤적 최적화 → 원본 대비 품질·토큰 비교, `best_skill.md` 산출 검증.

## 관련 페이지
- [[Microsoft]] — 제작사
- [[SkillCoach]] — 스킬 사용 능력 평가(3층 중 평가)
- [[agent-skills]] · [[claude-skills]] — 스킬 배포/큐레이션(3층 중 생성)
- [[온폴리시-증류]] — "학습 신호로 개선"의 가중치판(텍스트공간 대비)
- [[AI-에이전트-프레임워크]] · [[SkillClaw]] · [[Skill1-Unified-Evolution]]

## 원본
- 출처(코드): https://github.com/microsoft/SkillOpt (⭐12,019, 2026-07-10 당일 +276, MIT, v0.2.0)
- 출처(논문): https://huggingface.co/papers/2605.23904
- 성과: 52 조합 +19.1~24.8점(자가) / best_skill.md 300–2,000토큰 / SkillOpt-Sleep 야간 자가진화
- 신뢰도: ⭐⭐⭐⭐ (README WebFetch 실측 / 벤치 자가측정)
