#입력한 정수가 2와 3으로 나누어 떨어지는기 확인하기
number = int(input("정수를 입력하시오: "))
if number%2==0 and number%3==0 :
    print("2와 3으로 나누어 떨어집니다.")
else :
    if number%2==0:
        print("2로 나누어 떨어집니다.")
    elif number%3==0:
        print("3으로 나누어 떨어집니다.")
    else:
        print("나누어 떨어지지 않습니다.")
