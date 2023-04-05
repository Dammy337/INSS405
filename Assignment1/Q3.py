# >90 = A
# >80 = B
# 75 - 79 = C
# >60 = D
# <59 = F
sum = 0.00 # setting my initial sum value to be 0.00
for i in range(11): # Using for loop to get a range of score for the 11 courses
    score = int(input("Enter Score:")) # allow student to input score and set it to be an integer
    if score >= 90: # if score is greater than or equals 90
        print("Grade A") # prints grade A
    elif score >= 80: # If score is greater than or equals 80
        print("Grade B") # Prints Grade B
    elif score >= 75 and score<= 79: # If score is within 75 to 79
        print("Grade C") # prints Grade C
    elif score >= 60: # If score is greater than or equals 60
        print("Grade D") # Prints Grade D
    elif score <= 59: # If score is 59 or below
        print("Grade F") # Prints Grade F
    sum = sum + score # Keeping the sum within the for loop to ensure it takes all 11 score from student
average = sum/11 # Taking the average of all scores; exit the loop to allow average operate independently
print("Total sum ",sum) # Print the total score of student
print("Average Score ",average) # Prints the Average score of student
