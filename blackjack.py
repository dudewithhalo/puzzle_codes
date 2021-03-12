#balckjack or 21 game
import random
#the planning phase

dealer_cards = []


player_cards = []
#deal the cards

#Dealer cards
while len(dealer_cards) != 2:
    dealer_cards.append(random.randint(1,11))
    if len(dealer_cards) == 2:
        print("Dealer has X and",dealer_cards[1])

#player cards
while len(player_cards) != 2:
    player_cards.append(random.randint(1,11))
    if len(player_cards) == 2:
        print("Player has", player_cards)
#display the cards
#sum of the dealers cards
if sum(dealer_cards) == 21:
    print("Dealer has 21 and wins!")
elif sum(dealer_cards) > 21:
    print("Dealer has busted!")

#sum of the player cards

#if P card sum > 21 , it is a bust, P loses
#otherwise , option hit or say
#if P options stay compare sum of D vs P
#if p <21 and >D , then P wins
#if P < D , then P loses

while sum(player_cards) < 21:
    next_move = input("Do you  want to stay or hit?")
    if next_move == "hit":
        player_cards.append(random.randint(1,11))
        print("You have a total of {} from {}".format((sum(player_cards)),player_cards))
    else:
        print("The Dealer has a total of {} with {}".format((sum(dealer_cards)), dealer_cards))
        print("You have a total of {} with {}".format((sum(player_cards)), player_cards))
        if sum(dealer_cards) > sum(player_cards):
            print("Dealer Wins!")
        else:
            print("You Win!")
            break

#compare the sum of the cards between D and P

if sum(player_cards) > 21:
    print("You Busted!")
elif sum(player_cards)  == 21:
    print("You have BLACKJACK. You Win!")
