import json
import random
from math import fabs
from os import listdir
from time import sleep

import matplotlib.pyplot as plt
import numpy
import scipy.stats as sci
from seaborn import set
from playsound import playsound

import random , time, sys, json

from enum import IntEnum




##this is the loop that actually plays the rock paper scissors game with you and logs the data to a list.
##

recognized=1
skipit=input("If you've already played and want to skip straight to the second half, now is the time. Skip the first half? y/n")
while skipit not in ["y","n"]:
    skipit = input("I need a y or n here, not whatever you gave me?\n")
if skipit=="y":
    again=1
else:
    again=0

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2
def giveinput(recentmoves, tracker):
    try:
        move=int(input("\n\nEnter a choice. 0 for ROCK, 1 for PAPER, and 2 for SCISSORS"))
    except ValueError:
        move = int(input("\n\nNo letters, buddy. Try again. Enter a choice: 0 for rock, 1 for paper, 2 for scissors"))
    while move not in [0,1,2]:
        try:
            move = int(input("\n\nSeems something went wrong. Try again. Enter a choice: 0 for rock, 1 for paper, 2 for scissors"))
        except ValueError:
            move = int(input("\n\This is not your day. Enter a choice: 0 for rock, 1 for paper, 2 for scissors"))

    action= Action(move)
    if len(recentmoves)<3:
        recentmoves.append(str(action))
    else:
        recentmoves[tracker]=str(action)
        tracker+=1
        if tracker==3:
            tracker=0
    return action, recentmoves, tracker

def botaction(rockmode,papermode,scissormode):

    if rockmode>0:
        mixup=random.randint(1,5)
        if mixup==1:
            print("He licks his lips"),time.sleep(1)
        if mixup==2:
            print("\nPuppy meat rocks my world, baby\n"), time.sleep(1)

        k = random.choices([0, 1, 2], weights=(90, 5, 5), k=1)
        n = k[0]
        theymove = Action(n)
        rockmode-=1
        return theymove, rockmode, papermode, scissormode
    elif papermode>0:
        mixup=random.randint(1,5)
        if mixup==1:
            print("\nHere's a list of all the puppies I've eaten"), time.sleep(2)
        if mixup==2:
            print("\nMaybe I should play paper more? ;)"), time.sleep(1)
        k = random.choices([0, 1, 2], weights=(5, 90, 5), k=1)
        n = k[0]
        theymove = Action(n)
        papermode-=1
        return theymove, rockmode, papermode, scissormode
    elif scissormode>0:
        mixup=random.randint(1,5)
        if mixup==1:
                print("Gonna cut a bitch."), time.sleep(1.5)
        if mixup==2:
            print("\nSnip snip, you need a puppy cut..."), time.sleep(1.5)

        k = random.choices([0, 1, 2], weights=(5, 5, 90), k=1)
        n = k[0]
        theymove = Action(n)
        scissormode-=1
        return theymove, rockmode, papermode, scissormode
    else:
        rand=random.randint(1,14)
        if rand==1:
            print("\nLooks like you really like that one, huh?"), time.sleep(1)
        if rand==2:
            print("\nI've got a good read on your moves..."), time.sleep(2)
        if rand==3:
            print("\nTime to shake things up!"), time.sleep(1)
        if rand==4:
            print("\nHe seems to be planning something..."), time.sleep(1)
        if rand == 5:
            print("\nI think I'll eat Bo first..."), time.sleep(1)
        k=random.choices([0, 1, 2])
        n=k[0]
        theymove=Action(n)
        return theymove, rockmode, papermode, scissormode

