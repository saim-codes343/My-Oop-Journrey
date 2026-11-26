#a
marks = [45, 78, 62, 90, 55, 78]
marks.append(85)
marks.insert(0,40)
print('After append and insert:', marks)

#b
marks.remove(78)
marks.pop(3)
#popped = marks.pop()
print('After remove and pop:', marks)

#c
print('First three:' , marks[:3])
print('Last :', marks[-1:])
print('Every second mark:', marks[::2])

#d
total = sum(marks)
print('Sum of marks:', total,'Maximum mark:', max(marks),'Minimum mark:', min(marks), 'Average mark:', total/len(marks))

#e
b = marks
c = marks.copy()
b.append(100)
print('After appending 100 to b:', b)
print('Original marks:', marks)
print('Copy of marks:', c)