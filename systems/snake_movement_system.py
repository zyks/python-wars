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

            if info.is_head and self._elapsed_time > self._wait_interval:
                before_tail = None
                tail = None
                for e in entities:
                    e_next = e.get(SnakeInfo).next_segment
                    if e_next is not None:
                        e_next_info = e_next.get(SnakeInfo)
                        if e_next_info.player == info.player and e_next_info.is_tail:
                            before_tail = e
                            tail = e_next
                            break

                head_pos = entity.get(Position)
                head_mot = entity.get(Motion)
                tail_pos = tail.get(Position)
                bef_tail_pos = before_tail.get(Position)
                bef_tail_info = before_tail.get(SnakeInfo)

                tail_pos.x = bef_tail_pos.x
                tail_pos.y = bef_tail_pos.y
                bef_tail_pos.x = head_pos.x
                bef_tail_pos.y = head_pos.y
                head_pos.x = head_pos.x + head_mot.x_velocity
                head_pos.y = head_pos.y + head_mot.y_velocity

                if head_pos.x < 0:
                    head_pos.x += game_config.screen_size[0]
                if head_pos.x >= game_config.screen_size[0]:
                    head_pos.x -= game_config.screen_size[0]

                if head_pos.y < 0:
                    head_pos.y += game_config.screen_size[1]
                if head_pos.y >= game_config.screen_size[1]:
                    head_pos.y -= game_config.screen_size[1]

                bef_tail_info.next_segment = info.next_segment
                for e in entities:
                    e_info = e.get(SnakeInfo)
                    if e_info.player == info.player and e_info.next_segment == before_tail:
                        e_info.next_segment = tail
                        break
                info.next_segment = before_tail

                self._elapsed_time -= self._wait_interval

    def end(self):
        pass

