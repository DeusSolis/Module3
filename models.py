from random import choice
from settings import HEROES, INITIAL_PLAYER_HEALTH, ENEMY_LEVEL
from exceptions import EnemyDown, GameOver


class Enemy:
    def __init__(self):
        self.level = ENEMY_LEVEL
        self.health = self.level

    def __str__(self):
        return f'{self.level = }'

    def decrease_health(self):
        """decrease health enemy"""
        self.health -= 1
        if self.health == 0:
            self.level += 1
            self.health = self.level
            raise EnemyDown(self.level - 1)


    def select_attack(self):
        """Enemy attack"""
        return choice(HEROES)

    def select_defence(self):
        """Enemy defence"""
        return choice(HEROES)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.health_points = INITIAL_PLAYER_HEALTH

    def __repr__(self):
        return f'Player name {self.name}'

    def decrease_health(self):
        """decrease health player"""
        self.health_points -= 1
        if self.health_points == 0:
            raise GameOver(self.name, self.score)

    def select_attack(self):
        """Enemy attack"""
        while True:
            user_attack = str(input("Enter your choose to attack: Warrior, Wizard, Robber: \n")).strip().lower()
            if user_attack in HEROES:
                return user_attack

    def select_defence(self):
        while True:
            user_defence = str(input("Enter your choose to defence: Warrior, Wizard, Robber: \n")).strip().lower()
            if user_defence in HEROES:
                return user_defence

    @staticmethod
    def fight(player, enemy):
        if player == enemy:
            return "draw"
        elif player == "warrior" and enemy == "robber":
            return 'win'
        elif player == "robber" and enemy == "wizard":
            return 'win'
        elif player == "wizard" and enemy == "warrior":
            return 'win'
        else:
            return 'lose'

    def attack(self, enemy: Enemy):
        # attack = enemy.select_attack()
        attack = self.select_attack()
        defense = enemy.select_defence()
        battle = self.fight(attack, defense)

        if battle == 'draw':
            print("It's a draw!")
        elif battle == 'win':
            try:
                enemy.decrease_health()
                self.score += 1
                print(f"'Your attack is successful! +1 point {self.score = }")
            except EnemyDown:
                self.score += 2
                raise

        else:
            print('Your attack is failed')


    def defence(self, enemy: Enemy):

        defence = self.select_defence()
        attack = enemy.select_attack()
        battle = self.fight(defence, attack)

        if battle == 'draw':
            print("It's a draw defence")
        elif battle == 'win':
            print('You defense is SUCCESSFUL')
        else:
            self.decrease_health()
            print(f'Your defences have been breached. You have left {self.health_points}')
