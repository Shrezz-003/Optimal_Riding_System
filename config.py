# SCREEN SETTINGS
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
FPS = 60

# COLORS (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)       # Rejected / Bad Path
GREEN = (0, 200, 0)     # Optimal / Winning Path
BLUE = (0, 0, 255)      # Driver
GREY = (220, 220, 220)  # Roads
DARK_RED = (200, 50, 50)# Traffic Jam Zone

# PHYSICS & ECO-MATH
VEHICLE_SPEED = 5       # Speed of animation
FUEL_BURN_MOVING = 1.0  # Cost per pixel traveled
FUEL_BURN_IDLING = 5.0  # Penalty for traffic (Moderate)
TRAFFIC_FACTOR_JAM = 10.0 # Jammed roads are 10x slower/more expensive