from enum import Enum
import random
import sys
import threading
from game_client import GameClient
from game_server import GameServer


class PythonWars(object):

    def __init__(self, client_mode=False, server_mode=False):
        self._client_mode = client_mode
        self._server_mode = server_mode

        if self._server_mode:
            self._server = GameServer()
            # self._server_thread = threading.Thread(target=self._server.run)
        elif self._client_mode:
            self._client = GameClient(int(sys.argv[2]))

    def run(self):
        if self._server_mode:
            self._server.run()
            self._server._frame_provider.stop()
            # self._server_thread.start()

        elif self._client_mode:
            self._client.run()

        # self._server._frame_provider.stop()
        # self._server_thread.join()

server_mode = False
client_mode = False
for arg in sys.argv:
    if arg == "--server":
        server_mode = True
    elif arg == "--client":
        client_mode = True

g = PythonWars(client_mode, server_mode)
g.run()
