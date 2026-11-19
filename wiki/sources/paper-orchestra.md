---
title: "google-research/paper-orchestra — 연구 자료를 투고용 LaTeX 원고로 만드는 멀티에이전트 (사람 평가 승률 차 문헌조사 50–68% · 전체 14–38%)"
type: source
domain: ai-news
tags: [ai-news, github-trending, multi-agent, paper-writing, latex, google]
created: 2026-11-19
updated: 2026-11-19
sources: [https://github.com/google-research/paper-orchestra]
reliability: medium
---

**GitHub**: ★4,669(볼트 API 11-19 · 수집기 4,665 · 당일 +1,524) · Apache-2.0 · Python · 생성 2026-05-01 · HEAD d9bae99(2026-11-15T18:08Z) · 논문 arXiv 2604.05018(*PaperOrchestra*)

## 핵심 인사이트
> [!insight] 결과를 만드는 도구가 아니라, 이미 있는 결과를 "원고 모양"으로 조립하는 도구
> 아이디어 · 실험 로그 → 개요 → 문헌조사(Semantic Scholar) → 섹션 작성 → 퇴고 → 플롯/개념도 에이전트 → 학회 템플릿 LaTeX. [[Google]] Cloud AI Research. 기여의 중심은 **문헌조사 품질**이다 — 초록의 승률 차는 문헌조사(50–68%)가 전체 원고(14–38%)보다 훨씬 크다.

> [!warning] 수치의 조건 (초록 전문 볼트 대조)
> - 승률 차는 **"autonomous baselines" 대비 side-by-side 사람 평가**다 — 사람이 쓴 원고 대비가 아니다([[비매칭-비교]] 주의).
> - 벤치 PaperWritingBench(200편 역설계)는 저자 자신이 만든 것이고, README 48–51행: **평가 데이터셋 미포함(추후 공개)** → 지금은 재현 불가.
> - Gemini(Vertex 또는 키) / OpenAI 키 필요(README 30–41행).

## 도메인별 추출 (ai-news)
- **신뢰도**: ⭐⭐⭐ — Google 공식 레포 · 논문 있음 · 벤치 자체 제작 · 데이터 미공개.
- **즉시 활용**: 🟡 조건부 — 실험 결과가 이미 있는 초고 작업에만. 볼트 사용자의 학회 일정(CVPR 등)이 있을 때 문헌조사 초안 생성용으로 시험할 만하다.
- **6개월 영향력**: "문헌조사 자동화"가 연구자 워크플로에 들어오는 신호. 같은 날 [[Resolution-Hypothesis]] 가 보여 주듯 **생성기는 좋아지는데 판정(사람 평가)이 병목**인 구조는 같다.
- **대체 관계**: [[Spark-to-Paper]] · [[paperclip]] 계열 논문 작성 보조와 겹친다.
- **허와 실**: 결과를 만들어 주지 않는다. 인용 정확성(환각 인용) 평가 수치는 초록에 없음.
- **액션**: star · 데이터셋 공개 시 재확인.

## 관련 페이지
- [[Google]] · [[Spark-to-Paper]] · [[paperclip]] · [[AI-에이전트-프레임워크]] · [[Resolution-Hypothesis]] · [[비매칭-비교]]

## 원본
- 출처: https://github.com/google-research/paper-orchestra · https://huggingface.co/papers/2604.05018
- 확인 범위: GitHub API(스타 · 라이선스 · 생성일 · push) · HF papers API 초록 전문 · README 30–51행(키 · 데이터셋) · 🔴 파이프라인 단계 구성은 수집기 판독 · 실행 0
- 신뢰도: ⭐⭐⭐
