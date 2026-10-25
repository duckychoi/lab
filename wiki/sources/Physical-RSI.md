---
title: "Toward Recursive Self-Improvement in Physical AI — RSI 서베이가 스스로 결론낸다: 물리 연구 중 '재귀에 귀속되는 이득'을 분리한 것은 아직 없다"
type: source
domain: ai-news
tags: [ai-news, hf-paper, survey, rsi, robot-learning, embodied-ai, 수치0, 리딩리스트]
created: 2026-10-25
updated: 2026-10-25
sources: []
reliability: medium
---

# Toward Recursive Self-Improvement in Physical AI

**HF**: https://huggingface.co/papers/2610.29677 · arXiv 2610.29677 · **NUS**(National University of Singapore) · published 2026-10-21
**실측(2026-10-25 KST · `api/papers`)**: upvote **57**(수집기 일치 · 10-23 목록 6위) · 저자 Meng Luo · Zechen Bai · Shanqing Xu 외 · `githubRepo` = **`Physical2RSI/Awesome-Physical2RSI`**(🔴 코드가 아니라 리딩리스트)
**신뢰도**: ⭐⭐⭐ (서베이 · 실험 없음 · 결론이 자기 한정적이라 과장 위험 낮음)

> [!insight] 🏆 핵심 인사이트 — **RSI 를 제목에 단 논문이 RSI 의 부재를 결론으로 적었다**
> 초록 원문: *"Some systems also change the improver's knowledge or tools, but **the physical studies reviewed here have yet to isolate gains attributable to recursion**."*
> 🎯 [[RSI-프레이밍]](09-18 신설)의 판별 규칙 *"RSI 문구의 길이와 본문 정량성이 반비례"* — 이 초록은 **RSI 가 전문(全文)을 채우고 수치는 0개**다 ⇒ 규칙과 **부합(n=3)**. 🔴 **그러나 방향이 다르다**: 앞선 2건은 RSI 를 **미래형 동기**로 썼고, 이 서베이는 RSI 를 **아직 입증되지 않은 것**으로 명시한다 ⇒ **정직한 RSI 서술의 첫 사례.** 규칙을 "수치 없음 = 과장"으로 쓰면 오판한다 — 서베이는 원래 수치가 없다.

## 도메인별 추출 (ai-news)
- **신뢰도**: upvote 57 · 서베이 · 코드 = Awesome 리스트(10-16 Harness-RSI 사례와 같은 패턴: 프로젝트 URL 이 리딩리스트)
- **즉시 활용**: **YES(읽기)** — 이득이 이월되는 4조건이 평가 체크리스트로 쓸 만하다: *"feedback addresses remaining learning needs · the receiving component can use the change · its value survives changes in tasks or hardware · continued practice remains safe and affordable"*
- **6개월 영향력**: 중간 — [[임바디드-AI]] 쪽 RSI 주장의 반증 기준선
- **대체 관계**: 디지털 RSI([[Dream-RSI]] 류 · 코드 재작성 + 실행 테스트)와 물리 RSI 를 분리하는 기준
- **허와 실**: 과장 없음. 기존 연구는 *"concentrated in manipulation"* — 보행·이동은 공백
- **액션**: 같은 배치의 [[FRED]] · [[LaLa-World]] 를 이 4조건으로 대조(아래)

> [!note] 같은 배치 대조 — 4조건 중 "하드웨어 변경 후 가치 생존" 을 직접 측정한 것은?
> [[FRED]] — *"zero-shot environment generalization"* · 인간 영상 → 로봇 전이 50.0% ⇒ **과제 변경 생존**은 측정, 하드웨어 변경은 아님 · [[LaLa-World]] — 이종 데이터 공동학습 ⇒ 도메인 간 생존 측정. ⇒ **둘 다 RSI 가 아니라 1단(행동 개선)이다.** 서베이 결론과 일치.

## 관련 페이지
- [[RSI-프레이밍]] · [[Dream-RSI]] · [[임바디드-AI]] · [[VLA]] · [[월드모델]]
- 같은 배치: [[FRED]] · [[LaLa-World]] · [[microduck]] · [[flint-GGUF]](제작사명 "Recursive")
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2610.29677
- 신뢰도: ⭐⭐⭐ (HF upvote 57 · 서베이)
