class Motion(object):
    def __init__(self, x_velocity=0, y_velocity=0):
        self.x_velocity = x_velocity
        self.y_velocity = y_velocity
        self.changes_blocked = False

    def set(self, x_vel, y_vel):
        if self.x_velocity != x_vel or self.y_velocity != y_vel:
            self.x_velocity = x_vel
            self.y_velocity = y_vel
            self.changes_blocked = True

