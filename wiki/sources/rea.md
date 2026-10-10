---
title: "rea — 바이너리까지 내려가는 역공학을 MCP로 에이전트에 붙인다"
type: source
domain: ai-news
tags: [ai-news, github-trending, mcp, reverse-engineering, agent-skills, binary-analysis, ctf]
created: 2026-10-10
updated: 2026-10-10
sources: []
reliability: medium
---

# rea — 당일 증분 1위, 그런데 측정 수치는 0개

**GitHub**: https://github.com/morluto/rea
**★56,977** (당일 **+14,927 = 10-10 배치 최대 증분 · 트렌딩 1위**) · fork 11,079 · watchers 185
**open_issues 136 = 순수이슈 97 + PR 39**(PR 비중 **28.7%**) · MIT · TypeScript · created 2026-04-14 · pushed 2026-10-10

> [!insight] 핵심 인사이트
> **이 배치에서 유일하게 "자기 결론의 근거와 한계를 함께 반환한다"고 설계를 선언한 도구다.** README: *"results include the evidence and limitations behind each conclusion"*.
> 🎯 볼트 [[측정도구-먼저-반증]] 과 직결된다 — 도구가 자기 출력의 불확실성을 1급 반환값으로 올린 형태다.
> ⚖️ **단 검증은 안 했다.** 실제로 한계를 적는지 확인하지 않았고, 선언과 구현의 일치는 미확인이다.

> [!warning] ★56,977 · 성능·정확도 수치 0개
> 역공학 **성공률·오탐률 측정이 README 에 없다.** 소스 없는 바이너리를 정적 분석한다는 주장의 정확도를 판정할 근거가 0이다.
> 📌 [[관심-검증-역상관]] 후보 — 당일 증분 1위(+14,927)와 검증 0이 같은 레포에서 만난다.

> [!insight] 배치 내부 교차 — `skills.sh` 가 배포 포맷으로 굳어간다
> 본 레포는 `skills.sh` 배지를 보유하고, **같은 날 트렌딩 AI 5건 중 3건이 같은 경로를 쓴다**([[rea]] · [[mattpocock-skills]] · [[diagram-design]]). 10-06 [[text-to-cad]] · [[t3code]] 의 연장선이다.
> ⇒ ⚖️ **"스킬"이 레포 단위 배포 포맷으로 수렴 중이라는 당일 관측.** → [[에이전트-스킬]]

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ★·fork·당일 증분은 API 실측이고 **능력 측정은 전무**하다. MIT 라이선스 명시.
- **즉시 활용**: **조건부 NO.** 네이티브 바이너리 분석은 기존 **Hopper/Ghidra/IDA 설치를 사용**하므로 외부 의존이 크다. JS/Electron 정적 분석만 엔진 없이 돌아간다.
- **6개월 영향력**: 에이전트가 "읽을 수 있는 것"의 경계가 소스에서 **배포 산출물**로 내려간다. 웹앱·Electron 앱이 분석 대상이 되면 경쟁 제품 분석의 비용 구조가 바뀐다.
- **대체 관계**: 수동 Ghidra/IDA 세션을 대체하지 않고 **그 위에 에이전트 제어면을 얹는다**(= [[t3code]] 가 코딩 에이전트에 한 것과 같은 층 구조).
- **허와 실**: 🔴 *"남의 앱 기능을 보고 내 제품에 만들어 넣는다"* 는 자기 서술과 topics 의 `ctf`·`decompiler`·`disassembler` 가 같은 README 안에 있다. **합법 리버싱과 복제의 경계를 README 가 구분하지 않는다.**
- **액션**: 아래.

> [!warning] 설치가 외부 바이너리 분석기 설치 권한을 요구한다
> `npx rea-agents setup` 이고 *"승인 시 Hopper 를 설치할 수 있다"* 고 적는다. **파이프-투-셸은 아니지만** 에이전트가 서드파티 분석 엔진을 설치하는 권한을 요구한다.
> 📌 Node.js **22.x(>=22.19)/24.x(>=24.11)/26+** 요구 = **버전 창이 좁다.**

> [!question] 미해결
> - *"근거와 한계를 함께 반환"* 이 실제 출력에서 확인되는가 — **미검증**(실행 안 함).
> - 역공학 정확도 측정이 **정말 없는지**, 아니면 별 문서에 있는지 미확인(README 만 읽었다).
> - 라이선스·ToS 측면: 분석 대상 앱의 EULA 와의 관계를 README 가 다루지 않는다.

## 관련 페이지
- [[측정도구-먼저-반증]] — 근거·한계 동반 반환 설계
- [[관심-검증-역상관]] — ★56,977 · 검증 0
- [[에이전트-스킬]] · [[지표-창길이]] — 절대값 1위([[mattpocock-skills]])와 증분 1위(본 레포)가 다른 레포다
- [[mattpocock-skills]] · [[diagram-design]] — 같은 날 `skills.sh` 경로 3건
- [[t3code]] · [[text-to-cad]] — 10-06 배치의 같은 배포 경로
- [[morluto]] · [[ai-news]]

## 원본
- 출처: https://github.com/morluto/rea
- 수집: 2026-10-10 자동수집 (ai-news)
- 검증: GitHub API 실측(★·fork·open_issues 분해 136=97+39 검산 통과) · README i18n 18개 언어(한국어 `README_ko.md` 포함)
- 신뢰도: ⭐⭐⭐
