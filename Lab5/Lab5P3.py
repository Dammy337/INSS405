def collect():
    num1 = int(input("enter first number: "))
    num2 = int(input("enter second number: "))
    num3 = int(input("enter third number: "))

    sum = summation(num1, num2, num3)
    print(sum)
    print(ave(sum))
    print(minimum(num1, num2, num3))
    print(maximum(num1, num2, num3))
    print(multiplication(num1, num2, num3))

def summation(num1, num2, num3):
    sum = int(num1) + int(num2) + int(num3)
    return sum

def ave(sum):
    return int(sum/3)

def minimum(num1, num2, num3):
    print(min(num1, num2, num3))

def maximum(num1, num2, num3):
    print(max(num1,num2,num3))

def multiplication(num1, num2, num3):
    product = num1*num2*num3
    return product

collect()
