---
title: all-agentic-architectures — 35개 에이전틱 패턴을 동일 계약의 클래스로 패키징
type: source
domain: ai-news
tags: [ai-news, github-trending, agent, langgraph, design-pattern, interface, MIT]
created: 2026-09-15
updated: 2026-09-15
sources: []
reliability: medium
---

# GitHub: FareedKhan-dev/all-agentic-architectures — 패턴을 교체 가능하게

**URL**: https://github.com/FareedKhan-dev/all-agentic-architectures
**지표(2026-09-15 API 실측)**: ★**4,507**(raw 기록과 정확히 일치 · 당일 +217) · 포크 768 · 미결이슈 **10** · **MIT** · Jupyter Notebook · 생성 2025-09-24 · 최종푸시 **2026-06-22**

> [!insight] 핵심 인사이트
> Reflexion·LATS·GraphRAG·MemGPT·Voyager 등 문헌상 주요 에이전틱 패턴 **35종**을 **동일한 `.run(task)` 인터페이스와 `ArchitectureResult` 반환형**을 갖는 LangGraph 상태머신 클래스로 통일했다. **클래스만 교체하면 하위 코드를 바꾸지 않고 패턴을 갈아끼울 수 있다.**
>
> 🎯 **이게 왜 드문가**: 에이전트 패턴 비교 글은 많지만 대부분 **산문**이다. 산문은 "어느 게 더 나은가"를 **실험으로 물을 수 없다.** 동일 계약으로 묶는 순간 패턴이 **교체 가능한 변수**가 되고, 비로소 A/B가 가능해진다. [[firstmate]] 가 같은 일을 **파일시스템 레벨**에서 한다면 이건 **타입 레벨**에서 한다.

> [!insight] 기술적 주장 — deterministic-picker 패턴
> **LLM은 불리언·이넘 같은 범주형 특징만 확정하고, 결정 신호 합성은 Python이 수행**한다. LLM-as-Scorer의 평탄대역(점수가 뭉개지는) 병리를 회피하는 설계다.
> 자체 기술에 따르면 **35개 중 13개에 적용, 9개는 설계상 면역**. 📌 **뒤집어 읽으면 나머지 13개는 이 방어가 없다.**
> 🔗 [[요약자와-판정자-분리]] 와 같은 계열 — *판정을 LLM에게 맡기지 말고 결정 규칙을 코드로 내려라.*

> [!warning] 🔴 성립 조건 — README 배지는 **전부 자체 보고다**
> `283 테스트 통과 · 17 벤치 태스크 · 9 프로바이더 · 모킹 0회` — **외부 검증이 아니다.**
> 볼트는 [[vercel-skills]] 이후 배지 실카운트 대조를 해 왔고, [[SnailSploit]] 에서 첫 완전 일치를 확인한 바 있다. **이 레포의 배지는 아직 대조하지 않았다** — 테스트 수·벤치 태스크 수는 git tree에서 셀 수 있으므로 다음 배치 대조 대상으로 등록한다.

> [!warning] 🔴 지는 축 — 최종 푸시 2026-06-22 = **85일 정체**
> 이 배치 GitHub 5건 중 최장이다. 볼트 09-14 규칙에 따라 **임계선 판정은 걸지 않는다**(이 레포의 과거 푸시 간격 관측 기록 없음). 다만 **미결이슈 10건 = ★4,507 대비 0.2%** 로 이 배치 최저이므로, 정체가 *방치*인지 *완결*인지는 **이슈 축만 보면 후자에 가깝다.**

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ MIT·★4,507·이슈 극소. 배지 미대조·85일 정체 → medium
- **즉시 활용**: **YES.** 35개 패턴의 **실행되는** 구현이 한 계약 아래 있다는 것만으로 레퍼런스 가치가 높다. 노트북이 실행된 상태로 커밋돼 있어 출력까지 읽힌다.
- **대체 관계**: [[ai-engineering-hub]] 와 **정면 대조군**이다 — 같은 "예제 모음"인데 **재사용성 급이 다르다**(통일 계약 vs 디렉토리 복사).
- **액션**: star + deterministic-picker 적용 13개 / 미적용 13개 목록 추출

## 관련 페이지
- [[ai-engineering-hub]] — 재사용성 대조군(같은 배치)
- [[firstmate]] — 교체 가능성을 다른 레이어에서 푼 사례
- [[요약자와-판정자-분리]] · [[AI-에이전트-프레임워크]] · [[에이전트축-분기]]
- [[ai-news]]

## 원본
- 출처: https://github.com/FareedKhan-dev/all-agentic-architectures
- 검증: GitHub API 실호출(2026-09-15). **드리프트 0(완전 일치)**
- 신뢰도: ⭐⭐
