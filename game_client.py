import sys

import pygame
from pygame.constants import *

from components.graphics import Graphics
from components.motion import Motion
from components.position import Position
from components.tile_map import TileMap
from components.effect import Effect
from components.player_info import PlayerInfo
from entity_creator import EntityCreator
import game_config
from engine.engine import Engine
from engine.frame_provider import FrameProvider
from systems.receive_game_state_system import ReceiveGameStateSystem
from systems.render_system import RenderSystem
from systems.send_direction_data_system import SendDirectionDataSystem
from systems.snake_control_system import SnakeControlSystem
from systems.tile_map_render_system import TileMapRenderSystem


class GameClient(object):

    def __init__(self, client_port):
        self._client_port = client_port
        pygame.init()
        pygame.display.set_caption(game_config.title)

        self.load_sprites()

        self._engine = Engine()
        self._frame_provider = FrameProvider(pygame.time.get_ticks)
        self._creator = EntityCreator(self._engine)
        self._screen = pygame.display.set_mode(game_config.screen_size)

        self.init_components()
        self.init_systems()
        self.init_gameplay()

    def load_sprites(self):
        self.sprites = {'tile_atlas': pygame.image.load('assets/tiles.jpg'),
                        'power_up_atlas': pygame.image.load('assets/power_ups.png'),
                        'snake_head': pygame.image.load('assets/head.jpg'),
                        'snake_body': pygame.image.load('assets/body.jpg'),
                        'snake_tail': pygame.image.load('assets/tail.jpg')}

    def init_components(self):
        self._engine._entity_components_packer.add('render', [Graphics, Position])
        self._engine._entity_components_packer.add('tile_map', [TileMap])
        self._engine._entity_components_packer.add('player', [PlayerInfo, Motion])
        self._engine._entity_components_packer.add('power_up', [Position, Effect])

    def init_systems(self):
        self._engine.add_system(TileMapRenderSystem(self._engine, self._screen, self.sprites['tile_atlas']), 2)
        self._engine.add_system(RenderSystem(self._engine, self._screen, self.sprites), 1)
        self._engine.add_system(SnakeControlSystem(self._engine), 3)
        self._engine.add_system(SendDirectionDataSystem(self._engine, 'localhost', 8082), 2)
        self._engine.add_system(ReceiveGameStateSystem(self._engine, self._client_port), 1)

    def init_gameplay(self):
        self._creator.create_map("assets/maps/0.txt", "map")

    def check_quit_condition(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def run(self):
        self._frame_provider.add_action(self._engine.update)
        self._frame_provider.add_action(lambda _: self.check_quit_condition())
        self._frame_provider.add_action(lambda _: pygame.display.update())

        self._frame_provider.start()