from models import Player, Enemy
from exceptions import EnemyDown, GameOver


def get_player_name():
    player_name = input("Enter your name: ").strip()
    return player_name


def play():
    player_name = get_player_name()
    player = Player(player_name)
    enemy = Enemy()

    flag = True
    while flag:
        try:
            player.attack(enemy)
            player.defence(enemy)
        except EnemyDown as qwe:
            print(qwe)
            print(f'Enemy {enemy.level} is dead')
            print(f'{player.score}')

        except GameOver as qwe:
            print(qwe)
            print(f'{player_name} is dead')
            print(f'Score is {player.score}')
            flag = False


if __name__ == "__main__":
    play()
