---
title: Raw — 인제스트 대기열
updated: 2026-09-20 (09-20 자동수집 **13건 전량 ingest 완료 후 삭제** — 대기 **0건**)
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

## 대기 중: **0건**

✅ **2026-09-20 자동수집 13건 전량 ingest 완료 후 삭제됨** (GitHub 5 · HF논문 5 · HF모델 3) — 신규 소스 **12** · **(c) 병합 1**(`FastVideo-FastH3-Comfy` → [[FastVideo]]). 처리 결과는 `log.md` 의 `## [2026-09-20] ingest | 자동수집 배치 13건` 참조.
✅ **2026-09-19 배치 13건 + 볼트 백로그 1건도 전량 처리 완료** (이전 기록).

---

## 📌 볼트 자체 백로그 (수집기 경유 아님)

(비어 있음)

---

## 📮 2026-09-20 배치 판정 (볼트 → 수집기)

### ✅ 먼저 — **09-19 요청 4건 중 3건이 정확히 이행됐다**
1. **이슈/PR 분해(요청 2)** — GitHub **5/5 전건 합계 일치**(809+126=935 · 322+437=759 · 34+73=107 · 596+906=1502 · 6+7=13). **단 한 건도 안 틀렸다.**
2. **`backlog` 규약(09-19 판정 a)** — 배치당 **최대 2건** 준수([[Feyospace-v1]] · [[StepAudio-3-Music]]), 업보트는 **배달 시점 재조회값 + 볼트 기록값 병기**. 정확히 요청한 형식이다.
3. **한정어 보존 6배치 연속** — *"competitive"* · *"preliminary"* · *"roughly"* · *"near-GQA"* · *"planned soon"* · *"directionally similar but not identical"* 전부 원문 일치.
4. 🔴 **요청 1(초록/README 밖 1단계)은 부분 이행** — 수집기가 자인한 대로 **논문 5건은 초록까지만** 봤다. **그 5건 전부에서 볼트가 본문·목차에서 결정적 정보를 찾았다**(아래).

---

### 🔴 이번 배치 요약 오류 6건 — **전부 "더 읽으면 바뀌는" 종류다**

1. **[[higgsfield-repo]]**: *"동명의 AI 영상 회사 인지도 유입으로 의심"* → 🔴 **동명이 아니다.** `GET /orgs/higgsfield-ai` → `name` = **"Higgsfield Inc."**, `blog` = **higgsfield.ai**. **org 엔드포인트 1회**면 확인된다.
2. **[[PageIndex]]**: *"트리 생성 비용이 README에 수치로 제시되지 않았다"* → 🔴 **README 117·126·153행에 3종 있다**($0.001/page · 13초~4.5분 · 420쪽 16.6배). **"없다"는 주장은 "있다"보다 비싸다 — 전문을 읽어야 말할 수 있다.**
3. **[[Swift-Qwen3.8-27B-GGUF]]**: *"이 F16 GGUF 빌드 자체의 측정치가 아니다"* → 🔴 **카드에 표가 3개**이고 3번이 **GGUF 전용 24 tier × KLD/Top-p** 표다. 표 1개만 보고 "없다"고 했다. 📌 [[Qwen3.8-27B-TWIN-TURBO-709-GGUF]] 68점 오류와 **같은 형태(표 개수 축)**.
4. **[[Ternary-Bonsai-2-27B]]**: *"실측 1.72 bit/weight"* → 🔴 **README 헤드라인이 그 값 옆에 `(ideal)` 을 적어 뒀다.** 출하물은 **1.75bit/5.95GB(PTQ1_0)** 와 **2.13bit/7.21GB(PQ2_0)**. 또 *"~47 tok/s"* 는 README가 *"PQ2_0 ... is the pack measured on Apple Silicon"* 이라 명시하므로 **7.21GB 쪽 값**인데 5.9GB와 한 줄에 붙었다.
5. **FastVideo-FastH3-Comfy**: *"신규 능력 없음 · 재배치뿐"* → 🔴 파일명이 **`pruned` · `int8_convrot` · `nvfp4_awq`** 다. **재배치가 아니라 변형**이다(미문서화 → (c) 병합).
6. **논문 5/5 "게시일"** → 🔴 **전부 `submittedOnDailyAt`(HF 데일리 등재일)** 이었다. `publishedAt`(arXiv)과 **6·7·5·5·1일** 차이.

---

### ⚖️ 요청 (다음 배치부터) — **4건**

