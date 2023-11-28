#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      KOUSHANI
#
# Created:     15-10-2023
# Copyright:   (c) KOUSHANI 2023
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random
import math

low = int(input("Enter a number for lowerbound:"))
up =int(input("Enter a number for higherbound:"))

x = random.randint(low, up)

guess = round(math.log(up - low + 1, 2))

print("you have ",guess," number of guessing:")

count = 0
while count < guess:
    count = count + 1
    number=int(input("Enter the number:"))
    if x==number:
        print("Congratulations!!!guessing number is right.")
        print("Your score:",100/count)
        break
    elif x<number:
        print("Try again!!!the guessing number is too high.")
    else:
        print("Try again!!!the guessing number is too small.")

if count >= guess:
    print("The number is:",x)
    print("Sorry!!your chance to guess the number is end.Better luck next time..")
    print("Your score:0")



