class Entity(object):
    def __init__(self):
        self.components = {}

    def add(self, components):
        if not isinstance(components, list):
            components = [components]

        for c in components:
            if type(c) not in self.components:
                self.components[type(c)] = c

    def remove(self, component):
        component_type = type(component)

        if component_type in self.components:
            del self.components[component]

    def get(self, component):
        return self.components[type(component)]