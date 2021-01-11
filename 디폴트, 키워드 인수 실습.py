def test(a,b=10):
    return a + b

print("test(a,b=10)에서 test(10)의 결과 :",test(10))

def test2(a,b,c):
    return a+b+c

print("test2(a,b,c)에서 test2(b=20,c=30,a=10)의 결과 :",test2(b=20,c=30,a=10))
print("test2(a,b,c)에서 test2(10,c=30,b=20)의 결과 :",test2(10,c=30,b=20))
#print("test2(a,b,c)에서 test2(a=10,20,30)의 결과 :",test2(a=10,20,30))
#SynttaxError발생

