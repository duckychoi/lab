---
title: "kimi-k3-in-c — 2.78T 모델을 CPU 단독 C99로 추론"
type: source
domain: local-llm
tags: [local-llm, github, cpu-inference, c99, streaming, kimi, 스토리지병목]
created: 2026-09-09
updated: 2026-09-09
sources: []
reliability: high
---

# kimi-k3-in-c

> [!insight] 핵심 인사이트 — 병목은 RAM이 아니라 **스토리지**다
> 헤드라인은 *"2.78T 모델을 8GB RAM으로"* 지만, README 자신의 요구사항 표가 진짜 조건을 적어 놨다: **저장공간 ~1.7TB**(1.56TB 체크포인트 + 109GB packed trunk, 가급적 빠른 로컬 디스크).
> > *"**The gate is storage: the checkpoint is 1.56 TB.** Everything else is ordinary."*
> → **"8GB로 돌아간다"는 참이지만 "8GB만 있으면 된다"는 거짓이다.** raw가 이 구분을 이미 정확히 달아 놨다(이번 배치에서 **raw가 가장 잘 처리한 항목**).

> [!note] 실측 사다리 (README 표 · 같은 프롬프트, 출력 byte-identical)
> - **8 GB → 26.5 s/token** — 매 스텝 모델 전량을 디스크에서 스트리밍
> - **32 GB → 24.2 s/token**
> - **64 GB → 19.8 s/token**
> - **128 GB+ → 5.6 s/token** — 전부 메모리 상주, 디스크 대기 소멸
> 측정기: 1대, **124코어**, 빠른 NVMe. 실제 데모 캡처는 더 느린 드라이브라 **32.69 s/token**(8토큰 261.5초), **PEAK RSS 8.24GB**.
> → 8GB↔128GB 격차는 **약 4.7배**. 즉 *"메모리는 속도만 산다"* 는 저자 주장은 **표로 뒷받침된다**.

## 도메인별 추출 (local-llm)

- **실용성 판단**: **실배포 NO.** 토큰당 26.5초는 대화 불가. README 자신이 8GB 경로를 *"a **proof-of-life path** for 8 GB-class machines"* 라 부른다 — 저자도 실용이라 주장하지 않는다.
- **메모리 아키텍처**: RAG/KV 압축 계열이 아니라 **디스크 스트리밍 + packed 4-bit + 0.31GB 전문가 캐시**. MoE의 "토큰당 일부 전문가만 활성"을 **디스크 I/O 스케줄링 문제로 재정의**한 것.
- **Hermes 적용**: **불가**(하드웨어·지연 모두). 다만 **아이디어 한 개는 유효** — 상시 상주 대신 *필요한 레이어만 스트리밍*.
- **트레이드오프**: 정확히 **정확도 불변 / 속도 가변**. 8GB와 224GB의 출력이 **byte-identical** — 이게 이 프로젝트의 진짜 기여다. 양자화 품질 논쟁을 회피한다.
- **오픈소스 구현체**: **176KB C99 엔진, BLAS·프레임워크·GPU 전무.** 플랫폼 배지 **Linux x86-64**. v1.0.0에서 토큰당 연산 **약 8× 경량화**, 후속 질문 **3.9× 빠름**, 긴 프롬프트 **약 절반** 비용.

> [!insight] 진짜 가치는 추론이 아니라 **읽기 코드**
> 목차에 *"1. Reading a 1.56 TB checkpoint from its headers"* 가 있다. 초대형 체크포인트를 **헤더만 보고 96 샤드에서 필요한 것만 뽑아 쓰는** 방법이 176KB로 적혀 있는 셈. **모델을 돌리려는 사람보다 포맷을 다루려는 사람에게 더 유용**하다.

> [!warning] 신뢰도 유보
> 벤치마크는 **저자 단일 머신 1대**(124코어·NVMe) 기준이며 제3자 재현 보고를 볼트가 확인하지 않았다. `docs/data/` 에 원자료가 있다고 명시돼 있으나 미검증.

> [!action] 당장 할 것
> 다운로드하지 말 것(**1.7TB**). 대신 README의 **"The memory ladder: 8 GB to 224 GB"** 절과 체크포인트 헤더 파싱 부분만 읽는다. 1.56TB 커밋 전 엔진 일치를 증명하는 **런처블 데모 2종**이 제공된다 — 그것만 돌려 볼 것.

## 관련 페이지
- [[Kimi-K3]]
- [[Moonshot AI]]
- [[airllm]]
- [[ktransformers]]
- [[llms-from-scratch]]

## 원본
- 출처: https://github.com/FareedKhan-dev/kimi-k3-in-c
- 실측(2026-09-09): ⭐7,224 · fork 1,181 · C · Apache-2.0 · created 2026-08-01 · pushed 2026-08-26(14일) · archived=False
- raw 대비 드리프트: **완전 일치**
- 실측 수치: 2.78T params · 1.56TB 체크포인트 · **8.24GB peak RSS(측정)** · 176KB 엔진 · 0 GPU
- 신뢰도: ⭐⭐⭐ (수치 전건 README 원문 대조 완료)
