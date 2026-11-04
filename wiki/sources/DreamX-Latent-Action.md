---
title: "DreamX (KAIST·NVIDIA) — 비디오 확산모델을 잠재 행동 추출기로. 96.7%는 '서랍 닫기' 성공률이 아니라 도달+밀기 하위목표 평균이다"
type: source
domain: slam-3dgs
tags: [slam-3dgs, robotics, latent-action, video-diffusion, cosmos, cross-embodiment, human-to-robot, policy-learning, kaist, nvidia]
created: 2026-11-04
updated: 2026-11-04
sources: [https://huggingface.co/papers/2611.05377]
reliability: low
---

**HF**: published 2026-11-03 · upvote **33**(11-04 재조회 · 수집기 관측 33 · 데일리 공동 5위) · Jisoo Kim·Chaehyun Kim(공동 1저자) 외 7인(9명) · 교신 **Seungryong Kim** · 소속 **KAIST(8) · NVIDIA(Fu-En Yang)**(본문 표기) · HF 조직 KAIST AI · arXiv 2611.05377 · **코드 없음**(HF `githubRepo` null · 프로젝트 페이지 cvlab-kaist.github.io/DreamX의 외부 링크는 arXiv abs/pdf와 저자 홈페이지뿐 · 11-04 확인)

> [!note] 이름 충돌 주의
> 볼트의 [[DreamX-Phi]](Alibaba, 행동조건부 비디오 월드모델 2608.13489)·[[DreamX-World-1.0]](AMAP-ML/Alibaba, 인터랙티브 월드모델)과는 **다른 팀·다른 연구**다. 이 논문은 KAIST CVLab 작업이고, 본문에서 Alibaba DreamX 계열을 인용·계승한다는 표기는 확인하지 못했다. 공통점은 "비디오 생성 사전지식을 로봇 행동에 쓴다"는 방향뿐이다.

## 핵심 인사이트
> [!insight] 비디오 생성모델이 이미 "움직임"을 알고 있다면, 행동 라벨 대신 그 내부 표현을 읽어라
> 사전학습 비디오 DiT(**Cosmos-Predict2.5 2B**)의 시공간 토큰 열에 학습 가능한 쿼리 토큰을 붙인다. 백본 어텐션을 통과시켜 잠재 프레임당 **1,200 토큰 → 4 토큰**(300배 압축)의 잠재 행동을 뽑는다. 같은 백본에서 초기화한 디코더가 "초기 프레임 + 잠재 행동"으로 미래 영상을 복원하도록 감독한다. 그러면 잠재 행동에 외형(appearance)이 섞이지 않고 *움직임만* 남는다. 결과적으로 사람 손 영상과 로봇 영상이 **같은 행동 공간**을 공유한다. 쌍(paired) 데이터 없이 사람→로봇 영상 전이·행동 전이가 가능하다.
>
> 정책 쪽 실익: 미래 영상을 생성하는 비디오 정책(Mimic-Video)과 달리 **압축된 잠재 행동만 예측**한다. 그래서 정책 호출 지연이 28,226ms → **1,474ms**(19.1배)로 준다. 🔴 지연을 잰 하드웨어는 본문에 명시돼 있지 않다(grep "latency"·"GPU" 확인 · 학습만 H200 2장으로 명시).

> [!warning] 실로봇 서랍 닫기 수치의 구조 (Table 3·5 · 학습 궤적 45개 · 시나리오 3개 × 10회 · 양측 30,000스텝 학습)
> | 방법 | 위 서랍 도달/밀기 | 아래 서랍 도달/밀기 | 둘 다 도달/밀기 | **하위목표 SR 평균** | 지연(ms) |
> |---|---|---|---|---|---|
> | Mimic-Video | 80 / **20** | 100 / **0** | 100 / **0** | 50.0 | 28,226 |
> | DreamX | 100 / 80 | 100 / 100 | 100 / 100 | **96.7** | 1,474 |
>
> - 96.7%는 저자 정의상 "**도달(reach)과 밀기(push) 완료율의 평균**"을 3개 구성에 동일 가중한 값이다. 실제로 서랍을 닫았는지를 뜻하는 **밀기만** 보면 DreamX **93.3%**(80/100/100), Mimic-Video **6.7%**(20/0/0)다(볼트 계산). 비교 격차는 헤드라인보다 *더 크다*. 다만 Mimic-Video의 50%는 대부분 "다가가기"에서 나온 점수다.
> - 과제는 **단일 과제(서랍 닫기) · 1개 로봇 셋업 · 구성당 10회**다. 사람 영상만으로 학습한 위 서랍 구성도 100%(Table 6)로 보고됐지만, 같은 10회 규모다.
> - CALVIN 어블레이션(Table 7): 잠재 행동 조건화가 평균 연속 길이를 2.378→**2.643**으로 올린다. 외부 정책과 비교한 CALVIN 결과는 없다(내부 on/off 비교만 있음).

## 도메인별 추출 (slam-3dgs · 로봇)
- **현재 SOTA**: LARYBench(Table 1)의 잠재 행동 모델 중 1위다. 회귀 MSE 평균 **0.17**(차점 DiLA 0.38), 분류 정확도 **69.67%**(DiLA 62.25%). 32채널 압축판(FAE-32)도 0.22 / 67.15로 모든 베이스라인보다 낫다. 평가 방식은 모든 표현 모델을 고정하고 **공통 attentive probe**를 학습하는 것이다(부록 B.4). 🔴 베이스라인 수치를 직접 재실행했는지, LARY 원 논문 값을 옮겼는지는 확인하지 못했다.
- **영상 전이**: HumanAndRobot 제로샷 사람→로봇(Table 2): FVD **57.44** vs AdaWorld 170.19 · VideoWorld2 241.92, PSNR 26.52 vs 22.95/22.53. 학습에 쌍 데이터를 쓰지 않았고, 쌍 로봇 녹화는 평가 레퍼런스로만 썼다.
- **어블레이션 한정어**: 행동 라벨 보조감독은 회귀 MSE를 0.24→0.23으로 *약간 개선*하고, 분류는 65.3→64.8%로 *약간 악화*시킨다(Table 4, 축소 데이터 MolmoAct2·EgoVerse·EgoDex 부분집합). 저자는 이를 "비디오만으로 충분하다"는 근거로 읽는다.
- **실시간 가능성**: NO. 정책 호출 1.47초는 비디오 정책보다 19배 빠르지만, 30fps 제어 루프와는 거리가 멀다. 하드웨어 미명시라 내 장비 환산도 불가능하다.
- **카메라 파이프라인**: 480×640 입력, Cosmos 인과 VAE 잠재 프레임 단위. 사전학습 데이터는 사람(EgoVerse·EgoDex 등) + 로봇(MolmoAct2-BimanualYAM·Bridge·DROID·AgiBot) 6종이다.
- **응용 가능성**: 사람 시연 영상(스마트폰 1인칭)을 라벨 없이 로봇 정책 감독에 쓰는 경로다. 그러나 코드·가중치가 없어 지금은 재현할 수 없다. 공개를 지켜볼 대상이다.
- **수집기 평가**: 🔴 "성공률 평균 96.7%"는 **지표 오기**다. 저자 정의상 "하위목표(도달+밀기) 성공률 평균"이고, 서랍을 실제로 닫은 비율(밀기)은 93.3% vs 6.7%다. 소속을 "KAIST"로만 적은 것도 누락이다(NVIDIA 공저 1인). 추가 누락: 백본 Cosmos-Predict2.5 2B, 지연 측정 하드웨어 미명시, 코드 미공개. "학습 궤적 45개·시나리오당 10회×3"과 "약 19배"(저자 표기 19.1×)는 정확하다.

## 관련 페이지
- [[lary-benchmark]] (평가 벤치 LARY) · [[world-action-models]] · [[World-Action-Models-Survey]] · [[Cosmos-3]] (NVIDIA Cosmos 계열 백본)
- [[DreamX-Phi]] · [[DreamX-World-1.0]] (이름만 같은 Alibaba 계열 — 별개 연구)
- [[VLA]] · [[임바디드-AI]] · [[월드모델]] · [[Diffusion-월드모델]]
- [[NVIDIA]] · [[표-부분인용]] (하위목표 평균 vs 밀기 완료율) · [[복합지표-분해]]
- [[Route-Anything]] (같은 날 · RoboTwin VLA 정책 라우팅) · [[Kling-MLLM-Report]] · [[MoviEdit]] · [[Pandora-Client-Simulator]]

## 원본
- 출처: https://huggingface.co/papers/2611.05377 · https://arxiv.org/html/2611.05377v1 · https://cvlab-kaist.github.io/DreamX/
- 확인 범위: HF `api/papers/2611.05377` · arXiv HTML v1 Table 1~7, §3.4·4.1~4.5, 부록 A(학습 설정)·B.3(서랍 평가 프로토콜)·B.4·C.1·C.2 · 프로젝트 페이지 링크 목록 · 🔴 Table 8(교란 민감도) 미열람 · 코드 없음(실행 0회)
- 신뢰도: ⭐ (코드 없음 · 실로봇 단일 과제 10회×3 · LARYBench 1위는 공통 프로브 기준)
