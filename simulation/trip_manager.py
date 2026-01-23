from core.algorithms.pathfinding import find_path
from core.dsa.quadtree import Rectangle
import config


class TripManager:
    def __init__(self, quadtree, graph, routing_strategy):
        self.quadtree = quadtree
        self.graph = graph
        self.strategy = routing_strategy

    def request_fleet_dispatch(self, drivers, rider):
        """
        COMPARES ALL DRIVERS to find the one with the lowest REAL cost.
        """
        best_driver = None
        lowest_cost = float('inf')

        print("\n")
        print("Finding Your Best Captain...")
        print("\n")

        # Evaluate every driver
        for driver in drivers:
            start_node = self._get_closest_node(driver.x, driver.y)
            end_node = self._get_closest_node(rider.x, rider.y)

            # Calculate the Eco Path for this specific driver
            path = find_path(self.graph, start_node, end_node, self.strategy)

            # Calculate the REAL cost (Fuel + Jam Penalty)
            cost = self._calculate_real_cost(path)

            # Store this path on the driver so we can draw it as a "Candidate" (Red)
            # If they win, we will turn it Green later.
            driver.comparison_path = path
            driver.current_path = []  # Clear any old green path

            print(f"Driver {driver.id}: Length {len(path)} nodes | Cost {int(cost)}")

            # Is this the best one so far?
            if cost < lowest_cost:
                lowest_cost = cost
                best_driver = driver

        # ASSIGN THE WINNER
        if best_driver:
            print("-" * 50)
            print(f"Your Captain is on the way!! {best_driver.id} (Cost {int(lowest_cost)})")

            # Lock in the winner's path as the "Active" one (Green)
            best_driver.current_path = best_driver.comparison_path
            best_driver.comparison_path = []  # Clear the red line for the winner
            rider.assign_driver(best_driver.id)
            return True
        else:
            print("Sorry No Captain available!")
            return False

    def _get_closest_node(self, x, y):
        if not self.graph.adj_list: return (0, 0)
        return min(self.graph.adj_list.keys(), key=lambda n: (n[0] - x) ** 2 + (n[1] - y) ** 2)

    def _calculate_real_cost(self, path):
        total = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i + 1]
            for edge in self.graph.adj_list[u]:
                if edge['to'] == v:
                    total += self.strategy.get_edge_weight(edge)
                    break
        return total