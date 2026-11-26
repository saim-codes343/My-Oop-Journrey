list1 = set(map(int, input("Enter  a list:").split()))
list2 = set(map(int, input("Enter 2nd list:").split()))
print("common", list1 & list2)
print("different", list1 ^ list2)
