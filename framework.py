from Player import *
from unit import *
from feworld import *
from FinalAI import *
import Tkinter as tk
from PIL import ImageTk
from PIL import Image
import time
from simpleGUI import display


def _delete_window():
    try:
        print "Prof Oak: You can't run from a trainer battle!"
        #root.destroy()
    except:
        pass
def _destroy(event):
    pass

#pass in the GUI, map, and both players
def play_game(root, level, player1, player2, strat1 = "a", strat2 = "a"):

    root.protocol("WM_DELETE_WINDOW", _delete_window)
    root.bind("<Destroy>", _destroy)

    quit = False

    #get the # of units to start so you can tell when one dies
    p1units = len(player1.units)
    p2units = len(player2.units)

    while(len(player1.units) == p1units and len(player2.units) == p2units):
        #run while no units have died
        display(level,root)
        while(len(player1.movedUnits) != len(player1.units)):
            quit = player1.play_turn(level, strat1)
            display(level,root)
            if quit:
                break

        if quit:
            break

        if(len(player1.units) == p1units and len(player2.units) == p2units):
            #only let the computer move if the game has not ended
            print "\n"
            while (len(player2.units) != len(player2.actedUnits)):
                player2.play_turn(level, strat2)
                time.sleep(1)
                display(level,root)
                time.sleep(1)
            print "\n"
        #reset everything
        player1.movedUnits = []
        player1.actedUnits = []
        player2.movedUnits = []
        player2.actedUnits = []
    if len(player1.units) != p1units:
        print "Player 2 wins!"
    elif quit:
        print "Quitting..."
    else:
        print "Player 1 wins!"
    display(level,root)
    root.destroy()
    root.mainloop() 
