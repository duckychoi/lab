---
title: voicebox — 오픈소스 로컬 AI 음성 스튜디오
type: source
domain: ai-news
tags: [ai-news, github-trending, tts, voice-cloning, audio, local-llm, open-source]
created: 2026-06-24
updated: 2026-07-20
sources: []
reliability: medium
---

# voicebox (jamiepine/voicebox)

> [!insight] 핵심 인사이트
> ⭐**43,708 (2026-07-20, 당일 +610)** — 한 달 전 33,512(06-24)에서 **약 +10K 성장**하며 4.3만 돌파. 음성 클로닝·**받아쓰기(dictation)**·TTS를 **로컬 환경**에서 처리하는 오픈소스 AI 음성 스튜디오. 클라우드 TTS API(ElevenLabs 등) 의존을 끊고 데스크톱에서 자체 음성 파이프라인을 돌리려는 수요가 한 달 내내 +수백/일로 유지됨 — [[VoxCPM]]·[[supertonic]]·[[higgs-audio-v3-tts]]로 이어진 "토크나이저리스/로컬 TTS" 흐름이 *완성형 앱(스튜디오 UI)* 으로 패키징된 사례. 로컬 음성 스튜디오 카테고리의 대표 레포로 안착.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐ — ⭐33,512로 이미 대형 레포. 다만 음성 클로닝 품질·지원 언어·실시간성은 미검증.
- **즉시 활용**: YES(후보) — 내 [[reat-voice]] 파이프라인이 현재 클라우드 TTS에 의존. voicebox로 로컬 더빙/내레이션을 대체하면 비용 0 + 무제한 생성 가능성. 한국어 음성 품질이 관건.
- **6개월 영향력**: 영상 자동화([[video-saas]])의 음성 단계가 "API 종량제"에서 "로컬 무제한"으로 이동할 수 있는 거점. [[local-llm]] 도메인과 직접 교차.
- **대체 관계**: ElevenLabs / OpenAI TTS 종량 API의 오픈소스 로컬 대안. 데스크톱 앱이라 비개발자도 접근 가능.
- **허와 실**: "스튜디오"는 UX 포장. 실제 음성 엔진이 자체 모델인지 기존 오픈 모델(XTTS, F5 등) 래퍼인지 확인 필요. 음성 클로닝은 동의·저작권 리스크 동반.
- **액션**: star + 로컬 설치 → 한국어 내레이션 샘플 테스트, [[reat-voice]] 대체 가능성 측정.

> [!warning] 신뢰도/윤리 주의
> 음성 클로닝은 타인 음성 무단 복제 시 법적·윤리 문제. 본인 음성 또는 라이선스 확보 음성에만 사용.

> [!action] 당장 할 것
> voicebox 로컬 설치 후 한국어 TTS 품질을 ElevenLabs와 블라인드 비교 → 합격 시 [[reat-voice]] 백엔드 교체 PoC.

> [!question] 미해결 질문
> 백엔드 음성 모델 정체? 한국어 지원 수준? 실시간 스트리밍 가능 여부? GPU 요구사항?

## 관련 페이지

- [[reat-voice]]
- [[VoxCPM]]
- [[supertonic]]
- [[higgs-audio-v3-tts]]
- [[OmniVoice]]
- [[local-llm]]
- [[video-saas]]

## 원본
- 출처: https://github.com/jamiepine/voicebox
- 스타: ⭐43,708 (2026-07-20, 당일 +610) — raw 자동수집 / 이전 ⭐33,512 (2026-06-24)
- 신뢰도: ⭐⭐⭐ (대형 레포이나 음성 품질·언어 지원 미검증)
