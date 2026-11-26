nums = (10, 20, 30)
a, b, c = nums
print(f"Original: a={a} b={b} c={c}")
a, c = c, a
print(f"After swap: a={a} b={b} c={c}")