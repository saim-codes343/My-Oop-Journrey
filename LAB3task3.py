class Car:
    def __init__(self,make,model,year,price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
    def set(self,mk,md,yr,pr):
        self.make = mk
        self.model =md
        self.year = yr
        self.price = pr
    def printData(self):
        print("Make", self.make)
        print("Model", self.model)
        print("Year", self.year)
        print("Price", self.price)
c1=Car("Toyota","Corolla",2020,4500000)
c1.printData()
print("After setting new data" )
c1.set("Honda","Civic",2023,6200000)
c1.printData()