from .interface import RoutingStrategy


class FastestRoute(RoutingStrategy):
    def get_edge_weight(self, edge_data):
        distance = edge_data['distance']
        speed = edge_data['speed']
        traffic = edge_data['traffic_factor']  # 1.0 is clear, 5.0 is jam

        # Physics: Time = Distance / Speed
        # If traffic is 5.0 (bad), speed is divided by 5, so Time is 5x higher.
        estimated_time = distance / (speed / traffic)

        return estimated_time