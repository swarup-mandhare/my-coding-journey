#type conversion
# 1. AUTOMATIC
a = 10
b = 5.25
sum = a + b 
print(sum)
print("type of automatic casting : ",type(sum))

# here 10 was automatically converted from int to float

# 2. MANUAL - type casting

c = "5"
d = 10

# print(c + d)   it will show error as c is string type which cannot be added to int
# so we will do manually i.e type casting

e = int(c)
sum2 = d + e
print (sum2)
print("type of manual conversion example : ",type (sum2))

# another example
x = 3.14
x = str(x)
print("type of another example : ",type(x))
