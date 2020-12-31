#연습문제3
num = int(input("정수를 입력하시오: "))
num1 = num % 10
num = num // 10
num10 = num % 10
num = num // 10
num100 = num % 10
num = num // 10
sum = num + num100 + num10 + num1
print("자리수의 합:",sum)
