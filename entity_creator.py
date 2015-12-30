from components.tile_map import TileMap
from components.motion import Motion
from engine.entity import Entity
from components.graphics import Graphics
from components.position import Position
from components.player_info import PlayerInfo
from components.effect import Effect
import game_config


class EntityCreator(object):

    def __init__(self, engine):
        self._engine = engine

    def create_player(self, number, address, name=""):
        spawns = self._engine.get_entity_by_name("map").get(TileMap).spawns

        player_info_component = PlayerInfo(number, address)
        player_info_component.snake = self.create_snake(spawns[number-1])
        motion_component = Motion(*spawns[number-1].initial_direction)
        player = Entity([player_info_component, motion_component], name)
        self._engine.add_entity(player)

    def create_snake(self, spawn):
        x, y = spawn.initial_position
        step_x, step_y = spawn.initial_direction

        # create snake tail
        snake = [self.create_snake_segment(x, y, 0, False, True)]

        for i in range(1, 4):
            current = self.create_snake_segment(x + i * step_x, y + i * step_y, 0, False, False)
            snake = [current] + snake

        # create snake head
        snake = [(self.create_snake_segment(x + 4 * step_x, y + 4 * step_y, 0, True, False))] + snake
        return snake

    def create_snake_segment(self, x, y, rotation, is_head, is_tail):
        image = 'snake_body'
        if is_head:
            image = 'snake_head'
        if is_tail:
            image = 'snake_tail'

        entity = Entity()
        entity.add(Graphics(image, 0, 0))
        entity.add(Position(x, y, rotation))
        self._engine.add_entity(entity)
        return entity

    def create_map(self, file, name=""):
        tile_map = TileMap()
        tile_map.load_from_file(file)
        entity = Entity([tile_map], name)
        self._engine.add_entity(entity)

    def create_power_up(self, x, y, type, effect):
        entity = Entity()
        entity.add(Position(x, y, 0))
        entity.add(Graphics('power_up_atlas', type*32, 0, game_config.tile_size, game_config.tile_size))
        entity.add(Effect(effect))

        self._engine.add_entity(entity)

