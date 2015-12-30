from components.motion import Motion
from components.player_info import PlayerInfo
from components.position import Position
from engine.system import System
import game_config


class SnakeMovementSystem(System):

    def __init__(self, engine, wait_interval):
        self._engine = engine
        self._wait_interval = wait_interval
        self._elapsed_time = 0

    def start(self):
        pass

    def update(self, time):
        self._elapsed_time += time
        if self._elapsed_time < self._wait_interval:
            return

        players = self._engine.get_entity_by_group('player')

        for player in players:
            if not player.get(PlayerInfo).alive:
                continue

            snake = player.get(PlayerInfo).snake
            motion = player.get(Motion)
            old_position = Position()
            new_position = Position()
            head_position = snake[0].get(Position)
            new_position.set(head_position)
            new_position.move(motion, 1)
            motion.changes_blocked = False

            for segment in snake:
                segment_position = segment.get(Position)
                old_position.set(segment_position)
                segment_position.set(new_position)
                self._wrap_position(segment_position)
                new_position.set(old_position)

        self._elapsed_time -= self._wait_interval

    def end(self):
        pass

    def _wrap_position(self, position):
        if position.x < 0:
            position.x += game_config.screen_size[0]
        if position.x >= game_config.screen_size[0]:
            position.x -= game_config.screen_size[0]

        if position.y < 0:
            position.y += game_config.screen_size[1]
        if position.y >= game_config.screen_size[1]:
            position.y -= game_config.screen_size[1]

