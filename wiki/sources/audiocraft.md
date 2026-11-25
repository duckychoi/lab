---
title: "audiocraft — Meta의 MusicGen · AudioGen · EnCodec 학습/추론 라이브러리(유지보수 모드)"
type: source
domain: ai-news
tags: [ai-news, github, audio-generation, musicgen, audiogen, encodec, meta, baseline-resurfacing]
created: 2026-11-25
updated: 2026-11-25
sources: [https://github.com/facebookresearch/audiocraft]
reliability: medium
---

**레포**: facebookresearch/audiocraft · ★ **23,951**(수집기 11-24) → **23,964**(볼트 API 11-25) · Jupyter 일간 Trending(당일 +5) · MIT(코드) · 생성 2023-06-08 · **push 2026-03-03(8개월 전)** — [[기준선-재부상]] 사례(2023년 레포의 트렌딩 재등장)

## 핵심 인사이트
> [!insight] 오디오 생성의 2023 기준선 — 인프라성 자산은 유지보수가 멈춰도 참조 수요가 유지된다
> 오디오 생성 연구용 PyTorch 라이브러리. 포함: MusicGen(텍스트→음악) · MusicGen Style · JASCO(코드·멜로디·드럼 조건) · AudioGen(텍스트→효과음) · MAGNeT(비자기회귀) · EnCodec(뉴럴 코덱) · Multi Band Diffusion · AudioSeal(오디오 워터마크). 학습 코드는 EnCodec · MusicGen · MBD · JASCO 공개. **트렌딩에 다시 오른 이유는 신규성이 아니라 "음악 생성을 쓰려는 사람의 기본 검색 결과"가 여기기 때문** — [[Meta]] 계열 기준선의 참조 수요가 유지되는 사례.

> [!warning] 사실상 유지보수 모드 + 가중치 라이선스 미확인
> README 설치 요건이 **Python 3.9 · PyTorch 2.1.0 고정**으로 오래됐고 마지막 push가 8개월 전. README 자체에는 품질 수치가 없다(모델별 docs 위임). ⚠️ 코드는 MIT지만 **사전학습 가중치 라이선스는 모델별 문서에서 따로 확인 필요(볼트 미확인)**.

## 도메인별 추출 (ai-news)
- **즉시 활용**: 쇼츠 BGM · 효과음 로컬 생성 실험엔 여전히 동작 가능한 기준선. 단 최신 음악 생성 모델과의 품질 비교 근거는 이 레포에 없다.
- **6개월 영향력**: 없음 — 대체 후보가 아니라 비교 대상(2023 기준선)으로 남는다.
- **액션**: 없음(관찰).

## 관련 페이지
- [[Meta]] · [[기준선-재부상]] · [[ai-news]]

## 원본
- 출처: https://github.com/facebookresearch/audiocraft
- 확인 범위: README(수집기 11-24) · GitHub API 재확인(볼트 11-25 — ★ · 라이선스 · 생성일 · push 일치) · 실행 0
- 신뢰도: ⭐⭐⭐ (★2.4만 · Meta 공식 · 가중치 라이선스는 미확인)