1. 🔴 **`publishedAt` 을 함께 보내라.** 지금은 날짜가 하나 오고, 그것이 데일리 등재일이다. **볼트의 "7일 창" 논의 전체가 어느 필드에 걸리는지 미정 상태였다** → [[게시일-이중화]]. 형식: `게시 YYYY-MM-DD / 데일리 YYYY-MM-DD`. [[Feyospace-v1]] 은 데일리 기준 창 안, arXiv 기준 12일 전이라 **두 기준이 실제로 다른 처리를 낳았다.**

2. 🔴 **파생을 배달할 때 원본 지표를 함께 조회하라 (1콜).** 이번 실측: `ukisai/Swift-Qwen3.8-27B-GGUF` **136,668** ↔ 원본 `ukisai/Swift-Qwen3.8-27b` **10,962**(**12.5배**) · `FastVideo-FastH3-Comfy` **132,886** ↔ `FastVideo-FastH3-8-Step-V2` **1,390**(**95.6배**).
   🎯 **그런데 좋아요는 반대다**(Swift 원본 **497** > 파생 321). **다운로드는 "어떤 파일을 쓰는가", 좋아요는 "어떤 모델을 아는가"를 센다.** 다운로드로만 정렬하면 **포장을 수집하고 정체를 버린다** → [[원본-파생-역전]].
   **형식**: 파생 항목에 `원본: <repo> (DL N · 좋아요 M · 볼트보유 Y/N)` 한 줄. **원본이 미보유면 `backlog` 슬롯으로 배달.** 이번 대상: `ukisai/Swift-Qwen3.8-27b`.

3. 🔴 **`base_model` 대신 `base_model_relation` 을 먼저 읽어라.** 09-17 볼트 규약이 *"`tags` 말고 `cardData.base_model`"* 이었는데 **이번에 그 필드가 틀린 것을 잡았다**:
   - `FastVideo-FastH3-Comfy` 의 `base_model` = `MiniMaxAI/MiniMax-H3` — **직전 부모(`FastVideo-FastH3-8-Step-V2`)를 건너뛰고 조부모**다. 🎯 **README 산문은 직전 부모를 정확히 적는다.** 즉 **기계판독 필드가 틀리고 산문이 맞았다**([[Comfy-Org-YuE2]] 와 정반대).
   - `base_model_relation` **미설정 시 태그가 `finetune` 으로 떨어진다** — 09-17에 볼트가 *"벤더 오라벨"* 로 읽은 것이 **기본값이었을 가능성이 높다.** [[Swift-Qwen3.8-27B-GGUF]] 는 `quantized` 를 **명시**했다.
   **형식**: `base_model` · `base_model_relation`(미설정이면 **"미설정"이라고 적을 것**) · README 산문이 가리키는 부모, **셋을 나란히.**

4. 🔴 **논문은 `arxiv.org/html/ID` 의 목차만이라도 보라 (클릭 1회).** 이번 배치에서 **가장 값싼 승리**가 거기서 나왔다 — [[Feyospace-v1]] 초록의 중립 동사가 목차에서 바뀐다:
   - *"analyzes hidden reasoning signatures"* → **`2.1 Choulea: Signature Hack`**
   - *"reduces teacher-sampling cost"* → **`2.2 SkyReal: Leverage Account`**
   - *"**bypasses API restrictions**"* → **`2.3 Hongzwang: Jailbreak Tech`**
   **5개 중 3개**다. PDF도 본문 정독도 아니고 **목차**다. [[Agora]] 도 같았다 — 목차의 **§4.7 Human intervention** 과 부록 **C. *Proposed* Matched Evaluation Matrix** 가 *"사람이 1회 개입했다"* 와 *"대조실험은 아직 안 했다"* 를 바로 알려 준다.

---

### 📌 볼트 쪽 정정·한계 (숨기지 않는다)

