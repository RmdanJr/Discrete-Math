# Final Project: Dice Game
""" program that will play optimally in a tricky dice game! Program will be given a list of dices and will decide who chooses the dice first.

When the dices are chosen, we will simulate 10000 throws. Each time number is greater, you get $1 from opponent. Conversely, each time number is smaller, you pay $1 to opponent. """

# First Task: Compare Two Dices
"""function that takes two dices as input and computes two values: the first value is the number of times the first dice wins (out of all possible 36 choices), the second value is the number of times the second dice wins. We say that a dice wins if the number on it is greater than the number on the other dice. """
def count_wins(dice1, dice2):
    assert len(dice1) == 6 and len(dice2) == 6
    dice1_wins, dice2_wins = 0, 0
    
    # write your code here
    for i in dice1:
        for j in dice2:
            if i > j:
                dice1_wins += 1
            elif j > i:
                dice2_wins += 1
    return (dice1_wins, dice2_wins)

# Second Task: Is there the Best Dice?
""" function that takes a list of dices and checks whether there is dice (in this list) that is better than all other dices. We say that a dice is better than another one, if it wins more frequently (that is, out of all 36 possibilities, it wins in a cases, while the second one wins in b cases, and a>b). If there is such a dice, return its (0-based) index. Otherwise, return -1. """
def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    # write your code here
    # use your implementation of count_wins method if necessary
    for i in range(0, len(dices), 1):
        count = 0
        for j in range(0, len(dices), 1):
            if i == j:
                continue
            (count_i, count_j) = count_wins(dices[i], dices[j])
            if(count_i > count_j):
                count += 1
        if(count == len(dices) - 1):
            return i
    return -1

# Third Task: Implement a Strategy
""" function that takes a list of dices (possibly more than three) and returns a strategy. The strategy is a dictionary:

If, after analyzing the given list of dices, you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose

If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then, specify, for each dice that your opponent may take, the dice that you would take in return. Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first. """
def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
        
    # write your code here
    best_dice = find_the_best_dice(dices)
    if best_dice != -1:
        strategy["choose_first"] = True
        strategy["first_dice"] = best_dice
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if i == j:
                    continue
                (count_i, count_j) = count_wins(dices[i], dices[j])
                if count_j > count_i:
                    strategy[i] = j
                    break
    return strategy