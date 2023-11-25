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

print('Welcome to the Snake water gun game!!!\n')

print("Rock vs Paper -> Paper wins \nRock vs Scissors -> Rock wins \nPaper vs Scissors -> Scissor wins \n")


n=int(input("how many times you wan to play:"))

for _ in range(n):

    print("Enter your choice \n 1 - Snake \n 2 - Water \n 3 - Gun \n")

    choice=int(input("Enter your choice :"))

    while choice > 3 or choice <1:

      choice=int(input('Enter a valid choice please'))

    if choice == 1:

        player= 'Snake'

    elif choice == 2:

        player= 'Water'

    else:

        player= 'Gun'

    print('your choice:',player)



    print('\nNow its Computers Turn....')

    comp_choice = random.randint(1,3)

    while comp_choice == choice:

        comp_choice = random.randint(1,3)

    if comp_choice == 1:

        computer = 'Snake'

    elif comp_choice == 2:

        computer = 'Water'

    else:

        computer = 'Gun'

    print("Computer choice:", computer)
    print('\n')
    print(player,'Vs',computer)

    if choice == comp_choice:

        print('Its a Draw\n',end="")

        result="DRAW"

    if (choice==1 and comp_choice==2):

        print('Water wins\n',end="")

        result='Water'

    elif (choice==2 and comp_choice==1):

        print('Water wins\n',end="")

        result='Water'

    if (choice==1 and comp_choice==3):

        print('Gun wins\n',end= "")

        result='Gun'

    elif (choice==3 and comp_choice==1):

        print('Gun wins\n',end= "")

        result='Gun'

    if (choice==2 and comp_choice==3):

        print('Water wins\n',end="")

        result='Water'

    elif (choice==3 and comp_choice==2):

        print('Water wins\n',end="")

        result='Water'

    if result == 'DRAW':

        print("Its a tie\n")

    if result == player:

        print("you win\n")

    else:

        print("Computer wins\n")


print("Thanks for playing")
