---
title: "autoclip — 자막을 읽어 하이라이트를 자르는 도구, 그리고 '0개 완료'를 11개월 뒤에 실패로 바꾼 기록"
type: source
domain: video-saas
tags: [video-saas, 영상자동화, ai-news, github-trending, auto-highlight, whisper, ffmpeg, mcp, 수집기-정정]
created: 2026-09-22
updated: 2026-09-22
sources: []
reliability: high
---

# autoclip

> [!insight] 🎯 핵심 인사이트 — 이 도구는 **영상을 보지 않고 자막만 읽는다**. 그리고 README가 그 사실을 스스로 적어 둔다
> README 175행 원문: *"当前分析主要**基于字幕**，适合访谈、播客、课程和口播。**纯视觉动作或音乐类视频效果可能有限**。"*
> 파이프라인은 `step1_outline → step2_timeline → step3_scoring → step4_title → step5_clustering → step6_video`(`backend/pipeline/`) 6단계. 1~5단계는 **전부 텍스트 위의 LLM 호출**이고, 영상은 6단계에서 FFmpeg로 자를 때만 만진다. `requirements.txt` 에 OpenCV 같은 영상·이미지 분석 라이브러리는 **없다**.
> 📌 [[video-use]] 가 적었던 *"LLM은 영상을 transcript로 읽는다"* 는 구조의 **두 번째 사례**다. 같은 약점(순수 비주얼·음악 영상)을 가지며, autoclip은 이를 README에서 **먼저 인정한다**.

> [!warning] 🔴 수집기 정정 1 — *"README에 Whisper/ASR 언급 없음"* 은 틀렸다
> - **수집기가 봤을 09-20 버전 README(`9796e86d`)에도 있다**: 155행 `autoclip doctor  # 检查 ffmpeg / Whisper / 模型`
> - 현재 README(v1.3.1, `f82e0d82`): 114행 *"无字幕视频需要 `faster-whisper`，首次转写会下载语音模型"* · 161행 FAQ *"没有字幕也能使用吗？ — **可以**，需要先准备本地 Whisper 组件和语音模型"* · 56행 흐름도에 *"准备字幕 / **语音转写**"*
> - 코드: `backend/services/whisper_runtime.py`(faster-whisper, CTranslate2 기반, 데스크톱에선 **필요할 때 설치**) · `whisper_model_manager.py` · 루트 `check_whisper_status.sh` · `docs/WHISPER_SUBTITLE_STRATEGY.md`
> 🔴 따라서 *"로컬 파일은 자막을 따로 올려야 분석 근거가 생기는 구조"* 도 틀렸다. SRT는 **선택 사항**이고, 없으면 Whisper가 전사한다(Whisper 미설치 시 실패 힌트: *"到「设置 → 转写」安装 Whisper 模型…或导入 .srt 字幕"*, `failures.py`).
> 📌 [[메타데이터-부재-추론]] 의 README 판이다 — **읽은 범위에서 못 찾은 것**을 *"없다"* 로 썼다.

> [!warning] 🔴 수집기 정정 2 — 분석 모델은 *"DashScope `qwen-plus`"* 하나가 아니다
> `qwen-plus` 는 **구 README의 `.env` 예시 값**(305행)일 뿐이다. 같은 구 README 34행부터 이미 *"通义千问 / OpenAI 兼容接口 / Gemini / 硅基流动，也可用 **Ollama、LM Studio 本地模型**（免 key、离线）"*. 현재 README 53·134–138행도 동일(Ollama 기본 `qwen2.5:7b`).
> 📌 예시 값이 제품 사양으로 승격됐다 — [[표-부분인용]] 과 같은 형태(**한 칸만 읽고 표 전체를 대표시킴**).

> [!note] ✅ 수집기가 맞은 것
> - ✅ **시각(화면) 분석 없음** — README 175행 + 의존성으로 확인.
> - ✅ **v1.3 "0 clips completed" 버그** — 커밋 `7c447bf5`(2026-09-20): *"v1.3: fail loudly instead of 'Completed · 0 clips' (+ 3 latent bugs…)"*. `backend/pipeline/failures.py` 머리 주석: *"不能吞掉后继续跑成 `Completed · 0 切片`（**#100 #11 #24** 的共同表象）"*.
>   🎯 **볼트 추가**: 가장 오래된 이슈 **#11 *"ai生成切片为0"* 은 2025-10-09 에 열렸다** — 증상이 **약 11개월** 동안 "완료"로 표시됐다.
> - ✅ B站 업로드·자막 편집·모바일 **【开发中】** — 09-20 README 40·44·45행에 실재. 단 **v1.3.1 README(09-21)에서는 해당 목록이 빠졌다**(기능이 완성됐다는 뜻인지는 ⬜ 미확인).
> - ✅ Celery+Redis+React — 맞다. 단 **CLI 경로는 Redis가 필요 없다**(README 103행) · 데스크톱은 **Tauri**(`src-tauri/`).