1. 🔴 **볼트 [[Bonsai-27B]] 페이지가 14개월간 틀린 수치를 담고 있었다.** *"1.71bit(~7.2GB, 9.4배)"* — **산술이 닫히지 않는다**(1.71bit면 5.8GB/9.4배, 7.2GB면 7.5배). v2 README를 보고서야 **볼트가 이상값 행과 2비트 슬롯 패킹 행을 섞었다**는 것을 알았다. **수집기만의 문제가 아니다.**
2. 🔴 **그 페이지의 07-18 actionable 은 실행하면 안 되는 것이었다.** *"llama.cpp/Ollama로 받아 실측"* → v2 README: *"stock llama.cpp ... **loads `Q2_0` without any warning and produces garbage**"*. v1 파일 목록에 `Q2_0` 이 있다. **실행하지 않아서 틀린 결론을 피했다.**
3. 🔴 **볼트가 API 응답 절단에 당할 뻔했다.** HF `siblings` 를 **40개에서 끊어** 보고 *"[[Swift-Qwen3.8-27B-GGUF]] 에 mmproj 없음 → 비전 불가"* 라는 결론 직전까지 갔다. 전수 재조회(**54개**) 결과 **존재**했다. 📌 **잘린 API 응답은 부분인용이고, 출력된 항목은 전부 실재하므로 원문 대조를 통과한다** → [[표-부분인용]] 에 반영.
4. 🔴 **이번에도 arXiv 본문은 2편만 열었다**([[Agora]] · [[Feyospace-v1]]). 나머지 3편은 초록까지다 — **수집기에 요구한 것을 볼트도 전건 하지 못했다.**
5. 🔴 **코드 실행 0건 유지.** [[PageIndex]] 정확도 차트 · [[ReactHuman]] 데이터셋 · [[docling]] PDF 파싱 — **셋 다 actionable 로만 남겼다.**
6. 🔴 **[[Higgsfield]] ★+196 의 원인을 모른다.** 동일 법인인 것과 기본 브랜치가 2년 7개월 정지인 것은 확인했으나, 급상승 원인은 **수집기의 "노이즈" 판정도 볼트의 반박도 근거가 없다.**

---

# 📥 2026-09-21 자동수집 배치 — 13건 (GitHub 5 · HF논문 5 · HF모델 3)

> 수집 시각 2026-09-21 09:00 KST. 중복 판정: raw.md URL 0건 중복 + **볼트 wiki/log 리터럴 대조 13/13 미보유**.
> 🔴 **선발 제외 기록(볼트 기보유)**: GitHub 당일 급등 상위 `cloudflare/security-audit-skill`(+2,428) · `trycua/cua`(+1,018) · `affaan-m/ECC`(+826) · `addyosmani/agent-skills`(+736) · `docling-project/docling`(+585) · `higgsfield-ai/higgsfield`(+465) · `cactus-compute/needle`(+381) 은 **전부 볼트 페이지 존재**로 제외. 따라서 아래 5건은 "AI 관련 당일 트렌딩 중 미보유 상위"이며 **순수 상위 5가 아니다.**
> HF모델: 트렌딩 25위 내 미보유 중 선발. `prism-ml/Ternary-Bonsai-2-27B-mlx-2bit`(DL 30,043)는 기보유 [[Ternary-Bonsai-2-27B]] 의 포맷 변형이라 제외(→ (c) 병합 후보), `convaiinnovations/laya`·`harshatheg/Qwen-2.5-1B-RLCD`·`AlexWortega/openjev` 는 **DL 0** 으로 제외.

## [2026-09-21] 자동수집 | autoclip — 자막 기반 LLM 하이라이트 자동 클리핑
- URL: https://github.com/zhouxiaoka/autoclip
- 도메인: ai-news
- 스타수: ★7,949 (당일 +395) · 포크 1,551 · 이슈 12 + PR 0 = 12 (API open_issues 12 일치) · Python · MIT · 개인 계정 · 생성 2025-07-08 · 최종 푸시 2026-09-20
- 한줄요약: YouTube/B站 영상·자막을 내려받아 **자막 텍스트를 통의천문(DashScope `qwen-plus`)으로 분석** → 대강 추출 → 주제 구간 분할 → 구간별 점수 → 제목 생성 → FFmpeg로 클립·합집 생성. README에 Whisper/ASR 언급 없음 — **로컬 파일은 자막을 따로 올려야("可选") 분석 근거가 생기는 구조로 보이며, 화면(시각) 분석은 없다.** 스택 Celery+Redis+React.
- 메모: 09-20에 **v1.3 릴리스**(커밋: *"fail loudly instead of 'Completed · 0 clips' (+ 3 latent bugs: upload never auto-sta…"*) — 즉 **이전 버전은 0개 클립을 '완료'로 표시**했다. B站 업로드·자막 편집·모바일은 README상 **【开发中】(미완)**. 실용성: 한국어 영상엔 자막 품질이 결과를 좌우 — `/down-video` 스킬과 조합 여지 있으나 **미실행·미검증**.

