class NonexistentComponent(Exception):
    def __init__(self, entity, component):
        self.entity = entity
        self.component = component

    def __str__(self):
        return "Nonexistent component: `{0}' for entity: `{1}'".format(
            self.component, self.entity)