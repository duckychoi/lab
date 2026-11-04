---
title: "MoviEdit — 장편 멀티샷 영상 편집. 자체 벤치 Edit Success 1위지만 샷 간 일관성·영상 품질·외부 벤치 정확도는 상용에 진다"
type: source
domain: video-saas
tags: [video-saas, video-editing, multi-shot, long-form, adobe, kaist, benchmark, distillation, aleph]
created: 2026-11-04
updated: 2026-11-04
sources: [https://huggingface.co/papers/2611.02737]
reliability: medium
---

**HF**: published 2026-11-02 · upvote **39**(11-04 재조회 · 수집기 관측 38 · 데일리 3위) · Suhyeon Lee 외 8인(9명) · 소속 **Adobe · KAIST**(본문 표기, Jong Chul Ye 등) · HF 조직 Adobe · arXiv 2611.02737 · 공개물은 **벤치만**: [adobe-research/MoviEdit-Bench](https://github.com/adobe-research/MoviEdit-Bench) **★5 · 라이선스 "Other"**(api.github.com 11-04 실측 · HF 캐시값 2). LICENSE.md에 따르면 `bench/moviedit_bench/*.py` 평가 코드만 **Adobe Research License**다. **모델 가중치·학습 코드는 미공개**(레포 루트 `bench/`·`assets/`만 있음)

## 핵심 인사이트
> [!insight] "초안은 압축 공간에서 양방향, 완성은 원해상도에서 자기회귀"
> 장편 멀티샷 편집의 난점은 샷이 바뀌어도 같은 편집(같은 옷·같은 추가 물체)을 유지하는 것이다. MoviEdit는 이를 2단으로 푼다. **Draft Editor**는 시공간을 압축한 표현 위에서 양방향으로 전역 초안을 잡는다. **Render Editor**는 그 초안을 조건으로 전체 영상에 자기회귀 전파·정제한다. 두 모듈은 가중치를 공유한다. 데이터는 수동 라벨 없이 **3개 자동 파이프라인**으로 만든다(동기 멀티뷰 촬영·실제 멀티샷 영상·생성 멀티샷 콘텐츠). 원시 205,228쌍을 필터링해 **86,619쌍**(540p · 10~15초 · 4~6샷)이 남는다(Table 3).
>
> 속도 면의 실익은 **증류**에서 나온다. 540p·361프레임·**H100 8장** 기준 전체 시간 어텐션은 364.1초가 걸린다. 슬라이딩 윈도 258.9초, KV 캐시 166.8초, **VMM 증류(Draft 12스텝 · Render 4스텝)** 후 **11.8초**다(×30.9, Table 4). 입력 길이 15초보다 짧다. 🔴 Table 1·2의 품질 수치가 교사(teacher) 모델인지 증류 모델인지는 본문에서 확인하지 못했다(grep "teacher" 1건 = 증류 절차 설명).

> [!warning] Table 1 (V2V 텍스트 지시 편집 · MoviEdit-Bench · 판정 VLM = Gemma 4 + Qwen3 인용) — 이긴 칸과 진 칸
> | 지표 | MoviEdit | Aleph 2.0 | Gemini Omni Flash | HappyHorse-1.0 | Wan-Edit(최고 오픈) |
> |---|---|---|---|---|---|
> | **Overall Edit Success (VLM)** | **0.790** | 0.764 | 0.586 | 0.623 | 0.378 |
> | Non-subject 보존 LPIPS ↓ | **0.0741** | 0.0916 | 0.153 | 0.246 | 0.0816 |
> | Subject 보존 LPIPS ↓ | 0.121 | 0.146 | 0.193 | 0.291 | **0.103** |
> | **샷 간 편집 일관성 (VLM)** | 0.904 | **0.981** | 0.893 | 0.894 | 0.692 |
> | 편집 프롬프트 정렬 (VLM) | **0.884** | 0.846 | 0.834 | 0.815 | 0.515 |
> | ViCLIP | 0.190 | 0.186 | **0.194** | 0.193 | 0.178 |
> | **영상 품질 (VLM)** | 0.762 | 0.801 | **0.814** | 0.691 | 0.568 |
> | NIQE ↓ | 4.85 | 4.95 | 4.95 | 5.12 | 5.38 (Memory-V2V **4.82**) |
>
> - 이 논문의 핵심 주장은 "샷 간 일관성"이다. 그런데 그 칸(X-shot Edit Consistency)에서 **Aleph 2.0이 0.981로 MoviEdit(0.904)보다 높다**.
> - 영상 품질 VLM도 Gemini Omni Flash·Aleph 2.0보다 낮다. 종합 Edit Success 1위는 보존·국소화·프롬프트 정렬 칸에서 이긴 결과다.
> - 벤치 규모: 소스 영상 **64개 × 시나리오 2개 = 128 시나리오**(지역 편집 75% · 전역 편집 25%). 시나리오와 지시문은 LLM이 작성하고 사람이 검토했다. VLM 판정은 샷당 프레임 4장의 쌍 비교로 이진 판정한다. 사람 평가는 없다.

> [!warning] IV2V(편집된 프레임 전파)와 외부 단편 벤치에서는 우위가 사라진다
> - **Table 2 IV2V 첫 프레임 64 시나리오**: Overall **Aleph 2.0 0.806 > MoviEdit 0.803**. 임의 프레임: MoviEdit 0.786 vs Aleph 0.781(+0.005). 사실상 동률이다. Non-subject LPIPS는 Aleph가 낫다(0.0412 vs 0.0586).
> - **Table 9 FiVE-Bench(단편·단일샷)**: 정확도 지표 **FiVE-Acc가 MoviEdit 0.6623으로 Gemini Omni Flash 0.8007 · HappyHorse 0.7864 · Aleph 0.7784보다 낮다**. 배경 보존(PSNR 26.59)과 VPBench는 MoviEdit가 앞선다. 저자 요약은 "comparable to or competitive with"다.
> - 초록 "performs **on par with** industry frontier models"는 이 표들과 들어맞는다. "Edit Success 0.790 > Aleph 0.764" 한 칸만 옮기면 우위로 읽히지만, 저자 표현은 "대등"이다. → [[한정어-탈락]]

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 멀티샷 일관 편집(옷 교체·물체 추가가 모든 샷에 유지)은 쇼츠/광고 SaaS의 "한 번 수정 → 전 컷 반영" 기능에 직결된다. 그러나 **가중치가 없다**. 학습에는 H200 64장(FSDP, V2V 17K + IV2V 8K 스텝)이 들었고, 비공개 단편 편집 데이터와 비공개 MoE DiT 백본도 필요하다. 자체 구현은 비현실적이다. 현실적 경로는 상용 **Aleph 2.0**(Runway)이나 Gemini Omni Flash API다.
- **평가에 쓸 수 있는 것**: MoviEdit-Bench 평가 코드(Adobe Research License)는 **내 편집 파이프라인 QA 도구**로 쓸 수 있다. 7개 차원(비대상 보존·국소화·대상 보존·샷 간 일관성·프롬프트 정렬·편집 프레임 충실도·영상 품질)을 VLM 판정 + LPIPS/DINO/NIQE로 측정한다. 라이선스 조건(상업 사용 가부)은 미확인이다.
- **크리에이터 인사이트**: 저자 정성 관찰(Fig.7) — HappyHorse·Gemini Omni는 편집은 잘하지만 **원본을 이탈한다**(샷 전환·타이밍을 지키지 못하고, 원본에 없는 움직임을 환각). "편집"을 원하는 사용자에게 재생성형 툴이 주는 갭이 바로 이것이다.
- **경쟁 우위 빈틈**: 실패 사례(Fig.12): (a) 비슷한 피사체가 여럿이면 엉뚱한 대상을 편집, (b) 대상이 일부만 보이면 샷 간 연결 실패. 15초까지 학습했고 25초·17샷까지 일반화한다고 주장하지만, 이는 정성 예시뿐이다(Fig.15).
- **수집기 평가**: 🔴 "Overall(VLM)은 0.762로 Gemini Omni Flash 0.814·Aleph 2.0 0.801보다 낮음"은 **열 오인**이다. 0.762/0.814/0.801은 **Video Quality(VLM)** 열이고, Overall Edit Success는 0.790/0.586/0.764다(수집기가 같은 줄 앞에서 Edit Success로 맞게 인용한 값). 누락: 샷 간 일관성 Aleph 0.981 우위, IV2V 첫 프레임 Aleph 0.806 우위, FiVE-Acc 열세, VLM 판정자 정체(Gemma 4·Qwen3 인용), 128 시나리오 규모, 가중치 미공개.

## 관련 페이지
- [[AI-영상-생성-2026]] · [[InfinityEdit]] · [[JoyAI-Video-Edit]] · [[LiveEdit]] · [[What-to-Edit-Next]] (영상 편집 계열 소스)
- [[Kling-MLLM-Report]] (같은 날 · 영상 생성 이해 스택) · [[WaveForcing]] (자기회귀 영상 생성 · 증류)
- [[요약자와-판정자-분리]] (VLM 단일 판정 · 사람 대조 없음) · [[한정어-탈락]] · [[표-부분인용]] · [[벤치마크-외부축]] (자체 벤치 vs FiVE/VPBench)
- [[Alibaba]] (HappyHorse-1.0 · Alibaba Cloud)

## 원본
- 출처: https://huggingface.co/papers/2611.02737 · https://arxiv.org/html/2611.02737v1 · https://multi-shot-edit.github.io/
- 확인 범위: HF `api/papers/2611.02737` · arXiv HTML v1 Table 1·2·3·4·9, §3 증류, §4.1, 부록 B.2·VLM 판정 절, 한계·실패 사례 · GitHub API(레포 메타·루트) · raw LICENSE.md 앞부분 · 🔴 Table 5~8(데이터·벤치 세부)·Fig.10 스케일링 수치는 미열람 · 코드 실행 0회
- 신뢰도: ⭐⭐ (Adobe·KAIST · 평가 코드만 공개 · 자체 벤치 + 외부 단편 벤치 병기 · 사람 평가 없음)
