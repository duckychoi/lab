---
title: claude-video (/watch) — Claude가 영상을 보고 듣게 하는 플러그인
type: source
domain: video-saas
tags: [ai-news, video-saas, github-trending, claude-code, video-analysis, whisper, plugin]
created: 2026-07-06
updated: 2026-07-28
sources: []
reliability: high
---

# bradautomates/claude-video (GitHub ⭐11,484)

> [!update] 2026-07-28 갱신 — ⭐11,484 (당일 +434) + 4모드로 확장
> ⭐**11,484**(2026-07-28, 당일 +434, WebFetch "11.5k" 일치) ← ⭐3,704(07-06). 약 3배 성장. WebFetch 재확인: 프레임 추출이 **4단계 디테일 모드로 세분화** — `transcript`(텍스트만)·`efficient`(키프레임)·`balanced`(장면인지)·`token-burner`(무제한). **근접 중복 프레임 자동 dedup**으로 정적 구간 토큰 절약, **최초 실행 시 ffmpeg·yt-dlp 자동 설치(zero-config)**, Whisper는 Groq/OpenAI 폴백. 내 [[down-analysis]] 대비 "토큰 예산 vs 시각 충실도" 4단 트레이드오프가 정교화된 점이 새 참고 포인트.

**GitHub**: https://github.com/bradautomates/claude-video
**스타수**: ⭐11,484 (2026-07-28, 당일 +434) ← 3,704 (2026-07-06)

> [!insight] 핵심 인사이트
> `/watch <URL|경로> <질문>` 한 줄로 Claude가 영상을 **실제로 보고 듣게** 하는 플러그인. 파이프라인이 내 [[down-analysis]] 스킬과 사실상 동일: **자막 우선 → 필요한 구간만 다운로드 → 장면 인지(scene-aware) 프레임 추출 → 타임스탬프 전사(무료 자막, 없으면 Whisper API 폴백) → 각 프레임을 Read로 이미지 인식**. [[video-use]]("영상을 안 보고 transcript로만 읽음")의 명시적 한계를 정면으로 넘어서는 설계 — *"제목으로 추측하거나 화면의 90%를 놓치는 transcript"를 문제로 지목*.

## 핵심 인사이트

> [!note] 설계 포인트 (README 실측)
> - **자막 우선 전략** — 공개 영상 대부분은 무료 자막으로 커버, Whisper API 키는 자막 없는 영상에만 필요 → 비용 최소화
> - **scene-aware vs efficient** 2모드 — 장면 전환 기준 추출 또는 빠른 키프레임
> - **필요한 것만 다운로드** — 전체가 아닌 질문 관련 구간만
> - `agentskills.io` 호환(50+ 호스트), Claude Code 마켓플레이스 자동 업데이트
> - 활용례: 경쟁 콘텐츠 훅 분석·버그 화면녹화 진단·영상 요약·"과장 걷어낸 실제 신기능"·플레이리스트→노트

> [!action] 내 down-analysis와 대조 검증
> claude-video의 "자막 우선 → 필요 구간만 → scene-aware 프레임 → Whisper 폴백" 순서는 내 [[down-video]]+[[down-analysis]] 파이프라인의 정확한 벤치마크. 특히 **자막 우선으로 다운로드/전사 비용을 아끼는** 부분과 scene-aware 프레임 추출 로직을 대조해 내 스킬의 비용·정확도 개선 여지 확인.

## 도메인별 추출 (ai-news / video-saas)

- **신뢰도**: ⭐⭐⭐⭐ (⭐3,704 당일 +368 급상승, 파이프라인 실측 확인)
- **즉시 활용**: YES(대조용) — 내 down-analysis가 이미 유사 기능 제공하므로 대체보다 **설계 대조 레퍼런스**로. 자막 우선·구간 선택 로직은 즉시 참고 가치.
- **6개월 영향력**: "영상=읽을 수 있는 소스"가 코딩 에이전트 기본 역량으로 표준화. 내 video-saas 워크플로우의 입력단(경쟁 영상 분석)을 강화.
- **대체 관계**: [[video-use]](transcript-only) 상위 호환. 내 [[down-analysis]](Gemini 멀티모달)와는 상호 대조 관계.
- **허와 실**: 마케팅 걷어내면 = yt-dlp+ffmpeg+자막/Whisper+프레임 Read 조합의 깔끔한 패키징. 신기술이 아니라 **워크플로우 통합**이 가치.
- **액션**: 내 down-analysis와 자막 우선/프레임 추출 로직 대조 1건.

## 관련 페이지
- [[video-use]] — transcript-only 영상 에이전트 (상위 호환 대상)
- [[down-analysis]] — 내 영상 분석 스킬 (직접 대조)
- [[down-video]] — 내 영상 다운로드 스킬
- [[agentskills]] — 스킬 호스트 규격
- [[AI-영상-생성-2026]]
- [[video-saas]]

## 원본
- 출처: https://github.com/bradautomates/claude-video
- GitHub: ⭐3,704 (2026-07-06, 당일 +368)
- 스택: yt-dlp + ffmpeg + 무료 자막/Whisper API + scene-aware 프레임 Read
- 신뢰도: ⭐⭐⭐⭐ (급상승, 파이프라인 README 실측 확인)