def intro():
    intro = f"Hello there, {name}"
    for char in intro:
        sys.stdout.write(char)
        time.sleep(0.2)
    invite = "\nCmon, let's play Rock Paper Scissors!"
    for char in invite:
        sys.stdout.write(char)
        time.sleep(0.1)
    try:
        please = input("y/n")
    except ValueError:
        please = int(input("\nI didn't get that. y or n?"))
    while please.lower() != "y":
        please = (input("\nPlease? You don't want to play with me? I'm so lonely...and hungry... [y/n]"))

    playsound(
        '/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/FFIX battle theme.mp3',
        False)
    loopit = 0
    while loopit <= 4:
        i = "*"
        k = 9
        interval = 2
        for loop in range(1, 20, 2):
            if loop < 9:
                print(k * " " + loop * "*"), time.sleep(.1)
                k -= 1
            if loop > 9 and loop <= 19:
                increment = loop - interval
                print(k * " " + increment * "*"), time.sleep(.1)
                k += 1
                interval += 4
        loopit += 1
    print("\nThe rules are very simple!"), time.sleep(2)
    print("\nYou win, I let you go."), time.sleep(2)
    print("\nYou lose, and I, LORD PUPPYMUNCHER, get to eat your puppies!"), time.sleep(5)
    print("\nOh, and, this is a fight to the death. En Garde!"), time.sleep(2)


def playgame(rockmode,papermode,scissormode,recentmoves,tracker, phealth, bhealth):

    p1move,recentmoves,tracker=giveinput(recentmoves,tracker)
    if recentmoves==['Action.Rock','Action.Rock','Action.Rock']:
        scissormode=0
        rockmode=0
        papermode=1
        print("\nThink you've got me figured out? Have at you!"), time.sleep(2)
    if recentmoves==['Action.Paper','Action.Paper','Action.Paper']:
        scissormode=1
        rockmode=0
        papermode=0
        print("\nYou know, mixing things up from time to time is a good idea!"), time.sleep(2)
    if recentmoves == ['Action.Scissors', 'Action.Scissors', 'Action.Scissors']:
        scissormode = 0
        rockmode = 1
        papermode = 0
        print("\nYou thought you figured me out? I'm just getting started!"), time.sleep(2)
    if rockmode==0 and papermode==0 and scissormode==0:
        beastmode=random.randint(1,4)
        if beastmode==2:
            val= random.randint(1,3)
            if val==1:
                rockmode=random.randint(1,3)
            if val == 2:
                papermode = random.randint(1, 3)
            if val == 3:
                scissormode = random.randint(1, 3)
    botmove,rockmode,papermode,scissormode=botaction(rockmode,papermode,scissormode)

    movetracker.append(p1move) #this is the list entry
    print("ROCK\n"),time.sleep(.3)
    print("    PAPER\n\n"),time.sleep(.3)
    print("         SCISSORS\n"),time.sleep(.3)

    if p1move == botmove:
        print(f"\n\n\n\nIt's a draw!")
        return rockmode, papermode, scissormode, phealth, bhealth, tracker
    elif p1move == 0: #ROCK
        if botmove == 1: #VS paper
            playsound("/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/gothit.wav")


            print(f"\n\n\n\nYour ROCK lost to their PAPER! You take 1 damage!"), time.sleep(1)
            phealth-=1
            print(f"\nYou've got {phealth} hp, he's got {bhealth} hp left"), time.sleep(1)
        if botmove == 2: #vs scissors
            playsound("C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/hitthem.mp3")

            print(f"\n\n\n\nYour ROCK smashes their SCISSORS! It takes 1 damage!"), time.sleep(1.5)
            bhealth -= 1
            print(f"\nYou've got {phealth}, he's got {bhealth} left"), time.sleep(1)
    elif p1move == 1: #PAPER
        if botmove == 0: #vs ROCK
            playsound("/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/hitthem.mp3")

            print(f"\n\n\n\nYour PAPER covers their ROCK!! They take 1 damage!"), time.sleep(1.5)
            bhealth -= 1
            print(f"\nYou've got {phealth}, he's got {bhealth} left"), time.sleep(1)
        if botmove == 2: #vs SCISSORS
            playsound("/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/gothit.wav")

            print(f"\n\n\n\nYour PAPER loses to their SCISSORS! You take 1 damage!"), time.sleep(1.5)
            phealth -= 1
            print(f"\nYou've got {phealth}, he's got {bhealth} left"), time.sleep(1)
    elif p1move == 2: #scissors

        if botmove == 1: #vs paper
            playsound("/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/hitthem.mp3")
            bhealth-=1
            print(f"\n\n\n\nYour SCISSORS cut up their PAPER!"), time.sleep(1.5)
        if botmove == 0: # vs rock
            playsound("/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/gothit.wav")
            phealth -= 1
            print(f"\n\n\n\nYour SCISSORS lost to their ROCK!"), time.sleep(1.5)
    return rockmode, papermode, scissormode, phealth, bhealth,tracker





