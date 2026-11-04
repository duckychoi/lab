---
title: "JustVugg/colibri — 744B~2.8T MoE를 순수 C로 소비자 하드웨어에서 돌리는 추론 엔진"
type: source
domain: local-llm
tags: [local-llm, github-trending, moe, inference-engine, c, expert-streaming, nvme, on-device]
created: 2026-09-11
updated: 2026-11-04
sources: []
reliability: high
---

# colibri

> [!update] 2026-09-14 갱신 — ⭐**30,734**(3일 **+3,117 · +11.3%**) · 🔴 **raw가 중복을 못 잡고 재배달**
> **GitHub API 실호출(2026-09-14)**: ⭐**30,734**(raw 30,707 대비 **+27 드리프트**) · fork **3,305**(09-11 3,018 → **+287**) · 이슈 **127**(raw 일치) · **Apache-2.0**(일치) · C · created 2026-07-01 · **pushed 2026-09-14 = 당일 푸시, 활발**
> 🔴 **이 항목은 신규가 아니다.** 이 페이지는 **2026-09-11에 이미 생성**됐는데 raw가 *"볼트 미보유"* 로 판정해 재배달했다. 원인 분석 → [[백필-우회]]
> 📈 **모델 패밀리 8개 → 9개**(09-11 기록 대비 +1). raw 실사: GLM-5.2/5.3 **744B** · Kimi K3 **2.8T** · [[DeepSeek-V4.1-Flash]] **552B** · Qwen3.8-Flash-Next 125B 등.
> 🔴 **raw가 새로 가져온 한정어 — 09-11 페이지에 없던 것이라 채택한다**: 대시보드의 *"744B · 4 tok/s · TTFT 1.6s · disk 0"* 은 **`6× RTX 5090` 에 전문가를 전부 상주시킨 조건**이며 **디스크 스트리밍 구성의 수치가 아니다.** 같은 README가 MTP 투기실행이 **전문가 적중률 85% 부근에서 32% 손실**을 낸다고 자기 반증한다.
> 🎯 **09-11에 이 페이지가 세운 판정이 3일 뒤에도 유지된다** — *"빠르다를 팔지 않고 조용히 바꾸지 않는다를 판다"*. 위 한정어는 그 판정의 **추가 증거**다. 속도 수치에 조건을 붙이는 것과 SLA 없음을 선언하는 것은 같은 태도다. → [[자기제한-명시]]
> 설계 근거: 744B MoE는 토큰당 **~40B 활성 · 그중 ~11B만 교체**된다는 것 — 스트리밍이 성립하는 이유.

> [!insight] 핵심 인사이트
> **VRAM·RAM·NVMe를 단일 메모리 계층으로 취급하고, MoE 전문가(expert)를 디스크에서 스트리밍**해 744B~2.8T 모델을 소비자 하드웨어에서 돌린다. 순수 C·의존성 0.
> 그런데 이 저장소의 진짜 판정 포인트는 성능이 아니다 — **저자가 "속도에는 SLA가 없다"고 먼저 선언**하고, 대신 **의미론(semantics)에만 하드 개런티를 건다**.
> README 35~38행 원문: *"there is **no SLA on speed, and a hard guarantee on semantics**: ... [no experiment] **silently changes model precision or router semantics**"*
> → **"빠르다"를 팔지 않고 "조용히 바꾸지 않는다"를 판다.** [[자기제한-명시]] 계보의 가장 선명한 사례.

> [!warning] "돌아간다" ≠ "쓸 만하다" — 저자 실측 4구간
> README 322~327행 원문 수치. **같은 엔진인데 하드웨어에 따라 100배 이상 벌어진다**:
> - **6× RTX 5090 풀 레지던시**: 5.8~6.8 tok/s 디코드, TTFT **~13초**
> - **128GB CPU 전용 데스크톱**: ~1.8 tok/s (warm)
> - **RTX 5070 Ti 랩탑급 1대**: 1.07 tok/s
> - **25GB 개발 박스**: **0.05~0.1 tok/s (콜드)** — 저자가 *"the proven floor"* 라 부르는 하한
> → 최상단(6×5090 ≈ 2천만원+)에서도 **6.8 tok/s에 TTFT 13초**다. **"소비자 하드웨어에서 744B가 돌아간다"는 참이지만, 대화형으로 쓸 수 있다는 뜻은 아니다.**
> → 대시보드 캡션(54행)의 *"744B at **4 tok/s, TTFT 1.6s, disk 0**"* 는 **디스크 접근이 0인 풀 레지던시 조건**이다. 이 수치만 인용하면 안 된다.

