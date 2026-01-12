medical_cause=input("Did you have the medical cause Y or N:")

atten=int(input("Enter the student's attendance"))
if medical_cause=='Y':
    print("You are allowed")

else:
    if atten>75:
        print("Allowed")

    else:
        print("Not Allowed")