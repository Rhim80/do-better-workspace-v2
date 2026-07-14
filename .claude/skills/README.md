# Skills

이 폴더는 이 워크스페이스 전용 스킬을 담습니다.

## Skills란?

Skills는 Claude Code가 **키워드 기반으로 자동 트리거**하는 기능 모음입니다.
구 슬래시 커맨드 방식(`/daily-note`)을 대체합니다.

- 자연어 호출: "오늘 daily note 만들어줘"
- Claude가 description에 있는 키워드를 감지하여 자동 실행
- 각 스킬은 `SKILL.md`를 루트에 두고, 필요시 `scripts/`, `resources/` 같은 하위 폴더 사용

## 파일 구조

```
.claude/skills/
├── README.md             # 이 파일
└── [skill-name]/
    ├── SKILL.md          # 스킬 정의 (YAML frontmatter + 설명 + 실행 절차)
    ├── scripts/          # (선택) 실행 스크립트
    └── resources/        # (선택) 참고 자료, 템플릿
```

## SKILL.md 구조

```yaml
---
name: skill-name
description: 이 스킬이 언제 트리거되는지 명확히. "X를 언급하면 자동 실행" 형식 권장.
---

# 스킬 제목

본문 — 실행 절차, 예시, 주의사항
```

## 전역 vs 프로젝트 스킬

- **전역**: `~/.claude/skills/` — 모든 프로젝트에서 적용
- **프로젝트**: 이 폴더 — 이 워크스페이스에서만 적용

프로젝트 스킬이 전역 스킬과 이름이 같으면 프로젝트 것이 우선.

## 포함된 스킬

### Core (기본 일일 워크플로우)

| 스킬 | 용도 | 트리거 예시 |
|------|------|-------------|
| `setup-workspace` | 첫 clone 후 초기 설정 (대화형 프로필 작성) | "워크스페이스 세팅" |
| `daily-note` | 오늘의 Daily Note 생성/열기 | "오늘 daily note" |
| `daily-review` | 어제~오늘 git 변경 + todos 기반 우선순위 제안 | "일일 리뷰" |
| `todo` | 빠른 할 일 추가 (우선순위 자동 감지) | "할 일 추가" |
| `todos` | 할 일 조회/관리 (today/project/overdue/stats) | "todos", "오늘 할 일" |
| `thinking-partner` | 협력적 사고 — 질문으로 탐색 | "같이 생각해보자" |
| `idea` | 대화에서 아이디어 추출 후 저장 | "이거 기록", "메모해줘" |
| `weekly-synthesis` | 주간 종합 (테마/인사이트/다음 주 방향) | "주간 리뷰" |

### 확장

| 스킬 | 용도 | 트리거 예시 |
|------|------|-------------|
| `pdf-to-md` | PDF → Markdown 변환 | "PDF 변환", "PDF를 마크다운으로" |
| `csv-clean` | CSV 품질 정리 (소계/숫자/날짜/unpivot) | "CSV 정리", "데이터 클리닝" |
| `excel-to-csv` | Excel → CSV 변환 (UTF-8) | "엑셀 변환", "xlsx 변환" |
| `dashboard-prd` | 대시보드 PRD 대화형 생성 | "대시보드 PRD", "대시보드 기획" |
| `webapp-prd` | 웹앱 PRD 대화형 생성 | "웹앱 PRD", "앱 설계" |
| `transcript-organizer` | 긴 녹음 텍스트 구조화 (강의/미팅/인터뷰) | "녹음 정리", "미팅록" |
| `wiki-ingest` | 소스 → 00-wiki 복리 축적 | "wiki-ingest", "위키에 반영" |
| `wiki-lint` | 00-wiki 헬스체크 | "위키 점검", "wiki-lint" |
| `doc-updater` | Claude Code CHANGELOG 기반 공식 문서 자동 동기화 | "문서 업데이트", "CHANGELOG 확인" |
| `md-to-pdf` | 마크다운 → A4 PDF-ready HTML (Monochrome Dark 테마) | "핸드아웃", "PDF 만들어", "배포용" |
| `ripple` | 파일 수정 후 연관 파일 함께 갱신 + 프로젝트 progress.md 생성/추가 | "연관 업데이트", "ripple", "빠진거 없나" |
| `ko-geo` | 콘텐츠를 생성형 AI(ChatGPT·Perplexity)가 인용하도록 GEO 최적화 + 인용률 측정(검증 루프) | "GEO 최적화", "GEO 변환", "GEO 모니터링" |
| `review-analyzer` | 네이버 브랜드스토어 리뷰 크롤(로그인 불필요, URL→ID 자동) + 4단계 분석 | "네이버 리뷰", "브랜드스토어 리뷰", "리뷰 분석" |

### 로컬 도구 · 회신

| 스킬 | 용도 | 트리거 예시 |
|------|------|-------------|
| `kakao-read` **(macOS·윈도우)** | 본인 카톡 로컬 읽기/요약/검색, 카톡 체크(놓친 대화 훑기 → 요약·할일 바로 제시) | "카톡 읽어줘", "카톡 체크" |
| `reply-draft` | 인바운드 회신 초안 작성 — 골격·검증은 엔진, 말투·금지·첨부는 사전 `회신-원칙` | "회신 써줘", "답장 써" |

### Do Better Drive (프로젝트 구동 — 목적→완료 7단계)

프로젝트를 "목적 → 완료"까지 단계로 몰아가는 방법. 각 단계는 `progress.md`의 자기 칸을 채우고 다음으로 넘긴다. 개발자용 gstack의 비개발 버전. **한 스킬 `do-better-drive`가 7단계를 progress.md `status`로 이어간다** (단계 상세는 스킬 내부 `references/1~7`). (형식은 `10-projects/README.md`의 "Do Better Drive 진행" 참조.)

