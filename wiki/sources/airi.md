---
title: moeru-ai/airi — 셀프호스팅 AI 컴패니언 (실시간 음성·게임 플레이)
type: source
domain: ai-news
tags: [ai-news, github-trending, ai-companion, self-hosted, typescript, live2d, vrm, webgpu, local-llm]
created: 2026-07-28
updated: 2026-07-30
sources: []
reliability: high
---

# moeru-ai/airi (GitHub ⭐45,655)

> [!update] 2026-07-30 갱신 — ⭐45,655 (당일 +682)
> GitHub 스타 **45,655**(2026-07-30 자동수집·API 실검증, 당일 +682, MIT·TypeScript) ← 44,374(07-28). 이틀 새 +1,281 지속 유입 — 셀프호스팅 AI 컴패니언 수요 견조. 프로바이더 추상화·WebGPU 로컬 추론·DuckDB WASM 메모리 부품 스팟체크 액션 유지.

> [!insight] 핵심 인사이트
> Neuro-sama에서 영감받은 **셀프호스팅 AI 버추얼 컴패니언** 스택. ⭐**44,374**(2026-07-28, 당일 +572, WebFetch "44.4k" 일치·TypeScript·MIT). 단순 챗봇이 아니라 **실시간 음성 대화 + 게임 플레이(Minecraft·Factorio) + VRM/Live2D 캐릭터 애니메이션(오토블링크·시선추적)** 을 웹/Windows/macOS/모바일(PWA)에서 구동하는 "디지털 생명체 컨테이너". 핵심은 **모델·인프라 완전 교체 가능** — [[OpenAI]]·Claude([[Anthropic]])·DeepSeek·[[Ollama]] 다중 프로바이더, **WebGPU 브라우저 로컬 추론** + 데스크톱 CUDA/Metal, **DuckDB WASM·pglite 브라우저 내장 DB로 메모리**. Discord·Telegram 연동. 캐릭터 봇([[ChinameBot]] 계열)의 "음성+시각 아바타+지속 메모리"를 오픈소스로 통째 제공하는 레퍼런스 스택.

**GitHub**: https://github.com/moeru-ai/airi
**스타**: ⭐44,374 (2026-07-28, 당일 +572, WebFetch 실검증)
**신뢰도**: ⭐⭐⭐⭐ (4.4만 스타·MIT·TypeScript·기능 README 실확인 high)

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐ — 4.4만 스타·MIT·기능 실확인 high. 실배포 성숙도(음성 지연·게임 플레이 안정성)는 자체 데모 기준이라 실사용 검증 별도.
- **즉시 활용**: YES(대조·부품) — 내 봇 워크플로우와 겹치는 **음성 파이프라인·아바타·브라우저 로컬 메모리(DuckDB WASM)**가 부품 단위로 참고 가치. 특히 프로바이더 추상화(로컬 Ollama↔클라우드 교체)와 WebGPU 브라우저 추론은 무과금 로컬 축과 직결.
- **6개월 영향력**: "AI 컴패니언"이 텍스트 챗에서 **음성+시각 아바타+지속 메모리+환경 상호작용(게임)**의 통합 경험으로 표준화. 캐릭터 봇 SaaS의 기능 하한선을 끌어올림.
- **대체 관계**: 클로즈드 컴패니언 앱(Character.AI 류) 대비 **셀프호스팅·모델 교체 자유·로컬 프라이버시** 우위. [[speech-to-speech]](HF 음성 파이프라인)와 음성 축에서 계보 공유 — airi는 그 위에 아바타·메모리·게임을 얹은 완성 앱.
- **허와 실**: 마케팅("영혼의 컨테이너")을 걷어내면 = 음성 STT/TTS + LLM 프로바이더 라우팅 + Live2D/VRM 렌더 + 브라우저 DB 메모리의 잘 통합된 TypeScript 모노레포. 신기술이 아닌 **통합·셀프호스팅**이 가치.
- **액션**: DuckDB WASM 브라우저 메모리·프로바이더 추상화 계층을 부품으로 스팟체크 → 내 봇의 로컬 메모리/모델 교체 레이어에 참고.

> [!action] 당장 할 것
> airi의 **프로바이더 추상화(Ollama↔OpenAI↔Claude 교체) + DuckDB WASM 브라우저 메모리** 구현을 코드 레벨로 확인 → 내 캐릭터 봇에 "로컬 우선·클라우드 폴백" 모델 라우팅과 브라우저 내장 메모리 이식 가능성 판단.

## 관련 페이지
- [[speech-to-speech]]
- [[Ollama]]
- [[Anthropic]]
- [[OpenAI]]
- [[local-llm]]
- [[ai-news]]

## 원본
- 출처: https://github.com/moeru-ai/airi
- 스타: ⭐44,374 (2026-07-28, 당일 +572, WebFetch 실검증), TypeScript, MIT
- 기능: 실시간 음성 대화·게임 플레이(Minecraft/Factorio)·VRM/Live2D 아바타·WebGPU 로컬 추론·DuckDB WASM/pglite 메모리·다중 프로바이더(OpenAI/Claude/DeepSeek/Ollama)·Discord/Telegram
- 신뢰도: ⭐⭐⭐⭐ (스타·라이선스·기능 실확인 high, 실배포 안정성 자체 데모 기준)