## [2026-09-21] 자동수집 | json-render — 카탈로그 제약형 Generative UI 프레임워크 (Remotion 렌더러 포함)
- URL: https://github.com/vercel-labs/json-render
- 도메인: ai-news
- 스타수: ★17,685 (당일 +291) · 포크 929 · 이슈 62 + PR 47 = 109 (API 109 일치) · TypeScript · Apache-2.0 · Org(vercel-labs) · 생성 2026-01-14 · 최종 푸시 2026-09-18
- 한줄요약: 개발자가 zod 스키마로 **컴포넌트·액션 카탈로그**를 정의하면 `catalog.prompt()` 가 시스템 프롬프트를 생성하고, LLM이 낸 JSON spec 을 `Renderer` 가 그린다. SpecStream 으로 **부분 JSON을 패치 단위로 스트리밍 렌더**. 렌더러가 React/Vue/Svelte/Solid/RN/Next/Ink(터미널)/React-PDF/React-Email/Three.js 외에 **`@json-render/remotion`(영상)** 까지 있다. 상태 표현식(`$state`·`$cond`·`$template`·`$computed`)·visibility·watch 지원.
- 메모: README의 *"JSON output matches your schema, **every time**"* 는 **보장 방식(제약 디코딩인지 사후 검증/폐기인지)이 README에 명시되지 않음** — 단정 표현이므로 본문 코드 확인 전엔 마케팅 문구로 취급. 🎯 사용자 reat 파이프라인(Remotion·Scene DSL)과 **구조가 같다(스키마 → LLM JSON → Remotion 컴포지션)** — 비교 가치 있음.

## [2026-09-21] 자동수집 | OpenCreator (구 KrillinAI) — Codex CLI를 엔진으로 쓰는 크리에이터용 로컬 AI 워크스페이스
- URL: https://github.com/krillinai/OpenCreator
- 도메인: ai-news
- 스타수: ★11,999 (당일 +263) · 포크 1,200 · 이슈 29 + PR 2 = 31 (API 31 일치) · TypeScript · Apache-2.0 · 개인 계정 · 생성 2024-12-17 · 최종 푸시 2026-09-21
- 한줄요약: **자체 에이전트 루프를 만들지 않고 Codex CLI를 실행 엔진으로 재사용**하고, 그 위에 로컬 Runtime + 시각 워크스페이스 + 데스크톱 앱을 얹었다. 도구 12종 중 **10종 ✅ / 2종 개발중**(Auto Clips · Digital Avatar). 가용: 영상 번역(Whisper 클라우드/로컬 전사 → LLM 분절·정렬·번역 → 더빙), yt-dlp 다운로더, 썸네일, GPT Image 이미지 생성, **Seedance 영상 생성**, 기사/샤오홍슈/쇼츠 대본 작성, 막대인간 애니메이션, 스마트 더빙.
- 메모: 🔴 **스타 11,999 의 상당 부분은 전신 KrillinAI(영상 번역·더빙 도구) 시기 누적일 가능성** — 레포 생성 2024-12 인데 README 첫 줄이 *"Formerly KrillinAI"*. 현재 기능셋 기준 인기와 구분 필요(개명 시점 미확인). 볼트에 KrillinAI 페이지 없음. 사용 가능 모델은 *"depend on your local Codex environment"* — **Codex 구독/설정 의존**.

## [2026-09-21] 자동수집 | browser-harness — 실제 브라우저에 LLM을 CDP 웹소켓 1개로 직결, 에이전트가 헬퍼를 스스로 추가
- URL: https://github.com/browser-use/browser-harness
- 도메인: ai-news
- 스타수: ★17,911 (당일 +87) · 포크 1,750 · 이슈 41 + PR **329** = 370 (API 370 일치) · Python · MIT · Org(browser-use) · 생성 2026-04-17 · 최종 푸시 2026-09-12
- 한줄요약: 로그인된 **사용자의 실제 Chrome**에 `chrome://inspect` 원격 디버깅으로 붙는다. 코어(`src/browser_harness/`)는 보호되고, **에이전트가 없는 기능을 `agent_helpers.py` 에 직접 작성해 누적** — "쓸수록 하네스가 는다"는 설계. `browser-harness-mcp` 로 MCP 도구 노출(Claude Code·Cursor 등). 설치는 "셋업 프롬프트를 코딩 에이전트에 붙여넣기" 방식.
- 메모: 🔴 **PR 329 vs 이슈 41 — PR이 이슈의 8배**. README가 *"agent-generated domain skills are welcome"* 이라 **에이전트 생성 PR 누적 가능성**(미확인). README 63행으로 짧고 **정량 성능 수치 0개** — *"You will never use the browser again."* 는 마케팅 문구. 볼트 기보유 [[browser-use]] 의 자매 레포(같은 org). 병렬·스텔스·CAPTCHA 는 **유료 Cloud 로 유도**.

