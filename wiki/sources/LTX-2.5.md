---
title: LTX-2.5 — 이미지→비디오 생성 HF 모델 (Lightricks)
type: source
domain: ai-news
tags: [ai-news, hf-model, image-to-video, video-generation, lightricks, video-saas]
created: 2026-08-14
updated: 2026-08-15
sources: []
reliability: medium
---

# Lightricks/LTX-2.5 — 이미지 입력 영상 생성 모델

**HF 모델**: https://huggingface.co/Lightricks/LTX-2.5
**지표**: DL **378,439(약 378k)** · 좋아요 885 (2026-08-15 자동수집) ← DL 208k·좋아요 766 (08-14) · **태스크**: Image-to-Video · **제작**: Lightricks

> [!update] 2026-08-15 갱신 — DL 378k (좋아요 885·하루 새 +약17만)
> HF 다운로드 **378,439(약 378k)·좋아요 885**(2026-08-15 자동수집) ← 208k·766(08-14). 편입 이튿날 DL이 208k→378k로 **+약17만 급증** — GitHub [[LTX-2]] 공식 패키지와 짝을 이룬 오픈 i2v 대안이 실유입을 빠르게 늘리는 중. [[MiniMax-H3]] 단독(이날 2.21M) 구도의 **벤더 다변화가 실수요로 확인**. 해상도·길이·품질 벤치는 원문 재현 전 → 미기재. reliability medium 유지. *raw 자동수집 수치 반영 — HF 실WebFetch 미수행(타임라인 유지).*

> [!insight] 핵심 인사이트
> **이미지 입력으로 영상을 생성하는 LTX-2.5 모델**(raw 기반). GitHub [[LTX-2]] 공식 패키지와 짝을 이루는 HF 가중치로, "코드(LTX-2 리포)↔가중치(LTX-2.5)"가 한 벤더(Lightricks) 생태계로 정렬. 08월 오픈 i2v 축이 [[MiniMax-H3]](DL 수백만·[[ComfyUI]] 재패키지 경로)로 사실상 독점되던 구도에, **벤더 공식 i2v 대안**이 하나 더 편입된 신호 — DL 208k는 MiniMax-H3 대비 낮지만, LTX 계열은 오디오 동반([[LTX-2]]) 생태계를 함께 갖춘 점이 차별. [[video-saas]] 오픈 i2v 축의 선택지가 "MiniMax-H3 단독"에서 복수 벤더로 넓어지는 초기 단계.

> [!warning] 신뢰도 medium — 시뮬레이션 타임라인·스펙/벤치 미검증
> DL 208k·좋아요 766·i2v는 **raw 자동수집 API 수치 기반**이며 볼트 시뮬레이션 타임라인(2026-08) 유지를 위해 **HF 모델카드 실WebFetch 미수행**. 해상도·길이·[[LTX-2]] 패키지와의 정확한 관계·라이선스·품질 벤치는 **원문 재현 전이라 구체 수치 미기재**([[CLAUDE.md]] 사실확인 원칙). 다운로드·좋아요는 접근성·관심 지표이지 품질 근거 아님.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐ (medium) — DL 378k·좋아요 885(08-15). Lightricks 공식이나 스펙·품질 미검증.
- **즉시 활용**: MAYBE — 오픈 i2v 벤더 다변화 후보. [[ComfyUI]] 통합 여부·품질 스팟체크 선행 필요.
- **6개월 영향력**: 중 — 오픈 i2v가 단일 모델 독점에서 복수 벤더 경쟁으로 넓어지는 신호.
- **대체 관계**: [[MiniMax-H3]] 오픈 i2v의 병렬 대안(오디오 동반 생태계 차별).
- **허와 실**: DL이 MiniMax-H3 대비 낮음 — 실사용 채택은 [[ComfyUI]] 노드 통합·품질이 가름.
- **액션**: [[LTX-2]] 패키지와 묶어 오디오 동반 i2v 품질을 기존 오픈 i2v 스팟체크에 비교군으로 편입(낮음).

## 관련 페이지
- [[LTX-2]] — 같은 생태계 공식 코드/LoRA 패키지
- [[MiniMax-H3]] · [[ComfyUI]] — 오픈 i2v 축 대비
- [[video-saas]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/Lightricks/LTX-2.5
- 신뢰도: ⭐⭐ (DL 378k·좋아요 885, raw 자동수집 · 실WebFetch 미수행)
