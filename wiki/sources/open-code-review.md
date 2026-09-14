---
title: open-code-review — 결정론 파이프라인 + LLM 에이전트 하이브리드 코드리뷰 (Alibaba)
type: source
domain: ai-news
tags: [ai-news, github-trending, code-review, llm-agent, static-analysis, alibaba, go, ci-cd]
created: 2026-07-26
updated: 2026-07-30
sources: []
reliability: high
---

# alibaba/open-code-review (GitHub ⭐16,303)

> [!update] 2026-09-14 갱신 — ⭐**24,055**(46일 **+7,752 · +47.6%**) · 🔴 중복 재배달
> **GitHub API 실호출(2026-09-14)**: ⭐**24,055**(raw 24,042 대비 **+13**) · fork **1,772**(raw 일치) · 이슈 **147** · **Apache-2.0**(일치) · **Go**(일치) · created 2026-05-18(일치) · **pushed 2026-09-14 = 당일 푸시**
> 🔴 **신규 아님.** 이 페이지는 **2026-07-26 생성 · 07-30 갱신**(당시 ⭐16,303). raw가 *"볼트 미보유"* 로 오판 → [[백필-우회]]
> 📈 **46일 만에 16,303 → 24,055 (+7,752 · +47.6%)**. 이슈도 함께 늘었다(추정 증가) — **스타와 이슈가 같이 느는 것은 [[OpenMontage]] 의 "스타만 느는" 패턴과 반대**로, 실사용이 따라붙고 있다는 신호다.
>
> 📌 **새로 확인된 것 — 아키텍처 분업의 근거를 저자가 직접 적는다**
> 결정적(deterministic) 코드가 맡는 것: **파일 선별 · 관련 파일 번들링 · 룰 매칭 · 코멘트 위치보정**. LLM 에이전트가 맡는 것: **동적 판단 · 컨텍스트 수집**.
> 저자가 겨냥한 실패 3종을 README에 직접 명시: *대규모 변경 시 일부 파일만 골라 리뷰 · 지적 위치(줄번호/파일)의 **드리프트** · 프롬프트 미세 변동에 따른 **품질 요동***
> 번들마다 **격리 컨텍스트 서브에이전트**로 분할정복. `ocr` CLI, npm 전역 설치. **Git ≥2.41 필요**, LLM 프로바이더 별도 설정 필수(위임 모드 제외). **OpenSSF Best Practices Gold.**
>
> 🎯 **분업 기준이 명확하다 — "정답이 있는 것은 코드, 없는 것은 LLM"**. 줄번호 보정은 정답이 있고, 이 코드가 나쁜지는 없다. 볼트 [[요약자와-판정자-분리]] 의 코드리뷰 판본이며, [[MetroLLM-Bench]] 의 Tier1/Tier2 분리와 **같은 구조**다.
> 🔴 **raw가 가져온 한정어 — 채택한다**: **벤치마크가 이미지 파일(`imgs/benchmark-en.png`) 하나뿐이고 본문 수치가 0개다.** 성능 우위 주장은 **인용 금지**. [[AuK]]·[[VibeVoice-ASR-Streaming-7B]] 의 `## Performance`=이미지 패턴이 **세 번째로 반복**됐다 — 이제 단발 사례가 아니라 **관행**으로 봐야 한다.

> [!update] 2026-07-30 갱신 — ⭐16,303 (당일 +359)
> ⭐**16,303**(2026-07-30 자동수집·API 실검증, 당일 +359, Apache-2.0) ← 15,242(07-28). 나흘 새 +1,061로 하이브리드(결정론+LLM) 코드리뷰 채택 지속 확대. 결정론 룰셋(NPE·XSS·SQLi·thread-safety)+LLM 라인코멘트·~1/9 토큰·4모드 구조 유지.

> [!update] 2026-07-28 갱신 — ⭐15,242 (당일 +979, 급상승)
> ⭐**15,242**(2026-07-28, 당일 +979 급상승, WebFetch "15.2k" 일치) ← ⭐13,269(07-26). 이틀 새 급증 — 하이브리드 리뷰 수요 확산. WebFetch 재확인: **범용 에이전트 대비 ~1/9 토큰**으로 더 높은 정확도 주장, 리뷰 모드 4종(워크스페이스·브랜치 비교·단일 커밋·풀파일, git 히스토리 불필요), Claude Code·Codex·Cursor·OpenCode 통합·GitHub/GitLab/Gerrit CI 연동 재확인. 핵심 인사이트·액션 유지.

