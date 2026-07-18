# SSG.COM 산출물 디자인 가이드

> 이 파일이 SSG.COM 톤 산출물(보고서 PDF·대시보드·슬라이드)의 단일 출처다.
> 모든 색·타이포·간격은 아래 토큰 키로만 참조한다. 인라인 hex 직접 사용 금지.
> 컬러 근거: ssg.com 운영 CSS(`ssg_global.css`, 2026-07 배포본)에서 실측 추출.

## 1. Overview

SSG.COM의 화면 언어는 "백화점의 격"과 "이커머스의 속도"가 섞여 있다. 캔버스는 순백에 가깝게 비워두고, 텍스트는 짙은 차콜로 또렷하게, 포인트는 시그니처 레드 한 곳에만 찍는다. 세일가·강조 숫자에 레드가 쓰이고 나머지는 철저히 무채색 — 색이 많아질수록 SSG답지 않다.

보고서·대시보드로 옮길 때의 전압(voltage)은 낮게 유지한다. 화려한 그라데이션이나 장식 없이, 하얀 지면 위 얇은 헤어라인과 정갈한 숫자 표가 기본이고, 손익 악화·경고 등 "봐야 하는 숫자"에만 레드가 허용된다. 프리미엄 문맥(명품·멤버십)에는 골드 브라운을 아껴 쓴다.

목소리(voice)는 경영관리팀의 것이다: 단정하고, 숫자가 먼저 나오고, 수식어는 뒤로 뺀다. 문서 전체가 "회의에서 바로 읽는 자료"처럼 보여야 한다.

## 2. Key Characteristics

- 흰 캔버스 + 무채색 본문, 레드는 강조 1곳 원칙
- 세일가·경고·마이너스 수치에만 `{colors.ssg-red}` 사용
- 프리미엄(명품·멤버십) 맥락 한정 `{colors.premium-gold}`
- 헤어라인은 밝은 회색 1px — 두꺼운 테두리·그림자 지양
- 숫자는 크고 라벨은 작게 (KPI 카드의 위계)
- 표 중심 레이아웃, 여백은 넉넉하되 밀도 있는 데이터 영역
- 다크 네이비 `{colors.deep-navy}`는 헤더·푸터 등 구조 요소 전용
- 장식 일러스트 없음 — 데이터 자체가 비주얼

## 3. Colors

### Brand & Accent
- `{colors.ssg-red}`: #FF5452 — 시그니처 레드. 강조 수치·경고·핵심 CTA
- `{colors.ssg-red-deep}`: #E24F4F — 레드의 저채도 변형. 호버·보조 강조
- `{colors.deep-navy}`: #002041 — 구조색. 문서 헤더 밴드·푸터·표 헤더
- `{colors.premium-gold}`: #966E46 — 프리미엄 맥락 한정 (명품·멤버십 라벨)

### Surface
- `{colors.canvas}`: #FFFFFF — 기본 지면
- `{colors.surface-soft}`: #F9F9F9 — 카드·표 줄무늬 배경
- `{colors.surface-dim}`: #E9E9E9 — 비활성 영역

### Hairlines & Borders
- `{colors.hairline}`: #E5E5E5 — 기본 구분선 1px
- `{colors.hairline-strong}`: #D8D8D8 — 표 외곽선

### Text
- `{colors.text-primary}`: #222222 — 본문·수치
- `{colors.text-secondary}`: #666666 — 라벨·보조 설명
- `{colors.text-tertiary}`: #888888 — 캡션·출처 표기
- `{colors.text-inverse}`: #FFFFFF — 네이비/레드 배경 위

### Semantic
- `{colors.negative}`: #FF5452 — 손실·하락 (ssg-red와 동일값, 의미 분리)
- `{colors.positive}`: #222222 — 상승은 색 대신 굵기로 (이커머스 관례: 레드=할인/경고)
- `{colors.warning-bg}`: #F9F9F9 + 좌측 3px `{colors.ssg-red}` 보더 — 이상 신호 블록

## 4. Typography

### Font Family
- 화면·PDF: Pretendard, "Apple SD Gothic Neo", "Noto Sans KR", sans-serif
- 숫자: 같은 패밀리의 tabular-nums (자릿수 정렬 필수)

### Hierarchy
| 토큰 | 크기/행간 | 굵기 | 용도 |
|------|----------|------|------|
| `{typography.display-xl}` | 34/1.2 | 700 | 표지·헤드라인 수치 |
| `{typography.heading-lg}` | 22/1.35 | 700 | 섹션 제목 |
| `{typography.heading-md}` | 17/1.4 | 600 | 서브 섹션·카드 제목 |
| `{typography.body-md}` | 14/1.6 | 400 | 본문·해석 줄 |
| `{typography.label-sm}` | 12/1.4 | 500 | 표 헤더·KPI 라벨 |
| `{typography.caption}` | 11/1.4 | 400 | 출처·주석 |
| `{typography.kpi-number}` | 28/1.1 | 700, tabular | KPI 카드 수치 |

### Principles
- 제목은 짧게, 수치가 주인공. 볼드는 수치와 결론 문장에만
- 자간 조정 없음, 국문 기본 자간 유지
- 한 화면(페이지)에 굵기 3단계 이상 섞지 않기

### Note on Font Substitutes
Pretendard 미설치 환경에선 시스템 산세리프로 자연 폴백. 세리프 대체 금지.

## 5. Layout

