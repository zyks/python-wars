from components.tile_map import TileMap
from components.motion import Motion
from engine.entity import Entity
from components.graphics import Graphics
from components.position import Position
from components.snake_info import SnakeInfo
import game_config


class EntityCreator(object):

    def __init__(self, engine):
        self._engine = engine

    def create_snake(self, player, head_image, body_image, tail_image):
        x = 320
        y = 320
        step = game_config.tile_size

        # create snake tail
        next_s = self.create_snake_segment(tail_image, x, y, 0, player, False, True, None)

        for i in range(1, 4):
            current = self.create_snake_segment(body_image, x + i * step, y, 0, player, False, False, next_s)
            next_s = current

        # create snake head
        self.create_snake_segment(head_image, x + 4 * step, y, 0, player, True, False, next_s)

    def create_snake_segment(self, image, x, y, rotation, player, is_head, is_tail, next_s):
        entity = Entity()
        entity.add(Graphics(image, x, y))
        entity.add(Position(x, y, rotation))
        entity.add(Motion(game_config.tile_size, 0))
        entity.add(SnakeInfo(player, is_head, is_tail, next_s))
        self._engine.add_entity(entity)
        return entity

    def create_map(self, file):
        tile_map = TileMap()
        tile_map.load_from_file(file)
        entity = Entity([tile_map])
        self._engine.add_entity(entity)

