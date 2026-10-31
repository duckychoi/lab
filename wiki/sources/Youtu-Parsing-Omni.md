---
title: "Youtu-Parsing-Omni — 문서·이미지·오디오·비디오 단일 5B 파서"
type: source
domain: ai-news
tags: [ai-news, document-parsing, multimodal, open-weight, tencent]
created: 2026-10-31
updated: 2026-10-31
sources: [https://huggingface.co/papers/2610.39301]
reliability: medium
---

**HF**: published 2026-10-29 · upvote 128 · 저자 30 ([[Tencent]] Youtu) · arXiv 2610.39301

## 핵심 인사이트
> [!insight] "SOTA 96.96"의 격차는 0.05점이고, 전체 1위는 비공개 모델이다
> OmniDocBench v1.6: **96.96 vs TeleOCR 96.91(+0.05)** — 수치상 사실상 동률이다. OmniParsingBench 평균: 오픈웨이트 1위 75.08이지만 **비공개 Gemini-3-Pro가 77.44로 더 높다**(초록의 "open-weight" 한정어가 정확히 이 차이를 가린다 — 수집기는 한정어를 보존했다 ✅). 진짜 차별점은 오디오 78.08 · 텍스트 많은 영상 75.62 · 자연 영상 74.18로 **세 칸에서 Gemini-3-Pro(76.74 · 76.80 · 74.82)와 엇갈리는** 영역이고, 오픈웨이트 Logics-Parsing-Omni(75.58 · 65.36 · 67.34)는 크게 앞선다.

> [!warning] 저자 자백: 추론 가속 미구현
> Limitations 절: 전작의 병렬 디코딩이 없고 큰 디코더로 **자기회귀 디코딩**하므로 표처럼 밀집한 콘텐츠의 처리량이 **더 낮을 것으로 예상**한다고 적었다. 정확도 표만으로 도입을 판단하면 안 된다. 기하(Geometry) 항목(74.33)도 Gemini-3-Pro 85.43 · Logics 76.34보다 낮고, 자연 이미지(62.84)는 Qwen3.5 63.87 · Logics 67.53보다 낮다.

## 도메인별 추출
- **즉시 활용**: 조건부 YES — 음성·영상을 시공간 좌표가 달린 레코드로 뽑아 인용까지 하려는 경우 후보. 볼트 영상 인제스트(`down-analysis`) 대체 실험 대상. 🔴 볼트 미실행 · 처리 속도 미상 · 라이선스 필드 NOASSERTION 은 레포 파일 확인 필요.
- **트레이드오프**: 5B 단일 체크포인트로 10개 과제를 담지만 속도 수치를 초록이 주지 않는다.
- **대체 관계**: 다단계 전문 OCR(TeleOCR 등) 대비 정확도 동률 + 단일 모델이 장점. 문서만 다룬다면 갈아탈 이유가 약하다.

## 관련 페이지
- [[Tencent]] · [[Qwen]] · [[한정어-탈락]] · [[Your-Benchmark-Empirical-Measure]]

## 원본
- 출처: https://huggingface.co/papers/2610.39301 · 코드 https://github.com/TencentCloudADP/youtu-parsing (★356 · 라이선스 필드 NOASSERTION) · 가중치 https://huggingface.co/tencent/Youtu-Parsing-Omni (dl30 2,940 · ♥122 · 볼트 실측)
- 확인 범위: HF `api/papers` · arXiv HTML 본문 열람(2026-10-31) · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐ (저자 자기 측정 · 볼트 재현 없음)
