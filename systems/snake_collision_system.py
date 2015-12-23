from components.position import Position
from components.tile_map import TileMap
from components.player import Player
from engine.system import System
import game_config


class SnakeCollisionSystem(System):
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        pass

    def update(self, time):
        map = self._engine.get_entity_by_group("tile_map")[0].get(TileMap)
        players = self._engine.get_entity_by_group("player")

        for p in players:
            snake = p.get(Player).snake
            self.check_collision_with_walls(snake, map)

    def check_collision_with_walls(self, snake, map):
        head_x_tile = int(snake[0].get(Position).x / game_config.tile_size)
        head_y_tile = int(snake[0].get(Position).y / game_config.tile_size)

        if map.tiles[head_y_tile][head_x_tile] == TileMap.Tile.WALL:
            print("Collision")

    def end(self):
        pass