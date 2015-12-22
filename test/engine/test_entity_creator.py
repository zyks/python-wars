import unittest

from engine.engine import Engine
from entity_creator import EntityCreator


class TestEntityCreator(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEntityCreator, self).__init__(*args, **kwargs)
        self.entity_creator = EntityCreator(Engine())

    def test_create_snake_segment(self):
        self.entity_creator.create_snake_segment('img', 0, 0, 0, 1, True, False, None)
        self.assertEqual(len(self.entity_creator._engine._entity_list), 1)

    def test_create_snake(self):
        self.entity_creator.create_snake(1)
        self.assertEqual(len(self.entity_creator._engine._entity_list), 5)

