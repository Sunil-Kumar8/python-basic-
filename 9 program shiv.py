#indexing
str = ("sunil kumar")
ch = str[3]
print(ch)

#slicing
str = ("sunil kumar")
print(str[1:8])
print(str[5:])
print(str[0:len(str)])
print(str[:5])
print(str[-7:-3])


#string function
#return true if string ends with substr
str = "i am studing python"
print(str.endswith("on"))

#capitalizes 1st char
str = "i am studing python"
print(str.capitalize())

#replace all occurance of old
str = "i am studing python"
print(str.replace("studing" , "teaching"))

#return 1st index of 1st occurrer
str = "i am studing python"
print(str.find("am"))

#counts the occurence of substr
str = "i am studing python and python"
print(str.count("python"))


#practice question
#wap to input users first name & print its length
name = input("enter your name : ")
print("length of your name is" , len(name))

#wap to find the occurance of '$' in a string
str = "hi $ iam the $ symbol $99.99"
print(str.count("$"))