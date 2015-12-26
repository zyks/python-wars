from components.motion import Motion
from components.player_info import PlayerInfo
from engine.system import System
import pygame
import game_config


class SnakeControlSystem(System):

    def __init__(self, engine):
        self._engine = engine

    def start(self):
        pass

    def update(self, time):
        players = self._engine.get_entity_by_group('player')

        pressed = pygame.key.get_pressed()

        for player in players:
            player_info = player.get(PlayerInfo)
            if not player_info.is_local:
                continue

            motion = player.get(Motion)
            if motion.changes_blocked:
                continue

            if pressed[pygame.K_UP] and motion.y_velocity == 0:
                motion.y_velocity = (-1) * game_config.tile_size
                motion.x_velocity = 0
                motion.changes_blocked = True

            elif pressed[pygame.K_DOWN] and motion.y_velocity == 0:
                motion.y_velocity = game_config.tile_size
                motion.x_velocity = 0
                motion.changes_blocked = True

            elif pressed[pygame.K_LEFT] and motion.x_velocity == 0:
                motion.x_velocity = (-1) * game_config.tile_size
                motion.y_velocity = 0
                motion.changes_blocked = True

            elif pressed[pygame.K_RIGHT] and motion.x_velocity == 0:
                motion.x_velocity = game_config.tile_size
                motion.y_velocity = 0
                motion.changes_blocked = True

    def end(self):
        pass

