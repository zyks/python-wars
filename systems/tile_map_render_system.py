import pygame
from components.tile_map import TileMap
from engine.system import System
import game_config


class TileMapRenderSystem(System):
    def __init__(self, engine, screen, atlas):
        self._engine = engine
        self._screen = screen
        self._atlas = atlas

    def start(self):
        pass

    def update(self, time):
        entities = self._engine.get_entity_by_group("tile_map")
        for e in entities:
            tiles = e.get(TileMap).tiles
            y = 0
            for row in tiles:
                x = 0
                for tile in row:
                    atlas_area = (game_config.tile_size * tile.value, 0,
                                  game_config.tile_size, game_config.tile_size)
                    self._screen.blit(self._atlas, (x, y), atlas_area)
                    x += game_config.tile_size
                y += game_config.tile_size

    def end(self):
        pass
