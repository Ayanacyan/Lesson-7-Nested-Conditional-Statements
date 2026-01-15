print("What is your age?")
age=int(input("Enter your current age:"))

if (10<=age<=20):
    print("You are eligible for this class")
   
else:
    if(10<=age<=23):
        print("You are a little overage for this class")
    elif(8<=age<=20):
        print("You are a little underage for this class")
    else:
       if(24<=age):
            print("You are way too overage for this class")
        else:
            print("You are too underage for this class")
                       
