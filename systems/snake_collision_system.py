from components.position import Position
from components.power_up import PowerUp
from components.tile_map import TileMap
from components.player import Player
from engine.system import System
import game_config


class SnakeCollisionSystem(System):
    def __init__(self, engine):
        self._engine = engine

    def start(self):
        pass

    def update(self, time):
        map = self._engine.get_entity_by_group("tile_map")[0].get(TileMap)
        players = self._engine.get_entity_by_group("player")
        power_ups = self._engine.get_entity_by_group("power_up")

        for p in players:
            player_component = p.get(Player)
            snake = player_component.snake
            self.check_collision_with_walls(snake, map)
            self.check_collision_with_powerup(player_component, power_ups)

    def check_collision_with_powerup(self, player_component, powerups):
        snake = player_component.snake
        for power_up in powerups:
            snake_pos = snake[0].get(Position)
            power_up_pos = power_up.get(Position)

            if snake_pos.x == power_up_pos.x and snake_pos.y == power_up_pos.y:
                power_up.get(PowerUp).effect(player_component)
                self._engine.remove_entity(power_up)

    def check_collision_with_walls(self, snake, map):
        head_x_tile = int(snake[0].get(Position).x / game_config.tile_size)
        head_y_tile = int(snake[0].get(Position).y / game_config.tile_size)

        if map.tiles[head_y_tile][head_x_tile] == TileMap.Tile.WALL:
            print("Collision")

    def end(self):
        pass