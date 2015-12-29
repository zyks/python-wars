from components.motion import Motion
from components.player_info import PlayerInfo
from engine.system import System
import socket


class SendDirectionDataSystem(System):

    def __init__(self, engine, host, port, client_player_number):
        self._engine = engine
        self._client_player_number = client_player_number
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._elapsed_time = 0
        self._sending_interval = 40

    def start(self):
        pass

    def update(self, time):
        self._elapsed_time += time
        if self._elapsed_time >= self._sending_interval:
            self._elapsed_time -= self._sending_interval
        else:
            return

        players = self._engine.get_entity_by_group('player')

        for player in players:
            player_info = player.get(PlayerInfo)

            if player_info.number != self._client_player_number:
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

