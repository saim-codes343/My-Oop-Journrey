products = {"apple": 120, "banana": 60, "mango": 200}
product = input("Product: ").strip().lower()
if product in products:
        print("Price:", products[product])
else:
        print("Not found")