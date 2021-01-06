#랜덤한 두 값의 차 구하기
import random
num1 = random.randint(1,100)
num2 = random.randint(1,100)
answer = int(input(str(num1) + "-" + str(num2) + "="))
if answer == (num1-num2) :
    print("맞았습니다.")
else :
    print("틀렸습니다.")
