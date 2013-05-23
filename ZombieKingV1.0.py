
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
    
def decision1():
    choice = ''
    while choice != '1' and choice != '2':
        print ('You step back into the church. You hear noises from all around you. The way you see it, there are two options...')
        time.sleep(2)
        print('You can search the church (1), or go into the Catacombs (2) below the church to search for your companion')
        print('')
        print('Please enter your choice (1 or 2): ')
        choice = raw_input()
    return choice
    
def checkchoice(decision1):
    
    if decision1 == "1":
        choice1()
    else:
        choice2()

def choice1():
    print ('test Choice 1 Chosen')
    
def choice2():
    print ('test Choice 2 Chosen')
    

def main():
    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        choiceNumber = decision1()
        checkchoice(choiceNumber)
    
        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
