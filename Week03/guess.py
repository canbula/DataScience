import random


r = random.randint(1, 10)
n = 0
while n != r:
    n = int(input("Please enter a number: "))
    if n < r:
        print("Increase")
    elif n > r:
        print("Decrease")
    else:
        print("Correct")
