"""
그란데클립 의장 그룹 (5/26-27 캠프) 데모용 더미데이터 생성기.
4개 사업부 데이터 + 임원 보고용 통합 데이터를 같은 인프라에서 생성.

산출:
  amcr_sales.csv              어메이징크리 골프웨어 매출 (시즌·채널·SKU)
  amcr_product_master.csv     어메이징크리 상품 마스터
  amcr_inventory.csv          어메이징크리 시즌 재고 현황
  newmix_store_sales.csv      뉴믹스커피 성수·북촌 일매출
  newmix_menu_mix.csv         뉴믹스커피 메뉴별 판매
  magazine_c_issues.csv       매거진C 호별 판매·테마
  stayfolio_occupancy.csv     스테이폴리오 객실 점유율
  group_weekly_kpi.csv        그룹 통합 주간 KPI

규칙: utf-8-sig, random.seed 고정, 현실 패턴 (시즌·요일·매장 차이) 반영.
"""

import csv
import random
from datetime import date, timedelta
from pathlib import Path

random.seed(20260526)
OUT = Path(__file__).parent


# ───────────────────────────────────────────────────────────────
# 1. 어메이징크리 (AMCR) — 프리미엄 골프웨어. 그룹 매출 70%+
# ───────────────────────────────────────────────────────────────

AMCR_PRODUCTS = [
    # (sku, name, category, gender, season, cost, list_price)
    ("AMCR-SS-PT-101", "테크니컬 슬림 팬츠 / 화이트", "팬츠",   "여성", "SS25", 78000,  298000),
    ("AMCR-SS-PT-102", "테크니컬 슬림 팬츠 / 블랙",   "팬츠",   "여성", "SS25", 78000,  298000),
    ("AMCR-SS-PT-201", "스트레치 5포켓 팬츠 / 베이지",  "팬츠",   "남성", "SS25", 82000,  328000),
    ("AMCR-SS-PT-202", "스트레치 5포켓 팬츠 / 네이비",  "팬츠",   "남성", "SS25", 82000,  328000),
    ("AMCR-SS-TS-301", "메쉬 카라 반팔 티 / 화이트",   "상의",   "여성", "SS25", 42000,  198000),
    ("AMCR-SS-TS-302", "메쉬 카라 반팔 티 / 라일락",   "상의",   "여성", "SS25", 42000,  198000),
    ("AMCR-SS-TS-401", "쿨링 카라 반팔 티 / 차콜",     "상의",   "남성", "SS25", 45000,  218000),
    ("AMCR-SS-TS-402", "쿨링 카라 반팔 티 / 스카이",   "상의",   "남성", "SS25", 45000,  218000),
    ("AMCR-SS-SK-501", "플리츠 골프 스커트 / 화이트", "스커트", "여성", "SS25", 58000,  248000),
    ("AMCR-SS-SK-502", "플리츠 골프 스커트 / 네이비", "스커트", "여성", "SS25", 58000,  248000),
    ("AMCR-SS-OT-601", "경량 윈드 자켓 / 화이트",     "아우터", "여성", "SS25", 98000,  398000),
    ("AMCR-SS-OT-701", "경량 윈드 자켓 / 블랙",       "아우터", "남성", "SS25", 102000, 428000),
    ("AMCR-SS-AC-801", "선바이저 / 화이트",           "잡화",   "유니", "SS25", 12000,  68000),
    ("AMCR-SS-AC-802", "골프 글러브 / 블랙",           "잡화",   "유니", "SS25", 18000,  88000),
    # 캐리오버 (시즌 무관)
    ("AMCR-CR-PT-901", "데일리 골프 팬츠 / 블랙",     "팬츠",   "여성", "CARRY", 68000, 268000),
    ("AMCR-CR-TS-902", "베이직 카라 티 / 화이트",     "상의",   "여성", "CARRY", 38000, 178000),
    # 인기 SS25 추가 SKU
    ("AMCR-SS-PT-103", "테크니컬 슬림 팬츠 / 라이트그레이","팬츠","여성","SS25", 78000, 298000),
    ("AMCR-SS-DR-1001","원피스 골프 드레스 / 화이트", "원피스","여성","SS25", 72000, 348000),
]

AMCR_CHANNELS = [
    # (code, name, commission_rate, weight)
    ("DTC", "자사몰",              0.00, 0.22),
    ("LOTW","롯데백화점",         0.32, 0.15),
    ("SHIN","신세계백화점",       0.32, 0.13),
    ("HYUN","현대백화점",         0.30, 0.11),
    ("GLPS","골프장 프로샵",      0.25, 0.12),
    ("KKLB","카카오톡 선물하기",  0.18, 0.06),
    ("ZGZG","지그재그",            0.20, 0.05),
    ("USA", "해외(미국)",          0.20, 0.08),
    ("JPN", "해외(일본)",          0.22, 0.08),
]

