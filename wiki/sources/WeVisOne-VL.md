---
title: "WeVisOne-VL — 검출부터 알파 매트까지 한 VLM, 진짜 차별점은 점수가 아니라 '없으면 없다'고 말하는 능력"
type: source
domain: video-saas
tags: [video-saas, hf-paper, vlm, segmentation, matting, detection, ocr, tencent, wechat, 2B, 4B, open-weights, 규약15]
created: 2026-10-24
updated: 2026-10-24
sources: []
reliability: high
---

# WeVisOne-VL: Unified Visual Perception from Objects to Pixels

**arXiv**: 2610.31329 · **HF**: https://huggingface.co/papers/2610.31329
**업보트**: **229** (수집기 229 **일치**) · HF 데일리 10-23 목록 **1위 — 미확정**(규약 ⑮: 데일리 등재 10-23, 관측 10-24 = 등재 후 1일)
**날짜**: `publishedAt` 2026-10-22 · `submittedOnDailyAt` 2026-10-23 → [[게시일-이중화]] 1일
**저자**: 8인 · 전원 **WeChat Vision, Tencent Inc.** (HF `organization`=tencent 와 본문 소속 일치)
**코드**: https://github.com/Tencent/WeVisOne-VL (★93) · **가중치**: `tencent/WeVisOne-VL-2B` · `tencent/WeVisOne-VL-4B` (HF, apache-2.0)
**신뢰도**: ⭐⭐⭐⭐

> [!insight] 핵심 인사이트 — 이 모델의 간판은 "30개+ 벤치 선두"인데, 실제로 차별화되는 것은 **거부(rejection)** 다
> 초록의 수치는 *"over 30 benchmarks, leading performance"* 뿐이다. 볼트가 arXiv HTML(773,693B)을 열어 Table 2~8 을 대조했다.
> 🏆 **Ref-ZOM(대상이 없는 문장을 섞은 참조 분할) 거부율**: WeVisOne-VL-4B **86.0** · 2B 62.4 vs UniPixel-7B **0.3** · Youtu-VL-4B **1.3** · LaSagnA-7B **0.7** · Text4Seg-7B 25.9 · GSVA-7B 41.9.
> ⇒ 🎯 **기존 분할 VLM 대부분은 대상이 없어도 마스크를 그린다**(거부율 0~2%). 저자 서술: *"existing segmentation models tend to output a mask even when the target is absent"*. 📌 **크리에이터 툴에서 "그 물체 지워줘"가 엉뚱한 영역을 지우는 사고는 이 축에서 난다** — mIoU/cIoU 로는 안 보이는 축이다 → [[벤치마크-외부축]].
> ⚖️ 단 **같은 Ref-ZOM 에서 4B cIoU 72.2 < 2B 73.4** — 거부를 더 잘하는 대가로 분할 정확도가 소폭 낮다.

## 본문 수치 (arXiv HTML Table 2~8 · 초록에 없음)

| 축 | 벤치 | WeVisOne-VL-4B | 비교 | 볼트 판정 |
|---|---|---|---|---|
| 검출 | COCO mean F1 | **57.1** (2B 55.2) | GroundingDINO-T 56.6 · LocateAnything-3B 54.7 | 🔴 **2B 는 전용 검출기에 진다**. bold 는 *"among VLMs"* 기준 |
| 밀집 검출 | Dense200 mean F1 | **71.3** | LocateAnything-3B 58.7 · Qwen3-VL-4B 15.2 | ✅ 가장 큰 격차 (베이스 대비 4.7배) |
| 카운팅 | MixCount test | **40.4** | LocateAnything-3B 15.2 · Qwen3-VL-4B 4.3 | ✅ 2.66배 |
| OCR | SROIE mean F1 | **68.1** | PP-OCRv5 58.6 | ⚖️ HierText 에서 **2B 30.5 = PP-OCRv5 30.5 동률** — "전용 OCR 전부 상회"는 4B 기준 |
| 참조 분할 | RefCOCO val cIoU | **81.4** | UniPixel-7B 80.8 · Youtu-VL-4B 80.7 | ⚖️ +0.6 — 포화 구간 |
| 매팅(박스) | AM-2K MAD | **5.0** | SAM2-Matting(SAM3) 12.1 | ✅ |
| 매팅(박스) | P3M-500-NP MAD | 7.3 (**2B 6.6**) | SAM2-Matting(SAM3) 15.4 | 🔴 **2B 가 4B 를 이긴다** (PPM-100 도 2B 5.3 < 4B 6.1) |
| 매팅(텍스트) | WeRefMat (referring) MAD | **9.8** | Qwen3.5-9B+SAM2-Matting 22.4 | 🔴 **WeRefMat 은 저자 자체(in-house) 벤치** |

> [!warning] 🔴 "선두"의 정의가 표마다 다르다
> Table 2·4·6 캡션: *"Bold and underline denote the best… **among VLMs**"* / *"the specialized detector is **excluded from this ranking**"*. ⇒ **전용 모델과의 비교에서 지는 칸(COCO 2B, VisDrone IoU0.95 3.9 = GDINO 3.9 동률)은 순위 산정에서 빠져 있다.** "30개+ 벤치 선두"를 *"전용 모델 포함 최고"* 로 읽으면 과대독해다 → [[한정어-탈락]] · [[표-부분인용]].
> 📌 텍스트 프롬프트 매팅은 **비교 기준이 저자 자체 벤치(WeRefMat) 하나뿐**이다.

