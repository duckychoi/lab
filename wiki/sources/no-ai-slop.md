---
title: no-ai-slop — AI 문체 패턴 제거 스킬
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-skill, writing, claude-code, 자기제한-명시]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [petergyang/no-ai-slop]
---

# no-ai-slop — AI 문체 패턴 제거 스킬

**GitHub**: https://github.com/petergyang/no-ai-slop · `petergyang/no-ai-slop`
**지표(2026-09-13 API 실호출)**: ⭐**8,865** · fork **655** · 이슈 **22** · **MIT** · **2026-07-07 생성**(2개월 만에 8.8k) · 푸시 2026-09-02
**드리프트**: raw ⭐8,859 vs API **8,865**(+6)

> [!insight] 핵심 인사이트 — **탐지기가 아니라 검출기다. 그 구분을 저자가 먼저 한다**
> README 원문: *"The skill quotes every slop pattern it found **without guessing whether AI wrote the text**."*
> 🎯 이 한 문장이 제품 범위를 정확히 자른다. **"이 글 AI가 썼나?"에는 못 쓰고, "이 글에 상투 패턴이 있나?"에만 쓴다.** AI 판별 시장이 과열된 시점에 **판별을 하지 않겠다고 명시**한 것 → [[자기제한-명시]]의 모범 사례.
> 볼트가 반복 관찰한 방향의 반대다 — 대부분의 레포는 할 수 있는 것보다 크게 말한다. 이건 **할 수 있는 것보다 작게 말한다.**

> [!note] 실측 구조 — 정말 "SKILL.md 한 장"인가
> git tree 전체 조회(truncated=**false**) 결과 **총 14파일**. 그중 `SKILL.md` 는 **정확히 1개**(`skills/no-ai-slop/SKILL.md`).
> ✅ raw의 *"SKILL.md 한 장"* 주장 **확인**.
> ⚠️ 다만 GitHub `language` 가 **Python** 으로 잡히는 이유는 `scripts/build_plugin.py` 가 있기 때문이다 — **플러그인 빌드 스크립트**다. raw는 이걸 언급하지 않았다. 순수 문서 레포가 아니라 **문서 + 배포 스크립트** 구조다.

> [!warning] README가 20+ 중 10개만 열거한다
> README에 열거된 것은 **10개**: 이진 대조 · 목 가다듬기 서두 · 가짜 통찰 · 콜론 공개 · 극적 단문 · 피상 분석 · 중요성 과장 · 모호한 출처 · 동의어 돌려쓰기 · 가짜 심오 마무리.
> 나머지는 `skills/no-ai-slop/SKILL.md` 안에만 있고 **README에는 없다.** → 배지·설명의 "20+"를 검증하려면 SKILL.md를 직접 읽어야 한다. [[단위-불일치]] 예방선.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐8,865 · MIT · 파일 14개 실카운트 → **high**(규모가 작아 전수 검증이 쉬운 유형)
- **즉시 활용**: ✅ **YES.** 볼트 자신의 산출물에 바로 적용 가능하다. 볼트 페이지는 콜아웃·강조·단문을 많이 쓰는데, 그중 *"극적 단문"·"중요성 과장"·"가짜 심오 마무리"* 는 **이 볼트가 실제로 범하는 패턴**이다.
- **6개월 영향력**: 스킬이 *규칙 문서 한 장* 으로 유통되는 형태가 굳어지는 중 → [[에이전트-스킬]] 계보.
- **대체 관계**: 별도 린터 불필요. Claude Code·ChatGPT·Codex에 그대로 설치.
- **액션**: SKILL.md 전문을 읽고 **볼트 문체 규칙에 편입 검토**(actionable 등재).

## 관련 페이지
- [[에이전트-스킬]] · [[자기제한-명시]] · [[단위-불일치]]
- [[Claude-Red]] — 같은 "SKILL.md 묶음" 형식, 반대 도메인
- [[Claude-Code-워크플로우]]

## 원본
- 출처: https://github.com/petergyang/no-ai-slop
- 신뢰도: ⭐⭐⭐ (API 실호출 + git tree 전수 + README 원문 대조)