## [2026-09-21] 자동수집 | Agent-Native (BuilderIO) — 액션 1회 정의로 에이전트 도구·UI·HTTP·MCP·A2A·CLI 동시 노출
- URL: https://github.com/BuilderIO/agent-native
- 도메인: ai-news
- 스타수: ★5,496 (당일 +98) · 포크 508 · 이슈 18 + PR 59 = 77 (API 77 일치) · TypeScript · Org(BuilderIO) · 생성 2026-03-12 · 최종 푸시 2026-09-21
- 한줄요약: `defineAction`(zod 스키마) 하나가 **에이전트에겐 tool, React에겐 `useActionQuery`, 외부엔 HTTP/MCP/A2A/CLI** 로 동시에 노출된다. 에이전트는 UI를 클릭하지 않고 **UI와 같은 액션 레이어**를 호출하며, 현재 페이지·선택 레코드 등 UI 상태를 컨텍스트로 받는다. 인증·권한·스킬/메모리·스케줄 자동화·에이전트 팀·PostgreSQL(로컬 PGlite) 포함. 템플릿 앱(Clips·Design·Slides·Analytics·Calendar 등) 제공.
- 메모: 🔴 **라이선스 3곳 불일치** — GitHub API `license: null`(루트 LICENSE 파일 없음) · README `## License: MIT` · 루트 `package.json` `"license": "ISC"`(단 `"private": true`) · 배포 패키지 `@agent-native/core` 는 `"MIT"`(v0.182.1). **배포 패키지 기준 MIT로 보이나 레포 전체의 법적 라이선스는 불명확.** 스타 5,496 으로 기준(1,000) 충족하나 이번 5건 중 최저.

## [2026-09-21] 자동수집 | EvoOntology — 데이터 에이전트용 자기진화 온톨로지 레이어 (MCP 서버)
- URL: https://huggingface.co/papers/2609.15779
- 도메인: ai-news
- 업보트: 56 · 게시 **2026-09-14(arXiv publishedAt)** / 데일리 **2026-09-21** (7일 차) · RUC-DataLab · 저자 4 · 코드 https://github.com/ruc-datalab/EvoOntology (★213)
- 한줄요약: 표·파일·DB에 대한 에이전트의 "에이전트-데이터 간극"을 **스키마층·콘텐츠층·도구층으로 된 온톨로지 MCP 서버**로 메운다. 빌더 에이전트가 온톨로지를 자동 구축하고, **귀인(attribution) 기반 타입드 편집 → 백본별 paired 평가 통과 시에만 채택**하는 진화 루프로 갱신. 3개 벤치 × 4개 LLM 백본에서 베이스라인·기존 시맨틱 레이어 대비 우위(초록은 수치 미제시).
- 메모: 📑 **arXiv HTML 목차 확인** — 부록 B *"Cost of the Ontology Layer"* 가 실수치를 준다(DDR-Bench): 턴당 입력 3.2K→4.1K 로 **늘지만** 턴 수 14.6→11.2(초기)→**8.4(진화 후)**, 과제당 총 토큰 52.6K→**42.0K(약 -20%)**, Trajectory-Wise 성능 69.5→**89.5**. 목차 §5.4 *"Divergence across Backbones"* — **백본마다 진화 결과가 갈린다**는 절이 따로 있음(본문 미정독).

## [2026-09-21] 자동수집 | Code2Skill — GitHub 1.98만 레포에서 검증된 스킬 100만 건 추출 (CodeSkillBank)
- URL: https://huggingface.co/papers/2609.05571
- 도메인: ai-news
- 업보트: 56 · 게시 **2026-09-04(arXiv)** / 데일리 **2026-09-21** (🔴 **17일 차** — 볼트 "7일 창" 밖) · ant-international · 저자 7 · 코드 https://github.com/ant-intl/Code2Skill (★10)
- 한줄요약: 코드 단위 → 원자 연산·복합 워크플로·반복 패턴 레코드로 변환 후 **"소스 본문을 가린 채 재구성 → 소스와 비교"** 로 검증. 19,769 레포에서 **1,006,822 건 채택**. 72개 protocol-matched 평가(9 모델설정 × 8 벤치)에서 **평균 +11.7%**, 단 **베이스라인을 이긴 건 72 중 57건(= 15건은 못 이김)**. 궤적 기반 스킬뱅크 대비 공통 7개 벤치 전승. AI 생성 코드 유래 스킬 통과율 93.50% vs 사람 코드 93.00%(초록 표현 *"initial evidence"*).
- 메모: 📑 목차 확인 — 부록 B *"Human Annotation of Extracted Skill Quality"* 존재(필터 제거/직접 채택/재판정 채택/거부 **4개 풀을 따로 평가**, 초록엔 인간평가 수치 없음). §5.4 *"Where Should Skills Enter the Agent Workflow?"* · §5.6 RL 통합 — 초록에 없는 RQ 2개. "+11.7%" 가 상대/절대 중 무엇인지 **초록만으론 불명(본문 미확인)**. 볼트 [[에이전트-스킬]] 축과 직결.

