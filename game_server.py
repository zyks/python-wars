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
import socket
from time import time


class GameServer(object):

    def __init__(self, nb_of_players):
        self.nb_of_players = nb_of_players
        self._engine = Engine()
        self._creator = EntityCreator(self._engine)
        # self._frame_provider = FrameProvider(pygame.time.get_ticks)
        self._frame_provider = FrameProvider(time)
        self._registered_players = 0
        self._server_port = 8080

        self.init_components()
        self.init_gameplay()
        self.register_players()
        self.init_systems()

    def init_components(self):
        self._engine._entity_components_packer.add('render', [Graphics, Position])
        self._engine._entity_components_packer.add('tile_map', [TileMap])
        self._engine._entity_components_packer.add('player', [PlayerInfo, Motion])
        self._engine._entity_components_packer.add('power_up', [Position, Effect])

    def init_systems(self):
        self._engine.add_system(SnakeCollisionSystem(self._engine, self._creator), 0)
        self._engine.add_system(PowerUpSpawnSystem(self._engine, self._creator), 0)
        self._engine.add_system(SnakeMovementSystem(self._engine, 200), 2)
        self._engine.add_system(ReceiveDirectionDataSystem(self._engine, self._server_port), 1)
        self._engine.add_system(SendGameStateSystem(self._engine), 2)

    def init_gameplay(self):
        self._creator.create_map("assets/maps/0.txt", "map")

    def run(self):
        self._frame_provider.add_action(self._engine.update)
        print('Engine running!')
        self._frame_provider.start()

    def register_players(self):
        _socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        _socket.bind(('', self._server_port))
        _socket.settimeout(1)

        while self._registered_players < self.nb_of_players:
            print('Waiting for players')

            try:
                data, address = _socket.recvfrom(1024)
            except socket.error:
                continue

            [msg, player_name] = data.decode().split('-')

            if msg == 'register':
                self._registered_players += 1
                player_number = self._registered_players
                print('Registered player ', player_number, ' with address: ', address)
                self._creator.create_player(player_number, address, player_name)

                for _ in range(0, 3):
                    _socket.sendto(('registered-' + str(player_number)).encode(), address)

