from .interface import PricingStrategy


class StandardPricing(PricingStrategy):
    def calculate_fare(self, distance_km, time_minutes):
        base_fare = 2.00
        cost_per_km = 1.50
        cost_per_min = 0.25

        return base_fare + (distance_km * cost_per_km) + (time_minutes * cost_per_min)