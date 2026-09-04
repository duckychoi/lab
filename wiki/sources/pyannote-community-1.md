---
title: pyannote/speaker-diarization-community-1 — 3.1을 11/12 벤치마크에서 이긴 후속 (DL 5,072,652)
type: source
domain: ai-news
tags: [ai-news, hf-model, speech, speaker-diarization, audio, pyannote, generation-transfer]
created: 2026-09-04
updated: 2026-09-04
sources: []
reliability: high
---

# pyannote/speaker-diarization-community-1

**HuggingFace**: https://huggingface.co/pyannote/speaker-diarization-community-1
**다운로드(30일)**: **5,072,652** — raw 자동수집 값과 **완전 일치**
**좋아요 1,348 · 라이선스 `cc-by-4.0` · 게이트 `auto` · 생성 2025-04-15**

> [!warning] 🚨 raw 주장 정정 — **게이팅은 카드 열람을 막지 않는다**
> raw 자동수집 메모는 *"게이트 모델이라 카드 열람에 인증 필요, **벤치마크 수치는 미확인**"* 이라고 적었다. **틀렸다.** 모델 카드는 **비인증 상태로 전문 열람됐고 12개 벤치마크 표를 그대로 얻었다**(아래). 같은 배치 [[sam3]](`gated: manual`)도 마찬가지였다.
> → **규칙 추가: HF 게이팅은 *가중치 다운로드*를 막는 것이지 *모델 카드 열람*을 막지 않는다. raw가 "게이트라서 미확인"이라고 적어도 카드는 반드시 직접 확인한다.** 이는 09-03에 세운 *"raw가 결측을 적었더라도 HF 논문은 api/papers를 재확인한다"* 규칙의 **모델 쪽 대응물**이다. **동일 원인(raw의 성급한 결측 처리)이 논문·모델 양쪽에서 반복됐다.**

## 벤치마크 — DER(%), 낮을수록 좋음 (카드 원문, 2025-09 갱신)

완전 자동 처리 · **forgiveness collar 없음 · 중첩 발화 미제외**(관대한 조건을 쓰지 않았다는 점이 중요)

- **AISHELL-4**: 3.1 → 12.2 / **community-1 → 11.7** / precision-2 → 11.4
- **AliMeeting(ch1)**: 24.5 / **20.3** / 15.2
- **AMI(IHM)**: 18.8 / **17.0** / 12.9
- **AMI(SDM)**: 22.7 / **19.9** / 15.6
- **AVA-AVD**: 49.7 / **44.6** / 37.1
- **CALLHOME(part2)**: 28.5 / **26.7** / 16.6
- **DIHARD 3(full)**: 21.4 / **20.2** / 14.7
- **Ego4D(dev)**: 51.2 / **46.8** / 39.0
- **MSDWild**: 25.4 / **22.8** / 17.3
- **RAMC**: 22.2 / **20.8** / 10.5
- **REPERE(phase2)**: 7.9 / **8.9** / 7.4 ← ⚠️ **community-1이 유일하게 진 항목**
- **VoxConverse(v0.3)**: 11.2 / **11.2** / 8.5 ← 동률

**→ 12개 중 10승 1무 1패.** 카드의 *"much better than 3.1"* 은 **과장이 아니다.** 단 **REPERE에서는 3.1이 낫다**는 점을 카드가 **숨기지 않고 표에 남겼다** — 서술 정직성 상위.

> [!warning] 🚨 볼트 기존 페이지 정정 필요
> 볼트의 [[pyannote-speaker-diarization]] 페이지 제목은 *"speaker-diarization-3.1 — **화자 분리 최고 성능 모델**"* 이다. **2026-09-04 기준 사실이 아니다** — 같은 벤더가 **community-1 로 10개 항목에서 이겼고**, 그 위에 **precision-2**(클라우드 API)가 또 있다. 해당 페이지에 `> [!warning]` 로 판정 갱신을 명시했다.

