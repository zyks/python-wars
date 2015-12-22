class FrameProvider(object):
    def __init__(self, time_provider):
        self._clock = 0.0
        self._delta = 0.0
        self._actions = []
        self._time_provider = time_provider

    def add_action(self, action):
        if hasattr(action, '__call__'):
            self._actions.append(action)

    def start(self):
        self._clock = self._time_provider()

        while True:
            self._delta = self._time_provider() - self._clock
            self._clock = self._time_provider()

            for action in self._actions:
                action(self._delta)
