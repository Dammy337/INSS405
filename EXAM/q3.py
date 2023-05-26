import random
import random as rand
num = []
for i in range(100):
    numbers = random.randint(1,500)
    num.append(numbers)
    num.sort()
for numbers in num:
        if numbers % 2 == 1:
            print(numbers)
