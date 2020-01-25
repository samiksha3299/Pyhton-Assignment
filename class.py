class contact:

    def __init__(self, name,telephone,email):
        self.name = name
        self.telephone = telephone
        self.email = email

    def get_name(self):
        return self.name

    '''def set_name(self,name):
        set.name=samiksha
'''
    def get_telephone(self):
        return self.telephone

    '''def set_telephone(self,telephone):
        set.telephone=12345'''

    def get_email(self):
        return self.email

    '''def set_email(self,email):
        set.email=frnds@gmail.com'''
def main():
    my_con=contact('samiksha','123895','ffhsgh@gmail.com')
    print("name of person",my_con.get_name())
    print("telephone of person",my_con.get_telephone())
    print("email of person",my_con.get_email())

main()
