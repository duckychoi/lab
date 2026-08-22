---
title: 4DAnyone — 캐주얼 단안 비디오로 임의 인물 4D 재구성
type: source
domain: slam-3dgs
tags: [ai-news, hf-paper, 4d-reconstruction, monocular, human-reconstruction, slam-3dgs, video]
created: 2026-08-21
updated: 2026-08-22
sources: []
reliability: medium
---

# 4DAnyone — Create Anyone in 4D from a Casual Monocular Video (HF 데일리 3위·업39)

**HF Papers**: https://huggingface.co/papers/2608.20335
**지표**: 업보트 **39** (HF 데일리 **3위**) · arxiv **2608.20335**(미래형 ID) · **도메인**: slam-3dgs (교차 video-saas)

> [!update] 2026-08-22 업보트 갱신 — 업 61 (**HF API 실검증**·전일 39 대비 +22)
> HF 업보트 **61** (2026-08-22 HF API 실호출) ← 39(08-21). 데일리 3위 유지. [[WithEveryone]]와 "인물 중심 비전" 짝 유지.
> *본 항목은 2026-08-22 raw에 **재등재되지 않았다**(전일 인제스트분과 동일 항목이므로 중복 방지 규칙 적용) — raw 수집 메모에 기록된 업보트 갱신값만 반영하며, 이번엔 HF API로 직접 대조해 확정. 순위·업보트는 **화제성 지표이지 검증 가능성 지표가 아님**(같은 배치 [[FlashPrefill-V2]]가 데일리 최하위임에도 가장 구체적인 실측 수치를 제시한 사례 참조).*

> [!insight] 핵심 인사이트
> **평범한 단안(monocular) 비디오 한 개로 임의 인물의 4D(공간 3D + 시간)를 재구성** — 특수 장비·다중 카메라 없이 일상 영상으로 움직이는 사람을 시공간 볼륨으로 복원한다. 위키의 slam-3dgs·4D 재구성 축([[4D-Human-Scene-Reconstruction]]·[[Beyond-Pixels-4D]] 픽셀 넘어 4D)에 "**캐주얼 촬영본 하나로 누구든**"이라는 입력 문턱 최소화 각도를 더함. 재구성된 4D 인물은 [[video-saas]] 파이프라인의 자산(움직이는 캐릭터·아바타) 공급원이 될 수 있어, 단안 영상→3D/4D 에셋 워크플로우([[AI-3D-생성]])와 접목 지점이 생김. 입력이 "casual monocular"라는 점이 실용성의 핵심 주장이자 검증 포인트.

> [!warning] 신뢰도 — 미래형 arxiv ID·원문 미검증 (medium)
> 업보트 39·데일리 3위는 raw 자동수집 신호이며 arxiv **2608.20335는 미래형 ID로 원문 초록·방법·수치 재현 불가**([[CLAUDE.md]] 사실확인 원칙). "단안→4D 인물"의 **재구성 품질(지오메트리·시간 일관성·아티팩트)·처리 시간·벤치·소속은 raw 미기재 → 원문 대조 전 미검증**. 제목·한줄요약 기반 medium(수치 인용 금지).

## 도메인별 추출 (slam-3dgs · 교차 video-saas)

- **현재 SOTA**: 미확정 — raw는 관심 신호만. 4D 인물 재구성 최고 오픈 구현체·벤치 수치는 원문 대조 전 미검증.
- **실시간 가능성**: 미기재 — "casual monocular" 입력이 강점이나 처리 시간·프레임레이트 raw 없음.
- **카메라 파이프라인**: 단안 비디오 단일 입력 — 다중뷰·깊이센서 불요 주장(검증 필요).
- **응용 가능성**: [[video-saas]] 캐릭터·아바타 자산 공급, 단안 영상→4D 에셋 워크플로우([[AI-3D-생성]]) 접목.
- **필수 레퍼런스**: 원문/코드 공개 시 [[4D-Human-Scene-Reconstruction]]·[[Beyond-Pixels-4D]]와 입력 조건·품질 비교.

## 관련 페이지
- [[4D-Human-Scene-Reconstruction]] — 인물·씬 4D 재구성(직접 계보)
- [[Beyond-Pixels-4D]] — 픽셀 넘어 4D 표현(4D 축)
- [[slam-3dgs]] — SLAM·3DGS·카메라 도메인
- [[AI-3D-생성]] — 이미지/영상→3D 워크플로우(에셋 접목)
- [[video-saas]] — 재구성 4D 인물의 자산 활용처
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2608.20335 (arxiv 2608.20335·미래형 ID)
- 지표: 업보트 39 (2026-08-21, HF 데일리 3위)
- 신뢰도: medium (미래형 arxiv ID·원문 미검증·재구성 품질/벤치/소속 미기재·raw 자동수집)
- 수집: 2026-08-21 아침 자동수집 (HF 논문)
