from engine.exceptions import NonexistentComponent


class Entity(object):
    next_id = 0

    def __init__(self, components=[], name=""):
        if name == "":
            name = Entity.next_id

        self._name = name
        self.components = {}
        self.add(components)

        Entity.next_id += 1

    def name(self):
        return self._name

    def add(self, components):
        if not isinstance(components, list):
            components = [components]

        for c in components:
            if type(c) not in self.components:
                self.components[type(c)] = c

    def remove(self, component):
        if component in self.components:
            del self.components[component]

    def get(self, component):
        if component not in self.components:
            raise NonexistentComponent(self, component)

        return self.components[component]