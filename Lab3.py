Temperature = input("Enter Temperature:")
# HOT = >=50
# WARM = 30 - 50
# COLD = 0 - 30
# EXTREME COLD = <0
# EXTREME CHILL COLD, SHELTER IN PLACE = <-20
if(float(Temperature)>=50):
    print("hot")
elif(float(Temperature)>=30 and float(Temperature)<50):
    print("warm")
elif(float(Temperature)>=0 and float(Temperature)<30):
    print("cold")
elif(float(Temperature)>=-20 and float(Temperature)<0):
    print("extreme cold")
else:
    print("extreme chill cold, shelter in place")