match = 1
rockmode=0
papermode=0
scissormode=0
phealth=8
bhealth=8
while again==0:
    name = input("So...what is your name?")
    movetracker = []
    try:
        with open(
                f'C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records/{name}.json') as f:
            movetracker = json.load(f)
    except FileNotFoundError:
        movetracker = []
    if movetracker == []:
        recognized = 0
    if recognized == 1:
        print("Back for more, huh?")

    recentmoves = []
    tracker = 0

    if recognized==0:
        intro()
    if recognized==1:
        again=input("play the intro again? y/n")
        if again=="y":
            intro()
        else:
            again=1
            playsound('/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/audio/FFIX battle theme.mp3', False)
    while phealth>0 and bhealth>0:

        rockmode, papermode,scissormode,phealth,bhealth,tracker = playgame(rockmode, papermode,scissormode, recentmoves,tracker,phealth,bhealth)
        with open(f'C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records/{name}.json', 'w') as f:
            json.dump(movetracker, f)
    if bhealth==0:
        print("\nNOOOOOOOOOOO! I'll get your puppies next time!"),time.sleep(4)
        print("\nI'm melting!"), time.sleep(2)
        print("\nMelting, I say!"), time.sleep(1)
        pain="\nAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHH"
        for char in pain:
            sys.stdout.write(char)
            time.sleep(0.2)
        print("\n\nOut of the blue, Bella appears!"), time.sleep(3)
        print("\n*~Hiiiiii~*"), time.sleep(3)
        print("\nBella takes a dump on the puddle that was once Lord Puppymuncher"),time.sleep(4)
        print("\n THE END \n\n\n")
        while again == 0:
            more = input("Play again? Enter y or n")
            while more.lower() not in ["y", "n"]:
                more = input("Not a valid entry. Enter y or n")
            if more.lower() == "n":
                again = 1
    elif phealth==0:
        print("\n MWAHAHAHA...Now let's go find some puppies to eat..."), time.sleep(4)
        print("\n Ah, yes..."), time.sleep(2)
        stuffie="\nBo and Bella...."
        for char in stuffie:
            sys.stdout.write(char)
            time.sleep(0.4)

        print("\n YOU LOSE"), time.sleep(3)
        while again == 0:
            more = input("Play again? Enter y or n")
            while more.lower() not in ["y", "n"]:
                more = input("Not a valid entry. Enter y or n")
            if more.lower() == "n":
                again = 1




print("\n\n\nOk, on to the super rock paper scissors simulator function!")

#print(movetracker)
#print(recentmoves)




















###################################################################################
###################################################################################
###################################################################################





play1=""
play2=""
p1moves=""
p2moves=""
p1win=0
p2win=0

class player:
    def __init__(self,name,moves, probs):
        self.name=name
        self.moves=moves
        self.probs=probs

    def move(self):
        final=[0,0]
        move=random.choices([0,1,2,3,4,5,6,7,8],weights=(self.probs),k=1)
        choice=move[0]
        if choice==0:
            final=[0,0]
        elif choice==1:
            final=[0,1]
        elif choice==2:
            final=[0,2]
        elif choice==3:
            final=[1,0]
        elif choice==4:
            final=[1,1]
        elif choice==5:
            final=[1,2]
        elif choice==6:
            final=[2,0]
        elif choice==7:
            final=[2,1]
        elif choice==8:
            final=[2,2]

        return final

