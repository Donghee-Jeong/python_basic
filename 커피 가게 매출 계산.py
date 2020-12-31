americano_price = 2000
cafelatte_price = 3000
capucino_price = 3500

americanos = int(input("아메리카노 판매 개수 : "))
cafelatte = int(input("카페라떼 판매 개수 : "))
capucino = int(input("카푸치노 판매 개수 : "))

sales = americanos * americano_price
sales = sales + cafelatte*cafelatte_price
sales = sales + capucino*capucino_price
print("총 매출은",sales,"입니다.")

budget = 100000

if(sales>budget):
    print(sales-budget,"원 흑자")
else:
    print(budget-sales,"원 적자")
