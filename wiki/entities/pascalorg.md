---
title: pascalorg
type: entity
domain: ai-news
tags: [ai-news, entity, 3d, mcp, webgpu, local-first]
created: 2026-09-10
updated: 2026-09-10
sources: [Pascal-Editor.md]
reliability: high
---

# pascalorg

> [!insight] 핵심 인사이트
> **[[Pascal-Editor]]**(⭐23,176·MIT·React Three Fiber + WebGPU) 를 만든 조직. 이 볼트에서 **MCP를 GUI 애플리케이션 조작 인터페이스로 쓴 첫 본격 사례**의 제작자다.
> 노선은 **로컬 우선(local-first)** 이 일관된다 — 계정·API 키 불필요, 자동 업로드 없음, 프로젝트는 `~/.pascal/data/pascal.db` 에만. `npx @pascal-app/cli editor` 한 줄이 에디터 + **인증된 MCP 서비스**를 동시에 띄우고 충돌 없는 루프백 포트를 자동 선택.

> [!insight] 🎯 이 조직에서 배울 것 — 스킬이 자기 능력에 상한을 건다
> 공개 에이전트 스킬은 **단 2개**(`pascal-3d`, `furniture-fit`). 적은 수가 곧 **좁고 검증된 표면적**이다.
> `furniture-fit` 은 카드에 **하지 않는 것을 먼저 못박는다** — *"높이·개폐·배송 검증을 주장하지 않는, 경계가 명시된 근거 기반 설치면적 평가"*. 나아가 **MCP 툴 스키마를 런타임에 먼저 조회**해 옵션 필드가 없으면 **더 좁은 결과를 보고**하도록 규정한다.
> → **"레포에 기능이 있어도 설치된 릴리스에는 없을 수 있다"를 전제한 설계.** → [[자기제한-명시]]

> [!warning] 자기 한계를 명시하는 README
> - **로컬 CLI 서비스당 활성 에이전트 클라이언트 1개** — 씬 상태 공유로 **병렬 에이전트 불가**
> - npm `beta`(`1.0.0-beta.1`)가 **레포보다 뒤처짐** → 신규 기능은 GitHub 프리릴리스 수동 설치
> - 자인: *"레포 패키지는 엔드포인트·OAuth·도메인 검증·포털 스캔이 **심사 준비됐음을 증명하지 않는다**"*
> → [[vastsa]]의 [[PI-Desktop]] 샌드박스 자인과 함께 **이번 배치 "자기제한 명시" 2대 사례**.

## 관련 페이지
- [[Pascal-Editor]] — MCP 조작 로컬 3D 건축 에디터
- [[자기제한-명시]]
- [[에이전트-스킬]]
- [[AI-3D-생성]]
- [[PI-Desktop]]

## 원본
- 대표 레포: https://github.com/pascalorg/editor
- 실측(2026-09-10): ⭐**23,176** · 포크 2,911 · MIT · created 2025-10-16 · pushed 2026-09-10
- 신뢰도: ⭐⭐⭐ (11개월 누적 23K · MIT 명확 · 자기 한계 명시)
