num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
num3 = int(input("Enter the third number:"))
if (num1>=num2 and num1>=num3):
    print("First number is greater than all")
elif(num2>=num3 and num2>=num1):
    print("Second number is greater than all")
else:
    print("Third number is greater than all")

#simplified logic
# if num1 1 is less than num2 and num3 as in 1st condition so either num3 or num2 is greater so second 
# condition just needs one condition and else will have direct 