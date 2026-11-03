---
title: "Video Generation Meets Agent Harness — 비디오 생성기를 둘러싼 '하네스'를 분석 단위로 삼은 서베이"
type: source
domain: video-saas
tags: [video-saas, survey, agent-harness, agentic-video, world-model, rsi, 영상자동화]
created: 2026-11-03
updated: 2026-11-03
sources: [https://huggingface.co/papers/2610.40191]
reliability: medium
---

**HF**: published 2026-10-29 · upvote **55** · Liaoyuan Fan 외 20인(**21명** · 수집기와 일치) · HF 조직 표기 **Video Rebirth** · 본문 소속: Video Rebirth · NUS · NTU · HKUST · USTC 외(교신: Kevin Qinghong Lin · Mike Zheng Shou · Wei Liu) · arXiv 2610.40191 (cs.CV) · 레포 [agentic-videogen/awesome-agentic-videogen](https://github.com/agentic-videogen/awesome-agentic-videogen) **★40 · 라이선스 필드 없음** (GitHub API 11-03 실측 · HF 캐시 30) — 논문 목록형 awesome 레포라 실행 코드가 아니다

## 핵심 인사이트
> [!insight] "좋은 클립 생성"에서 "피드백으로 비디오 과제를 끝내는 것"으로 질문이 바뀐다
> 하네스는 비디오 모델 주변의 실행 런타임이다. 컨텍스트를 구성하고, 도구를 노출하고, 상태를 유지하고, 피드백을 라우팅하고, 권한·예산을 강제한다. 서베이는 세 무대를 다룬다. ①에이전틱 비디오 생성(대본·샷 계획·에셋·샷 제작·편집) ②에이전틱 월드모델링(게임엔진이나 코딩 에이전트가 작성한 프로그램이 월드 상태를 쥐고, 비디오 모델은 렌더만 맡는 설계 포함) ③비디오 모델 개발의 [[RSI-프레이밍|RSI]].
> 실무에 가장 쓸모 있는 구분은 **피드백이 바꾸는 대상과 시간축이 다르다**는 것이다. 프롬프트 수정·테이크 교체는 *현재 산출물*을 바꾼다. 스킬 보존은 *다음 과제*를 바꾼다. 데이터셋·비평가·생성기 갱신은 *다음 모델 버전*을 바꾼다. 저자 문장으로는 "현재 비디오를 잘 고쳤다는 사실이 미래 능력 향상을 입증하지 않는다".

> [!warning] RSI는 제목에 있지만 결론은 '아직 없음'이다
> 기여 목록에 **"No surveyed system yet revises the procedure that trains and validates the generator"**라고 적혀 있다. 기존 비디오 연구는 "building blocks rather than evidence that one system has completed the full RSI loop"이라고도 썼다. 볼트 [[RSI-프레이밍]]의 패턴(RSI를 제목에 단 서베이가 RSI 부재를 결론으로 적음)과 같은 방향의 사례다.

> [!warning] 확인 범위 — HTML 본문이 1.2절에서 잘린다
> arXiv HTML(66KB)은 Abstract·§1.1·§1.2와 Table 1 머리글까지만 렌더링되고 끝난다(LaTeXML "Experimental support… view the build logs" 문구로 종료). §2 이후 각 장의 분류표·사례·평가 요구사항은 **이번에 확인하지 못했다**. 수집기의 "신규 실험 수치 0건"은 서베이 성격상 타당하다. 다만 이를 검증할 수 있었던 범위는 초록과 서론뿐이다.

## 도메인별 추출 (video-saas)
- **기능 벤치마킹**: 비디오 제작 SaaS를 하네스로 보면 필요한 층이 바로 나온다. *프로젝트 상태*(레퍼런스가 샷 사이에 유지되는가), *테이크 검사*(무엇이 맞았는지 보존하면서 국소 수정), *예산*(생성 비용 계상). 샷별 계약·요소 고정·QA 판정을 저장하는 구조가 이 서베이가 말하는 "harness state"에 해당한다.
- **크리에이터 인사이트**: 저자는 "그럴듯한 영상이 서사 요구를 어기거나 의도한 행동을 실현하지 못할 수 있다"고 쓰고, 그래서 **품질 점수 하나로는 다음에 무엇을 할지 정해지지 않는다**고 했다. 국소 결정으로 이어지는 진단(어느 샷·어느 요소가 틀렸나)이 핵심이다. → [[MaLiang-Harness]] (P2V gap)와 같은 문제의식이다.
- **워크플로우**: 브리프 → 일관된 샷 → 레퍼런스 유지 → 테이크 검사 → 정답 보존 편집. 서론이 직접 열거한 순서다.
- **경쟁 우위 빈틈**: "엔진이 월드 상태를 쥐고 비디오 모델은 렌더만" 설계는 [[ATAS]](월드스테이트 중심)와 같은 축이다. 장기 일관성을 생성기 내부 기억이 아니라 외부 상태로 푸는 방향이다.
- **평가 체크리스트(서론 기준)**: ①현재 산출물 수정 ②하네스 상태 갱신 ③생성기 파라미터 갱신 ④평가기 갱신 ⑤개선 절차 자체 변경, 이 다섯을 섞지 말 것. 저자는 개선이 개발에 재진입하는 **4개 채널**을 식별했다고 쓴다. 채널의 구체 내용은 §2 이후라 미확인이다.

## 관련 페이지
- [[하네스-설계-축]] · [[RSI-프레이밍]] · [[Self-Evolving-Agent-Harness]] (같은 서베이형 · 주장-증거 대장) · [[Harness-Handbook]]
- [[MaLiang-Harness]] · [[ATAS]] · [[AI-영상-생성-2026]] · [[월드모델]] · [[Diffusion-월드모델]] · [[seedance-2]]
- [[WaveForcing]] (같은 날 · 스트리밍 생성기 측) · [[CoworkOS]] (같은 날 · 하네스가 후학습까지 돌린 사례)

## 원본
- 출처: https://huggingface.co/papers/2610.40191 · https://arxiv.org/html/2610.40191
- 확인 범위: HF `api/papers/2610.40191` · arXiv HTML(초록·§1.1·§1.2만 렌더) · GitHub API 메타 · 🔴 §2 이후 본문·Table 1 내용·4개 채널 상세 미확인(HTML 절단 · PDF 미열람)
- 신뢰도: ⭐⭐ (서베이 · 실험 없음 · 분류 체계 참고용 · 다기관 21인)
