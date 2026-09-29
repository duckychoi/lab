---
title: LTX-2 — 오디오 동반 영상 생성 모델 공식 추론/LoRA 학습 패키지 (Lightricks)
type: source
domain: ai-news
tags: [ai-news, github-trending, video-generation, audio-video, lora, video-saas]
created: 2026-08-14
updated: 2026-08-15
sources: []
reliability: medium
---

# Lightricks/LTX-2 — 오디오-비디오 생성 공식 패키지

**GitHub**: https://github.com/Lightricks/LTX-2
**스타수**: ⭐9,016 (2026-08-15 자동수집, 당일 **+161**) ← 8,990 (08-14, +205) · **제작**: Lightricks
**성격**: **LTX-2 오디오-비디오 생성 모델의 공식 Python 추론/LoRA 학습 패키지** — 오디오 동반 영상 생성 지원

> [!update] 2026-08-15 갱신 — ⭐9,016 (당일 +161·9천 돌파)
> GitHub ⭐**9,016**(2026-08-15 자동수집, 당일 +161) ← 8,990(08-14, +205). 편입 이튿날 **9천 돌파** — 오디오 동반 오픈 i2v + LoRA 학습을 갖춘 벤더(Lightricks) 공식 축 위치 유지, HF 가중치 [[LTX-2.5]](이날 DL 378k로 급증)와 짝. 해상도·오디오 동기 품질·라이선스는 원문 재현 전 → 미기재. reliability medium 유지. *raw 자동수집 수치 반영 — GitHub 실WebFetch 미수행(타임라인 유지).*

> [!insight] 핵심 인사이트
> **영상과 오디오를 함께 생성하는 LTX-2 모델의 공식 코드베이스**(raw 기반). 08월 위키의 오픈 i2v 축이 [[MiniMax-H3]]([[ComfyUI]] 재패키지 경로)로 두꺼워지는 가운데, LTX-2는 **① 벤더 공식 리포(Lightricks 제작)라는 점 ② 오디오까지 동반 생성한다는 점**에서 결이 다르다 — 무성 영상 생성이 대부분이던 오픈 축에서 "소리까지 한 번에"는 실용 편집 단계를 줄이는 차별점([[video-saas]] 오픈 축). 특히 **LoRA 학습 패키지 동반**은 [[unsloth]](LLM 파인튜닝)와 같은 결의 "오픈 미디어 모델을 내가 직접 커스터마이징"하는 제작 축을 영상 쪽에도 여는 신호. HF 모델 [[LTX-2.5]](i2v)와 한 생태계로, GitHub 패키지↔HF 가중치가 짝을 이룸.

> [!warning] 신뢰도 medium — 공식 리포이나 스펙·품질 미검증
> Lightricks 공식 리포로 프로젝트 실재는 신뢰되나, ⭐8,990·당일 +205는 **raw 자동수집 API 수치**이며 **GitHub 실WebFetch 미수행**(타임라인 유지). 해상도·길이·오디오 동기 품질·라이선스·[[LTX-2.5]]와의 관계 세부는 **원문 재현 전이라 구체 수치 미기재**([[CLAUDE.md]] 사실확인 원칙). 오디오-비디오 동기 품질은 미실측.

## 도메인별 추출 (ai-news / video-saas 교차)

- **기능 벤치마킹**: 오디오 동반 영상 생성 — 내 영상 자동화에 "무성 클립 + 별도 TTS/BGM" 대신 "동반 생성"을 검토할 참조점(단 편집 통제력은 분리 파이프가 유리할 수 있음).
- **크리에이터 인사이트**: 오픈 축 사용자는 "설치·통제 가능 + 소리까지"를 원함 — 공식 LoRA 학습 지원이 커스터마이징 갭을 메움.
- **워크플로우**: 공식 Python 추론 → LoRA 학습으로 도메인 특화 → HF [[LTX-2.5]] 가중치 연계(추정).
- **경쟁 우위 빈틈**: 폐쇄형 [[Higgsfield]]·[[Seedance]] 대비 "오픈 + 오디오 동반 + 자체 LoRA"가 차별점 후보(품질 미검증).
- **액션**: [[ComfyUI]] 오픈 i2v 스팟체크에 LTX-2 계열을 오디오 동반 비교군으로 편입 검토(낮음).

