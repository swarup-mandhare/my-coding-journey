#OPERATORS

#arithematic operator
x=10
y=20

print( x + y )
print( x - y )
print( x * y )
print( x / y )
print( x % y )  #remainder
print( x ** y ) #a^b

print("----------------------------------------------------------------------------------------------------------------------------------")

#relational operators

#in relational operators ! stands for negation, i.e it says 'is not'

print( x==y ) # is x equal to y, ans will be FALSE
print( x != y) # x is not equal to y, ans will be TRUE
print( x >= y) 
print( x > y)
print( x <= y) 
print( x < y)

print("----------------------------------------------------------------------------------------------------------------------------------")

#assignment operators

#ao just assigns operations within the same value 
num = 10
# num = num + 10
num += 10 #shortcut of above statement
num **= 10
print("num = ", num )

print("----------------------------------------------------------------------------------------------------------------------------------")

#logical operators
#not operator
print(not False) #True
print(not True) #False
t = 100
u = 50
print(not (t>u)) #since t is greater than u but we used not so it will give opposite o/p
print(not (t<u))

#and operator
value1=True
value2=True
value3=False
print("and vlaue : ",value1 and value2) #gives true when both are true
print("and vlaue : ",value1 and value3) #gives false if one of the value is false

#or operator

print("or value : ",value1 or value2) 
print("or value : ",value1 or value3) #gives true even if one of the value is true

#operations with operators

print("or value of mixed operation", (t > u) or value3)

print("or value of mixed operation", (t == u) or value2)

print("and value of mixed operation", (t > u) and value2)

print("and value of mixed operation", (t > u) and value3)