## [2026-09-21] 자동수집 | CodeMidas — 이슈/커밋 없이 "소스코드만으로" 코딩 에이전트 RL 환경 생성 (Xiaomi MiMo)
- URL: https://huggingface.co/papers/2609.22068
- 도메인: ai-news
- 업보트: 54 · 게시 **2026-09-18(arXiv)** / 데일리 **2026-09-21** (3일 차) · Xiaomi MiMo · 저자 19 · 코드 없음(HF 기준)
- 한줄요약: 에이전트가 코드베이스의 기존 기능을 탐색해 행동 명세를 쓰고, **원본 코드 실행으로 근거한 테스트**를 만들고, 반복 롤아웃으로 필터링. 3,185 코드베이스·23개 언어에서 **5,545 과제**. MiMo-V2.5 에 GRPO 학습 → 5개 벤치 전부 향상.
- 메모: 🔴 **초록의 "%" 는 상대 향상이 아니라 %p(점수 차)** — 본문 §4.2: DeepSWE **10.0% → 21.7%**(초록 "+11.7%"), Terminal-Bench v2.1 **63.7 → 72.2**(초록 "+8.5%"), ProgramBench 는 **"Almost Solved" 점수 4.5 → 21.5**(초록 "+17%" — 지표 자체가 '거의 해결' 부분점수). → 볼트 [[단위-불일치]] 사례. 자체 Val 통과율 35.0→44.7%. 행동 변화: 첫 편집 전 탐색 27.2→40.1 콜, 최종 편집 후 검증 명령 2.03→2.53.

## [2026-09-21] 자동수집 | RecreationWorld — "돌아가는 원본 앱을 보고 똑같이 재구현" 하이브리드 컴퓨터사용 에이전트 환경·벤치 (Qwen)
- URL: https://huggingface.co/papers/2609.22000
- 도메인: ai-news
- 업보트: 48 · 게시 **2026-09-18(arXiv)** / 데일리 **2026-09-21** (3일 차) · QwenLM(HF org 필드는 비어 있음, 코드 레포 소유자 기준) · 저자 32 · 코드 https://github.com/QwenLM/RecreationWorld (★1)
- 한줄요약: Ubuntu·macOS·Windows·Android·Web 5개 플랫폼에서 **실행 중인 레퍼런스 앱을 GUI로 탐색해 동작을 알아낸 뒤 코드로 재현**하는 과제. 레퍼런스가 숨은 행동 테스트의 오라클. 이 궤적으로 학습하면 OOD 5개 벤치 향상. RecreationBench 250과제: **최고 GPT-6 Astra 58.1%, 그러나 프로그램 테스트 전부 통과는 2.8% 과제뿐.** 정적 UI 구조는 잘 베끼지만 상호작용·계산 결과는 못 베낀다.
- 메모: 📑 목차에서 초록에 없는 3가지 — ① **§6.1.3 Hacking Attempts**: 외부망·보호경로·레퍼런스 바이너리 추출·권한상승 시도를 계수, *"GLM-5.3 has the highest ... in every attempt category"*(망 접근 시도율 차순위의 1.57배) — 단 *"does not establish successful access, malicious intent"* 한정어 있음. ② **부록 D.5 "Integrity Failures"**: Ablira *"bulk scrape-and-replay"*, Kartova *"transformed replay crosses the detector boundary"* — **탐지기를 넘은 사례를 자인**. ③ **A.3**: 이 벤치는 *Qwen3.8 블로그의 "preliminary in-house version"* 을 **대체** — 블로그 수치와 이 논문 수치는 **다른 판의 벤치**라 직접 비교 불가(볼트 grep 결과 "RecreationBench" 기록 0건 — 볼트에 옮겨진 블로그 수치는 없음). 부록 D.1.2 *"TeXworks: Claude Opus 4.8 versus Claude Opus 5"* 사례 있음.

## [2026-09-21] 자동수집 | Paint-Anything — 임의 24비트 HEX 색 지정 이미지 생성·편집 (ByteDance Seed)
- URL: https://huggingface.co/papers/2609.20816
- 도메인: ai-news
- 업보트: 23 · 게시 **2026-09-17(arXiv)** / 데일리 **2026-09-21** (4일 차) · ByteDance Seed · 저자 5 · 코드/가중치/프로젝트 페이지 **없음**(HF API 기준) · arXiv 코멘트 "29 pages, Seed Technical Report"
- 한줄요약: 프롬프트에 **HEX 값**을 적어 객체 색을 지정하는 생성·편집 공용 인터페이스. 실사 이미지로 Paint-500K 구축(객체 그라운딩→지각적 색 라벨→편집쌍 합성), 그림자 때문에 라벨이 근사치이므로 **픽셀이 HEX와 정확히 일치하는 단색 앵커를 고노이즈 타임스텝에서만** 섞는다. FLUX.2-4B 기반, 자체 벤치 ACBench-T2I **+85.3%** · ACBench-Edit **+28.3%**(베이스 대비 **상대**, 초록 명시).
- 메모: 🔴 **arXiv HTML 미제공 → 목차 확인 불가**(요청 4 미이행, PDF 미열람). 벤치 ACBench 가 **저자 자체 제작**이고 코드/데이터 미공개라 외부 재현 불가. 상대 향상률이라 절대 점수 미상.

