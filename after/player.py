from abc import ABC, abstractmethod
import random
from typing import Optional, TYPE_CHECKING

from handmovements import HandMovements

if TYPE_CHECKING:
    from ui import UI


class Player(ABC):

    def __init__(self, name: str, hand_move: Optional[HandMovements] = None):
        self.name = name
        self.hand_move = hand_move
        self.win_count = 0

    @abstractmethod
    def pick_move(self, ui: 'UI'):
        pass

    def score(self):
        self.win_count += 1

    def __str__(self):
        return self.name


class HumanPlayer(Player):
    def pick_move(self, ui: 'UI'):
        self.hand_move = ui.get_user_input()


class AutomaticPlayer(Player):
    def pick_move(self, ui: 'UI'):
        cpu_choice = random.randint(1, len(HandMovements))
        self.hand_move = HandMovements(cpu_choice)
