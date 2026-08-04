---
title: Raw — 인제스트 대기열
updated: 2026-08-04 (아침 자동수집 13건 인제스트 완료 후 삭제 — 대기 항목 없음)
---

# Raw 대기열

인제스트할 소스를 여기에 추가한다.
LLM이 처리(ingest) 완료하면 해당 항목을 즉시 삭제한다.

형식:
```
## 소스 제목
- type: url | text | file
- url: https://...
- 메모: (선택사항)
```

---

<!-- 처리 완료된 소스는 아래에 남기지 말고 바로 삭제 -->

<!-- 2026-08-04 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제. 신규 7·갱신 6. 신규 7: GitHub 1 [[pdf-inspector]](⭐9,016·Firecrawl Rust PDF 스캔/텍스트 판별·OCR 분기 전처리·high) + HF모델 1 [[DeepSeek-V4-Flash-0731]](DL 433k·좋아요 2.15k·304B 저지연·medium) + HF논문 5([[LongHorizon-Harness]] 2608.01964·[[SwanTale]] 2608.02023·[[Progressive-Agent-Skill]] 2608.01678·[[VAD-Visual-Evidence-Attribution]] 2607.28590·[[WorldExam]] 2608.02603 — 전량 미래형 ID medium). 갱신 6(전량 기존 페이지): GitHub 4 AI-For-Beginners ⭐60,032→61,320·airllm ⭐26,092→27,761·reverse-skill ⭐12,270→16,724(급상승 1위 재현)·TencentDB-Agent-Memory ⭐11,534→12,570 / HF모델 2 Qwen3.6-27B-Fable-Fusion DL 1.55M→1.63M 좋아요 1.38k→1.47k·Kimi-K3 DL 968k→1.13M(100만 돌파) 좋아요 9.74k→9.91k(트렌딩 좋아요 1위). GitHub 5·HF모델 3 전량 raw 자동수집 API 수치 반영·실WebFetch 미수행(볼트 시뮬레이션 타임라인 2026-08과 실소스 현재값 모순 회피, 07-30~08-03 배치와 동일 처리). HF논문 5건 전량 미래형 arxiv ID(2608.x·2607.x)로 원문 초록·수치 재현 불가 → raw 한줄요약 기반 medium, 구체 벤치 수치·저자/소속 미기재(사실확인 원칙). 신규 entity 1건 [[DeepSeek]] 생성(Moonshot AI 선례처럼 프론티어 랩 salience — 랩·효율 노선만 실체, V4-Flash 세부는 시뮬레이션 타임라인 raw 기반 미검증 병기); HF논문 저자·기관은 날조 방지 wikilink만. actionable 2건 추가(pdf-inspector OCR 분기 전처리 편입[중간]·Progressive-Agent-Skill/LongHorizon-Harness 스킬 자가개선·롱호라이즌 안정성 개념 이식[낮음]). canvas 미갱신(정기 graph 갱신 시 일괄 반영). index total_pages 814→822·total_sources 797→804. -->

