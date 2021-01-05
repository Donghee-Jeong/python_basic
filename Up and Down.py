#내가 만든 조건문 문제1
import random
randomValue = random.randrange(1,11)    #1부터10사이의 값

count = 3   # 3번의 기회
isCorrect = False   # 맞췄는지 여부

while count>0 :
    choice = int(input("몇일까요? "))
    # 랜덤값과 입력값 비교
    if randomValue>choice :
        print("Up!")
    elif randomValue==choice :
        isCorrect = True
        break
    else :
        print("Down!")
    count-=1
    
if isCorrect :
    print("정답입니다!")
else :
    print("맞추지 못했습니다!")
