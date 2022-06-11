#
# #Variables    //Indentation error mainly caused for unwanted spaces
#
# age = 20
# age = 30
# price = 23.34
# first_name = "Mosh"
# is_online = False
# print("plaban")
# print(age)
#
# #Input function
#
# name = input("What is your name ?")
# print("Hello "+ name+"!")
#
# #Type conversion
#
# birth_year = input("Enter your birth year: ")  #এখানে আমরা যেটা ইনপুট দেবো সেটা String টাইপের
# age = 2020 - int(birth_year);    # to convert type cast ; functions are int(),str(),float(),bool();
# print(age)
#
# #Exercise : sum of two numbers : 1
#
# a = input("First : ")  # "10" this input is string
# b = input("Second : ") # "10" this input is string                    "10"+"10"=1010
# c = float(a) + float(b)
#
# print(c) # its ok
# #print("Sum : "+c)    # It has error
#
# print("Sum : " + str(c))
#
# Exercise : sum of two numbers : 2
#
# a = float(input("First : "))  # "10" this input is string
# b = float(input("Second : ")) # "10" this input is string                    "10"+"10"=1010
# c = a + b
#
# print(c) # its ok
# #print("Sum : "+c)    # It has error
#
# print("Sum : " + str(c))
#
# Strings
#
# course='Python for Beginners'
# print(course.upper())
# print(course.lower())
# print(course.find('o'))   # this returns the index of the charecter if it found and -1 means not found
# print(course.find('for'))   # this returns the starting index of the charecter if it found and -1 means not found
# print(course.replace('for',"4"))   # replacing function
#
# print('for' in course)  # this returns boolean value
#
# # Arithmatic operator
# print(10+10)
# print(10-10)
# print(10*10)
# print(10/3)     # =3.3333333 ;
#
# print(10//3)   # =3;
#
# print(10%3)    # =1;
# print(10**3)  # =1000; this is called 10 to the power 3
#
# x =10
# x = x+3   #13
# x +=3     #16
# print("Value : " + str(x))

# # Comparison Operators
# x = 3>=2   # this returns boolean value ; different operators are > ; < ; >= ; <= ; == ; != etc
# print(x)

# Logical Operator
#
# price = 25
# print(price>10 and price <30)   # if both are true
# print(price>10 or price <30)    # if any one is true
#
#
# # if Statements
#
# temperature = 5
# if temperature>30:
#     print("It's a hot day")  # লেখার মধ্যে একটা কোটেশন থাকলে ডাবল কোটেশন এর মধ্যে লেখা লাগবে ; না হলে একটা কোটেশন এর মধ্যে ও লেখা যাবে
#     print('Drink plenty of water')  #সেম কলামের জিনিসগুলো হলো ইনডেনটেন্ট
# elif temperature>20:
#     print("It's a nice day")
# elif temperature>10:
#     print("It's a bit cold")
# else: print("It's cold")
# print("Done") #এটা ইফ ব্লক এর ইনডেনটেন্ট নয়

# # Weight conversion programme
# weight = float(input("Weight: "))
# unit = input("(K)g or (L)s : ")
# if unit.upper() == "K":
#     converted =weight/0.45
#     print("Weight in Lbs: "+ str(converted))
# else:
#     converted = weight* 0.45
#     print("Weight in Kgs: "+ str(converted))

# # While loop
# i=1
# while i <= 10:  # in python ; we can use 1000 as 1_000
#     print(i)
#     print(i * '*')
#     i=i+1

# # Lists
# names = ["John","Bob","Mosh","Sam","Mary"]
# print(names[1])
# print(names[2])
# print(names[-1])  # last eliment of the list
# print(names[-2])  # last second eliment of the list
#
# names[0]= "Jon"
# print(names)
# print(names[0:3])
# print(names)

# # List Method
# numbers = [1,2,9,4,5]
# numbers.append(6)
# print(numbers)
#
# numbers.insert(0,-1) #জ িরো ইনডেক্সে Value এড হবে Array সাইজ বাড়বে
# print(numbers)
#
# numbers.remove(9)  # remove the value from the list ; it is not array index
# print(numbers)
#
# print(10 in numbers) # returns true of false
# print(len(numbers))
#
#

#
# # For loop
# for i in range(4):
#     print(i,end=' ')
# print(" ")
#
# sum =0
# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)
# for item in numbers:
#     sum = sum + item
# print("Sum : "+str(sum))
# print("")
# i =0
# while i< len(numbers):
#     print(numbers[i])
#     i = i+1
#


# # the range function
# numbers_range = range(3,9)
# for item in numbers_range:
#     print(item)
#
# print("")
#
# numbers_range = range(3,9,2)   # here 2 is steps ;;py it means after value of 3 ; we have to get 9 in 2 steps
# for item in numbers_range:
#     print(item)

