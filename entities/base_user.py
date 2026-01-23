import uuid

class BaseUser:
    def __init__(self, x, y):
        self.id = str(uuid.uuid4())
        self.x = x
        self.y = y

    def get_position(self):
        return (self.x, self.y)