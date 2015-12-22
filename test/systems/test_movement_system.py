import unittest
from engine.entity import Entity
from components.motion import Motion
from components.position import Position
from systems.movement_system import MovementSystem

class TestMovementSystem(unittest.TestCase):

    def test_moving_entity(self):
        entity = Entity([Position(0,0,0), Motion(3,4)])
        self.sut = MovementSystem(EngineStub([entity]))
        self.sut.update(1)

        pos = entity.get(Position)
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.y, 4)

    def test_moving_system_with_interval(self):
        entity = Entity([Position(0, 0, 0), Motion(3, 4)])
        pos = entity.get(Position)
        self.sut = MovementSystem(EngineStub([entity]), 2)

        self.sut.update(1)
        self.assertEqual(pos.x, 0)
        self.assertEqual(pos.y, 0)

        self.sut.update(2)
        self.assertEqual(pos.x, 3)
        self.assertEqual(pos.y, 4)


class EngineStub(object):
    def __init__(self, entites_to_return):
        self.entities = entites_to_return

    def get_entity_by_group(self, name):
        return self.entities