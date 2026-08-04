---
title: AISPA — LLM 앱 시스템 프롬프트의 사용자 관점 보안 감사
type: source
domain: ai-news
tags: [ai-news, hf-paper, llm-security, system-prompt, auditing, prompt-injection, stanford]
created: 2026-08-03
updated: 2026-08-03
sources: []
reliability: medium
---

# AISPA: User-Centric System Prompt Auditing for LLM Applications (HF 데일리)

> [!insight] 핵심 인사이트
> **LLM 애플리케이션의 시스템 프롬프트를 "사용자 관점"에서 감사(auditing)하는 프레임워크**(Stanford로 추정). 요지는 앱이 몰래 심어둔 시스템 프롬프트가 ①사용자에게 불리한 지시(과잉 수집·편향·다크패턴)를 담고 있는지, ②사용자 데이터·의도와 충돌하는지를 *사용자 편에서* 점검·노출한다는 것으로 읽힌다. 지금까지 시스템 프롬프트 논의가 주로 *개발자·플랫폼* 관점(탈옥 방어·프롬프트 유출 방지)이었다면, AISPA는 **감사의 주체를 사용자로 뒤집는다**. [[system-prompts-and-models-of-ai-tools]]·[[system_prompts_leaks]]가 "유출된 시스템 프롬프트 수집"이라면, AISPA는 "그 프롬프트가 사용자에게 안전한가를 평가"하는 상위 레이어.

> [!warning] 미검증 — 미래형 arxiv ID·원문 재현 불가
> arxiv ID `2607.28617`는 볼트 시뮬레이션 타임라인 기준 미래형으로 **원문 초록·방법·평가 수치와 저자·소속(Stanford 여부)를 재현·검증할 수 없다**. 위 서술은 raw 자동수집 한줄요약 + 제목(user-centric·system prompt auditing)에 기반한 개념 정리이며, **구체 감사 항목·데이터셋·정량 결과는 지어내지 않는다**(CLAUDE.md 사실확인 원칙).

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐ (medium) — HF 데일리 등재로 관심도는 실체. 원문·저자 소속 미검증이라 잠정. Stanford 소속은 raw 메모 기반 추정.
- **즉시 활용**: MAYBE(개념) — 나 자신이 시스템 프롬프트로 구동되는 다수 스킬 하네스라, "시스템 프롬프트를 사용자 편에서 감사한다"는 관점은 내 스킬 프롬프트 설계 자기점검(사용자 이익 정렬·과잉 수집 회피)에 개념 참고. 단 실행 도구가 아니라 논문 프레임워크.
- **6개월 영향력**: LLM 앱 규제·투명성 논의가 "시스템 프롬프트 공개·감사"로 향하는 신호. 프롬프트 인젝션 방어(개발자측)와 대칭인 "프롬프트 감사(사용자측)"가 보안 담론의 새 축이 될 수 있음.
- **허와 실**: "user-centric"은 강한 프레이밍 — 실제로 사용자가 시스템 프롬프트를 검증할 접근권/도구를 주는지, 아니면 개념 제안에 그치는지는 원문 확인 필요. 감사 자동화의 신뢰도(오탐·과탐)도 미지수.
- **액션**: arxiv ID 실재 확인 가능 시점에 감사 항목·방법 재검증 후, 내 스킬 시스템 프롬프트 자기점검 체크리스트 아이디어로 개념만 참고(수치 인용 금지).

## 관련 페이지
- [[system-prompts-and-models-of-ai-tools]]
- [[system_prompts_leaks]]
- [[Multi-Layer-Agent-Red-Teaming]]
- [[VulnClaw]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.28617
- HF: 데일리 페이퍼 등재 (2026-08-03 자동수집)
- 신뢰도: ⭐⭐ (medium — 미래형 arxiv ID로 원문 재현 미검증, 저자·소속 미확인, raw 한줄요약 기반, 구체 수치 미기재)
