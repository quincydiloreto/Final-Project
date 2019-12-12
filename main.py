#final project black jack

import random

print("Welcome to Blackjack!")
win_counter = "Games Won:", 0
print(win_counter)

#dictionary with cards and values
cards = {'Ace of Diamonds':1, '2 of Diamonds':2, '3 of Diamonds':3, '4 of Diamonds':4,
     '5 of Diamonds':5, '6 of Diamonds':6, '7 of Diamonds':7, '8 of Diamonds':8, '9 of Diamonds':9,
     '10 of Diamonds':10, 'Jack of Diamonds':10, 'Queen of Diamonds':10, 'King of Diamonds':10,
     'Ace of Hearts':1, '2 of Hearts':2, '3 of Hearts':3, '4 of Hearts':4, '5 of Hearts':5,
     '6 of Hearts':6, '7 of Hearts':7, '8 of Hearts':8, '9 of Hearts':9, '10 of Hearts':10,
     'Jack of Hearts':10, 'Queen of Hearts':10, 'King of Hearts':10, 'Ace of Clubs':1, 
     '2 of Clubs':2, '3 of Clubs':3, '4 of Clubs':4, '5 of Clubs':5, '6 of Clubs':6, 
     '7 of Clubs':7, '8 of Clubs':8, '9 of Clubs':9, '10 of Clubs':10, 'Jack of Clubs':10, 
     'Queen of Clubs':10, 'King of Clubs':10, 'Ace of Spades':1,  '2 of Spades':2, '3 of Spades':3, 
     '4 of Spades':4, '5 of Spades':5, '6 of Spades':6, '7 of Spades':7, '8 of Spades':8, 
     '9 of Spades':9, '10 of Spades':10, 'Jack of Spades':10, 'Queen of Spades':10, 'King of Spades':10
 }

#dealing cards
deal = random.choice(list(cards.items()))[1]
deal1 = random.choice(list(cards.items()))[1]


  

print("Your cards are:", deal, "; ", deal1)

total = deal+deal1

#player turn
'''
if deal in cards == 'Ace of Diamonds' or 'Ace of Hearts' or 'Ace of Clubs' or 'Ace of Spades':
    ACE = input("Do you want Ace to be 1 or 11? " )
    if ACE == 1:
        total + 1

    elif ACE == 11:
        total + 11
        
    else:
        pass
    print(total)        
else: 
    pass  
'''
if deal == 1:
    total += 10
    if total > 21:
        total -= 10
else:
    pass

if deal1 == 1:
    total += 10
    if total > 21:
        total -= 10
else:
    pass


print("You are at: ", total)
    
answer = input("Will you hit or stay? ")

while answer == "hit":
    deal2 = random.choice(list(cards.items()))[1]
    print("New card is:, ", deal2)
    print(deal2+total)
    total = deal2+total
    if total > 21:
        print("You bust! End of turn")
        break    
    answer = input("Will you hit or stay? ")
    if answer == "stay":
        print("end of turn")
    else:
        pass
if answer == "stay":
        print("end of turn")
else:
    pass


#dealers turn

deal_tur = random.choice(list(cards.items()))[1]
deal_tur1 = random.choice(list(cards.items()))[1]

deal_tot = deal_tur + deal_tur1

print("Dealer cards are:", deal_tur, "; ", deal_tur1)

if deal_tur == 1:
    deal_tot += 10
    if deal_tot > 21:
        deal_tot -= 10
else:
    pass

if deal_tur1 == 1:
    deal_tot += 10
    if deal_tot > 21:
        deal_tot -= 10
else:
    pass

while deal_tot <= 16:
    deal_tur2 = random.choice(list(cards.items()))[1]
    print("Dealer new card is:, ", deal_tur2)
    print(deal_tur2+deal_tot)
    if deal_tot > 21:
        print("Dealer bust!")
        break
if deal_tot >= 17:
    print("Dealer stays at ", deal_tot)
else:
    pass

#finding winner

if deal_tot > total:
    print("dealer wins!")
elif deal_tot < total:
    print("You win!")
    win_counter + 1
elif deal_tot == total:
    print("game was a push!")
else:
    pass     

