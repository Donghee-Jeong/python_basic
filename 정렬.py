data = input("입력: ")
data = data.split(",")
for i in range(len(data)-1):
    for j in range(len(data)-1-i):
        if data[j]>data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
print(data)
