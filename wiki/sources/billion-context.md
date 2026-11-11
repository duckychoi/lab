---
title: "billion-context — 에이전트↔모델 API 사이 프록시가 소비된 대화를 계층 요약으로 바꿔 100K 창으로 장기 세션 유지 (LongMemEval-S 79.20% · 원문 회수는 약함)"
type: source
domain: local-llm
tags: [local-llm, github-trending, agent-memory, context-compression, proxy, claude-code]
created: 2026-11-11
updated: 2026-11-11
sources: [https://github.com/ranxianglei/billion-context]
reliability: medium
---

**레포**: [ranxianglei/billion-context](https://github.com/ranxianglei/billion-context) · ★**6,619** · fork 543 · open_issues **1,012**(이슈+PR) · 라이선스 API 표기 `NOASSERTION` · TypeScript · created 2026-08-06 · pushed 2026-11-11T08:58Z (GitHub API 볼트 실측)

## 핵심 인사이트
> [!insight] 압축 메모리는 "추론 사슬"은 지키고 "원문 한 줄"은 잃는다
> 저장소 내 벤치(`benchmarks/third-party-1500`, v0.1.202 — 볼트가 원문 표 확인): **LongMemEval-S** full 83.20% vs **bc 79.20%**(2위) vs 최고 RAG 62.60%, 평균 입력 106.0k → 30.5k. 반면 **MemoryAgentBench** 매크로 평균은 bc **43.54%** 로 bm25 53.70% · embedding-rerank 55.21% 보다 낮고, 긴 문맥 속 정확 회수(AR) EM 은 **27.00%**(bm25 59.00%). 1.48M 토큰 TTL 에서 full 은 전건 실패, bc 는 Recall@10 18.58%(bm25 22.08% 보다 낮음). 즉 "살아남는다"와 "잘 찾는다"는 다른 축이다.

> [!warning] 헤드라인이 유리한 비교만 골랐다 → [[표-부분인용]]
> - README 68행 요약은 *"+16.6% over best RAG"*(79.20 vs 62.60) · *"#1 on ContextBench"* · *"100% survival"* 을 내세운다. 같은 표의 **full 대비 −4.0%p** 와 **MemoryAgentBench 매크로 최하위권**은 README 요약에 없다(벤치 문서 본문에는 있다).
> - 슬로건 "5× fewer tokens" ↔ LME 실측 106.0k → 30.5k = **약 3.5배**(볼트 계산 · 수집기 지적과 일치).
> - 벤치 문서는 *"We conducted an independent, strictly controlled third-party evaluation"* 이라 쓰지만 프로젝트 저장소 안에 있고 평가 주체가 적혀 있지 않다 — 독립성 확인 불가(수집기 지적 · 볼트 문장 확인).
> - 라이선스: README 기준 MIT + 추가 조항(사용자 노출 제품은 사용 표기 의무)이라는 것은 **수집기 판독**이다. 볼트는 조항 원문을 검출하지 못했다 — 사용 전 LICENSE 직접 확인.

## 도메인별 추출 (local-llm)
- **실용성 판단**: 장시간 코딩 에이전트 세션의 토큰 비용 절감에는 측정 근거가 있다(LME 독립세션 비용 −71.1%, README). README 는 정상 세션 prefix 캐시 적중 95–97% · 압축 비용 ≤2% 를 제시(47·362행). 자체 프리프린트: 4.5개월 · 174,327 호출 · 누적 입력 18.76B 토큰에서 204,800 토큰 창 초과 0건(README 64행).
- **메모리 아키텍처**: 외부 DB·RAG 가 아니라 **컨텍스트 안의 계층 요약**(프록시가 스트림을 중계하며 이미 소비된 구간을 요약으로 교체, 필요 시 복원). [[mem0]] 식 추출 메모리, [[MemPalace]] 식 원문 저장과 다른 세 번째 계열.
- **Hermes 적용**: 조건부 — Anthropic/OpenAI 호환 API 를 쓰는 호스트(Claude Code·Codex·OpenCode·Gemini CLI·aider 등, 수집기)에 프록시로 끼운다. 긴 로그에서 특정 줄을 찾는 작업이 많다면 불리.
- **트레이드오프**: 정확도 −4.0%p(LME) ↔ 입력 토큰 약 3.5배 절감. 정확 문자열 회수는 크게 손해(AR 27.00%).
- **오픈소스 구현체**: npm `billion-context` 0.1.213(수집기). 0.1.x · 오픈 이슈+PR 1,012건으로 초기 단계.

> [!question] 미해결
> 모든 API 트래픽이 프록시를 지난다 — 키·대화가 로컬에만 머무는지, 요약 호출이 어디로 가는지 볼트 미확인.

## 관련 페이지
- [[mem0]] · [[MemPalace]] · [[claude-mem]] · [[context-mode]] · [[리서치-LLM-장기기억에이전트-메모리-아키텍처-SOTA-2026]] · [[표-부분인용]] · [[한정어-탈락]]

## 원본
- 출처: https://github.com/ranxianglei/billion-context
- 확인 범위: GitHub API 메타 · README 패턴 검색 · `benchmarks/third-party-1500/README.md` 표(83.20 · 79.20 · 43.54 · 55.21 · 27.00 · 18.58 · 22.08 · 106.0k/30.5k) · 🔴 ContextBench 세부 · 프리프린트 본문 · 코드 · 실행 미확인
- 신뢰도: ⭐⭐ (★6,619 · 자체 저장소 벤치 · 독립 재현 없음)
