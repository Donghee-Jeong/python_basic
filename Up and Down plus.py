# up & down 게임
import random

randomNumber = random.randrange(1,101)

print("1~100까지의 숫자 중 임의의 수를 입력해야한다.")

count = 5
up_continue = 0
down_continue = 0

while count>0:
    number = int(input("숫자를 입력하시오: "))

    if number>100 or number<1 :
        print("숫자를 잘 못 입력했습니다.")
        continue

    count -= 1

    
    if number > randomNumber :
        down_continue += 1
        up_continue = 0
        if down_continue >= 3:
            count += 1
        print("Down! (남은 기회 :",count,"번)")
    elif number < randomNumber :
        down_continue = 0
        up_continue += 1
        if up_continue >= 3:
            count += 1
        print("Up! (남은 기회:",count,"번)")
    else:
        print("정답입니다!")
        print("게임이 종료됩니다.")
        break

    if count == 0 and number != randomNumber:
        print("정답은 %d입니다." %randomNumber)
        print("게임이 종료됩니다.")
        break
