import random
from components.player_info import PlayerInfo
from components.position import Position
from components.tile_map import TileMap
from engine.system import System
import game_config


class PowerUpSpawnSystem(System):

    def __init__(self, engine, entity_creator, creating_interval=3000):
        self._engine = engine
        self._entity_creator = entity_creator
        self._elapsed_time = 0
        self._creating_interval = creating_interval
        self._power_up_types = [(apple_effect, 2),
                                (wormy_apple_effect, 15)]

    def start(self):
        pass

    def end(self):
        pass

    def update(self, delta_time):
        tiles = self._engine.get_entity_by_group('tile_map')[0].get(TileMap)
        players = self._engine.get_entity_by_group('player')

        self._elapsed_time += delta_time
        if self._elapsed_time >= self._creating_interval:
            for i, (effect, uniqueness) in enumerate(self._power_up_types):
                if random.randint(0,uniqueness) == 0:
                    x, y = self._get_free_position(tiles, players)
                    x *= game_config.tile_size
                    y *= game_config.tile_size
                    self._entity_creator.create_power_up(x, y, i, effect)
                    self._elapsed_time -= self._creating_interval

    def _get_free_position(self, tiles, players):
        x, y = 0, 0
        while True:
            x, y = tiles.random_position(TileMap.Tile.EMPTY)
            if not self._position_on_players(x, y, players):
                break

        return x, y

    def _position_on_players(self, x, y, players):
        for player in players:
            if self._position_on_player(x, y, player):
                return True

        return False

    def _position_on_player(self, x, y, player):
        snake = player.get(PlayerInfo).snake

        for segment in snake:
            pos = segment.get(Position)
            if pos.x == x * game_config.tile_size and pos.y == y * game_config.tile_size:
                return True

        return False


def wormy_apple_effect(engine, player_info_component):
    tail = player_info_component.snake[-1]
    tail_pos = tail.get(Position)
    tail_pos.set(player_info_component.snake[-2].get(Position))
    engine.remove_entity(player_info_component.snake[-2])
    del player_info_component.snake[-2]


def apple_effect(entity_creator, player_info_component):
    tail = player_info_component.snake[-1]
    tail_pos = tail.get(Position)
    segment = entity_creator.create_snake_segment(tail_pos.x, tail_pos.y, 0, False, False)
    player_info_component.snake.insert(-1, segment)

