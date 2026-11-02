---
title: "Wizard — 스켈레톤·지오메트리 프록시와 에이전트 상태관리로 만든 실시간 게임 월드모델"
type: source
domain: ai-news
tags: [ai-news, world-model, game, video-generation, agentic, real-time, video-saas]
created: 2026-11-02
updated: 2026-11-02
sources: [https://huggingface.co/papers/2610.40339]
reliability: low
---

**HF**: published 2026-10-29 · upvote 22 · Tencent · NUS · NTU (Yuzhe Wu · Zijun Lin · Yeying Jin) · arXiv 2610.40339 · 코드 **없음** (HF `githubRepo` null) · 프로젝트 페이지 wyzardwu.github.io/wizard (200 OK, 레포 링크 없음)

## 핵심 인사이트
> [!insight] 게임 로직은 에이전트가, 화면은 영상 모델이 맡는다
> 에이전트가 게임 상태(HP, 사망 판정 등)와 3D 장면 지오메트리를 명시적으로 유지한다. 캐릭터 동작은 모션 라이브러리에서 검색해 대상 스켈레톤에 리타깃한다. 이것을 OpenGL로 "시각 프록시"(R=높이, G=캐릭터 슬롯+방향)로 렌더링하고, 영상 모델은 그 프록시를 따라 그린다. 규칙의 일관성이 생성 모델이 아니라 **명시 상태**에서 나온다는 점이 [[Matrix-Game-3.0]] 계열의 행동 조건부 모델과 갈리는 지점이다.

> [!warning] 정량 평가가 0건이다
> 실험 절(5장)은 **그림 5·6의 정성 예시뿐**이다. 기준선 비교, 수치 지표, 사용자 연구가 전혀 없다. "zero-shot 일반화", "precise control", "mechanically consistent"는 **측정되지 않은 주장**이다. 초록과 제목의 "Manipulate **Any** World"도 마찬가지다. 저자가 밝힌 한계는 ① 모션 라이브러리 의존 탓에 특이한 체형 캐릭터에는 맞는 동작을 찾기 어렵다 ② 롤아웃이 길어지면 프록시와 영상의 일관성이 떨어진다. "임의 동작"은 실제로는 **라이브러리에 있는 동작**이다.

> [!warning] 수치의 출처
> - 750 장면 · 178 캐릭터는 **학습 데이터 규모**다. 50.3시간 = Elden Ring 녹화 8.8h + 절차적 합성 11.6h + Unreal 3.3h + WildWorld 26.6h이고, 클립은 44,075개다. 평가 규모가 아니다.
> - "실시간"은 **24 FPS · 2 디노이징 스텝** 값이다(Wan2.2-TI2V-5B, [[causal-forcing-plus-plus]] 방식 3단계 증류). **GPU 기종은 본문에 없다.** 세션 전 초기화(장면 재구성 + 리깅)에 최대 5분이 든다.
> - 데이터 라이선스: WildWorld는 비상업 연구 라이선스이고, Elden Ring 영상은 "연구 목적으로만" 쓴다고 적었다. 상업적으로 재사용할 수 없다.

## 도메인별 추출 (ai-news)
- **신뢰도**: 논문만 있다 · upvote 22 · 코드·가중치 없음 · 정량 평가 0 → 낮음.
- **즉시 활용**: NO. 공개된 구현체가 없다.
- **6개월 영향력**: "LLM 에이전트 = 게임 엔진 상태, 영상 모델 = 렌더러" 분업 패턴의 사례다. 구조적 프록시(스켈레톤·깊이)를 조건으로 쓰는 방식은 video-saas 쪽 캐릭터 일관성 제어에 참고할 수 있다.
- **대체 관계**: 행동 조건부 월드모델(키보드·마우스 입력)을 명시 상태 + 프록시 렌더링으로 대체하자는 제안이다.
- **허와 실**: 실제 기여는 데이터 구축(4개 소스 → 통합 프록시 인코딩)과 프록시 조건 + 캐릭터별 적응형 마스킹 설계다. "실시간·일반화·정밀 제어"는 그림 예시로만 뒷받침된다.
- **액션**: 코드 공개 여부만 관찰한다.

## 관련 페이지
- [[월드모델]] · [[Diffusion-월드모델]] · [[AI-영상-생성-2026]] · [[causal-forcing-plus-plus]] · [[Matrix-Game-3.0]] · [[L3G-World]]
- [[한정어-탈락]] ("Any World" ↔ 라이브러리 동작) · [[자기제한-명시]]

## 원본
- 출처: https://huggingface.co/papers/2610.40339
- 확인 범위: HF `api/papers` · arXiv HTML 본문 전체(1~6장) · 프로젝트 페이지 HTTP 200 확인(레포 링크 없음) · 🔴 GPU 기종과 24 FPS 측정 조건은 본문에 없어 미확인 · 영상 결과물 시청 0회
- 신뢰도: ⭐ (Tencent · 코드 없음 · 정량 평가 없음)
