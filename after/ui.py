from handmovements import HandMovements
from player import Player


class UI:
    def display_rules(self):
        print("Rock paper scissor spock and lizard...\n Welcome to the game.")
        print("Rules are simple...")
        print(
            "Scissors decapitate Lizard, Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors.")
        print("To begin press [Enter]")
        _ = input()

    def display_entity_options(self) -> None:
        """Displays the user choices
        """
        choices_text = ", ".join(f"({entity.value} for {entity.name})" for entity in HandMovements)
        print(f"Select {choices_text}:", end='\t')

    def get_user_input(self) -> HandMovements:
        """Takes user inputs and selects the entities

        Returns:
            HandMovements: Entity selected by user
        """
        available_choices = [entity.value for entity in HandMovements]
        while True:
            try:
                self.display_entity_options()
                choice = int(input())

                if choice not in available_choices:
                    print("Please select from available choices")
                else:
                    return HandMovements(choice)
            except ValueError:
                print("You entered something other than a number")

    def display_current_round(self, player_one: Player, player_two: Player) -> None:
        print(f"{player_one} ({player_one.hand_move.name}) x {player_two} ({player_two.hand_move.name})")
        print("....")

    def display_round_winner(self, message: str) -> None:
        print(message)

    def display_scores(self, *players: Player):
        print("Scoreboard:")
        print("======================================")
        for player in players:
            print(f"{player} : {player.win_count}", end='\t')
        print("\n======================================")

    @staticmethod
    def get_user_name() -> str:
        """Static method to get user name as input

        Returns:
            str: Name enterd by user
        """
        print("Please enter your name:", end='\t')
        return str(input().strip())
