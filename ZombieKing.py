"""
    Author: Jordan Cooper
    Last Modified By: Jordan Cooper
    Last Modified: May 23 13
    Program Description: The Player will be asked to make a series of decisions that will ultimately
                         lead to the success or failure of the mission, to save your companion from
                         the evil Zombie King and his horde of undead minions. The player must go through
                         3 different levels of decisions and use the special items in an attempt to win the game.
    Version 1.4 - Completed the final game
                - 3 decision levels 
                - formatted the outcome text to look neat and readable
                
"""
import time

def displayIntro():
    print ("The year is 2014, It's been one year since Patient zero was infected by Chemical 114.")
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
    time.sleep(3)
    print ('The zombies attack you and your companion!')
    time.sleep(3)
    print ('You manage to get away but the horde of zombies takes your Companion and drags her away!')
    print ('You know they are using her for bait but you must try and save her!')
    print ('')
    print ('')

def displayRules():
    
    time.sleep(3)
    print ("Rules: Please enter the options displayed in the 'Please enter line' only those words will" )
    print ("       be accepted and bring you to the next level of the game. ")
    print ("NOTE:  If at any time you wish to change your answer simply type 'back' on the option line")
    time.sleep(10)
    print("")
    print("")
    
# Pick between the Church(1) and Catacombs(2) collect as raw_input
def decision1():
    choice = ''
    while choice != 'church' and choice != 'catacombs':
        print ('You step back into the church. You hear noises from all around you. The way you see it, there are two options...')
        time.sleep(3)
        print('You can search the church, or the catacombs below the church to search for your companion')
        time.sleep(3)
        print('')
        print('Please enter your choice (church or catacombs): ')
        choice = raw_input()

        if choice == "church":
            churchDecision2()
        else:
            catacombsDecision2()
#Church______________________________________________________________________________________________
def churchDecision2():
    choice =''
    while choice != 'left' and choice != 'right' and choice != 'back':
        print ('You begin to search the church...')
        time.sleep(1)
        print ('You Continue to walk until you reach the end of the hallway, you can go left into the next room')
        time.sleep(3)
        print ('Or you can go right, and follow the adjoining hallway')
        time.sleep(3)
        print('')
        print ("Please enter your choice 'left' or 'right' or 'back': ")
        choice = raw_input()

        if choice == "left":
            churchDecision3Left()
        elif choice == "right":
            churchDecision3Right()
        elif choice == "back":
            decision1()
#LEFT Church _________________________________________________________________________________________           
def churchDecision3Left():
    choice =''
    while choice != 'MG' and choice != 'HG' and choice != 'back':
        print ('You begin to search the room...')
        time.sleep(1)
        print ('You find a machine gun and ammo in a small crate in the room.')
        time.sleep(3)
        print ("You can take the machine gun but you can't carry your hand gun and the machine gun.")
        time.sleep(3)
        print('')
        print ("Please enter your choice 'MG' (for take machine gun) or 'HG' (for keep hand gun) or 'back': ")
        choice = raw_input()
    
        if choice == "MG":
            churchDecision4MG()
        elif choice == "HG":
            churchDecision4HG()
        elif choice == "back":
            churchDecision2()

def churchDecision4MG():
    
    print ('')
    time.sleep(2)
    print ('You take the Machine Gun and continue into the next room')  
    time.sleep(3)
    print ('Suddenly a horde of zombies pop out and attack you!')
    time.sleep(3)
    print ('You fire  your gun killing as many of the zombies as you can when suddenly...')
    time.sleep(3)
    print ('You lose your footing and fall through the floor!')
    time.sleep(3)
    print ('You land in the basement surrounded by zombies!')
    time.sleep(3)
    print ('Your gun jams!')
    time.sleep(2)
    print ('The zombies take this opportunity to strike! ... You have Died!')
    time.sleep(3)
    print ('')
    print ('')
    
def churchDecision4HG():
    
    print ('')
    time.sleep(2)
    print ('You leave the Machine Gun and continue into the next room')  
    time.sleep(3) 
    print ('Suddenly a horde of zombies pop out and attack you!')
    time.sleep(3)
    print ('You struggle to get your gun out')
    time.sleep(3)
    print ('You fire your gun!')
    time.sleep(2)
    print ('Sadly the horde of zombies is too much to handle... You have Died!')
    time.sleep(3)
    print ('')
    print ('')
    
