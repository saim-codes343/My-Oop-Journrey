class Customer:
    def __init__(self,name,phone,):
        self.name = name
        self.phone = phone
    def update_phone(self, phone):
        self.phone = phone   
    
    def __str__(self):
        return f"Customer Name: {self.name}, Phone: {self.phone}"    
class  Order:
    def __init__(self,  customer, items):
        self.customer = customer
        self.items = items


    def __str__(self):
        return f"Order - Customer: {self.customer.name}, Items: {', '.join(self.items)}"   
c = Customer("John Doe", "123-456-7890")
o1 = Order(c, ["item1", "item2", "item3"])
o2 = Order(c, ["item4", "item5"])
print(o1)
print(o2)

del o1
del o2
print("Customer after deleting orders:", c)