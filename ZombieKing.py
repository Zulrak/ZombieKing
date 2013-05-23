""" Name: Jordan Cooper
    Date: Wednesday, May 08, 2013
    Purpose: Create a working version of the diagram (as seen in the table of contents).
             The Player will be asked to make a series of decisions that will ultimately
             lead to the success or failure of the mission, collecting the treasure from
             the friendly dragon's choice. The program must provide at least 3 levels of
             decisions.
"""
import time

def displayIntro():
    print ('The year is 2014, Its been one year since Patient zero was infected by Chemical 114.')
    print ('Chemical 114 was supposed to be a cure for the common cold, and in a way it worked,')
    print ('those who are infected no longer catch colds, they caught their death.')
    print ("They didn't stay dead though, the dead soon came back to life and when they did they were zombies.")
    time.sleep(15)
    print ('')
    print ('')
    print ('You and your Companion are walking down the road when you come across a graveyard,')
    time.sleep(3)
    print ('the trees are all dead and all of the graves have been disturbed.')
    time.sleep(3)
    print ('You see a church on the grounds and decide to go in and search for supplies.')
    time.sleep(3)
    print ('As you walk up to the church you hear a slight groaning sound...')
    time.sleep(3)
    print ('Suddenly the doors swing open!')
    time.sleep(2)
    print ('The zombies attack you and your companion!')
    time.sleep(2)
    print ('You manage to get away but the horde of zombies takes your Companion and drags her away!')
    print ('You know they are using her for bait but you must try and save her!')
    print ('')
    print ('')

# Pick between the Church(1) and Catacombs(2) collect as raw_input
def decision1():
    choice = ''
    while choice != 'church' and choice != 'catacombs':
        print ('You step back into the church. You hear noises from all around you. The way you see it, there are two options...')
        time.sleep(2)
        print('You can search the church, or the catacombs below the church to search for your companion')
        print('')
        time.sleep(2)
        print('Please enter your choice (church or catacombs): ')
        choice = raw_input()

        if choice == "church":
            churchDecision2()
        else:
            catacombsDecision2()

def churchDecision2():
    choice =''
    while choice != 'left' and choice != 'right':
        print ('You begin to search the church...')
        time.sleep(1)
        print ('You Continue to walk until you reach the end of the hallway, you can go left into the next room')
        print ('Or you can go right, and follow the adjoining hallway')
        time.sleep(3)
        print ('Please enter your choice left or right: ')
        choice = raw_input()

        if choice == "left":
            churchDecision3Left()
        else:
            churchDecision3Right()
#LEFT decision2 _________________________________________________________________________________________           
def churchDecision3Left():
    choice =''
    while choice != 'MG' and choice != 'HG':
        print ('You begin to search the room...')
        time.sleep(1)
        print ('You find a machine gun and ammo in a small crate in the room.')
        print ("You can take the machine gun but you can't carry your hand gun and the machine gun.")
        time.sleep(3)
        print ('Please enter your choice MG (for take machine gun) or HG (for keep hand gun): ')
        choice = raw_input()
    
        if choice == "MG":
            decision4AA()
        else:
            decision4AB()


def decision4AA():
    print ('You take the Machine Gun and continue into the next room')  
    print ('Suddenly a horde of zombies pop out and attack you!')
    time.sleep(2)
    print ('You fire  your gun killing as many of the zombies as you can when suddenly...')
    time.sleep(2)
    print ('You lose your fotting and fall through the floor!')
    time.sleep(2)
    print ('You land in the basement surrounded by zombies!')
    time.sleep(2)
    print ('Your gun jams!')
    time.sleep(2)
    print ('The zombies take this opertunity to strike! ... You have Died!')
    time.sleep(3)
    print ('')
    print ('')
    
def decision4AB():
    print ('You leave the Machine Gun and continue into the next room')   
    print ('Suddenly a horde of zombies pop out and attack you!')
    time.sleep(2)
    print ('You struggle to get your gun out')
    time.sleep(2)
    print ('You fire your gun!')
    time.sleep(2)
    print ('Sadly the horde of zombies is too much to handle... You have Died!')
    time.sleep(3)
    print ('')
    print ('')
#RIGHT_________________________________________________________________________________________________
  
def churchDecision3Right():
    choice =''
    while choice != 'sneak' and choice != 'fight':
        print ('You continue to walk down the hallway...')
        time.sleep(1)
        print ('You hear a large number of groaning zombies further down the hall...')
        time.sleep(2)
        print ('As a skilled zombie killer you can sneak past these zombies without being detected...usually.')
        print ("Or you can put those zombie killing skills to use and fight them like a man!.")
        time.sleep(3)
        print ('Please enter your choice sneak or fight: ')
        choice = raw_input()
        
        if choice == "sneak":
            churchDecision4Sneak()
        else:
            churchDecision4Fight()
        
def churchDecision4Sneak():
    
        print ('You continue to sneak down the hallway...')
        time.sleep(1)
        print ('As you slowly move past the horde of zombies, making sure to not to make a sound...')
        time.sleep(2)
        print ('You accidently step on a rotten floor board!')
        time.sleep(2)
        print ("The zombies suddenly become aware of your presence!.")
        time.sleep(2)
        print ("The zombies charge at you! They claw, bite and chase you as you start to run!.")
        time.sleep(2)
        print ("While running away from the zombies you are bitten!")
        time.sleep(2)
        print ('The virus begins to spread through your viens.')
        time.sleep(1)
        print ("You try to fight it but their is no hope.")    
        time.sleep(1)
        print ("You have turned into a zombie! You have died!")    
        
def churchDecision4Fight():
    
        print ('You continue to walk down the hallway...')
        time.sleep(1)
        print ('You pick up a rotten floor board and charge at the zombies!')
        time.sleep(2)
        print ('Even with all of your zombie killing skill you are no match for the zombie horde!')
        time.sleep(2)
        print ("While you savagely strike at the zombies you are bitten!")
        time.sleep(2)
        print ('The virus begins to spread through your viens.')
        time.sleep(1)
        print ("You try to fight it but their is no hope.")    
        time.sleep(1)
        print ("You have turned into a zombie! You have died!")    
        
#End of the church options________________________________________________________________________________
        

def catacombsDecision2():
    print ('test Choice 2 Chosen')
   


def main():    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        # displayIntro()
        decision1()

        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()