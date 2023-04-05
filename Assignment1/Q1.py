# using for loop here to allow user input number only 10 times and run the codes within the loop
for i in range(10):
    num = int(input("Enter number:")) # This input statement requests input from user
    if int(num) % 2 == 0: # This if statement looks to satisfy the mathematical operator where remainder is 0
        print(num, "is a even number") # prints result if the above condition is satisfied

    else:  # Since we can only have two outcomes, else statement executes otherwise
        print(num,"is an odd number") #prints the outcome different from the having remainder 0 as Odd