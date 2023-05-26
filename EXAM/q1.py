import statistics
def user_input():
    numbers = []
    for i in range(11):
        num = int(input("Enter number: "))
        numbers.append(num)
    return numbers
def total_number(numbers):
    sum = 0.00
    for i in range(len(numbers)):
        sum = sum+int(numbers[i])
    return sum
def mean_number(numbers):
    mean = sum(numbers)/len(numbers)
    return mean
def median_number(numbers):
    median = statistics.median(numbers)
    return median

user_number = user_input()
print("sum:", total_number(user_number))
print("mean:", mean_number(user_number))
print("median:", median_number(user_number))