from components.player_info import PlayerInfo
from engine.system import System
import socket
import pickle


class SendGameStateSystem(System):

    def __init__(self, engine):
        self._engine = engine
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._counter = 0
        self._elapsed_time = 0
        self._sending_interval = 100

    def start(self):
        pass

    def update(self, time):
        self._elapsed_time += time

        if self._elapsed_time >= self._sending_interval:
            self._elapsed_time -= self._sending_interval
            players = self._engine.get_entity_by_group('player')
            power_ups = self._engine.get_entity_by_group('power_up')

            data = {'players': players, 'power-ups': power_ups}

            pickled = pickle.dumps(data)

            for player in players:
                player_info = player.get(PlayerInfo)
                self._socket.sendto(pickled, (player_info.host, player_info.port))

    def end(self):
        pass
