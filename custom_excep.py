class MyError(Exception):
    def __init__(self,value):
        self.value=value
    def __str_(self):
        return(repr(self.value))
try:
    raise(MyError(3*2))
except MyError as error:
    print("A new Exception occured:",error.value)
