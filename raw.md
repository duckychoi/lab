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
