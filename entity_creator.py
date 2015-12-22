from engine.entity import Entity
from components.graphics import Graphics
from components.position import Position
from components.snake_info import SnakeInfo


class EntityCreator(object):

    def __init__(self, engine):
        self._engine = engine

    def create_snake(self, player):
        # create snake head
        next_s = self.create_snake_segment('head-img', 0, 0, 0, player, True, False, None)

        for _ in range (0, 3):
            current = self.create_snake_segment('body-img', 0, 0, 0, player, False, False, next_s)
            next_s = current

        # create snake tail
        self.create_snake_segment('tail-img', 0, 0, 0, player, False, True, next_s)

    def create_snake_segment(self, image, x, y, rotation, player, is_head, is_tail, next_s):
        entity = Entity()
        entity.add(Graphics(image, x, y))
        entity.add(Position(x, y, rotation))
        entity.add(SnakeInfo(player, is_head, is_tail, next_s))
        self._engine.add_entity(entity)
        return entity

