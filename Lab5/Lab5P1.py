def definition():
    numCheck = int(input("enter a number: "))
    even(numCheck)
def even(num):
    if (int(num) %2 == 0):
        print(even(num))
    else:
        print("odd number")
definition()