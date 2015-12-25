import random
from components.position import Position
from components.snake_info import SnakeInfo
from components.tile_map import TileMap
from engine.system import System
import game_config


class PowerUpSpawnSystem(System):
    def __init__(self, engine, entity_creator, creating_interval=3000):
        self._engine = engine
        self._entity_creator = entity_creator
        self._elapsed_time = 0
        self._creating_interval = creating_interval
        self._power_up_types = [(self.apple_effect, 2),
                                (self.wormy_apple_effect, 15)]

    def start(self):
        pass

    def end(self):
        pass

    def update(self, delta_time):
        tiles = self._engine.get_entity_by_group("tile_map")[0].get(TileMap)

        self._elapsed_time += delta_time
        if self._elapsed_time >= self._creating_interval:
            for i, (effect, uniqueness) in enumerate(self._power_up_types):
                if random.randint(0,uniqueness) == 0:
                    x, y = tiles.random_position(TileMap.Tile.EMPTY)
                    x *= game_config.tile_size
                    y *= game_config.tile_size
                    self._entity_creator.create_power_up(x, y, i, effect)
                    self._elapsed_time -= self._creating_interval

    def wormy_apple_effect(self, player_component):
        tail = player_component.snake[-1]
        tail_pos = tail.get(Position)
        tail_pos.set(player_component.snake[-2].get(Position))
        self._engine.remove_entity(player_component.snake[-2])
        del player_component.snake[-2]
        player_component.snake[-2].get(SnakeInfo).next_segment = tail

    def apple_effect(self, player_component):
        tail = player_component.snake[-1]
        tail_pos = tail.get(Position)
        tail_info = tail.get(SnakeInfo)
        segment = self._entity_creator.create_snake_segment(tail_pos.x, tail_pos.y, 0, tail_info.player, False, False, tail)
        player_component.snake[-2].get(SnakeInfo).next_segment = segment
        player_component.snake.insert(-1, segment)
