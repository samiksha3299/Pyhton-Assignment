a=list()
b=list()
n1=int(input("Enter the size of the First List ::"))
n2=int(input("Enter the size of the second List ::"))
print("Enter the Element of first List ::")
for i in range(int(n1)):
   k1=int(input(""))
   a.append(k1)
print("Enter the Element of second List ::")
for j in range(int(n2)):
   k2=int(input(""))
   b.append(k2)
print("Missing values in second list:", (set(a).difference()))
