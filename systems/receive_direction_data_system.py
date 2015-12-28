from components.motion import Motion
from components.player_info import PlayerInfo
from engine.system import System
import socket
import game_config


class ReceiveDirectionDataSystem(System):

    def __init__(self, engine, port):
        self._engine = engine
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self._socket.bind(('', self._port))
        self._socket.settimeout(0.1)

    def start(self):
        pass

    def update(self, time):
        players = self._engine.get_entity_by_group('player')
        players_number = len(players)

        moves = {}
        for _ in range(0, players_number):
            try:
                data, _ = self._socket.recvfrom(1024)
            except socket.error:
                return
            player_number, move = data.decode().split('-')
            moves[player_number] = move

        if len(moves) != 0:
            self._apply_moves(players, moves)

    def end(self):
        pass

    def _apply_moves(self, players, moves):
        for player_number, move in moves.items():
            for player in players:
                player_info = player.get(PlayerInfo)
                if str(player_info.number) == player_number:
                    self._apply_move(player, move)

    def _apply_move(self, player, move):
        player_motion = player.get(Motion)

        if move == 'UP':
            player_motion.set(0, (-1) * game_config.tile_size)
        elif move == 'DOWN':
            player_motion.set(0, game_config.tile_size)
        elif move == 'LEFT':
            player_motion.set((-1) * game_config.tile_size, 0)
        elif move == 'RIGHT':
            player_motion.set(game_config.tile_size, 0)

