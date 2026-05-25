# 그란데클립 의장 그룹 디자인 가이드

> 그란데클립코리아 — 김봉진 의장이 설립한 컴퍼니빌더의 보고·대시보드·발표 자료에 일관되게 적용되는 비주얼 시스템. 의장 본인이 디자이너 출신이고, 그룹 산하 브랜드(뉴믹스커피·매거진C·어메이징크리·스테이폴리오) 모두 "감성 브랜드"로 포지셔닝되어 있기 때문에, 보고 자료조차 잡지 같은 톤이 유지되어야 한다.

## Overview

그란데클립 자료 표면은 **거의 종이 같은 따뜻한 백색** (`{colors.canvas}` — #FAF8F4) 위에 깊은 무채색 타이포그래피가 얹힌 잡지 같은 캔버스다. 회사가 PT덱·SaaS 대시보드 톤이 아니라 **편집디자인 톤** — 매거진C의 도큐멘터리 무드와 뉴믹스커피의 미니멀 흑백 톤을 양쪽에서 끌고 온 것 — 으로 일관되어 있어, 매출 표 한 장조차 잡지 한 페이지처럼 떨어진다.

브랜드 voltage는 단 하나의 액센트, **그란데클립 레드** (`{colors.gc-red}` — #C8281E)에서만 나온다. KPI 변동, 알림, 핵심 숫자에 점적으로 들어가고 그 외 모든 곳에서는 무채색이 화면을 지배한다. 일본 잡지 *POPEYE*/*BRUTUS* 의 절제된 액센트 사용법과 같은 원리 — "한 페이지에 빨강은 한 군데만".

타이포 보이스는 **Pretendard + IBM Plex Serif** 페어링. Pretendard가 한글 본문·UI·헤드라인을 담당하고, IBM Plex Serif는 매거진 발행물 헤드와 인용구에 들어간다. 두 폰트가 같이 등장하면 "F&B·골프웨어·잡지·숙박을 한 회사가 운영하는데도 톤이 흩어지지 않는" 시각적 접합부 역할을 한다.

**Key Characteristics:**
- 종이 같은 따뜻한 백색 캔버스 (`{colors.canvas}` — #FAF8F4) — 순백 #FFF가 아니다. 인쇄물 같은 깊이.
- 잉크 톤 본문 (`{colors.ink}` — #1A1A1A) — 순흑 #000보다 미세하게 따뜻한 잉크 톤.
- 액센트는 그란데클립 레드 1색만 (`{colors.gc-red}` — #C8281E). KPI 변동·핵심 강조·알림에만.
- 디스플레이는 **Pretendard 700 + IBM Plex Serif Italic** 페어링. 본문은 Pretendard 400/500.
- 박스/카드는 모서리 거의 직각 (`{rounded.none}` 0px) — 잡지 그리드 느낌.
- Hairline은 1px `{colors.hairline}` (#D8D2C8) — 종이 위 인쇄선처럼 미세.
- 차트는 흑백 그라데이션 + 강조 1개만 레드. 무지개 팔레트 금지.
- 한 화면에 빨강 한 군데. 두 군데 이상이면 강조가 죽는다.

## Colors

### Brand & Accent
- **Canvas** (`{colors.canvas}` — #FAF8F4): 모든 보고서·대시보드의 기본 배경. 페이퍼 톤 백색. 순백 #FFF 사용 금지.
- **Ink** (`{colors.ink}` — #1A1A1A): 본문·헤드 기본 색. 순흑 #000 사용 금지 (잉크의 따뜻함이 종이와의 대비를 만든다).
- **GC Red** (`{colors.gc-red}` — #C8281E): 단일 액센트. KPI 증감 표시, 알림 점, "주의" 라벨, 인용구 시작 markings에만. CTA 버튼 색이 아니라 **편집 강조 색**.
- **GC Red Soft** (`{colors.gc-red-soft}` — #F4DED9): 매우 옅은 레드 — 표 셀 강조 배경에 한해 사용 (행 하이라이트). 직접 본문 색으로 쓰지 않음.

### Surface
- **Surface Soft** (`{colors.surface-soft}` — #F2EEE6): 캔버스보다 한 단계 어두운 페이퍼 — 카드 배경, 사이드바, 푸터.
- **Surface Card** (`{colors.surface-card}` — #FFFFFF): 캔버스 위 카드 — 진짜 순백을 카드에서만 허용 (캔버스 대비 한 단계 밝게 보이는 효과).
- **Surface Ink** (`{colors.surface-ink}` — #1A1A1A): 잡지 풀블리드 헤더 영역 — 페이지 상단 magazine-style 헤더에 한정.

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #D8D2C8): 기본 1px 구분선. 표 행간, 섹션 디바이더, 카드 외곽.
- **Hairline Strong** (`{colors.hairline-strong}` — #A39B8A): 강조 구분선 — 표 헤더 아래, 섹션 사이 굵은 디바이더.

### Text
- **Text Primary** (`{colors.text-primary}` — #1A1A1A): 본문·헤드 — Ink 토큰과 동일하지만 의미적으로 텍스트용.
- **Text Body** (`{colors.text-body}` — #4A4742): 긴 본문 단락 — 잉크보다 한 단계 부드러움.
- **Text Muted** (`{colors.text-muted}` — #8B8478): 라벨·캡션·메타 정보.
- **Text Faint** (`{colors.text-faint}` — #B8B0A0): 회색 톤 데이터 라벨 (강조 안 되는 곁가지 정보).

### Semantic
- **Positive** (`{colors.positive}` — #1A1A1A): 증가·긍정도 잉크로. 색을 안 쓰는 게 시그니처. 화살표 ▲ 만으로 표현.
- **Negative** (`{colors.negative}` — #C8281E): 감소·주의·이상치 — GC Red 와 동일. 한 화면에 1~2회 이내.
- **Neutral** (`{colors.neutral}` — #8B8478): 변동 없음, 데이터 부족, 보류.

## Typography

### Font Family
한글·UI는 **Pretendard** (variable, weight 400~800). 잡지 헤드·인용구는 **IBM Plex Serif** (Italic 600). 영문 캡션·라벨은 **Pretendard**가 영문도 잘 받기 때문에 단일 폰트로 통일.

대안 페어링: IBM Plex Serif가 없는 환경에서는 **Noto Serif KR** (Bold) 가 차선. 절대 다른 산세리프를 두 개 섞지 말 것 — 두 산세리프가 페이지에 동시에 등장하면 그란데클립 톤이 즉시 무너진다.

### Hierarchy

| 토큰 | 크기 | 굵기 | 행간 | 자간 | 용도 |
|---|---|---|---|---|---|
| `{typography.editorial-xl}` | 56px | IBM Plex Serif Italic 600 | 1.05 | -0.5px | 보고서 표지 헤드라인 ("이번 주, 그란데클립") |
| `{typography.editorial-lg}` | 36px | IBM Plex Serif Italic 600 | 1.15 | -0.3px | 섹션 헤드 ("어메이징크리 SS25 현황") |
| `{typography.display-lg}` | 32px | Pretendard 700 | 1.2 | -0.5px | 대시보드 페이지 H1 |
| `{typography.display-md}` | 24px | Pretendard 700 | 1.3 | -0.3px | 카드 헤드, 사업부명 |
| `{typography.kpi-xl}` | 48px | Pretendard 800 | 1.0 | -1.0px | KPI 숫자 (이번 주 매출 등) |
| `{typography.kpi-md}` | 28px | Pretendard 700 | 1.1 | -0.5px | 보조 KPI 숫자 |
| `{typography.body-lg}` | 17px | Pretendard 400 | 1.7 | 0 | 인사이트 본문, 잡지 본문 |
| `{typography.body-md}` | 15px | Pretendard 400 | 1.6 | 0 | 기본 본문 — 표 셀, 일반 단락 |
| `{typography.body-sm}` | 13px | Pretendard 400 | 1.5 | 0 | 표 캡션, footer body |
| `{typography.label-uppercase}` | 11px | Pretendard 700 | 1.3 | 1.2px | 카테고리 라벨, 섹션 마커 (AMCR / NEWMIX / 매거진C / STAYFOLIO) |
| `{typography.caption}` | 12px | Pretendard 400 | 1.4 | 0 | 데이터 출처, 기간 표기, 작은 주석 |
| `{typography.quote}` | 18px | IBM Plex Serif Italic 400 | 1.6 | 0 | 인용구 — 의장 한 마디 강조에만 |

### Principles
- IBM Plex Serif Italic은 **헤드와 인용구에만**. 본문에 들어가지 않음.
- KPI 숫자는 Pretendard 800 — 가장 굵은 weight로 한 화면에 한두 군데만.
- 라벨 (사업부명·카테고리)은 UPPERCASE + 1.2px tracking — 매거진 인덱스 톤.
- 인쇄물 호환 — 모든 폰트 사이즈가 A4 PDF로 출력했을 때 깨지지 않게 설정 (12pt 미만 본문 사용 자제).

### Note on Font Substitutes
Pretendard가 시스템에 없을 경우 fallback: `system-ui, -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif`. Noto Sans KR로 떨어져도 큰 차이 없지만, Pretendard의 한글 자간이 가장 잡지 톤에 가까움.

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 40px · `{spacing.xxl}` 64px · `{spacing.section}` 96px.
- **Section padding (vertical):** `{spacing.section}` (96px) 잡지 chapter 간격.
- **Editorial header:** `{spacing.xxl}` (64px) 상하 여백 — 헤드라인 호흡.
- **Card internal padding:** `{spacing.lg}` (24px) 본문 카드, `{spacing.xl}` (40px) KPI 메인 카드.
- **표 행 높이:** `{spacing.md}` (16px) 상하 패딩 — 셀이 답답하지 않게.
- **Gutters:** `{spacing.lg}` (24px) 카드 사이.

### Grid & Container
- **A4 출력용:** 너비 794px (210mm @ 96dpi), 좌우 마진 56px.
- **웹 대시보드:** 최대 1280px 중앙 정렬.
- **컬럼:** 12 컬럼 그리드. 보고서 본문은 8 컬럼, 사이드 메타는 4 컬럼.
- **KPI 카드 그리드:** 데스크탑 4-up, 태블릿 2-up, 모바일 1-up.

### Whitespace Philosophy
그란데클립 자료는 **여백을 데이터로 본다**. 잡지가 가장자리 광활한 흰 여백을 그대로 두는 것처럼, 보고서도 화면을 꽉 채우지 않는다. 한 페이지의 60~65% 정도만 콘텐츠로, 나머지는 호흡. 데이터를 더 많이 넣고 싶으면 페이지를 추가하지 표를 압축하지 않는다.

## Elevation & Depth

| Level | Treatment | 용도 |
|---|---|---|
| Flat | 배경색 차이만 | 본문 섹션, 헤더, 푸터 |
| Hairline | 1px `{colors.hairline}` 외곽선 | 카드, 표 외곽 |
| Soft Lift | `{colors.surface-card}` 배경 (캔버스보다 한 단계 밝음) + hairline | KPI 카드, 사업부 카드 |
| Editorial Slab | `{colors.surface-ink}` (잉크색) 풀블리드 배경, 흰 텍스트 | 잡지-스타일 챕터 헤더, 보고서 표지 — 한 보고서에 1번 |

드롭 섀도우 금지. 그란데클립 톤에서 그림자는 SaaS적이라 즉시 어색해진다. 깊이는 색 차이와 hairline으로만.

### Decorative Depth
- **Editorial Slab Header** (`{component.editorial-slab}`): 보고서 첫 페이지에 잉크 색 풀블리드 영역 + 흰 텍스트로 표지를 만든다. 매거진 표지 톤. `{spacing.xxl}` 패딩.
- **Sidebar Marker** (`{component.section-marker}`): 섹션 좌측 4px 폭 `{colors.gc-red}` 세로 라인 — 인용구 또는 의장 코멘트 강조 1군데에만.

## Shapes

### Border Radius Scale

| 토큰 | 값 | 용도 |
|---|---|---|
| `{rounded.none}` | 0px | 모든 카드·버튼·이미지 기본값 — 잡지 톤 |
| `{rounded.sm}` | 2px | 작은 라벨 칩 (시즌 라벨, 채널 라벨) |
| `{rounded.md}` | 4px | 한정적 — 토글 버튼만 |
| `{rounded.full}` | 50% | KPI 변동 인디케이터 (▲ ▼ 원형 점) |

### Photography Geometry
사진은 직사각 풀블리드. 둥근 사진 금지. 사진 비율은 잡지 기준 4:3 또는 16:9 — 인스타그램 정사각 비율은 그란데클립 자료에서 사용하지 않음.

## Components

### Top Navigation
- 배경: `{colors.canvas}` + 하단 `{colors.hairline-strong}` 1px.
- 로고 좌측, 사업부 메뉴 중앙, 메타 정보 (날짜·작성자) 우측.
- 메뉴 라벨: `{typography.label-uppercase}` — AMCR · NEWMIX · 매거진C · STAYFOLIO · 그룹.

### KPI Card
- 배경: `{colors.surface-card}` + 1px `{colors.hairline}` 외곽.
- 패딩: `{spacing.xl}` (40px).
- 구조:
  1. 라벨 (`{typography.label-uppercase}`, `{colors.text-muted}`)
  2. 큰 숫자 (`{typography.kpi-xl}`, `{colors.ink}`)
  3. 변동 (▲/▼ + 퍼센트, `{colors.gc-red}` 또는 `{colors.ink}`)
- `{rounded.none}` — 모서리 직각.

### Section Quote (의장 코멘트용)
- 좌측 `{component.section-marker}` (4px gc-red 세로 라인).
- `{typography.quote}` — IBM Plex Serif Italic.
- 출처 라벨 한 줄: "— 의장, 5/26 미팅 메모".

### Data Table
- 헤더: `{colors.text-muted}` + `{typography.label-uppercase}` + 하단 `{colors.hairline-strong}` 2px.
- 본문 행: 1px `{colors.hairline}` 행간선.
- 강조 행: `{colors.gc-red-soft}` 배경 — 한 표에 1~2행만.
- 숫자는 우측 정렬, 텍스트는 좌측 정렬.

### Footer
- 배경: `{colors.surface-soft}`.
- `{typography.body-sm}` + `{colors.text-muted}`.
- 단순 — 출처·생성 시각·보안 등급 한 줄.

## Do's and Don'ts

### Do's
- 종이 톤 캔버스 `{colors.canvas}` 위에 잉크 톤 `{colors.ink}` 본문.
- 빨강은 한 화면에 한 군데. KPI 변동 또는 핵심 인사이트 강조.
- 헤드라인 IBM Plex Serif Italic, 본문 Pretendard 페어링.
- 표·카드 모서리 직각 (`{rounded.none}`).
- 여백을 데이터로 인식 — 답답하면 페이지를 더 만든다.
- 사업부 라벨 UPPERCASE + 1.2px tracking.
- 차트는 무채색 + 강조 한 색.

### Don'ts
- 순백 #FFF 캔버스 — 페이퍼 톤이 그란데클립 시그니처.
- 순흑 #000 본문 — 잉크는 따뜻한 톤이어야 함.
- 한 화면에 빨강 두 군데 이상 — 강조가 죽는다.
- 드롭 섀도우, 글래스모피즘, 그라데이션 배경 — SaaS 톤.
- 모서리 둥근 카드 (`{rounded.md}` 이상) — 잡지 톤 깨짐.
- 두 산세리프 동시 사용 (예: Pretendard + Noto Sans 동시).
- 차트에 무지개 팔레트 — 무채색 + 강조 1색.
- KPI 숫자 옆에 작은 그래프 (sparkline) 남발 — 한 페이지 2개 이내.

## Responsive Behavior

### Breakpoints

| Breakpoint | 너비 | 동작 |
|---|---|---|
| Desktop | ≥1280px | 12 컬럼 풀 그리드, KPI 4-up |
| Tablet  | 768~1279px | 8 컬럼, KPI 2-up |
| Mobile  | <768px | 단일 컬럼, KPI 1-up, 표는 가로 스크롤 |
| Print A4 | 794px 고정 | 출력 최적화 — 페이지 분할, 헤더 반복 |

### Touch Targets
모바일 최소 터치 영역 44x44px. 표 행 클릭 가능하면 행 높이 48px 이상.

### Collapsing Strategy
모바일에서 사이드 메타 (작성자·날짜)는 본문 하단으로 이동. 사업부 탭은 드롭다운으로 축약.

### Image Behavior
헤더 풀블리드 사진은 모바일에서도 풀블리드 유지. 잡지 톤 핵심.

## Iteration Guide

1. **새 보고서 페이지를 만들 때**: 표지 (Editorial Slab Header) → 요약 KPI 4개 → 사업부별 섹션 → 의장 코멘트 → 액션 아이템 순.
2. **사업부 추가 시**: 새 라벨을 `{typography.label-uppercase}` 톤으로 추가, 색상 변경 없음 (사업부별 색 구분 금지 — 모두 잉크).
3. **데이터 추가 시**: 표 행을 늘리지 말고 차트로 분리. 잡지처럼 한 페이지에 들어갈 만큼만.
4. **알림·이상치 표시**: GC Red 1군데. 두 군데 이상이면 우선순위 정해서 하나만.
5. **인용구 등장**: 의장 코멘트, 외부 인터뷰만. 일반 본문 강조에 quote 스타일 사용 안 함.
6. **PDF 출력 검증**: 인쇄 시 폰트 안 깨지는지, 페이지 break 위치, 가독성 12pt 이상 확인.
7. **차트 컬러**: 무채색 4단계 (잉크 → 다크그레이 → 미드 → 라이트) + 강조 1개만 GC Red.
8. **새 화면을 만들 때 자가검증**: "이 화면이 잡지 한 페이지로 인쇄됐다면 어색하지 않은가?" — Yes 이면 OK.

## Known Gaps

- **모바일 전용 패턴 미정**: 그란데클립 자료는 임원진 데스크탑/A4 PDF 사용이 기본. 모바일 케이스가 정해지면 추가 가이드 필요.
- **다크모드 미정**: 잡지 톤이라 다크모드는 별도 시스템으로 만들거나 제공 안 하는 방향 (Editorial Slab Header가 사실상 부분 다크 영역).
- **사업부별 보조 액센트**: 현재 사업부 색 구분 안 함. 만약 필요하면 채도 낮춘 무채색 hue (warm gray ↔ cool gray) 정도로만 — GC Red는 그룹 전체 1개 액센트로 유지.
- **데이터 시각화 라이브러리 가이드**: D3·Recharts 등 차트 라이브러리 매핑 미작성 — 현재는 톤 가이드만.
