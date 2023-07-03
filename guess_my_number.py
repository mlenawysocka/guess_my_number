import random
number = random.randrange(1,100)
while True:
    a = int(input('Choose a number: '))

    if a == number:
        print(f'You have guessed it! The number is: {number}.')
        break
    elif a > number:
        print("Sorry - my number is smaller. Try again!")
    elif a < number:
        print("Sorry - my number is greater. Try again!")
    else:
        break
