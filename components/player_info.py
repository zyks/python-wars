from enum import Enum


class PlayerInfo(object):

    def __init__(self, number, address, name):
        self.snake = []
        self.number = number
        self.name = name
        self.address = address
        self.alive = True
        self.won = False
        # self.host = host
        # self.port = port
