import random

guess = 0
number = 0
count=0
number = random.randrange(1, 10)


while guess != number:
    count += 1
    guess = int(input('Guess a number in the range 1-10: '))
    if guess == number:
        print(f'Yes! The number chosen is {number}, you got it in {count} attempts.')
        break
    else:
        print(f'Nope! try again, the answer is not {guess}.')
