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
            print('Game state received!')

        self._update_engine_data(unpickled)

    def end(self):
        pass

    def _update_engine_data(self, data):
        # update engine data
        pass

