from game import Game
from player import HumanPlayer, AutomaticPlayer
from ui import UI


def main() -> None:
    """Main function to start the game
    """
    user_name = UI.get_user_name()
    game = Game(HumanPlayer(user_name), AutomaticPlayer('CPU'))
    game.play()


if __name__ == '__main__':
    main()
