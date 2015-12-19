import unittest
from engine.engine import Engine
from engine.system import System


class TestEngine(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestEngine, self).__init__(*args, **kwargs)
        self.engine = Engine()

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


class SystemTest(System):

    def start(self):
        pass

    def update(self):
        pass

    def end(self):
        pass
