from enum import Enum


class TileMap(object):
    class Tile(Enum):
            EMPTY = 0
            WALL = 1

    def __init__(self):
        self.tiles = []
        self._char_to_tile = {
            'X': TileMap.Tile.WALL
        }

    def load_from_file(self, file_name):
        with open(file_name) as f:
            for line in f:
                self.tiles.append([self.char_to_tile(c) for c in line.rstrip("\r\n")])

    def char_to_tile(self, c):
        return self._char_to_tile.get(c, TileMap.Tile.EMPTY)
