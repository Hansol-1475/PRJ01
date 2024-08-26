# 연봉
costLeast = 9860 # 최저시급
costMonthLeast = 2060740 # 최저월급
costYearLeast = 12*costMonthLeast # 최저연봉

# if costYearLeast <= 14000000 :
#     pass # 6퍼
# elif 14000000 < costYearLeast <= 50000000 : # 5천만
#     pass # 15퍼
# elif 50000000 < costYearLeast <= 88000000 : # 8천 8백만
#     pass # 24퍼
# elif 88000000 < costYearLeast <= 150000000 : # 1억 5천
#     pass # 35퍼

# 월급
rank = {
    '사장': 100000000, #1억
    '부사장': 80000000,
    '전무이사': 700000000,
    '상무이사': 60000000,  
    '부장': 50000000, #5천
    '부부장': 45000000, 
    '차장': 42000000,
    '부차장': 40000000, 
    '과장': 37000000,
    '대리': 35000000,
    '선임주임': 33000000,
    '주임': 30000000,
    '선임책임': 28000000,
    '책임': 26000000,
    '사원': 24000000,
    '인턴': 19000000
}


def directIncomeTax(title) : # 연봉에 따른 월소득세
    salary = rank[title]
    if 88000000 < salary <= 150000000 : # 35퍼
        salCal = salary - 88000000
        taxCal = salCal/12
        taxCal *= 0.35
        taxCal += 760000
        taxCal += 625000
        return taxCal
    
    elif 50000000 < salary <= 88000000 : # 24퍼
        salCal = salary - 50000000
        taxCal = salCal/12
        taxCal *= 0.24
        taxCal += 625000
        return taxCal
    
    elif 14000000 < salary <= 50000000 : # 15퍼 
        salCal = salary - 14000000
        taxCal = salCal/12
        taxCal *= 0.15
        taxCal += 70000
        return taxCal

    else :
        taxCal = salary/12
        taxCal *= 0.06
        return taxCal # 7만원
         

for key in rank:
    tax = directIncomeTax(key)
    print('{}의 세금은 {:,.0f}입니다.'.format(key,tax))