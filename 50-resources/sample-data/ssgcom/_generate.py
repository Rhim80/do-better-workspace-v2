# SSG.COM FP&A 데모용 더미데이터 생성기 (수치 전부 가상 — 구조만 실제 업무 흐름 반영)
# 실행: python3 _generate.py
import csv, random
from datetime import date, timedelta
from pathlib import Path

random.seed(20260718)
OUT = Path(__file__).parent
START, END = date(2026, 1, 1), date(2026, 6, 30)

# 카테고리 마스터: (카테고리, 사업부, 운영몰, 매입유형, 원가율, 판매수수료율, 물류변동비율, 결제수수료율, 반품율, 평균주문금액, 일평균거래액[원])
CATS = [
    ("신선식품",     "그로서리",   "이마트몰",  "직매입",  0.76, None, 0.085, 0.023, 0.020, 42000, 220_000_000),
    ("가공식품",     "그로서리",   "이마트몰",  "직매입",  0.72, None, 0.075, 0.023, 0.015, 38000, 160_000_000),
    ("생수·음료",    "그로서리",   "이마트몰",  "직매입",  0.78, None, 0.095, 0.023, 0.010, 27000, 90_000_000),
    ("델리·베이커리", "그로서리",   "이마트몰",  "직매입",  0.68, None, 0.080, 0.023, 0.025, 24000, 45_000_000),
    ("명품·부티크",  "브랜드패션", "신세계몰",  "위수탁",  None, 0.18, 0.012, 0.023, 0.050, 780000, 130_000_000),
    ("패션의류",     "브랜드패션", "신세계몰",  "위수탁",  None, 0.22, 0.015, 0.023, 0.080, 96000, 110_000_000),
    ("뷰티",         "브랜드패션", "신세계몰",  "위수탁",  None, 0.20, 0.014, 0.023, 0.030, 62000, 95_000_000),
    ("스포츠·아웃도어","브랜드패션","신세계몰",  "위수탁",  None, 0.21, 0.015, 0.023, 0.060, 88000, 60_000_000),
    ("가전·디지털",  "라이프스타일","SSG오픈마켓","오픈마켓", None, 0.07, 0.008, 0.023, 0.025, 340000, 180_000_000),
    ("리빙·주방",    "라이프스타일","SSG오픈마켓","오픈마켓", None, 0.12, 0.010, 0.023, 0.035, 71000, 85_000_000),
    ("유아동",       "라이프스타일","SSG오픈마켓","오픈마켓", None, 0.13, 0.010, 0.023, 0.040, 54000, 55_000_000),
    ("반려동물",     "라이프스타일","SSG오픈마켓","오픈마켓", None, 0.13, 0.010, 0.023, 0.020, 47000, 35_000_000),
]

# 프로모션 (자사분담액 = 총집행액 x 자사분담률)
PROMOS = [
    ("P2601", "설 선물세트 기획전",        date(2026,1,12), date(2026,1,25), "그로서리·브랜드패션", "신선식품·가공식품·명품·부티크", "카드 제휴할인", 420_000_000, 0.50, "설 명절 수요 대응, 카드사 공동 분담"),
    ("P2604", "유니버스 클럽 멤버십 위크",  date(2026,4,6),  date(2026,4,12), "전사",              "전 카테고리",                  "장바구니 쿠폰",  350_000_000, 0.70, "멤버십 가입 촉진 목적"),
    ("P2605", "새벽배송 장바구니 쿠폰 대전", date(2026,5,8),  date(2026,5,21), "그로서리",           "신선식품·가공식품·생수·음료·델리·베이커리", "장바구니 쿠폰", 870_000_000, 0.80, "새벽배송 신규 권역 확대 프로모션, 자사분담 80%"),
    ("P2606", "여름 가전 페스타",          date(2026,6,15), date(2026,6,28), "라이프스타일",       "가전·디지털",                  "즉시할인 쿠폰",  280_000_000, 0.60, "경쟁사 세일 대응"),
]

# 월별 성장 팩터 (카테고리별)
def month_factor(cat, m):
    grocery_growth = {1: 1.00, 2: 0.97, 3: 1.02, 4: 1.05, 5: 1.08, 6: 1.10}
    if cat in ("신선식품", "가공식품", "생수·음료", "델리·베이커리"):
        return grocery_growth[m]
    if cat == "명품·부티크":
        return {1: 1.18, 2: 0.92, 3: 0.95, 4: 1.00, 5: 1.15, 6: 0.98}[m]  # 설·가정의달 선물 수요
    if cat == "가전·디지털":
        return {1: 0.95, 2: 0.96, 3: 1.02, 4: 1.06, 5: 1.10, 6: 0.85}[m]  # 6월 역성장 (경쟁사 세일 잠식)
    if cat == "패션의류":
        return {1: 0.92, 2: 0.95, 3: 1.08, 4: 1.10, 5: 1.05, 6: 0.98}[m]
    return {1: 0.98, 2: 0.97, 3: 1.00, 4: 1.03, 5: 1.06, 6: 1.04}[m]

def promo_lift(cat, delivery, d):
    lift = 1.0
    for pid, _, s, e, _, targets, _, _, _, _ in PROMOS:
        if not (s <= d <= e):
            continue
        if pid == "P2601" and cat in ("신선식품", "가공식품", "명품·부티크"):
            lift *= 1.38
        elif pid == "P2604":
            lift *= 1.20
        elif pid == "P2605" and cat in ("신선식품", "가공식품", "생수·음료", "델리·베이커리"):
            lift *= 1.60 if delivery == "새벽배송" else 1.12  # 새벽배송 집중 + 쓱배송 후광
        elif pid == "P2606" and cat == "가전·디지털":
            lift *= 1.25
    return lift

