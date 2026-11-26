people = [("Ali", 20), ("Sara", 22), ("Hina", 19)]
for name, age in people:
    print(f"Name: {name}, Age: {age}")
oldest = max(people, key = lambda x : x[1])
print(f"oldest  {oldest[0]} {oldest[1]}.")    