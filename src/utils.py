import random
from typing import Callable

def rollDice() -> bool:
    """
    Simulates rolling a 100-sided dice.

    :returns: True if the user wins, False if the house wins.
    :rtype: bool
    """
    roll = random.randint(1, 100)
    if 51 <= roll <= 99:
        return True
    else:
        return False
    
def multiple_betters(funds: int, initial_wager: int, wager_count: int, number_of_betters: int, betting_function: Callable[[int, int, int, bool], None]) -> None:
    """
    Simulates multiple bettors playing a given betting strategy and plots their account values.

    :param funds: The initial amount of money each bettor has to bet with.
    :param initial_wager: The amount of money each bettor bets on each round.
    :param wager_count: The number of rounds each bettor will bet on.
    :param number_of_betters: The number of bettors to simulate.
    :param betting_function: The betting function to use for the simulation.
    """
    for i in range(number_of_betters):
        add_legend = (i == 0)
        betting_function(funds, initial_wager, wager_count, add_legend)