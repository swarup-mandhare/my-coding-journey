#report card system

name = input("Hello ! Please enter your name to access the report card system: ")
print("Hello", name)
grade = int(input(f"Please enter your grade, {name}:"))

if(grade<3):
    print("Please enter a valid class, this system is made for grade 3 and above!")
    
elif(grade<=8):
    print("So",name,"you are in",grade,"grade and you have 3 subjects: English , Science, Mathematics!")
    eng = int(input("Enter your English marks:"))
    sci = int(input("Enter your Science marks:"))
    math = int(input("Enter your Mathematics marks:"))
    avg = (eng + sci + math)/3
    if(avg>=90 and avg<100):
        print("You have secured",avg,"%","and passed with A grade!!! \nCongratulations!!!")
    elif(avg>=80 and avg<100):
        print("You have secured",avg,"%","and passed with B grade!!! \nCongratulations!!!")
    elif(avg>=70 and avg<100):
        print("You have secured",avg,"%","and passed with C grade!!! \nCongratulations!!!")
    elif(avg>=60 and avg<100):
        print("You have secured",avg,"%","and passed with D grade!!! \nCongratulations!!!")
    else:
        print("Hard luck!!!, you did not make it but it's not over!!!\nTry next time!!!")
    
        
        
elif(grade<=10):
    print("So",name,"you are in",grade,"grade and you have 5 subjects: English , Biology, Chemistry, Physics, Mathematics!")
    eng2 = int(input("Enter your English marks:"))
    bio = int(input("Enter your Biology marks:"))
    phy = int(input("Enter your Physics marks:"))
    chem = int(input("Enter your Chemistry marks:"))
    math2 = int(input("Enter your Mathematics marks:"))
    avg2 = (eng2 + bio + chem + phy + math2)/5
    print(type(avg2))
    if(avg2>=90 and avg2<100):
        print("You have secured",avg2,"%","and passed with A grade!!! \nCongratulations!!!")
    elif(avg2>=80 and avg2<100):
        print("You have secured",avg2,"%","and passed with B grade!!! \nCongratulations!!!")
    elif(avg2>=70 and avg2<100):
        print("You have secured",avg2,"%","and passed with C grade!!! \nCongratulations!!!")
    elif(avg2>=60 and avg2<100):
        print("You have secured",avg2,"%","and passed with D grade!!! \nCongratulations!!!")
    else:
        print("Hard luck!!!, you did not make it but it's not over!!!\nTry next time!!!")
        

else:
    print("Please enter a valid class greater than 3 and less than 11!")
