---
title: context-mode — AI 코딩 에이전트 컨텍스트 윈도우 최적화
type: source
domain: ai-news
tags: [ai-news, context-window, token, optimization, coding-agent, sandbox, elastic-license, 캐시된-지표-신선도, 라이선스-미확정, 측정-미이행]
created: 2026-05-07
updated: 2026-10-11
sources: []
reliability: medium
---

# mksglu/context-mode

> [!update] 2026-10-11 갱신 — 🔴🔴 **볼트 기재값이 158일 묵었다: ⭐13,388 → ★26,503 (+98.0%)** · 🏆 **`NOASSERTION` 정체 확정 = Elastic License 2.0** · 🔴 **98% 클레임 5개월째 미실측**
> ✅ **볼트 독립 GitHub API 재조회**(HTTP 200): ★**26,503** · fork **1,905** · `open_issues` **342**(금일 배치 최다) · TypeScript · created **2026-02-23** · pushed **2026-10-11**(활동 중) · topics `claude-code-hooks, claude-code-plugins, claude-code-skill, antigravity`.
>
> 🔴🔴 **[[캐시된-지표-신선도]] 볼트 내부 2번째 실측 사례다.**
> 본 페이지는 **⭐13,388 (2026-05-06 기준)** 을 적어 두고 그대로 있었다. **158일 뒤 실측 26,503 = +13,115 (+98.0%, 거의 2배 · 일평균 약 83)**.
> ⇒ 📌 **선행 사례는 10-10 [[claude-mem]](6개월 +60.1%)이고, 이번은 기간이 더 짧은데 증가율이 더 크다.**
> 🎯 **그리고 이 페이지는 수집 단계에서 발견됐다** — 볼트 자기한계 목록의 *"1,236개 소스 중 몇 건이 묵었는지 모른다"* 항목에 **해당하는 페이지를 수집기가 1건 찾아 줬다.** ⚖️ **즉 볼트는 아직 자기 기록의 나이를 스스로 점검하지 못하고 외부 지적에 의존한다** → 아래 action.
>
> 🏆🏆 **새 정보 1 — 수집기 판정 요청 해소: `NOASSERTION` 은 "라이선스 없음"이 아니라 Elastic License 2.0 이다**
> 수집기는 *"라이선스 `NOASSERTION` — 표준 SPDX 로 해석되지 않는다. 재배포 조건을 API 응답만으로는 확정할 수 없다"* 며 **볼트 판정을 요청했다.**
> ✅ **볼트가 `api.github.com/repos/mksglu/context-mode/license` 로 원문을 직접 받았다(HTTP 200 · 3,840자)**: **`Elastic License 2.0 (ELv2)` · Copyright 2026 Mert Koseoglu.**
> **핵심 제약 2건(원문)**: ① *"You may not provide the software to third parties as a **hosted or managed service**, where the service provides users with access to any substantial set of the features or functionality of the software."* ② *"You may not move, change, disable, or circumvent the license key functionality..."*
> ⇒ 🔴🔴 **따라서 이것은 오픈소스가 아니라 source-available 이다.** 📌 **볼트 소유자 축(영상 SaaS)에서 결정적이다 — 본 도구를 제품에 넣어 호스팅 서비스로 제공하면 라이선스 위반 소지가 있다.** ⚖️ **개인 로컬 사용은 제약 대상이 아니다.**
> 🆕 **볼트 판정(수집기 요청 응답): `NOASSERTION` 은 "라이선스 없음"으로 적으면 틀린다 — 반드시 `/license` 엔드포인트로 원문을 1회 확인한다.** 📌 **비용이 API 1회이고, 본 사례에서 "MIT 급으로 써도 된다"는 오판을 막았다.** ⇒ 상설 해소 경로에 **⑧ `GET /repos/{owner}/{repo}/license`** 를 추가한다.
> 🔴 **그리고 이것은 본 페이지의 기존 기재를 정정한다** — 구 버전은 *"신뢰도 ⭐⭐⭐⭐"* 와 *"즉시 활용: YES"* 를 적었고 **라이선스를 언급하지 않았다.** `reliability` 를 `high` → **`medium`** 으로 내린다(성능 클레임 미검증 + 상용 제약).
>
> 🔴 **새 정보 2 — 98% 절감 클레임이 5개월째 미실측이다.**
> 구 버전 action 은 *"context-mode 설치 → before/after 토큰 비교"* 였다. ⚖️ **158일이 지났고 실행되지 않았다.**
> ⇒ 📌 **이것이 볼트 *"외부 코드 실행 0건 20배치 연속"* 적자의 구체적 비용이다** — 적자가 추상적 지적이 아니라 **특정 수치 1건(98%)이 5개월간 검증되지 않은 상태**로 나타난다.
> 🎯 **[[관심-검증-역상관]] 적용**: ★가 2배 되는 동안 **검증은 0회**였다.
>
> 📌 **새 정보 3 — `open_issues` 342 = 금일 배치 최다**(★ 대비 **1.29%**). 🔴 **순수이슈/PR 분해 미실행**(볼트 5배치 연속 누락 항목). ⚖️ **342 를 "품질 문제"로 읽을 수도 "활발한 사용"으로 읽을 수도 있고, 분해 없이는 판정 불가다.**
> 📌 topics 의 **`antigravity`** 는 볼트 미확인 용어다 — 추정하지 않는다.
>
> > [!action] 당장 할 것 (갱신)
> > ⬜ 🔴 **98% 절감 실측** — 5개월 이월. ⚖️ **단 ELv2 확인 후에는 "제품 탑재"가 아니라 "로컬 검증"으로 범위를 좁혀 실행한다.**
> > ⬜ 🔴 **볼트 전수 나이 점검 스크립트 1회 집행** — `updated:` 가 90일 이상 된 소스를 전부 뽑는다. 📌 **본 페이지와 [[claude-mem]] 2건이 외부 지적으로 발견됐으므로 3번째를 기다리지 말고 볼트가 센다.** 비용은 `grep` 한 번이다.
> > ⬜ `open_issues` 342 분해.