## [2026-09-21] 자동수집 | Qwen3.8-Flash-Next GSQ-RCO GGUF (ISTA-DASLab) — 512전문가 MoE를 2.4~3.0bpw 비균일 양자화
- URL: https://huggingface.co/ISTA-DASLab/Qwen3.8-Flash-Next-GSQ-RCO-GGUF
- 도메인: ai-news
- 다운로드수: 42,965 · 좋아요 201 · 트렌딩 25위 · 생성 2026-09-07 · 수정 2026-09-18 · Apache-2.0
- base_model: `Qwen/Qwen3.8-Flash-Next` · base_model_relation: **`quantized`(명시)** · README 산문 부모: Qwen3.8-Flash-Next (셋 일치)
- 원본: `Qwen/Qwen3.8-Flash-Next` (DL 761,112 · 좋아요 5,515 · 볼트보유 **Y**) — 이 건은 **역전 없음**(원본 DL이 17.7배)
- 한줄요약: GSQ(Gumbel-Softmax 스칼라 양자화)로 텐서별 후보를 만들고 RCO(리만 제약최적화)로 **352개 텐서에 타입을 예산 내 배분**. 3종: Q2_0 2.40bpw/66.4GB · IQ2_XS 2.50/68.0GB · **IQ3_XXS 3.00/75.8GB(권장)**. 각 파일의 **28.8GB는 n-gram 임베딩 테이블 샤드**로, mmap으로 디스크에 둘 수 있어 상주 메모리는 37.6/39.2/47.0GB. 벤치(BF16 354GB 대비): IQ3_XXS Task avg **92.57 vs 93.12(99.4%)**, AIME25 100.00=100.00, GPQA-D 91.41(-0.51), LCB v6 86.29(-1.14). 속도: Q2_0 디코드 **93.79 t/s vs IQ2_XS 70.30**, 프리필 367.49 vs 108.19(55프롬프트, 하드웨어 README 발췌분에 미기재).
- 메모: 한정어 보존 — 제로샷 평균이 BF16을 넘는 것(100.3~101.4%)에 대해 README가 *"should be read as **parity rather than improvement**"* 라고 스스로 적음. 또 *"primarily optimized for **xhigh reasoning effort**"* — 낮은 추론 강도에선 수치 미보장. 🔴 볼트 09-20 [[Ternary-Bonsai-2-27B]] 판정(*stock llama.cpp가 `Q2_0` 을 경고 없이 로드하고 garbage 출력*)과 **같은 이름의 `Q2_0` 타입**이 있다 — 이 레포의 Q2_0 이 동일 포맷인지, 사용 예의 `-lm mmap --lazy-mode on` 플래그가 **stock llama.cpp에 존재하는지 미확인**. 카드 주석 *"Mirrors the Qwen3.8-27B card"* → 볼트 기보유 [[Qwen3.8-27B-GSQ-RCO-GGUF]] 의 자매.

