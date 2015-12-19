import unittest
from engine.entity import Entity
from engine.exceptions import NonexistentComponent


class TestEntity(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEntity, self).__init__(*args, **kwargs)
        self.entity = Entity()
        self.component1 = Component1()
        self.component2 = Component2()

    def test_add_component_with_single_component(self):
        self.entity.add(self.component1)
        self.assertEqual(len(self.entity.components), 1)

    def test_add_component_with_array_of_components(self):
        self.entity.add([self.component1, self.component2])
        self.assertEqual(len(self.entity.components), 2)

    def test_get_component(self):
        self.entity.add(self.component1)
        self.assertEqual(self.entity.get(Component1), self.component1)

    def test_remove_component(self):
        self.entity.add([self.component1, self.component2])
        self.entity.remove(Component1)
        self.assertEqual(len(self.entity.components), 1)

        with self.assertRaises(NonexistentComponent):
            self.entity.get(Component1)

class Component1:
    pass


class Component2:
    pass