def selectplayers():
    print("Who do you want to simulate with? ")
    print(listdir("C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records")) # returns list
    play1=input("Please enter the file name to use for player 1. Remember, ignore the .json")
    try:
        with open(f'C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records/{play1}.json') as f:p1moves = json.load(f)
    except FileNotFoundError:
        play1=input("Try again. Please enter the file name to use for player 1. Remember, ignore the .json")
        with open(f'C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records/{play1}.json') as f:p1moves = json.load(f)

    play2=input("\nPlease enter the file name to use for player 2. Remember, ignore the .json")
    try:
        with open(f'C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records/{play2}.json') as f:p2moves = json.load(f)
    except FileNotFoundError:
        play2=input("Try again. Please enter the file name to use for player 2. Remember, ignore the .json")
        with open(f'C:/Users/Matt0/Documents/python learning/Automate the boring stuff/rock paper scissors project/player records/{play2}.json') as f:p2moves=json.load(f)
    return play1, p1moves, play2, p2moves
def namerecog():
    peopleset = {
        "matt": "A real person!",
        "kat": "The prettiest girl that ever lived!",
        "ember": "Ember really likes playing rock, as she relates to them, given her intelligence.",
        "ash": "Ash doesn't have a clue what he's doing. He just randomly picks something.",
        "trump": "Trump is a big fan of rock, but he's also prone to snipping up treaties and regulations with his scissors.",
        "obama": "Obama favors diplomacy, so he likes paper, but he also drone strikes weddings, so he also likes the occasional rock.",
        "neenee":"NeeNee's gardening experience has given her lots of love for snipping plants and throwing scissors.",
        "iris": "*~~~~Hi Kat~~~~*",
        "victorp":"Wants to be hip. Is not hip. Is sexy, tho.",
        "bo":"Bo really likes consistency- he doesn't follow up with different things much, instead he follows up with the same thing pretty often.",
        "bella":"Always a bit restless, Bella doesn't like playing the same move twice.",
        "tina":"Will play anything, but is always thinking about shredding up paper receipts, so she follows with paper a lot."


    }
    try:
        print(f"{p1.name.lower()}:\n {peopleset[p1.name.lower()]}"),  sleep(1)
    except KeyError:
        print(f"{p1.name}: A newcomer in these parts, little is known about this mysterious figure.")
    try:
        print(f"{p2.name.lower()}:\n {peopleset[p2.name.lower()]}"),  sleep(1)
    except KeyError:
        print(f"{p2.name}: A newcomer in these parts, little is known about this mysterious figure.")


def calcprobs(moves): ###updated to calculate a move nuanced set of probabilities per player- now there are 9 PAIRS of moves instead of a general propensity towards 1 move or another.
    paircounts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for cases in range(len(moves)):
        try:
            opts = 0
            pairtype = 0
            while opts < 3:
                for interval in range(0, 3):  # ordering or R2R, R2P, R2S; S2R; S2P; S2S; P2R; P2P; P2S
                    if moves[cases] == opts and moves[cases + 1] == interval:  # R2R
                        paircounts[pairtype] += 1
                    pairtype += 1
                opts += 1
        except IndexError:
            break

    #print(p1moves)
    #print(paircounts)
    probs = [x / len(moves) for x in paircounts]

    return probs

def runagame(p1win, p2win):
    p1move = p1.move()
    p2move = p2.move()
    for pairno in range(0,2):
        while p1move[pairno] == p2move[pairno]:
            #print("draw, going again!")
            p1move = p1.move() #if equal, you need to redraw the moves, as they'll get caught in an infinite loop
            p2move = p2.move() #if equal, you need to redraw the moves, as they'll get caught in an infinite loop



        if p1move[pairno] == 0: ##ROCK vs
            if p2move[pairno] == 1: ##paper
                #print(f"{p2.name} wins")
                p2win += 1
            elif p2move[pairno] == 2: ##scissors
                #print(f"{p1.name} wins")
                p1win += 1

        elif p1move[pairno] == 1: ##PAPER vs
            if p2move[pairno] == 0: #rock
                #print(f"{p1.name} wins")
                p1win += 1
            elif p2move[pairno] == 2: #scissors
                #print(f"{p2.name} wins")
                p2win += 1
        elif p1move[pairno] == 2: #SCISSORS
            if p2move[pairno] == 0: #Rock
                #print(f"{p1.name} wins")
                p2win += 1
            elif p2move[pairno] == 1: #Paper
                #print(f"{p2.name} wins")
                p1win += 1
    return p1win, p2win


