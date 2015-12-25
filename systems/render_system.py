from engine.system import System
from engine.engine import Engine
from components.graphics import Graphics
from components.position import Position


class RenderSystem(System):

    def __init__(self, engine, background):
        self._engine = engine
        self._background = background

    def start(self):
        pass

    def update(self, time):
        for entity in self._engine.get_entity_by_group('render'):
            graphics = entity.get(Graphics)
            entity_position = entity.get(Position)
            image_position = graphics.image.get_rect()
            image_position.x = entity_position.x
            image_position.y = entity_position.y
            atlas_area = (graphics.x, graphics.y,
                          graphics.width, graphics.height)
            self._background.blit(graphics.image, image_position, atlas_area)

    def end(self):
        pass

