import unittest
from engine.entity import Entity
from engine.matchingComponentsEntityGroup import MatchingComponentsEntityGroup


class TestMatchingComponentsEntityGroup(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestMatchingComponentsEntityGroup, self).__init__(*args, **kwargs)
        self.sut = MatchingComponentsEntityGroup()
        self.entity = Entity()
        self.component1 = Component1()
        self.component2 = Component2()
        self.component3 = Component3()
        self.entity.add([self.component1, self.component2])

    def test_add(self):
        self.sut.add("test1", [Component1])
        self.sut.add("test2", [Component2])
        self.assertEqual(len(self.sut.registered_groups), 2)

    def test_remove(self):
        self.sut.add("test", [Component1])
        self.assertEqual(len(self.sut.registered_groups), 1)
        self.sut.remove("test")
        self.assertEqual(len(self.sut.registered_groups), 0)

    def test_on_registered_entity(self):
        self.sut.add("test_valid", [Component1, Component2])
        self.sut.add("test_invalid", [Component1, Component3])
        self.sut.on_entity_registered(self.entity)
        self.assertIn(self.entity, self.sut.get("test_valid"))
        self.assertNotIn(self.entity, self.sut.get("test_invalid"))


class Component1:
    pass


class Component2:
    pass


class Component3:
    pass
