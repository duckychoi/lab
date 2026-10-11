---
title: "ConwayResearch — 8GB 미만 2비트 양자화로 도구호출을 지키는 제공자"
type: entity
domain: local-llm
tags: [entity, huggingface, gguf, quantization, iq2, tool-calling, bfcl, 숨김유인-부호]
created: 2026-10-11
updated: 2026-10-11
sources: [Underdog-Saluki-27B.md]
reliability: low
---

# ConwayResearch

**HuggingFace**: https://huggingface.co/ConwayResearch
**대표 산출물**: [[Underdog-Saluki-27B]] — dl30 **59,191** · dlAll **59,191** · ♥**295** · trendingScore **287** · Apache-2.0(볼트 API 실측 2026-10-11)
✅ **`dl30 == dlAll`** ⇒ **30일 창보다 어린 저장소**다 → [[지표-창길이]]

> [!insight] 🏆 특징 — 양자화 목표를 "크기"가 아니라 "능력 보존 축"으로 잡는다
> [[Qwen3.8-27B]](54GB)를 **7.89GB IQ2 단일 GGUF** 로 줄이고 **stock llama.cpp** 로 돌아가게 했다(패치 불필요).
> 🎯 **그리고 보존 대상을 도구호출로 명시했다**: 자체 `Underdog Bench`(= BFCL v4 120 과제, **모델 테스트 전 동결 선언**, thinking off · temp 0)에서 **88 vs 원본 84** ⇒ **크기 1/6.8 에 +4**. 병렬 도구호출은 **42 vs 35**.
> 🔴 **대가가 크다**: AIME 2025 **79.2 vs 96.7(-17.5)** · AIME 2026 80.0 vs 94.6 · MuSR 67.5 vs 79.6 ⇒ **지시이행·도구호출은 유지되고 수학·다단계 추론이 무너진다.**
> ⇒ 🆕 **"양자화 손실은 균일하지 않다"는 볼트 미기록 분해**다(n=1, 개념 신설하지 않는다).

> [!insight] 🏆🏆 **[[숨김유인-부호]] 근거 있는 자기 축소 — 볼트 판정 기준의 신설 근거가 됐다**
> 카드 명시 3건: *"public scores come from a different harness than ours"* · *"120 tasks is a modest test"* · *"a few tasks of any gap is run-to-run variation"*
> 🎯 **자기 우위(88 vs 84 = 4과제)를 저자가 직접 "분산 범위일 수 있다"고 깎는다.**
> ⇒ 🆕 **10-10 [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] 와 같은 행동인데 결정적 차이가 있다: 여기서는 비교 하네스가 실제로 다르므로 깎을 근거가 있다.**
> 📌 **볼트 판정: "자기 우위 축소"를 일률 반례로 셀 수 없고 근거 유무로 2분한다** — 본 제공자는 **근거 있는 축소**(반례 강도 약함: 사실을 적은 것이므로 유인에 반하지 않는다).

> [!warning] 🔴 미확인
> 제공자 실체(개인/연구조직) · 소속 · 다른 저장소 · 자금 출처 **전부 미조회.** HF 프로필 **미열람.** 📌 이름(`ConwayResearch`)이 조직처럼 보이나 **확인하지 않았다.**
> 🔴 ***"9개 벤치 96% 평균 보존율"* 의 목록·계산식이 카드에 없다**(표에는 7개뿐). 볼트 역산은 BFCL 2종 포함 가정 시 **95.7%** 로 근접하나 **확정 아님.**
> 🔴 **볼트가 모델을 다운로드·실행하지 않았다** — 메모리·토큰/초 실측 0건. *"테스트 전 동결 선언"* 은 **검증 불가**다.

## 관련 페이지
- [[Underdog-Saluki-27B]] — 주 저장소
- [[Qwen3.8-27B]] — base_model(54GB 원본) · [[ISTA-DASLab]] — GSQ-RCO 경로
- [[숨김유인-부호]] — 🏆 **근거 유무 2분 판정의 신설 근거**
- [[Ternary-Bonsai-2-27B]] · [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] — 같은 축 경쟁 양자화
- [[하네스-설계-축]] · [[지표-창길이]] · [[local-llm]]

## 원본
- 대표 산출물: [[Underdog-Saluki-27B]] (https://huggingface.co/ConwayResearch/Underdog-Saluki-27B-1.0)
- 확인: ✅ **볼트 HF API 실측**(dl30·dlAll·♥·trendingScore·pipeline_tag·lastModified) · 🔴 프로필·카드 본문 미열람 · 모델 미실행
- 신뢰도: ⭐⭐ (저장소 메타 볼트 실측 · 벤치 설정 구체적 · **전건 벤더 자기보고 · 제공자 실체 미확인**)
