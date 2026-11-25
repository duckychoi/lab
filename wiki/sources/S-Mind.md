---
title: "S-Mind — 공간 토큰으로 다시점 기하를 MLLM 내부에 심는 공간지능 학습 (arXiv 2611.28649)"
type: source
domain: slam-3dgs
tags: [slam-3dgs, paper, spatial-intelligence, mllm, lora, multi-view, scene-tokens, qwen]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/papers/2611.28649]
reliability: medium
---

**논문**: arXiv 2611.28649 · 업보트 **31**(수집기 11-25) → **32**(볼트 API 11-25) · 소속 Nanyang Technological University · 저자 15명 · 코드 https://github.com/KANABOON1/S-Mind (★11 · Apache-2.0)

## 핵심 인사이트
> [!insight] 뷰당 장면 토큰 2개 + 카메라 토큰 4개 — 3D를 외부 도구가 아니라 "내부 토큰"으로 심는다
> Qwen3.5(4B · 9B)에 **뷰당 장면 토큰 2개 + 카메라 토큰 4개**를 넣어 ① 여러 시점을 하나의 3D 장면으로 융합 ② 추론 중 채택한 시점으로 장면을 재표현하도록 지도(**LoRA r64** — [[동결-교정층]] 표본). 표 2 탐침: 융합 점 복원 65.11%(기준선 최대 16.02%), 선언 시점 변환 82.17%(최대 37.28%). 표 5: 변환된 장면 토큰을 바꿔치면 회전 과제 정확도 76.0 → 59.5로 떨어져 **토큰이 실제로 쓰인다는 인과 근거**. 도구 기반 방법 대비 속도: MindCube-Tiny **81배**(111.74 → 1.38초, 정확도 56.95 → 88.00), ViewSpatial 115배(표 1).

> [!warning] 초록은 이긴 상대만 나열하고 지는 행(Claude)은 본문에만 있다 — [[자기제한-명시]] 반대 사례(초록-본문 비대칭)
> 4개 공간 벤치 평균 **9B 74.03%** — GPT-6-Astra 73.58(+0.45) · Qwen3.8-Flash 73.98은 넘고 **Claude-Opus-5.5 74.15에는 0.12점 진다**. 본문 산문에는 *"matches GPT-6-Astra, Qwen3.8-Flash, and Claude-Opus-5.5 (73.58%, 73.98%, and 74.15%)"* 로 **전부 공개되어 있으나**(볼트 11-25 HTML 직접 확인 — 수집기가 "주 결과표가 이미지라 행별 확인 불가"라고 했던 수치는 실제로는 본문 산문에 존재), **초록의 우위 목록에는 Claude가 빠져 있다**: *"surpasses frontier general models such as GPT-6-Astra (+0.45), Kimi-K3.1-Pro (+1.97), and GLM-5.3-Flash (+7.80)"*. 본문은 "matches"(동률 취급)로 정직, 초록만 선택적. 프런티어 수치는 EASI 리더보드(2026-07-01) 인용값 — 원문 각주로 확인.

## 도메인별 추출 (slam-3dgs)
- **실용성**: 소형 오픈 VLM(4B/9B)의 공간 추론을 크게 올리는 방법 — 로봇 · AR용 경량 모델 후보. LoRA만으로 도구 기반 방법 대비 81배 속도.
- **필수 레퍼런스**: 장면 토큰 교체 실험(표 5) — "토큰이 실제 기하를 담당하는지"를 입증하는 인과 설계, 공간지능 계열 평가 설계 참고.
- **한계**: 레포 ★11 초기 단계 · 프런티어 비교는 타 리더보드 인용(2026-07 시점) · 4개 자체 벤치 중심.
- **액션**: 없음(관찰 — 소형 VLM 공간 과제 요구 시 재검토).

## 관련 페이지
- [[자기제한-명시]] · [[동결-교정층]] · [[Depth-Pro-2]] · [[slam-3dgs]]

## 원본
- 출처: https://huggingface.co/papers/2611.28649
- 확인 범위: HF papers API(볼트 11-25 — 업보트 32 · NTU · githubRepo 일치) · **arXiv HTML 직접 판독(볼트 11-25)** — Claude 지는 행 · EASI 인용 각주 · 초록 우위 목록 원문 문자열 확인, 수집기 판독과 일치 · 실행 0
- 신뢰도: ⭐⭐⭐ (초록 선택 비교는 있으나 본문이 정직 · 수치 원문 검증 완료)