def dow_factor(cat, d):
    wd = d.weekday()  # 0=월
    if cat in ("신선식품", "가공식품", "생수·음료", "델리·베이커리"):
        return [1.08, 1.00, 0.97, 0.98, 1.02, 1.10, 1.12][wd]  # 주말·월요일 장보기
    return [0.98, 0.97, 0.98, 1.00, 1.05, 1.10, 1.05][wd]

# --- 1) 매출실적 일별 ---
rows = []
d = START
while d <= END:
    for (cat, div, mall, buy, cost_r, fee_r, logi_r, pg_r, ret_r, aov, base) in CATS:
        deliveries = [("새벽배송", 0.45), ("쓱배송", 0.55)] if div == "그로서리" else [("택배배송", 1.0)]
        for delivery, share in deliveries:
            gmv = base * share * month_factor(cat, d.month) * dow_factor(cat, d) * promo_lift(cat, delivery, d)
            gmv *= random.uniform(0.93, 1.07)
            gmv = int(round(gmv, -4))
            if buy == "직매입":
                net = int(round(gmv * (1 - ret_r), -4))       # 상품매출 (반품 차감)
            else:
                net = int(round(gmv * fee_r, -4))              # 수수료 매출
            orders = max(1, int(gmv / (aov * random.uniform(0.9, 1.1))))
            rows.append([d.isoformat(), div, cat, delivery, gmv, net, orders])
    d += timedelta(days=1)

with open(OUT / "매출실적_일별_2026상반기.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["일자", "사업부", "카테고리", "배송유형", "거래액", "순매출", "주문건수"])
    w.writerows(rows)

# --- 2) 카테고리 마스터 ---
with open(OUT / "카테고리_마스터.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["카테고리", "사업부", "운영몰", "매입유형", "정산기준", "원가율", "판매수수료율", "물류변동비율", "결제수수료율", "반품율"])
    for (cat, div, mall, buy, cost_r, fee_r, logi_r, pg_r, ret_r, aov, base) in CATS:
        basis = "상품매출(총액)" if buy == "직매입" else "수수료매출(순액)"
        w.writerow([cat, div, mall, buy, basis, cost_r if cost_r else "", fee_r if fee_r else "", logi_r, pg_r, ret_r])

# --- 3) 프로모션 집행내역 ---
with open(OUT / "프로모션_집행내역_2026상반기.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["프로모션ID", "프로모션명", "시작일", "종료일", "대상사업부", "대상카테고리", "프로모션유형", "총집행액", "자사분담률", "자사분담액", "비고"])
    for pid, name, s, e, divs, targets, ptype, spend, share, note in PROMOS:
        w.writerow([pid, name, s.isoformat(), e.isoformat(), divs, targets, ptype, spend, share, int(round(spend * share, -4)), note])

# --- 4) 비용계획 (월별 고정비, 계획 vs 집행) ---
COST_PLAN = {  # 항목: (월 계획액, {월: 집행액})
    "인건비":            (1_400_000_000, {}),
    "물류센터 운영(고정)": (2_200_000_000, {}),
    "IT·시스템":         (800_000_000, {}),
    "마케팅·프로모션":    (600_000_000, {1: 760_000_000, 2: 480_000_000, 3: 520_000_000, 4: 810_000_000, 5: 1_340_000_000, 6: 900_000_000}),
    "지급수수료·기타":    (300_000_000, {}),
    "감가상각비":         (500_000_000, {}),
}
with open(OUT / "비용계획_2026.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["월", "비용항목", "계획액", "집행액", "비고"])
    for m in range(1, 13):
        for item, (plan, actual_map) in COST_PLAN.items():
            if m <= 6:
                actual = actual_map.get(m) or int(plan * random.uniform(0.96, 1.03))
                actual = int(round(actual, -6))
            else:
                actual = ""
            note = "프로모션 확대로 계획 초과" if (item == "마케팅·프로모션" and m == 5) else ""
            w.writerow([m, item, plan, actual, note])

# --- 검증: P2605 기간 그로서리 새벽배송 스파이크 ---
import statistics
promo_s, promo_e = date(2026, 5, 8), date(2026, 5, 21)
dawn = [(date.fromisoformat(r[0]), r[4]) for r in rows if r[3] == "새벽배송"]
in_p = [g for dd, g in dawn if promo_s <= dd <= promo_e]
base_may = [g for dd, g in dawn if dd.month == 5 and not (promo_s <= dd <= promo_e)]
lift = statistics.mean(in_p) / statistics.mean(base_may)
print(f"rows={len(rows)}")
print(f"P2605 새벽배송 GMV lift vs 5월 비프로모션: {lift:.2f}x (기준 +30% = 1.30 이상 필요)")
june_elec = statistics.mean([r[4] for r in rows if r[2] == "가전·디지털" and r[0][5:7] == "06"])
may_elec = statistics.mean([r[4] for r in rows if r[2] == "가전·디지털" and r[0][5:7] == "05"])
print(f"가전·디지털 6월/5월 일평균 GMV: {june_elec/may_elec:.2f}x (역성장 확인)")
