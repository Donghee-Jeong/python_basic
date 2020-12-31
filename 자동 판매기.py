insert = int(input("투입한 돈: "))
price = int(input("물건값: "))

change = insert - price
print("거스름돈:",change)

coin500 = change // 500
change = change % 500
coin100 = change // 100
change = change % 100
coin50 = change // 50
change = change % 50
coin10 = change // 10

print("500원 동전의 개수:",coin500)
print("100원 동전의 개수:",coin100)
print("50원 동전의 개수:",coin50)
print("10원 동전의 개수:",coin10)
