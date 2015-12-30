from components.player_info import PlayerInfo
from components.position import Position
import game_config


class SnakeHelpers(object):
    def __init__(self, engine, creator):
        self._engine = engine
        self._entity_creator = creator

    def shorten_snake(self, player_info, desired_length):
        snake = player_info.snake
        for i in range(0,desired_length-1):
            if len(snake) > desired_length:
                self._engine.remove_entity(snake[desired_length-1])
                del snake[desired_length-1]
        if len(snake) < game_config.snake_minimal_length:
            self.kill_snake(player_info)

    def extend_snake(self, player_info, desired_length):
        snake = player_info.snake
        tail_pos = snake[-1].get(Position)
        for i in range(0, desired_length - len(snake)):
            segment = self._entity_creator.create_snake_segment(tail_pos.x, tail_pos.y, 0, False, False)
            snake.insert(-1, segment)

    def kill_snake(self, player_info_component):
        player_info_component.state = PlayerInfo.State.DEAD
        for s in player_info_component.snake:
            self._engine.remove_entity(s)
        player_info_component.snake = []
