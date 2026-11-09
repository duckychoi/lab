---
title: "PLatour — 큰 모델이 읽고 작은 모델이 생성하는 잠재 통신(PACT). 이득 일부는 무정보 신호·자기 통신·receiver 단독 학습으로도 재현된다는 자기 반증"
type: source
domain: local-llm
tags: [local-llm, hf-paper, latent-communication, model-collaboration, ablation, kcl, self-refutation]
created: 2026-11-09
updated: 2026-11-09
sources: [https://huggingface.co/papers/2611.06976]
reliability: medium
---

**논문**: [2611.06976](https://huggingface.co/papers/2611.06976) · King's College London · 업보트 15 · 코드 [zhenyi4/platour](https://github.com/zhenyi4/platour) ★10

## 핵심 인사이트
> [!insight] "성능이 올랐다"는 "통신이 일했다"의 증거가 아니다
> 동결된 sender(큰)·receiver(작은)를 **0 초기화 선형 브리지**로 잇고 태스크 보상으로 학습. 오픈 베이스라인·Mostik 보고치를 넘지만, 통제 실험에서 **일부 태스크 이득이 무정보 sender 신호 · 자기 자신과의 통신 · receiver 단독 학습으로 재현**됨 ⇒ 브리지가 sender 정보를 안 쓰고 **파라미터 효율 어댑터**로 작동할 수 있다. 진단 도구 **PACT-Check** 제안.

> [!note] 자기 반증을 초록에 넣은 드문 사례
> 볼트가 반복 지적해 온 "헤드라인 증분의 출처" 문제([[비매칭-비교]] · [[DPDM]] 11-08)를 저자가 스스로 분해했다. 구체 수치는 초록에 없음(수집기 판독 일치).

## 도메인별 추출 (local-llm)
- **실용성**: 큰 모델 prefill + 작은 모델 decode 로 비용 절충 — 로컬 소형 모델 + 원격 대형 모델 하이브리드의 한 형태
- **트레이드오프**: 브리지 학습이 필요 · 이득의 진짜 출처는 PACT-Check 로 따로 재야 함
- **Hermes 적용**: 점검표로 YES — 모델 협업 논문을 볼 때 "receiver 만 학습해도 같은가?" 대조군 확인
- **오픈소스 구현체**: YES(★10)

## 관련 페이지
- [[비매칭-비교]] · [[DPDM]] · [[TwIL-8B]](같은 배치 소형 추론 모델)

## 원본
- 출처: https://huggingface.co/papers/2611.06976
- 확인 범위: HF papers API 초록(볼트 재조회)
- 신뢰도: ⭐⭐
