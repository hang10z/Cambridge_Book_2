#### My Magic 8 BALL
## **********

import random

# put answers in a Tuple

answers = (
    "Go for it!",
    "No Way Jose",
    "Im not sure, Ask me again",
    "Fear of the unknown is what imprisons us!",
    "It would be madness to do that!",
    "Only you can save mankind!",
    "Makes no difference to me, do it or don't",
    "Yes, that is the right choice"
    )

print ("Welcome to My Magic 8 Ball! \n\n")


#Get the users name

user_name = input("Hello, Please Type in your First Name!\n")

# Get the users questions

question = input ("Ask me for advice, then press ENTER to shake me \n")

print("SHAKING ... \n" * 4)

# use the randint function to select random Answer

choice = random.randint(0, 7)

# print the answer on the screen
print(answers[choice])

#exit cleanly
print("Thanks for playing", user_name,", Press ENTER to Put Down the Magic Ball and Quit")


