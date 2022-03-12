import random

def menu():
    choice=0
    game=False
    while choice!='1' and '2':
        choice=input('Enter 1 to play game, or 2 to exit: ')
        if choice!='1' and choice!='2':
            print('Enter 1 or 2')
        else:
            break

    if choice=='1':
        game=True
    elif choice=='2':
        game=False

    return game

def deckCreation():
    deckSize=0
    accept=False
    while accept!=True:
        deckSize=input('Enter a number between 4 and 30 that is even. This will be your deck size: ')
        if deckSize.isdigit()==True:
            deckSize=int(deckSize)
            if deckSize>3 and deckSize<31:
                division=deckSize%2
                if division==0:
                    accept=True
                else:
                    print('Enter an even number')
            else:
                print('Enter a number between 4 and 30')
        else:
            print('Enter a number')
                    
    deck=[]
    with open('dogs.txt', 'r') as file:
        for x in range(0,deckSize):
            line=file.readline()
            field=line.split(',')
            name=field[0]
            excersise=random.randint(1,5)
            agility=random.randint(1,5)
            intelligence=random.randint(1,100)
            drool=random.randint(1,10)
            deck.append([name,excersise,agility,intelligence,drool])

    random.shuffle(deck)
    half=len(deck)/2
    half=int(half)
    card_num=len(deck)
    userDeck=[]
    for item in range(0,half):
        card=deck[item]
        userDeck.append(card)
    comDeck=[]
    for item in range(half,card_num):
        card=deck[item]
        comDeck.append(card)

    print(userDeck)
    print(comDeck)
    return userDeck,comDeck

def comparison(pos,currentCards):
    userValue=currentCards[0][pos]
    print(userValue)
    comValue=currentCards[1][pos]
    print(comValue)
    if comValue>userValue:
        print('com')
    else:
        print('user')
    

def userTurn(prevWinner,userDeck,comDeck):
    print()
    if prevWinner==True:
        print('Name: '+userDeck[0][0])
        print('Excersise: '+str(userDeck[0][1]))
        print('Agility: '+str(userDeck[0][2]))
        print('Intelligence: '+str(userDeck[0][3]))
        print('Drool: '+str(userDeck[0][4]))
    print()
    choice=0
    print('''Categories:
Excersise    (1)
Agility      (2)
Intelligence (3)
Drool        (4): ''')
    while choice!='1'and'2'and'3'and'4':
        choice=input('Enter 1, 2, 3 or 4: ')
        if choice=='1':
            print('You chose excersise')
            pos=1
        elif choice=='2':
            print('You chose agility')
            pos=2
        elif choice=='3':
            print('You chose intelligence')
            pos=3
        elif choice=='4':
            print('You chose drool')
            pos=4
        else:
            print('invalid')

    currentCards=[]
    currentCards.append((userDeck[0]))
    currentCards.append((comDeck[0]))
    del userDeck[0]
    del comDeck[0]
    print(currentCards)
    print(userDeck)
    print(comDeck)
    comparison(pos,currentCards)
    


prevWinner=True
userDeck,comDeck=deckCreation()
userTurn(prevWinner,userDeck,comDeck)
