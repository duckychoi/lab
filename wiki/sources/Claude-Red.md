---
title: claude-red — 공격보안 스킬 라이브러리
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, offensive-security, claude-code, 실카운트-일치]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [SnailSploit/Claude-Red]
---

# claude-red — 공격보안 스킬 라이브러리

**GitHub**: https://github.com/SnailSploit/Claude-Red · `SnailSploit/Claude-Red`
**지표(2026-09-13 API 실호출)**: ⭐**3,788** · fork **566** · 이슈 **12** · **Python** · **MIT** · 생성 **2026-03-04** · 푸시 **2026-08-30**
**드리프트**: raw ⭐3,787(+1) → API값 채택. fork·이슈·라이선스 **일치**

> [!insight] ✅ 핵심 인사이트 — **배지 수치가 실제와 정확히 일치한 첫 사례**
> 볼트는 09-11 [[vercel-skills]] 에서 *"79개는 자기보고이고 검증되지 않았다"* 를 기록했고, 그 이후 배지 수치를 전부 실카운트로 대조해 왔다. 이번엔 **일치한다**.
> - 배지 `skills-78` → git tree 전체 조회(truncated=**false**) 결과 **`SKILL.md` 실파일 78개**
> - 배지 `categories-23` → `Skills/` 하위 **실디렉토리 23개**
>
> 🎯 **이 배치에서 산문/배지/실물이 셋 다 일치한 유일한 레포다.** 같은 배치 [[CloddsBot]] 은 배지 `skills-121+` 와 산문 *"118+ strategies"* 가 세는 대상부터 다르다. **차이는 규모가 아니라 습관이다** — 같은 스킬 묶음 형식인데 한쪽은 맞고 한쪽은 안 맞는다.

**검증된 23개 카테고리(실디렉토리)**: `active-directory` `ai` `api` `auth` `cicd` `cloud` `container` `crypto` `exploit-dev` `forensics` `fuzzing` `infrastructure` `iot` `mobile` `network` `post-exploitation` `privesc` `recon` `social-engineering` `supply-chain` `utility` `web` `wireless`

> [!note] 구조 — 온디맨드 로딩
> SQLi·shellcode·EDR 우회·ADCS 등 공격면별 방법론을 `SKILL.md` **한 장씩**으로 구조화하고, 대화 트리거로만 로드한다. 78장을 항상 물리지 않는다는 점이 설계 핵심 — **컨텍스트 예산을 스킬 수와 분리**한 형태.

> [!warning] 2주 이상 정체
> 최종 푸시 **2026-08-30**. 이 배치 GitHub 5건 중 **유일하게 2주 이상 멈춰 있다**(pentagi 09-10 · YuE 09-11 · CloddsBot 09-12 · no-ai-slop 09-02).
> 공격보안은 기법 수명이 짧은 도메인이라 **정체가 곧 감가**다. 78개 중 몇 개가 아직 유효한지는 별도 검증이 필요하다.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐3,788 · MIT 본문 1,085B · **실카운트 78/23 일치** → **high**
- **즉시 활용**: ⚠️ **구조만.** 내용은 허가된 대상이 있어야 쓸 수 있다. 다만 **"방법론을 스킬 한 장으로 쪼개 온디맨드 로드"** 라는 형식 자체는 볼트 도메인(리서치 절차)에 그대로 이식 가능.
- **6개월 영향력**: [[에이전트-스킬]] 이 *"프롬프트 모음"* 에서 **"카테고리 트리 + 온디맨드 로딩"** 으로 성숙하는 흐름의 사례.
- **허와 실**: 과장이 없다. 다만 **정체 2주**가 실질 리스크.
- **액션**: 카테고리 트리 구조를 볼트 스킬 구성의 레퍼런스로 기록.

> [!question] 미해결
> 78개 스킬의 **품질 분산**은 측정되지 않았다. 개수 일치는 확인했지만 *"78개가 다 쓸 만한가"* 는 다른 질문이다 — [[단위-불일치]] 가 해결돼도 **품질 검증은 남는다**.

## 관련 페이지
- [[pentagi]] — 같은 배치 공격보안. **PentAGI는 실행기, 이쪽은 방법론 문서**
- [[vercel-skills]] — 배지 자기보고 문제의 원 사례. 이번 건은 그 반대 결과
- [[no-ai-slop]] — 같은 "SKILL.md 묶음" 형식
- [[에이전트-스킬]] · [[단위-불일치]]

## 원본
- 출처: https://github.com/SnailSploit/Claude-Red
- 신뢰도: ⭐⭐⭐ (API 실호출 + git tree 전수 실카운트 78/23 대조)
