from handmovements import HandMovements
from typing import Tuple, Optional, Union

from player import Player


class Rules:
    """Class to register all the rules
    """
    winner_actions = {
        (HandMovements.PAPER, HandMovements.ROCK): 'covers',
        (HandMovements.PAPER, HandMovements.SPOCK): 'disapproves',
        (HandMovements.ROCK, HandMovements.LIZARD): 'crushes',
        (HandMovements.ROCK, HandMovements.SCISSOR): 'crushes',
        (HandMovements.SCISSOR, HandMovements.PAPER): 'cuts',
        (HandMovements.SCISSOR, HandMovements.LIZARD): 'decapitates',
        (HandMovements.SPOCK, HandMovements.SCISSOR): 'smashes',
        (HandMovements.SPOCK, HandMovements.ROCK): 'vaporizes',
        (HandMovements.LIZARD, HandMovements.SPOCK): 'poisons',
        (HandMovements.LIZARD, HandMovements.PAPER): 'eats',
    }

    def get_results(self, player_one: Player, player_two: Player) -> Tuple[Optional[Player], str]:
        winner, loser = self._get_winner_and_loser(player_one, player_two)
        message = self._get_message(winner, loser)
        return winner, message

    def _get_winner_and_loser(self, player_one: Player, player_two: Player) -> Union[Tuple[Player, Player], Tuple[None, None]]:
        if player_one.hand_move == player_two.hand_move:
            return None, None
        if (player_one.hand_move, player_two.hand_move) in self.winner_actions:
            return player_one, player_two
        return player_two, player_one

    def _get_message(self, winner: Player, loser: Player):
        if winner is not None:
            action = self.winner_actions[(winner.hand_move, loser.hand_move)]
            return f'{winner} ({winner.hand_move.name}) wins the round as {winner.hand_move.name} {action} {loser.hand_move.name}'
        return 'It\'s a tie'



