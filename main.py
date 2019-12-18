#final project black jack

import random
'''
this is the intro code, it gives a welcome message with a win counter
it will then use a dictionary to store the values of the cards. 
it then will give you two random cards and adds the values together. 
'''
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
under the player trun it first checks to see if the card you got was an ace.
it will check to see if the card value will go over 21, if it does 
the card value that will be added to the total will be 1, if it does not go over 21
it will be 11 that is added to the total  
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
"""
this next chunk will use a while loop that will check your input
if it is hit it will give you another card, if thats the case it will
add the number you just got to your total. if you go over 21 it will end your turn
if not it will keep prompting you until you get to a spot where you want to stay
"""
while answer == "hit":
    deal2 = random.choice(list(cards.items()))[1]
    print("New card is:, ", deal2)
    print("You are now up to: ", deal2+total)
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
if total == 21:
    print("Congratulations on the Blackjack!")
else:
    pass    

#dealers turn
if total > 21:
    print("Dealer wins!")
    exit()
else:
    pass
deal_tur = random.choice(list(cards.items()))[1]
deal_tur1 = random.choice(list(cards.items()))[1]

print("Dealer cards are:", deal_tur, "; ", deal_tur1)

deal_tot = deal_tur + deal_tur1


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
print("Dealer Total is: ", deal_tot)


while deal_tot <= 16:
    deal_tur2 = random.choice(list(cards.items()))[1]
    print("Dealer new card is:, ", deal_tur2)
    print(deal_tur2 + deal_tot)
    deal_tot = deal_tur2 + deal_tot
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
    
elif deal_tot == total:
    print("game was a push!")
else:
    pass     

