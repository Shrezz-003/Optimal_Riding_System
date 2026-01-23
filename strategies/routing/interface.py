from abc import ABC, abstractmethod

class RoutingStrategy(ABC):
    @abstractmethod
    def get_edge_weight(self, edge_data):
        pass