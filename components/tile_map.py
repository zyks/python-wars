from enum import Enum
import random
import game_config


class TileMap(object):
    class Tile(Enum):
            EMPTY = 0
            WALL = 1

    class Spawn:
        def __init__(self, pos, dir):
            self.initial_position = pos
            self.initial_direction = dir

    def __init__(self):
        self.spawns = []
        self.tiles = []
        self.width = 0
        self.height = 0
        self._char_to_tile = {
            'X': TileMap.Tile.WALL
        }

    def load_from_file(self, file_name):
        with open(file_name) as f:
            for i, line in enumerate(f):
                line = line.rstrip("\r\n")
                self.tiles.append([self.char_to_tile(c) for c in line])
                self.spawns += [self.char_to_spawn(c, j, i) for j, c in enumerate(line) if c in ['>', '^', '<', 'V']]

        self.height = len(self.tiles)
        if self.height > 0:
            self.width = len(self.tiles[0])

    def char_to_tile(self, c):
        return self._char_to_tile.get(c, TileMap.Tile.EMPTY)

    def char_to_spawn(self, c, column, row):
        pos = (column * game_config.tile_size, row * game_config.tile_size)
        if c == '>':
            return TileMap.Spawn(pos, (game_config.tile_size, 0))
        if c == '<':
            return TileMap.Spawn(pos, ((-1) * game_config.tile_size, 0))
        if c == '^':
            return TileMap.Spawn(pos, (0, (-1) * game_config.tile_size))
        if c == 'V':
            return TileMap.Spawn(pos, (0, game_config.tile_size))

    def random_position(self, required_type=None):
        x, y = 0, 0

        condition = True
        while condition:
            x = random.randint(0, self.width-1)
            y = random.randint(0, self.height-1)
            condition = required_type is not None and self.tiles[y][x] != required_type

        return x, y
