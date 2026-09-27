---
title: Xiaomi — 로봇(신체)과 LLM·RL 인프라(두뇌) 양쪽에 투자하는 중국 제조사
type: entity
domain: ai-news
tags: [ai-news, local-llm, slam-3dgs, xiaomi, mimo, robotics, agentic-rl]
created: 2026-09-27
updated: 2026-09-27
sources: [MiMo-V2.6-Pro-RL.md, MiMo-V2.6-RL-Livestream.md, Xiaomi-Robotics-VLA-Scaling.md, Xiaomi-Robotics-U0.md]
reliability: medium
---

# Xiaomi

> [!insight] 🎯 볼트 커버리지가 두 축으로 갈린다 — 같은 회사가 신체와 두뇌 양쪽에 있다
> 볼트가 09-18에 관찰한 구조가 오늘 강화됐다:
> - **두뇌(LLM·RL)**: [[MiMo-V2.6-Pro-RL]](오늘 · **1.024조 파라미터 · MIT**) · [[MiMo-V2.6-RL-Livestream]](09-18 · 훈련 생중계)
> - **신체(로보틱스)**: [[Xiaomi-Robotics-VLA-Scaling]] · [[Xiaomi-Robotics-U0]]
> 🎯 **오늘 이 두 축이 처음으로 교차 검증됐다** — 09-18 사용자 소스의 *"1조 파라미터"* 주장이 오늘 `safetensors.total` **1,024,216,603,392** 로 **실측 확정**됐다. 즉 볼트는 **같은 조직의 주장을 9일 간격으로 추적해 확정한 첫 사례**를 갖게 됐다.

> [!note] 확인된 사실
> - **MiMo 팀 공식 사이트 `mimo.xiaomi.com` 실존**(볼트 09-18 직접 fetch). V2.5 라인업 + **agentic RL 중심 논문 목록**(ARL-Tangram · MoE RL 라우터 정렬).
> - **훈련 중 RL 메트릭을 라이브 대시보드로 공개** — 볼트 관측 범위에서 메이저 랩 최초급 → [[검사가능성-공사]] 의 산업 적용.
> - **스텝당 1,568 프롬프트 × 16 롤아웃** — 09-18 2차 보도 → 오늘 **모델카드 1차 출처 확보.**
> - 공개 성향이 강하다: **MiMo-V2.6-Pro-RL 이 MIT** 이고 학습 방법(YORO·비동기 GRPO·GRS·GAR)을 카드에 서술한다.
> - 루푸리(샤오미 LLM 총괄) 홍보 · HuggingFace 공동창업자 Thomas Wolf 호평 · HN 토론 존재.

> [!warning] 🔴 미확인
> - **"스텝당 약 20억 토큰"** — 09-18 이래 여전히 미검증. 볼트 산술 추정(25,088 시퀀스 → 시퀀스당 ~79,700 토큰)은 **자릿수가 그럴듯하나 측정이 아니다.**
> - 성능 수치 **전건 벤더 자기보고** · 자사 명칭 벤치 3개 혼재 · 경쟁 열 `-` 2건.
> - ⬜ 회사 전체 AI 조직 구조·투자 규모 미조사.

## 관련 페이지
- [[MiMo-V2.6-Pro-RL]] · [[MiMo-V2.6-RL-Livestream]] — LLM·RL 축
- [[Xiaomi-Robotics-VLA-Scaling]] · [[Xiaomi-Robotics-U0]] — 로보틱스 축
- [[검사가능성-공사]] — 훈련 생중계의 이론축
- [[하네스형-에이전틱-RL]] — YORO 의 하니스 전이 주장
- [[분포내-우위]] · [[비매칭-비교]] — 자사 벤치 문제

## 원본
- 출처: https://huggingface.co/XiaomiMiMo · https://mimo.xiaomi.com
- 신뢰도: ⭐⭐ (**소스 4건 누적 · 1조 파라미터 실측 확정 · MIT 공개**로 근거가 축적됐다. 단 성능 주장은 전부 자기보고)
