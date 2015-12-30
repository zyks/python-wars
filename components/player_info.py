from enum import Enum


class PlayerInfo(object):
    class State(Enum):
        ALIVE = 0
        DEAD = 1
        WIN = 2

    def __init__(self, number, address):
        self.snake = []
        self.number = number
        self.address = address
        self.state = PlayerInfo.State.ALIVE
        # self.host = host
        # self.port = port
