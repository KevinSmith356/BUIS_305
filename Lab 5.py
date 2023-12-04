# Step 2
number1 = int(input('Enter Number1:'))
# Step 3-5
if number1 % 3 == 0 and number1 % 5 == 0:
    print('Tic Tac')
elif number1 % 3 == 0:
    print('Tic')
elif number1 % 5 == 0:
    print('Tac')
else:
    print(number1)
# Step 6-7
number = int(input('Enter Number:'))
while 0 <= number <= 20:
    if number % 3 == 0 and number % 5 == 0:
        print('Tic Tac')
    elif number % 3 == 0:
        print('Tic')
    elif number % 5 == 0:
        print('Tac')
    else:
        print(number)
    number += 1
# Step 8
import random
print(random.randint(50,100))
# Step 9
user1 = 0
while user1 < 5:
    value = int(input('Enter User Data:'))
    if value > 0:
        print('Greater than zero')
        break
    else:
        print('Must enter value that is not zero')
# Step 10
user_value = int(input('Enter Point:'))
while user_value < 20:
    user_value += 1
    random_value = random.randint(1,20)
    if user_value > 1:
        print('No perfect match')
        if user_value == random_value:
            print('Perfect match')
        else:
            print('user_value and random_value does not match')
        break
    else:
        print('Enter integer')