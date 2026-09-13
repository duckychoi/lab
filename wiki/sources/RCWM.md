---
title: RCWM — 재귀 장면 프로그램으로 3D 월드 복원
type: source
domain: slam-3dgs
tags: [slam-3dgs, hf-daily-paper, world-model, code-generation, 3d-reconstruction, no-numbers]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: medium
identifiers: [arXiv:2609.11499]
---

# RCWM — Recursive Code World Models: Building Complex Worlds through Recursive Scene Programs

**HF**: https://huggingface.co/papers/2609.11499 · **arXiv**: 2609.11499
**지표(2026-09-13 API 실호출)**: 업보트 **28** · 저자 **3인** · **발행 2026-09-10**
**드리프트**: 업보트·저자 수 **완전 일치**. 🔴 발행일 raw *"09-11"* → 실제 **09-10**
**도메인 재판정**: raw `ai-news` → **`slam-3dgs`** 이관. 단일 이미지 → 3D 장면 복원이 주제다.

> [!insight] 핵심 인사이트 — **표현이 아니라 "짓는 순서"가 빠져 있었다는 진단**
> 초록 첫 문장이 이 논문의 위치를 정확히 잡는다: *"Code world models represent worlds as executable programs, but **this representation alone does not determine how to construct a complex world**."*
> 🎯 **코드로 세계를 표현하자**는 이미 있었다. 없던 것은 **복잡한 세계를 어떤 절차로 쌓느냐**다. RCWM의 답은 **솔버가 자기 자신을 재귀 호출**하는 것이고, 모든 호출이 **같은 3단계**를 따른다:
> *"establish the whole, recursively reconstruct unresolved parts, and **revisit the whole** to refine their composition."*
> **전체 → 국소 → 전체 재방문**. 마지막 재방문이 설계의 요점이다 — 국소 정제 뒤에 생기는 *"경계·공간 관계·공유 오차"* 를 부모 단계가 흡수한다. 국소만 고치면 전체가 어긋나는 문제를 **구조로** 막는다.
> 이건 [[국소-수리-원리]] 에 빠져 있던 조각이다: **국소 수리 뒤에 전역 정합을 누가 책임지는가.** 답 = **부모 호출**.

> [!note] VLM 코딩 에이전트가 눈 역할을 한다
> *"A vision-language coding agent **directly compares reference images with scene renders** to guide refinement, recursive descent, and return."*
> 렌더 결과와 원본을 **직접 비교**해 ① 정제 방향 ② 더 내려갈지 ③ 돌아올지를 정한다. 재귀의 종료 조건이 고정 깊이가 아니라 **시각 비교 결과**다.
> *Reference-aligned views* 로 **공유 카메라 투영을 모든 레벨에 전파**해 레벨 간 좌표계가 갈라지지 않게 한다.

> [!warning] 🔴 **초록에 정량 수치가 하나도 없다 — 인용 시 수치 주장 금지**
> - 성능: *"outperforms prior code-based image-to-scene reconstruction methods"* — **벤치명 · 점수 · 비교군 전부 없음**
> - 어블레이션: *"Ablation studies further support the benefits of recursive construction and **suggest** that deeper calls **can** improve finer-scale reconstruction."* — **suggest · can** 으로 이중 헤지
>
> → 이 페이지에서 인용 가능한 것은 **구조 설명뿐**이다. 성능 비교 문장을 만들지 않는다.
> 같은 배치 [[FreeFlow]] 와 비교하면 결손의 단계가 보인다: **FreeFlow는 수치는 있고 대조군이 없다. RCWM은 둘 다 없다.**

## 도메인별 추출 (slam-3dgs)

- **현재 SOTA**: **판단 불가.** 자칭 우위이나 근거 수치 0개.
- **실시간 가능성**: **없다고 봐야 한다.** VLM 에이전트가 렌더-비교를 재귀적으로 반복하는 구조라 **호출 수가 장면 복잡도에 비례**한다. 실시간 SLAM 경로가 아니라 **오프라인 복원** 경로다.
- **카메라 파이프라인**: 입력 **단일 참조 이미지**. 출력은 **실행 가능한 장면 코드**(RSP) — 메시나 가우시안이 아니라 **프로그램**이다. → 편집·재실행이 되고, diff가 된다.
- **응용 가능성**: 🎯 출력이 코드라는 점이 실익이다. 3DGS 산출물은 고치기 어렵지만 **코드는 국소 수정이 가능**하다. 볼트의 [[검사가능성-공사]] 노선과 정확히 맞는다.
- **필수 레퍼런스**: 선행 code-based image-to-scene 계열 논문 확인 필요(초록에 이름이 없어 추적이 한 단계 더 든다).

> [!question] 미해결
> ① 재귀 **깊이의 실제 분포**와 비용 ② 어떤 벤치에서 쟀는가 ③ 실패 모드(재귀가 수렴하지 않는 장면). **셋 다 초록 밖.** 본문 확인 전까지 reliability **medium** 유지.

## 관련 페이지
- [[국소-수리-원리]] — **"국소 수리 후 전역 재정합"의 책임 주체**를 이 논문이 채운다
- [[월드모델]] · [[검사가능성-공사]] · [[Diffusion-월드모델]]
- [[World-in-World]] — 같은 배치·같은 "월드 모델" 명칭이나 **접근이 정반대**(RCWM=명시적 코드 재구성 / WiW=동결 비디오 모델 제어)
- [[FreeFlow]] — 같은 배치, 수치 결손의 앞 단계

## 원본
- 출처: https://huggingface.co/papers/2609.11499
- 신뢰도: ⭐⭐ (HF API 실호출 + 초록 원문 대조. **정량 근거 부재로 medium**)
