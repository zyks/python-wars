import sys

import pygame
from pygame.constants import *

from components.graphics import Graphics
from components.motion import Motion
from components.position import Position
from components.tile_map import TileMap
from components.snake_info import SnakeInfo
from components.power_up import PowerUp
from components.player import Player
import game_config
from engine.engine import Engine
from engine.frame_provider import FrameProvider
from entity_creator import EntityCreator
from systems.power_up_spawn_system import PowerUpSpawnSystem
from systems.render_system import RenderSystem
from systems.snake_collision_system import SnakeCollisionSystem
from systems.snake_control_system import SnakeControlSystem
from systems.tile_map_render_system import TileMapRenderSystem
from systems.snake_movement_system import SnakeMovementSystem


class PythonWars(object):

    def __init__(self):
        pygame.init()
        pygame.display.set_caption(game_config.title)

        self.load_sprites()

        self.engine = Engine()
        self.creator = EntityCreator(self.engine, self.sprites)
        self.screen = pygame.display.set_mode(game_config.screen_size)
        self.frame_provider = FrameProvider(pygame.time.get_ticks)

        self.init_engine()

    def load_sprites(self):
        self.sprites = {'tile_atlas': pygame.image.load('assets/tiles.jpg'),
                        'power_up_atlas': pygame.image.load('assets/power_ups.jpg'),
                        'snake_head': pygame.image.load('assets/head.jpg'),
                        'snake_body': pygame.image.load('assets/body.jpg'),
                        'snake_tail': pygame.image.load('assets/tail.jpg')}

    def init_engine(self):
        self.engine._entity_components_packer.add('render', [Graphics, Position])
        self.engine._entity_components_packer.add('snake-movement', [Position, Motion, SnakeInfo])
        self.engine._entity_components_packer.add('snake-control', [Motion, SnakeInfo])
        self.engine._entity_components_packer.add('tile_map', [TileMap])
        self.engine._entity_components_packer.add('player', [Player])
        self.engine._entity_components_packer.add('power_up', [Position, PowerUp])

        self.engine.add_system(SnakeCollisionSystem(self.engine), 0)
        self.engine.add_system(PowerUpSpawnSystem(self.engine, self.creator), 0)
        self.engine.add_system(TileMapRenderSystem(self.engine, self.screen, self.sprites['tile_atlas']), 2)
        self.engine.add_system(RenderSystem(self.engine, self.screen), 1)
        self.engine.add_system(SnakeMovementSystem(self.engine, 200), 2)
        self.engine.add_system(SnakeControlSystem(self.engine), 3)

        snake = self.creator.create_snake(1)
        self.creator.create_player(snake)
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

