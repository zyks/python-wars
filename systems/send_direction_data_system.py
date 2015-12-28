from components.motion import Motion
from components.player_info import PlayerInfo
from engine.system import System
import socket


class SendDirectionDataSystem(System):

    def __init__(self, engine, host, port):
        self._engine = engine
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def start(self):
        pass

    def update(self, time):
        players = self._engine.get_entity_by_group('player')

        for player in players:
            player_info = player.get(PlayerInfo)

            if not player_info.is_local:
                continue

            player_motion = player.get(Motion)
            x = player_motion.x_velocity
            y = player_motion.y_velocity
            data = str(player_info.number) + '-'

            if x == 0 and y < 0:
                data += 'UP'
            elif x == 0 and y > 0:
                data += 'DOWN'
            elif x > 0 and y == 0:
                data += 'RIGHT'
            elif x < 0 and y == 0:
                data += 'LEFT'
            else:
                data += 'DIRECTION_ERROR'

            self._socket.sendto(data.encode(), (self._host, self._port))

    def end(self):
        pass

