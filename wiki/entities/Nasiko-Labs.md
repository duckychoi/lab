---
title: Nasiko Labs
type: entity
domain: ai-news
tags: [ai-news, 조직, rust, agent-security]
created: 2026-09-24
updated: 2026-09-24
sources: [nasiko.md]
reliability: medium
---

# Nasiko Labs

[[nasiko]](★8,841 · Rust) 개발 조직. **A2A 에이전트 컨트롤 플레인**을 만든다.

> [!insight] 🎯 볼트가 이 조직 때문에 규칙 하나를 고쳤다
> nasiko의 GitHub API 라이선스가 `NOASSERTION` 이라 수집기가 *"실제 조건 미확인"* 으로 적었다. **LICENSE 파일 196행을 열어 보니 Apache License 2.0 원문 그대로 + `Copyright 2026 Nasiko Labs` 기입**이었다.
> → **`NOASSERTION` 은 "라이선스 불명"이 아니다.** 탐지 실패일 수도 있다. 같은 값을 받은 [[treg]]([[superdesigndev]])은 *"tools-registry License"* 라는 진짜 커스텀이었으므로 **두 상태가 한 값에 접혀 있다** → [[메타데이터-부재-추론]]

## 확인된 것
- 저작권 표기 **`Copyright 2026 Nasiko Labs`** (LICENSE 부록 고지, 볼트 실측)
- README 742행 전문 — Docker 전용 구동 절차, OS별 설치 가이드, 환경변수, 트러블슈팅까지 완비
- 스택 선택: **Postgres · Redis · S3(RustFS)** + 선택적 **Tempo / Loki / OTel Collector**
- topics 에 `agent-security` · `mcp-gateway` 를 직접 넣었다 — **자기 위치를 보안·게이트웨이로 선언**

## ⬜ 미확인
- 법인 실체·국적·규모 **전부 미확인**. README에 조직 소개 섹션 없음(742행 전수 확인).
- 다른 레포 보유 여부 미조회.
- pushed 2026-09-14 이후 10일 미갱신 — 활동 지속성 미확인.

## 관련 페이지
- [[nasiko]] — 유일 확인 산출물
- [[treg]] · [[superdesigndev]] — 같은 `NOASSERTION`, 다른 실체
- [[메타데이터-부재-추론]]
- [[ai-news]]
