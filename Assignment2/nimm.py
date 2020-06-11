"""
File: nimm.py
-------------------------
Add your comments here.
"""

PILE = 20

def main():

    stones =  PILE
    player = 1
    while stones > 0:
        print ("There are " + str (stones) + " stones left")
        x = int(input("Player" + str(player)+" would you like to remove 1 or 2 stones? "))
        #if x==1 or x==2:
         #   print("Ey enna?")
        while x!= 1 and x!= 2:
            x = int(input("Please enter either 1 or 2 "))
        stones = stones - x
        if player == 1:
            player = 2
        else:
            player = 1
    print("Game Over")
    print("Player "+str(player)+ " wins!")

# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