> [!insight] 핵심 인사이트
> 툴 출력을 샌드박스 처리하여 컨텍스트 윈도우 토큰을 98% 절감. Claude Code · Cursor · Gemini CLI 등 14개 플랫폼 지원. 에이전트 비용의 핵심 병목인 "툴 출력 토큰 팽창"을 직접 해결.

**GitHub**: https://github.com/mksglu/context-mode  
**스타**: ★**26,503** (볼트 API 실측 **2026-10-11**) — 🔴 **구 기재값 ⭐13,388 (2026-05-06) 은 158일 묵은 값이었다**  
**라이선스**: **Elastic License 2.0 (ELv2)** — 🔴 **오픈소스 아님 · 호스팅 서비스 제공 금지**(볼트 원문 확인)  
**신뢰도**: ⭐⭐ (★는 실측 / **98% 절감 클레임 5개월째 미검증 · 상용 제약 있음**)

## 도메인별 추출

- **신뢰도**: 🔴 **26.5K 스타**(13K 는 구값) — 158일 +98.0%. **98% 절감 클레임은 5개월째 실측 0회.** 라이선스 ELv2 = source-available.
- **즉시 활용**: ⚖️ **조건부 YES — 개인 로컬 사용은 가능하고 제품 탑재는 ELv2 제약 대상이다.** 장기 세션의 컨텍스트 초과·비용 문제를 직접 겨냥한다.
- **6개월 영향력**: 에이전트 컨텍스트 관리가 표준 미들웨어로 자리잡으면 장시간 코딩 세션 가능. [[claude-mem]] · [[beads]]와 유사 문제 다른 접근
- **대체 관계**: [[claude-mem]](세션 간 기억), [[beads]](메모리 레이어) 대비 실시간 토큰 압축에 집중
- **허와 실**: 🔴 **98% 절감은 5개월째 미검증이다** — 최적 케이스일 가능성이 높으나 **볼트가 확인하지 않았으므로 허인지 실인지 모른다.** 샌드박스가 에이전트 판단에 필요한 정보를 가릴 가능성도 미검증. 🆕 **새로 확인된 실질 제약은 성능이 아니라 라이선스다.**
- **액션**: Claude Code 세션에 설치 후 실제 토큰 절감률 측정

> [!action] 당장 할 것
> context-mode 설치 → Claude Code 장시간 작업 세션에서 토큰 사용량 before/after 비교.

> [!warning] 주의
> 98% 절감 클레임은 검증 필요. 툴 출력 샌드박스가 에이전트 판단에 필요한 정보를 가리는 경우 없는지 확인.

## 관련 페이지
- [[캐시된-지표-신선도]] — 🔴 **볼트 내부 2번째 실측 사례**(158일 +98.0%)
- [[관심-검증-역상관]] — ★ 2배 · 검증 0회
- [[claude-mem]] — 선행 1번째 사례(6개월 +60.1%)
- [[Claude-Code-워크플로우]]
- [[claude-mem]]
- [[beads]]
- [[에이전트-메모리-레이어]]
- [[Terminal-Agent-Context-Compression]]

## 원본
- 출처: https://github.com/mksglu/context-mode
- 수집: 2026-05-06 최초 · **2026-10-11 자동수집 재관측**(158일 만의 2번째 관측)
- 신뢰도: ⭐⭐ (★·fork·issues·라이선스 **볼트 API 실측** / 🔴 **98% 절감 클레임 5개월째 미검증 · 코드 미실행 · `open_issues` 미분해**)
- 확인 범위: ✅ **볼트 독립 조회 2건** — `api.github.com/repos/mksglu/context-mode`(HTTP 200) · `.../license`(HTTP 200 · 원문 3,840자 수신 → **Elastic License 2.0 확정**). 🔴 README 미재열람 · 설치·실행 0회.
