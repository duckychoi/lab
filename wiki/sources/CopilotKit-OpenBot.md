---
title: "CopilotKit/OpenBot — 셀프호스팅 "AI 동료" 워크스페이스 (템플릿은 MIT, 핵심 의존성은 별도 라이선스)"
type: source
domain: ai-news
tags: [ai-news, github-trending, agent-workspace, governance, copilotkit, license]
created: 2026-11-14
updated: 2026-11-14
sources: [https://github.com/CopilotKit/OpenBot]
reliability: medium
---

**레포**: [CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot) · ★**12,166** · fork 1,497 · MIT(GitHub API) · TypeScript · repo id 1336502227 · created 2026-08-17 · pushed 2026-11-14T09:00Z (볼트 실측). 수집기 11-13 ★11,917.

> [!note] 이름 충돌 — 볼트의 [[openbot]] 과 다른 레포
> [[openbot]] 은 `nightly-labs/openbot`. 이 페이지는 `CopilotKit/OpenBot`(레포 ID 1336502227). 옵시디언 링크는 대소문자를 가리지 않으므로 파일명을 `CopilotKit-OpenBot` 으로 뒀다 → [[정규명-우선-중복검사]].

## 핵심 인사이트
> [!insight] "모든 행동이 일어나기 전에 결정된다" — 에이전트 거버넌스를 API 단에 둔 구조
> 봇마다 브라우저 · 파일 · 도구가 있는 "컴퓨터"를 붙이고, 사인인 · 역할 · 도구 권한 · 승인 · 감사를 API 에서 강제한다. 모델은 OpenAI · Claude · Gemini · OpenAI 호환, 외부 에이전트는 AG-UI, 도구는 MCP. 프런트는 Mac/Windows/웹/iOS/Android/Slack/Teams, 백엔드는 Kubernetes + PostgreSQL(수집기 판독).

> [!warning] "오픈소스"의 범위 — README 105–115행 (볼트 직접 판독)
> *"The OpenBot application template is open source under the MIT license … It uses **CopilotKit Intelligence**, which is separately licensed."*
> | 실행 위치 | CopilotKit Intelligence 라이선스 |
> |---|---|
> | 노트북 · 개인 실험 | 무료 로컬 라이선스 필요 |
> | Kubernetes 평가 | 무료 trial 라이선스 필요 |
> | Kubernetes · 운영 | production 라이선스 필요(유료 요금제) |
>
> 로컬 라이선스 갱신에도 인터넷이 필요하다(115행). GitHub API 의 `MIT` 는 템플릿만 가리킨다 → [[파생표기-함정]](API 라이선스 필드가 실제 사용 조건을 대표하지 않는다).

## 도메인별 추출 (ai-news)
- **신뢰도**: ★12,166 · 3개월 차 · 성능·안정성 수치 없음.
- **즉시 활용**: NO — 개인 볼트 규모에는 과하고, 핵심 계층이 라이선스 토큰에 묶인다.
- **6개월 영향력**: "에이전트에게 컴퓨터를 주고 승인·감사를 강제"하는 구조는 [[OpenSandbox]](실행 격리)와 함께 사내 에이전트 도입의 기본 요건이 되어 간다.
- **대체 관계**: 직접 대체 대상 없음. 설계 참고용.
- **허와 실**: 템플릿은 열려 있고 지능·메모리·거버넌스 서비스는 닫혀 있다.
- **액션**: 없음. 승인·감사 흐름만 참고.

## 관련 페이지
- [[openbot]](다른 레포) · [[OpenSandbox]] · [[파생표기-함정]] · [[정규명-우선-중복검사]] · [[AI-에이전트-프레임워크]]

## 원본
- 출처: https://github.com/CopilotKit/OpenBot
- 확인 범위: GitHub API 메타 · README 70 · 97 · 105–115행 직접 판독 · 🔴 기능 목록은 수집기 판독 · 실행 미확인
- 신뢰도: ⭐⭐ (★12,166 · 측정 0 · 상용 의존)
