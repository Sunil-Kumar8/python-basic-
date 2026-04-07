#lists
marks = [12.3, 345.3, 456.3, 445.4, 101.1, 000.1]
print(marks)
print(type(marks))
print(marks[0])
print(marks[5])
print(marks[3])
print(len(marks))

#lists are mutable
student = ["sunil", 33.6, 54.9, "ayan"]
print(student[0])
student[0] = "shivam"
print(student)

#list slicing
marks = [12, 245, 346, 26, 4563, 42]
print(marks[1:4])
print(marks[ :4])
print(marks[1: ])
print(marks[-3:-1])

#methods in list
list = [2, 1, 3]
list.append(4)
print(list)

list = [24545, 2568, 1254432, 842, 675432,6798.3]
list.sort()
print(list)

list = [24545, 2568, 1254432, 842, 675432,6798.3]
list.sort(reverse = True)
print(list)
list = ["a", "g", "r", "p", "d"]     #in lists we also arrange characters
list.sort(reverse = True)
print(list)

list = ["a", "g", "r", "p", "d"]
list.reverse()
print(list)

list = [3, 7, 9, 1]
list.insert(3, 6)          #insert value in data at any place
print(list)

list = [3, 7, 9, 1, 9]
list.remove(9)            #remove firt given value of similler num
print(list)

list = [3, 7, 9, 1, 9]
list.pop(4)               # its remove value of a given index num
print(list)