### Spacing System
- `{spacing.xs}` 4px · `{spacing.sm}` 8px · `{spacing.md}` 16px · `{spacing.lg}` 24px · `{spacing.xl}` 40px · `{spacing.xxl}` 64px · `{spacing.section}` 80px

### Grid & Container
- A4 PDF: 콘텐츠 폭 720px, 좌우 여백 동일, 12컬럼 개념 (KPI 카드 4개 = 3컬럼씩)
- 대시보드: max-width 1200px, gutter `{spacing.lg}`

### Whitespace Philosophy
섹션 사이는 `{spacing.xl}` 이상 벌리고, 표 내부는 조밀하게. "지면은 비우고 표는 채운다."

## 6. Elevation & Depth

| 레벨 | 값 | 용도 |
|------|-----|------|
| 0 | 없음 | 기본 — 표·본문 (인쇄 전제) |
| 1 | 0 1px 3px rgba(0,0,0,0.06) | 화면용 KPI 카드 |
| 2 | 0 4px 12px rgba(0,0,0,0.08) | 화면용 모달·툴팁 |

Decorative Depth: 그림자를 장식으로 쓰지 않는다. PDF 산출물은 레벨 0 + 헤어라인만.

## 7. Shapes

| 토큰 | 값 | 용도 |
|------|-----|------|
| `{rounded.none}` | 0 | 표·구분선 |
| `{rounded.sm}` | 4px | 배지·태그 |
| `{rounded.md}` | 8px | KPI 카드·경고 블록 |
| `{rounded.full}` | 999px | 상태 pill |

Photography Geometry: 사진 요소를 쓰지 않는 문서 체계. 필요 시 직각 크롭.

## 8. Components

- **Top Navigation / 문서 헤더**: `{colors.deep-navy}` 밴드, 좌측 문서 제목(`{colors.text-inverse}`), 우측 기준일·작성팀. 높이 64px
- **Buttons**: primary = `{colors.ssg-red}` 배경 + 흰 텍스트, `{rounded.sm}`; secondary = 흰 배경 + `{colors.hairline-strong}` 보더
- **Cards & Containers**: `{colors.canvas}` 배경 + `{colors.hairline}` 1px 보더 + `{rounded.md}`. KPI 카드는 라벨(`{typography.label-sm}`, `{colors.text-secondary}`) 위, 수치(`{typography.kpi-number}`) 아래, 증감/의미 한 줄 최하단
- **Inputs & Forms**: 문서 체계에선 미사용. 대시보드 필터는 흰 배경 + 헤어라인 보더
- **Signature Components**: ① 손익 테이블 — 헤더 행 `{colors.deep-navy}` 배경 + 흰 텍스트, 짝수 행 `{colors.surface-soft}`, 마이너스 수치 `{colors.negative}`; ② 이상 신호 블록 — `{colors.warning-bg}` 좌측 레드 보더 + 원인 추정 줄; ③ 프리미엄 라벨 — `{colors.premium-gold}` 텍스트 pill
- **Footer**: 헤어라인 위 `{typography.caption}` — 데이터 출처·기준일·"수치는 데모용 가상 데이터" 표기

## 9. Do's and Don'ts

**Do**
- 레드는 페이지당 강조 1~2곳으로 제한
- 모든 수치 우측 정렬 + tabular-nums
- 표 아래 해석 줄을 반드시 배치
- 증감은 +/− 부호와 %p 표기로 명확히
- 인쇄(흑백 복사) 시에도 위계가 남는지 확인

**Don't**
- 그라데이션·장식 아이콘·이모지 사용 금지
- 레드/네이비 외 유채색 추가 금지 (차트 예외: 무채색 + 레드 1색 원칙)
- 셀 배경색으로 히트맵 남발 금지
- 둥근 모서리 12px 초과 금지
- 골드를 일반 강조에 사용 금지 (프리미엄 맥락 전용)

## 10. Responsive Behavior

| Breakpoint | 값 | 처리 |
|-----------|-----|------|
| desktop | ≥1024px | KPI 4열, 표 전체 노출 |
| tablet | 768~1023px | KPI 2×2, 표 가로 스크롤 |
| mobile | <768px | KPI 1열, 표는 카드형 변환 |

- Touch Targets: 최소 44px
- Collapsing Strategy: 해석 줄은 접지 않는다 — 접는 건 상세 표
- Image Behavior: max-width 100%, 차트는 SVG 우선

## 11. Iteration Guide

1. 새 산출물은 이 파일의 토큰만으로 시작한다
2. 새 색이 필요하면 먼저 기존 토큰으로 해결되는지 확인
3. 토큰 추가 시 이 파일에 먼저 정의하고 사용한다
4. 컴포넌트 변형은 Signature Components에 추가 기록
5. 레드 사용처가 3곳을 넘으면 디자인을 의심한다
6. 표가 화면을 넘치면 열을 줄이지 말고 표를 나눈다
7. PDF 출력 후 흑백 인쇄 미리보기로 위계 검증
8. 실제 SSG.COM UI와 어긋나는 발견이 있으면 이 파일을 갱신한다

## 12. Known Gaps

- 인쇄물·오프라인 BI 가이드(공식 브랜드북)는 미확인 — 웹 CSS 실측 기반
- 공식 전용 서체 여부 미확인 (웹은 시스템 산세리프 계열)
- 신세계 유니버스 클럽 전용 컬러 체계 미확인 (골드 토큰은 웹 실측 근사)
- 다크모드 팔레트 미정의 (현 산출물 범위 밖)
