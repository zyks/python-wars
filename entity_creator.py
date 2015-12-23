from components.tile_map import TileMap
from engine.entity import Entity
from components.graphics import Graphics
from components.position import Position
from components.snake_info import SnakeInfo


class EntityCreator(object):

    def __init__(self, engine):
        self._engine = engine

    def create_snake(self, player, head_image, body_image):
        start_x = 300
        start_y = 300
        # create snake head
        next_s = self.create_snake_segment(head_image, start_x, start_y, 0, player, True, False, None)

        for i in range(1, 4):
            current = self.create_snake_segment(body_image, start_x + i * 32, start_y, 0, player, False, False, next_s)
            next_s = current

        # create snake tail
        self.create_snake_segment(body_image, start_x + 4 * 32, start_y, 0, player, False, True, next_s)

    def create_snake_segment(self, image, x, y, rotation, player, is_head, is_tail, next_s):
        entity = Entity()
        entity.add(Graphics(image, x, y))
        entity.add(Position(x, y, rotation))
        entity.add(SnakeInfo(player, is_head, is_tail, next_s))
        self._engine.add_entity(entity)
        return entity

    def create_map(self, file):
        tile_map = TileMap()
        tile_map.load_from_file(file)
        entity = Entity([tile_map])
        self._engine.add_entity(entity)

