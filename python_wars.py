import pygame
import sys
from components.graphics import Graphics
from components.position import Position
from components.tile_map import TileMap
import game_config
from pygame.constants import *
from engine.engine import Engine
from engine.frame_provider import FrameProvider
from entity_creator import EntityCreator
from systems.render_system import RenderSystem
from systems.tile_map_render_system import TileMapRenderSystem


class PythonWars():
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(game_config.title)

        self.engine = Engine()
        self.creator = EntityCreator(self.engine)
        self.screen = pygame.display.set_mode(game_config.screen_size)
        self.frame_provider = FrameProvider(pygame.time.get_ticks)


        self.init_engine()

    def init_engine(self):
        tile_atlas = pygame.image.load('assets/tiles.jpg')
        self.engine._entity_components_packer.add('render', [Graphics, Position])
        self.engine._entity_components_packer.add('tile_map', [TileMap])
        self.render_system = RenderSystem(self.engine, self.screen)
        self.engine.add_system(TileMapRenderSystem(self.engine, self.screen, tile_atlas), 2)
        self.engine.add_system(self.render_system, 1)

        head_image = pygame.image.load('assets/head.jpg')
        body_image = pygame.image.load('assets/body.jpg')
        self.creator.create_snake(1, head_image, body_image)

        self.creator.create_map("assets/maps/0.txt")

        "add system, entities etc."

    def check_quit_condition(self, delta):
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self.frame_provider.add_action(self.engine.update)
        self.frame_provider.add_action(self.check_quit_condition)
        self.frame_provider.start()


g = PythonWars()
g.run()

