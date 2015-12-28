from components.player_info import PlayerInfo
from engine.system import System
import socket
import pickle


class SendGameStateSystem(System):

    def __init__(self, engine):
        self._engine = engine
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        pass

    def update(self, time):
        players = self._engine.get_entity_by_group('player')
        power_ups = self._engine.get_entity_by_group('power_up')

        data = {'players': players, 'power-ups': power_ups}

        pickled = pickle.dumps(data)

        for player in players:
            player_info = player.get(PlayerInfo)
            self._socket.sendto(pickled, (player_info.host, player_info.port))

    def end(self):
        pass

