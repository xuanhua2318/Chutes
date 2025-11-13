#-------------------------------------------------------------------------------
# Name:        Chutes.py
# Purpose:     Coding a program to play a children's game
#
# Author:      Xuan Hua
#
#
# Due Date:    11/17/2025
#-------------------------------------------------------------------------------


import random

def main():

    #TODO SCROLL DOWN AND SEE PRINT STATEMENTS BELOW FOR ALL VARIABLE NAMES
    #TODO Write them down if that is the best way to remember them.
    #TODO set turn to 0, player1 and player2 positions to 1
    #????
    turn = 0
    player1pos = 1
    player2pos = 1



    #TODO set boolean winner to false
    #????
    winner = False

    #TODO input the names for each the players
    #????
    player1name = input("Enter player 1's name: ")
    player2name = input("Enter player 2's name: ")

    #Dipslay the header for the game
    #IF YOU ARE LOOKING FOR VARIABLE NAMES? KEEP SCROLLING
    print('{:10s}{:10s}{:10s}{:10s}'.format("Player", "Turn",
                "Roll", "Pos"))
    print('{:10s}{:10s}{:10s}{:10s}'.format("------", "----",
                "----", "---"))

    #TODO create a loop that iterates until there is a winner
    while winner == False: #????:

        #TODO update the value of turn, turn is the current round of play
        #????
        turn+=1

        #Generates a random number from 1 to 6 for player 1
        roll1 = random.randint(1,6)

        #TODO add roll1 to update player 1's position
        #????
        player1pos += roll1

        #TODO check the chutes and ladder for the player 1
        #????
        chutes_top = [11,15,30,44,58,64]
        chutes_bottom = [4,7,21,31,43,54]
        ladders_bottom = [8,12,28,33,48,59]
        ladders_top = [16,27,39,46,55,75]
        
        for index in range(len(chutes_top)):
            if player1pos == chutes_top[index]:
                player1pos = chutes_bottom[index]
            
            if player1pos == ladders_bottom[index]:
                player1pos = ladders_top[index]
            
    
        

        #end chutes and ladder for player 1

        #code to print player 1, play close attention to variable names
        #YOU HAVE FOUD THE VARIABLE NAMES!
        print('{:10s}{:10s}{:10s}{:10s}'.format(player1name, str(turn), str(roll1),
                        str(player1pos)))

        #TODO if player 1 has won set condition to get out of the loop
        #????


        #Generates a random number from 1 to 6 for player 2
        roll2 = random.randint(1,6)

        #TODO add roll2 to update player 2's position
        #????



        #TODO check the chutes and ladder for the player 2
        #???? Note, depending how you code this, it may need to be indented



        #end chutes and ladder for player 2

        #code to print player2, play close attention to variable names
        #YOU HAVE FOUD THE VARIABLE NAMES!
        print('{:10s}{:10s}{:10s}{:10s}'.format(player2name, str(turn), str(roll2),
                        str(player2pos)))
        print('==================================')


        #TODO if player 2 has won set condition to get out of the loop
        #????




     #end of the while loop

    #TODO determine and display the winner  (see sample output)
    #????




main()
# this will pause your program if you run it from the desktop
input('Press any key to end program: ')

