## Card Game Project - "Using python to create a multiple function using a deck of cards"
## Name - Shriram Sivaraman
## Course - Introduction to Python Programming 
## Course code - MSIT 3440
## Description - The objective of the program is to create multiple functions to handle deck of cards

from __future__ import print_function
import operator
import random

def deckOK(deck):
    ''' checks a deck of cards passed in as a parameter
    the deck must have 52 unique card representations.
    The function does not check values or suits but it will
    detect duplicate cards. '''
    if len(deck)!=52:
        print ('BAD DECK: wrong number of cards (',len(deck),')')
        return False
    for card in deck:
        if deck.count(card) > 1:
            print ('BAD DECK: duplicate card (',card,')')
            return False
    print ('The deck looks OK')
    return True

## Function 1 to accept the cards
def makeDeck():
    values=range(2,15)*4
    suits=['s','d','h','c']*13
    combine=[]
    combine=range(len(values))
    for inc in combine:
        combine[inc]=values[inc],suits[inc]
    return list(combine)

raw_input('hit enter to make the deck of cards, shuffle and check it')
my_deck = makeDeck()        
print (deckOK(my_deck))
random.shuffle(my_deck)
random.shuffle(my_deck)

## Function 2 to determine the name of the cards
def cardValueName(card):
    try:
        assign=makeDeck()
        if  11 in assign[card]:
            return 'Jack'
        elif 12 in assign[card]:
            return 'Queen'
        elif 13 in assign[card]:
            return 'King'
        elif 14 in assign[card]:
            return 'Ace'
        elif 2 in assign[card]:
            return '2'
        elif 3 in assign[card]:
            return '3'
        elif 4 in assign[card]:
            return '4'
        elif 5 in assign[card]:
            return '5'
        elif 6 in assign[card]:
            return '6'
        elif 7 in assign[card]:
            return '7'
        elif 8 in assign[card]:
            return '8'
        elif 9 in assign[card]:
            return '9'
        elif 10 in assign[card]:
            return '10'
    except IndexError:
        print (' The number is out of range! enter a number between 0-51')        ## handling the out-of-range values
        return ''

raw_input('hit enter to see the value of the card on top of the deck')
print (cardValueName(my_deck[0]))
## Function 3 - To determine the suit name

def cardSuitName(card):
    try:
        assign=makeDeck()
        if 'c' in assign[card]:
            return 'Clubs'
        elif 'd' in assign[card]:
            return 'Diamond'
        elif 's' in assign[card]:
            return 'Spade'
        elif 'h' in assign[card]:
            return 'Hearts'
    except IndexError:
        print ('The number is out of range! Enter a number between 0-51')       ## handling the out-of-range values
        return ''
        
## Function 4 - To combine the card number and suit name

def cardName(card):
    try:
        return cardValueName(card)+' of '+cardSuitName(card)
    except IndexError:
        print ('The number is out of range! Enter a number between 0-51')
        return ''


## Function 5 - To display the list of cards

def printCards(cards):
    assign=[]
    ## for loop to list all the cards
    for inc in range(cards):
        assign.append(cardName(inc))
    ##print(*assign,sep='\n')                                            ## To print the items in the list line by line (commented out to print as list)
    return assign

## Initializing variables and passing it as argument        
my_dump=52
my_draw=printCards(my_dump)
print ('Deck has total number of ',len(my_draw),' cards')               ## to determine the total number of cards in the deck

## Function 6 - Deal cards

def dealCards(cards):
    global my_draw
    assign=my_draw.pop(0)                                               ## To remove the specific card from the deck 
    return assign

my_drive=dealCards(my_dump)
print ('\nThe card which is popped off from the deck is : ',(my_drive))
print ('\nDeck now has total number of ',(len(my_draw)),' cards')


## Function 7 - Deal hands

