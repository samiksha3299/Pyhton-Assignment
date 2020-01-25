matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten_matrix=[]
for sublist in matrix:
    for val in sublist:
        flatten_matrix.append(val)
print(flatten_matrix)

f_m=[va for sb in matrix for va in sb]
print(f_m)

planets=[['Mercury','venus','Earth'],['Mars','Jupiter','Saturn'],['Uranus','Neptune','Pluto']]
flatten_planets=[planet for sublist in planets for planet in sublist if len(planet)<6]
print(flatten_planets)
