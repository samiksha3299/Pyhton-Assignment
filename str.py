class Car:
    def __init__(self,color,mileage):
        self.color=color
        self.mileage=mileage
    def __str_(self):
        return f'a{self.color}car'
obj=Car("red",24546)
print(obj)
