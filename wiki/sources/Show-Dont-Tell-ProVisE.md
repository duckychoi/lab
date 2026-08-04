---
title: Show, Don't Tell (ProVisE) — 생성 픽셀로 공간인지를 평가하는 프로토콜
type: source
domain: video-saas
tags: [ai-news, hf-paper, spatial-cognition, image-generation, benchmark, evaluation, vlm]
created: 2026-07-25
updated: 2026-07-25
sources: []
reliability: medium
---

# Show, Don't Tell (Evaluating Spatial Cognition in Generative Pixels Rather Than LLM Text)

> [!insight] 핵심 인사이트
> HF Daily ↑34. 문제제기: 공간 과제는 원래 **가리키기·표시·그리기 같은 시각 제스처**로 표현되는데, 기존 벤치는 모델을 좌표·텍스트 출력으로 강제해 **"답-인터페이스 불일치"**를 만들고 이미지 생성 모델을 불리하게 한다. 해법 **ProVisE**(Protocolized Visual Evaluation): 이미지 생성모델이 표시영역·깊이필드·궤적 등 **픽셀 공간 답**을 프로토콜대로 내면, 이를 좌표·선택지로 파싱해 **원래 벤치 지표로 채점**(텍스트 VLM과 동일 지표·의미로 비교). 결과가 흥미롭다 — 깊이추정·관계검증처럼 **답이 시각적일 땐 이미지 생성모델이 +18점**, 크기비교·실현가능성처럼 **관측 너머 변환이 필요한 추론은 텍스트 모델 우세**. 상호보완적이며, 시각적 복구가 텍스트 모델 실패의 **~37%를 회수**. 오답의 88%는 파싱은 되나 예측이 틀림 → "소통 채널은 작동, 실패는 기술이 아니라 공간인지".

> [!note] 배경 정보
> "생성 픽셀로 능력을 평가"는 [[KeyFrame-Compass]](키프레임 조건부 생성 평가)·[[Generative-World-Renderer]](엔진 G-buffer 렌더)와 같은 **생성 출력을 정량 잣대로 삼는** 흐름. down-analysis/영상 이해에서 "모델이 공간을 이해하는가"를 **텍스트가 아닌 시각 출력으로** 검증하는 관점은 video-saas 품질평가에 시사.

## 도메인별 추출 (video-saas / ai-news 교차)

- **기능 벤치마킹**: 이미지 생성모델을 "공간인지"로 평가하는 프로토콜 — 내 영상/이미지 파이프의 출력 품질을 **정답 지표로 자동 채점**하는 설계 참고.
- **크리에이터 인사이트**: 생성모델은 "보여주는" 과제(깊이·관계·궤적)에 강하고 "추론하는" 과제엔 약함 → 툴 선택 시 **태스크-인터페이스 매칭**이 품질을 가른다는 실전 교훈.
- **워크플로우**: ProVisE는 프로토콜을 **에이전트가 자동 설계·검증**(Agentic construction)해 새 벤치에 확장 — 평가 자동화 아이디어.
- **경쟁 우위 빈틈**: 텍스트 출력만 보던 영상 AI 평가에 "픽셀 출력으로 공간이해 검증"을 더하면, down-analysis 시각분석의 **정량 신뢰도** 확보 여지.

> [!warning] 미래형 ID·원문 미검증
> 초록 WebFetch 실확인(ProVisE·+18점·37% 회수·88% 파싱성공 구체 확인). 2607.21072 미래형 ID·원문·재현 미검증 medium. 수치는 벤치 구성·프로토콜 설계에 좌우.

## 관련 페이지
- [[KeyFrame-Compass]]
- [[Generative-World-Renderer]]
- [[VideoChat3]]
- [[video-saas]]
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2607.21072
- HF Daily Papers: ↑34
- 핵심: ProVisE — 이미지 생성모델이 픽셀공간 답 생성 → 파싱해 원 벤치 지표로 채점. 시각적 답 태스크 +18점, 추론 태스크는 텍스트 우세, 시각복구가 텍스트 실패 37% 회수, 오답 88%는 파싱성공·예측오류
- 신뢰도: ⭐⭐ (초록 WebFetch 실확인, 미래형 ID·원문·재현 미검증 medium)
