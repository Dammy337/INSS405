# the first thing to do is to import the random function
# then use a for loop
import random as rand
# this for loop ranges from 0 to 1000
for i in range(1000):
    # Within this for loop, I am assigning the randomNumber to the rand.randint explained
    # in class to ensure that a random number is generated and loop 1000 times to give 1000 random  numbers
    randomNumbers = rand.randint(0,1000)
    # next we print the randomNumbers
    print(randomNumbers)