from engine.system import System
from components.motion import Motion
from components.position import Position


class MovementSystem(System):
    def __init__(self, engine, wait_interval=0):
        self.engine = engine
        self.wait_interval = wait_interval
        self.elapsed_time = 0

    def end(self):
        pass

    def update(self, time):
        entities = self.engine.get_entity_by_group("movement")
        self.elapsed_time += time

        for e in entities:
            pos = e.get(Position)
            mot = e.get(Motion)

            if self.elapsed_time > self.wait_interval:
                pos.x += mot.x_velocity
                pos.y += mot.y_velocity
                self.elapsed_time -= self.wait_interval

    def start(self):
        pass