def dealHands(deck, nHands, nCards):
    hand=[]
    if (nHands*nCards > len(deck)):                                   ## To check whether the total cards exceeds the deck
        print ('Enter the current number of cards within the limit')
    elif (nHands*nCards <= len(deck)):                                ## To assure the total cards is distributed to every player
        for i in range(nHands):
            for inc in range(nCards):
                hand.append((dealCards(len(deck))))
        chunk = [hand[x:x+nCards] for x in range(0,len(deck),nCards)] ## To create a list within a list containing cards
    return chunk

## variables initialized and passed as argument
my_list=printCards(20)
my_risk=dealHands(my_list,2,10)
print(" \nDistributing the cards to hands ")
print ('Hand 0:'," /  ".join(my_risk[0]))
print ('Hand 1:'," /  ".join(my_risk[1]))
##print ('Hand 2:'," /  ".join(my_risk[2]))                           ## In case to increase the number of players(commented out to handle two players)
##print ('Hand 3:'," /  ".join(my_risk[3]))
print ('Deck now has total number of ',(len(my_draw)),' cards after distribution')

## Function 8 - To sort using suit
def cardSuitKey(card):
    if 'Clubs' in card:
        return 'c'
    elif 'Spade' in card:
        return 's'
    elif 'Diamond' in card:
        return 'd'
    elif 'Hearts' in card:
        return 'h'

hands=dealHands(my_list,2,5)
print ("\nCards available in Hand 0 and Hand 1 before sorting with Suit value")
print ('Hand 0 :'," / ".join(hands[0]))
print ('Hand 1 :'," / ".join(hands[1]))
## Sorting the cards as per the suit
hands[0].sort(key = cardSuitKey)
hands[1].sort(key = cardSuitKey)
print ("Cards available in Hand 0 and Hand 1 after sorting with Suit value")
print ('Hand 0 :'," /  ".join(hands[0]))
print ('Hand 1 :'," / ".join(hands[1]))

## Function 9 - To sort using card value

def cardValueKey(card):
    if 'Ace' in card:
        return 14
    elif 'King' in card:
        return 13
    elif 'Queen' in card:
        return 12
    elif 'Jack' in card:
        return 11
    elif '10' in card:
        return 10
    elif '9' in card:
        return 9
    elif '8' in card:
        return 8
    elif '7' in card:
        return 7
    elif '6' in card:
        return 6
    elif '5' in card:
        return 5
    elif '4' in card:
        return 4
    elif '3' in card:
        return 3
    elif '2' in card:
        return 2

hands=dealHands(my_list,2,5)
print ("\nCards available in Hand 0 and Hand 1 before sorting with card value")
## sorting the cards as per value
print ('Hand 0 :'," / ".join(hands[0]))
print ('Hand 1 :'," / ".join(hands[1]))
hands[0].sort(key = cardValueKey)
hands[1].sort(key = cardValueKey)
print ("Cards available in Hand 0 and Hand 1 after sorting with card value")
print ('Hand 0 :'," /  ".join(hands[0]))
print ('Hand 1 :'," / ".join(hands[1]))
    
    

## Task 5 - Card Game Elements
## Function 10 - To list the cards as per color
def cardColor(card):
    ## If loop made to run to check for card color
    if 'Clubs' in card:
        return 'black'
    elif 'Spade' in card:
        return 'black'
    elif 'Hearts' in card:
        return 'red'
    elif 'Diamond' in card:
        return 'red'

## Testing for color 
my_deck=52
card=dealCards(my_deck)
print ('\nThe popped card ',dealCards(card),' is ',cardColor(card))


## Function 11- check for same color for two cards from the suit
def sameCardColor(card1,card2):
    if cardColor(card1)==cardColor(card2):            ## Condition to check if both cards belong to same color
        return True
    else:
        return False


## Testing for same color check follows

card1=dealCards(my_deck)
card2=dealCards(my_deck)
my_spaw=sameCardColor(card1,card2)
## If loop made to run to display if cards have same color or not
if my_spaw is True:
    print ('Popped cards',card1,' and ',card2,' are of same color ')
else:
    print ('Popped cards',card1,' and ',card2,' are of different color')


## Function 12- Check for Sequence UP
    

