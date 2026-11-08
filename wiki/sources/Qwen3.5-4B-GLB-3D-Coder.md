---
title: "ccore/Qwen3.5-4B-GLB-3D-Coder — 텍스트로 GLB 내보내기 버튼 달린 Three.js 페이지를 쓰는 4B. 정량 벤치 0, 비교는 이미지 1종"
type: source
domain: local-llm
tags: [local-llm, hf-model, qwen3.5, fine-tune, threejs, glb, 3d, game-asset, code-generation, gguf, synthetic-data]
created: 2026-11-08
updated: 2026-11-08
sources: [https://huggingface.co/ccore/Qwen3.5-4B-GLB-3D-Coder, Qwen3.5-4B-3D-Coder.md]
reliability: low
---

**HF**: [ccore/Qwen3.5-4B-GLB-3D-Coder](https://huggingface.co/ccore/Qwen3.5-4B-GLB-3D-Coder) · 다운로드 **24,479(30일 = 누적)**(볼트 11-08 API · 수집기 20,256 → **+4,223/1일**) · ♥265 · trendingScore 241 · Apache-2.0 · base Qwen/Qwen3.5-4B · created 11-01 · sha `8f32a199`(lastModified 11-06) · GGUF Q4_K_M·Q8_0

## 핵심 인사이트
> [!insight] 전작([[Qwen3.5-4B-3D-Coder]])의 "장면 생성"을 "에셋 내보내기"로 좁혔다
> 설명 → 미리보기 + **Export GLB** 버튼이 달린 완결 HTML/JS → 브라우저에서 `.glb` 저장 → 게임 엔진 반입. 학습 데이터셋 `ccore/ThreeJS-3D-GLB-Assets` 공개(**40 domains · 3,918예**, 카드 grep 검출). 같은 개인 개발자가 1주 만에 낸 후속 — "특화 소형 모델을 장르 단위로 계속 쪼개는" 개인 레시피의 반복.

> [!warning] 평가 = 동일 프롬프트 좌우 비교 이미지
> 카드 비교 대상 **DeepSeek V4.1 Flash 1017(high reasoning effort)**(grep 4회) — 정량 지표 0. "recorded evaluation" 은 Q8_0·thinking on 조건이라고만 적혀 있다. 전작과 마찬가지로 **합성 데이터의 생성 모델·약관 미확인**. 11-05 이전 다운로드분은 재다운로드 필요(카드 공지).

## 도메인별 추출 (local-llm)
- **실용성 판단**: 4B Q4_K_M — 노트북급. 지연 수치 없음.
- **Hermes 적용**: NO(3D 에셋 무관). 인디 게임·프로토타입 에셋 초안용.
- **트레이드오프**: 로우폴리 한정 · 품질 정량 근거 없음.
- **오픈소스 구현체**: 가중치 + 데이터셋 공개.

## 관련 페이지
- [[Qwen3.5-4B-3D-Coder]](전작) · [[Qwen]] · [[AI-3D-생성]] · [[특화-역류]] · [[계수기-배수]]
- 같은 배치: [[idol]](이미지→3DGS, 다른 3D 생성 경로)

## 원본
- 출처: https://huggingface.co/ccore/Qwen3.5-4B-GLB-3D-Coder
- 확인 범위: HF API expand(볼트 11-08) · 카드 raw 15,453B grep(3,918 · 40 domains · Export GLB · DeepSeek V4.1 Flash 1017 검출) · 추론 0회
- 신뢰도: ⭐ (개인 · 벤치 없음)