> [!note] 구조 — 병목은 연산이 아니라 전문가 캐시 적중률
> README 561행: *"...touches 301 of them, so the **expert cache hit rate is what sets tok/s**"*
> → MoE 추론에서 **토큰당 활성 전문가는 일부**이므로, 문제는 FLOPs가 아니라 **어느 전문가가 어느 계층에 있느냐**다. colibri는 이걸 스케줄링 문제로 재정의했다.
> - GLM-5.2(744B) int4 기준: **상주 9.9GB / 디스크 ~370GB**
> - 미러 SSD는 **시작 시 검증**(파일 크기 + safetensors 헤더가 바이트 단위 동일해야 함), 불일치 파일은 조용히 주 디스크로 폴백 → **부분 미러도 유효**(231행)
> - CUDA VRAM 전문가 계층 실측: **1.44 → 10.05 tok/s (7.0배)**, 8GB 카드 2장, **출력이 CPU 경로와 비트 단위 동일**(414·437행)
> → 마지막 항목이 중요하다. **가속을 붙여도 출력이 바뀌지 않음을 비트 동일성으로 증명**한다 = 위의 "의미론 개런티"를 실제로 검증 가능한 형태로 내놨다.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **조건부.** 배치·비대화형 워크로드(야간 일괄 요약·대량 분류)에는 **지금 쓸 수 있다**. 대화형은 불가 — 최상급 구성에서도 TTFT 13초. 내 환경(단일 소비자 GPU)이면 **1 tok/s 내외**를 각오해야 한다.
- **메모리 아키텍처**: **디스크를 메모리 계층에 편입**하는 방식. RAG/KV압축과 다른 축 — 모델 가중치 자체를 스트리밍한다. [[DeepSeek-V4.1-Flash]] 가 **KV 캐시**를 줄인 것과 대비되는 짝: 저쪽은 컨텍스트 비용, 이쪽은 **가중치 상주 비용**을 공격한다.
- **Hermes 적용**: **직접 적용은 부적합**(지연). 다만 *"양자화가 라우터 시맨틱을 조용히 바꾸지 않는다"* 는 검증 방식은 이식 가능 — 내가 쓰는 양자화 모델이 **비트 동일성 테스트를 통과하는지** 확인하는 습관.
- **트레이드오프**: **속도 ↔ 모델 크기**를 정면으로 교환한다. 744B를 1 tok/s로 돌지, 27B를 60 tok/s로 돌지의 선택. **"큰 모델이 느리게"가 "작은 모델이 빠르게"보다 나은 과제**가 무엇인지는 사용자가 판단해야 하며, 저자는 그 판단을 대신해주지 않는다.
- **오픈소스 구현체**: ⭐**27,617**(당일 +98) · fork 3,018 · **Apache-2.0** · C · 2026-07-01 개설 · 8개 모델 패밀리를 **각각 단일 C 파일**로 지원.

> [!action] 당장 할 것
> **속도를 재지 말고 개런티를 재라.** 내 하드웨어에서 tok/s를 재는 건 위 4구간으로 이미 예측된다(느리다). 대신 **CUDA 전문가 계층 on/off 출력이 비트 동일한지** 확인하는 것이 이 저장소에서 배울 값. 통과하면 **"가속은 출력을 바꾸지 않는다"를 검증한 첫 로컬 스택**이 된다.

> [!question] 미해결 질문
> `--ram` 설정과 전문가 캐시 적중률의 관계가 README에 정성적으로만 있다. **적중률 x%일 때 tok/s가 얼마인가**의 곡선이 없어서, 내 하드웨어에서의 성능을 **사전에 계산할 수 없다**. 결국 직접 돌려봐야 안다.

## 관련 페이지
- [[자기제한-명시]]
- [[DeepSeek-V4.1-Flash]]
- [[에이전트축-분기]]
- [[측정도구-먼저-반증]]
- [[Zhipu AI]]

## 원본
- 출처: https://github.com/JustVugg/colibri
- 실측(2026-09-11): ⭐**27,617**(raw 27,613→27,614, 드리프트 +3~4) · fork **3,018**(일치) · **Apache-2.0**(일치) · C · created 2026-07-01 · pushed 2026-09-11
- **README 원문 대조**: 35~38행 "no SLA on speed / hard guarantee on semantics" **원문 확인** · 322~327행 4구간 수치 **전건 확인** · 414·437행 "bit-identical to CPU" **확인** · 561행 전문가 캐시 적중률 **확인**
- raw 대비: **수치 일치, 인용 정확.** 볼트 추가 발견 = **비트 동일성 검증**(raw 미기재) · **대시보드 4 tok/s는 disk 0 조건**임(단독 인용 위험)
- 신뢰도: ⭐⭐⭐ (성능 주장을 스스로 제한 · 실측 구간을 하한까지 공개 · 검증 가능한 개런티 형태)

