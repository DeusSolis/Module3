class EnemyDown(Exception):
    """When the enremy is down"""

    def __str__(self):
        return 'Congratulations you win'


class GameOver(Exception):
    """When game is over"""

    def __str__(self):
        return 'Game over'
