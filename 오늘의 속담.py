import random

str = []

str.append("꿈을 지녀라. 그러면 어려운 현실을 이길 수 있다.")
str.append("사람은 사랑할 때 누구나 시인이 된다.")
str.append("고생 없이 얻을 수 있는 진실로 귀중한 것은 하나도 없다.")
str.append("시작이 반이다.")

randomStr = random.choice(str)
print("#"*20)
print("# 오늘의 속담 #")
print("#"*20)
print("")
print(randomStr)
