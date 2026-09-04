---
title: pyannote/speaker-diarization-3.1 — 화자 분리 최고 성능 모델
type: source
domain: ai-news
tags: [ai-news, hf-model, speech, speaker-diarization, audio, pytorch, tts]
created: 2026-06-02
updated: 2026-09-04
sources: []
reliability: high
---

# pyannote/speaker-diarization-3.1

**HuggingFace**: https://huggingface.co/pyannote/speaker-diarization-3.1  
**다운로드**: 9,650,000+ (월간, 2026-06-02 기준)  
**라이선스**: MIT  
**신뢰도**: ⭐⭐⭐⭐⭐ (HF 다운로드 최상위, INTERSPEECH 2023 논문)


> [!warning] 🔄 2026-09-04 판정 갱신 — 이 페이지 제목의 "최고 성능"은 더 이상 사실이 아니다
> 같은 벤더가 **[[pyannote-community-1]]** 을 내놓았고, 카드 공개 벤치마크 12종에서 **3.1 대비 10승 1무 1패**다(3.1이 이긴 건 REPERE phase2 뿐: 7.9 vs 8.9). 그 위에 클라우드 전용 **precision-2** 가 또 있다.
> **원 서술은 지우지 않고 보존한다** — 2026-06-02 시점에는 맞았고, *무엇이 언제 뒤집혔는지가 그 자체로 기록*이기 때문이다(볼트 09-03 정정 관행 준수).
> ⚠️ **다운로드는 아직 3.1이 앞선다**: 3.1 **9,494,162** vs community-1 **5,072,652**(2026-09-04 API 실측). 단 3.1은 06-02 기록(9,650,000) 대비 **감소**했고 community-1은 상승 중 — *"세대 교체가 다운로드에서 안 일어난다"* 패턴의 **세 번째 재현**이자 볼트 최초의 **세대교체 시계열 관측 대상**.

## 핵심 인사이트

> [!insight] 핵심 인사이트
> 월 965만 다운로드 — HF 전체 모델 중 최상위권 오디오 모델. "누가 언제 말했는가" 자동 분리. 순수 PyTorch 기반(onnxruntime 제거), GPU 가속, 화자 수 자동/수동 지정. 영상 분석·팟캐스트·회의 녹취 자동화에 즉시 활용 가능.

> [!action] 당장 할 것
> `pip install pyannote.audio` 후 reat-voice/down-analysis 파이프라인에 통합. 멀티 스피커 인터뷰 영상 자막 분리에 즉시 적용. HF 토큰 + 이용 약관 동의 필요.

## 도메인별 추출 (ai-news)

**즉시 활용**: YES — pip 설치, 3줄 코드로 기동  
**신뢰도**: ⭐⭐⭐⭐⭐ (HF 최상위, 논문 있음)  
**대체 관계**: AssemblyAI, Rev.ai 유료 화자 분리 API 대체 가능  
**트레이드오프**: 로컬 GPU 있으면 빠름, CPU는 느림; HF 토큰 + 약관 동의 필요

**성능 지표 (DER %):**
- REPERE: 7.8% (최고 성능)
- VoxConverse: 11.3%
- AISHELL-4: 12.2%
- AMI (headset): 18.8%
- DIHARD 3: 21.7%

**사용법:**
```python
from pyannote.audio import Pipeline
pipeline = Pipeline.from_pretrained(
    "pyannote/speaker-diarization-3.1",
    use_auth_token="YOUR_HF_TOKEN"
)
diarization = pipeline("audio.wav")
# 화자 수 지정
diarization = pipeline("audio.wav", num_speakers=2)
```

**GPU 가속:**
```python
pipeline.to(torch.device("cuda"))
```

> [!note] 배경 정보
> reat-voice로 생성한 TTS 음성이나 down-video로 받은 영상의 멀티 스피커 분리에 직접 적용 가능. 회의 녹음 → 화자별 자막 분리 → LLM 요약 파이프라인의 핵심 부품.

## 관련 페이지
- [[VoxCPM]]
- [[AI-영상-생성-2026]]

## 원본
- 출처: https://huggingface.co/pyannote/speaker-diarization-3.1
- 신뢰도: ⭐⭐⭐⭐⭐ (월 965만 다운로드, INTERSPEECH 2023)
