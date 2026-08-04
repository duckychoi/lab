---
title: nanoGPT — 중형 GPT 학습/파인튜닝 최소 코드 레퍼런스 (deprecated)
type: source
domain: ai-news
tags: [ai-news, github-trending, education, gpt, training, karpathy, deprecated]
created: 2026-07-06
updated: 2026-07-06
sources: []
reliability: high
---

# karpathy/nanoGPT (GitHub ⭐60,816)

**GitHub**: https://github.com/karpathy/nanoGPT
**스타수**: 60,816 (2026-07-06 기준, 당일 +246)

> [!insight] 핵심 인사이트
> [[Andrej Karpathy]]의 **GPT-2(124M)를 ~300줄 `train.py` + ~300줄 `model.py`로 재현**하는 교육/실험 레퍼런스. "teeth over education"(교육보다 실전) 지향으로 minGPT를 재작성 — 8×A100 40GB 한 노드로 4일이면 OpenWebText에서 GPT-2 재현. 코드가 극도로 단순해 스크래치 학습·파인튜닝 실험의 해킹 베이스로 최적. 당일 +246 스타는 신규성이 아니라 **레퍼런스 상수의 꾸준한 재유입**.

> [!warning] deprecated — nanochat로 대체됨
> 레포 상단 공지(2025-11): nanoGPT는 이제 **"매우 오래됐고 deprecated"**, 개선판 사촌 **nanochat**(karpathy/nanochat)을 쓰라고 명시. 지금 새로 시작한다면 nanochat이 정답 — nanoGPT는 후대를 위해 남겨둔 아카이브. *당일 급상승 = 도구 채택이 아니라 교육 레퍼런스 재확산* 신호로 해석([[AI-For-Beginners]]·[[cs249r_book]]과 같은 "레퍼런스 급등" 계열).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ (Karpathy 저작, 검증된 교육 표준. 단 deprecated 상태)
- **즉시 활용**: 제한적 — 신규 프로젝트엔 nanochat 권장. nanoGPT는 "GPT 내부를 300줄로 읽는" 학습·개념 확인용.
- **6개월 영향력**: 낮음(도구로서) — 이미 지식 자산으로 흡수됨. [[llms-from-scratch]]와 함께 "LLM을 밑바닥부터" 교육 계보의 정전(canon).
- **대체 관계**: 자기 사촌 **nanochat**이 상위 호환. [[pytorch]] 위에서 돌아가는 최소 학습 루프.
- **허와 실**: 과장 없음 — 순수 교육/해킹 베이스. "medium-sized GPT" 이상은 대상 아님.
- **액션**: 스크래치 학습 개념이 필요할 때 model.py 정독. 실제 실험은 nanochat로.

## 관련 페이지
- [[Andrej Karpathy]] — 저자, LLM-Wiki 철학 창안자
- [[llms-from-scratch]] — 밑바닥부터 LLM 교육 계보
- [[pytorch]] — 하부 프레임워크
- [[AI-For-Beginners]] — 교육 레퍼런스 급등 계열
- [[cs249r_book]] — ML 시스템 교재
- [[ai-news]]

## 원본
- 출처: https://github.com/karpathy/nanoGPT
- GitHub: ⭐60,816 (2026-07-06, 당일 +246)
- 상태: **deprecated** — 후속 nanochat 권장(2025-11 공지)
- 신뢰도: ⭐⭐⭐⭐⭐ (Karpathy 교육 표준 / deprecated 명시)
