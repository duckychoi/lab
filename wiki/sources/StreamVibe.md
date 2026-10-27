---
title: "StreamVibe — 요청 없이 화면만 보고 '다음에 뭘 원하는지' 추론하는 스트리밍 VLM. 모델 +10.7% · 하네스 추가 +12.3%"
type: source
domain: ai-news
tags: [ai-news, hf-paper, streaming-vlm, proactive-agent, user-intent, video-understanding, memory, google]
created: 2026-10-27
updated: 2026-10-27
sources: [https://huggingface.co/papers/2610.34662]
reliability: medium
---

# StreamVibe: Proactive Video Agents for Evolving User Intent

**HF**: https://huggingface.co/papers/2610.34662 · published **2026-10-26** · 소속 표기 **Google**(HF org) · Chengzhi Liu 외 · upvote **154**(수집기 153 · +1)
**코드**: HF 논문 메타에 `githubRepo` **없음**(볼트 확인) · **신뢰도**: ⭐⭐ medium (대형 기관 · 코드 미공개)

> [!insight] 핵심 인사이트 — **"명시적 요청"이 없는 상호작용을 벤치로 만들었다**
> 의도를 3종으로 나눈다: **explicit · implicit**(예: 웹사이트를 보며 *"다음에 어디를 눌러야 하지?"*) · **dynamic**(요청이 계속 바뀜). StreamVibe-Bench: 평가 **4.1K** · 학습 **85K**.
> 결과 3개 중 수집기가 1개만 전했다:
> 1. StreamVibe-VL — 일반 영상 이해 유지 + 응답 타이밍·답변 품질 **+10.7%**
> 2. 🆕 **기존 proactive 모델은 의도 이해·응답 시점 결정이 약하다**(특히 implicit·dynamic)
> 3. 🆕 **StreamVibe-Harness**(의도를 지속 상태로 두는 계층 메모리) → 장시간 상호작용에서 **proactive +12.3%**
> ⇒ 🎯 이 배치의 공통 주제가 여기서도 반복: **모델 개선(+10.7) 위에 하네스 개선(+12.3)이 따로 얹힌다** → [[Trial-by-Trace]] · [[하네스-설계-축]].

> [!warning] 주의
> - ⚖️ +10.7% · +12.3% 는 **"other baselines" 대비 상대치** — 베이스라인 명단·절대값 미기재 → [[비매칭-비교]].
> - ⚖️ 자체 벤치(StreamVibe-Bench)에서 자체 모델 평가 — 규약 ㉒ "자체 벤치" 해당.

## 도메인별 추출 (ai-news · video-saas 접점)
- **video-saas 연결**: 영상 편집 UI 에서 사용자의 다음 행동(클립 선택·자막 수정)을 화면 스트림으로 예측해 먼저 제안하는 기능의 연구 근거. 현재 볼트 영상 파이프라인(reat-*)은 명시적 명령형이라 직접 적용 대상은 아님.
- **6개월 영향력**: "에이전트가 먼저 말 거는" 화면 보조(브라우저·OS 에이전트) 경쟁의 평가 기준이 생겼다.

## 관련 페이지
- [[Google]] · [[에이전트-메모리-레이어]] · [[하네스-설계-축]] · [[비매칭-비교]]
- 같은 배치: [[InteractiveWorld]] · [[Trial-by-Trace]] · [[Trajectory2Gym]]
- [[ai-news]] · [[video-saas]]

## 원본
- https://huggingface.co/papers/2610.34662 · 볼트 HF API 실측(2026-10-27): upvote 154 · githubRepo null
