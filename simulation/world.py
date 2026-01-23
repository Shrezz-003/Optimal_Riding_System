from core.dsa.quadtree import QuadTree, Rectangle
from core.dsa.graph import Graph
import config

class World:
    def __init__(self):
        self.graph = Graph()
        self.width = config.SCREEN_WIDTH
        self.height = config.SCREEN_HEIGHT
        self.quadtree = QuadTree(Rectangle(0, 0, self.width, self.height))
        self.drivers = []

    def update(self):
        # Rebuild QuadTree every frame (simple approach for dynamic objects)
        self.quadtree = QuadTree(Rectangle(0, 0, self.width, self.height))
        for driver in self.drivers:
            driver.move()
            self.quadtree.insert(driver)