from player import Player
from rules import Rules
from ui import UI


class Game:
    """Game class
    """
    def __init__(self, player_one: Player, player_two: Player, max_round: int = 5) -> None:
        
        self.ui = UI()
        self.max_round = max_round
        self.rules = Rules()
        self.player_one = player_one
        self.player_two = player_two
    
    def do_turn(self) -> None:
        """Function to continue the rounds
        """
        self.player_one.pick_move(self.ui)
        self.player_two.pick_move(self.ui)

        self.ui.display_current_round(self.player_one, self.player_two)

        winner, message = self.rules.get_results(self.player_one, self.player_two)
        self.ui.display_round_winner(message)
        if winner:
            winner.score()

    def play(self):
        self.ui.display_rules()
        for i in range(self.max_round):
            self.do_turn()
            self.ui.display_scores(self.player_one, self.player_two)
