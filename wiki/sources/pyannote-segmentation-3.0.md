---
title: "pyannote/segmentation-3.0 — 10초 청크 화자 분할 · VAD · 겹침발화 검출 모델"
type: source
domain: ai-news
tags: [ai-news, hf-model, speaker-diarization, vad, overlap-detection, pyannote, baseline-resurfacing]
created: 2026-11-25
updated: 2026-11-25
sources: [https://huggingface.co/pyannote/segmentation-3.0]
reliability: high
---

**모델**: pyannote/segmentation-3.0 · 다운로드 30일 **4,388,795**(볼트 API 11-25 — 수집기 값과 정확 일치) · 누적 409,961,875(일치) · 좋아요 2,881(일치) · trendingScore 42(트렌딩 70위) · HF 내부 ID `650d827e…` · MIT · gated(자동 승인) · 생성 2023-09-22 · 수정 2024-05-10 — 2023년 모델의 트렌딩 재진입([[기준선-재부상]])

## 핵심 인사이트
> [!insight] 30일 439만 다운로드의 정체는 "부품" — 단독으로는 긴 녹음을 못 나눈다
> 16kHz 모노 10초 입력 → 프레임별 7클래스(무음 · 화자 1/2/3 · 두 명 동시 3조합) **"powerset"** 출력. pyannote.audio 3.0 · AISHELL · AliMeeting · AMI · DIHARD · Ego4D · VoxConverse 등 9개 데이터셋 합본 학습. **단독으로는 긴 녹음 전체 화자 분리 불가**(10초 청크만) — 화자 임베딩을 더한 speaker-diarization-3.x 파이프라인의 부품이고, VAD · 겹침발화 검출 파이프라인에 단독 사용 가능. 30일 439만은 파이프라인 의존 다운로드로 보인다. 볼트 [[pyannote-community-1]] · [[pyannote-speaker-diarization]] 의 하위 부품 — [[pyannote]] 축.

> [!note] 카드 한계
> DER 등 성능 수치 없음. 상단에 유료 pyannoteAI 전환 권유.

## 도메인별 추출 (ai-news)
- **즉시 활용**: /down-analysis · /reat-voice 의 화자 분리 체인 내부에서 이미 간접 사용 중일 가능성 — 별도 도입 가치는 **VAD · 겹침 검출 단독 용도** 정도.
- **대체 관계**: [[pyannote-speaker-diarization]] 파이프라인이 이미 이 모델을 내부 사용 — 페이지 분리의 실익은 "부품 단위 재사용" 기록.
- **기준선 재부상 각**: 2023 모델 · 수정 2024-05 이후 정지 상태인데 439만/30일 — 인프라성 모델의 다운로드는 개선이 아니라 파생 파이프라인의 규모를 반영한다([[기준선-재부상]]).
- **액션**: 없음(이미 간접 보유).

## 관련 페이지
- [[pyannote]] · [[pyannote-community-1]] · [[pyannote-speaker-diarization]] · [[기준선-재부상]] · [[ai-news]]

## 원본
- 출처: https://huggingface.co/pyannote/segmentation-3.0
- 확인 범위: HF API 재확인(볼트 11-25 — dl30 · 누적 · 좋아요 · 생성 · 수정 전부 정확 일치) · 모델 카드(수집기 11-25 — gated라 카드 본문 HTML 판독) · 실행 0
- 신뢰도: ⭐⭐⭐ (수치 API 정확 일치 · pyannote 표준 부품)
