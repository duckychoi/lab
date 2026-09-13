---
title: Edge0-35B-A3B-preview — SSD 오프로드 MoE 엣지 추론
type: source
domain: local-llm
tags: [local-llm, edge-ai, moe, quantization, on-device, mlx, 한정어-탈락]
created: 2026-09-13
updated: 2026-09-13
sources: [raw.md]
reliability: high
identifiers: [Edge0/Edge0-35B-A3B-preview]
---

# Edge0-35B-A3B-preview — SSD 오프로드 MoE 엣지 추론

**HF**: https://huggingface.co/Edge0/Edge0-35B-A3B-preview · `Edge0/Edge0-35B-A3B-preview`
**지표(2026-09-13 API 실호출)**: 다운로드 **1,596**(30일) · ♥**626** · 트렌딩 **3위** · 생성 **2026-09-08**
**라이선스**: **apache-2.0**(카드 2행 실측) — 🔴 **raw가 라이선스를 아예 적지 않았다.** 이 배치 HF모델 3건 중 유일한 누락
**safetensors 실측**: **34,660,610,688 = 34.66B** — 이름 35B와 **정합**(반올림 범위)
**드리프트**: 다운로드·♥·생성일 **전건 일치**

> [!insight] 핵심 인사이트 — **전문가를 RAM이 아니라 스토리지에 둔다**
> 4비트 MoE 전문가 가중치를 **스토리지에 상주**시키고 라우팅된 것만 스트리밍해, RAM에는 **활성 가중치만** 올린다. 여기까지는 알려진 오프로드다.
> 🎯 차별점은 **prerouter** 다 — 다음 스텝에 필요한 전문가를 **한 스텝 앞서 예측**해 스트리밍 지연을 forward 계산에 **겹친다**. 오프로드의 고질적 문제(전문가 로드 대기)를 **예측으로 숨긴다**.
> 효과 주장: *"**up to +59%** decode throughput; the gain grows with storage"*(74행) — **up to** 표기이므로 상한이다.

## 🔴 헤드라인 vs 실측 — 조건절이 세 곳에 흩어져 있다

> [!warning] ① "폰급 메모리"의 측정 환경은 폰이 아니다
> 헤드라인(21행): *"A 35B-class sparse MoE that runs in **phone-class memory**."*
> **성능 표 바로 위 한 줄**(116행): *"Measured with `examples/bench.py` on a **Mac mini M4 Pro, 24 GB**"*
> → **24GB 데스크톱에서 잰 값이다.** 폰에서 측정한 수치는 카드에 없다. "폰급 메모리에 들어간다"와 "폰에서 쟀다"는 다른 주장인데 헤드라인은 앞을 말하고 독자는 뒤를 읽는다.

> [!warning] ② 3 GiB는 **조건부** 수치다 (같은 조건이 두 곳에 반복)
> - 표 각주(122행): *"\*Short contexts; **long contexts add KV cache**."*
> - Limitations(144~145행): *"Long contexts grow the KV cache; **use shorter contexts to keep peak memory at 3 GiB**."*
> → **"3 GiB"는 짧은 컨텍스트 전제에서만 성립**한다. 실측 peak는 **2.9 GiB**(표 120행).

> [!note] ③ 🔀 헤드라인이 오히려 **과소** 표기다
> 헤드라인(23·58행) *"**15 tok/s**"* vs **표 실측(120행) `14.9–17.7 tok/s`(범위)**.
> **표가 더 유리한데 산문이 하단값을 택했다.** prefill은 cold **113** / warm **140** tok/s.
> 📌 09-12에 볼트가 지적한 *"한정어 탈락은 양방향으로 일어난다"* 의 실례 — 이 카드는 **과장 방향 2건(①②)과 과소 방향 1건(③)을 동시에** 갖는다.

## 품질 손실 — 평균이 최악을 가린다 (표 103~111행 전수)

| 과제 | int4 | fp16 base | 델타 |
|---|---:|---:|---:|
| **AIME 2026** | 86.6 | 92.7 | **-6.1** |
| HumanEval | 90.9 | 95.1 | -4.2 |
| GPQA-Diamond | 79.8 | 81.8 | -2.0 |
| MMLU-Pro | 81.0 | 84.6 | -3.6 |
| **IFBench** | **57.9** | 61.7 | -3.8 |
| **평균** | **79.2** | **83.2** | **-3.9** |

