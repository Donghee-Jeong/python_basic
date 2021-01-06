#두자리 수 복권
import random
number = random.randrange(10,100)
user = int(input("복권번호를 입력하시오(0에서 99사이): "))

number_10 = number//10
number_1 = number%10

user_10 = user//10
user_1 = user%10

price=0

if number_10==user_10:
    if number_1==user_1:
        price=100
    else:
        price=50
elif number_10==user_1:
    if number_1==user_10:
        price=100
    else:
        price=50
elif number_1==user_10:
    if number_10==user_1:
        price=100
    else:
        price=50
elif number_1==user_1:
    if number_10==user_10:
        price=100
    else:
        price=50
        
print("당첨번호는",number,"입니다.")
print("상금은 %d만원입니다." %price)
