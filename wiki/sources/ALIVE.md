---
title: "ALIVE — 스트리밍 비디오 LLM 에 능동 알림 · 다중 작업 · 되묻기를 넣는다 (Tsinghua · 초록 수치 0)"
type: source
domain: video-saas
tags: [video-saas, paper, streaming-video, video-llm, proactive, rl, benchmark]
created: 2026-11-22
updated: 2026-11-22
sources: [https://huggingface.co/papers/2611.21366]
reliability: medium
---

**논문**: arXiv 2611.21366 · 업보트 40(볼트 · 수집기 일치) · Tsinghua · 저자 16 · 코드 [lijinzhao30/ALIVE](https://github.com/lijinzhao30/ALIVE) ★40

## 핵심 인사이트
> [!insight] 영상 모델의 과제가 "무엇을 답할까"에서 "언제 말하고 언제 침묵할까"로
> 스트리밍 비디오 LLM 이 요청을 개별 처리하는 한계를 겨냥: 능동 모니터링(조건 발생 시 먼저 알림), 스트리밍 중 다중 작업 조율, 정보 부족 시 되묻는 feedback-seeking. ALIVE-SFT-288K · ALIVE-RL-3K 로 2단계 학습 — 대조 SFT 로 "언제 · 어떻게 응답할지", RL(BACA: 궤적 단위 + 국소 advantage 결합)로 응답 · 침묵 결정을 다듬는다. 피드백 탐색 평가용 FSI-Bench 신설.

> [!warning] 수치 없음
> 공개 벤치 4종 + FSI-Bench 에서 "비교 모델 중 종합 최고"라고만 한다. 초록에 수치 · 베이스 모델 크기 없음(볼트 `%` 검색 0건). FSI-Bench 는 저자가 만든 벤치다([[분포내-우위]] 주의).

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 라이브 방송 · 촬영 모니터링에서 "이 장면이 나오면 알려 줘"형 기능의 연구 기반. 편집 SaaS 의 실시간 어시스턴트로 이어질 수 있다.
- **크리에이터 인사이트**: 되묻기(feedback-seeking)는 생성 SaaS 의 프롬프트 보완 대화와 같은 문제 — 정보가 부족할 때 추측 대신 질문.
- **경쟁 우위 빈틈**: 지연 · 프레임 처리율이 초록에 없다 — 실시간성 미확인.

## 관련 페이지
- [[WeMM-Video]] · [[Qwen3.5-Omni]] · [[분포내-우위]] · [[video-saas]]

## 원본
- 출처: https://huggingface.co/papers/2611.21366
- 확인 범위: HF papers API(초록 전문 · 업보트 · 조직 · githubRepo) · 🔴 본문 표 미열람
- 신뢰도: ⭐⭐⭐
