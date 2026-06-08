#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SWEETCH(스위치) AX Bootcamp 데모용 더미데이터 생성기.
실제 자사몰(sweetch.co.kr) 제품·가격 기반. 가방 브랜드.
채널: 자사몰 / 무신사 / 29CM / SSG / 면세점(B2B성)
페르소나: 권승현(MD) — 기획전 성과 분석.
"""
import csv
import random
from datetime import date, timedelta

random.seed(20260609)

OUT = "."

# ── 채널 정의 (실제 입점 채널 — 웹리서치 확인) ──────────────────
# fee_rate = 채널 판매수수료, price_factor = 자사몰 정가 대비 채널 판매가 배율
CHANNELS = {
    "자사몰":   {"code": "OWN", "fee": 0.035, "price_factor": 1.00, "weight": 0.29},
    "무신사":   {"code": "MUS", "fee": 0.30,  "price_factor": 1.00, "weight": 0.37},
    "29CM":    {"code": "29C", "fee": 0.28,  "price_factor": 1.00, "weight": 0.18},
    "SSG":     {"code": "SSG", "fee": 0.22,  "price_factor": 1.00, "weight": 0.10},
    "면세점":   {"code": "DTY", "fee": 0.10,  "price_factor": 0.78, "weight": 0.08},
}

# ── 제품 마스터 (실제 SWEETCH 라인업·정가 기반) ─────────────────
# (sku, 제품명, 라인, 카테고리, 정가, 자사몰할인율, 원가율)
PRODUCTS = [
    ("TOTE-001-WL", "TOTE BRIEF 001 WIDE L",      "Tote Brief", "토트백",   159000, 0.05, 0.34),
    ("TOTE-001-XS", "TOTE BRIEF 001 XS",          "Tote Brief", "토트백",    59000, 0.05, 0.36),
    ("VOY-DP-003",  "VOYAGER DAYPACK 003",        "Voyager",    "백팩",     119000, 0.15, 0.33),
    ("VOY-DMC-001", "VOYAGER DOUBLE MINI CROSS 001","Voyager",  "크로스백",  59000, 0.15, 0.37),
    ("CITY-RK-001S","CITY BOYS RUCKSACK 001 S",   "Cityboys",   "백팩",     185000, 0.10, 0.32),
    ("CITY-LC-001", "CITY BOYS LAPTOP CASE",      "Cityboys",   "노트북케이스",62000, 0.05, 0.35),
    ("SHD-BAG-M",   "SHOULDER BAG M",             "Glossy",     "숄더백",   109000, 0.05, 0.34),
    ("BOAT-TT-M",   "BOAT TOTE BAG M",            "Glossy",     "토트백",    89000, 0.05, 0.35),
    ("HDL-PCH-001", "HANDLE POUCH 001",           "Accessory",  "파우치",    25000, 0.00, 0.40),
    ("HDL-PCH-002", "HANDLE POUCH 002",           "Accessory",  "파우치",    25000, 0.00, 0.40),
    ("CAM-PCH-001", "CAMERA POUCH 001",           "Accessory",  "파우치",    35000, 0.05, 0.38),
    ("HLM-BAG-001", "HELMET BAG 001",             "Voyager",    "크로스백",  79000, 0.05, 0.36),
]

# 제품별 인기 가중치 (베스트셀러 TOTE BRIEF WIDE L 강세)
POP_WEIGHT = {
    "TOTE-001-WL": 0.20, "VOY-DP-003": 0.15, "VOY-DMC-001": 0.12,
    "CITY-RK-001S": 0.08, "TOTE-001-XS": 0.08, "BOAT-TT-M": 0.08,
    "SHD-BAG-M": 0.07, "CITY-LC-001": 0.06, "CAM-PCH-001": 0.05,
    "HDL-PCH-001": 0.05, "HDL-PCH-002": 0.04, "HLM-BAG-001": 0.02,
}

COLORS_BAG = ["Midnight Black", "Forest Green", "Cloud Cream", "Grape Grey",
              "Stone Grey", "Sand", "Summer Grey"]
COLORS_PCH = ["Black", "Cream", "Stone Grey", "Sand", "Silver", "Graphite"]

# ── 기획전(프로모션) 정의 — content.csv와 연동 ──────────────────
# 권승현 업무: "기획전별 매출·환불·순매출·이익 산출"
# 기획전 기간엔 주문 수 자체가 튀어야 분석에서 급등일로 검출됨
PROMOS = [
    # (기획전명, 시작, 끝, 대상SKU리스트, 일주문 부스트배율, 추가할인율)
    ("봄맞이 Voyager 신상 기획전", date(2026,5,3),  date(2026,5,5),
        ["VOY-DP-003","VOY-DMC-001","HLM-BAG-001"], 2.6, 0.10),
    ("무신사 단독 5월 블랙 위크",   date(2026,5,12), date(2026,5,14),
        ["TOTE-001-WL","CITY-RK-001S","SHD-BAG-M"], 2.8, 0.12),
    ("29CM 위클리 PICK",          date(2026,5,22), date(2026,5,23),
        ["BOAT-TT-M","TOTE-001-XS","CAM-PCH-001"], 4.2, 0.08),
    ("자사몰 회원의 날",           date(2026,5,28), date(2026,5,29),
        ["TOTE-001-WL","VOY-DP-003","HDL-PCH-001"], 3.0, 0.10),
]

START = date(2026, 5, 1)
END   = date(2026, 5, 31)

def daterange(a, b):
    d = a
    while d <= b:
        yield d
        d += timedelta(days=1)

def weighted_choice(d):
    keys = list(d.keys()); ws = list(d.values())
    return random.choices(keys, weights=ws, k=1)[0]

prod_by_sku = {p[0]: p for p in PRODUCTS}

def own_price(sku):
    p = prod_by_sku[sku]
    return round(p[4] * (1 - p[5]) / 50) * 50  # 자사몰 판매가(할인반영), 50원 단위

def channel_price(sku, ch):
    p = prod_by_sku[sku]
    base = own_price(sku) if ch == "자사몰" else round(p[4] / 50) * 50  # 외부는 정가 기준
    return round(base * CHANNELS[ch]["price_factor"] / 50) * 50

# ── 1) product_master.csv ─────────────────────────────────────
with open(f"{OUT}/product_master.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["sku","제품명","라인","카테고리","정가","자사몰판매가","원가",
                "무신사수수료율","29CM수수료율","SSG수수료율","면세점수수료율","자사몰수수료율"])
    for p in PRODUCTS:
        sku, name, line, cat, listp, disc, costr = p
        cost = round(listp * costr / 50) * 50
        w.writerow([sku, name, line, cat, listp, own_price(sku), cost,
                    CHANNELS["무신사"]["fee"], CHANNELS["29CM"]["fee"],
                    CHANNELS["SSG"]["fee"], CHANNELS["면세점"]["fee"],
                    CHANNELS["자사몰"]["fee"]])

# ── 2) sales.csv (주문 라인) ──────────────────────────────────
seq = {}
rows = []
def next_id(chcode, d):
    key = (chcode, d.strftime("%y%m%d"))
    seq[key] = seq.get(key, 0) + 1
    return f"{chcode}-{d.strftime('%y%m%d')}-{seq[key]:03d}"

REGIONS = ["서울","경기","부산","인천","대구","대전","광주","기타"]
ORDER_STATUS = ["결제완료","배송완료","배송완료","배송완료","교환","환불"]

for d in daterange(START, END):
    # 요일 효과 (주말 약간↑), 월말 페이 데이↑
    wd = d.weekday()
    day_factor = 1.0
    if wd >= 5: day_factor *= 1.15
    # 기획전 부스트
    active_promos = [pm for pm in PROMOS if pm[1] <= d <= pm[2]]
    boost = 1.0
    promo_skus = set()
    for pm in active_promos:
        boost = max(boost, pm[4])
        promo_skus |= set(pm[3])
    base_orders = int(random.gauss(22, 4) * day_factor * boost)
    base_orders = max(8, base_orders)

    for _ in range(base_orders):
        # 주문 단위로 채널·지역·상태 1회 결정
        ch = weighted_choice({k: v["weight"] for k, v in CHANNELS.items()})
        chcode = CHANNELS[ch]["code"]
        oid = next_id(chcode, d)
        region = random.choice(REGIONS)
        status = random.choices(ORDER_STATUS, weights=[10,40,40,4,3,3], k=1)[0]
        # 주문당 1~3 라인
        n_lines = random.choices([1,2,3], weights=[70,24,6], k=1)[0]
        # 기획전 중이면 대상 SKU로 집중
        for _l in range(n_lines):
            if promo_skus and random.random() < 0.72:
                sku = random.choice(list(promo_skus))
            else:
                sku = weighted_choice(POP_WEIGHT)
            p = prod_by_sku[sku]
            qty = random.choices([1,2], weights=[88,12], k=1)[0]
            unit = channel_price(sku, ch)
            # 기획전 추가할인
            extra_disc = 0.0
            for pm in active_promos:
                if sku in pm[3]:
                    extra_disc = max(extra_disc, pm[5])
            sale_unit = round(unit * (1 - extra_disc) / 50) * 50
            color = random.choice(COLORS_PCH if p[2]=="Accessory" else COLORS_BAG)
            promo_name = ""
            for pm in active_promos:
                if sku in pm[3]:
                    promo_name = pm[0]; break
            rows.append([oid, d.isoformat(), ch, sku, p[1], color, qty,
                         sale_unit, qty*sale_unit, status, region, promo_name])

random.shuffle(rows)  # 그래도 order_id 내부 일관성은 위에서 보장됨
with open(f"{OUT}/sales.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["order_id","주문일","채널","sku","제품명","색상","수량",
                "판매단가","판매금액","주문상태","배송지역","기획전"])
    for r in sorted(rows, key=lambda x: (x[1], x[0])):
        w.writerow(r)

# ── 3) content.csv (SNS 콘텐츠 + 기획전 일정) ──────────────────
CONTENT = []
# 기획전 → 콘텐츠 게시
for pm in PROMOS:
    CONTENT.append([pm[1].isoformat(), "기획전", pm[0], "전채널",
                    ",".join(pm[3]), "", "", "기획전 오픈"])
# 인스타 콘텐츠 (일부는 기획전 시작일과 겹쳐 매출 견인)
insta = [
    (date(2026,5,3),  "릴스",    "Voyager 신상 데일리 룩", "VOY-DP-003",  18400, 920, 142),
    (date(2026,5,8),  "피드",    "통근백 16인치 수납 리뷰", "TOTE-001-WL", 7300, 410, 33),
    (date(2026,5,12), "릴스",    "블랙 위크 하울",          "CITY-RK-001S",24100, 1510, 205),
    (date(2026,5,16), "스토리",  "주말 보트토트 코디",       "BOAT-TT-M",   5200, 230, 18),
    (date(2026,5,22), "캐러셀",  "29CM 컬러 8종 한눈에",    "BOAT-TT-M",   9800, 560, 71),
    (date(2026,5,25), "피드",    "파우치 정리 꿀팁",         "HDL-PCH-001", 6100, 330, 26),
    (date(2026,5,28), "릴스",    "회원의 날 베스트 모음",     "TOTE-001-WL", 21200, 1330, 188),
]
for d, typ, title, sku, reach, like, save in insta:
    CONTENT.append([d.isoformat(), typ, title, "인스타그램", sku, reach, like, save])

with open(f"{OUT}/content.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["게시일","유형","제목","채널","대상sku","도달수","좋아요","저장수"])
    for c in sorted(CONTENT, key=lambda x: x[0]):
        w.writerow(c)

# ── 4) inventory.csv (재고) ───────────────────────────────────
# 잘 나가는데 재고 바닥인 SKU 의도 배치 (베스트셀러 결품 위험)
INV_OVERRIDE = {
    "TOTE-001-WL": 38,   # 베스트셀러인데 재고 적음 → 경보
    "VOY-DP-003": 52,
    "CITY-RK-001S": 210, # 과재고
    "HDL-PCH-002": 480,  # 과재고
}
with open(f"{OUT}/inventory.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["sku","제품명","현재고","입고예정","입고리드타임(일)"])
    for p in PRODUCTS:
        sku = p[0]
        stock = INV_OVERRIDE.get(sku, random.randint(90, 340))
        incoming = random.choice([0, 0, 60, 120, 200])
        lead = random.choice([21, 28, 35, 45])  # 가방 생산 리드타임 김
        w.writerow([sku, p[1], stock, incoming, lead])

print("생성 완료: product_master.csv, sales.csv, content.csv, inventory.csv")
print(f"sales 라인 수: {len(rows)}")
