from .base_user import BaseUser
import config


class Driver(BaseUser):
    def __init__(self, x, y, vehicle):
        super().__init__(x, y)
        self.vehicle = vehicle
        self.is_available = True

        self.current_path = []  # The Winner's Path (Green)
        self.comparison_path = []  # The Rejected Path (Red)

    def move(self):
        """Moves the driver towards the next point in the path."""
        if not self.current_path:
            return False

        target_x, target_y = self.current_path[0]

        dx = target_x - self.x
        dy = target_y - self.y
        distance = (dx ** 2 + dy ** 2) ** 0.5

        # Snap to target if close enough
        if distance < 5:
            self.x = target_x
            self.y = target_y
            self.current_path.pop(0)
            return True

        # Move along the vector
        speed = config.VEHICLE_SPEED
        move_x = (dx / distance) * speed
        move_y = (dy / distance) * speed

        self.x += move_x
        self.y += move_y
        return True