def fullgame(bouts,loop):

    p1total = 0
    p2total = 0
    margin=[]
    p1logwins=[]
    p2logwins=[]

    for k in range(bouts):
        p1win = 0
        p2win = 0
        for i in range(loop):
            p1win, p2win = runagame(p1win, p2win)

        margin.append(p1win - p2win)
        p1logwins.append(p1win)
        p2logwins.append(p2win)
        #print(f"The round ends, {p1.name} has {p1win} wins and {p2.name} has {p2win}")

        if p1win==p2win:
                continue

        elif p1win>p2win:
                #print(f"{p1.name} won this bout!")
                p1total+=1
        else:
                #print(f"{p2.name} won this bout!")
                p2total+=1

    if p1total>p2total:
        results="HERE'S HOW IT WENT!"
        print(f"\n{results.center(48, '=')}")

        print(f"\nwow, it looks like {p1.name}'s the winner of this series of bouts with {p1total} wins vs {p2total}! ")
    else:
        results = "HERE'S HOW IT WENT!"
        print(f"\n{results.center(48, '=')}")
        print(f"\nOh boy! {p2.name}'s the winner of this series of bouts with {p2total} wins vs {p1total}! ")

    if match>=80:
        stats(p1logwins, p2logwins, margin, bouts)

def stats(p1logwins, p2logwins, margin,bouts):
    print(f"On average, {p1.name} got {numpy.mean(p1logwins)} wins with an SD of {numpy.std(p1logwins)} ")
    print(f"this translates to a 95% CI around the mean of {sci.t.interval(alpha=0.95, df=len(p1logwins)-1, loc=numpy.mean(p1logwins), scale=sci.sem(p1logwins))}")

    print(f"\n\nOn average, {p2.name} got {numpy.mean(p2logwins)} wins with an SD of {numpy.std(p2logwins)}")
    print(f"this translates to a 95% CI around the mean of {sci.t.interval(alpha=0.95, df=len(p2logwins)-1, loc=numpy.mean(p2logwins), scale=sci.sem(p2logwins))}")

    if numpy.mean(margin)<0:
        print(f"\nThe average margin of victory was {  fabs(numpy.mean(margin))}, SD={numpy.std(margin)} in {p2.name}'s favor")
        print(f"this translates to a 95% CI around the mean of {sci.t.interval(alpha=0.95, df=len(margin) - 1, loc=numpy.mean(margin), scale=sci.sem(margin))}")
    elif numpy.mean(margin)>0:
        print(f"\nThe average margin of victory was {  fabs(numpy.mean(margin))}, SD={numpy.std(margin)} in {p1.name}'s favor")
        print(f"this translates to a 95% CI around the mean of {sci.t.interval(alpha=0.95, df=len(margin)-1, loc=numpy.mean(margin), scale=sci.sem(margin))}")

    print(f"\nWe can look at if either player is more likely to win on average using several hypothesis tests."
          f"\n The first is an independent samples t-test that determines if the mean win rates differ"
          f"\nOn average, {p1.name} got {numpy.mean(p1logwins)}"
          f"\nOn average, {p2.name} got {numpy.mean(p2logwins)} ")

    print(sci.stats.ttest_ind(p1logwins,p2logwins, equal_var=True,nan_policy="propagate", alternative="two-sided"))
    print(f"\n\n Another way to look at it is to see if the margin of victor is significantly different from 0, since"
          f"\n a non zero margin on average= one side wins more or less on average"
          f"\n So, is the value of {numpy.mean(margin)} significantly different from 0?")

    print(sci.stats.ttest_1samp(margin, popmean=0, axis=0, nan_policy="propagate", alternative="two-sided"))
    print("\n\nlet's graph stuff!\n The graphs plot wins and victory margins. Bigger gaps between the lines=bigger odds of someone winning bouts\n")
    print("\n\n TO CONTINUE YOU MUST CLOSE THE GRAPH WINDOWS!")

    set()
    margmean=numpy.mean(margin)

    zeroline=0
    CImargin=(abs(sci.sem(margin))*2.58)*2
    CImargin2=sci.t.interval(alpha=0.95, df=len(margin) - 1, loc=numpy.mean(margin), scale=sci.sem(margin))


    location=[]
    location.append(CImargin2[0])
    location.append(0)
    plt.figure(1)
    height, bins, patches =plt.hist(margin,bins=100,alpha=.4)
    _= plt.hist(margin, bins=100, color="k", alpha=.4)
    _=plt.axvline(margmean,color="red", linestyle="dashed")
    _=plt.axvline(zeroline,color="green", linestyle="dashed")
    _=plt.fill_betweenx([0, height.max()], CImargin2[0], CImargin2[1], color='red', alpha=0.15)  # Mark between 0 and the highest bar in the histogram
    _=plt.title('Plotting the amount by which games are won/lost')
    _=plt.xlabel(f"<---{p2.name} wins--_________--{p1.name} wins--->")
    #plt.show()



    p1mean=numpy.mean(p1logwins)
    p2mean=numpy.mean(p2logwins)

    p1ci=sci.t.interval(alpha=0.95, df=len(p1logwins) - 1, loc=numpy.mean(p1logwins), scale=sci.sem(p1logwins))
    p2ci=sci.t.interval(alpha=0.95, df=len(p2logwins) - 1, loc=numpy.mean(p2logwins), scale=sci.sem(p2logwins))

    centerline=match/2
    #for a graph with both win rates
    plt.figure(2)
    height2, bins, patches=plt.hist(p1logwins, bins=100, alpha=.5, label=f"{p1.name}")
    height3, bins, patches=plt.hist(p2logwins, bins=100, alpha=.5, label=f"{p2.name}")

    plt.axvline(centerline,color="k", linestyle="dashed")
    plt.axvline(p1mean,color="blue", linestyle="dashed")
    plt.fill_betweenx([0, height2.max()], p1ci[0], p1ci[1], color='grey', alpha=0.35)  # Mark between 0 and the highest bar in the histogram
    plt.fill_betweenx([0, height3.max()], p2ci[0], p2ci[1], color='grey', alpha=0.35)  # Mark between 0 and the highest bar in the histogram

    plt.axvline(p2mean,color="red", linestyle="dashed")
    plt.title(f'Comparison of win rates for {p1.name} vs {p2.name}')
    plt.xlabel("# of wins per round")
    plt.ylabel("frequency")

    plt.legend(loc="best")
    plt.show()

