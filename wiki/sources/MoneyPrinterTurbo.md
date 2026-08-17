---
title: harry0703/MoneyPrinterTurbo — AI LLM 기반 쇼트폼 영상 자동 생성 엔진
type: source
domain: ai-news
tags: [ai-news, github-trending, video-saas, short-form, automation, LLM, tts, subtitles]
created: 2026-05-29
updated: 2026-08-17
sources: []
reliability: high
---

# MoneyPrinterTurbo — AI 쇼트폼 영상 완전 자동화

> [!update] 2026-08-17 갱신 — ⭐105,044 (당일 +494·10만 돌파, 약 두 달 만 +2만)
> GitHub ⭐**105,044**(2026-08-17 자동수집, 당일 +494·**10만 돌파**) ← 85,539(06-11) ← 77,436(06-02). 약 두 달 만의 재등장에서 8.5만→10.5만으로 **+2만 누적·10만 대관문 통과** — 텍스트 입력만으로 쇼트폼 영상(대본→TTS→자막→배경영상→편집)을 일괄 생성하는 완성형 오픈 파이프라인의 대중적 채택이 계속 확대. 오픈 i2v 백본이 [[MiniMax-H3]]·[[LTX-2.5]]로 다변화되는 흐름과 함께, "완성형 자동 편집 파이프라인" 레이어(MoneyPrinterTurbo)도 동반 성숙 — 내 [[video-saas]] 파이프라인([[reat-render]])의 기능 격차 벤치 1순위 유지. 단 결과물 품질은 연결한 LLM/TTS/영상 API 수준에 의존(자체 생성 능력 아님)·"Money Printer" 마케팅 톤 주의. reliability high 유지(성숙 OSS·실재). *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 텍스트 입력 하나로 고화질 쇼트폼 영상(음성·자막·배경음악·편집)까지 일괄 생성. GitHub ⭐85,539 (2026-06-11; 이전 ⭐77,436 2026-06-02) — GitHub Trending 상위권 유지. 영상 자동화 SaaS 구현의 완성형 레퍼런스.

## 도메인별 추출 (video-saas + ai-news 교차)

- **신뢰도**: ⭐⭐⭐⭐⭐ — ⭐85,539 (2026-06-11), 커뮤니티 검증, 중국어·영어 양방향 지원, 실제 영상 생성 데모 다수
- **즉시 활용**: YES — Docker 또는 pip 설치. LLM API 키만 있으면 바로 영상 생성 가능
- **6개월 영향력**: [[Pixelle-Video]], [[reat-slides]], [[reat-scene]] 같은 영상 자동화 파이프라인의 오픈소스 완성형 사례. 내 video-saas 구현의 기능 참조·경쟁 벤치마크
- **대체 관계**: Pictory, Synthesia(유료 SaaS) 대비 완전 로컬·무료. [[Pixelle-Video]] 대비 더 많은 스타·커뮤니티 검증
- **허와 실**: "Money Printer" 명칭에서 보이듯 쉬운 수익화 마케팅 톤 — 실제 영상 품질은 LLM/TTS API 수준에 의존

> [!action] 당장 할 것
> 로컬 설치 후 한국어 쇼트폼 영상 생성 테스트. 내 video-saas 파이프라인([[reat-render]])과 기능 격차 분석

## 주요 기능

- **완전 자동화**: 스크립트 생성 → 음성합성 → 자막 → 배경영상 → 편집 일괄 처리
- **다언어 지원**: 한국어 포함 다국어 TTS
- **배경음악**: 자동 배경음악 삽입
- **Web UI**: Streamlit 기반 웹 인터페이스

## 관련 페이지

- [[Pixelle-Video]] — AI 쇼트 영상 자동 생성 엔진 (GitHub ⭐12,394)
- [[FunASR]] — ASR 툴킷, 영상 파이프라인 음성 처리에 통합 가능
- [[AI-영상-생성-2026]] — 영상 AI 전체 지형도
- [[reat-render]] — 로컬 Remotion 기반 영상 렌더링 파이프라인

## 원본

- 출처: https://github.com/harry0703/MoneyPrinterTurbo
- 스타: ⭐105,044 (2026-08-17, 당일 +494·10만 돌파) ← ⭐85,539 (06-11) ← ⭐77,436 (06-02)
- 언어: Python
- 신뢰도: ⭐⭐⭐⭐⭐ (10만 돌파·대중적 채택 지속 — 단 결과물 품질은 연결 API 의존·raw 자동수집)
