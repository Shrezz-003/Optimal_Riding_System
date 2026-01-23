class Vehicle:
    def __init__(self, efficiency, tank_size):
        self.efficiency = efficiency
        self.tank_size = tank_size
        self.current_fuel = tank_size

    def burn_fuel(self, amount):
        if self.current_fuel >= amount:
            self.current_fuel -= amount
            return True
        return False