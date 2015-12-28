from components.motion import Motion
from components.player_info import PlayerInfo
from components.tile_map import TileMap
from engine.entity import Entity
from engine.system import System
import socket
import pickle


class ReceiveGameStateSystem(System):

    def __init__(self, engine, port):
        self._engine = engine
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(('', self._port))

    def start(self):
        pass

    def update(self, time):
        data, _ = self._socket.recvfrom(65565)

        unpickled = pickle.loads(data)

        if len(unpickled) != 0:
            self._update_engine_data(unpickled)

    def end(self):
        pass

    def _update_engine_data(self, data):
        map = self._engine.get_entity_by_name("map")
        self._engine.clear()
        self._engine.add_entity(map)

        for p in data['players']:
            self._engine.add_entity(p)
            player_info = p.get(PlayerInfo)
            for s in player_info.snake:
                self._engine.add_entity(s)

        for p in data['power-ups']:
            self._engine.add_entity(p)