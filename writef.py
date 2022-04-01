# f=open("w.txt","a")
# n=f.write("this is writable file...\n")
# print(n)
# f.close()

# f=open("w.txt","w")
# n=f.write("this is writable file...\n")
# print(n)
# f.close()



# f=open("w.txt","r")
# c=f.read()
# print(c)
# f.close()


# read and write both :
# f3=open("w.txt","r+")
# print(f3.read())
# f3.write("thank u")
# f3.close()

f4=open("1.txt","r+")
print(f4.tell())
print(f4.readline())

f4.seek(0)
#print(f4.tell())
print(f4.readline())

f4.seek(10)

print(f4.tell())
#print(f4.readlines())   #readline() method returns one line from the file.
#print(f4.tell())
f4.close()                                                                                                                                                                                                          