## 🔄 2026-11-04 갱신 (인제스트 2026-11-04) — ★47,469 · **v2.0.0·v2.1.0(GGUF 네이티브·Mistral-Large-4 1T) · 🔴 볼트가 놓친 보안 권고 8건(08-05) · 볼트 핵심 인용구 "no SLA on speed"·"bit-identical"은 현 README에서 사라짐**

**GitHub API 실측(11-04 09시대)**: ★**47,469**(수집기와 완전일치) · fork **5,483** · open_issues **170** · watchers 380 · Apache-2.0 ✅ · C · 소유 `JustVugg`(User) · pushed 2026-11-04T07:43Z · 릴리스(최신 5) **v2.1.0(10-31)** · v2.0.0(10-06) · v1.12.1(09-24) · v1.12.0(09-20) · v1.11.0(09-13)
- 📈 볼트 직전 ★30,734 · fork 3,305 · 이슈 127(09-14) → **★ +16,735(+54.5%) · fork +2,178 · open +43 / 51일 · 릴리스 +4**(v1.12.0~v2.1.0; v1.11.0은 09-13 발행인데 09-14 갱신이 기록하지 않았다). 이 페이지는 **51일 미갱신**이었다 → [[캐시된-지표-신선도]].
- 🔴 볼트 정정: 프론트매터 `updated` 가 09-14 갱신 후에도 **09-11로 남아 있었다** → 이번에 11-04로 교체.

> [!warning] 🔴 볼트 과거 누락 — 공개 보안 권고 8건이 페이지 생성(09-11) **이전**에 이미 있었다
> `api.github.com/repos/JustVugg/colibri/security-advisories` 실측: **8건 전부 2026-08-05 공개**(high 6 · medium 2). 예: 조작된 safetensors로 **스택 버퍼 오버플로(RSP 제어)**(GHSA-pmq2-6f2p-hjvf) · safetensors 로더 **힙 OOB 쓰기**(GHSA-4gw4-j89j-4c8r) · 신뢰할 수 없는 모델 파일 → tok.h/st.h/json.h 힙 손상(GHSA-wc4x-3786-cxh7) · NaN 라우터 로짓 → 음수 인덱스 힙 OOB(GHSA-5xpg-vw35-2687) · SERVE 프로토콜 음수 `max_tok` → KV 캐시 힙 OOB 쓰기 · **`/profile` 무인증 텔레메트리 노출**(medium) · slowloris DoS(medium).
> - v2.0.0 노트 "Correctness and security": *"the published advisory fixes **carried to glm53, qwen36 and deepseek_v41**"* + #1930 모델 디렉터리 내 심링크로 엔진 쓰기 경로를 돌리는 공격 차단. 노트 문구상 이 엔진들엔 10-06 전까지 같은 수정이 없었다(⚖️ 문구 해석, 코드 미확인).
> ⇒ 볼트 09-11 판정 *"의미론 하드 개런티 = 신뢰 근거"* 는 **수치 의미론**에 대한 것이었고, **"남이 올린 GGUF/safetensors를 연다 = 공격면"** 은 다루지 않았다. v2.1.0의 GGUF 네이티브 실행으로 이 공격면은 더 넓어졌다(임의 커뮤니티 GGUF를 변환 없이 읽음).

**헤드라인 수치 — README(raw 893행) 원문 대조 · 하드웨어·양자화·설정 병기**

| 수치(수집기) | README 원문 조건 | 판정 |
|---|---|---|
| Qwen3.6-35B-A3B **6.0** CPU / **9.9** Vulkan iGPU (머신 A) | 머신 A = Ryzen 7 PRO 8700GE 8코어·61–64GB DDR5·NVMe·Radeon 780M(266~267행). 9.9 = **"Vulkan, expert tier + dense chain"**, 6.0 = CPU, 중간값 8.0 = tier만. **각 실행 전 page cache 비움·100토큰 디코드**(306~312행). 양자화: 이 행엔 미표기(다운로드 23GB, 208행) | ✅ 수치 일치 · 설정 누락 |
| **30.0** CUDA (머신 C) | 머신 C = **RTX 3070 8GB + Threadripper 3945WX**, dense·DeltaNet 층을 카드에(**per-row int4 container**, 269~270행). 30.0은 **opt-in `Q36_DN_GPU=1`** 적용값이고 범위는 **25.4→30.0**(392~396행) | 🟡 상한만 인용 |
| GLM-5.2(744B) **0.05–0.1 / 1.83 / 9.0–9.2** | 동일 **int4 container**(594행; HF `GLM-5.2-colibri-int4-g64-with-int8-mtp` 429GB, 681행). 0.05–0.1 = 25GB 노트북 **콜드**("the honest floor") · 1.83 = Ryzen AI Max+ 395 128GB **CPU only, warm** · 6×RTX 5090 **전 전문가 상주: 5.8–6.8, "9.0–9.2 with selective NUMA interleave"**(597~598행) | 🔴 **9.0–9.2는 NUMA 인터리브 조건값** — 수집기가 한정어 탈락. 볼트 09-11의 5.8–6.8이 기본값으로 여전히 README에 있다 |
| Mistral-Large-4 UD-IQ1_S **1.34–1.36** CUDA (머신 D) | 머신 D = i5-13500·62GB·**RTX PRO 4000 Blackwell SFF 24GB(70W)**·NVMe 2개 md 어레이(271~272행). 233GB GGUF, 카드·RAM에 없는 건 NVMe에서. prompt **"240 tokens in 66–82 s"**, Vulkan 1.16–1.17(250·634행) | ✅ 일치 · 프롬프트 지연(66–82초) 누락 |