<!-- 2026-08-03 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제. 신규 6·갱신 7. 신규 6: generative-ai-for-beginners(GitHub ⭐115,125·Microsoft 21강 생성형 AI 입문·교육 자산 high) + HF논문 5(RLSVR 2607.23802·N0-VTLA 2607.23782·Meshy-T2 2607.28675·AISPA 2607.28617·QQWorld 2607.28415 — 전량 미래형 ID medium). 갱신 7(전량 기존 페이지): GitHub 4 AI-For-Beginners ⭐50,871→60,032(6만 돌파)·airllm ⭐23,500→26,092·Agent-Reach ⭐63,584→65,181·TencentDB-Agent-Memory ⭐10,488→11,534 / HF모델 3 Unlimited-OCR DL 2.6M 좋아요 3.8k·Qwen3.6-27B-Fable-Fusion DL 1.55M 좋아요 1.38k·Kimi-K3 DL 968k(100만 근접) 좋아요 9.74k(트렌딩 좋아요 1위). GitHub 5·HF모델 3 전량 raw 자동수집 API 수치 반영·실WebFetch 미수행(볼트 시뮬레이션 타임라인 2026-08과 실소스 현재값 모순 회피, 07-30~08-02 배치와 동일 처리). HF논문 5건 전량 미래형 arxiv ID(2607.x)로 원문 초록·수치 재현 불가 → raw 한줄요약 기반 medium, 구체 벤치 수치·저자/소속 미기재(AISPA Stanford도 추정·미확인, 사실확인 원칙). 신규 entity 미생성(HF논문 저자·기관 salience 대비 날조 방지 — Microsoft·Meshy·Moonshot AI 기존 페이지 wikilink만). actionable 2건 추가(Meshy-T2를 TRELLIS.2 3D 백본 스팟체크에 편입[낮음]·RLSVR/AISPA 자기검증·프롬프트 감사 개념 위키/스킬 이식 검토[낮음]). canvas 미갱신(정기 graph 갱신 시 일괄 반영). -->

<!-- 2026-08-02 아침 자동수집 8건(GitHub 5 + HF모델 3, HF논문 0[일요일 데일리 미갱신]) 전체 인제스트 완료 후 삭제. 신규 3·갱신 5. 신규 3(전량 GitHub): TRELLIS.2(⭐10,031·Microsoft 3D 생성 구조화 latent·Python·세부 미검증 medium)·copilot-sdk(⭐10,318·GitHub 공식 Copilot Agent 통합 SDK·Java·API 커버리지 미검증 medium)·reverse-skill(⭐12,270·당일 +1,320 급상승 1위·리버스엔지니어링 스킬 AI 라우팅·PowerShell·개인 프로젝트·화제성 경계 low). 갱신 5(전량 기존 페이지): deer-flow ⭐78,859(+209)·TencentDB-Agent-Memory ⭐10,488(+227·1만 돌파) / HF모델 3 Unlimited-OCR DL 2.54M 좋아요 3.73k·GLM-5.2 DL 2.05M(200만 돌파) 좋아요 4.74k·Qwen3.6-27B-Fable-Fusion DL 1.37M 좋아요 1.26k. GitHub 5·HF모델 3 전량 raw 자동수집 API 수치 반영·실WebFetch 미수행(볼트 시뮬레이션 타임라인 2026-08과 실소스 현재값 모순 회피, 07-30~08-01 배치와 동일 처리). 신규 3건 세부 스펙(TRELLIS.2 아키텍처·copilot-sdk API/언어 커버리지·reverse-skill 라우팅 엔진)·HF 벤치(GLM-5.2 SWE/Terminal·Fable-Fusion ARC-C·Unlimited-OCR ParseBench)는 원문 실검증 전이라 구체 수치 미기재·인용 시 미검증 병기(사실확인 원칙). 신규 entity 미생성(Microsoft 기존 페이지 wikilink만; github/zhaoxuya520/baidu/zai-org는 salience 대비 날조 방지). actionable 2건 추가(TRELLIS.2 오픈 3D 백본 품질 스팟체크[낮음]·스킬 라우팅/에이전트 SDK 임베드 설계 패턴 개념 추출[낮음]). canvas 미갱신(대형 JSON — 정기 graph 갱신 시 일괄 반영). -->

