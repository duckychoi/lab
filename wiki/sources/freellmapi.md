---
title: "freellmapi — 34개 제공자 무료 티어를 OpenAI 호환 /v1 하나로. '월 74억 토큰'은 측정이 아니라 쿼터 합산이고, 무료판 카탈로그는 30일 늦다"
type: source
domain: ai-news
tags: [ai-news, github-trending, llm-router, openai-compatible, free-tier, failover, open-core, 카탈로그-지연]
created: 2026-10-25
updated: 2026-10-25
sources: []
reliability: low
---

# freellmapi

**GitHub**: https://github.com/tashfeenahmed/freellmapi
**실측(2026-10-25 KST)**: ★ **41,181**(수집기 일치) · MIT · TypeScript · created **2026-04-21**(6개월) · pushed 10-24 · README **61,136 B**(배치 최장) · TypeScript daily 19위(+715 today)
**신뢰도**: ⭐⭐ (★4.1만이나 핵심 수치는 자기 합산 주장 · 오픈코어)

> [!insight] 핵심 인사이트 — **간판 숫자 "7.4 billion tokens per month" 는 처리량이 아니라 남의 쿼터의 합이다**
> README 62행: *"Every serious AI lab now offers a free tier … **On its own each tier is a toy. Stacked together, they add up to roughly 7.4 billion tokens** per month"* ⇒ 산출 근거가 제공자별 무료 쿼터 합산이며 **실제 라우팅 처리량 측정이 아니다.** 쿼터는 *"change quotas without notice"*(README 자신) ⇒ 숫자 자체가 시간 함수.
> 🎯 **진짜 상품은 라우터가 아니라 카탈로그 피드다**: *"Free installs get the monthly snapshot, so a model reaches them **30 days after** it joins the live feed"* · 실시간 = **$19/yr**. ⇒ MIT 코드 + 유료 신선도 = **신선도를 파는 오픈코어**.

> [!warning] 리스크
> 다수 제공자 무료 티어의 자동 페일오버·키 회전은 **각 제공자 약관(다중 계정·자동화 제한)과 충돌 가능**. README 의 *"Keys are stored encrypted"* 외 약관 검토 언급은 열람 범위(README 전문)에서 확인 못 함.

## 도메인별 추출 (ai-news)
- **신뢰도**: ★41,181 · 6개월 · 논문 없음 · 핵심 수치 자기 합산
- **즉시 활용**: **조건부 YES** — 개인 실험·배치 요약 같은 저가치 대량 추론에 한정. 볼트 크론 리서치 에이전트의 보조 모델 후보로 볼 수 있으나 **응답 모델이 요청마다 바뀌면 [[주제재생성-중복]] 노트 품질 편차가 커진다**
- **6개월 영향력**: 중간 — 무료 티어 차익거래가 막히면(약관) 급락할 구조
- **대체 관계**: [[9router]] 와 같은 층(모델 라우터) · [[cindy]] 는 한 층 위(하네스)
- **허와 실**: 474 패밀리 · 635 엔드포인트는 카탈로그 규모이지 품질 지표가 아니다 → [[카탈로그-등가가정]]
- **액션**: 보류. 쓰더라도 볼트 판정 작업(정확도 필요)에는 쓰지 않는다

## 관련 페이지
- [[9router]] · [[카탈로그-등가가정]] · [[캐시된-지표-신선도]] · [[복합지표-분해]]
- 같은 배치: [[cindy]] · [[gemini-cli]] · [[claude-howto]]
- [[ai-news]]

## 원본
- 출처: https://github.com/tashfeenahmed/freellmapi
- 신뢰도: ⭐⭐ (GitHub 스타 41,181 · 자기 합산 수치)
