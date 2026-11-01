---
title: "MLLM Retrieval Heads — 근거 탐색 헤드는 모달리티 간에 공유된다"
type: source
domain: ai-news
tags: [ai-news, interpretability, multimodal, retrieval]
created: 2026-11-01
updated: 2026-11-01
sources: [https://huggingface.co/papers/2610.32411]
reliability: medium
---

**HF**: published 2026-10-23 · upvote 28 · 저자 5(중국과학원 정보공학연구소 · Tencent) · arXiv 2610.32411 · HF `githubRepo` 없음

## 핵심 인사이트
> [!insight] 2% 미만의 공유 헤드가 인과적으로 중요하다
> 같은 정답을 말로 또는 화면으로 준 쌍 입력을 만들어 내용을 고정했다. 18개 체크포인트에서 검색 헤드는 희소하고 모달리티 간 대부분 공유되며, 옴니모달 모델은 백본의 헤드를 대체로 보존한다. 제거하면 시청각 검색이 거의 사라지고 문서 이해·공간 지각·시각 수학도 나빠진다.

> [!warning] 6.03점의 기준점
> Qwen3-VL-8B MMDocIR **Micro** R@1 56.45→62.48(+6.03) · Macro는 +5.05 · 레이아웃 Micro +1.46. **출판된 검색기보다 위지만 평가 설정이 달라**, 저자는 같은 설정의 미학습 헤드 대비 이득만 통제된 비교로 본다. 무작위 헤드는 38.00이다.

## 도메인별 추출
- **즉시 활용**: NO(코드 저장소 미확인). **6개월 영향력**: 어텐션 해석이 모델 개선의 목적함수로 쓰인 사례다. 문서 RAG의 페이지 선택에 연결된다.
- **허와 실**: "공유 헤드 2% 미만"은 비중 수치이며 효과 크기가 아니다. 효과는 제거 실험 쪽에서 읽어야 한다.

## 관련 페이지
- [[Youtu-Parsing-Omni]] · [[Qwen]] · [[Tencent]] · [[한정어-탈락]]

## 원본
- 출처: https://huggingface.co/papers/2610.32411
- 확인 범위: HF `api/papers` · arXiv HTML 본문 · 🔴 코드 실행 0회 · 수치는 전부 저자 보고
- 신뢰도: ⭐⭐ (코드 미확인 · 볼트 재현 없음)
