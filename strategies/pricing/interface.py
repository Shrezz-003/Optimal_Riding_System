from abc import ABC, abstractmethod

class PricingStrategy(ABC):
    @abstractmethod
    def calculate_fare(self, distance_km, time_minutes):
        """Calculates the total cost of the ride."""
        pass