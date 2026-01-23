from .interface import PricingStrategy


class SurgePricing(PricingStrategy):
    def __init__(self, multiplier):
        self.multiplier = multiplier  # e.g., 2.0x or 3.5x

    def calculate_fare(self, distance_km, time_minutes):
        # We reuse the logic, but multiply the result
        base_fare = 2.00
        cost_per_km = 1.50
        cost_per_min = 0.25

        normal_price = base_fare + (distance_km * cost_per_km) + (time_minutes * cost_per_min)
        return normal_price * self.multiplier