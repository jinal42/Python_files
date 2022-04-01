f4=open("1.txt","r+")

print(f4.readline())
print(f4.readline())

print(f4.tell())
f4.seek(100)
print(f4.readline())


f4.seek(150)

print(f4.read(14))

print(f4.tell())
f4.seek(200)
print(f4.readline())

f4.close()