<!-- 2026-08-01 아침 자동수집 8건(GitHub 5 + HF모델 3, HF논문 0[토요일 데일리 미갱신]) 전체 인제스트 완료 후 삭제. 신규 0·갱신 8(전량 기존 페이지): GitHub 5 hermes-agent ⭐223,586·Agent-Reach ⭐63,584·speech-to-speech ⭐9,955(급상승 1위)·jcode ⭐14,760·book-to-skill ⭐14,471 / HF모델 3 Unlimited-OCR DL 2.46M 좋아요 3.68k·Qwen3.6-27B-Fable-Fusion DL 1.17M(100만 돌파) 좋아요 1.17k·Kimi-K3 DL 560k 좋아요 9.35k(트렌딩 좋아요 1위). GitHub 5·HF모델 3 전량 raw 자동수집 API 수치 반영·실WebFetch 미수행(볼트 시뮬레이션 타임라인 2026-08과 실소스 현재값 모순 회피, 07-30 배치와 동일 처리). 자체벤치(Fable-Fusion ARC-C·Kimi-K3 GPQA/BrowseComp·Unlimited-OCR ParseBench)는 인용 시 미검증 병기. 신규 entity·actionable 미생성(전량 기존 항목 유지). HF논문 0: 7-31자 5건(AskChem·Qwen-UI-Agent·Metis·Frontis-MA1·PhiZero)은 7-31 인제스트 완료분이라 중복 재추가 안 함. -->

<!-- 2026-07-31 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제. 신규 6(openwork + HF논문 5: PhiZero·Frontis-MA1·Metis·AskChem·Qwen-UI-Agent) / 갱신 7(ECC ⭐236,434·chrome-devtools-mcp ⭐48,211·last30days-skill ⭐55,775·speech-to-speech ⭐9,425·GLM-5.2 DL 1.53M·Unlimited-OCR DL 2.6M 좋아요 3.61k·Qwen3.6-27B-Fable-Fusion DL 956k 좋아요 1.06k). raw "GitHub 5"(openwork·ECC·speech-to-speech·last30days-skill·chrome-devtools-mcp) 중 openwork만 신규·나머지 4 기존 → 갱신. "HF모델 3"(Unlimited-OCR·GLM-5.2·Qwen3.6-Fable-Fusion)은 전부 기존 → 갱신. "HF논문 5"만 신규 페이지. GitHub 5건 전량 WebFetch 실검증(스타·라이선스·성격 raw와 일치 → high, chrome-devtools-mcp Apache-2.0 확정·ECC MIT/TS 재확인). HF모델 3건은 raw 자동수집 API 수치 반영(볼트 시뮬레이션 타임라인 유지 위해 HF 실WebFetch 미수행). HF논문 5건은 미래형 arxiv ID(2607.x)로 원문 초록·수치 재현 불가 → raw 한줄요약 기반 medium, 구체 벤치 수치 미기재(사실확인 원칙). 신규 entity 미생성(different-ai·논문 저자/기관 salience 대비 날조 방지 — Alibaba·Zhipu-AI·Baidu·huggingface 기존 페이지 wikilink만). actionable 2건 추가(openwork 워크플로 공유 포맷·라이선스 확인[낮음]·Metis+AskChem 메모리모델/클레임구조화 LLM-Wiki 개념이식 검토[낮음]). -->

<!-- 2026-07-30 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제. 신규 5(TurboVLA·HumanCLAW·DecoEvo·CLBench-V·CoRT — 전량 HF논문) / 갱신 8(ECC ⭐235,876·VibeVoice ⭐51,534·airi ⭐45,655·open-code-review ⭐16,303·speech-to-speech ⭐8,141·Unlimited-OCR DL 2.69M 좋아요 3.54k·Kimi-K3 좋아요 8.8k·Qwen3.6-27B-Fable-Fusion 좋아요 974). raw "GitHub 5"(ECC·VibeVoice·airi·open-code-review·speech-to-speech)·"HF모델 3"(Unlimited-OCR·Qwen-Fable·Kimi-K3)은 전부 기존 페이지 → 갱신. "HF논문 5"만 신규 페이지. 갱신 8건은 raw 자동수집 API 실검증 수치(GitHub 스타·HF DL/좋아요)로 반영. 신규 5건은 미래형 arxiv ID(2607.x)로 원문 초록·수치 재현 불가 → raw 한줄요약 기반 medium, 구체 벤치 수치 미기재(사실확인 원칙). 신규 entity 미생성(논문 저자·기관 미상, salience 대비 날조 방지 — Microsoft·Moonshot AI·Baidu·Alibaba·huggingface·moeru-ai·affaan-m 기존 페이지 wikilink만). actionable 2건 추가(로컬 음성 스택 3종 묶음 평가[중간]·rubric-guided RL 위키 자기검증 개념검토[낮음]). -->