## 관련 페이지
- [[LTX-2.5]] — 같은 생태계 i2v HF 모델
- [[MiniMax-H3]] · [[ComfyUI]] — 오픈 i2v 축 대비
- [[unsloth]] — 오픈 모델 커스터마이징 제작 축(영상판 LoRA)
- [[video-saas]] · [[ai-news]]

## 원본
- 출처: https://github.com/Lightricks/LTX-2
- 신뢰도: ⭐⭐ (⭐9,016·당일 +161, raw 자동수집 · 실WebFetch 미수행, 스펙·품질 미검증)

---

## 🔓 2026-09-29 — **논문 확보. 이 페이지가 스펙의 정당한 소유자다**

> [!insight] arXiv **2601.03233** — *LTX-2: Efficient Joint Audio-Visual Foundation Model*
> 게재 **2026-01-06T18:24:41Z** · **저자 29인**(Yoav HaCohen, Benny Brazowski, Nisan Chiprut, Yaki Bitterman 외 25).
> 🎯 **경로가 특이하다**: 이 ID 는 **[[LTX-2.5]] 의 HF API `tags` 배열에 `arxiv:2601.03233` 로 박혀 있었다.** 2.5 카드는 `gated: auto` 로 35일째 막혀 있는데, **메타데이터가 논문 주소를 흘렸고 논문은 열려 있었다** → [[무응답-오귀속]] · [[벤치마크-이미지-봉인]](저장소-로컬 봉인).

### 구조 (초록 축자 기반)
- **비대칭 듀얼 스트림 트랜스포머**: **영상 14B + 오디오 5B**
- 결합: **양방향 audio-video cross-attention** + temporal positional embeddings + **cross-modality AdaLN**(공유 타임스텝 조건화)
- 설계 의도: *"allocating **more capacity for video generation than audio generation**"* — 비대칭은 의도다
- **modality-CFG**(modality-aware classifier-free guidance) — 오디오·영상 정렬/제어 개선
- 텍스트 인코더: **multilingual** (🎯 [[LTX-2.5]] 태그의 en/de/es/fr/ja/ko/zh/it/pt 9개 언어와 정합)
- 오디오 범위: 음성 **이상** — *"rich, coherent audio tracks that follow the characters, environment, style, and emotion of each scene — complete with natural **background and foley** elements"*

> [!warning] 🟡 성능 주장의 범위를 잘라서 읽는다
> *"state-of-the-art audiovisual quality and prompt adherence **among open-source systems**, while delivering results **comparable to** proprietary models **at a fraction of their computational cost** and inference time."*
> - ✅ SOTA 주장 = **오픈소스 한정**
> - ✅ 상용 대비 = **동급(comparable)**, 우위 아님
> - 🔴 **벤치 이름·점수·평가자 수가 초록에 0개다.** *"In our evaluations"* 가 전부 — 어떤 평가인지 미기술 → [[HexaAnything]](같은 배치)와 **같은 형태의 무수치 결과 보고**다.
> - 🔴 *"All model weights and code are publicly released"* ↔ **[[LTX-2.5]] 는 `gated: auto`** — 버전이 다르므로 모순으로 단정하지 않되, `Lightricks/LTX-2` 저장소 게이트 여부 확인이 필요하다(actionable).

> [!warning] 🔴 **LTX-2 ≠ LTX-2.5** — 이 스펙을 2.5 에 옮겨 적지 않는다
> 논문 2026-01-06 / [[LTX-2.5]] 모델 생성 2026-07-23 = **6개월 반 차이.** 14B+5B 는 **이 페이지(LTX-2)의 값**이다. [[한정어-탈락]] 방지.

## 관련 페이지 추가
- [[LTX-2.5]] — 후속 버전(스펙 미확인) · [[무응답-오귀속]] · [[한정어-탈락]] · [[벤치마크-이미지-봉인]]
- [[YuE2]] — 🎯 같은 배치 · 오디오 생성 통합 계열 · [[VoiceStudio]] — 분리형 대비축 · [[AI-영상-생성-2026]]

## 원본 갱신
- 논문: https://arxiv.org/abs/2601.03233 (볼트 2026-09-29 09:09 UTC · arXiv API `totalResults=1` 실확인)
- 확인 범위: **초록 전문 + 서지(저자 29인·게재일).** 🔴 본문·벤치표·가중치·코드 미확인 · 🔴 미실행
