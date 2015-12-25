from enum import Enum
import random


class TileMap(object):
    class Tile(Enum):
            EMPTY = 0
            WALL = 1

    def __init__(self):
        self.tiles = []
        self.width = 0
        self.height = 0
        self._char_to_tile = {
            'X': TileMap.Tile.WALL
        }

    def load_from_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                self.tiles.append([self.char_to_tile(c) for c in line.rstrip("\r\n")])
        self.height = len(self.tiles)
        if self.height > 0:
            self.width = len(self.tiles[0])

    def char_to_tile(self, c):
        return self._char_to_tile.get(c, TileMap.Tile.EMPTY)

    def random_position(self, required_type=None):
        x, y = 0, 0

        condition = True
        while condition:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            condition = required_type is not None and self.tiles[y][x] != required_type

        return x, y