> [!insight] 핵심 인사이트
> [[Alibaba]] 오픈소스 **하이브리드 코드리뷰 도구** — "결정론적 파이프라인 + LLM 에이전트"를 한 파이프에 결합한다. ⭐13,269 (2026-07-26, WebFetch 실검증, Go, 2026-05-18 생성). 순수 LLM 리뷰가 흔들리는 지점(재현성·오탐)을 **파인튜닝된 내장 룰셋(NPE·thread-safety·XSS·SQL injection)** 이라는 결정론 층으로 잡고, 그 위에 LLM 에이전트가 **라인 단위(line-level) 코멘트**로 맥락 리뷰를 얹는 2층 구조가 핵심. OpenAI·Anthropic API 호환이라 백엔드 모델 교체가 자유롭고, "알리바바 사내 스케일에서 검증(battle-tested)"을 표방한다. 위키의 코드-에이전트 계보에서 [[code-review-graph]](그래프 컨텍스트 축소)·[[graphify]](코드→지식그래프)가 *리뷰 입력을 구조화*했다면, open-code-review는 *리뷰 판정 자체를 결정론+LLM으로 이중화*하는 축이다.

**GitHub**: https://github.com/alibaba/open-code-review
**스타**: ⭐13,269 (2026-07-26, WebFetch 실검증)
**신뢰도**: ⭐⭐⭐⭐ (Alibaba 공식·1.3만 스타·기능 README 실확인·Go, 단 사내검증 주장은 외부 재현 전)

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — [[Alibaba]] 공식 레포·⭐13,269(WebFetch 일치)·설명/기능 실확인 → high. "battle-tested at Alibaba scale"은 자체 주장이라 외부 도입 성과는 별도 검증.
- **즉시 활용**: YES(후보) — OpenAI/Anthropic 호환이라 기존 Claude/GLM 키로 바로 붙일 수 있고, 결정론 룰셋이 CI에 **재현 가능한 게이트**를 제공. 위키·스케줄 코드 산출물의 자동 사전리뷰로 실험 가능.
- **6개월 영향력**: "LLM만으로 리뷰"에서 "**규칙 결정론 + LLM 맥락**"의 하이브리드가 사내 도입 기준으로 자리잡을 가능성 — 오탐·비재현성 이슈로 순수 LLM 리뷰를 못 쓰던 조직의 진입로.
- **대체 관계**: 순수 LLM PR 리뷰봇 대비 **결정론 룰셋으로 재현성·특정 취약점(SQLi/XSS) 커버리지** 우위. [[code-review-graph]]·[[graphify]]와는 상보 — 이들은 컨텍스트를, open-code-review는 판정 파이프를 담당.
- **허와 실**: 내장 룰셋이 Java/보안 취약점(NPE·thread-safety) 중심이라 언어·도메인 편향 가능. Go 구현이라 자체 확장엔 Go 이해 필요. "사내 검증"은 성능 수치 미공개.
- **액션**: Anthropic 호환 모드로 소규모 레포에 붙여 **결정론 룰셋 히트율 vs LLM 코멘트 유용도**를 분리 측정 → 위키 코드 산출물 자동리뷰 게이트 편입 여부 판단.

> [!action] 당장 할 것
> open-code-review를 Anthropic/OpenAI 호환 백엔드로 소규모 레포에 연결 → 내장 룰셋(NPE·XSS·SQLi·thread-safety) 히트와 LLM 라인코멘트를 분리 로깅해 "결정론 층이 실제로 오탐을 줄이는가"를 실측.

## 관련 페이지
- [[Alibaba]]
- [[code-review-graph]]
- [[graphify]]
- [[aisuite]]
- [[ai-news]]

## 원본
- 출처: https://github.com/alibaba/open-code-review
- 스타: ⭐13,269 (2026-07-26, WebFetch 실검증), Go, 2026-05-18 생성·2026-07-26 최근 푸시
- 기능: 결정론 파이프라인 + LLM 에이전트, 라인 단위 코멘트, 내장 룰셋(NPE·thread-safety·XSS·SQL injection), OpenAI·Anthropic API 호환
- 신뢰도: ⭐⭐⭐⭐ (Alibaba 공식·스타/기능 실확인 high, 사내검증 주장 외부 재현 전)
