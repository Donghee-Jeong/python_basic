items = {"커피음료":7,"펜":3,"종이컵":2,"우유":1,"콜라":4,"책":5}

while 1:
    item = input("물건의 이름을 입력하시오: ")
    print("현재 재고는",items[item],"개 입니다.")

    c = int(input("1: 수량증가, 2: 수량감소 "))
    n = int(input("수량의 개수를 입력해주세요"))
    if c==1:
        items[item] += n
    elif c==2:
        items[item] -= n