> [!note] 구조 — 베이스와 데이터
> - **Qwen3-VL 위에 2B/4B 두 규모** + `<OBJ>` 토큰마다 호출되는 경량 픽셀 디코더(박스 + 비전 인코더 다층 피처 입력) ⇒ 별도 대형 분할 모델 불필요.
> - 학습 데이터 **약 1억(100M) 이미지**. 라벨 생성 파이프라인이 **[[sam3|SAM3]] + 자체 DINO형 검출기 + Rex-Omni 제안 → Qwen3-VL 검증**이다 ⇒ 🎯 **SAM3 가 교사로 쓰였고, 매팅 비교에서 SAM3 기반 SAM2-Matting 을 이긴다.** 교사를 넘은 것인지, 교사 라벨을 Qwen3-VL 필터로 정제한 효과인지 본문은 분리하지 않는다.
> - 저자 명시: *"Formal benchmarks are kept isolated from training"*.

> [!warning] 저자 자기제한 (§8 Limitations)
> ① *"limited amount of general-purpose training data **may compromise the general capabilities relative to the base model**"* — 일반 VQA 능력 저하를 저자가 인정하되 **수치는 없다** → [[특화-역류]] 의 예상 사례(미측정).
> ② CoT 없음 → 복잡 추론 제한. ③ 단일 턴. ④ *"real-world user instructions are often **vague and hesitant**"* — 벤치 프롬프트는 깨끗하다는 것을 저자가 적었다 → [[벤치마크-외부축]].

## 도메인별 추출 (video-saas 템플릿)

- **기능 벤치마킹**: 🟢 **"텍스트로 지정한 피사체의 알파 매트"** 를 단일 4B 모델로 낸다 — 썸네일 누끼·제품 컷아웃·배경 교체의 앞단. 난이도 **낮음**: 가중치 apache-2.0 공개 · 레포에 `wevisone_vl/` 패키지 + `demo/` + `tutorials/` + `evaluation/` 실존(Python 233KB · Notebook 10.4MB). 4.83B(4B 모델 safetensors 실측) ⇒ 소비자 GPU 1장 범위로 추정(VRAM 미실측).
- **크리에이터 인사이트**: 사용자가 원하는 것 = *"이거 빼줘"가 틀리면 안 하는 것*. 툴이 주던 것 = 무조건 마스크. 🏆 **거부율 86.0 은 UX 신뢰 지표**다.
- **프롬프트 패턴**: 점·박스·마스크·알파 중 **출력 입도를 지시문으로 고른다**(*"any user-specific granularity"*). 구체 프롬프트 템플릿은 레포 `tutorials/` 미열람.
- **워크플로우**: 이미지 단위. 🔴 **영상(시간축 일관성) 평가는 없다** — 영상 누끼에 쓰려면 프레임별 실행 + 별도 추적이 필요하다.
- **디자인 레퍼런스**: 해당 없음(모델 논문).
- **경쟁 우위 빈틈**: SAM 계열은 "무엇을" 이해가 약하고 VLM 계열은 "어디를" 정밀도가 약하다는 틈을 한 모델로 메운다. 🔴 단 **4B 가 2B 보다 매팅에서 나쁜 칸**이 있어 "큰 게 낫다"가 성립하지 않는다 — 용도별 2B/4B 선택 실험이 필요하다.

> [!action] 당장 할 것
> 1. **(중간)** `tencent/WeVisOne-VL-2B` 로 **거부 테스트** — 볼트/작업 이미지에 "없는 물체"를 지시해 마스크를 그리는지 확인. 거부율 86.0(4B)·62.4(2B) 차이가 실사용에서도 보이는지.
> 2. **(낮음)** 2B vs 4B 박스 매팅 비교 — 논문상 2B 우세 칸 재현 여부.

> [!question] 미해결
> - 일반 VQA 저하 폭(저자 인정, 수치 없음).
> - HF 가중치 `downloads` **0**(10-22 생성, 집계 지연 가능) — 채택 신호는 아직 없다 → [[캐시된-지표-신선도]].

## 관련 페이지
- [[Tencent]] — 🔴 레포 API `NOASSERTION` 인데 LICENSE 본문은 **Apache-2.0**(벤더 규칙 재현)
- [[sam3]] — 라벨 교사이자 매팅 비교 대상
- [[Qwen]] — 베이스 Qwen3-VL
- [[벤치마크-외부축]] · [[한정어-탈락]] · [[표-부분인용]] · [[특화-역류]] · [[파생표기-함정]] · [[게시일-이중화]] · [[캐시된-지표-신선도]]
- [[LayerEditor]] — 같은 10-23 목록 · RGBA 출력이라는 같은 목적지(크리에이터 편집)
- [[FAPL]] · [[OpenDS-World]] · [[IQuest-Q1]] — 같은 배치
- [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2610.31329 (arXiv 2610.31329)
- 열어 본 것: HF papers API · **arXiv HTML v1 전문**(Table 2·4·6·7·8, §8) · GitHub API(repo·contents·languages·LICENSE 본문) · HF models API
- 관측: 2026-10-24T09:06Z (18:06 KST)
- 신뢰도: ⭐⭐⭐⭐ (코드·가중치 실존 · 표 다수 · 단 텍스트 매팅은 자체 벤치)
