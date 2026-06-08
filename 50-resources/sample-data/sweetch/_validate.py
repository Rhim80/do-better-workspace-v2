#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""스파이크 검증: 기획전/콘텐츠 연동일이 일·SKU 양쪽에서 +30% 이상 급등하는지 확인."""
import csv
from collections import defaultdict

with open("sales.csv", encoding="utf-8-sig") as f:
    rows = list(csv.DictReader(f))

# 환불·교환 제외한 유효매출 기준
def valid(r): return r["주문상태"] not in ("환불","교환")

day_total = defaultdict(int)
day_sku = defaultdict(lambda: defaultdict(int))
for r in rows:
    if not valid(r): continue
    amt = int(r["판매금액"])
    day_total[r["주문일"]] += amt
    day_sku[r["주문일"]][r["sku"]] += amt

avg = sum(day_total.values()) / len(day_total)
print(f"일평균 매출: {avg:,.0f}원")
print(f"검출 임계값(+30%): {avg*1.3:,.0f}원\n")

# 콘텐츠/기획전 연동일
PROMO_DAYS = {
    "2026-05-03":"봄 Voyager 기획전+릴스",
    "2026-05-12":"무신사 블랙위크+릴스",
    "2026-05-22":"29CM PICK+캐러셀",
    "2026-05-28":"회원의날+릴스",
}
print("=== 연동일 일총매출 검증 ===")
ok = True
for d, label in PROMO_DAYS.items():
    t = day_total.get(d, 0)
    ratio = t/avg
    flag = "✅" if ratio >= 1.30 else "❌"
    if ratio < 1.30: ok = False
    # 그날 최대 SKU 급등 배율
    sku_avg = defaultdict(list)
    for dd, skus in day_sku.items():
        for s, v in skus.items():
            sku_avg[s].append(v)
    top_sku = max(day_sku[d].items(), key=lambda x: x[1])
    print(f"{flag} {d} {label}: {t:,}원 (평균 대비 {ratio:.2f}배), TOP SKU={top_sku[0]} {top_sku[1]:,}원")

print(f"\n전체 검증: {'PASS' if ok else 'FAIL — day_factor 상향 필요'}")

# 베스트셀러 결품 경보 확인
with open("inventory.csv", encoding="utf-8-sig") as f:
    inv = {r["sku"]: r for r in csv.DictReader(f)}
sku_total = defaultdict(int)
for r in rows:
    if valid(r): sku_total[r["sku"]] += int(r["수량"])
print("\n=== 재고 경보 후보 (월판매 대비 재고 적은 순) ===")
ratios = []
for s, sold in sku_total.items():
    stock = int(inv[s]["현재고"])
    ratios.append((stock/max(sold,1), s, stock, sold))
for r in sorted(ratios)[:4]:
    print(f"  {r[1]}: 재고 {r[2]} / 월판매 {r[3]}개 (소진배율 {r[0]:.1f})")