> [!warning] ⚠️ 볼트 추가 발견 — "설정했는데 안 먹던" 값
> `step3_scoring.py` 의 docstring: *"设置页那个值以前只改了 API 进程的内存，**流水线从来没读过**。"* — **v1.3 이전엔 설정 페이지의 최저 점수 임계값이 파이프라인에 전달되지 않았다**(커밋 `ef83c2dd`, #104). README 168행의 *"阈值从 0.7 降到 0.5"* 조언은 **v1.3 이상에서만 유효**하다.
> 또 `backend/pipeline/config.py` 에는 `MIN_SCORE_THRESHOLD = 7.0` 이, 실제 import되는 `backend/core/shared_config.py` 에는 `0.7` 이 있다 — 잔재로 보이나 사용처는 ⬜ 미확인.

## 도메인별 추출 (video-saas)

> [!note] 도메인 재분류 근거
> 수집기는 `ai-news` 로 분류했으나 **제품 전체가 영상 자동화 파이프라인**(다운로드 → 전사 → LLM 분석 → 클립·합집 → 플랫폼 프리셋 내보내기)이므로 도메인 1(`video-saas`)로 옮긴다. GitHub 레포라 `/down-video` 선행 절차는 해당 없음.

- **신뢰도**: ⭐⭐⭐ — ★8,577 · MIT · 코드·프롬프트 전부 공개. README의 한정어가 정직하다(*"不保证一定有片段"* 168행 · *"效果可能有限"* 175행 · *"个人业余维护"* 206행). 🔴 단 **개인 취미 유지보수**이고 핵심 실패 증상이 11개월 방치됐다.
- **기능 벤치마킹**: 난이도 **낮음**. 구조가 단순하다 — `prompt/` 에 **5개 프롬프트 × 7개 장르**(business·content_review·entertainment·experience·knowledge·opinion·speech) + 기본 세트. 장르별 프롬프트 분기가 사실상 이 도구의 "모델"이다.
- **크리에이터 인사이트**: 사용자가 원하는 것 = "긴 영상에서 쓸 만한 조각". 도구가 주는 것 = **말이 많은 영상의 조각**. 🎯 **토킹헤드엔 맞고, 리액션·액션·음악 영상엔 원리적으로 약하다** — 이 갭이 빈틈이다.
- **프롬프트 패턴**: 대강(大纲) → 시간점(时间点) → 추천 이유(推荐理由, 점수) → 제목 → 주제 클러스터링. **점수와 이유를 같은 호출에서 받는다**(`final_score` + `recommend_reason`). 임계값 미달 시 *"兜底补齐"*(폴백으로 채움) 로직 존재.
- **워크플로우**: 데스크톱(.dmg/.exe, Python·FFmpeg 내장) · Docker Web · **CLI/MCP** 3형태. `autoclip run talk.mp4 --provider ollama --json` → `autoclip export ID --preset shorts`. **`autoclip mcp` = stdio MCP 서버** + `skills/autoclip/SKILL.md` — [[에이전트-스킬]] 로 바로 붙는다.
- **디자인 레퍼런스**: 내보내기 프리셋(抖音·小红书·YouTube Shorts·B站) + 자막 번인 + 제목 카드. v1.3.1부터 UI **8개 언어(한국어 포함)**.
- **경쟁 우위 빈틈**: **시각 신호를 쓰는 하이라이트**(웃음·동작·장면 전환). autoclip·[[video-use]] 둘 다 transcript 기반이므로 여기가 비어 있다. [[OpenCreator]] 도 Auto Clips를 개발 중이다(README "In development", 커밋상 09-10부터 작업).

> [!action] 당장 할 것
> 볼트 운영자의 한국어 토크 영상 1건(3–5분, README 권장 길이)을 `autoclip run --provider ollama` 로 돌려 **Whisper 한국어 전사 품질 → 클립 수**를 본다. 0개면 v1.3의 실패 단계 메시지(`INGEST/SUBTITLE/ANALYZE/HIGHLIGHT/EXPORT`)가 **어디서 멈췄는지 말해 주는지**가 검증 포인트다.

## 관련 페이지
- [[스키마-준수-보장]]  *(09-22 연결)*
- [[video-saas]]
- [[video-use]]
- [[OpenCreator]]
- [[MoneyPrinterTurbo]]
- [[OpenMontage]]
- [[openai-whisper]]
- [[에이전트-스킬]]
- [[메타데이터-부재-추론]]
- [[표-부분인용]]
- [[검사가능성-공사]]

## 원본
- 출처: https://github.com/zhouxiaoka/autoclip
- 볼트 실측(2026-09-22, GitHub API): ★**8,577**(raw 7,949 → +628, 약 1일) · fork **1,594** · **MIT** · Python · owner **User** · open issues **24**(raw 12) · created 2025-07-08T04:51:15Z · pushed 2026-09-22T08:50:08Z · topics 13 · homepage zhouxiaoka.github.io/autoclip_intro
- 릴리스: v1.0.0(2025-09-15) → v1.2.1(2026-09-06) → **v1.3.0(09-20)** → **v1.3.1(09-21)**
- 수치 출처: README 현재판(`f82e0d82`) 전문 218행 + 09-20판(`9796e86d`) 890행 대조 · `backend/pipeline/failures.py` · `step3_scoring.py` · `whisper_runtime.py` · `requirements.txt` · 이슈 #11 원문 메타데이터
- raw 대비: 볼트 추가 = 🔴 **"Whisper/ASR 없음" 정정(구·현 README + 코드 3곳)** · 🔴 **"qwen-plus 단일" 정정(예시 값의 사양화)** · ✅ 0-clips 버그 확인 + **증상 기간 약 11개월(#11, 2025-10-09)** · ⚠️ **v1.3 이전 임계값 설정 무효** · 도메인 **video-saas 재분류**
- 신뢰도: ⭐⭐⭐ (코드 공개·한정어 정직 / 개인 유지보수·장기 방치 버그)
