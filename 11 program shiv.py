#tuples
tup = (3, 6, 2, 9)
print(tup)
print(type(tup))
print(tup[3])
print(tup[1])

tup = ()     #empty tuple
print(tup)

tup = (3,)    #enter single value in tuple
print(tup)
print(type(tup))

#slicing ; like string and list
tup = (3, 6, 2, 9)
print(tup[1:3])

#methods
tub = (3, 6, 2, 9)
print(tup.index(9))    #place where first time value will come
print(type(tub))

tup = (2, 6, 4, 5, 6, 6)
print(tup.count(6))     # count how much time value will given

#practice question
#wap to ask the user to enter names of their 3 favorite movie & store them in a list
movies = []
mov1 = input("enter 1st movie")
mov2 = input("enter 2nd movie")
mov3 = input("enter 3rd movie")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#wap to check if a list contains a palindrome of elements. (hint: use copy() metrhod)
# palindrome are those word that we will read from both side start and end they will same (like: [1,2,3,2,1] and [1, "abc", "abc", 1] )
list1 = ["m", "a", "a", "m"]
copy_list1 = list1.copy()
copy_list1.reverse()
if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

#wap to count the number of student with the "A"grade in the following tuple.
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A"))

#WAP to shoth the above value in a list & sort them from "A" to "D"
grade = ["C", "D", "A", "A", "B", "B", "A"]
grade.sort()
print(grade)