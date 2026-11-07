---
title: "ConardLi/garden-skills — 결정론적 render(t) 페이지로 MP4를 뽑는 motion-showreel 등 6개 스킬. 기술 검수와 취향 리뷰를 분리"
type: source
domain: video-saas
tags: [video-saas, ai-news, github-trending, agent-skills, motion-graphics, code-video, tts, gpt-image-2]
created: 2026-11-07
updated: 2026-11-07
sources: [https://github.com/ConardLi/garden-skills]
reliability: medium
---

**GitHub**: [ConardLi/garden-skills](https://github.com/ConardLi/garden-skills) **★14,558 · 포크 1,681 · 오픈이슈 26**(볼트 11-07 실측 · 수집기 11-06 ★14,383 → +175/1일) · MIT · JavaScript · created 2026-04-21 · **pushed 2026-10-25**(13일 전) · 최신 릴리스 `motion-showreel-v0.1.0`(10-11) · daily 트렌딩 12위(11-06)

## 핵심 인사이트
> [!insight] "한 개의 결정론적 render(t) 페이지 → 스틸·콘택트시트·프록시·마스터 전부"
> 대표 스킬 `motion-showreel` 은 영상을 **시간 t 의 순수 함수인 웹 페이지 하나**로 정의하고, 같은 페이지에서 스틸·콘택트시트·저해상 프록시·최종 마스터 MP4 와 편집 가능한 소스를 모두 뽑는다. 43개 스타일 라이브러리 · 내장 신스/Tone.js 음악 · 비트 감지 · Gemini/MiniMax TTS(사용자 제공 대본만 읽음) · 최대 20분 챕터 영상. 특히 **기술 검수(크기·fps·길이·프레임 수·블랙프레임·라우드니스·true peak·루프 이음·결정론)를 취향 리뷰와 분리**해 기술 항목은 전부 PASS 를 요구한다 — "보기 좋다"와 "규격이 맞다"를 섞지 않는 QA 설계.

> [!note] 급상승의 성격
> 마지막 푸시가 10-25 라 11-06 의 +175 는 신규 개발이 아니라 **노출 효과**로 보인다(수집기 판단에 볼트 동의 — 볼트 재조회 pushed_at 동일). SKILL.md 6개(볼트 tree API 실측 = README 배지 6 일치).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: Remotion([[Remotion]]) 대신 **"브라우저 페이지 렌더 → 프레임 캡처"** 경로. 사용자의 reat-* 스킬(Remotion 기반)과 직접 비교 대상. 차용할 것은 두 가지 — ① 결정론 검사(같은 t → 같은 픽셀) ② 기술 QA 체크리스트(라우드니스·true peak·블랙프레임)를 렌더 후 자동 PASS/FAIL 로.
- **워크플로우**: 확인 체크포인트 2회(요구사항 → 스타일 프레임) 후 자율 제작. 사람 개입 지점을 "스타일 확정"에만 두는 구조.
- **크리에이터 인사이트**: TTS 가 **사용자 대본만 읽는다**는 제약은 환각 내레이션을 막는 의도적 설계.
- **즉시 활용**: YES(읽기) — `motion-showreel` SKILL.md 의 QA 항목을 reat-render 후검사에 이식. 나머지 5개(`web-video-presentation` · `web-design-engineer` · `gpt-image-2` · `beautiful-article` · `kb-retriever`)는 미열람.

## 관련 페이지
- [[에이전트-스킬]] · [[Remotion]] · [[AI-영상-생성-2026]] · [[After-Effects-MCP]]
- [[scenario-skills]] (같은 날 · 생성형 미디어 스킬) · [[mattpocock-skills]]
- [[요약자와-판정자-분리]] (기술 판정과 취향 판정의 분리)

## 원본
- 출처: https://github.com/ConardLi/garden-skills
- 확인 범위: GitHub API·tree API(볼트 11-07) · README 는 수집기 기준(motion-showreel 절 약 60행) · 실행 0회
- 신뢰도: ⭐⭐ (★14.6k · 정량 벤치 없음)
