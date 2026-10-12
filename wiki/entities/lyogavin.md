---
title: "lyogavin (Gavin Li) — airllm 제공자, 메모리 축만 보고하는 레포 운영자"
type: entity
domain: local-llm
tags: [entity, github, local-llm, inference, memory-optimization, 간판-지체]
created: 2026-10-12
updated: 2026-10-12
sources: [airllm.md]
reliability: low
---

# lyogavin

**GitHub**: https://github.com/lyogavin
**블로그/채널**(README 배지 실측): Medium `@lyo.gavin` · `gavinliblog.com` · Patreon `gavinli` · GitHub Sponsors · Discord · WeChat(Anima)

> [!insight] 핵심
> [[airllm]] 의 제공자. **레이어 단위·전문가 단위 스트리밍으로 VRAM 상주량을 낮추는** 추론 도구를 만든다. 📌 양자화·증류·프루닝 없이 메모리만 줄이는 접근이다(README: *"without quantization, distillation, or pruning"*).

> [!note] ✅ 확인된 것 (볼트 실측 2026-10-12)
> - [[airllm]]: ★**36,880** · fork 3,837 · **Apache-2.0** · Jupyter Notebook · created **2023-06-12** · pushed **2026-10-12T06:31:50Z** · open issues 161 · 12,746 KB
> - **3년 이상 지속 개발** — 2023/11 초기 버전 → 2026/09 학습 지원까지 업데이트 이력이 연속적이다
> - ✅ **메모리 수치에 측정 하드웨어를 명시한다**: *"measured end to end on one RTX 6000 Ada / RTX 4090 / RTX 3090"* 📌 금일 배치에서 하드웨어를 적은 소스는 드물다
> - PyPI `airllm` 배포 · MacOS(mlx) 지원 · Colab 노트북 제공

> [!warning] 🔴 보고 품질이 축에 따라 극단적으로 갈린다
> | 축 | 보고 수준 |
> |---|---|
> | **메모리** | 🟢 하드웨어·측정방식까지 명시(2.8T → 3.72GB 등) |
> | **속도** | 🔴 **절대값 0개.** 상대 배수("3x", "10%")만 있고 그 근거도 PNG 봉인 |
> ⇒ 📌 **[[상대속도-가림]] 의 가장 순수한 사례**를 만든 운영자다. ⚖️ **"불투명하다"고 평가하면 부정확하다** — 한 축은 매우 투명하다.

> [!warning] 🔴 간판을 갱신하지 않는다 — [[간판-지체]] 최초 사례
> GitHub `description` 과 README 제목이 **2024/04 상태**(*"70B inference with single 4GB GPU"*)에 고정돼 있다. 📌 **본문 헤드라인은 Kimi K3 2.8T / under 4GB** 를 적는다 — **40배 차이**.
> ⇒ 🎯 **자기 능력을 과소표기하는 방향**이다. 📌 수집 공정이 간판을 먼저 읽으므로 그 과소표기가 하류로 전파된다.

> [!warning] 🔴 README 에 상업 링크가 섞여 있다
> `## AI Agents Recommendation:` 섹션(29~33행)에 **외부 서비스 2건**이 추천으로 올라와 있다(`godmodeai.co` · `crazyfaceai.com`). 📌 기술 문서 상단부에 **관계 미표기 추천 링크**가 있다 — ⚖️ 광고인지 자기 운영 서비스인지 **미확인**. 볼트는 기록만 한다.

> [!note] 🔴 미확인
> - 소속·개인/조직 여부(개인 개발자로 보이나 확정 아님)
> - 추천 링크 2건과의 관계
> - [[airllm]] 외 다른 레포 보유 여부 — **볼트가 사용자 레포 목록을 조회하지 않았다**

## 관련 페이지
- [[airllm]] — 유일 보유 소스
- [[상대속도-가림]] · [[간판-지체]] · [[의존성-요구-충돌]] · [[단위-불일치]]
- [[Qwen3.8-Flash-Next-GSQ-RCO-GGUF]] — airllm 이 지원 대상으로 적는 모델
- [[local-llm]] · [[ai-news]]
