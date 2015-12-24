from components.motion import Motion
from components.position import Position
from components.snake_info import SnakeInfo
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
        entities = self._engine.get_entity_by_group('snake-movement')

        for entity in entities:
            info = entity.get(SnakeInfo)

            if not info.is_head or self._elapsed_time < self._wait_interval:
                continue

            tail = self._find_segment_pointing_at(entities, None)
            b_tail = self._find_segment_pointing_at(entities, tail)
            bb_tail = self._find_segment_pointing_at(entities, b_tail)

            head_pos = entity.get(Position)
            head_mot = entity.get(Motion)
            tail_pos = tail.get(Position)
            bef_tail_pos = b_tail.get(Position)
            bef_tail_info = b_tail.get(SnakeInfo)

            tail_pos.set(bef_tail_pos)
            bef_tail_pos.set(head_pos)
            head_pos.x = head_pos.x + head_mot.x_velocity
            head_pos.y = head_pos.y + head_mot.y_velocity
            head_mot.changes_blocked = False

            self._wrap_position(head_pos)

            bef_tail_info.next_segment = info.next_segment
            bb_tail.get(SnakeInfo).next_segment = tail
            info.next_segment = b_tail

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

    def _find_segment_pointing_at(self, entities, target):
        for e in entities:
            e_info = e.get(SnakeInfo)
            if e_info.next_segment == target:
                return e

        return None

