# Hot = >= 50
# warm = 30 - 50
# cold = 0 - 30
# Extreme_cold = <0


for i in range(5):
    temperature = int(input("enter temperature: "))
    if(int(temperature)) >= 50:
        print("Hot")
    elif(int(temperature) <50 and int(temperature) >=30):
        print("warm")
    elif(int(temperature) <30 and int(temperature) >=0):
        print("cold")
    elif(int(temperature) <0):
        print("Extreme cold")