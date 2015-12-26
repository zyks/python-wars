from components.tile_map import TileMap
from components.motion import Motion
from engine.entity import Entity
from components.graphics import Graphics
from components.position import Position
from components.player_info import PlayerInfo
from components.power_up import PowerUp
import game_config


class EntityCreator(object):

    def __init__(self, engine, sprites):
        self._engine = engine
        self._sprites = sprites

    def create_player(self, snake, number, is_local):
        player_info_component = PlayerInfo(number, is_local)
        player_info_component.snake = snake
        motion_component = Motion(game_config.tile_size, 0)
        player = Entity([player_info_component, motion_component])
        self._engine.add_entity(player)

    def create_snake(self):
        x = 320
        y = 320
        step = game_config.tile_size

        # create snake tail
        snake = [self.create_snake_segment(x, y, 0, False, True)]

        for i in range(1, 4):
            current = self.create_snake_segment(x + i * step, y, 0, False, False)
            snake = [current] + snake

        # create snake head
        snake = [(self.create_snake_segment(x + 4 * step, y, 0, True, False))] + snake
        return snake

    def create_snake_segment(self, x, y, rotation, is_head, is_tail):
        image = self._sprites['snake_body']
        if is_head:
            image = self._sprites['snake_head']
        if is_tail:
            image = self._sprites['snake_tail']

        entity = Entity()
        entity.add(Graphics(image, 0, 0))
        entity.add(Position(x, y, rotation))
        self._engine.add_entity(entity)
        return entity

    def create_map(self, file):
        tile_map = TileMap()
        tile_map.load_from_file(file)
        entity = Entity([tile_map])
        self._engine.add_entity(entity)

    def create_power_up(self, x, y, type, effect):
        entity = Entity()
        entity.add(Position(x, y, 0))
        entity.add(Graphics(self._sprites['power_up_atlas'], type*32, 0, game_config.tile_size, game_config.tile_size))
        entity.add(PowerUp(effect))

        self._engine.add_entity(entity)

