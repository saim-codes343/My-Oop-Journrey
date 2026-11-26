nums = list(map(int, input("Numbers: ").split()))
even = [num for num in nums if num % 2 == 0]
odd = [num for num in nums if num %2 != 0]
print("Even numbers:", even)
print("Odd numbers:", odd)