def cardSequenceUp(card1,card2):
    val1=cardValueKey(card1)
    val2=cardValueKey(card2)
    if (val1+1) == val2:                        ## condition to check if val2 is one greater than val 1
        return True
    else:
        return False

## Testing for ascending up
card1=my_draw[1]
card2=my_draw[2]
card3=my_draw[3]

print ('\nCheck for the sequence up and sequence down cards')
print(card1,' --->', card2,' ascending is ', cardSequenceUp(card1,card2))
print(card2,' --->', card3,' ascending is ', cardSequenceUp(card2,card3))
print(card3,' --->', card1,' ascending is ', cardSequenceUp(card3,card1))
print(card3,' --->', card2,' ascending is ', cardSequenceUp(card3,card2))

       
##Function 13- Check for Sequence Down

def cardSequenceDown(card1,card2):
    val1=cardValueKey(card1)
    val2=cardValueKey(card2)
    if (val2+1) == val1:                      ## condition to check val1 is one greater than val2
        return True
    else:
        return False

## Testing for descending down
card1=my_draw[1]
card2=my_draw[2]
card3=my_draw[3]

print(card1,' --->', card2,' descending is ', cardSequenceDown(card1,card2))
print(card2,' --->', card3,' descending is ', cardSequenceDown(card2,card3))
print(card3,' --->', card1,' descending is ', cardSequenceDown(card3,card1))
print(card3,' --->', card2,' descending is ', cardSequenceDown(card3,card2))

## Function 14 - Listing all elements from same suit

def cardsOfSuit(hand,suit):
    assign=[]
    if suit=='c':
        for inc in range(len(hand)):
            if 'Clubs' in hand[inc]:
                assign.append(hand[inc])
    if suit=='d':
        for inc in range(len(hand)):
            if 'Diamond' in hand[inc]:
                assign.append(hand[inc])
    if suit=='h':
        for inc in range(len(hand)):
            if 'Hearts' in hand[inc]:
                assign.append(hand[inc])
    if suit=='s':
        for inc in range(len(hand)):
            if 'Spade' in hand[inc]:
                assign.append(hand[inc])
    return assign
                        
print ('\nThe cards in the hand are :'," / ".join(my_draw))
hand_of_card=cardsOfSuit(my_draw,'c')
print ('The cards removed from specified suit(c) are :'," / ".join(hand_of_card))



## Function 15 - removing a random element from a list
def randomCard(hand):
    assign=[]
    random.shuffle(hand)
    assign=hand.pop()
    return assign

random_element=randomCard(my_draw)
print ("The random card removed from the suit in hand:",random_element)


## Function 16 - removing the highest value card
def highestCard(hand):
    hand.sort(key = cardValueKey)
    assign=hand.pop(-1)
    return assign

high_val=highestCard(my_draw)
print ("The highest value card from the suit in hand: ",high_val)

##Function 17 - removing the lowest value card
def lowestCard(hand):
    hand.sort(key = cardValueKey)
    assign=hand.pop(0)
    return assign

low_val=lowestCard(my_draw)
print ("The lowest value card from the suit in hand : ",low_val)

## Function 18 - default check for suit

def cardsOfSuit(hand,suit):
    assign=[]
    if suit=='c':
        for inc in range(len(hand)):
            if 'Clubs' in hand[inc]:
                assign.append(hand[inc])
    elif suit=='d':
        for inc in range(len(hand)):
            if 'Diamond' in hand[inc]:
                assign.append(hand[inc])
    elif suit=='h':
        for inc in range(len(hand)):
            if 'Hearts' in hand[inc]:
                assign.append(hand[inc])
    elif suit=='s':
        for inc in range(len(hand)):
            if 'Spade' in hand[inc]:
                assign.append(hand[inc])
    else:
        for inc in range(len(hand)):
            assign.append(hand[inc])
    return assign
                        
print ('\nThe cards in the hand are :'," / ".join(my_draw))
hand_of_card=cardsOfSuit(my_draw,None)                                  ## None value check and it returns all the cards from the suit
print ('The cards removed from specified suit :'," / ".join(hand_of_card))
    

        

    



    
    







               
    



