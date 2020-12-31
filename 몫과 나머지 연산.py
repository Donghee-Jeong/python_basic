#p=int(input("분자를 입력하시오: "))
#q=int(input("분모를 입력하시오: "))
#print("나눗셈의 몫 =",p//q) # //는 나눗셈 결과의 몫만을 취할 수 있다.
#print("나눗셈의 나머지 =",p%q)

#num=int(input("정수를 입력하시오 : "))
#print(num%2) # 출력결과가 0이면 짝수, 1이면 홀수

#sec=int(input("초를 입력하시오: "))
#min=sec//60
#remainder=sec%60
#print(min,"분",remainder,"초")

hour=int(input("시를 입력하시오: "))
min=int(input("분을 입력하시오: "))
min=min + (hour*60)
sec=min * 60
print("입력한 시간은",min,"분 혹은",sec,"초 입니다.")
