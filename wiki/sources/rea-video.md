---
title: "JuneYaooo/rea-video — 레퍼런스 영상을 샷 단위로 분해해 실촬영/AI 생성/코드 렌더를 판정하고 재현 계획(프롬프트·조명·BPM·Remotion 타이밍)을 낸다"
type: source
domain: video-saas
tags: [video-saas, github-trending, agent-skill, video-analysis, reverse-prompt, remotion, shot-breakdown, apache-2.0]
created: 2026-11-09
updated: 2026-11-09
sources: [https://github.com/JuneYaooo/rea-video]
reliability: medium
---

**GitHub**: [JuneYaooo/rea-video](https://github.com/JuneYaooo/rea-video) · ★**4,964**(볼트 11-09 API · 수집기 3,842 → **+1,122/1일, +29%**) · 포크 711 · 이슈 5 · Apache-2.0 · Python · created 2026-10-29 · pushed 11-08

## 핵심 인사이트
> [!insight] 영상 레퍼런스 → "촬영 / 생성 / 코딩" 3분할 리메이크 계획
> 샷마다 토킹헤드·AI 영상·3D·모션그래픽·화면녹화를 판정하고, AI 샷엔 **역추정 프롬프트 + 모델 제안**, 코드형 샷엔 **[[Remotion]] 재구성용 타이밍**, 그 외 카메라 위치·조명·색보정·컷 템포·음성(사람/AI)·BPM·효과음 위치까지 report.html 로 낸다. ffmpeg + Python 3.10+, Gemini·Doubao 같은 영상 이해 모델 키가 있으면 판정 정확도↑(없어도 동작).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 내 SaaS 에 "레퍼런스 영상 업로드 → 샷별 재현 레시피" 기능으로 이식 가능. 난이도 중 — 샷 분할(ffmpeg scene detect) + VLM 판정 + 프롬프트 역추정. 이 볼트의 `/down-analysis` 스킬과 같은 축
- **크리에이터 인사이트**: 사용자가 원하는 건 "이 영상 어떻게 만들었나"의 **제작 방식 판정**이지 요약이 아니다
- **프롬프트 패턴**: 역추정 프롬프트 품질 수치 없음 — 판정 정확도 벤치 0건
- **경쟁 우위 빈틈**: Remotion 타이밍 출력은 reat-* 파이프라인(Remotion)과 직결
- ⚠️ 상세 문서 중국어

## 관련 페이지
- [[Remotion]] · [[에이전트-스킬]] · [[garden-skills]](11-07 motion-showreel) · [[scenario-skills]]

## 원본
- 출처: https://github.com/JuneYaooo/rea-video
- 확인 범위: GitHub API(볼트 11-09) · README 미정독 · 실행 0회
- 신뢰도: ⭐⭐ (★5.0K · 하루 +29% · 정확도 수치 0)
