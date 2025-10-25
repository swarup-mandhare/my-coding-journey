# lists is a built-in data type that stores set of values
# it can store elements of different types (int, float, string, etc...) unlike java and c++
marks = [96.2, 98.7, 89.6, 94.5, 95.6] 
print(marks)
print(type(marks))
print(len(marks))
print(marks[0])
print(marks[3])

# diff in string indexing and lists

name = "Swarup Satish Mandhare"
print(name[3:9])


student = ["Swarup", 99.8, "Pune"]

# strings in python are mutable - cannot be changed
# lists are mutable - can be changed

print(student[0])
student[0]="Atharva"
print(student[0])
# we changed the student name from Swarup to Atharva 