from filecmp import cmp
from Art import *

from celebs import data
import time
import replit
import random

score = 0
print(logo)
time.sleep(0.5)
while True:



    # Generate 2 random number
    random_a = random.randint(0, 49)
    random_b = random.randint(0, 49)

    # Assign those random numbers to the Dictionary to determine option A and B
    option_a = (" \n" + data[random_a]['name'] + " from " + data[random_a]['country'] + '\n' +
                data[random_a]['description'])
    option_b = (" \n" + data[random_b]['name'] + " from " + data[random_b]['country'] + '\n' +
                data[random_b]['description'])

    if option_a == option_b:
        option_b = (" \n" + data[random_b]['name'] + " from " + data[random_b]['country'] + '\n' +
                data[random_b]['description'])
    # Get option a and b follower numbers
    option_a_follower = data[random_a]['follower_count']
    option_b_follower = data[random_b]['follower_count']
    # Convert them to Integer
    option_a_follower = int(option_a_follower)
    option_b_follower = int(option_b_follower)

    if option_a_follower > option_b_follower:
        correct_answer = option_a
    elif option_b_follower > option_a_follower:
        correct_answer = option_b
    else:
        break

    print(f"Current score:{score}")
    print(option_a + "\n\n\n" + option_b)

    user_answer = input("Who has more followers?\n: ")
    if user_answer == 'A' or user_answer=='a':
        if option_a_follower>option_b_follower:

            score=score+10
            print(score)
            time.sleep(0.5)
            print(great)
            time.sleep(0.5)

        else:
            time.sleep(0.5)
            print(sorry)
            time.sleep(0.5)
            break
    else:
        user_answer =='B' or user_answer=='b'
        if option_b_follower>option_a_follower:
            score=score+10
            print(score)
            time.sleep(0.5)
            print(great)
            time.sleep(0.5)
            option_b=option_a


        else:
            time.sleep(0.5)
            print(sorry)
            time.sleep(0.5)
            break






