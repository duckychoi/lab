---
title: "unsloth — 양자화 재배포 생태계의 관심 1위, 그러나 다운로드 1위는 아니다"
type: entity
domain: local-llm
tags: [entity, huggingface, gguf, quantization, on-device, 원본-파생-역전, 배포출처-봉인]
created: 2026-10-11
updated: 2026-10-11
sources: [embeddinggemma-2-GGUF.md]
reliability: medium
---

# unsloth

**HuggingFace**: https://huggingface.co/unsloth
**금일 산출물**: [[embeddinggemma-2-GGUF]] — dl30 **50,551** · ♥**241** · trendingScore 235 · Apache-2.0 · `base_model = ['google/embeddinggemma-2']`(볼트 API 실측 2026-10-11)

> [!insight] 🏆 볼트가 실측으로 확인한 위치 — 파생 생태계 "2위, 관심 1위"
> 볼트가 `?search=embeddinggemma-2&limit=100` 으로 파생 전수를 열거해 2세대 64건을 집계한 결과:
> - **다운로드 1위는 `onnx-community/embeddinggemma-2-ONNX` 76,556** 이고 unsloth 는 **50,551 로 2위**다(1위의 0.66배).
> - **관심은 반대다**: unsloth ♥**241** vs onnx-community ♥**15** = **16.1배**.
> ⇒ 🎯 **즉 unsloth 는 "가장 많이 쓰이는 재배포자"가 아니라 "가장 많이 알려진 재배포자"다.**
> 📌 **해석: ONNX 는 배포 런타임이라 CI·서비스가 기계적으로 받아가고, unsloth 는 사람이 별을 준다** — ⚖️ **두 지표가 다른 모집단을 센다.** 🆕 **이것이 [[원본-파생-역전]] 의 진짜 축이 "원본 vs 파생"이 아니라 "런타임 수요 vs 커뮤니티 관심"임을 보여준다.**
> 🔴 **수집기는 unsloth 를 사실상 파생 1위로 제시했고(45,605 원본과 단일 비교) 볼트가 반증했다** — 세부는 [[embeddinggemma-2-GGUF]].

> [!warning] 🔴 성능 주장의 근거가 레포 안에 없다 — [[배포출처-봉인]]
> unsloth 는 일반적으로 *"Dynamic 3.0 이 다른 양자화를 능가한다"* 고 주장하나 **금일 모델([[embeddinggemma-2-GGUF]])에 대한 수치는 카드에 없다.**
> ⇒ 🎯 **양자화 손실을 확인할 경로가 카드 내부에 0개다.** 📌 카드에 실린 벤치(MTEB code 78.68 등)는 **전부 원본 전정밀도 수치**이므로 **"GGUF 로 그 점수가 난다"고 쓰면 틀린 인용**이다.
> ⚖️ **성능 주장을 이 레포에서 하지 않았으므로 과장은 아니다** — 금일 "벤치 부재" 3건 중 하나다.

> [!warning] 🔴 미확인
> 조직 실체·규모·자금 출처 **미조회.** HF 프로필·`unsloth.ai` **미열람.** 📌 **볼트는 unsloth 를 이번에 엔티티로 처음 세웠다** — 그간 GGUF 재배포자로 여러 번 스쳤으나 페이지가 없었다.
> 🔴 **Dynamic 3.0 양자화 방식의 기술적 내용 미확인** · 전체 보유 모델 수 미집계.
> 🔴 **한국어 품질 미확인**(금일 모델의 볼트 용도 전제인데 모른다).

## 관련 페이지
- [[embeddinggemma-2-GGUF]] — 금일 산출물
- [[원본-파생-역전]] — 🏆 **집계 역전 재확립 · 런타임 수요 vs 커뮤니티 관심 축**
- [[배포출처-봉인]] — 양자화 손실 확인 경로 부재
- [[Google]] — 원본 `google/embeddinggemma-2` 제공자
- [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] · [[Qwen-Image-2.1-Uncensored-GGUF]] — 볼트 보유 GGUF 선례
- [[HuggingFace]] · [[local-llm]]

## 원본
- 대표 산출물(금일): [[embeddinggemma-2-GGUF]] (https://huggingface.co/unsloth/embeddinggemma-2-GGUF)
- 확인: ✅ **볼트 HF API 실측** — 해당 모델 expand 8필드 · `base_model` 확정 · **파생 99건 열거 후 2세대 64건 집계**(unsloth 순위 2위 확정) · 🔴 프로필·카드 본문 미열람
- 신뢰도: ⭐⭐⭐ (볼트가 **생태계 내 상대 위치를 전수 열거로 실측**했다 / 🔴 조직 실체 미확인 · 자체 양자화 벤치 0건)
