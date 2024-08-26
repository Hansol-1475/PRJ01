import csv
import random

a = [3500000, 3700000, 3900000, 4100000, 4300000, 4500000, 4700000, 4900000, 5100000, 5300000, 5500000, 5700000, 5900000, 6100000, 6300000, 6500000, 6700000, 6900000, 7100000, 7300000, 7500000, 7700000, 7900000, 8100000, 8300000, 8500000, 8700000, 8900000, 9100000, 9300000, 9500000, 9700000, 9900000, 10100000, 10300000, 10500000, 10700000, 10900000, 11100000, 11300000]
b = [1000000, 1100000, 1200000, 1300000, 1400000, 1500000, 1600000, 1700000, 1800000, 1900000, 2000000, 2100000, 2200000, 2300000, 2400000, 2500000, 2600000, 2700000, 2800000, 2900000]

# 가게 정보 리스트
store_data = [
    ["가게명", "매출", "지출"],
    ["가게1", random.choice(a), random.choice(b)],
    ["가게2", random.choice(a), random.choice(b)],
    ["가게3", random.choice(a), random.choice(b)],
    ["가게4", random.choice(a), random.choice(b)],
    ["가게5", random.choice(a), random.choice(b)],
    ["가게6", random.choice(a), random.choice(b)],
    ["가게7", random.choice(a), random.choice(b)],
    ["가게8", random.choice(a), random.choice(b)],
    ["가게9", random.choice(a), random.choice(b)],
    ["가게10", random.choice(a), random.choice(b)]
]

filename = "2024년6월.csv"

# 파일 생성 및 데이터 쓰기
with open(filename, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(store_data)

print(f"{filename} 파일이 성공적으로 생성되었습니다.")
