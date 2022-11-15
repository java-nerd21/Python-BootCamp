computer = [11,11]
i = computer.index(11)
computer[i] = 1



def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        index = hand.index(11)
        hand[index] = 1
        return sum(hand)
    elif score == 21:
        return 0
    else:
        return score

score = calculate_score(hand=computer)
print(score)