a=input("enter the first name:")
i=[]
i.append(a)
for m in range(5):
    k =int(input("enter the theory number:"))
    i.append(k)
for n in range(3):
    k=int(input("enter the practical number:"))
    i.append(k)
j=i[1:6]
jsum=sum(j)
k=i[6:9]
ksum=sum(k)
s=sum(j+k)
per=(s/500)*100
print(a,"obtained",jsum,"marks out of 460 in theory and",ksum,"marks out of 40 in practicals and successfully passed the exam with",per,"in aggregate.Many congratutlations to",a)