#RIGHT_________________________________________________________________________________________________
  
def churchDecision3Right():
    choice =''
    while choice != 'sneak' and choice != 'fight' and choice != 'back':
        print ('You continue to walk down the hallway...')
        time.sleep(2)
        print ('You hear a large number of groaning zombies further down the hall...')
        time.sleep(3)
        print ('As a skilled zombie killer you can sneak past these zombies without being detected...usually.')
        time.sleep(2)
        print ("Or you can put those zombie killing skills to use and fight them like a man!.")
        time.sleep(3)
        print('')
        print ("Please enter your choice ;sneak; or ;fight; or 'back': ")
        choice = raw_input()
        
        if choice == "sneak":
            churchDecision4Sneak()
        elif choice == "fight":
            churchDecision4Fight()
        elif choice == "back":
            churchDecision2()
        
def churchDecision4Sneak():
    
    print ('')
    time.sleep(1)
    print ('You continue to sneak down the hallway...')
    time.sleep(3)
    print ('As you slowly move past the horde of zombies, making sure to not to make a sound...')
    time.sleep(3)
    print ('You accidently step on a rotten floor board!')
    time.sleep(3)
    print ("The zombies suddenly become aware of your presence!.")
    time.sleep(3)
    print ("The zombies charge at you! They claw, bite and chase you as you start to run!.")
    time.sleep(3)
    print ("While running away from the zombies you are bitten!")
    time.sleep(3)
    print ('The virus begins to spread through your veins.')
    time.sleep(3)
    print ("You try to fight it but there is no hope.")    
    time.sleep(3)
    print ("You have turned into a zombie! You have died!") 
    print ('')
    print ('')   
        
def churchDecision4Fight():
    
    print ('')
    time.sleep(2)
    print ('You continue to walk down the hallway...')
    time.sleep(2)
    print ('You pick up a rotten floor board and charge at the zombies!')
    time.sleep(3)
    print ('Even with all of your zombie killing skill you are no match for the zombie horde!')
    time.sleep(3)
    print ("While you savagely strike at the zombies you are bitten!")
    time.sleep(3)
    print ('The virus begins to spread through your veins.')
    time.sleep(3)
    print ("You try to fight it but there is no hope.")    
    time.sleep(3)
    print ("You have turned into a zombie! You have died!")    
    print ('')
    print ('')
        
#Catacombs________________________________________________________________________________
        
def catacombsDecision2():
    choice =''
    while choice != 'down' and choice != 'forward' and choice != 'back':
        print ('You begin to search the church...')
        time.sleep(2)
        print ('You find the passageway to the catacombs under the alter!')
        time.sleep(2)
        print ('You walk down the crumbling spiral staircase, with each step you feel colder and colder...')
        time.sleep(2)
        print ('When you reach the bottom of the staircase you realize there is a ladder that could lead to a second level of the catacombs')
        time.sleep(2)
        print ('You can go down the ladder or continue to search through the catacombs.')
        time.sleep(3)
        print('')
        print ("Please enter your choice 'down' or 'forward' or 'back': ")
        choice = raw_input()

        if choice == "down":
            catacombsDecision3Down()
        elif choice == "forward":
            catacombsDecision3Forward()
        elif choice == "back":
            decision1()
#Down________________________________________________________________________
def catacombsDecision3Down():
    choice =''
    while choice != 'take' and choice != 'leave' and choice != 'back':
        print ('You climb down the ladder and start to walk down the new hallway')
        time.sleep(3)
        print ('The hall is filled with the corpses of the dead,')
        time.sleep(3)
        print ('they must be the remains of other survivors who have come here searching for supplies.')
        time.sleep(3)
        print ('You notice the corpse of a prison guard. You can take his tactical supplies, riot gear and weapons')
        time.sleep(3)
        print ("but you won't be able to carry all of this gear and your medical pack.")
        time.sleep(3)
        print ('You will have to make a difficult choice, Take the gear or keep your medical pack...')
        time.sleep(3)
        print('')
        print ("Please enter your choice 'take' (the tactical supplies) or 'leave' (the tactical supplies) or 'back':")
        choice = raw_input()

        if choice == "take":
            catacombsDecision4Take()
        elif choice == "leave":
            catacombsDecision4Leave()
        elif choice == "back":
            catacombsDecision2()

