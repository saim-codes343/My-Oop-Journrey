class Battery:
    def __init__(self, capacity):
        self.capacity = capacity
    def __str__(self):
        return f"Battery capacity: {self.capacity} mAh"
    def __del__(self):
        print(f"Battery with capacity {self.capacity} mAh is being deleted.")
class Phone:
    def __init__(self, model, capacity):
        self.model = model
        self.battery = Battery(capacity)
    def __str__(self):
        return f"Phone model: {self.model}, {self.battery}"
    def __del__(self):
        print(f"Phone model {self.model} is being deleted.")
        
        
p1 = Phone("Galaxy", 5000)     
p2 = Phone("pixcel", 4500)  
print(p1)
print(p2)
del p1
del p2 
