class Position(object):

    def __init__(self, x, y, rotation):
        self.x = x
        self.y = y
        self.rotation = rotation

    def set(self, position):
        self.x = position.x
        self.y = position.y
        self.rotation = position.rotation

