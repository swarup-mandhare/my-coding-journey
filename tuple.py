# immutable type of list written in () --- assignments is not allowed in tuple

tup = (23, 35, 67, 54, 89)
print(tup[2])
print(tup[4])
print(type(tup))

# single value is treated as int so if we have single value we should add comma at end

tup2 = (1)
print(type(tup2))

tup3 = (1,)
print(type(tup3))

# slicing operation can be performed in tuple as well and works same as lists and string

