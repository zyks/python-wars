import argparse
import sys
import threading
from game_client import GameClient
from game_server import GameServer


class PythonWars(object):

    def __init__(self, arguments):
        self._arguments = arguments

        if self._arguments.mode == "server":
            self._server = GameServer(self._arguments.players)
            # self._server_thread = threading.Thread(target=self._server.run)
        elif self._arguments.mode == "client":
            self._client = GameClient(self._arguments.port, self._arguments.name)

    def run(self):
        if self._arguments.mode == "server":
            self._server.run()
            self._server._frame_provider.stop()
            # self._server_thread.start()

        if self._arguments.mode == "client":
            self._client.run()

        # self._server._frame_provider.stop()
        # self._server_thread.join()


parser = argparse.ArgumentParser()
parser.add_argument("mode", help="specify in which mode game should be run", choices=["client", "server"])
parser.add_argument("--port", type=int, default=40000, help="specify player port")
parser.add_argument("-p", "--players", type=int, default=2, help="how many players will be in game")
parser.add_argument("-n", "--name", default="unknown_player", help="specify player's name")

PythonWars(parser.parse_args()).run()
