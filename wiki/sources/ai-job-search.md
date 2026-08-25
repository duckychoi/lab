---
title: ai-job-search — Claude Code 기반 구직 자동화 프레임워크
type: source
domain: ai-news
tags: [ai-news, github-trending, claude-code, agent, job-search, latex, automation]
created: 2026-07-08
updated: 2026-08-25
sources: []
reliability: high
---

# MadsLorentzen/ai-job-search

**GitHub**: https://github.com/MadsLorentzen/ai-job-search
**지표**: ⭐**34,528** · 포크 **11,973** · 이슈 **8** · **Python** · **MIT** · 최종 푸시 **2026-08-23** — 전량 **GitHub API 실호출 검증**(2026-08-25) · 트렌딩 데일리 **3위** ← ⭐12,704·포크4.1k(07-08)
**라이선스**: MIT · **스택**: Claude Code(AI 백본) + Python 3.10+ + TypeScript/Bun(CLI) + LaTeX(moderncv)

> [!update] 2026-08-25 갱신 — ⭐**34,528**(12,704 → 3.45만·약 2.7배)·**이슈 8건**이라는 이례적 수치
> ⭐**34,528** (2026-08-25 **GitHub API 실호출 검증**) ← 12,704(07-08). 약 7주 **+21,824(약 2.7배)**. 당일 +434·트렌딩 **3위**·포크 **11,973**·최종 푸시 **2026-08-23**(활성).
> **가장 눈에 띄는 건 오픈이슈 8건이다.** 포크가 **11,973건**인데 이슈가 **8건** — 포크 대비 이슈 비율이 **0.0007건/포크**로, 같은 배치 [[hermes-agent]](0.75건/포크·이슈 35,603)와 **1,000배 규모의 차이**다.
> 이 격차는 두 가지로 읽힌다. (1) **구조적 이유**: 이 레포는 프레임워크가 아니라 **개인 머신에서 도는 워크플로 패키지**여서, 사용자가 포크해 자기 CV·자기 공고에 맞춰 고쳐 쓰고 **업스트림에 문제를 제기할 이유가 적다.** (2) **활동의 방향**: 포크 1.2만은 "쓰고 있다"의 증거이지만 이슈 8건은 "**함께 고치고 있지 않다**"의 증거이기도 하다 — 커뮤니티 형성이 아니라 **개별 복제 소비**에 가깝다.
> ⚠️ **효과는 여전히 미검증.** 공고 평가·CV 맞춤·커버레터·면접 준비를 자동화한다는 기능 서술은 있으나, **실제 채용 결과(서류 통과율·면접 전환율)가 개선된다는 근거는 레포에도 위키에도 없다.** ATS 호환성 체크 역시 *자체 체크*이지 실제 ATS 통과 보장이 아니다. 3.45만 스타는 **구직 자동화 수요의 크기**를 말해줄 뿐이다.

> [!insight] 핵심 인사이트
> [[anthropic-claude-code]] 위에 얹은 **end-to-end 구직 자동화 프레임워크**. 채용공고 평가 → CV/커버레터 LaTeX 맞춤 수정 → PDF 컴파일·레이아웃 검증 → ATS 호환성 체크 → 면접 준비까지를 에이전트로 처리한다. 핵심은 개별 도구가 아니라 **"Claude Code를 특정 실무 도메인(구직)에 통째로 특화시킨 워크플로우 패키지"** — [[awesome-claude-code]]·[[claude-skills]]로 이어진 "Claude Code = 배포 플랫폼" 흐름이 개인 실생활 유스케이스로 착지한 사례. **drafter-reviewer 이중 검수**(작성 에이전트 + 리뷰 에이전트)는 7/4 [[codex-plugin-cc]]의 "작성+리뷰 멀티에이전트" 패턴을 단일 벤더로 재현.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ (⭐12,704 당일 +2,514, MIT, README WebFetch 실측 — "built on Claude Code" 명시 확인)
- **즉시 활용**: 부분 YES — 프레임워크 자체보다 **구조**가 참고감. LaTeX 템플릿 치환 + drafter-reviewer 이중 검수 + PDF 레이아웃 자동 검증 루프는 내 문서 생성 파이프라인(이력·제안서)에 이식 가능.
- **6개월 영향력**: "Claude Code로 실무 도메인 앱을 통째로 싸는" 패턴이 표준화됨. 도구 판매가 아니라 **워크플로우 레시피 배포**가 오픈소스 단위가 됨을 재확인.
- **대체 관계**: 유료 이력서 첨삭·ATS 최적화 SaaS를 로컬 에이전트로 대체. 단 Claude Code 구독 종속.
- **허와 실**: 마케팅 걷어내면 = 잘 짜인 프롬프트/스킬 모음 + LaTeX 파이프. "AI가 알아서 취업"이 아니라 사람이 검수하는 반자동 도구.
- **액션**: drafter-reviewer 이중 검수 + PDF 레이아웃 자동 검증 루프만 발췌해 내 문서 생성 스킬에 적용 실험.

## 관련 페이지
- [[anthropic-claude-code]] — 이 프레임워크의 AI 백본
- [[awesome-claude-code]] — Claude Code 리소스 큐레이션 (동일 생태계)
- [[claude-skills]] — 스킬=배포 단위 흐름
- [[codex-plugin-cc]] — drafter-reviewer(작성+리뷰) 멀티에이전트 원형
- [[Claude-Code-워크플로우]]
- [[ai-news]]

## 원본
- 출처: https://github.com/MadsLorentzen/ai-job-search
- GitHub: ⭐12,704 (2026-07-08, 당일 +2,514), MIT, 포크 4.1k
- 신뢰도: ⭐⭐⭐ (라이브 스타·README WebFetch 실측)
