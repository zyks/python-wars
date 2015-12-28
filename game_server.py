import pygame

from components.graphics import Graphics
from components.motion import Motion
from components.position import Position
from components.tile_map import TileMap
from components.effect import Effect
from components.player_info import PlayerInfo
from engine.frame_provider import FrameProvider
import game_config
from engine.engine import Engine
from entity_creator import EntityCreator
from systems.power_up_spawn_system import PowerUpSpawnSystem
from systems.receive_direction_data_system import ReceiveDirectionDataSystem
from systems.send_game_state_system import SendGameStateSystem
from systems.snake_collision_system import SnakeCollisionSystem
from systems.snake_movement_system import SnakeMovementSystem


class GameServer(object):

    def __init__(self):
        self._engine = Engine()
        self._creator = EntityCreator(self._engine)
        self._frame_provider = FrameProvider(pygame.time.get_ticks)

        self.init_components()
        self.init_systems()
        self.init_gameplay()

    def init_components(self):
        self._engine._entity_components_packer.add('render', [Graphics, Position])
        self._engine._entity_components_packer.add('tile_map', [TileMap])
        self._engine._entity_components_packer.add('player', [PlayerInfo, Motion])
        self._engine._entity_components_packer.add('power_up', [Position, Effect])

    def init_systems(self):
        self._engine.add_system(SnakeCollisionSystem(self._engine, self._creator), 0)
        self._engine.add_system(PowerUpSpawnSystem(self._engine, self._creator), 0)
        self._engine.add_system(SnakeMovementSystem(self._engine, 200), 2)
        self._engine.add_system(ReceiveDirectionDataSystem(self._engine, 8082), 1)
        self._engine.add_system(SendGameStateSystem(self._engine), 2)

    def init_gameplay(self):
        self._creator.create_map("assets/maps/0.txt")
        snake = self._creator.create_snake()
        self._creator.create_player(snake, 1, True, 'localhost', 8084, "player1")

    def run(self):
        self._frame_provider.add_action(self._engine.update)
        self._frame_provider.start()