> [!warning] 카드 주장 *"within **3.9 points** of its fp16 base"* 는 **5개 과제 델타의 산술평균**이다(볼트 재계산 확인: 79.24 vs 83.18 = -3.94).
> 🔴 **최악 축 AIME는 -6.1로 평균의 1.6배.** 추론 난도가 높은 과제일수록 4비트 손실이 크다는 방향성이 표에 그대로 있다. 평균 한 숫자만 인용하면 이 방향성이 사라진다.

> [!insight] 🎯 볼트 추가 실측 — **표와 Limitations가 서로를 증명한다** (raw는 둘을 따로 적었다)
> - 표: **IFBench 57.9** — 5개 과제 중 **절대값 최하**. fp16 base조차 61.7로 유일하게 60점대 초반
> - Limitations(139행): *"not yet optimized for agentic tasks — **tool use, multi-step planning**, and long-horizon autonomy are currently **weak**"*
>
> **IFBench는 지시 따르기 벤치이고, 지시 따르기는 툴 사용의 전제다.** 즉 **자인한 약점과 표의 최저점이 같은 능력을 가리킨다.** 카드는 이 둘을 다른 절에 떨어뜨려 놨지만 **같은 사실의 두 표현**이다.
> → **에이전트 용도로는 쓰지 않는다**는 판단이 자인 한 줄이 아니라 **수치로도 뒷받침된다.**

> [!warning] 기타 검증 항목
> - **베이스 ≠ 오리지널**: `base_model: Qwen/Qwen3.5-MoE-35B-A3B`. 사전학습이 아니라 **int4 양자화 + Recover-LoRA + prerouter 어댑터** 조합이다 → [[파생표기-함정]]
> - **자체 측정**: *"All benchmarks were run **by us**"*(OpenCompass)
> - **플랫폼 제약**: MLX 백엔드 → **현재 Apple Silicon 전용**(142행). 다른 백엔드는 예고 상태
> - **`preview` 릴리스** — 안정판 아님

## 도메인별 추출 (local-llm)

- **실용성 판단**: ✅ **조건부 배포 가능.** 단 조건이 셋이다 — **Apple Silicon** · **짧은 컨텍스트** · **비에이전트 용도**. 셋 중 하나라도 어긋나면 카드 수치가 성립하지 않는다.
- **하드웨어/지연**: Mac mini M4 Pro 24GB에서 **decode 14.9–17.7 tok/s · prefill 113/140 · peak 2.9 GiB**.
- **메모리 아키텍처**: 스토리지 상주 전문가 + **prerouter 선예측 프리페치**. RAG도 KV 압축도 아닌 **가중치 계층 오프로드**.
- **트레이드오프**: 평균 **-3.9점**에 35B급을 3 GiB로. 단 **AIME -6.1**, **에이전트 용도 부적합**.
- **오픈소스 구현체**: `edge0` 프레임워크(MLX) + base + `lora_edge0_35b.safetensors` + `prerouter_edge0_35b.safetensors` 동봉.

> [!action] 당장 할 것
> Apple Silicon 환경이 있다면 **짧은 컨텍스트 요약·분류 작업**에 한정해 실측. **툴 호출 파이프라인에는 투입하지 않는다**(IFBench 57.9 + 자인).

## 관련 페이지
- [[MetroLLM-Bench]] — 같은 배치 local-llm. **엣지로 가는 두 경로**: 이쪽은 양자화+오프로드, 저쪽은 PEFT 증류
- [[MiniCPM5-2B-GGUF]] · [[X-AuT]] — 09-12 local-llm 재판정 선례
- [[Alibaba]] — 베이스 Qwen3.5-MoE 제공
- [[한정어-탈락]] · [[파생표기-함정]] · [[단위-불일치]]

## 원본
- 출처: https://huggingface.co/Edge0/Edge0-35B-A3B-preview
- 신뢰도: ⭐⭐⭐ (HF API + safetensors 총계 + 카드 168행 전문 대조 + 평균 재계산 검증)
