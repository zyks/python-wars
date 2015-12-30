from enum import Enum


class PlayerInfo(object):

    def __init__(self, number, address):
        self.snake = []
        self.number = number
        self.address = address
        self.alive = True
        self.won = False
        # self.host = host
        # self.port = port
