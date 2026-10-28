---
title: "Hy-Nomas (Tencent Hunyuan) — 8B 오픈 가중치 인터랙티브 월드모델. 텍스트·카메라 혼합 지시에서 앞서지만 공간 기억은 Genie 3에 진다(승 13.3% / 패 30.0%)"
type: source
domain: ai-news
tags: [ai-news, hf-paper, world-model, interactive-video, open-weights, tencent, hunyuan, diffusion, camera-control, lora, rtx4090, slam-3dgs]
created: 2026-10-28
updated: 2026-10-28
sources: [https://huggingface.co/papers/2610.36729, https://github.com/Tencent-Hunyuan/Hy-Nomas, https://arxiv.org/html/2610.36729]
reliability: medium
---

# Hy-Nomas: Towards Free-form Interactive World Generation

**HF**: https://huggingface.co/papers/2610.36729 · published **2026-10-27** · **Tencent Hunyuan**(Qiaoling Chen 외 · 저자 **38**) · upvote **89**(수집기 일치)
**코드**: https://github.com/Tencent-Hunyuan/Hy-Nomas — ★**328**(🔴 수집기 274 → **+54 드리프트**) · GitHub API license `NOASSERTION`이지만 LICENSE 본문 첫 단락은 *"Hy-Nomas is licensed under **Apache-2.0**, except for the third-party components"*다(Tencent 레포에서 반복되는 병합 고지 → 파서 실패 패턴, [[Tencent]] 참조). 서드파티 구성요소 일부는 **Tencent Hunyuan Community License**를 따른다(LICENSE 729행). 레포에는 `hymm/` `reactor/` `captioning_harness/` `kernel/` 디렉터리와 기술 보고서 PDF가 있다.
**가중치**: HF `tencent/Hy-Nomas`(base_ar · distilled · **distilled_int8** · LoRA cinematic/dual_arm_robotics · PE · VAE DCAE-V) · 벤치 `tencent/Hy-Nomas-Bench`
**신뢰도**: ⭐⭐ medium

> [!insight] 핵심 인사이트 — "설명은 계속 보이게, 행동 지시는 자기 시간 창에만"
> 8B autoregressive MMDiT가 캐시된 이력을 조건으로 가변 길이 세그먼트를 생성한다. 핵심은 **구조화 캡션 + action-aware causal attention**이다. 장면과 주체를 설명하는 맥락은 세그먼트를 넘어 접근 가능하고, 행동 지시는 해당 시간 창에서만 보인다(세그먼트 안에서 행동 순서가 뒤바뀌는 문제를 저자가 직접 관찰한 뒤 고친 설계). **VLM Prompt Enhancer**가 사용자 요청과 멀티모달 이력을 다음 세그먼트의 구조화 조건으로 바꾼다. 커리큘럼 순서는 causal → 텍스트 → 카메라 → **자기 생성 이력으로 학습** → 디퓨전 증류다.
> 실용 포인트: **RTX 4090 1장**에서 돈다(INT8 가중치·KV, sliding-window attention, CPU offload). 1280×704 · 24FPS · 100초(7세그먼트) 생성 시 **피크 20.53 GiB**.

> [!warning] 주의 — 초록에 정량 수치가 없어서 arXiv 본문을 한 번 확인했다
> - 👥 **평가는 전부 인간 쌍대 비교(승/무/패)다.** 3인 1조 훈련된 평가자가 기준을 맞춘 뒤 평가했다. 자동 지표는 없다. 수집기의 "정량 수치 없음"은 초록 기준으로는 맞지만, 본문에는 승률이 있다.
> - ✅ Bench-1(멀티턴 자유 텍스트): 지시 따르기 승률 **65.0%** vs HappyOyster-Directing, **75.0%** vs LingBot-World v2. 🔴 **물리적 그럴듯함은 HappyOyster 상대 45.0%**(무승부를 빼면 우위일 수 있지만, 승률 자체는 50% 미만이다).
> - Bench-2(카메라, 100개 궤적): 승/무/패 vs Genie 3 **32/54/14** · HappyOyster **36/54/10** · LingBot v2 **29/61/10**. 무승부가 과반이어서 저자도 *"advantage is smaller for camera control"*이라고 썼다.
> - 🔴 **Bench-4(공간 기억) vs Genie 3: 승 13.3% · 무 56.7% · 패 30.0%** — 저자가 *"Genie 3 maintains stronger spatial consistency"*라고 인정했다. **수집기 요약은 이 부정적 결과를 빠뜨렸다**(→ [[인용-부호]] 10-27 InteractiveWorld와 같은 패턴).
> - ⚖️ 비교 조건이 서로 다르다. Genie 3는 공식 API가 텍스트 상호작용을 지원하지 않아 Bench-2·4에서만 평가했다. HappyOyster는 모드를 나눠 평가했다. LingBot v2는 저자가 직접 개조했다. 이미지가 필요한 모델은 Hy-Nomas가 만든 첫 프레임으로 시작했다 → [[비매칭-비교]]. "superior over existing world models"는 **Bench 1~3에 한정된 말**이다.
> - 📌 Hy-Nomas-Bench는 자체 벤치다(Bench-3은 60케이스, 2~7세그먼트).

## 도메인별 추출 (ai-news · slam-3dgs 접점)
- **써 볼 가치**: 오픈 가중치 + 단일 4090 + LoRA 적응 워크플로까지 공개됐다. **dual_arm_robotics LoRA**는 로봇 데이터 생성용 시뮬레이터 후보다(저자 결과는 정성 비교뿐: 베이스 모델은 사람 손과 양팔 로봇을 혼동했다).
- **slam-3dgs 연결**: 공간 기억(재방문 일관성)이 약점이라는 결과는 [[월드모델]]의 "명시적 3D 메모리 없는 비디오 모델" 한계와 같다. Genie의 우위를 저자는 Street View grounding 덕분으로 추정했다. 3DGS/SLAM 기반 메모리([[Latent-Spatial-Memory]] · [[HY-World-2.0]] · [[AnchorWorld]])를 결합할 여지가 있다.
- 계보: [[HY-World-2.0]](같은 Tencent 월드모델 라인) · [[Diffusion-월드모델]] · [[World-Infinity]] · [[InteractiveWorld]](이름만 유사, Meta 어시스턴트 벤치)

## 관련 페이지
- [[Tencent]] · [[Hy3]] · [[HY-World-2.0]] · [[Hunyuan3D-Buffalo]]
- [[월드모델]] · [[Diffusion-월드모델]] · [[비매칭-비교]] · [[인용-부호]]
- 같은 배치(10-28): [[Rollback]] · [[PDRVLA]] · [[ChronoReplay]] · [[The-Trinity]]
- [[ai-news]] · [[slam-3dgs]]

## 원본
- https://huggingface.co/papers/2610.36729 · https://github.com/Tencent-Hunyuan/Hy-Nomas · https://arxiv.org/html/2610.36729 (§6.2, §7.2~7.4)
- 볼트 실측(2026-10-28): upvote 89 · 저자 38 · ★328 · license NOASSERTION(본문 Apache-2.0) · 레포 생성 2026-10-21 · README 14·45·158·184행
