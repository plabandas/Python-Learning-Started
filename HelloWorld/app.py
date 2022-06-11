
#Variables

age = 20
age = 30
price = 23.34
first_name = "Mosh"
is_online = False
print("plaban")
print(age)

#Input function

name = input("What is your name ?")
print("Hello "+ name+"!")

#Type conversion

birth_year = input("Enter your birth year: ")  #এখানে আমরা যেটা ইনপুট দেবো সেটা String টাইপের
age = 2020 - int(birth_year);    # to convert type cast ; functions are int(),str(),float(),bool();
print(age)

#Exercise : sum of two numbers : 1

a = input("First : ")  # "10" this input is string
b = input("Second : ") # "10" this input is string                    "10"+"10"=1010
c = float(a) + float(b)

print(c) # its ok
#print("Sum : "+c)    # It has error

print("Sum : " + str(c))

Exercise : sum of two numbers : 2

a = float(input("First : "))  # "10" this input is string
b = float(input("Second : ")) # "10" this input is string                    "10"+"10"=1010
c = a + b

print(c) # its ok
#print("Sum : "+c)    # It has error

print("Sum : " + str(c))

Strings

course='Python for Beginners'
print(course.upper())
print(course.lower())
print(course.find('o'))   # this returns the index of the charecter if it found and -1 means not found
print(course.find('for'))   # this returns the starting index of the charecter if it found and -1 means not found
print(course.replace('for',"4"))   # replacing function

print('for' in course)  # this returns boolean value

# Arithmatic operator
print(10+10)
print(10-10)
print(10*10)
print(10/3)     # =3.3333333 ;

print(10//3)   # =3;

print(10%3)    # =1;
print(10**3)  # =1000; this is called 10 to the power 3

x =10
x = x+3   #13
x +=3     #16
print("Value : " + str(x))

#Operator Precedence