class Rectangle:
    def __init__(self, x, y, w, h):
        self.x, self.y = x, y
        self.w, self.h = w, h

    def contains(self, point):
        px, py = point.get_position()
        return (self.x <= px < self.x + self.w and
                self.y <= py < self.y + self.h)


class QuadTree:
    def __init__(self, boundary, capacity=4):
        self.boundary = boundary
        self.capacity = capacity
        self.drivers = []
        self.divided = False

    def insert(self, driver):
        if not self.boundary.contains(driver):
            return False

        if len(self.drivers) < self.capacity:
            self.drivers.append(driver)
            return True

        if not self.divided:
            self.subdivide()

        return (self.northeast.insert(driver) or
                self.northwest.insert(driver) or
                self.southeast.insert(driver) or
                self.southwest.insert(driver))

    def subdivide(self):
        x, y = self.boundary.x, self.boundary.y
        w, h = self.boundary.w / 2, self.boundary.h / 2

        self.northeast = QuadTree(Rectangle(x + w, y, w, h))
        self.northwest = QuadTree(Rectangle(x, y, w, h))
        self.southeast = QuadTree(Rectangle(x + w, y + h, w, h))
        self.southwest = QuadTree(Rectangle(x, y + h, w, h))
        self.divided = True

    def query(self, range_box, found_drivers):
        if not self.boundary_intersects(range_box):
            return

        for driver in self.drivers:
            if range_box.contains(driver):
                found_drivers.append(driver)

        if self.divided:
            self.northwest.query(range_box, found_drivers)
            self.northeast.query(range_box, found_drivers)
            self.southwest.query(range_box, found_drivers)
            self.southeast.query(range_box, found_drivers)

    def boundary_intersects(self, range_box):
        return not (range_box.x > self.boundary.x + self.boundary.w or
                    range_box.x + range_box.w < self.boundary.x or
                    range_box.y > self.boundary.y + self.boundary.h or
                    range_box.y + range_box.h < self.boundary.y)