number = int(input("enter a number: "))
# we used the modulus operator to check if the user input is divisible by 3,5,15
# and print respective game result.
#we also made sure the user input satisfies the higher divisible number first
# incase it is divisible by more than one factor.
if(number %15 == 0):
    print("Bowie State University")
elif(number %5 == 0):
    print("Bowie State")
elif(number %3 == 0):
    print("Bowie")
else:
    print("Game over")
