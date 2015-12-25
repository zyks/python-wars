class Graphics(object):

    def __init__(self, image, x=0, y=0, width=0, height=0):
        self.image = image
        self.x = x
        self.y = y

        if width == 0 or height == 0:
            self.width = image.get_width()
            self.height = image.get_height()
        else:
            self.width, self.height = width, height
