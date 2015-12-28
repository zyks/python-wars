from engine.system import System
from engine.engine import Engine
from components.graphics import Graphics
from components.position import Position


class RenderSystem(System):

    def __init__(self, engine, background, sprites):
        self._engine = engine
        self._background = background
        self._sprites = sprites

    def start(self):
        pass

    def update(self, time):
        for entity in self._engine.get_entity_by_group('render'):
            graphics = entity.get(Graphics)
            entity_position = entity.get(Position)
            image = self._sprites[graphics.image_name]
            image_position = image.get_rect()
            image_position.x = entity_position.x
            image_position.y = entity_position.y

            if graphics.width == 0 or graphics.height == 0:
                graphics.width = image.get_width()
                graphics.height = image.get_height()

            atlas_area = (graphics.x, graphics.y,
                          graphics.width, graphics.height)
            self._background.blit(image, image_position, atlas_area)

    def end(self):
        pass

