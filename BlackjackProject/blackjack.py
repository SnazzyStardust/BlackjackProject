import random
#Dealer/Player list inits
dealer_hand = []
player_hand = []

#Dealer Hand + Hiding 1st
while len(dealer_hand) != 2:
    dealer_hand.append(random.randint(1, 11))
    if len(dealer_hand) == 2:
        print("Dealer has [REDACTED] & ", dealer_hand[1])

#Player Hand
while len(player_hand) != 2:
    player_hand.append(random.randint(1, 11))
    if len(player_hand) == 2:
        print("Player has ", player_hand, " which equals ", sum(player_hand))

#Dealer Auto Win/Lose Checks
if sum(dealer_hand) == 21:
    print("Dealer Wins")
elif sum(dealer_hand) > 21:
    print("Dealer is Bust")

#Player Sum
while sum(player_hand) < 21:
    move_taken = str(input("Stay or Hit? "))
    if move_taken == "hit":
        player_hand.append(random.randint(1, 11))
        print("Player has ", player_hand, " which equals ", sum(player_hand))
    else:
        print("Player has ", player_hand, " which equals ", sum(player_hand))
        print("Dealer has ", dealer_hand, " which equals ", sum(dealer_hand))
        if sum(dealer_hand) > sum(player_hand):
            print("Dealer Wins")
        else:
            print("Player Wins")
            break

#Player Auto Win/Lose Checks
if sum(player_hand) > 21:
    print("Player is Bust")
elif(sum(player_hand)) == 21:
    print("Player is Blackjack")