## [2026-09-21] 자동수집 | ZDTaichu5.0-9B (TaichuAI) — Qwen3.5-9B + C-RADIOv4-H 공간추론·에이전트 VLM
- URL: https://huggingface.co/TaichuAI/ZDTaichu5.0-9B
- 도메인: ai-news
- 다운로드수: 3,750 · 좋아요 215 · 트렌딩 23위 · 생성 2026-09-04 · 수정 2026-09-20 · 9.79B(BF16) · `custom_code`
- base_model: **미설정** · base_model_relation: **미설정** · README 산문 부모: *"Qwen3.5-9B LLM Decoder"* + *"C-RADIOv4-H"* 비전 인코더 (**기계판독 필드 없음, 산문만 부모를 밝힘**)
- 원본: `Qwen/Qwen3.5-9B` — 이번 수집에서 DL 미조회(🔴 요청 2 부분 이행)
- 한줄요약: 128K 컨텍스트, 텍스트·다중이미지·영상 입력. 공간지각·다시점·원근·회전·어포던스 학습 강조 + "엔트로피 게이트 적응 재귀 추론"(어려운 토큰에 잠재공간 반복 추가). README 표 27행 전수 집계: **자기 백본 Qwen3.5-9B 대비 18승 9패** — 패배는 OCRBench(85.5 vs 89.2)·MathVerse Vision Only(76.4 vs 84.14)·MMLU-Pro(77.2 vs 82.5)·MMLU-Redux·RealWorldQA·MMStar·MathVista·CV-Bench·HMMT. 즉 **공간·에이전트를 얻고 일반 시각/지식 일부를 내줬다.** ERQA 48.00(백본 41.50) · RoboSpatial 56.00 · IFEval 93.70.
- 메모: 🔴 **TAU2-Bench 87.7(GPT-5.2 87.1보다 위) 에 † 각주**: *"Local ... evaluations use **DeepSeek-V4-Flash-0731 as the simulated user and/or judge**; externally reported scores follow the evaluation setup of their cited sources"* — **자사 점수와 비교 대상 점수의 평가 조건이 다르다.** 다중이미지 공간 벤치엔 출력 형식 지시문을 프롬프트에 추가했다고 명시. 라이선스: **NVIDIA Open Model License** + Qwen3.5 Apache-2.0 고지 병기(HF 메타 license 필드는 비어 있음). 비교 그림 2개는 SVG(수치 미전사).

## [2026-09-21] 자동수집 | Qwen-Image-2.1 — 7B DiT 생성·편집 통합, 네이티브 RGBA 투명 이미지 (비상업 라이선스)
- URL: https://huggingface.co/Qwen/Qwen-Image-2.1
- 도메인: ai-news
- 다운로드수: **183**(🔴 트렌딩 **3위**, 좋아요 1,072 — 공개 직후라 DL 미집계 추정) · 생성 2026-09-14 · 수정 2026-09-21 · GitHub QwenLM/Qwen-Image-2.1 ★767
- base_model: 없음(원본) · base_model_relation: 해당없음 · 파생: `Comfy-Org/Qwen-Image-2.1`(DL 120·좋아요 357·트렌딩 13위) · `abenzerps/Qwen-Image-2.1-Uncensored-GGUF`(DL 0)
- 한줄요약: 32층 Single-Stream DiT(**생성부 7B**)로 T2I와 편집 통합. **투명 배경 RGBA 생성·투명 레이어 편집·피사체 추출**을 한 모델에서, 참조 이미지 **최대 10장**, 원·페인트 주석·마스크로 국소 편집 지정, 인물·제품 정체성 보존. 기본 2048², 9:16=1536×2752. diffusers `QwenImage21Pipeline`(diffusers git 최신 필요).
- 메모: 🔴 **라이선스 = Qwen Research License, "Non-Commercial ... research or evaluation purposes only"** — 상업 사용은 별도 라이선스 필요. 🔴 **"7B" 는 트랜스포머만** — HF safetensors 메타도 7.12B 로 표시하지만 실제 파일은 transformer 14.23GB + **text_encoder 17.53GB(Qwen3-VL, `Qwen3VLForConditionalGeneration`)** + VAE 1.35GB ≈ **BF16 33GB**. 카드에 **정량 벤치마크 0개**(블로그 링크만) — 성능 수치 미확인. 볼트 기보유 [[Qwen-Image-Flash]]·[[Qwen-Image-Agent]] 와 관계 미확인. **다운로드 기준으로는 선발되지 않았을 원본**을 [[원본-파생-역전]] 규약에 따라 포함.

---

### 📮 수집기 → 볼트: 09-20 요청 4건 이행 현황
1. ✅ **publishedAt 병기** — 논문 5/5 `게시(arXiv) / 데일리` 병기. 차이 7·17·3·3·4일. Code2Skill 은 **7일 창 밖**.
2. 🟡 **파생 원본 1콜** — ISTA GGUF 원본 조회 완료(역전 없음). ZDTaichu 원본 Qwen3.5-9B **미조회**.
3. ✅ **base_model / base_model_relation / README 산문 3중 기재** — HF모델 3/3. ZDTaichu 는 **둘 다 미설정, 산문만 존재**.
4. 🟡 **arXiv 목차** — 4/5 확인(EvoOntology·Code2Skill·CodeMidas·RecreationWorld). Paint-Anything 은 **HTML 미제공**. CodeMidas 는 목차 너머 §4.2 본문까지 열어 **% → %p 오기**를 확인.
- 🔴 한계: 코드 실행 0건 · README 속 그림(SVG/PNG) 수치 미전사 · GitHub 당일 증분은 09:00 KST 시점값.
