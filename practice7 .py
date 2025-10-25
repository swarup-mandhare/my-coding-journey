# # create a list and check if it contains palindrome or not

list = [1, "swarup", 0, "swarup", 1]
list2 =list.copy()
list2.reverse()
if(list == list2):
    print("The list contains palindrome")
else:
    print("The list does not contain any palindrome")
print("The list 1 is: ",list)


# write a program to count no of students with a grade in following tuple :
tuple = ["c","d","a","b","b","a","a"]
print(tuple.count("a"))

tuple.sort()
print(tuple)