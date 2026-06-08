# SWEETCH 디자인 가이드

> 브랜드 비주얼 아이덴티티 단일 출처. PDF 보고서·HTML 대시보드·랜딩·슬라이드 어떤 산출물이든 이 파일을 참조하면 SWEETCH 톤이 적용된다.
> 토큰 syntax: 인라인 hex 금지, 모든 참조는 토큰 키로 (`{colors.cobalt}`, `{typography.display-xl}` 등).
> 색 체계는 실제 자사몰(sweetch.co.kr) 렌더링 화면에서 추출했다 (2026-06 확인).

## Overview

SWEETCH(스위치)는 SWEET + SWITCH의 합성어 — "달콤한 변화"를 만드는 가방 브랜드다. 비주얼의 뼈대는 **깔끔한 흰 배경**(`{colors.surface}` — #ffffff) 위에 **검정 타입**(`{colors.ink}` — #111111)을 얹은 크리스프 미니멀이다. 따뜻한 종이 질감이 아니라, 군더더기 없는 화이트 스페이스 위에 제품 사진과 한 줄의 색만 호흡한다. 브랜드의 에너지는 장식이 아니라 **가방 자체의 풀블리드 사진** — 도심을 항해하는 데일리 룩, 16인치 노트북이 들어가는 통근백, 컬러웨이가 한 줄로 늘어선 컷 — 에서 나온다.

색의 voltage는 단 하나, **코발트 블루**(`{colors.cobalt}` — #0000C7)다. 자사몰의 워드마크는 검정이지만, 프로모 바·멤버십 그래픽·핵심 CTA 버튼은 이 선명한 전기 블루로 친다. 흰 바탕과 검정 타입이 "단정한" 쪽을 잡고, 코발트 블루 한 점이 "달콤한 변화"의 에너지를 담당한다. 이 블루는 절제할수록 강해진다 — 한 화면에 한두 군데, 진짜 행동을 유도할 자리에만.

제품의 컬러는 브랜드 UI 컬러가 아니다. Voyager 라인의 컬러웨이(Cloud Cream · Forest Green · Grape Grey · Rosy Pink · Sun Lime · Summer Grey 등)는 **제품 사진과 차트 카테고리 범례 안에서만** 등장하고, UI의 액션·텍스트·강조 컬러로 끌어오지 않는다.

Type voice는 한 패밀리(Inter/Pretendard 계열)를 두 무게로 운용한다 — 헤드라인은 600(SemiBold)으로 또렷하게, 본문은 400(Regular)으로 편안하게. SemiBold와 Regular의 부드러운 대비가 SWEETCH의 에디토리얼 시그니처다. 라벨류만 UPPERCASE + 트래킹으로 "큐레이션된" 느낌을 준다.

**Key Characteristics:**
- 흰 배경(`{colors.surface}` — #ffffff) 위 검정 타입(`{colors.ink}` — #111111). 라이트 모드가 기본 — 다크 반전은 푸터·히어로 오버레이에만.
- 포인트 컬러는 코발트 블루(`{colors.cobalt}` — #0000C7) 하나. 프로모·CTA·핵심 강조에만 절제해서.
- 워드마크/로고는 검정(`{colors.ink}`). 블루는 행동 유도(CTA·링크·강조) 전용 — 로고를 블루로 칠하지 않는다.
- 헤드라인은 sentence-case가 기본, 라벨류만 UPPERCASE.
- Voyager 컬러웨이(`{colors.cloud-cream}` 등)는 제품 사진·차트 범례에만 등장 — UI 액션 컬러로 끌어오지 않는다.
- 제품 사진이 밴드를 채운다. 가방이 늘 주인공, UI 크롬은 물러나 작은 검정 라벨로.
- 버튼은 부드러운 모서리 `{rounded.md}`(8px) — 가방의 둥근 마감을 닮은 라운드.
- 여백은 넉넉하고 그리드 정렬: `{spacing.section}`(80px) 주요 밴드 사이, `{spacing.xl}`(40px) 카드 내부.
- 옅은 중성 그림자(`{component.card}`)로 흰 바탕 위 카드의 깊이감. 하드 섀도우 금지.

## Colors

### Brand & Accent
- **Cobalt** (`{colors.cobalt}` — #0000C7): 시그니처 포인트 컬러. 주요 CTA 버튼, 프로모 바, 핵심 KPI 강조, 링크, 차트 1순위 시리즈. 자사몰 렌더링에서 추출한 유일한 유채색 포인트.
- **Cobalt Soft** (`{colors.cobalt-soft}` — #4b4bd6): Cobalt의 옅은 단계. hover·active 보조 상태, 차트 보조 시리즈, 옅은 강조.
- **Cobalt Tint** (`{colors.cobalt-tint}` — #eceefb): 강조 존·인용 블록 배경에 쓰는 아주 옅은 블루 틴트. 면적으로 깔 때만.

### Surface
- **Surface** (`{colors.surface}` — #ffffff): 기본 페이지 바닥 + 카드·테이블 표면. 크리스프 화이트.
- **Surface Soft** (`{colors.surface-soft}` — #f4f4f5): 표 헤더·존 구분·푸터 인접 스트립. 차가운 라이트 그레이.
- **Surface Muted** (`{colors.surface-muted}` — #e9e9ec): 비활성 영역·구분 존.
- **Ink Panel** (`{colors.ink-panel}` — #121212): 다크 반전 패널(푸터·히어로 오버레이)에만.

### Voyager 컬러웨이 (제품 사진·차트 카테고리 전용)
- **Cloud Cream** (`{colors.cloud-cream}` — #ece3d2)
- **Forest Green** (`{colors.forest-green}` — #2f4a3a)
- **Grape Grey** (`{colors.grape-grey}` — #8b8392)
- **Summer Grey** (`{colors.summer-grey}` — #b9b4aa)
- **Midnight Black** (`{colors.midnight-black}` — #20201e)
- **Sun Lime** (`{colors.sun-lime}` — #c7d44e)
- **Rosy Pink** (`{colors.rosy-pink}` — #e7b7b0)
> 이 컬러웨이들은 차트에서 라인/카테고리 구분, 제품 카드 컬러 칩에만. UI 액션·텍스트·브랜드 강조 컬러로 쓰지 않는다 (그건 Cobalt 전용). Forest Green은 **제품 컬러웨이 이름일 뿐 브랜드 색이 아니다.**

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #e4e4e7): 흰 바탕 위 1px 구분선. 섹션·표 행·카드 외곽.
- **Hairline Strong** (`{colors.hairline-strong}` — #d4d4d8): 강조 구분선, 표 헤더 하단.

### Text
- **Ink** (`{colors.ink}` — #111111): 모든 헤드라인·기본 텍스트·워드마크.
- **Body** (`{colors.body}` — #3f3f46): 본문 러닝 텍스트.
- **Muted** (`{colors.muted}` — #71717a): 캡션·메타·푸터 링크.
- **On Dark** (`{colors.on-dark}` — #fafafa): 다크 패널 위 텍스트.

### Semantic
- **Success** (`{colors.success}` — #2f7d4f): 순마진 흑자·목표 달성·"남는 장사" 양호.
- **Warning** (`{colors.warning}` — #c98a2b): 재고 임박·마진 누수 주의.
- **Danger** (`{colors.danger}` — #b3503f): 결품 임박·환불 급증·적자.
> 시맨틱 컬러는 데이터의 상태 표시 전용. 브랜드 강조(Cobalt)와 혼동하지 않는다.

## Typography

### Font Family
**Inter**(또는 Pretendard) variable. 한 패밀리를 두 무게로 — SemiBold(600) 디스플레이 + Regular(400) 본문. 폴백 스택: `"Pretendard", -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif`.

무게 페어:
- Display(600 SemiBold): 헤드라인·섹션 헤드·카드 타이틀·버튼
- Body(400 Regular): 본문·설명·메타. 굵게 하지 않는다.

600/400의 부드러운 대비가 SWEETCH 시그니처. 한글은 Pretendard로 대체해도 무게 매핑 동일.

### Hierarchy

| Token | Size | Weight | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|
| `{typography.display-xl}` | 56px | 600 | 1.1 | -0.5px | 보고서 표지 타이틀 |
| `{typography.display-lg}` | 40px | 600 | 1.15 | -0.3px | 섹션 헤드 |
| `{typography.display-md}` | 32px | 600 | 1.2 | -0.2px | KPI 카드 수치, 서브섹션 |
| `{typography.display-sm}` | 24px | 600 | 1.3 | 0 | 카드 타이틀, 표 제목 |
| `{typography.title-md}` | 20px | 600 | 1.4 | 0 | 소제목, 리드 문단 |
| `{typography.title-sm}` | 18px | 400 | 1.45 | 0 | 인트로 문단 |
| `{typography.label-uppercase}` | 13px | 600 | 1.3 | 1.2px | 카테고리 라벨, 채널 태그 (UPPERCASE) |
| `{typography.body-md}` | 15px | 400 | 1.55 | 0 | 기본 본문 |
| `{typography.body-sm}` | 13px | 400 | 1.5 | 0 | 표 셀, 보조 메타 |
| `{typography.caption}` | 11px | 400 | 1.4 | 0.3px | 캡션, 출처 |
| `{typography.button}` | 14px | 600 | 1.0 | 0.5px | 버튼 라벨 (sentence-case) |

### Principles
SemiBold(600) 헤드라인과 Regular(400) 본문의 부드러운 대비를 항상 유지. 라벨류(`{typography.label-uppercase}`)만 UPPERCASE + 1.2px 트래킹으로 "큐레이션" 느낌. 헤드라인은 sentence-case가 기본. 큰 디스플레이는 음수 트래킹(-0.5~-0.2px)으로 단정하게 조인다.

### Note on Font Substitutes
Inter/Pretendard가 없으면 시스템 산세리프 스택으로 폴백. 한글 비중이 높은 보고서는 Pretendard 우선. 디스플레이 트래킹만 -0.3px로 맞추면 톤 유지.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 40px · `{spacing.xxl}` 56px · `{spacing.section}` 80px.
- **Section padding(수직):** `{spacing.section}`(80px) 주요 밴드 사이.
- **Card 내부:** `{spacing.xl}`(40px) 콘텐츠 카드, `{spacing.lg}`(24px) KPI 카드.
- **Gutter:** `{spacing.lg}`(24px) 3-up 그리드 카드 사이.

### Grid & Container
- **Max content width:** ~1080px 중앙 정렬 (A4 PDF 친화 폭).
- **본문:** 12-column 그리드. 히어로 사진 밴드만 풀블리드.
- **카드 그리드:** 데스크탑 3-up, 태블릿 2-up, 모바일 1-up.
- **KPI 카드:** 4-up 행 (데스크탑) → 2-up (태블릿).

### Whitespace Philosophy
SWEETCH는 사진과 여백이 일하게 둔다. 가방 사진 주변 여백은 넉넉하게, 카피는 그 아래 단정하게 정렬. 여백은 `{spacing.section}`(80px)으로 균일하게. 그라데이션·장식 배경 없이 크리스프 화이트가 깊이를 만든다.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | 그림자 없음 | 본문 섹션, 푸터, 사진 밴드 |
| Hairline | 1px `{colors.hairline}` border | 섹션 구분, 표 행, 카드 외곽 |
| Card | `{colors.surface}` + soft shadow (0 1px 3px rgba(17,17,17,0.06)) | KPI 카드, 콘텐츠 카드 |
| Card Raised | soft shadow (0 4px 16px rgba(17,17,17,0.08)) | 강조 카드, 표지 |
| Photo | 풀블리드 사진, 모서리 `{rounded.lg}` | 히어로, 제품 컷 |

하드 무채색 섀도우 금지. 중성 그레이의 옅은 soft shadow로 흰 바탕 위 카드의 깊이를 낸다.

### Decorative Depth
- **Cobalt Accent Bar** (`{component.accent-bar}`): KPI 카드 좌측 또는 섹션 헤드 아래 3px `{colors.cobalt}` 바. SWEETCH의 유일한 장식 요소 — 핵심 지점에만 절제해서.
- **Colorway Chip Row**: Voyager 컬러웨이 칩을 작은 원형으로 나열(제품 소개·범례). `{rounded.full}`.

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | 표 셀, 풀블리드 사진 일부 |
| `{rounded.sm}` | 4px | 태그, 칩, 작은 배지 |
| `{rounded.md}` | 8px | 버튼, 인풋 — 기본 라운드 |
| `{rounded.lg}` | 12px | 카드, 콘텐츠 컨테이너, 제품 사진 |
| `{rounded.xl}` | 20px | 히어로 사진 밴드, 표지 카드 |
| `{rounded.full}` | 9999px | 컬러웨이 칩, 원형 아이콘 버튼 |

라운드 위계는 "기본 8~12px의 부드러운 마감". 둥근 모서리가 가방의 손맛과 "달콤한" 브랜드 톤을 읽히게 한다.

### Photography Geometry
히어로 사진은 풀블리드 + `{rounded.xl}`(20px). 그리드 안 제품 컷은 `{rounded.lg}`(12px), 4:5 또는 1:1 크롭. 컬러웨이 라인업 컷은 와이드 16:9. 사진은 자연색 라이프스타일 컷 — 흑백 강제하지 않되 채도는 차분하게.

## Components

### Top Navigation
**`top-nav`** — 흰 바, 상단 고정. 64px, `{colors.surface}` 배경, 하단 1px `{colors.hairline}`. 좌측 SWEETCH 워드마크(`{colors.ink}` — 검정), 중앙 메뉴(New, Product, Campaign, Journal), 우측 검색·계정·장바구니 아이콘. 메뉴는 `{typography.body-md}` sentence-case. 프로모 고지 바가 필요하면 nav 위에 `{colors.cobalt}` 풀폭 스트립 한 줄.

### Buttons
**`button-primary`** — 시그니처 CTA. 배경 `{colors.cobalt}`, 텍스트 `{colors.on-dark}`(흰색), `{rounded.md}`(8px), 패딩 12px×24px, 높이 44px. 타입 `{typography.button}` sentence-case. 둥근 모서리 + 코발트 배경이 SWEETCH 버튼.

**`button-secondary`** — 배경 투명, 1px `{colors.ink}` 외곽선, 텍스트 `{colors.ink}`. 보조 액션.

**`button-on-tint`** — Cobalt Tint 존 위 버튼. 배경 `{colors.surface}`, 텍스트 `{colors.ink}`, hairline 외곽.

**`button-icon`** — 원형 아이콘 버튼. 40×40px, 배경 `{colors.surface}`, `{rounded.full}`, 아이콘 `{colors.ink}`.

**`text-link`** — 인라인 링크. `{colors.cobalt}`, 밑줄 없음, sentence-case. → glyph 동반.

### Cards & Containers
**`hero-band`** — 풀블리드 제품 사진 밴드, `{rounded.xl}`. h1은 `{typography.display-xl}` 좌측 정렬, 하단 `{typography.title-sm}` 서브카피. 수직 패딩 `{spacing.xxl}`(56px).

**`kpi-card`** — 보고서 핵심 지표 카드. 배경 `{colors.surface}`, `{rounded.lg}`, soft shadow, 패딩 `{spacing.lg}`(24px), 좌측 `{component.accent-bar}`. 상단 `{typography.label-uppercase}` 라벨, 중앙 `{typography.display-md}`(32px) 수치, 하단 `{typography.body-sm}` "그래서 무슨 의미" 한 줄(필수). 수치만 있는 카드 금지.

**`data-table`** — 분석 표. 헤더 행 배경 `{colors.surface-soft}`, `{typography.label-uppercase}`. 본문 행 `{typography.body-sm}`, 1px `{colors.hairline}` 구분. 양수/음수 마진은 `{colors.success}`/`{colors.danger}`. `{rounded.lg}` 외곽 클립.

**`insight-card`** — 원인·해석 카드. 배경 `{colors.cobalt-tint}`, `{rounded.lg}`, 패딩 `{spacing.xl}`. 좌측 `{component.accent-bar}`. 표 옆 "왜 움직였나" 3~4줄 해석을 담는다.

**`product-card`** — 3-up 그리드 제품 카드. 상단 4:5 제품 사진(`{rounded.lg}`), 하단 `{typography.label-uppercase}` 라인 태그, `{typography.display-sm}` 제품명, `{typography.body-sm}` 가격·컬러웨이 칩.

**`alert-row`** — 재고/마진 경보 행. 배경 `{colors.surface}`, 좌측 4px 시맨틱 컬러 바(`{colors.danger}` 결품 / `{colors.warning}` 임박). `{typography.body-md}` 제품명 + 소진일수 + 권장 액션.

### Inputs & Forms
**`text-input`** — 배경 `{colors.surface}`, 텍스트 `{colors.ink}`, `{rounded.md}`, 패딩 12px×16px, 높이 44px, 1px `{colors.hairline}`. focus 시 외곽 `{colors.cobalt}`.

### Signature Components
**`accent-bar`** — 3px `{colors.cobalt}` 세로 또는 가로 바. KPI/insight 카드 좌측, 섹션 헤드 아래. SWEETCH의 시그니처 비-타이포 요소.

**`colorway-chip-row`** — Voyager 컬러웨이 원형 칩 나열(`{rounded.full}`, 16px). 제품·차트 범례에서 컬러 카테고리 표시.

**`cta-band-tint`** — 푸터 직전 CTA 밴드. 배경 `{colors.cobalt-tint}`, 중앙 `{typography.display-lg}` 헤드 + `{component.button-primary}`. 수직 패딩 `{spacing.section}`.

### Footer
**`footer`** — 다크 반전 푸터. 배경 `{colors.ink-panel}`, 텍스트 `{colors.on-dark}`. 4-column(Shop / Product / Company / Support). 수직 패딩 `{spacing.xxl}`. 하단 사업자 정보 `{typography.caption}`. 본문이 라이트여도 푸터는 잉크 패널로 닫는다.

## Do's and Don'ts

### Do
- 페이지를 제품 사진으로 앵커. 가방이 브랜드 voltage.
- 헤드라인은 sentence-case `{typography.display-*}` SemiBold(600). 라벨류만 UPPERCASE.
- SemiBold(600) 디스플레이 + Regular(400) 본문의 부드러운 대비 유지.
- Cobalt Blue(`{colors.cobalt}`)는 CTA·링크·핵심 강조에만. Voyager 컬러웨이는 사진·차트 범례에만.
- 워드마크/로고는 검정. 블루는 행동 유도 자리에만.
- 기본 `{rounded.md}`(8px)~`{rounded.lg}`(12px). 칩만 `{rounded.full}`.
- KPI/표 수치 옆에 "그래서 무슨 의미" 한 줄 필수.
- `{spacing.section}`(80px)로 밴드 사이 수직 리듬.

### Don't
- Cobalt·Voyager 컬러웨이·시맨틱 3종 밖의 브랜드 컬러 도입 금지.
- 코발트 블루를 넓은 면적에 칠하지 말 것 — 포인트는 점으로 찍을 때 강하다.
- 로고/워드마크를 블루로 칠하지 말 것 (워드마크는 검정).
- 본문을 굵게(600+) 만들지 말 것. 본문은 400 유지.
- 직각 버튼 금지. 둥근 모서리가 SWEETCH 손맛.
- 히어로 뒤 그라데이션 금지. 크리스프 화이트가 깊이를 만든다.
- Voyager 컬러웨이를 UI 액션/텍스트 컬러로 끌어오지 말 것 (사진·범례 전용).
- 전면 대문자 헤드라인 금지 — 라벨만 UPPERCASE.
- 수치만 있는 KPI 카드 금지 — 해석 줄 없으면 미완성.

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Mobile | < 768px | 햄버거 nav; hero h1 56→36px; KPI 카드 1-up; 표 가로 스크롤; 푸터 4→1 col |
| Tablet | 768–1024px | 가로 nav 유지; 카드 2-up; KPI 2-up |
| Desktop | 1024–1440px | 풀 nav; 카드 3-up; KPI 4-up |
| Wide | > 1440px | 데스크탑 동일, max 1080px 중앙 |

### Touch Targets
- `{component.button-primary}` 최소 44×44px.
- `{component.button-icon}` 40×40 (주변 여백으로 44px 확보).
- `{component.text-input}` 높이 44px.

### Collapsing Strategy
- nav는 < 768px에서 햄버거 시트(화이트 풀스크린 오버레이, 상단 `{component.accent-bar}`).
- 제품 사진은 모든 브레이크포인트에서 풀블리드 유지.
- 카드 그리드는 카드 축소가 아니라 컬럼 수를 줄인다.
- 데이터 표는 데스크탑 전체 → 모바일 가로 스크롤.

### Image Behavior
- 히어로 사진 반응형 크롭 — 데스크탑 와이드, 모바일 세로.
- 제품 컷은 native 비율 유지(4:5, 1:1), 레터박스 금지.
- 워드마크는 뷰포트 폭에 비례 스케일.

## Iteration Guide

1. 한 번에 컴포넌트 하나. YAML 키 참조(`{component.kpi-card}`, `{component.alert-row}`).
2. 새 컴포넌트는 `{rounded.md}`(8px) 기본. 원형은 칩/아이콘만 `{rounded.full}`.
3. 변형(`-active`, `-disabled`)은 `components:` 별도 엔트리.
4. `{token.refs}` 사용 — 인라인 hex 금지.
5. hover 상태 문서화 금지. Default + Active만.
6. 디스플레이 sentence-case 600 / 본문 400 — 대비 흐리지 않기.
7. Cobalt는 포인트·액션 전용. Voyager 컬러웨이는 시스템 액션 토큰으로 확장하지 않기.
8. 강조가 필요하면 타입 키우기 전에 사진을 먼저 키운다.

## Known Gaps

- 포인트 컬러 Cobalt(#0000C7)는 자사몰 렌더링 화면에서 직접 추출한 확정값(브랜드 워드마크는 검정). 단, 인쇄 CMYK 변환값·보조 톤은 미스코프.
- 정확한 SWEETCH 웹폰트(자사몰 실제 사용 서체)는 미확인 — Inter/Pretendard로 근사. 확정 시 `{typography.*}` 매핑만 교체.
- Voyager 컬러웨이 hex는 컬러 *이름*만 실재 확인(자사몰 카탈로그), 정확한 색값은 근사 — 차트 범례용으로는 충분하나, 정밀 매칭 시 자사몰 제품 스와치 픽셀 샘플링 필요.
- 자사몰 about 페이지가 미니멀 톤("curated minimalism")만 확인 — 모션·트랜지션 타이밍, 폼 검증 상태는 미스코프.
- 다크 반전(푸터·히어로 오버레이) 외 다크 모드 전체 표면은 미정의.
