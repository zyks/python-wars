from engine.matchingComponentsEntityGroup import MatchingComponentsEntityGroup


class Engine(object):

    def __init__(self):
        self._entity_list = []
        self._system_list = []
        self._match_entity_components = MatchingComponentsEntityGroup()

    def add_entity(self, entity):
        self._entity_list.append(entity)
        self._match_entity_components.on_entity_registered(entity)

    def remove_entity(self, entity):
        if entity in self._entity_list:
            self._entity_list.remove(entity)
            self._match_entity_components.on_entity_unregistered(entity)

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

    def get_entity_by_group(self, group):
        return self._match_entity_components.get(group)

