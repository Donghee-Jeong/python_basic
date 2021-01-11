def test():
    global k
    k=10

k=0
test()
print("global키워드 사용 시 k : %d" %k)

def test2():
    k=10
    
k=0
test2()
print("global키워드 사용 안할 시 k : %d" %k)
