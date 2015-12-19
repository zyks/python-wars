class NonexistentComponent(Exception):
    def __init__(self, entity, component):
        self.entity = entity
        self.component = component

    def __str__(self):
        return "Nonexistent component: `{0}' for entity: `{1}'".format(
            self.component, self.entity)


class NonexistentEntityGroup(Exception):
    def __init__(self, group_name):
        self.group_name = group_name

    def __str__(self):
        return "Nonexistent entity group: `{0}'".format(self.group_name)
