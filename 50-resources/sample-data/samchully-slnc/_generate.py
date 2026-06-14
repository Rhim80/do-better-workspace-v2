#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
삼천리 SL&C(외식 사업부) AX Bootcamp 데모용 더미데이터 생성기.

실제 확인된 브랜드 5종(Chai797·호우섬·서리재·바른고기 정육점·이타마에 스시) 기반.
채널: 오피스 상권 / 백화점·쇼핑몰 / 로드샵 (리서치 확인값).

생성 파일:
  store_master.csv  - 매장 마스터 (브랜드·채널·상권·임대료·BEP·변동비율)
  menu_master.csv   - 메뉴 마스터 (브랜드·카테고리·판매가·원가율)
  pos_sales.csv     - POS 일매출 (매장×일자×메뉴카테고리)  [Q1 2026]
  promotions.csv    - 신메뉴·행사 일정 (매출 급등 원인)
  trade_area.csv    - 상권/출점 후보지 비교 (기존 매장 + 신규 후보)

스파이크: 신메뉴 출시·행사일에 해당 브랜드 매장의 그날 객수를 끌어올려
일 총매출이 평소 평균 대비 +30% 이상 분명히 넘게 설계 (생성 후 검증).
"""
import csv, random, datetime, statistics
from pathlib import Path

random.seed(42)
OUT = Path(__file__).parent

# ----------------------------------------------------------------------------
# 1. 브랜드 정의 (리서치 확인 — Chai797/호우섬/서리재/바른고기정육점/이타마에스시)
# ----------------------------------------------------------------------------
# 객단가(점심 기준 추정), 브랜드 코드
BRANDS = {
    "Chai797":       {"code": "CH", "avg_ticket": 38000, "tier": "프리미엄"},
    "호우섬":         {"code": "HS", "avg_ticket": 32000, "tier": "캐주얼"},
    "서리재":         {"code": "SR", "avg_ticket": 45000, "tier": "프리미엄"},
    "바른고기 정육점":  {"code": "BG", "avg_ticket": 52000, "tier": "프리미엄"},
    "이타마에 스시":    {"code": "IT", "avg_ticket": 68000, "tier": "파인다이닝"},
}

# 채널: 임대료 수준·수수료(백화점만)·요일 가중 다름
CHANNELS = {
    "오피스상권":      {"rent_idx": 1.00, "fee_rate": 0.00, "weekday_bias": 1.25},  # 평일 점심 강세
    "백화점·쇼핑몰":   {"rent_idx": 1.55, "fee_rate": 0.14, "weekday_bias": 0.85},  # 주말 강세 + 입점수수료
    "로드샵":         {"rent_idx": 0.80, "fee_rate": 0.00, "weekday_bias": 1.00},
}

# ----------------------------------------------------------------------------
# 2. 매장 마스터 (확인된 입점 위치 기반 — 25개 직영 매장)
# ----------------------------------------------------------------------------
# (브랜드, 매장명, 채널, 상권, 좌석수, 일평균객수기준)
STORES_RAW = [
    # Chai797 — 오피스 상권 핵심 + 백화점 Plus
    ("Chai797", "여의도IFC점",    "오피스상권",    "여의도",   120, 210),
    ("Chai797", "센터원점",       "오피스상권",    "종로",     110, 195),
    ("Chai797", "강남파이낸스점",  "오피스상권",    "강남역",   130, 230),
    ("Chai797", "더현대서울점",    "백화점·쇼핑몰",  "여의도",   90,  175),
    ("Chai797", "스타필드수원점",  "백화점·쇼핑몰",  "수원",     95,  150),
    ("Chai797", "을지로센터점",    "오피스상권",    "을지로",   85,  44),   # 부진 매장 (BEP 미달)
    # 호우섬 — 백화점·쇼핑몰 중심
    ("호우섬",   "더현대서울점",    "백화점·쇼핑몰",  "여의도",   80,  220),
    ("호우섬",   "코엑스몰점",      "백화점·쇼핑몰",  "삼성",     85,  205),
    ("호우섬",   "현대판교점",      "백화점·쇼핑몰",  "판교",     75,  160),
    ("호우섬",   "신세계대전점",    "백화점·쇼핑몰",  "대전",     70,  43),   # 부진 매장 (BEP 미달)
    ("호우섬",   "롯데명동점",      "백화점·쇼핑몰",  "명동",     78,  140),
    # 서리재 — 오피스 + 로드샵
    ("서리재",   "광화문점",       "오피스상권",    "광화문",   90,  130),
    ("서리재",   "삼성동점",       "오피스상권",    "삼성",     85,  120),
    ("서리재",   "해운대점",       "로드샵",        "부산",     95,  33),   # 부진 매장 (BEP 미달, 계절 편차)
    # 바른고기 정육점 — 오피스 상권
    ("바른고기 정육점", "강남점",   "오피스상권",    "강남역",   70,  95),
    ("바른고기 정육점", "을지로점", "오피스상권",    "을지로",   65,  82),
    ("바른고기 정육점", "여의도점", "오피스상권",    "여의도",   72,  98),
    # 이타마에 스시 — 파인다이닝, 백화점·오피스 프리미엄
    ("이타마에 스시", "광화문디타워점", "오피스상권",  "광화문",   38,  52),
    ("이타마에 스시", "롯데월드몰점",  "백화점·쇼핑몰", "잠실",     40,  60),
    ("이타마에 스시", "현대판교점",   "백화점·쇼핑몰",  "판교",     36,  44),
    ("이타마에 스시", "도곡점",      "로드샵",        "도곡",     34,  40),
    # 추가 오피스 매장 (규모 맞춤)
    ("Chai797", "판교테크원점",    "오피스상권",    "판교",     105, 165),
    ("호우섬",   "롯데월드몰점",    "백화점·쇼핑몰",  "잠실",     82,  170),
    ("서리재",   "여의도점",       "오피스상권",    "여의도",   88,  115),
    ("바른고기 정육점", "판교점",   "오피스상권",    "판교",     68,  88),
]

stores = []
for i, (brand, name, channel, area, seats, base_cust) in enumerate(STORES_RAW, 1):
    bcode = BRANDS[brand]["code"]
    store_id = f"{bcode}-{i:03d}"
    rent_idx = CHANNELS[channel]["rent_idx"]
    # 월 임대료(만원): 좌석·채널 임대지수 기반 추정
    monthly_rent = round(seats * 9 * rent_idx / 10) * 10  # 만원 단위
    # 변동비율(식자재+카드수수료+포장 등): 브랜드 tier별
    tier = BRANDS[brand]["tier"]
    var_cost_rate = {"캐주얼": 0.42, "프리미엄": 0.38, "파인다이닝": 0.45}[tier]
    # 손익분기 일객수(BEP): 임대+인건 고정비를 객단가·기여로 나눈 추정
    avg_ticket = BRANDS[brand]["avg_ticket"]
    fixed_monthly = monthly_rent * 10000 + seats * 28 * 10000  # 임대 + 인건(좌석당 추정)
    contrib_per_guest = avg_ticket * (1 - var_cost_rate)
    bep_daily = round(fixed_monthly / 26 / contrib_per_guest)  # 월 26영업일
    stores.append({
        "store_id": store_id, "brand": brand, "store_name": name,
        "channel": channel, "trade_area": area, "seats": seats,
        "monthly_rent_manwon": monthly_rent,
        "var_cost_rate": var_cost_rate,
        "bep_daily_guests": bep_daily,
        "_base_cust": base_cust, "_avg_ticket": avg_ticket,
        "_fee_rate": CHANNELS[channel]["fee_rate"],
        "_weekday_bias": CHANNELS[channel]["weekday_bias"],
    })

with open(OUT / "store_master.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["store_id","brand","store_name","channel","trade_area",
                "seats","monthly_rent_manwon","var_cost_rate","bep_daily_guests"])
    for s in stores:
        w.writerow([s["store_id"],s["brand"],s["store_name"],s["channel"],
                    s["trade_area"],s["seats"],s["monthly_rent_manwon"],
                    s["var_cost_rate"],s["bep_daily_guests"]])

# ----------------------------------------------------------------------------
# 3. 메뉴 마스터 (브랜드별 카테고리 + 대표메뉴, 판매가·원가율)
# ----------------------------------------------------------------------------
MENU = [
    # (브랜드, 카테고리, 대표메뉴, 판매가, 원가율)
    ("Chai797","딤섬","하가우",13000,0.30),
    ("Chai797","요리","호두꿀크림 중새우",53000,0.36),
    ("Chai797","면·밥","해물짬뽕",16000,0.28),
    ("Chai797","코스","런치코스",45000,0.34),
    ("호우섬","딤섬","새우완탕",11000,0.31),
    ("호우섬","면·밥","XO볶음밥",14000,0.27),
    ("호우섬","요리","멘보샤",24000,0.38),
    ("호우섬","음료·주류","칭따오",8000,0.22),
    ("서리재","구이","꽃등심구이",58000,0.42),
    ("서리재","구이","차돌박이",36000,0.40),
    ("서리재","식사","된장찌개",12000,0.25),
    ("서리재","주류","소주",5000,0.18),
    ("바른고기 정육점","한우구이","한우등심",72000,0.48),
    ("바른고기 정육점","한우구이","한우안창",58000,0.46),
    ("바른고기 정육점","식사","한우비빔밥",18000,0.30),
    ("바른고기 정육점","주류","와인글라스",15000,0.25),
    ("이타마에 스시","오마카세","런치 오마카세",90000,0.46),
    ("이타마에 스시","오마카세","디너 오마카세",180000,0.48),
    ("이타마에 스시","단품","스시 세트",55000,0.42),
    ("이타마에 스시","주류","사케",18000,0.28),
]
with open(OUT / "menu_master.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["brand","category","menu_name","price_krw","cost_rate"])
    for row in MENU:
        w.writerow(row)

# 브랜드별 카테고리 집계용 가중치 (매출 믹스)
from collections import defaultdict
brand_cats = defaultdict(list)
for brand, cat, menu, price, cost in MENU:
    brand_cats[brand].append((cat, price, cost))
# 카테고리 단위 평균 단가/원가율 (중복 카테고리 평균)
brand_cat_stats = {}
for brand, items in brand_cats.items():
    cat_map = defaultdict(list)
    for cat, price, cost in items:
        cat_map[cat].append((price, cost))
    brand_cat_stats[brand] = {
        cat: (statistics.mean(p for p,_ in v), statistics.mean(c for _,c in v))
        for cat, v in cat_map.items()
    }

# ----------------------------------------------------------------------------
# 4. 프로모션·신메뉴 일정 (매출 급등 원인) — Q1 2026
# ----------------------------------------------------------------------------
# (시작일, 종료일, 브랜드, 유형, 명칭, 부스트배율)
PROMOS = [
    ("2026-01-15","2026-01-31","이타마에 스시","신메뉴","겨울 제철 오마카세 개편", 1.9),
    ("2026-02-01","2026-02-14","Chai797","행사","발렌타인 딤섬 페어", 1.7),
    ("2026-02-09","2026-02-18","서리재","행사","설 한우 프로모션", 2.0),
    ("2026-03-02","2026-03-15","호우섬","신메뉴","봄 시즌 딤섬 3종 출시", 1.8),
    ("2026-03-20","2026-03-31","바른고기 정육점","행사","화이트데이 한우 디너세트", 1.6),
]
with open(OUT / "promotions.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["start_date","end_date","brand","promo_type","promo_name"])
    for row in PROMOS:
        w.writerow(row[:5])  # boost는 내부용, csv엔 노출 안 함

def promo_boost(brand, d):
    """해당 브랜드·날짜에 적용되는 부스트 배율 (없으면 1.0)."""
    b = 1.0
    for s,e,pb,_,_,boost in PROMOS:
        sd = datetime.date.fromisoformat(s); ed = datetime.date.fromisoformat(e)
        if pb == brand and sd <= d <= ed:
            b = max(b, boost)
    return b

# ----------------------------------------------------------------------------
# 5. POS 일매출 생성 (매장 × 영업일 × 메뉴카테고리)  Q1 2026
# ----------------------------------------------------------------------------
start = datetime.date(2026,1,1)
end   = datetime.date(2026,3,31)
days = [start + datetime.timedelta(d) for d in range((end-start).days+1)]

# 주문번호: {채널코드}-{YYMMDD}-{순번}  (POS는 일 매출 라인 단위라 batch id 사용)
CH_CODE = {"오피스상권":"OF","백화점·쇼핑몰":"DP","로드샵":"RD"}

rows = []
batch_seq = defaultdict(int)
for s in stores:
    brand = s["brand"]
    base = s["_base_cust"]
    ticket = s["_avg_ticket"]
    wbias = s["_weekday_bias"]
    cats = brand_cat_stats[brand]
    # 카테고리별 매출 믹스 가중치 (대표메뉴 단가 기반 정규화)
    cat_weights = {c:1.0 for c in cats}  # 균등 베이스, 일부 조정
    for d in days:
        dow = d.weekday()  # 0=월
        # 요일 패턴: 오피스는 평일점심 강세(월~금↑, 주말↓), 백화점은 주말↑
        if s["channel"] == "오피스상권":
            dow_f = 1.18 if dow < 5 else 0.45
        elif s["channel"] == "백화점·쇼핑몰":
            dow_f = 0.92 if dow < 5 else 1.45
        else:  # 로드샵
            dow_f = 0.95 if dow < 5 else 1.35
        # 시즌: 설 연휴(2/16-18 추정) 소폭 하락 오피스, 1월초 신년 약세
        season_f = 1.0
        if datetime.date(2026,2,16) <= d <= datetime.date(2026,2,18):
            season_f = 0.6 if s["channel"]=="오피스상권" else 1.1
        if d <= datetime.date(2026,1,3):
            season_f *= 0.7
        boost = promo_boost(brand, d)
        # 그날 객수 — 부스트는 객수 자체를 끌어올림(일 총매출이 +30% 넘게)
        noise = random.uniform(0.88, 1.12)
        guests = round(base * dow_f * season_f * boost * noise)
        if guests <= 0:
            continue
        # 배치 주문번호
        batch_seq[s["channel"]] += 1
        chc = CH_CODE[s["channel"]]
        batch_id = f"{chc}-{d:%y%m%d}-{batch_seq[s['channel']]:04d}"
        # 카테고리별로 매출 분배 (객수 기준 + 단가)
        n_cat = len(cats)
        for cat,(price,cost) in cats.items():
            # 카테고리 객수 비중 (균등 + 노이즈)
            cat_share = (1.0/n_cat) * random.uniform(0.7,1.3)
            cat_guests = max(1, round(guests * cat_share))
            # 객단가는 메뉴 카테고리 단가 근처에서 변동
            unit = round(price * random.uniform(0.9,1.15) / 100) * 100
            gross = cat_guests * unit
            fee = round(gross * s["_fee_rate"])
            food_cost = round(gross * cost)
            rows.append([
                batch_id, d.isoformat(), s["store_id"], brand, s["store_name"],
                s["channel"], s["trade_area"], cat, cat_guests, unit,
                gross, fee, food_cost,
            ])

with open(OUT / "pos_sales.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["order_batch_id","date","store_id","brand","store_name",
                "channel","trade_area","menu_category","guests","avg_unit_krw",
                "gross_sales_krw","channel_fee_krw","food_cost_krw"])
    w.writerows(rows)

# ----------------------------------------------------------------------------
# 6. 상권/출점 후보지 비교 (기존 매장 상권 + 신규 후보)
# ----------------------------------------------------------------------------
# (상권명, 유형[기존/후보], 일유동인구(천명), 오피스인구(천명), 월임대료지수,
#  경쟁밀도[동종 외식 점포수/100m], 접근성점수[1-10], 비고)
TRADE = [
    ("여의도",   "기존", 95,  82, 1.00, 14, 9, "오피스 핵심, 점심 수요 강세"),
    ("강남역",   "기존", 140, 70, 1.30, 22, 10,"유동 최다, 임대료·경쟁 동반 최고"),
    ("판교",     "기존", 78,  88, 0.95, 11, 8, "IT 오피스, 객단가 여력 높음"),
    ("광화문",   "기존", 88,  76, 1.05, 16, 9, "오피스+관광 혼합"),
    ("을지로",   "기존", 70,  58, 0.90, 19, 7, "노후 상권, 야간 수요 약함"),
    ("삼성",     "기존", 92,  80, 1.15, 17, 8, "코엑스 연계, 주중·주말 고른 수요"),
    ("잠실",     "기존", 130, 45, 1.20, 20, 9, "쇼핑몰 집객, 가족 단위"),
    ("수원",     "기존", 85,  40, 0.85, 12, 7, "스타필드 의존, 평일 약세"),
    ("대전",     "기존", 60,  35, 0.70, 9,  6, "지방 백화점, 집객 한계"),
    ("부산",     "기존", 110, 38, 0.80, 15, 7, "해운대 관광 수요, 계절 편차"),
    ("도곡",     "기존", 55,  42, 1.10, 8,  7, "고소득 주거, 디너 수요"),
    ("명동",     "기존", 160, 30, 1.40, 28, 8, "관광 의존, 임대료 최고권"),
    # 신규 출점 후보지
    ("마곡",     "후보", 72,  90, 0.78, 6,  8, "신흥 오피스, 경쟁 희박·임대료 낮음"),
    ("용산",     "후보", 105, 62, 1.10, 13, 9, "신규 개발+관광, 균형형"),
    ("성수",     "후보", 98,  48, 1.05, 24, 8, "트렌드 상권, 경쟁 과밀"),
    ("위례",     "후보", 50,  35, 0.72, 5,  6, "주거 신도시, 디너 가능성"),
    ("광교",     "후보", 64,  70, 0.82, 7,  7, "수원권 오피스, 판교 대안"),
    ("송도",     "후보", 58,  55, 0.75, 6,  6, "국제업무지구, 외국인 수요"),
    ("청담",     "후보", 70,  40, 1.35, 18, 8, "프리미엄 다이닝, 파인다이닝 적합"),
    ("동탄",     "후보", 80,  52, 0.74, 8,  7, "신도시 가족, 쇼핑몰 입점형"),
]
with open(OUT / "trade_area.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.writer(f)
    w.writerow(["trade_area","type","daily_traffic_k","office_pop_k","rent_index",
                "competition_density","access_score","note"])
    for row in TRADE:
        w.writerow(row)

# ----------------------------------------------------------------------------
# 7. 스파이크 검증 — 프로모션 연동일이 일·브랜드 양쪽에서 +30% 넘게 잡히는지
# ----------------------------------------------------------------------------
print(f"생성 완료: store_master={len(stores)}행, menu_master={len(MENU)}행, "
      f"pos_sales={len(rows)}행, promotions={len(PROMOS)}행, trade_area={len(TRADE)}행")
print("\n=== 스파이크 검증 (브랜드 일매출, 프로모션일 vs 비프로모션일 평균) ===")
# 브랜드×날짜 일매출 집계
bd = defaultdict(float)
for r in rows:
    bd[(r[3], r[1])] += r[10]  # brand, date -> gross
for s,e,brand,ptype,pname,boost in PROMOS:
    sd = datetime.date.fromisoformat(s); ed = datetime.date.fromisoformat(e)
    promo_days, base_days = [], []
    for (b,dt), v in bd.items():
        if b != brand: continue
        d = datetime.date.fromisoformat(dt)
        if sd <= d <= ed: promo_days.append(v)
        else: base_days.append(v)
    pavg = statistics.mean(promo_days); bavg = statistics.mean(base_days)
    lift = (pavg/bavg - 1)*100
    flag = "OK" if lift >= 30 else "!! 미달"
    print(f"  [{flag}] {brand:14s} {pname:22s} 프로모일평균 {pavg/1e6:6.1f}백만 / "
          f"평소 {bavg/1e6:6.1f}백만 → +{lift:4.1f}%")
