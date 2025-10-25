str = "i am a coder!"

print(str.endswith("er!"))              # returns true if string ends with substr

print(str.capitalize())                 # capitalize the first charecter

print(str.replace("ode" , "der"))
str1 = "I am studing JavaScript from 23rd, I am so happy!"
print(str1.replace("JavaScript","Python"))
str2 = "Ohh my Gooddd !!! "
print(str2.replace("o","c"))

print(str1.find("JavaScript"))          # returns index of first occurrer
print(str1.find("Python"))              # returns -1 if value not present
print(str1.find("a"))

print(str1.count("I"))                  #returns number of ocourences
print(str1.count("a"))