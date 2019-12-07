#final project black jack

import random

print("Welcome to Blackjack!")
win_counter = "Games Won:", 0
print(win_counter)

#dictionary with cards and values
cards = {'Ace of Diamonds':(1,11), '2 of Diamonds':2, '3 of Diamonds':3, '4 of Diamonds':4,
     '5 of Diamonds':5, '6 of Diamonds':6, '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
     '10 of Diamonds':10, 'Jack of Diamonds':10, 'Queen of Diamonds':10, 'King of Diamonds':10,
     'Ace of Hearts':(1,11), '2 of Hearts':2, '3 of Hearts':3, '4 of Hearts':4, '5 of Hearts':5,
     '6 of Hearts':6, '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9, '10 of Hearts':10,
     'Jack of Hearts':10, 'Queen of Hearts':10, 'King of Hearts':10, 'Ace of Clubs':(1,11), 
     '2 of Clubs':2, '3 of Clubs':3, '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6, 
     '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9, '10 of Clubs':10, 'Jack of Clubs':10, 
     'Queen of Clubs':10, 'King of Clubs':10, 'Ace of Spades':(1,11),  '2 of Spades':2, '3 of Spades':3, 
     '4 of Spades':4, '5 of Spades':5, '6 of Spades':6, '7 of Spades':7, '8 of Spades':8, 
     '9 of Spades':9, '10 of Spades':10, 'Jack of Spades':10, 'Queen of Spades':10, 'King of Spades':10
 }

#dealing cards

deal = random.choice(list(cards.keys()))
deal1 = random.choice(list(cards.keys()))
print("Your cards are:", deal, "; ", deal1)
print("You are at: ", (deal + deal1))

#player turn
answer = input("Will you hit or stay? ")

while answer == "hit":
    deal2 = random.choice(list(cards.keys()))
    print(deal2)
    answer = input("Will you hit or stay? ")
    if answer == "stay":
        print("end of turn")
    else:
        pass
if deal == 'Ace of Diamonds' and 'Ace of Hearts' and 'Ace of Clubs' and 'Ace of Spades':
    ACE = input("Do you want Ace to be 1 or 11?" )
    if ACE == 1:
        deal + 1
    elif ACE == 11:
        deal + 11
    else:
        pass    
else: 
    pass  




#dealers turn

     

