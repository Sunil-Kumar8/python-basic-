"""single line if else/ ternary operater

<variable> = <variable1> if <condition> else <variabl2>"""
food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)

#<string1> if <condition> else <string2>
food = input("food : ")
print("sweet") if food == "cake" else "no"

#clever if / ternary operater
age = int(input("age : "))
vote = ("yes", "no") [age < 18]
print(vote)

sal = float(input("salary : "))
tax = sal*(0.1, 0.2) [sal>50000]       #0-50k = 10% (0.1) and 50k + =20% (0.2)
print(tax)


#concept of nesting
# we will put new if statement under first one if statement. 
age = 65
if(age >= 18) :
    if(age >= 80) :
        print("cannot drive")
    else:
         print("can drive")
else:
    print("cannot drive") 