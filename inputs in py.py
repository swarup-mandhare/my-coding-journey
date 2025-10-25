# name = input("enter your name: ")
# print("welcome ", name )
# age =input("what is your age " + name + " ? ")
# print("wonderful!")
# print("so " + name + " your age is " , age," right?")

# # type of input value is always a string

# val= input("enter a value: " )
# print(type(val))

# # so to change the type we will type caste it !

# val2 = int(val)
# print(type(val2))

# or
 
# val= int(input("enter a value: " )) ---> this can be done in the first place directly !

name = input("enter your name: ")
age = int(input("enter your age: "))
percent = float(input("enter your percentage: "))

print("hello ",name)
print("you are",age,"years old and secured",percent,"% in your academics")

print(type(name))
print(type(age))
print(type(percent))