> [!insight] 🔁 "세대 교체가 다운로드에서 안 일어난다" — **세 번째 재현**
> - **3.1**: DL **9,494,162** · 좋아요 **3,352** (구세대인데 **1.87배** 더 받음)
> - **community-1**: DL **5,072,652** · 좋아요 **1,348** (**성능은 더 좋은데 채택은 절반**)
>
> 볼트는 이 패턴을 이미 두 번 적었다 — `timesfm-2.5 > timesfm-3.0`(09-03), 그리고 *"좋아요는 누적되고 다운로드는 이동한다"*. 여기선 **좋아요조차 구세대가 2.5배** 많다(3.1은 2023-11 생성, community-1은 2025-04 생성 — **누적 기간이 17개월 차이**). → **3회 재현으로 "판정 보류" 단계를 넘어섰다.** 원인 가설: ①문서·튜토리얼·기존 코드가 3.1 기준으로 고착 ②`from_pretrained` 문자열을 바꿀 유인이 약함 ③성능 차이(DER 1~4%p)가 교체 비용을 못 넘김. **③이 맞다면 이는 "더 나은 모델이 이기지 않는다"의 정량적 임계값 문제**다.
>
> ⚠️ 단, 3.1의 DL은 볼트 06-02 기록(**9,650,000**)보다 **감소**했고(-155,838) community-1은 상승 중이다 — **이동은 일어나고 있으나 느리다.** 다음 회차에 두 값을 함께 재관측하면 **교체 속도를 정량화**할 수 있다(볼트 최초의 세대교체 시계열).

## 실무 정보 (카드 원문)

- 입력: **16kHz 모노**. 스테레오/다채널은 **자동 다운믹스**, 다른 샘플레이트는 **자동 리샘플**
- 개선점: **화자 배정·화자 수 세기 향상** · **exclusive diarization**(전사 타임스탬프와의 정합이 단순해짐) · **오프라인 사용 용이**
- 설치: `pip install pyannote.audio` + 이용조건 동의 + HF 토큰
- GPU: `pipeline.to(torch.device("cuda"))` · 메모리 선적재 지원 · `ProgressHook` 진행 모니터링
- **화자 수 지정**: `num_speakers=2` 또는 상·하한 지정 가능
- **precision-2** 로 올리려면 **코드 한 줄 교체**(단, pyannoteAI **서버에서 실행** — 로컬 아님)

> [!warning] precision-2는 로컬이 아니다
> 표의 최고 성능 열(precision-2)은 **API 키로 pyannoteAI 클라우드에서 도는 모델**이다. 벤더가 **오픈 모델 표에 자사 상용 모델을 나란히 세워** 성능 우위를 보여주는 구조 — 정직하지만 **동일 조건 비교로 읽으면 안 된다**(로컬 vs 클라우드). 볼트의 *"오픈 가중치 ≠ 오픈 시스템"*([[MiniMax-H3]]) 축의 **음성판**.

## 도메인별 추출 (ai-news)

- **신뢰도**: ⭐⭐⭐⭐⭐ — DL 507만·12개 학술 벤치마크 공개·관대한 조건 미사용·**패배 항목까지 공개**.
- **즉시 활용**: **YES.** `/down-analysis`·`/reat-voice` 파이프라인에서 **모델 문자열만 바꾸면 됨**. 화자 배정·화자 수 세기 개선은 다화자 인터뷰 자막 분리에 직접 이득.
- **6개월 영향력**: **exclusive diarization** 이 전사 타임스탬프 정합을 단순화한다는 점이 크다 — 볼트의 SRT 기반 [[TCR]] 관심사(타이밍 정확도)와 **같은 축**이다.
- **대체 관계**: [[pyannote-speaker-diarization]](3.1)을 **대체**. 단 REPERE류(방송 뉴스) 도메인은 예외.
- **허와 실**: *"much better"* 는 **검증됐다**(10/12승). 다만 개선폭은 대체로 **DER 1~4%p** 로, 극적이지 않다.

> [!action] 당장 할 것
> `/down-analysis` 파이프라인의 pyannote 호출을 **`community-1` 로 교체**하고, **같은 다화자 오디오 1건**을 3.1과 community-1로 각각 돌려 화자 수 판정이 달라지는지 확인. 볼트 자체 A/B 1건이면 위 벤치마크가 우리 데이터에서도 성립하는지 판정된다.

## 관련 페이지
- [[pyannote-speaker-diarization]] · [[sam3]] · [[VoiceStudio]] · [[TCR]] · [[Audio-Visual-Intelligence-Foundation-Models]] · [[AVA-Encoder]] · [[kyutai-labs]] · [[PyTorch]] · [[MiniMax-H3]] · [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/pyannote/speaker-diarization-community-1
- 벤더 블로그: https://www.pyannote.ai/blog/community-1
- 수집: 2026-09-04 자동수집 (ai-news)
- 검증: 모델 카드 defuddle 원문 + HF API 실측 (2026-09-04) — **raw의 "미확인" 주장 반증**
- 신뢰도: ⭐⭐⭐⭐⭐