def _amcr_discount(channel, sku_season):
    """채널·시즌별 평균 할인율"""
    if channel == "DTC":         return random.choice([0, 0, 0, 0.10, 0.15])
    if channel in ("LOTW","SHIN","HYUN"): return random.choice([0, 0, 0.05, 0.10])
    if channel == "GLPS":        return random.choice([0, 0.10])
    if channel == "KKLB":        return random.choice([0.10, 0.15, 0.20])
    if channel == "ZGZG":        return random.choice([0.15, 0.20, 0.25])
    return random.choice([0, 0.05])  # 해외


def gen_amcr_sales():
    """4월 1주~5월 4주 어메이징크리 매출 (SS25 시즌 피크 반영)"""
    rows = []
    order_seq = {ch[0]: 0 for ch in AMCR_CHANNELS}
    start = date(2026, 4, 1)
    end   = date(2026, 5, 24)
    cur = start
    while cur <= end:
        # 요일·시즌 가중치
        dow = cur.weekday()
        weekend_boost = 1.35 if dow >= 5 else 1.0
        # 5월 중순부터 SS 시즌 피크
        season_boost = 1.0 + max(0, (cur - date(2026, 5, 8)).days * 0.025)
        # 어린이날·가정의 달 4월 말~5월 초 작은 스파이크
        if date(2026, 4, 28) <= cur <= date(2026, 5, 8):
            season_boost *= 1.15
        # 비 오는 주말 시뮬레이션 (4월 셋째주 주말)
        if cur in (date(2026, 4, 19), date(2026, 4, 20)):
            season_boost *= 0.55

        # 하루 주문 건수
        base_orders = 95
        n_orders = int(base_orders * weekend_boost * season_boost * random.uniform(0.85, 1.18))

        for _ in range(n_orders):
            ch = random.choices(
                [c[0] for c in AMCR_CHANNELS],
                weights=[c[3] for c in AMCR_CHANNELS]
            )[0]
            ch_info = next(c for c in AMCR_CHANNELS if c[0] == ch)
            order_seq[ch] += 1
            yymm = cur.strftime("%y%m")
            dd = cur.strftime("%d")
            order_id = f"{ch}-{yymm}{dd}-{order_seq[ch]:04d}"

            # 주문당 상품 수 (1~3)
            n_items = random.choices([1, 2, 3], weights=[0.62, 0.30, 0.08])[0]
            for line_no in range(1, n_items + 1):
                product = random.choice(AMCR_PRODUCTS)
                sku, name, cat, gender, season, cost, list_price = product
                # 시즌 SKU에 가중치 (4~5월 SS25 70% / CARRY 30%)
                if season == "CARRY" and random.random() > 0.30:
                    product = random.choice([p for p in AMCR_PRODUCTS if p[4] == "SS25"])
                    sku, name, cat, gender, season, cost, list_price = product

                disc = _amcr_discount(ch, season)
                unit_price = round(list_price * (1 - disc) / 100) * 100
                qty = random.choices([1, 1, 1, 2], weights=[0.78, 0.08, 0.08, 0.06])[0]
                amount = unit_price * qty

                rows.append({
                    "order_id": order_id,
                    "order_date": cur.isoformat(),
                    "channel_code": ch,
                    "channel_name": ch_info[1],
                    "line_no": line_no,
                    "sku": sku,
                    "product_name": name,
                    "category": cat,
                    "gender": gender,
                    "season": season,
                    "list_price": list_price,
                    "unit_price": unit_price,
                    "discount_rate": disc,
                    "qty": qty,
                    "amount": amount,
                    "commission_rate": ch_info[2],
                })
        cur += timedelta(days=1)

    with open(OUT / "amcr_sales.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"amcr_sales.csv: {len(rows)}건")


def gen_amcr_product_master():
    rows = []
    for sku, name, cat, gender, season, cost, list_price in AMCR_PRODUCTS:
        rows.append({
            "sku": sku,
            "product_name": name,
            "category": cat,
            "gender": gender,
            "season": season,
            "list_price": list_price,
            "cost": cost,
            "margin_rate": round((list_price - cost) / list_price, 3),
            "launch_date": "2026-03-01" if season == "SS25" else "2025-09-01",
        })
    with open(OUT / "amcr_product_master.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"amcr_product_master.csv: {len(rows)}건")


def gen_amcr_inventory():
    """5/24 기준 시즌 재고 — 인기 SKU 일부 품절 임박, 캐리오버 과재고"""
    rows = []
    for sku, name, cat, gender, season, cost, list_price in AMCR_PRODUCTS:
        # 인기 SKU 시뮬: 슬림팬츠 화이트·메쉬티 라일락은 재고 부족
        if sku in ("AMCR-SS-PT-101", "AMCR-SS-TS-302", "AMCR-SS-PT-103"):
            on_hand = random.randint(28, 65)
            weekly_sellout = random.randint(45, 78)
        elif season == "CARRY":
            on_hand = random.randint(380, 620)
            weekly_sellout = random.randint(18, 35)
        else:
            on_hand = random.randint(180, 480)
            weekly_sellout = random.randint(35, 95)
        wos = round(on_hand / max(weekly_sellout, 1), 1)  # weeks of stock
        rows.append({
            "snapshot_date": "2026-05-24",
            "sku": sku,
            "product_name": name,
            "category": cat,
            "season": season,
            "on_hand_qty": on_hand,
            "weekly_sellout_qty": weekly_sellout,
            "weeks_of_stock": wos,
            "status": "긴급보충" if wos < 1.0 else ("주의" if wos < 2.5 else ("과재고" if wos > 12 else "정상")),
        })
    with open(OUT / "amcr_inventory.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"amcr_inventory.csv: {len(rows)}건")


# ───────────────────────────────────────────────────────────────
# 2. 뉴믹스커피 — 성수·북촌 일매출 (그란데클립FnB)
# ───────────────────────────────────────────────────────────────

NEWMIX_MENU = [
    # (code, name, category, price, cost)
    ("NM-COF-001", "아메리카노",          "커피",   5500,  1100),
    ("NM-COF-002", "라떼",                "커피",   6500,  1500),
    ("NM-MIX-001", "뉴믹스 오리지널",    "믹스",   6800,  1700),
    ("NM-MIX-002", "뉴믹스 말차",         "믹스",   7500,  2000),
    ("NM-MIX-003", "뉴믹스 약과",         "믹스",   7500,  2100),
    ("NM-MIX-004", "뉴믹스 군밤",         "믹스",   7500,  2000),
    ("NM-MIX-005", "뉴믹스 현미",         "믹스",   7200,  1900),
    ("NM-DST-001", "약과 디저트 세트",    "디저트", 8500,  2400),
    ("NM-DST-002", "쿠키",                 "디저트", 4500,  1100),
    ("NM-RTL-001", "뉴믹스 스틱 5입",     "리테일", 12000, 3600),
    ("NM-RTL-002", "뉴믹스 기프트 박스",  "리테일", 38000, 11500),
]

def gen_newmix_store_sales():
    """5/1 ~ 5/24 일매출 — 성수(외국인 비중↑) vs 북촌(주말 가족↑)"""
    rows = []
    start = date(2026, 5, 1)
    end   = date(2026, 5, 24)
    cur = start
    while cur <= end:
        dow = cur.weekday()
        weekend = dow >= 5
        # 성수
        seongsu_orders = int(random.uniform(165, 245) * (1.18 if weekend else 1.0))
        seongsu_revenue = seongsu_orders * random.uniform(8800, 11200)
        seongsu_foreign = random.uniform(0.28, 0.42)
        # 북촌
        bukchon_orders = int(random.uniform(135, 205) * (1.35 if weekend else 1.0))
        bukchon_revenue = bukchon_orders * random.uniform(9800, 12500)
        bukchon_foreign = random.uniform(0.18, 0.28)

        rows.append({
            "date": cur.isoformat(),
            "store": "성수",
            "orders": seongsu_orders,
            "revenue": int(seongsu_revenue),
            "avg_ticket": int(seongsu_revenue / seongsu_orders),
            "foreign_ratio": round(seongsu_foreign, 3),
            "weather": random.choice(["맑음", "맑음", "흐림", "맑음", "비"]),
        })
        rows.append({
            "date": cur.isoformat(),
            "store": "북촌",
            "orders": bukchon_orders,
            "revenue": int(bukchon_revenue),
            "avg_ticket": int(bukchon_revenue / bukchon_orders),
            "foreign_ratio": round(bukchon_foreign, 3),
            "weather": random.choice(["맑음", "맑음", "흐림", "맑음", "비"]),
        })
        cur += timedelta(days=1)

    with open(OUT / "newmix_store_sales.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"newmix_store_sales.csv: {len(rows)}건")


def gen_newmix_menu_mix():
    """5월 1~24일 메뉴별 판매수량 (매장별)"""
    rows = []
    for store, weight_shift in [("성수", {"NM-MIX-001": 1.35, "NM-RTL-001": 1.5, "NM-RTL-002": 1.6}),
                                  ("북촌", {"NM-DST-001": 1.45, "NM-MIX-002": 1.20})]:
        for sku, name, cat, price, cost in NEWMIX_MENU:
            base_qty = {
                "커피": 1100, "믹스": 850, "디저트": 380, "리테일": 95,
            }[cat]
            qty = int(base_qty * weight_shift.get(sku, 1.0) * random.uniform(0.78, 1.22))
            rows.append({
                "period": "2026-05-01~24",
                "store": store,
                "sku": sku,
                "menu_name": name,
                "category": cat,
                "unit_price": price,
                "unit_cost": cost,
                "qty_sold": qty,
                "revenue": qty * price,
            })
    with open(OUT / "newmix_menu_mix.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"newmix_menu_mix.csv: {len(rows)}건")


# ───────────────────────────────────────────────────────────────
# 3. 매거진C — 의자 다큐 잡지
# ───────────────────────────────────────────────────────────────

def gen_magazine_c_issues():
    issues = [
        # (vol, title, theme_chair, theme_designer, pub_date, kr_sold, intl_sold, retail_kr, retail_intl)
        ("Vol.10", "그리고 다시 의자",       "Eames Lounge Chair",   "Charles & Ray Eames", "2025-03", 4800, 1850, 24000, 38000),
        ("Vol.11", "공간이 앉는 자세",       "Wishbone Chair",        "Hans Wegner",          "2025-06", 5250, 2100, 24000, 38000),
        ("Vol.12", "오피스의 의자",          "Aeron Chair",           "Bill Stumpf",          "2025-09", 4920, 2350, 26000, 42000),
        ("Vol.13", "흙으로 빚은 의자",       "Ant Chair",             "Arne Jacobsen",        "2025-12", 5380, 2680, 26000, 42000),
        ("Vol.14", "여행 가방 옆 의자",      "Folding Chair",         "Achille Castiglioni",  "2026-03", 5650, 2890, 26000, 42000),
        ("Vol.15", "(준비중)",                "TBD",                    "TBD",                  "2026-06", 0,    0,    26000, 42000),
    ]
    rows = []
    for vol, title, chair, designer, pub, kr, intl, rp_kr, rp_intl in issues:
        sub_kr = int(kr * random.uniform(0.18, 0.32))
        rows.append({
            "volume": vol,
            "title": title,
            "feature_chair": chair,
            "feature_designer": designer,
            "publish_month": pub,
            "kr_sold_qty": kr,
            "intl_sold_qty": intl,
            "total_sold": kr + intl,
            "subscriber_sold": sub_kr,
            "retail_price_kr": rp_kr,
            "retail_price_intl": rp_intl,
            "revenue_estimated": kr * rp_kr + intl * rp_intl,
        })
    with open(OUT / "magazine_c_issues.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"magazine_c_issues.csv: {len(rows)}건")


# ───────────────────────────────────────────────────────────────
# 4. 스테이폴리오 — 객실 점유율
# ───────────────────────────────────────────────────────────────

def gen_stayfolio_occupancy():
    properties = [
        # (code, name, country, rooms, weekday_adr, weekend_adr)
        ("SF-KR-001", "삼청동 한옥 / 청류재",    "한국",     1,  450000, 580000),
        ("SF-KR-002", "제주 애월 / 빌라 모노",   "한국",     3,  280000, 380000),
        ("SF-KR-003", "강릉 솔내음 한옥",        "한국",     2,  240000, 320000),
        ("SF-JP-001", "교토 마치야 / 시조",       "일본",     2,  320000, 420000),
        ("SF-JP-002", "후쿠오카 야나기 게스트",   "일본",     4,  180000, 240000),
        ("SF-TW-001", "타이베이 / 가오슝 빌라",   "대만",     3,  220000, 290000),
        ("SF-TH-001", "치앙마이 / 정원 빌라",     "태국",     5,  150000, 200000),
        ("SF-VN-001", "다낭 / 오션뷰 빌라",       "베트남",   4,  170000, 240000),
    ]
    rows = []
    for code, name, country, rooms, wkd_adr, wkn_adr in properties:
        # 5월 1~24일 점유율
        wkd_nights, wkn_nights = 0, 0
        wkd_capacity, wkn_capacity = 0, 0
        d = date(2026, 5, 1)
        while d <= date(2026, 5, 24):
            is_weekend = d.weekday() >= 5
            if is_weekend:
                wkn_capacity += rooms
                wkn_nights += min(rooms, int(rooms * random.uniform(0.78, 0.98)))
            else:
                wkd_capacity += rooms
                wkd_nights += min(rooms, int(rooms * random.uniform(0.42, 0.72)))
            d += timedelta(days=1)
        total_nights = wkd_nights + wkn_nights
        total_capacity = wkd_capacity + wkn_capacity
        revenue = wkd_nights * wkd_adr + wkn_nights * wkn_adr
        rows.append({
            "property_code": code,
            "property_name": name,
            "country": country,
            "rooms": rooms,
            "period": "2026-05-01~24",
            "weekday_adr": wkd_adr,
            "weekend_adr": wkn_adr,
            "weekday_nights_sold": wkd_nights,
            "weekend_nights_sold": wkn_nights,
            "total_nights_sold": total_nights,
            "total_capacity": total_capacity,
            "occupancy_rate": round(total_nights / total_capacity, 3),
            "revenue": revenue,
        })
    with open(OUT / "stayfolio_occupancy.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"stayfolio_occupancy.csv: {len(rows)}건")


# ───────────────────────────────────────────────────────────────
# 5. 그룹 통합 주간 KPI — 의장 보고용
# ───────────────────────────────────────────────────────────────

def gen_group_weekly_kpi():
    """ISO week 단위. 2026 W14~W21 (4월 첫 주 ~ 5월 셋째 주)"""
    rows = []
    weeks = [
        # (week_label, period_start, period_end)
        ("W14", "2026-04-01", "2026-04-05"),  # (partial)
        ("W15", "2026-04-06", "2026-04-12"),
        ("W16", "2026-04-13", "2026-04-19"),
        ("W17", "2026-04-20", "2026-04-26"),
        ("W18", "2026-04-27", "2026-05-03"),
        ("W19", "2026-05-04", "2026-05-10"),
        ("W20", "2026-05-11", "2026-05-17"),
        ("W21", "2026-05-18", "2026-05-24"),
    ]
    # 어메이징크리 주간 매출 시뮬 (월 합 ~50~60억 가정, 시즌 피크 W19~21)
    base_amcr = 1_080_000_000
    base_newmix = 145_000_000
    base_magc = 12_000_000
    base_stay = 38_000_000

    for i, (lbl, ps, pe) in enumerate(weeks):
        # AMCR — 시즌 피크 우상향, W16에 비 영향 소폭 디핀
        amcr_factor = 1.0 + i * 0.06 + random.uniform(-0.04, 0.04)
        if lbl == "W16":
            amcr_factor *= 0.78
        amcr_rev = int(base_amcr * amcr_factor)
        # 뉴믹스 — 외국인 관광객 영향 안정적, 5월 가정의 달 살짝
        newmix_factor = 1.0 + (0.08 if lbl in ("W18", "W19") else 0) + random.uniform(-0.05, 0.05)
        newmix_rev = int(base_newmix * newmix_factor / 4)  # 주단위로
        # 매거진C — 분기 발행. W21 Vol.14 후속 매출
        magc_rev = base_magc if lbl in ("W18", "W19", "W20") else int(base_magc * 0.3)
        # 스테이폴리오 — 봄 시즌 강세
        stay_factor = 1.0 + (0.15 if lbl in ("W18", "W19", "W20") else 0)
        stay_rev = int(base_stay * stay_factor / 4)

        total = amcr_rev + newmix_rev + magc_rev + stay_rev
        rows.append({
            "week": lbl,
            "period_start": ps,
            "period_end": pe,
            "amcr_revenue": amcr_rev,
            "newmix_revenue": newmix_rev,
            "magazine_c_revenue": magc_rev,
            "stayfolio_revenue": stay_rev,
            "group_total_revenue": total,
            "amcr_share": round(amcr_rev / total, 3),
            "newmix_orders": int(newmix_rev / 11000),
            "stayfolio_occupancy_avg": round(random.uniform(0.55, 0.72), 3),
            "magazine_c_subscriber_growth": random.randint(-12, 38),
        })
    with open(OUT / "group_weekly_kpi.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    print(f"group_weekly_kpi.csv: {len(rows)}건")


if __name__ == "__main__":
    gen_amcr_sales()
    gen_amcr_product_master()
    gen_amcr_inventory()
    gen_newmix_store_sales()
    gen_newmix_menu_mix()
    gen_magazine_c_issues()
    gen_stayfolio_occupancy()
    gen_group_weekly_kpi()
    print("\nAll CSVs generated.")
