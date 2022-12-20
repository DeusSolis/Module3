import sys
from models import Player, Enemy
from exceptions import EnemyDown, GameOver


def get_player_name():
    while True:
        player_name = input("Enter your name: ").strip()
        if player_name == "":
            continue
        else:
            break
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
            print(f'Enemy {enemy.level - 1} is dead')
            print(f'Player score = {player.score}')

        except GameOver as qwe:
            print(qwe)
            print(f'{player_name} is dead')
            print(f'Score is {player.score}')
            flag = False
        except KeyboardInterrupt:
            print("Good game")
            sys.exit()

        finally:
            print('Слава Україні!!')


if __name__ == "__main__":
    play()
