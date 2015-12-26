class Position(object):

    def __init__(self, x=0, y=0, rotation=0):
        self.x = x
        self.y = y
        self.rotation = rotation

    def set(self, position):
        self.x = position.x
        self.y = position.y
        self.rotation = position.rotation

    def move(self, motion, time):
        self.x += time * motion.x_velocity
        self.y += time * motion.y_velocity

