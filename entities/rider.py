from .base_user import BaseUser

class Rider(BaseUser):
    def __init__(self, x, y, dest_x, dest_y):
        super().__init__(x, y)
        self.dest_x = dest_x
        self.dest_y = dest_y
        self.status = "SEARCHING"

    def assign_driver(self, driver_id):
        self.driver_id = driver_id
        self.status = "RIDING"