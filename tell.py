f4=open("1.txt","r+")
print(f4.tell())
print(f4.readline())

print(f4.tell())
print(f4.readline())


print(f4.tell())
print(f4.readlines())   #readline() method returns one line from the file.
print(f4.tell())
f4.close()