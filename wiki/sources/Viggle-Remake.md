---
title: "Viggle/Viggle-Remake — MiniMax-H3 위 LoRA 2종으로 영상 속 인물 교체·사물/배경 편집 + 영화 전체를 컷 단위로 처리하는 MCP 에이전트. 정량 벤치 0, 모델 안에 안전장치 없음"
type: source
domain: video-saas
tags: [video-saas, hf-model, video-editing, character-replacement, lora, minimax-h3, mcp, viggle]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/Viggle/Viggle-Remake]
reliability: medium
---

**HF**: https://huggingface.co/Viggle/Viggle-Remake · 다운로드(30일) **97,356** = 누적 97,356 · ♥246 · trendingScore 239 · `pipeline_tag: video-to-video` · base `MiniMaxAI/MiniMax-H3` · 생성 2026-10-22 · 수정 2026-11-07 (HF API 2026-11-10 09:06Z · 수집기와 전건 일치)
**라이선스**: 가중치 `minimax-h3-community-license`(`license: other`) · 코드·프롬프트 Apache-2.0(`LICENSE-CODE`)

## 핵심 인사이트
> [!insight] 모델보다 "컷 단위로 쪼개 돌리는 에이전트"가 제품이다
> `--mode swap`(인물·캐릭터 교체) · `--mode edit`(사물 교체/삭제/삽입 · 배경 · 날씨 · 조명) 각 rank-256 LoRA(2.67GB, rank 128/64 는 1.34/0.67GB). 입력 = 원본 영상 + **직접 칠한 키프레임** + 프롬프트. 원본의 모션·카메라·타이밍과 **사운드트랙은 그대로 실린다**(카드 148행: "Sound is carried, not made" — 무음 원본은 무음). 1회 렌더 90~345프레임(24fps, `--frames` = 17n+5, 권장 294 이하). 그보다 긴 영상은 **MCP 서버가 컷 분할 → 키프레임 작성 → 프롬프트 → 렌더 → 사운드트랙과 이어붙이기**를 한다(카드 107행).

> [!warning] 🔴 카드가 직접 쓴 위험 문구 (153~157행 볼트 확인)
> 동의한 배우의 재촬영·세트 변경용이라고 밝히면서, **실존 인물도 똑같이 합성해 낸다 · 정체성은 사용자가 칠한 프레임에서 온다 · 이미지 편집기의 안전장치는 이 모델 상류에 있고 모델 안에는 없다 · 신원이나 동의를 검증할 수 없다**고 적는다. 데모 영상에도 "AI-generated parody" 표기가 붙어 있다. SaaS 에 붙인다면 동의 확인은 서비스 계층의 책임이 된다.

> [!warning] 자원과 라이선스
> - 베이스 약 **144GB** + 텍스트 인코더 필수. `sample.py` bf16 은 **80GB+ GPU 1장**. RTX 5090(32GB)은 ComfyUI 워커로 1280×736 · 345프레임 창 하나에 **약 28분**(RAM 약 60GB), 데모 1편 전체에 약 3시간(카드 100~101행).
> - 정량 벤치 **0건**. 품질 근거는 데모 영상뿐.
> - 제품·서비스에 가중치를 실으면 MiniMax H3 Community License 의 의무(라이선스 사본 제공 · 수정 파일 표시 등, 카드 197~200행)가 붙는다. 전문은 볼트 미열람.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: "촬영본 리메이크"(인물 교체 · 배경/날씨 변경). 구현 난이도는 모델보다 **컷 분할 · 키프레임 일관성 · 이어붙이기 오케스트레이션**에 있다 — 그 부분이 MCP 로 공개됐다.
- **크리에이터 인사이트**: 키프레임을 사용자가 직접 칠해야 한다 = 정체성 통제권을 주는 대신 진입 장벽.
- **워크플로우**: 원본 → 컷 분할 → 컷별 키프레임 1~4장 → swap/edit 렌더 → 자가검수 → 원본 오디오와 결합.
- **경쟁 우위 빈틈**: 5090 에서 12초 창 하나에 28분 — 실시간 편집 UX 는 불가. 배치 큐 + 진행률 UI 가 필요.
- **디자인 레퍼런스**: 없음(카드에 UI 없음).

## 관련 페이지
- [[Viggle]] · [[MiniMax-H3]] · [[MiniMax]] · [[Qwen-Image-2.1-viggle-turbo]] · [[P-H3-Image-Comfy]] · [[rea-video]] · [[AI-영상-생성-2026]] · [[PCBRouteAgent]]

## 원본
- 출처: https://huggingface.co/Viggle/Viggle-Remake
- 확인 범위: HF API(expand) + 모델 카드 raw 11,532B(핵심 구절 행 번호 대조) · 🔴 추론 미실행 · 라이선스 전문 · mcp/README 미열람
- 신뢰도: ⭐⭐ (dl30 97,356 · ♥246 · 벤치 0)
