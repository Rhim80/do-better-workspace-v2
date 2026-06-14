## Overview

삼천리 SL&C의 리포트 표면은 **딥 잉크 차콜(`{colors.ink}` — #1f1d1b)** 과 **웜 크림(`{colors.cream}` — #f4efe7)** 위에 **테라코타(`{colors.clay}` — #b5573a)** 가 가늘게 흐르는, 프리미엄 다이닝의 차분한 격조를 옮긴 시스템이다. 표지·섹션 헤더·KPI 밴드는 잉크 바탕에 크림·테라코타 타이포가 얹히고, 본문 표·해석 줄은 크림 캔버스 위에 잉크로 가라앉는다. 5개 브랜드(Chai797·호우섬·서리재·바른고기 정육점·이타마에 스시)가 하나의 외식 포트폴리오로 묶이는 만큼, 장식은 색을 늘리지 않고 **세리프 타이포의 격조**와 **테라코타 헤어라인 한 줄**로 전압(voltage)을 만든다.

테라코타는 절대 면(fill)으로 쓰지 않는다. 헤드라인 위 짧은 룰(rule), 표 상단 보더, KPI 숫자의 강조, 브랜드 배지 테두리처럼 **선·강조에만** 등장한다. 잉크가 권위를, 크림이 여백의 품위를, 테라코타가 "이건 외식 사업부 문서다"라는 따뜻한 식음(食飮) 시그널을 담당한다. 색을 더 넣고 싶을 때는 색이 아니라 **여백과 세리프 크기**를 키운다.

타입 보이스는 **세리프 디스플레이(헤드라인) + 산세리프 본문**의 짝이다. 헤드라인·브랜드명·KPI 숫자는 세리프(Noto Serif KR / Cormorant 계열)로 격조를 만들고, 표 안 숫자·라벨·캡션은 가독성 높은 산세리프(Noto Sans KR / Inter)로 떨어뜨린다. 디스플레이 세리프와 본문 산세리프의 대비가 이 시스템의 편집 시그니처다. 임원 보고·출점 검토 자료라는 용도에 맞게, 데이터는 또렷하게 보이되 표면은 고급 레스토랑의 메뉴북처럼 가라앉는다.

**Key Characteristics:**
- 웜 크림 캔버스(`{colors.cream}` — #f4efe7)가 기본 바닥. 표지·헤더·KPI 밴드만 잉크(`{colors.ink}`)로 반전.
- 헤드라인·브랜드명은 **세리프 디스플레이**, 본문·표는 **산세리프**. 둘의 대비가 격조의 핵심.
- 테라코타(`{colors.clay}`)는 **선·강조 전용** — 헤드라인 룰, 표 상단 보더, 브랜드 배지, KPI 숫자 강조. 절대 버튼·면 채움으로 쓰지 않는다.
- KPI 숫자는 세리프 큰 사이즈(`{typography.display-md}`) + 바로 아래 한 줄 해석 라벨이 짝을 이룬다 (숫자만 두지 않는다).
- 표는 가로 헤어라인(`{colors.hairline}`) 위주, 세로줄 최소화. 상단 보더만 테라코타 1px.
- 모서리는 거의 직각에 가깝게 — `{rounded.sm}`(6px)가 기본, 배지만 `{rounded.full}`.
- 여백은 넉넉하게: 섹션 간 `{spacing.section}`(72px), KPI 밴드 내부 `{spacing.xxl}`(48px), 카드 내부 `{spacing.lg}`(24px).
- 5개 브랜드는 색이 아니라 **세리프 배지·라벨**로 구분 (브랜드별 색 남발 금지).

## Colors

### Brand & Accent
- **Ink** (`{colors.ink}` — #1f1d1b): 시스템의 권위 색. 표지·섹션 헤더·KPI 밴드 배경, 디스플레이 헤드라인 강조 텍스트. 순흑이 아닌 짙은 차콜.
- **Ink Deep** (`{colors.ink-deep}` — #121110): 잉크 밴드 안에서 한 단계 더 깊은 음영 — 푸터·하단 스트립.
- **Clay** (`{colors.clay}` — #b5573a): 시그니처 액센트(테라코타). 헤드라인 룰, 표 상단 보더, KPI 숫자 강조, 브랜드 배지 테두리. **선·강조 전용, 면 채움 금지.**
- **Clay Soft** (`{colors.clay-soft}` — #cd8366): 크림 위 옅은 테라코타 — 보조 라벨, 캡션 강조.

### Surface
- **Cream** (`{colors.cream}` — #f4efe7): 기본 페이지 바닥. 본문·표·카드의 캔버스.
- **Cream Card** (`{colors.cream-card}` — #faf6ef): 카드·표 셀 배경 — 크림보다 한 톤 밝게.
- **Sand** (`{colors.sand}` — #e8dfd0): 표 헤더 행·구분 스트립의 베이지 톤.
- **Ink Band** (`{colors.ink-band}` — #1f1d1b): KPI·섹션 헤더 밴드 (= `{colors.ink}`, 표면 역할로 별칭).

### Hairlines & Borders
- **Hairline** (`{colors.hairline}` — #ddd2c0): 크림 위 1px 구분선. 표 행 사이, 섹션 사이, 카드 외곽.
- **Hairline Clay** (`{colors.hairline-clay}` — #b5573a): 표 상단·헤드라인 아래에 들어가는 테라코타 1px 룰. = `{colors.clay}`.

### Text
- **Ink Text** (`{colors.ink-text}` — #2a2724): 크림 위 본문·표 기본 텍스트. 짙은 차콜-브라운.
- **Ink Soft** (`{colors.ink-soft}` — #6a625a): 보조 텍스트·해석 라벨·캡션.
- **On Ink** (`{colors.on-ink}` — #f4efe7): 잉크 밴드 위 텍스트 (= 크림).
- **Muted** (`{colors.muted}` — #9a8f80): 푸터 링크, 페이지 번호, 메타데이터.

### Semantic
- **Alert** (`{colors.alert}` — #b23a2e): BEP 미달·적자 매장·마진누수 경보. 테라코타 계열이라 톤을 깨지 않는다.
- **Caution** (`{colors.caution}` — #b5851f): 주의 신호(임대료 과중·경쟁 과밀). 머스타드 톤.
- **Positive** (`{colors.positive}` — #4f6f52): 흑자 우위·출점 적합 — 절제된 세이지 그린.

## Typography

### Font Family
헤드라인·브랜드명·KPI 숫자는 **세리프** (`Noto Serif KR`, 영문 `Cormorant Garamond` / `EB Garamond`). 본문·표·라벨은 **산세리프** (`Noto Sans KR`, 영문 `Inter`). Fallback 스택: 세리프 `"Noto Serif KR", "Cormorant Garamond", Georgia, serif` / 산세리프 `"Noto Sans KR", Inter, -apple-system, sans-serif`.

격조는 세리프 디스플레이에서, 가독은 산세리프 본문에서. 표 안 숫자에 세리프를 쓰지 않는다 (정렬·판독성 저하).

### Hierarchy

| Token | Size | Weight | Family | Line Height | Letter Spacing | Use |
|---|---|---|---|---|---|---|
| `{typography.display-xl}` | 48px | 600 | Serif | 1.1 | 0 | 표지 타이틀 ("2026 Q1 외식 사업부 리뷰") |
| `{typography.display-lg}` | 34px | 600 | Serif | 1.15 | 0 | 섹션 헤더 ("브랜드별 점포 수익성") |
| `{typography.display-md}` | 28px | 600 | Serif | 1.2 | 0 | KPI 숫자, 브랜드명 |
| `{typography.title-lg}` | 20px | 600 | Serif | 1.3 | 0 | 카드 타이틀, 표 캡션 |
| `{typography.label-uppercase}` | 12px | 600 | Sans | 1.3 | 1.5px | KPI 라벨, 카테고리 ("OPERATING PROFIT") |
| `{typography.body-md}` | 15px | 400 | Sans | 1.6 | 0 | 본문·해석 줄 |
| `{typography.body-sm}` | 13px | 400 | Sans | 1.55 | 0 | 표 본문, 보조 설명 |
| `{typography.table-num}` | 14px | 500 | Sans (tabular) | 1.4 | 0 | 표 안 숫자 — tabular-nums 정렬 |
| `{typography.caption}` | 11px | 400 | Sans | 1.4 | 0.4px | 캡션, 출처, 페이지 번호 |
| `{typography.quote}` | 22px | 500 (italic) | Serif | 1.4 | 0 | 임원 보고용 헤드라인 코멘트 |

### Principles
디스플레이는 세리프 600, 본문은 산세리프 400 — 둘을 섞지 않는다. KPI 라벨·카테고리만 산세리프 대문자 1.5px 트래킹으로 "각인된" 느낌을 준다. 표 안 숫자는 반드시 tabular-nums로 자릿수를 맞춰 매출·객수 정렬이 흐트러지지 않게 한다.

임원 보고용 한 줄 헤드라인은 `{typography.quote}`(세리프 이탤릭)로 본문에서 떼어내 격조를 준다.

### Note on Font Substitutes
세리프가 없으면 `Georgia`, 산세리프가 없으면 `Inter`로 대체. 한글은 `Noto Serif KR` / `Noto Sans KR`가 1순위이며 웹폰트로 임베드한다 (PDF 출력 시 한글 깨짐 방지).

## Layout

### Spacing System
- **Base unit:** 4px.
- **Tokens:** `{spacing.xxs}` 4px · `{spacing.xs}` 8px · `{spacing.sm}` 12px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 32px · `{spacing.xxl}` 48px · `{spacing.section}` 72px.
- **섹션 간 수직 패딩:** `{spacing.section}`(72px).
- **KPI 밴드 내부:** `{spacing.xxl}`(48px) 상하.
- **카드 내부:** `{spacing.lg}`(24px). 표 셀: 세로 `{spacing.sm}`(12px) / 가로 `{spacing.md}`(16px).

### Grid & Container
- **최대 본문 폭:** A4 인쇄 기준 ~720px 콘텐츠 폭 (좌우 여백 넉넉히).
- **KPI 카드:** 데스크탑 4-up, 태블릿 2-up, 인쇄 4-up 고정.
- **표:** 풀 폭. 세로줄 없이 가로 헤어라인으로만 행 구분.

### Whitespace Philosophy
SL&C 리포트는 여백으로 격조를 만든다. 표와 표 사이, 헤드라인과 본문 사이에 `{spacing.section}` 여백을 일정하게 둔다. 배경 패턴·그라데이션을 넣지 않는다 — 빈 공간은 크림 그대로 둔다. 강조가 필요하면 색이 아니라 여백과 테라코타 룰 한 줄로 처리한다.

## Elevation & Depth

| Level | Treatment | Use |
|---|---|---|
| Flat | 그림자·보더 없음 | 본문 섹션, 푸터 |
| Soft hairline | 1px `{colors.hairline}` | 표 행, 섹션 구분, 카드 외곽 |
| Clay rule | 1px `{colors.clay}` 상단 룰 | 표 상단, 헤드라인 아래 |
| Card surface | `{colors.cream-card}` 배경 + 미세 그림자 (0 1px 2px rgba(31,29,27,.06)) | KPI 카드, 브랜드 카드 |
| Ink band | `{colors.ink}` 풀 폭 밴드 | 표지, 섹션 헤더, KPI 밴드 |

드롭섀도는 거의 쓰지 않는다. 깊이는 크림 캔버스와 잉크 밴드의 명암 대비, 그리고 테라코타 룰에서 나온다.

### Decorative Depth
- **Clay Rule** (`{component.clay-rule}`): 헤드라인 아래·표 상단에 들어가는 폭 40~64px의 짧은 테라코타 1px 룰. 시스템의 유일한 진짜 장식 요소. 의미를 표시할 때만 절제해서 사용.
- **Brand Badge** (`{component.brand-badge}`): 브랜드명을 감싸는 테라코타 테두리 배지. 5개 브랜드 포트폴리오를 구분하는 신호 (색이 아니라 테두리·라벨로).

## Shapes

### Border Radius Scale

| Token | Value | Use |
|---|---|---|
| `{rounded.none}` | 0px | 표, 풀폭 밴드 |
| `{rounded.sm}` | 6px | KPI 카드, 브랜드 카드, 입력 — 기본 라운드 |
| `{rounded.md}` | 10px | 강조 카드 (임원 코멘트 박스) |
| `{rounded.full}` | 9999px | 브랜드 배지, 채널 태그 칩 |

라운드 위계는 "표는 직각, 카드는 살짝 둥글게, 배지는 원형." 메뉴북의 클래식한 직각 프레임과 도장(印)의 원형이 공존하는 느낌.

### Photography Geometry
사진을 쓸 경우(표지 다이닝 이미지) 4:3 또는 16:9, `{rounded.sm}` 모서리. 본문은 사진보다 타이포·표 중심이라 이미지는 표지에만 절제해서 쓴다.

## Components

### Top / Cover
**`report-cover`** — 잉크 풀 폭 표지. `{colors.ink}` 배경에 크림 세리프 `{typography.display-xl}` 타이틀, 그 아래 테라코타 룰(`{component.clay-rule}`), 하단에 사업부명·기간·작성자를 `{typography.label-uppercase}`로. 좌상단 작은 "SL&C" 워드마크.

**`section-header`** — 각 섹션 시작. 잉크 밴드 또는 크림 위 세리프 `{typography.display-lg}` + 아래 테라코타 룰. 잉크 밴드일 때 텍스트는 `{colors.on-ink}`.

### KPI
**`kpi-card`** — 한눈 요약 4장. 배경 `{colors.cream-card}`, `{rounded.sm}`, 패딩 `{spacing.lg}`. 상단에 `{typography.label-uppercase}` 라벨(테라코타 `{colors.clay-soft}`), 가운데 세리프 `{typography.display-md}` 숫자(`{colors.ink}`), **하단에 한 줄 해석 라벨**(`{typography.body-sm}`, `{colors.ink-soft}`). 숫자만 두는 카드는 미완성.

**`kpi-band`** — KPI 카드 4장을 감싸는 잉크 풀 폭 밴드(선택). 카드는 밴드 위에 크림으로 떠 있다.

### Tables
**`data-table`** — 수익성·상권 표. 헤더 행 배경 `{colors.sand}`, 텍스트 `{colors.ink-text}` `{typography.label-uppercase}`. 본문 행은 `{colors.cream}` / `{colors.cream-card}` 교차(zebra). 표 상단에 테라코타 1px 룰, 행 사이 `{colors.hairline}` 1px. 세로줄 없음. 숫자 셀은 `{typography.table-num}` 우측 정렬 tabular-nums.

**`table-emphasis-row`** — 매출↔이익 순위 역전, BEP 미달 매장, 출점 1순위 후보 등 강조 행. 배경 옅은 `{colors.sand}`, 첫 셀에 `{colors.clay}` 좌측 3px 보더. 텍스트 굵게(600).

### Callouts
**`exec-comment-box`** — 임원 보고용 헤드라인 코멘트. `{colors.cream-card}` 배경, `{rounded.md}`, 좌측 `{colors.clay}` 4px 보더, 세리프 이탤릭 `{typography.quote}`. "매출 1등 브랜드가 영업이익 1등은 아니다" 같은 한 줄이 여기 들어간다.

**`alert-chip`** — BEP 미달·적자·마진누수 경보 칩. `{rounded.full}`, 배경 투명, 1px `{colors.alert}` 테두리, 텍스트 `{colors.alert}` `{typography.caption}`. 주의(임대료 과중·경쟁 과밀)는 `{colors.caution}` 버전, 출점 적합은 `{colors.positive}` 버전.

**`brand-badge`** — 브랜드 구분 배지. `{rounded.full}`, 1px `{colors.clay}` 테두리, 세리프 브랜드명, 크림 배경. 5개 브랜드를 색이 아니라 라벨로 구분.

### Inputs & Forms
**`text-input`** — (대시보드 변형 시) 배경 `{colors.cream-card}`, 1px `{colors.hairline}`, `{rounded.sm}`, 포커스 시 보더 `{colors.clay}`. 텍스트 `{typography.body-md}`.

**`channel-tag`** — 채널 필터 칩(오피스상권·백화점쇼핑몰·로드샵). `{rounded.full}`, 비활성은 1px `{colors.hairline}` 테두리 투명 배경, 활성은 `{colors.ink}` 배경 + 크림 텍스트.

### Footer
**`footer`** — 하단 `{colors.ink-deep}` 스트립. 텍스트 `{colors.on-ink}`, 페이지 번호·작성자·출처를 `{typography.caption}`로. 좌측 "SL&C" 워드마크. 절대 반전하지 않는다 (항상 짙은 잉크).

## Do's and Don'ts

### Do
- 헤드라인·브랜드명·KPI 숫자는 **세리프**, 본문·표는 **산세리프**로 분리한다. 대비가 격조다.
- 테라코타는 **선·강조에만** — 헤드라인 룰, 표 상단 보더, 브랜드 배지, KPI 숫자 강조.
- KPI 숫자 아래 **한 줄 해석 라벨**을 반드시 짝지운다. 숫자만 둔 카드는 off-brand.
- 표는 가로 헤어라인으로만 행을 가르고, 표 상단에 테라코타 1px 룰을 둔다.
- 매출↔이익 역전 행·BEP 미달 매장은 `{component.table-emphasis-row}`로 테라코타 좌측 보더 강조.
- 여백은 `{spacing.section}`(72px)로 일정하게. 강조는 색이 아니라 여백·세리프 크기로.
- 표 안 숫자는 tabular-nums로 자릿수를 맞춘다.
- 5개 브랜드는 `{component.brand-badge}`로 구분 — 라벨로, 색으로가 아니라.

### Don't
- 테라코타를 **면(fill)으로 쓰지 않는다.** 테라코타 버튼·테라코타 배경 금지 — 선·강조 전용.
- 잉크·테라코타·크림·세이지 외 새 브랜드 색을 넣지 않는다. 특히 브랜드별 색 부여 금지.
- 표 안 숫자에 세리프를 쓰지 않는다 (정렬·판독 저하).
- 배경에 그라데이션·텍스처·패턴을 깔지 않는다. 빈 공간은 크림 그대로.
- 디스플레이 세리프를 400 weight로 떨어뜨리지 않는다 (600 고정 — 격조 유지).
- 경보 색(`{colors.alert}`/`{colors.caution}`)을 본문 전반에 남발하지 않는다 — 경보 칩·행에만.
- 표지·헤더가 아닌 본문 섹션을 잉크로 반전하지 않는다 (가독 저하).

## Responsive Behavior

### Breakpoints

| Name | Width | Key Changes |
|---|---|---|
| Print (A4) | 720px 콘텐츠 | KPI 4-up 고정, 표 풀폭, 페이지 나눔 |
| Mobile | < 768px | KPI 4-up → 2-up; 표 가로 스크롤; 표지 타이틀 48→34px |
| Tablet | 768–1024px | KPI 2-up; 표 풀폭 |
| Desktop | > 1024px | KPI 4-up; 본문 폭 720px 중앙 정렬 |

### Touch Targets
- `{component.channel-tag}` 칩은 높이 36px 이상, 좌우 패딩 16px.
- 필터·버튼 최소 44px 탭 영역.

### Collapsing Strategy
- KPI 카드는 컬럼 수만 줄이고(4→2) 카드 자체는 축소하지 않는다.
- 표는 모바일에서 가로 스크롤. 핵심 컬럼(브랜드·매장·영업이익률)은 좌측 고정 권장.
- 테라코타 룰·헤어라인 두께는 모든 브레이크포인트에서 1px 유지.

### Image Behavior
- 표지 이미지는 4:3/16:9 유지, 레터박스 금지. 모바일에서 세로 크롭.

## Iteration Guide

1. 한 번에 한 컴포넌트만. YAML 키로 참조 (`{component.kpi-card}`, `{component.data-table}`).
2. 새 컴포넌트는 `{rounded.sm}`(6px) 기본. 원형은 배지/칩만.
3. 변형(`-emphasis`, `-active`)은 `components:`에 별도 항목.
4. 토큰 키로만 참조 — 인라인 hex 금지.
5. hover 상태는 문서화하지 않는다. 기본·강조(active)만.
6. 디스플레이는 세리프 600, 본문은 산세리프 400 — 대비를 흐리지 않는다.
7. 테라코타는 브랜드 시그널 전용 — "주 액션 색"으로 확장하지 않는다.
8. 강조가 고민되면: 색을 더하기 전에 여백을 키우고 세리프를 키운다.

## Known Gaps

- 삼천리 SL&C / Chai797 공식 BI의 정확한 PANTONE 잉크·테라코타 값은 미확인 — 프리미엄 모던 다이닝 톤(차콜+테라코타+크림)을 기준으로 한 합리적 추정값. 실제 BI가 확인되면 `{colors.ink}`/`{colors.clay}` 교체.
- 5개 브랜드(Chai797·호우섬·서리재·바른고기 정육점·이타마에 스시) 각각의 개별 BI 컬러는 미반영 — 포트폴리오 리포트는 통합 잉크/테라코타 톤으로 묶고, 브랜드는 배지·라벨로만 구분 (브랜드별 색 부여는 의도적으로 배제).
- 표지 사진 에셋(다이닝/시그니처 메뉴 이미지)은 미포함 — 데모에서는 타이포·표 중심으로 출력하고, 사진은 선택.
- 차트(파이·바) 색 팔레트는 잉크→테라코타→세이지 그라데이션을 권장하나 정확한 스텝은 산출물에서 확정.
- 애니메이션·트랜지션(대시보드 변형 시)은 범위 밖.
