import random

from yatzy.action import Action
from yatzy.gamestate import GameState


class ActorRandom:

    def __init__(self):
        pass

    def get_action(self, state: GameState, playable_combinations) -> Action:
        playable_combinations = list(playable_combinations.keys())
        score = random.randint(0, 1)
        if state.rolls > 2:
            score = True
        locked_dices = [random.randint(0, 1) for x in range(0, 5)]
        action = Action(score, locked_dices, random.choice(playable_combinations))
        return action
