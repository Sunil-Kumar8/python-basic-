#street light colur detection
light = input("light colour : ")
if (light == "red") :
    print("stop")
elif (light == "yellow") :
    print("look")
elif (light == "green") :
    print("go")
else :
    print("light damage") 


# grade of student 
marks = int(input("marks : "))
if (marks >=90):
    print("sunil 10th marks"  ,"A")
elif (marks >=80 and marks <90):
    print("sunil 10th marks" ,"B")
elif (marks >=70 and marks <80):
    print("sunil 10th marks" ,"C")
else:
    print("sunil 10th marks" ,"D")

    # practice question
A = int(input("A : "))
G = input("M/F : ")
if((A == 1 or A== 2) and G == "M") :
        print("fee is 100") 
elif (A == 3 or A == 4 or G == "F") :
        print("fee is 200")
elif (A == 5 and G == "M") :
        print("fee is 300")
else:
     print("no fee")


# voting age
age = 21

if(age>=18) :
     print("can vote and apply for licence")


#wap  to check if a number by the user is odd or even
# we say that any num which is divided by 2 or given reminder 0 that num called even. any num other than this called odd
num = int(input("enter the number"))
if(num%2 == 0) :
     print("even")
else:
     print("odd")     

#wap to find the greatest of 4 numbers entered by the user
a = int(input("enter the first largest number"))
b = int(input("enter the secound largest number"))
c = int(input("enter the third largest number"))
d = int(input("enter the fourt largest number"))
if(a >= b and a >=c and a >= d) :
     print("first is largest number", a)
elif(b>=c and b>=d):
     print("secound is largest number", b)
elif(c>=d) :
     print("third is largest numbe", c)
else:
     print("fourth is largest number", d)          

#wap to check if a number is multible of 7 or not
x = int(input ("enter the number:"))
if(x % 7 == 0) :
     print("x is a multible of 7")
else:
     print("not multiple of 7")