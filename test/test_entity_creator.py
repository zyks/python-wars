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
        sprites = {'snake_body': ImageStub(), 'snake_head': ImageStub(), 'snake_tail': ImageStub()}
        self.entity_creator = EntityCreator(self.engine, sprites)

    def test_create_snake_segment(self):
        self.entity_creator.create_snake_segment(0, 0, 0, True, False)
        self.assertEqual(len(self.entity_creator._engine._entity_list), 1)
        self.assertEqual(self.engine.get_entity_by_group('renderable'), self.engine._entity_list)

    def test_create_snake(self):
        self.entity_creator.create_snake()
        self.assertEqual(len(self.entity_creator._engine._entity_list), 5)
        self.assertEqual(self.engine.get_entity_by_group('renderable'), self.engine._entity_list)


class ImageStub(object):

    def get_width(self):
        return 32

    def get_height(self):
        return 32