> **처음 쓰는 분은** [`00-system/03-guides/do-better-drive-사용법.md`](../../00-system/03-guides/do-better-drive-사용법.md) — 초심자 기준 7단계 안내 + 예시 프로젝트 워크스루.

| 스킬 | 용도 | 트리거 예시 |
|------|------|-------------|
| `do-better-drive` | 프로젝트를 목적→완료 7단계로 구동. progress.md `status`로 단계를 이어감, 매 단계마다 멈춰 확인. | "새 프로젝트 시작", "검토", "회고", "내보내기" |

**7단계** (스킬 내부 `references/1~7` — 아무 단계나 직접 진입 가능):

| 단계 | 하는 일 | 트리거 예시 |
|------|------|-------------|
| ① 프레임 | 목적·대상 확정 | "새 프로젝트 시작", "이거 할까 말까" |
| ② 될 일인가 | 효과 실현성 | "이거 될 일인가", "실현성 점검" |
| ③ 계획 | 구조·합격 기준 | "계획 짜자", "구조 잡자" |
| ④ 생산 | 변형→비교→확정→끝까지 생산 | "생산 시작", "변형 뽑아 비교" |
| ⑤ 냉정한 검토 | 합격 기준 대조 + 계획 이행 감사 | "검토", "이거 됐나 봐줘", "합격인가" |
| ⑥ 내보내기 | 유통 경로로 발행·발송 | "내보내기", "발행하자", "모객 시작" |
| ⑦ 돌아보기·배우기 | 교훈 포착→복리 | "돌아보기", "회고", "배운 것 뽑아줘" |

### 의존성이 있는 스킬

- `csv-clean` ← `excel-to-csv` (Excel → CSV → 정리 파이프라인)
- `dashboard-prd` / `webapp-prd` → 파일 분석 시 `excel-to-csv` 호출 가능
- `transcript-organizer` → 마지막 단계에서 `wiki-ingest` 자동 호출
- `kakao-read`(카톡 체크) → 읽은 창에서 업무 신호(약속·할일·문의)를 요약·할일로 바로 제시 (`todo` 추가 제안)
- `do-better-drive` — 7단계(①프레임→②될 일인가→③계획→④생산→⑤검토→⑥내보내기→⑦돌아보기)를 프로젝트 `progress.md` `status`로 이어감. 검토(⑤)에서 막히면 앞 단계로 되돌림
- `do-better-drive` ④생산 → 확정된 방향을 기존 콘텐츠·산출 스킬로 끝까지 생산 (다시 만들지 않고 호출)
- `do-better-drive` ⑥내보내기 → 발행·발송을 기존 스킬(`ghost-publish`·`gmail`·`slack`·`naver-commerce`·`note-publish` 등)에 맡김 (다시 만들지 않고 호출)
- `do-better-drive` ⑦돌아보기 → 재사용할 지식을 `wiki-ingest`로 `00-wiki`에 축적 (지식 복리)
- `ripple` → `00-system/01-templates/progress-template.md`(progress.md 생성) + 마지막에 `wiki-ingest` 제안

### Python 의존성이 있는 스킬

- `csv-clean` — pandas
- `excel-to-csv` — openpyxl
- `pdf-to-md` — pymupdf4llm
- `review-analyzer` — selenium (+ Chrome 브라우저). `--no-login`은 이것만 필요. 로그인·시트 업로드는 선택 의존(주석 참조: `scripts/requirements.txt`)

### 시스템 의존성 / 플랫폼 제약

- `kakao-read` — **macOS 전용**. Windows/Linux에선 스크립트가 "macOS 전용" 안내 후 종료(다른 스킬엔 영향 없음). Python 패키지 의존은 없음(표준 라이브러리만). 단 시스템 도구 `sqlcipher`가 필요:
  ```bash
  brew install sqlcipher
  # 최초 1회 본인 userId 캐시 (워크스페이스 루트에서)
  python3 .claude/skills/kakao-read/scripts/kakao_read.py setup
  ```
  카카오톡 데스크톱 앱에 한 번 이상 로그인돼 있어야 한다. 설정은 `~/.config/kakao-read/`(HOME)에 저장 — 워크스페이스 밖이라 git 추적 안 됨.
- `ko-geo` — 변환·진단은 의존성 0. 모니터링 **수동 모드(manual)도 키 0개**(표준 라이브러리만). **자동 모드(run)**만 API 키 필요 — `scripts/.env`에 `PERPLEXITY_API_KEY`/`GEMINI_API_KEY`(Gemini는 무료 티어 가능). `python-dotenv`는 있으면 쓰고 없으면 환경변수로 대체(graceful).

**권장 세팅 (워크스페이스 전용 venv)**:

```bash
# 워크스페이스 루트에서 1회 실행
python3 -m venv .venv
source .venv/bin/activate
pip install "pandas>=2.0.0" "openpyxl>=3.1.0" "pymupdf4llm>=0.0.17"
```

이후 Python 스킬을 쓸 때마다 `source .venv/bin/activate` 한 번 실행. `.venv/`는 `.gitignore` 처리됨.

**venv 없이 직접 설치하려면** (Python 3.12+ / Homebrew 환경에서는 PEP 668 때문에 실패할 수 있음):

```bash
pip install -r .claude/skills/csv-clean/scripts/requirements.txt
# 실패 시: pip install --user ... 또는 pipx 고려
```
