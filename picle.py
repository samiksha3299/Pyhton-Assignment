import pickle

phonebook={'Chris':'555-111','Katie':'555-222','Joanne':'555-333'}
output_file=open('phonebook.dat','wb')
pickle.dump(phonebook,output_file)
print(phonebook)
output_file.close()
