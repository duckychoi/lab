---
title: "Wave Forcing — 이전 청크가 다 지워지기 전에 읽게 해서 디노이징을 파이프라인으로 만든 스트리밍 비디오 생성"
type: source
domain: video-saas
tags: [video-saas, streaming-video, autoregressive, diffusion, real-time, wan2.1, multi-gpu, pipeline-parallel]
created: 2026-11-03
updated: 2026-11-03
sources: [https://huggingface.co/papers/2611.00859]
reliability: medium
---

**HF**: published 2026-10-31 · upvote **74**(11-03 재조회 · 수집기 09시 관측 73) · Yijie Jin 외 9인(10명) · HF 조직 표기 **DENG Lab @ SJTU** · arXiv 2611.00859 · 코드 [SJTU-DENG-Lab/WaveForcing](https://github.com/SJTU-DENG-Lab/WaveForcing) **★89 · Apache-2.0** (api.github.com 11-03 실측 · HF `githubStars` 캐시값은 68) · 루트에 `training/`·`wave_rt/`·`naive_rt/` 존재(실행 0회)

## 핵심 인사이트
> [!insight] 속도와 품질은 서로 다른 설정에서 나온 숫자다
> 청크 단위 인과 어텐션으로 **아직 디노이징이 끝나지 않은 이전 청크의 깨끗한 중간 상태**를 다음 청크가 조건으로 읽는다. 엇갈린 디노이징·캐시갱신 단계를 모델 복제본(GPU당 1단계)에 나눠 **파이프라인이 찬 뒤 라운드당 완성 청크 1개(1F1C)**를 낸다. 저자는 이 방식이 "청크당 작업량과 **첫 출력 지연은 줄이지 않는다**"고 직접 적었다. 빨라지는 것은 처리량이고, 첫 프레임이 나오는 시간은 그대로다.
>
> 헤드라인 **147.6 FPS는 4스텝** 모델 값이다. 4스텝의 VBench Total은 **80.74로 Rolling Forcing(81.15)보다 낮다**. "품질 comparable"은 **5스텝** 모델 값이고, 5스텝의 E2E는 **96.46 FPS**다.

> [!warning] "comparable"의 실제 폭 (본문 Table 1, Wan2.1-T2V-1.3B)
> | 지표 | Rolling Forcing (5스텝·1GPU) | RF + 인과마스크 (5스텝·8GPU·WaveRT) | WF 5스텝 (8GPU) | WF 4스텝 (8GPU) | Causal Forcing (4스텝·1GPU) |
> |---|---|---|---|---|---|
> | VBench Total | 81.15 | 80.89 | **81.64** | 80.74 | 79.61 |
> | VBench Quality | 83.77 | 83.35 | **84.40** | 83.93 | 82.83 |
> | Semantic | **70.66** | 71.05 | 70.59 | 67.95 | 66.72 |
> | Dynamic(단편) | 51.39 | 37.50 | 94.44 | 84.72 | 100.00 |
> | VBench-Long Quality | 81.18 | 80.50 | 81.26 | 80.89 | **82.15** |
> | Dynamic(100초) | 36.63 | 46.60 | 91.45 | 74.97 | 96.61 |
> | Subject 보존 ↑ | 92.75 | 91.26 | **97.10** | 91.88 | 71.11 |
> | Camera Drift ↓ | **0.17** | 0.40 | 0.37 | 0.36 | 11.14 |
> | E2E FPS | 17.46 | **96.56** | 96.46 | **134.81** | 19.06 |
>
> - 품질 차이: Total **+0.49**, Long Quality **+0.08**. Semantic은 **−0.07**로 오히려 낮다. Drift는 0.17→0.37로 **나빠졌다**. 큰 차이는 **Dynamic Degree**(51→94, 37→91)에만 있다.
> - VBench-Long Quality 1위는 WF가 아니라 **Causal Forcing(82.15)**이다. 다만 Causal Forcing은 피사체 보존이 71.11이라 저자가 "unusable"로 판정했다.
> - 🔴 **같은 8GPU WaveRT 위에서 돌린 RF+인과마스크가 96.56 FPS**로, WF 5스텝(96.46)과 같다. 5스텝끼리 비교하면 속도 이득은 *방법*이 아니라 *런타임(WaveRT)*에서 나온다. WF의 기여는 같은 속도에서 Dynamic·Subject를 올린 **학습 레시피** 쪽이다. 이 문장은 볼트가 표에서 읽어낸 해석이고, 저자는 이렇게 쓰지 않았다.

> [!warning] 시스템 수치는 더미 가중치로 쟀다
> Table 4·6과 §5.3은 **"All rows use dummy DiT weights and a real-weight VAE"**라고 적었다. 7.07배는 같은 규모·같은 스텝의 **단일 GPU 롤링 추론 19.06 FPS** 대비 값이고, 병렬화·그래프·커널·디코딩 변경이 합쳐진 결과다(저자 명시). 14B 모델은 **학습하지 않았다**("required computation exceeds…"). 14B 6.08배는 아키텍처만 같은 실행 측정이다.
> - Wave Parallelism의 "최대 2.53배"는 **Sage+W8A8**에서만 나온 값이다(1.025~2.530배, 6규모 전승). **BF16에서는 0.985~1.862배**이고, **9B에서 Ulysses에 1.53% 진다**(45.70 vs 46.41 FPS). → [[배수-조건분산]]

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 실시간 스트리밍 생성은 *H200 8장 1노드*가 전제다(4스텝 기준 디노이징 4 + store 1 + VAE 3). SaaS에 넣으려면 GPU 8장을 세션 1개가 점유한다. 1.3B·832×480 기준이며, 상용 품질 해상도·모델 규모의 학습 체크포인트는 없다.
- **크리에이터 인사이트**: 기존 스트리밍 모델의 불만은 "움직임이 죽는다"(RF 100초 Dynamic 36.63)와 "피사체가 사라진다"(Causal Forcing 30초·75초 시점 소실)다. WF는 둘을 동시에 잡은 첫 수치를 냈다.
- **평가 교훈**: 저자 스스로 한계 절에서 **"VBench 점수가 높아도 피사체 소실·카메라 드리프트가 함께 나타난다"**고 썼다. 그래서 SAM3+DINO로 Subject 보존과 Camera Drift 지표를 따로 만들었다. 100프롬프트 부분집합 기준이다. 영상 품질 QA에서 *총점 하나*를 믿지 말라는 직접 근거로 쓸 수 있다.
- **워크플로우**: 3단계 학습(혼합노이즈 초기화 → 교사 유도 모션 감독(DMD) → 자기생성 이력 인과적응). 어블레이션에서 2단계를 빼면 Dynamic이 **74.97→15.73**으로 무너진다(Table 2).
- **경쟁 우위 빈틈**: 프롬프트 갱신·온라인 상호작용은 **미지원**이고 향후 과제로 적혀 있다(§7·부록 E). 대화형 [[월드모델]]로 가는 길은 아직 열려 있지 않다.

## 관련 페이지
- [[causal-forcing-plus-plus]] (직접 비교군 계열) · [[AI-영상-생성-2026]] · [[Diffusion-월드모델]] · [[월드모델]] · [[drama-3]] (스트리밍 속도 정의 문제)
- [[배수-조건분산]] (2.53배 = Sage+W8A8 한정) · [[한정어-탈락]] (comparable ≠ better · 4스텝 속도와 5스텝 품질의 결합) · [[표-부분인용]] · [[상대속도-가림]]
- [[Video-Generation-Agent-Harness]] (같은 날 · 비디오 모델을 렌더러로 쓰는 하네스 관점)

## 원본
- 출처: https://huggingface.co/papers/2611.00859 · https://arxiv.org/html/2611.00859
- 확인 범위: HF `api/papers/2611.00859` · arXiv HTML 본문 Table 1·2·4·6, §5.1~5.5, §7 · GitHub API(레포 메타·루트 목록) · 🔴 Table 6 개별 규모 행과 부록 C.3 반복 범위는 일부만 확인 · 코드 실행 0회
- 신뢰도: ⭐⭐ (코드 공개·Apache-2.0·★89 · 품질 표는 실체크포인트 · 시스템 표는 더미 가중치 · 1.3B만 학습)
