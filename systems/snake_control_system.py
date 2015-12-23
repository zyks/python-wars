from components.motion import Motion
from components.snake_info import SnakeInfo
from engine.system import System
import pygame
import game_config


class SnakeControlSystem(System):

    def __init__(self, engine):
        self._engine = engine

    def start(self):
        pass

    def update(self, time):
        entities = self._engine.get_entity_by_group('snake-control')

        pressed = pygame.key.get_pressed()

        for entity in entities:
            info = entity.get(SnakeInfo)

            if not info.is_head:
                continue

            motion = entity.get(Motion)

            if pressed[pygame.K_UP] and motion.y_velocity == 0:
                motion.y_velocity = (-1) * game_config.tile_size
                motion.x_velocity = 0

            if pressed[pygame.K_DOWN] and motion.y_velocity == 0:
                motion.y_velocity = game_config.tile_size
                motion.x_velocity = 0

            if pressed[pygame.K_LEFT] and motion.x_velocity == 0:
                motion.x_velocity = (-1) * game_config.tile_size
                motion.y_velocity = 0

            if pressed[pygame.K_RIGHT] and motion.x_velocity == 0:
                motion.x_velocity = game_config.tile_size
                motion.y_velocity = 0

    def end(self):
        pass

