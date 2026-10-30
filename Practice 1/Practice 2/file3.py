f = open('abc.txt', 'w')
s = input('Enter Something: ')
f.write(s)
s = input('Enter Something Else: ')
f.write(s)
f.close()
import os
print(os.path.abspath("abc.txt"))