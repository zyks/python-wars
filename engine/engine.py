class Engine(object):

    def __init__(self):
        self._entity_list = []
        self._system_list = []

    def add_entity(self, entity):
        self._entity_list.append(entity)

    def remove_entity(self, entity):
        if entity in self._entity_list:
            self._entity_list.remove(entity)

    def add_system(self, system, priority):
        index = 0
        for _, p in self._system_list:
            if p < priority:
                index += 1
        self._system_list.insert(index, (system, priority))
        system.start()

    def remove_system(self, system):
        system.end()
        for s, p in self._system_list:
            if s == system:
                self._system_list.remove((s, p))

    def update(self, time):
        for system, _ in self._system_list:
            system.update(time)

