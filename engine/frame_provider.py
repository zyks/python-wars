class FrameProvider(object):
    def __init__(self, time_provider):
        self._clock = 0.0
        self._delta = 0.0
        self._actions = []
        self._time_provider = time_provider
        self._working = False

    def add_action(self, action):
        if hasattr(action, '__call__'):
            self._actions.append(action)

    def start(self):
        self._working = True
        self._clock = self._time_provider()
        while self._working:
            self._delta = (self._time_provider() - self._clock) * 1000
            self._clock = self._time_provider()

            for action in self._actions:
                action(self._delta)

    def stop(self):
        self._working = False

