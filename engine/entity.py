from engine.exceptions import NonexistentComponent


class Entity(object):
    def __init__(self, components=[]):
        self.components = {}
        self.add(components)

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