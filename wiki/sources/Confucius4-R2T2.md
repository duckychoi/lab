---
title: "Confucius4-R2T2 — 한 번 낸 글자를 고치지 않는 stable-prefix 스트리밍 ASR. 160ms 에서 5.76% vs 베이스 21.01%, 다만 상용 B 와 full-context 기준에는 못 미친다"
type: source
domain: local-llm
tags: [local-llm, hf-paper, asr, streaming, netease-youdao, qwen3-asr, korean]
created: 2026-11-10
updated: 2026-11-10
sources: [https://huggingface.co/papers/2611.06043]
reliability: medium
---

**논문**: [2611.06043](https://huggingface.co/papers/2611.06043) · Netease Youdao · 업보트 **85**(papers API 2026-11-10 09:06Z · 수집기와 일치) · 코드 [netease-youdao/Confucius4-R2T2](https://github.com/netease-youdao/Confucius4-R2T2) ★875 · 생성 2026-09-08

## 핵심 인사이트
> [!insight] 스트리밍 ASR 의 소비자가 사람에서 기계로 바뀌면 "나중에 고쳐지는 토큰"이 비용이 된다
> 번역기·음성 에이전트는 토큰이 나오는 즉시 행동한다. 논문은 **Longest Stable Prefix(LSP)** 를 정의하고(접두사 순서에 단조 · 전체 오디오 출력과 일치 · 최대성 증명), LSP 라벨로 학습하면 **구조 변경 없이** full-context 모델이 stable-prefix 스트리밍 모델이 된다고 주장한다. Qwen3-ASR-1.7B 의 인코더·프로젝터는 동결, 중·영 1,500시간으로 사후학습(초록 확인).

> [!warning] 헤드라인 5.76% 옆에 놓아야 할 값 3개 (볼트 README 표 직접 대조)
> - README 요약: 160ms · 임시 토큰 1개에서 **5.76%** vs 베이스 동일 설정 21.01%, **full-context 기준 5.15%**(수집기 요약에 없던 값). "오픈소스 평가 대상 중 1위"는 README 자기 서술이다.
> - 표 12열 중 상용 **Comm. B\*** 가 LS-clean 1.25(R2T2 U=1 1.91) · AMI 8.44(10.07) · Wenet-meeting **3.75**(6.74) 로 앞선다. Earnings22 는 AssemblyAI\* 7.47 이 R2T2 7.61 보다 낮다. 단 `*` 는 "보이는 가설을 나중에 고칠 수 있는" 시스템 표시라 **고치지 않는다는 조건이 다르다** — [[비매칭-비교]] 의 역방향(R2T2 에 불리한 쪽 조건 차이).
> - 사후학습에 없던 10개 언어 18세트 매크로 평균: R2T2 U=1 **8.40** · U=0 9.60 · Base 160ms 30.75 · Base offline **5.99**. **한국어 FLEURS CER: U=0 6.77 · U=1 7.52 · Base offline 4.22** — 한국어는 U=0 이 더 좋고, 오프라인 대비 격차는 영·중보다 크다. 수집기 판독 전건 일치.

> [!note] 수집기 보완 1건
> 수집기는 라이선스를 "NOASSERTION"으로만 적었다. README License 절: **코드 Apache-2.0 · 가중치는 NetEase Model Use License Agreement**(별도 파일). 상업 이용 전 가중치 라이선스 확인 필요. 지연 수치는 서빙·네트워크·렌더링 시간 제외(README 37 · 131행).

## 도메인별 추출 (local-llm)
- **실용성**: 1.7B · 청크 80ms~2s · `U` 로 정확도-지연 절충. 실시간 자막/통역에서 "고쳐 쓰기 없는" 출력이 필요할 때.
- **트레이드오프**: 안정성의 값 = full-context 대비 +0.61%p(5.76 vs 5.15, 영·중 13세트 README 요약).
- **Hermes 적용**: 보류 — 텔레그램 봇은 음성 스트림 입력이 없다. 영상 자막 파이프라인 쪽 후보.
- **오픈소스 구현체**: YES — 코드 + 가중치 공개.

## 관련 페이지
- [[Nemotron-3.5-Transcribe-30B-A4B]] · [[VibeVoice-ASR-Streaming-7B]] · [[FunASR]] · [[openai-whisper]] · [[비매칭-비교]] · [[표-부분인용]]

## 원본
- 출처: https://huggingface.co/papers/2611.06043
- 확인 범위: HF papers API 초록 전문 + GitHub README(30,187B) 정확도 표 · 교차언어 표 · License 절 · 🔴 논문 PDF · 지연 그림 · 추론 실행 없음
- 신뢰도: ⭐⭐ (업보트 85 · ★875 · 자체 측정)
