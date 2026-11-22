---
title: "FlashML-org/FreeVideo — MiniMax H3 를 VRAM 8GB 부터 돌리는 로컬 추론 엔진 (🔴 가중치는 H3 Community License · 지역 제한)"
type: source
domain: video-saas
tags: [video-saas, github-trending, minimax-h3, local-inference, comfyui, int8, license]
created: 2026-11-22
updated: 2026-11-22
sources: [https://github.com/FlashML-org/FreeVideo]
reliability: medium
---

**GitHub**: ★4,205(볼트 API 11-22 · 수집기 11-21 3,960) · Python · 코드 Apache-2.0 · 생성 2026-09-13 · push 2026-11-21

## 핵심 인사이트
> [!insight] 저사양 진입 장벽은 내려갔고, 한국에서의 걸림돌은 그대로다
> OpenVDN 의 8스텝 VDN-H3(arXiv 2609.20744) 위에 가중치 스트리밍 · 비동기 프리페치 · 청크 연산을 얹어 [[MiniMax-H3]] 를 "VRAM 8GB + RAM 16GB 부터" 구동한다는 ComfyUI 플러그인 겸 Windows/macOS/Linux 런처. 텍스트 · 첫/끝 프레임 · 이미지/영상/오디오 레퍼런스, LoRA, 2패스 샘플링, v0.4.0 에이전트 연동 · 1분 이상 영상, v0.5.0 H3 Image(최대 16MP).

> [!warning] 🔴 라이선스 — [[라이선스-지역-제외]] 파생 8번째
> README 149행(볼트 확인): 코드는 Apache-2.0, **가중치는 MiniMax H3 Community License — "includes territorial and acceptable-use restrictions"**. 볼트 11-12 실측으로 H3 LICENSE 는 대한민국을 적용 지역에서 제외한다. 이 레포는 제한의 존재를 README 에 스스로 적었다(정직한 쪽) — 다만 어느 지역인지는 적지 않는다.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 가중치 스트리밍으로 VRAM 상한을 낮추는 방식은 [[Tideway]] (LLM MoE) 와 같은 발상의 영상판.
- **프롬프트 패턴 / 워크플로우**: 생성 영상에 워크플로를 내장(v0.2.3 — 영상을 ComfyUI 캔버스에 떨어뜨리면 프롬프트 · 시드 복원, 볼트 README 27행 확인). 재현성 UX 로 참고할 만하다.
- **수치**: README 의 정량은 "RTX 3090 에서 5초 영상이 int8 로 약 2.3배 빨라짐"(v0.3.0, 25행) 1건 — **자기 이전 버전 대비 상대값**이고 절대 생성 시간 · 화질 지표는 없다([[상대속도-가림]]). Mac 은 M5 24GB 프리뷰.
- **경쟁 우위 빈틈**: 로컬 8GB 구동이 사실이어도 한국 사업자는 가중치 조건 때문에 서비스에 못 쓴다 → API 형 대안 유지.

## 관련 페이지
- [[MiniMax-H3]] · [[MiniMax]] · [[라이선스-지역-제외]] · [[Minimax-h3_Singularity-x-10Eros-Max_PRISM]] · [[hyperflow-h3-flash]] · [[Tideway]] · [[상대속도-가림]] · [[video-saas]]

## 원본
- 출처: https://github.com/FlashML-org/FreeVideo
- 확인 범위: GitHub API · README 원문 문자열(8GB · 2.3x · territorial 149행 · community-results) · 🔴 docs/community-results.md 미열람 · 실행 0
- 신뢰도: ⭐⭐⭐
