from engine.entity import Entity


class MatchingComponentsEntityGroup(object):
    def __init__(self):
        self.registered_groups = {}
        self.groups = {}

    def add(self, name, group):
        if name not in self.registered_groups:
            self.registered_groups[name] = group

    def remove(self, name):
        if name in self.registered_groups:
            del self.registered_groups[name]

    def get(self, name):
        return self.groups[name]

    def on_entity_registered(self, entity):
        for name in self.registered_groups:
            if self.match_group(entity, name):
                self.add_to_group(entity, name)

    def match_group(self, entity, group):
        for _, component in entity.components.items():
            if not isinstance(component, tuple(self.registered_groups[group])):
                return False

        return True

    def add_to_group(self, entity, group):
        if group in self.groups:
            self.groups[group].append(entity)
        else:
            self.groups[group] = [entity]