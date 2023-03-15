# >=90 = A
# 70-89 = B
# 60-69 = C
# <=59 = F
Score1 = int(input("Enter Score for INS 405:"))

Score2 = int(input("Enter Score for BUIS 360:"))
Score3 = int(input("Enter Score for DANL 470:"))
# converted all input from user to integer and added display preference to print
Sum = Score1 + Score2 + Score3
print("Sum =", Sum)
# Also converted the Average to a fload to display output in one decimal place
average = float(Sum/3)
print("Average", average)
if (average)>=90:
    print("A")
elif (average)>=70 and Sum/3<=89:
    print("B")
elif (average)>=60 and Sum/3<=69:
    print("C")
else:
    print("F")