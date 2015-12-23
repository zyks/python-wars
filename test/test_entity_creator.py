import unittest
from components.graphics import Graphics
from components.position import Position
from engine.engine import Engine
from entity_creator import EntityCreator


class TestEntityCreator(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEntityCreator, self).__init__(*args, **kwargs)
        self.engine = Engine()
        self.engine._entity_components_packer.add('renderable', [Position, Graphics])
        self.entity_creator = EntityCreator(self.engine)

    def test_create_snake_segment(self):
        self.entity_creator.create_snake_segment(None, 0, 0, 0, 1, True, False, None)
        self.assertEqual(len(self.entity_creator._engine._entity_list), 1)
        self.assertEqual(self.engine.get_entity_by_group('renderable'), self.engine._entity_list)

    def test_create_snake(self):
        self.entity_creator.create_snake(1, None, None)
        self.assertEqual(len(self.entity_creator._engine._entity_list), 5)
        self.assertEqual(self.engine.get_entity_by_group('renderable'), self.engine._entity_list)