- ⚠️ README가 스스로 붙인 측정 정의: *"Measured is what was timed on the machine named, decode speed for the chat models … A blank means nobody has measured it yet"*(200~202행). 머신 D 표는 `coli serve` · 450토큰 프롬프트 후 128토큰 스트리밍 · HTTP 포함 · **2회 중 좋은 값**(608~610행) — 즉 **best-of-2**다.
- 📝 v2.1.0 노트 추가 수치(같은 머신 D): Qwen3.6-35B-A3B UD-Q4_K_M CUDA 디코드 104.8 · MTP(`Q36_MTP=1`) 99.7–104.5→115.8–120.1 · Qwen3.8-Flash-Next 262K 컨텍스트 디코드 9.6→45.7 · Hermes Agent 한 턴 86s→4.9s(대화 parking). Kimi K3 UD-IQ1_S(594GB) **0.349 tok/s**.

> [!warning] 🔴 볼트 핵심 인용구의 출처가 바뀌었다 (09-11 본문 정정 표기)
> - 09-11 인용 *"there is **no SLA on speed, and a hard guarantee on semantics**"*(당시 35~38행) → 현 README **0건**(grep `SLA`). 대응 문장은 181~184행 *"the default policy never silently changes model precision or router semantics. Less fast memory may cost speed; it must not quietly redefine the model."* — **개런티 내용은 유지, "SLA 없음" 선언 문구는 삭제.**
> - 09-11 인용 *"bit-identical to CPU"*(당시 414·437행) → 현 README **0건**(grep `identical`). 품질은 *"Quality is measured, not assumed"* 로 docs/benchmarks.md에 넘김(652~655행, 미열람).
> - 09-11 *"6×5090 TTFT ~13초"* → 현 README **0건**(grep `TTFT`).
> - MTP **"85% 적중에서 32% 손실"** 자기 반증은 731행 연구 과제 표에 **남아 있다** ✅.
> ⇒ 09-11 본문·[[자기제한-명시]] 의 colibri 인용은 **"2026-09 README 기준"** 으로 읽는다. 태도(조건 병기·하한 공개)는 현 README에도 유지된다.

> [!insight] 조건 병기는 늘었고, 한정어 탈락은 수집 단계에서 생긴다
> 현 README는 수치마다 머신 문자(A~D)·컨테이너·opt-in 플래그·cold/warm·best-of-2를 붙인다. 수집기가 틀린 곳은 README가 아니라 **요약 과정**이다(NUMA 인터리브·`Q36_DN_GPU=1`·프롬프트 66–82초 탈락) → [[한정어-탈락]]. 1T급 실용 판정은 09-11과 같다: **디코드 1~2 tok/s대 + 프롬프트 수십 초 = 배치·검증용**. 새로 달라진 건 **35B-A3B급은 24GB 카드에서 100 tok/s대**라는 점 — colibri가 "초대형 전용"에서 **일반 MoE 런타임**으로 넓어졌다.

- **수집기 평가**: ★ 완전일치 · 머신 A·C·D 사양 정확 · v2.1.0 요약 정확. 오류/누락 = ① **GLM-5.2 9.0–9.2의 "selective NUMA interleave" 조건 탈락** ② 30.0의 opt-in 플래그·25.4 하단 탈락 ③ 양자화 미기재(GLM int4-g64, 35B는 README 행에 미표기) ④ 보안 권고 8건·v2.0.0 보안 절 언급 0 ⑤ v2.0.0(10-06) 누락.
- **Hermes 적용**: 24GB급 카드가 있으면 Qwen3.6-35B-A3B GGUF를 변환 없이 `coli import` → `coli serve` 로 OpenAI 호환 서빙 가능(문서 기준, 미실행). 단 **출처 불명 GGUF는 열지 말 것**(위 권고 계열).
