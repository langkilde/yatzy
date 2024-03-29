from yatzy.mechanics import gameengine as Engine, utilities

from yatzy.mechanics.action import Action
from yatzy.mechanics.gamestate import GameState
from players.player_user import User

# the game is centered around the game state
state: GameState = Engine.create_initial_state()

# we have to choose which player to play as
player = User()

# the game loop
while not Engine.game_over(state):
    valid_action = False
    action: Action = Action(False)
    utilities.print_game_state(state)

    print(utilities.serialize_state(state))
    while not valid_action:
        action: Action = player.get_action(state)
        valid_action = Engine.validate_action(state, action)
        print("valid action?", valid_action)

    print(utilities.serialize_state(state))

    state = Engine.step(state, action)