<!-- 2026-07-29 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제. 신규 9(ECC·DocsGPT·OpenSpace·agent-governance-toolkit·HiFi-UMI·RARG·ReDesign·InMind·Mage-VL) / 갱신 4(OpenViking ⭐26,604→27,604·Laguna-S-2.1 DL 3,056→67,286·Solar-Open2-250B DL 2,784→4,804·Kimi-K3 좋아요 7.21k→8,320). 13건 전량 WebFetch 실검증: GitHub 4 스타·라이선스·기능 high(ECC 235k 규모 이례적·내부수치 자체표기로 실사용 검증 별도), HF논문 5 초록·구체수치 실검증 medium(RARG·InMind·ReDesign·Mage-VL 저자/기관 확보, 미래형 2607.x ID·원문 재현 미검증), HF모델 갱신 3 모델카드 실측. 신규 entity 미생성(arc53·HKUDS·poolside·affaan-m salience 대비 날조 방지 — Microsoft·Tencent·KAIST AI·Volcengine·Upstage·Moonshot AI 기존 페이지 wikilink만). concept [[에이전트-메모리-레이어]]에 InMind '검색 사각지대' 추가. -->

<!-- 2026-07-28 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제. 신규 6(airi·Kimi-K3·JarvisHub·Progress-Reward-Modeling·MAPD·StateAct) / 갱신 6(Kronos ⭐34,707·open-code-review ⭐15,242·claude-video ⭐11,484·last30days-skill ⭐54,415·Unlimited-OCR DL 2.69M·라이선스MIT확인·Qwen3.6-27B-Fable-Fusion DL 737k) / entity 1(Moonshot AI). 13건 전량 WebFetch 실검증: GitHub 스타·기능 high, HF논문 4 초록·저자·기관·구체수치 실검증 medium(미래형 2607.x ID·원문 재현 미검증), Kimi-K3 모델카드·초록 medium(자체벤치·Claude Fable 5 열위 자인), HF모델 갱신 2 모델카드 실확인. 신규 entity Moonshot AI만 생성(Kimi K2.6/K2.7/K3 허브·프론티어 랩 salience — Salesforce·baidu·moeru-ai·Northwestern·BIT는 wikilink만). -->

<!-- 2026-07-11 자동수집 13건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-12 JEPA·월드모델 심층분석 인제스트 완료 후 정리 -->
<!-- 2026-07-12 아침 자동수집 11건 처리 완료 후 삭제 -->
<!-- 2026-07-13 아침 자동수집 13건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-14 아침 자동수집 13건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-15 아침 자동수집 13건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-16 아침 자동수집 13건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-17 아침 자동수집 13건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-18 아침 자동수집 8건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-19 아침 자동수집 5건 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-20 아침 자동수집 10건(GitHub 5 + HF논문 5) 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-21 아침 자동수집 11건(GitHub 5 + HF논문 5 + HF모델 1) 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-22 아침 자동수집 12건(GitHub 5 + HF논문 5 + HF모델 2) 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-25 아침 자동수집 13건(GitHub 5 + HF논문 5 + HF모델 3) 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-26 아침 자동수집 7건(GitHub 5 + HF모델 2) 전체 인제스트 완료 후 삭제 -->
<!-- 2026-07-27 아침 자동수집 11건(GitHub 5 + HF논문 5 + HF모델 1) 전체 인제스트 완료 후 삭제 -->

---
