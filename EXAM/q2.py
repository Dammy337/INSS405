import random
import random as rand
def random_numbers():
    num = []
    for i in range(100):
        number = random.randint(1,500)
        num.append(number)
    return num
def sort(num):
    sort_number = sorted(num)
    return sort_number
new_sort = random_numbers()
print("Numbers: ", sort(new_sort))
