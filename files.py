file=open("philosopher.txt","w")

file.write("hello\n")
file.write("philosopher\n")

file.close()

file=open("philosopher.txt","r")
A=file.read()
print(A)
