input_string="aeiNPTvy"
"""
s=input_string.split()
lower=[]
upper=[]
for a in input_string:
    if a.islower():
        lower.append(a)
    else:
        upper.append(a)
str=lower+upper

new="str"

"""
y=sorted(sorted(["aeiNPTvy"],reverse=True),key=str.lower)
print(y)
