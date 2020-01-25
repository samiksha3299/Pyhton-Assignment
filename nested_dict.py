people={
         1:{'name':'john','age':'27','sex':'male'},
         2:{'name':'marie','age':'22','sex':'female'}
        }
for p_id,p_info in people.items():
    print("\nPerson ID:",p_id)
    for key in p_info:
        print(key+':',p_info[key])


"""people[3]={}
people[3]['name']='Luna'
people[3]['age']='24'
people[3]['sex']='female'
people[3]['married']='no'
people[4]={'name':'Peter','age':'29','sex':'male','married':'no'}

del people[3]['married']
del people[4]['married']
print(people[3])
print(people[4])"""

