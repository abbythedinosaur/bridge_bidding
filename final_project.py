# a program to determine how to open a bid in a round of bridge
# card count should be based off a standard 13 card hand
#note: ace = 4 points, king = 3 points, queen = 2 points, jack = 1 point
#all other cards = 0 points


# user input section for card length and strength
while True:
    try:
        club_count = eval(input("How many clubs do you have? "))
        if club_count < 0:
            raise ValueError
        break
    except NameError:
        print("Not a valid number, try again")
    except ValueError:
        print("Not a valid number, try again")
while True:
    try:
        if club_count == 0:
            club_points = 0
            print("0 points in clubs")
        elif club_count >= 0:
            club_points = eval(input("How many points in clubs do you have? "))
        elif club_points < 0:
            raise ValueError
        break
    except ValueError:
        print("Not a valid number, try again")
while True:
    try:
        diamond_count = eval(input("How many diamonds do you have? "))
        if diamond_count < 0:
            raise ValueError
        break
    except NameError:
        print("Not a valid number, try again")
    except ValueError:
        print("Not a valid number, try again")

while True:
    try:
        if diamond_count == 0:
            diamond_points = 0
            print("0 points in diamonds")
        elif diamond_count >= 0:
            diamond_points = eval(input("How many points in diamonds do you have? "))
        if diamond_points < 0:
            raise ValueError
        break
    except ValueError:
        print("Not a valid number, try again")

while True:
    try:
        heart_count = eval(input("How many hearts do you have? "))
        if heart_count < 0:
            raise ValueError
        break
    except NameError:
        print("Not a valid number, try again")
    except ValueError:
        print("Not a valid number, try again")

while True:
    try:
        if heart_count == 0:
            heart_points = 0
            print("0 points in hearts")
        heart_points = eval(input("How many points in hearts do you have? "))
        if heart_points < 0:
            raise ValueError
        break
    except ValueError:
        print("Not a valid number, try again")

spade_count = (13-club_count-diamond_count-heart_count)

while True:
    try:
        if spade_count == 0:
            spade_points = 0
            print("You have 0 spades and 0 points in spades")
        elif spade_count == 1:
            spade_points = eval(input("You have 1 spade. How many points in spades do you have? "))
        elif spade_count >= 1:
            spade_points = eval(input("You have " + str(spade_count) + " spades. How many points in spades do you have? "))
        else:
            raise ValueError
        break
    except ValueError:
        print("Not a valid number, try again")
        
        
# sum of all points in all suits
total_points = (club_points + diamond_points + heart_points + spade_points)
print("Your hand has", total_points, "points")

# a list of the suits, to be indexed later
suits = ["clubs", "diamonds", "hearts", "spades"]
suit_sing = ["club", "diamond", "heart", "spade"]

# a list of the suit counts
suit_count_list = []
suit_count_list.append(club_count)
suit_count_list.append(diamond_count)
suit_count_list.append(heart_count)
suit_count_list.append(spade_count)

longest_suit_int = max(suit_count_list)

# a list of the suit points
suit_point_list = []
suit_point_list.append(club_points)
suit_point_list.append(diamond_points)
suit_point_list.append(heart_points)
suit_point_list.append(spade_points)

# index positions of the longest and strongest suits
strongest_suit_index = suit_point_list.index(max(suit_point_list))
longest_suit_index = suit_count_list.index(max(suit_count_list))

#strongest and longest suits
strongest_suit = suits[strongest_suit_index]
longest_suit = suits[longest_suit_index]
longest_suit_sing = suit_sing[longest_suit_index]
strongest_suit_sing = suit_sing[strongest_suit_index]

# a tree to determine if a hand is balanced or unbalanced
for i in suit_count_list:
    if i > 4:
        hand = "unbalanced"
        break
    elif i <= 2:
        point_position = suit_count_list.index(i)
        if suit_point_list[point_position] >= 3:
            hand = "balanced"
        elif suit_point_list[point_position] < 3:
            hand = "unbalanced"
            break
    elif i == 3:
        hand = "balanced"
print("Your hand is", hand)

# this tree determines bidding if a hand is balanced
if hand == "balanced":
    if total_points >= 20:
        print("Bid 2 no trump")
    elif total_points >= 15:
        print("Bid 1 no trump")
    elif total_points >= 12:
        if spade_count >= 5:
            if spade_count == heart_count:
                if spade_points >= heart_points:
                    print("Bid 1 spade")
                elif heart_points > spade_points:
                    print("Bid 1 heart")
                else:
                    print("Welp")
            else:
                print("Bid 1 spade")
        elif heart_count >= 5:
            if heart_count == diamond_count:
                print("Bid 1 heart")
            else:
                print("Bid 1 heart")
        elif diamond_count >= club_count:
            if diamond_count == club_count:
                if diamond_points == club_points:
                    print("Bid 1 diamond or 1 club")
                elif diamond_points > club_points:
                    print("Bid 1 diamond")
                elif club_points > diamond_points:
                    print("Bid 1 club")
                else:
                    print("Welp")
        elif club_count > diamond_count:
            print("Bid 1 club")
        else:
            print("Welp")
    elif total_points < 12:
        print("Pass")
    else:
        print("Welp")

# this tree determines bidding if a hand is unbalanced
if hand == "unbalanced":
    if total_points >= 22:
        print("Bid 2 clubs")
    elif total_points >= 13:
        if longest_suit_int >= 5:
            if longest_suit == "spades":
                print("Bid 1 spade")
            if longest_suit == "hearts":
                if spade_count == heart_count:
                    if heart_points >= spade_points:
                        print("Bid 1 heart")
                    elif spade_points > heart_points:
                        print("Bid 1 spade")
                    elif longest_suit != "spades":
                        print("Bid 1 heart")
                    else:
                        print("Welp")
                elif heart_count > spade_count:
                    print("Bid 1 heart")
            elif longest_suit == "diamonds":
                if diamond_count == heart_count:
                    print("Bid 1 heart")
                elif diamond_count > heart_count:
                    print("Bid 1 diamond")
            elif longest_suit == "clubs":
                if diamond_count == club_count:
                    if diamond_points >= club_points:
                        print("Bid 1 diamond")
                    elif club_points > diamond_points:
                        print("Bid 1 club")
                elif club_count > diamond_count:
                    print("Bid 1 club")
        elif longest_suit_int < 5:
            if diamond_count >= 3:
                print("Bid 1 diamond")
            elif club_count >=3:
                print("Bid 1 club")
    elif total_points < 13:
        print("Pass")
    else:
        print("Welp")
