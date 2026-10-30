class Book:
    def __init__(self,id,title,author,price):
        self.id = id
        self.title = title
        self.author= author
        self.price = price
    def  set(self,id,title,author,price):
         self.id = id
         self.title = title
         self.author= author
         self.price = float(price)
    

    def __str__(self):
        return f"Id : {self.id}, Title: {self.title}, Author: {self.author}, Price: {self.price} "
def find_book(books    

book = []

while True:
    print("1.Add a Book")
    print("2. Search a Book")
    print("3. Display all Books")
    print(" 4. Exit")
    choice = int(input("Enter Your Choice:"))

    if choice == 1:
        id = int(input("Enter Book id"))
        title = input("Enter Book title"))
        author = input("Enter Book author"))
        price = int(input("Enter Book price"))
        book = Book(id,title,author,price)

    elif choice == 2:
        search.id = int(input("Enter Book id to search"))



        

     

