# all the methods change the original list itself

list = [2,1,3]

print(list.append(4))       # adds one element at end --- also if we print appended list while performing appen operation it will not print appended value immediately it will print at next calling
print (list)

list.sort()                 # sorts in ascending order
print (list)

list.sort (reverse=True)    # sorts in descending order  -- can work for strings as well
print (list)

list.reverse()              # reverses the list
print (list)

list.insert(1,5)            # inserts element at given index and continues the whole list again
print(list)

list.remove(2)              # removes first occurrence of element 
print(list)

list.pop(1)                 # removes element at particular index
print(list)
