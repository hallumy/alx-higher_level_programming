#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
neg_num = 0
if number < 0:
    number *= -1
    neg_num = 1
num = number % 10
if neg_num == 1:
    number *= -1
    num *= -1
if num == 0:
    print(f'Last digit of {number} is {num} and is 0')
elif num < 6:
    print(f'Last digit of {number} is {num} and is less than 6 and not 0')
else:
    print(f'Last digit of {number} is {num} and is greater than 5')
