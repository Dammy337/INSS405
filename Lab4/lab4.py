import random
sum = 0.00
for i in range (9):
    score = input("enter score: ")
    sum = sum + int(score)
avg = sum/9
print("sum:", sum)
print("Average: ", avg)
