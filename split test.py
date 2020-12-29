text="a/b/c/d"
print(text)
result = text.split("/")
print(result)

text2="a,b,c,d"
print(text2)
result2 = text2.split(",")
print(result2)

text3="a b c d"
print(text3)
result3 = text3.split()
print(result3)

result4 = "+".join(result3)
print(result4)
