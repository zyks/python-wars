from components.position import Position
from components.effect import Effect
from components.tile_map import TileMap
from components.player_info import PlayerInfo
from engine.system import System
import game_config
from snake_helpers import SnakeHelpers


class SnakeCollisionSystem(System):

    def __init__(self, engine, entity_creator):
        self._engine = engine
        self._entity_creator = entity_creator
        self._snake_helper = SnakeHelpers(self._engine, self._entity_creator)

    def start(self):
        pass

    def update(self, time):
        map = self._engine.get_entity_by_group("tile_map")[0].get(TileMap)
        players = self._engine.get_entity_by_group("player")
        power_ups = self._engine.get_entity_by_group("power_up")

        for player in players:
            player_info_component = player.get(PlayerInfo)
            self.check_collision_with_walls(player_info_component, map)
            self.check_collision_with_powerup(player_info_component, power_ups)
            self.check_collision_with_players(player_info_component, players)

    def check_collision_with_powerup(self, player_info_component, powerups):
        if not player_info_component.alive:
            return

        snake = player_info_component.snake

        for power_up in powerups:
            snake_pos = snake[0].get(Position)
            power_up_pos = power_up.get(Position)

            if snake_pos.x == power_up_pos.x and snake_pos.y == power_up_pos.y:
                effect = power_up.get(Effect).effect

                if effect.__name__ == 'apple_effect':
                    effect(self._entity_creator, player_info_component)
                elif effect.__name__ == 'wormy_apple_effect':
                    effect(self._engine, player_info_component)

                self._engine.remove_entity(power_up)

    def check_collision_with_walls(self, player_info_component, map):
        if not player_info_component.alive:
            return

        snake = player_info_component.snake
        head_x_tile = int(snake[0].get(Position).x / game_config.tile_size)
        head_y_tile = int(snake[0].get(Position).y / game_config.tile_size)

        if map.tiles[head_y_tile][head_x_tile] == TileMap.Tile.WALL:
            self._snake_helper.kill_snake(player_info_component)

    def check_collision_with_players(self, player_info_component, players):
        if not player_info_component.alive:
            return

        snake = player_info_component.snake
        head_pos = snake[0].get(Position)

        for player in players:
            player_snake = player.get(PlayerInfo).snake
            player_number = player.get(PlayerInfo).number

            for i in range(0, len(player_snake)):
                if player_number == player_info_component.number and i == 0:
                    continue

                segment_position = player_snake[i].get(Position)
                if head_pos.x == segment_position.x and head_pos.y == segment_position.y:
                    eaten = len(player_snake) - (i + 1)
                    if eaten < len(player_info_component.snake):
                        self._snake_helper.shorten_snake(player.get(PlayerInfo), i + 1)
                        self._snake_helper.extend_snake(player_info_component, len(snake) + eaten)
                    else:
                        self._snake_helper.kill_snake(player_info_component)

                    break

    def end(self):
        pass

