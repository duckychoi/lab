---
title: Video-Oasis — 영상 이해 평가를 다시 생각하다
type: source
domain: ai-news
tags: [ai-news, huggingface, paper, video-understanding, benchmark, naver, evaluation]
created: 2026-07-10
updated: 2026-07-10
sources: []
reliability: medium
---

# HF논문: Rethinking Evaluation of Video Understanding (Video-Oasis, arXiv 2603.29616)

**HuggingFace**: https://huggingface.co/papers/2603.29616
**기관**: 세종대(Sejong U) + [[NAVER]] Cloud (Sungjune Park·Jaeyun Lee·Inwoong Lee·Taeoh Kim·Dongyoon Wee·Minho Shim·Yukyung Choi)

> [!insight] 핵심 인사이트
> **기존 영상 이해 벤치마크의 절반 이상이 "영상을 보지 않고도" 풀린다는 것을 실증한 진단 스위트.** WebFetch로 초록 실측: 3개 진단 축으로 벤치를 감사 — ①**시각 의존성**(Blind/Audio/Summary), ②**시간 의존성**(Center-Frame/Frame Shuffling/Bag-of-Frames), ③사람 개입 모호성 검증. 충격적 수치: **14개 데이터셋의 55% 샘플이 시각 입력·시간 맥락 없이 풀림**. shortcut 취약 문항을 걸러내자 SOTA 모델도 랜덤(25.6%)보다 겨우 조금 높은 수준으로 추락. 진짜 영상 이해에 필요한 5개 도전 범주(정밀 지각·공간 세계 이해·시간 동역학·인과 추론·전역 서사)를 증류. 이것은 [[Beyond-Static-Leaderboards]]의 영상판 — **"벤치 점수 높음 ≠ 영상 이해"**를 정량화. 내 [[down-analysis]]·[[claude-video]] 평가에 "이 분석이 영상을 실제로 봤는가, 자막·요약만 봤는가"를 검증하는 축을 준다.

## 도메인별 추출 (ai-news / video-saas 교차)

- **신뢰도**: ⭐⭐⭐ (arXiv 2603.29616 초록 WebFetch 검증 — 55%·25.6%·3진단축·5범주 확인. 재현 미실측 → medium)
- **즉시 활용**: 간접 — 평가 프레임워크. [[down-analysis]] 결과가 "프레임을 실제로 봤는지 vs 자막만으로 답했는지" 자가검증하는 체크리스트로 이식.
- **6개월 영향력**: 비디오 LLM 벤치가 "시각·시간 의존성 필터링"을 표준 전처리로 채택하는 방향. [[Light-Omni]]의 "무겁게 볼 구간만 고른다"와 대조적 보완(무엇을 볼지 vs 봤는지 검증).
- **대체 관계**: VideoMME 등 기존 벤치를 대체가 아닌 **감사(audit)** — 기존 벤치 위에 얹는 신뢰성 레이어.
- **허와 실**: "55%가 시각 없이 풀림"은 초록 명시 강력 수치. 단 14개 데이터셋 범위·필터 기준의 일반화는 원문 재현 필요.
- **액션**: down-analysis에 "Blind 테스트"(자막·요약만으로 같은 답 나오면 시각분석 미흡) 자가검증 스텝 추가 검토.

## 관련 페이지
- [[Compositional-Action-Shortcuts]] — 같은 [[NAVER]] 팀, "객체 지름길" 완화(쌍 논문)
- [[Beyond-Static-Leaderboards]] — 정적 리더보드 타당성 한계(영상판 대응)
- [[Video-MME-Logical]] — 영상 시간·논리 추론 벤치
- [[down-analysis]] · [[claude-video]] — 영상 이해 스킬(검증 축 이식)
- [[NAVER]] — 제작 기관
- [[ai-news]]

## 원본
- 출처: https://huggingface.co/papers/2603.29616
- arXiv: 2603.29616, Video-Oasis (세종대 + NAVER Cloud)
- 성과: 14데이터셋 55% 시각/시간 무관 풀림 / 필터 후 SOTA≈랜덤(25.6%) / 5 영상 네이티브 범주
- 신뢰도: ⭐⭐⭐ (초록 원문 검증 / 재현 미실측)
