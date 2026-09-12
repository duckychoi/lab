---
title: m-a-p (Multimodal Art Projection)
type: entity
domain: ai-news
tags: [ai-news, music-generation, open-model, research-collective, license-nc]
created: 2026-09-12
updated: 2026-09-12
sources: [YuE2-3B.md]
reliability: medium
---

# m-a-p (Multimodal Art Projection)

> [!insight] 한 줄
> **오픈 음악 생성 모델 YuE 계열**과 평가 벤치 **WildSongBench** 를 함께 내놓는 연구 집단. 모델과 그 모델을 재는 자를 **같은 곳에서 만든다.**

## 산출물
- **[[YuE2-3B]]** (2026-09-12 인제스트) — ♥271 · 3.63B · **cc-by-nc-4.0** · 기획→시맨틱→합성→디코드 4단계, 편집 가능한 악보 중간 표현. RTX 4090에서 3.58분 곡을 71초에 생성.
- **WildSongBench** (HF 데이터셋) — 192개 프롬프트 음악 생성 벤치. YuE2 카드의 순위표 근거.
- 원 논문 **arXiv 2503.08638**(YuE: 장문 음악 생성).

> [!warning] 🔴 평가 독립성 — 자기 모델을 자기 벤치로 잰다
> [[YuE2-3B]] 의 *"WildSongBench 1위"* 주장은 **m-a-p가 만든 벤치에서 m-a-p 모델이 1위**라는 구조다.
> 이 자체가 부정은 아니다(벤치를 공개했고 프로토콜 차이도 스스로 고지했다). 다만 **[[측정도구-먼저-반증]] 원칙상 제3자 재현 전까지 순위는 자체 보고로 취급**한다.
> 실제로 볼트 실측 결과 카드 헤드라인이 **Suno만 비교 대상으로 지목**하고 **실제 2위 Mureka 9(6.9377, 격차 0.0255)는 표 안에만** 두었다 → [[한정어-탈락]] ④.
> 같은 배치 [[SWE-Bench-Pro-Verified]] 가 실증한 바: **벤치의 신뢰성은 제작자 선언이 아니라 외부 감사로 확인된다.**

> [!warning] 라이선스 정책 — 상업 이용 금지
> YuE2-3B 가중치는 **CC BY-NC 4.0**. 오픈 가중치이나 **수익형 사용 불가.**

> [!question] 미확인
> 조직 형태(학계 랩 / 커뮤니티 / 법인), 소속, 자금 출처 **미조사**. HF 조직 계정과 GitHub(`multimodal-art-projection`)만 확인.

## 관련 페이지
- [[YuE2-3B]]
- [[측정도구-먼저-반증]]
- [[한정어-탈락]]
- [[SWE-Bench-Pro-Verified]]
- [[ai-news]]
