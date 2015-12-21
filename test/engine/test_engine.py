import unittest
from engine.engine import Engine
from engine.entity import Entity
from engine.system import System


class TestEngine(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEngine, self).__init__(*args, **kwargs)
        self.engine = Engine()
        self.engine._match_entity_components.add('test1', [Component1])
        self.entity = Entity()
        self.entity.add(Component1())

    def test_add_system(self):
        system = SystemTest()
        self.engine.add_system(system, 1)
        res = len(self.engine._system_list)
        self.assertEqual(res, 1)

    def test_add_two_systems(self):
        system1 = SystemTest()
        system2 = SystemTest()
        self.engine.add_system(system1, 2)
        self.engine.add_system(system2, 1)
        self.assertEqual(self.engine._system_list[0][0], system2)
        self.assertEqual(self.engine._system_list[1][0], system1)

    def test_remove_systems(self):
        system1 = SystemTest()
        self.engine.add_system(system1, 2)
        self.engine.remove_system(system1)
        res = len(self.engine._system_list)
        self.assertEqual(res, 0)

    def test_add_entity(self):
        self.assertEqual(len(self.engine._entity_list), 0)
        self.engine.add_entity(self.entity)
        self.assertEqual(len(self.engine._entity_list), 1)

    def test_remove_entity(self):
        self.engine.add_entity(self.entity)
        self.assertEqual(len(self.engine._entity_list), 1)
        self.engine.remove_entity(self.entity)
        self.assertEqual(len(self.engine._entity_list), 0)

    def test_get_entity_by_group(self):
        self.engine.add_entity(self.entity)
        res = self.engine.get_entity_by_group('test1')
        self.assertEqual(res, [self.entity])
        self.engine.remove_entity(self.entity)
        res = self.engine.get_entity_by_group('test1')
        self.assertEqual(res, [])


class SystemTest(System):

    def start(self):
        pass

    def update(self, time):
        pass

    def end(self):
        pass


class Component1:
    pass

