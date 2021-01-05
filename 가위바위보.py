import random

count = 0
win = 0

while count < 5 :
    computer_num = random.randrange(1,4)
    player_num = int(input("가위,바위,보 중 하나를 선택하시오: "))
    if player_num==1:   # p: 가위
        # c : 가위 => 무승부
        if computer_num==2: # c : 바위 => 컴퓨터 승
            count+=1
        elif computer_num==3 :  # c : 보 => 플레이어 승
            win+=1
            count+=1
    elif player_num==2: # p : 바위
        if computer_num==1: # c :  가위 => 플레이어 승
            win+=1
            count+=1
        # c : 바위 => 무승부
        elif computer_num==3 : # c : 보 => 컴퓨터 승
            count+=1
    else: # p : 보
        if computer_num==1: # c : 가위 => 컴퓨터 승
            count+=1
        elif computer_num==2: # c : 바위 => 플레이어 승
            win+=1
            count+=1
        # c : 보 => 무승부
    print("사용자는 %d, 컴퓨터는 %d" %(player_num,computer_num))

if win>=3:  # 이긴 횟수가 3보다 크면
    print("사용자 승!")
else :
    print("컴퓨터 승!")
