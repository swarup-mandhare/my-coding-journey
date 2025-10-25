#odd even number
name = input("Enter your name to proceed:")
num = int(input(f"Enter the number {name}: "))
if(num%2==0 and num>0):
    print("The number",num,"is an even number!")
elif(num%2!=0 and num>0):
    print("The number",num,"is an odd number!")
elif(num==0):
    print("0 is neither odd nor even")
else:
    print("Enter a valid non-negative number greater than 0 !")
    
