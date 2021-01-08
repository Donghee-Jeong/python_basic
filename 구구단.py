#구구단
for i in range(1,10):
    for j in range(2,10):
        print(j,"*",i,"=",j*i,end=" ")
    print("")

want = input("출력할 단을 입력하시오: ")
want_list = want.split(",")
for i in want_list:
    for j in range(1,10):
        print(int(i),"*",j,"=",int(i)*j,end=" ")
    print("")
