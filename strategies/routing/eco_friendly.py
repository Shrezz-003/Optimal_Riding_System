from .interface import RoutingStrategy
import config


class EcoFriendlyRoute(RoutingStrategy):
    def get_edge_weight(self, edge_data):
        distance = edge_data['distance']
        speed = edge_data['speed']
        traffic = edge_data['traffic_factor']

        # 1. Base Cost (Fuel to move distance)
        move_cost = distance * config.FUEL_BURN_MOVING

        # 2. Time Cost (Penalty for sitting in traffic)
        # Physics: Time = Distance / (Speed / Traffic)
        real_speed = max(1, speed / traffic)
        time_taken = distance / real_speed

        # Idle cost only applies heavily if traffic slows us down
        idle_cost = time_taken * config.FUEL_BURN_IDLING

        return move_cost + idle_cost