def catacombsDecision4Take():
    
    time.sleep(3)
    print ("You put on the dead guard's riot gear and pick up his supplies")
    time.sleep(3)
    print ('You continue to walk down the hall until you reach the end of the hall')
    time.sleep(3)
    print ('At the end of the hall you see a large cave, upon closer inspection you see your companion!')
    time.sleep(3)
    print ('She is being guarded by the zombie king and his horde of zombies!')
    time.sleep(3)
    print ('You charge in and attack the zombie king!')
    time.sleep(3)
    print ('The zombies try to bite you but you are protected by your armor!')
    time.sleep(3)
    print ('With one steady shot from your rifle you shoot the zombie king in the head!')
    time.sleep(2)
    print ('You finish off the rest of the zombies with your tactical knife and rescue your companion!')
    time.sleep(3)
    print ('Congratulations you have successfully rescued your companion and defeated the zombie king!')
    print ('')
    print ('')

def catacombsDecision4Leave():
    
    print ('')
    time.sleep(3)
    print ('You continue to walk down the hall until you reach the end of the hall')
    time.sleep(3)
    print ('At the end of the hall you see a large cave, upon closer inspection you see your companion!')
    time.sleep(3)
    print ('She is being guarded by the zombie king and his horde of zombies!')
    time.sleep(3)
    print ('You charge in and attack the zombie king!')
    time.sleep(3)
    print ('The zombie king throws his sword at you!')
    time.sleep(3)
    print ('You move to dodge the blade, the blade cuts your neck and opens up an artery')
    time.sleep(3)
    print ('You try to bandage your wound with your medical kit but there is no time!')
    time.sleep(3)
    print ('You try to untie your companion')
    time.sleep(3)
    print ('The horde blocks your path!')
    time.sleep(1)
    print ("You try to run but it's too late!")
    time.sleep(1)
    print ('You have lost too much blood. You start to black out...')
    time.sleep(3)
    print ('You lost too much blood to survive. The horde of zombies eats your corpse!')
    print ('You have died!!!')
    print ('')
    print ('')


#Forward_________________________________________________________________________________________

def catacombsDecision3Forward():
    choice =''
    while choice != 'caution' and choice != 'run' and choice != 'back':
        print ('You begin to search the catacombs...')
        time.sleep(3)
        print ('As you walk down the hall you notice a pile of corpses down the hall')
        time.sleep(3)
        print ('The bodies are riddled with arrows, the hall must be booby trapped')
        time.sleep(3)
        print('You can proceed with caution or take your chances and run like hell!')
        print('')
        print ("Please enter your choice 'caution' or 'run' or 'back': ")
        choice = raw_input()

        if choice == "caution":
            catacombsDecision4Caution()
        elif choice == "run":
            catacombsDecision4Run()
        elif choice == "back":
            catacombsDecision2()
            
def catacombsDecision4Caution():
    
    print ('')
    print('You pick up a handful of rocks from the floor and toss them down the hall...')
    time.sleep(3)
    print('The rocks triggered the pressure plates on the floor, can hear the arrow dispenser firing but no arrows appear, it must have ran out.')
    time.sleep(3)
    print('Slowly you proceed down the hall, you cut the tripwire and proceed down the dark, wet hall')
    time.sleep(3)
    print('Suddenly...')
    time.sleep(1)
    print('You turn the corner and a zombie pops out and eats you! You have died!')
    time.sleep(3)
    print('')
    print ('')
    
def catacombsDecision4Run():
    
    print ('')
    print('Taking a few steps back, you get ready to run past the traps!')
    time.sleep(3)
    print('You sprint past the pressure triggered arrows, leap past the corpses of those who fell before you')
    print('but just as you think you have made it past the traps...')
    time.sleep(3)
    print('Your foot lands on the tripwire! The ground begins to crumble under you!')
    time.sleep(3)
    print('You have been impaled on a pile of jagged steel spikes')
    print('You have died!')
    time.sleep(3)
    print('')
    print ('')
    
#End of game_________________________________________________________________________________________          
def main():    
    
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':
        displayIntro()
        displayRules()
        decision1()

        print ('Do you want to play again? (yes or no)')
        playAgain = raw_input()


if __name__ == "__main__": main()