################################################################################
endit=0

print("\nThis simulator analyzes your and other people's real and fictional rock paper scissors data to model\n"
      "massively long rock paper scissors matches. Though this can't be used to determine who will win any one match,\n"
      "it does give evidence for who is more likely to win bouts or matches in the grand scheme of things.\n")
while endit==0:
    play1, p1moves, play2, p2moves=selectplayers()

    p1probs=calcprobs(p1moves)
    p2probs=calcprobs(p2moves)

    p1 = player(play1, p1moves, p1probs)
    p2 = player(play2, p2moves, p2probs)
    namerecog()

    #p1win,p2win=runagame(p1win,p2win)


    try:
        match=int(input("\nHow many rock paper scissors battles? Best of... [use 80+ for \n graphs and hyp tests, they don't show it LT 80 b/c they look dumb.]"))
    except ValueError:
        match=int(input("\nNo words. How many rock paper scissors battles? Best of... [use 80+ for \n graphs and hyp tests, they don't show if LT 80 b/c they look dumb.]"))



    try:
        bouts=int(input(f"\nHow many sets of {match}?"))
    except ValueError:
        bouts=int(input(f"\nNo words. How many sets of {match}?"))
    print("\nRunning the battles now. This might take a few minutes if you're doing huge numbers...")

    trurounds = round(match / 2)
    # if trurounds %2==1:
    #   trurounds+=1
    fullgame(bouts,int(trurounds))

    moresims=input("\nRun another simulated match? y/n")
    while moresims.lower() not in ["y" ,"n"]:
        moresims = input("\nYou can only input y/n. Run another simulated match? y/n")
    if moresims.lower()== "n":
        endit=1
    print("Ok, that's it. you can close me now!")
