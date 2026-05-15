import pygame
import sys
import config
from simulation.world import World
from simulation.trip_manager import TripManager
from ui.renderer import Renderer
from entities.rider import Rider
from entities.driver import Driver
from entities.vehicle import Vehicle
from strategies.routing.eco_friendly import EcoFriendlyRoute


def main():
    pygame.init()
    screen = pygame.display.set_mode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
    pygame.display.set_caption("EcoRide: Manual Fleet Dispatch Mode")
    clock = pygame.time.Clock()

    world = World()
    routing_strategy = EcoFriendlyRoute()
    trip_manager = TripManager(world.quadtree, world.graph, routing_strategy)
    renderer = Renderer(screen)

    # --- 1. SETUP THE MAP WITH A JAM ---
    print("Building City Grid...")
    world.graph.adj_list.clear()
    step = 80
    for x in range(0, config.SCREEN_WIDTH, step):
        for y in range(0, config.SCREEN_HEIGHT, step):
            if x + step < config.SCREEN_WIDTH:
                world.graph.add_edge((x, y), (x + step, y), step)
            if y + step < config.SCREEN_HEIGHT:
                world.graph.add_edge((x, y), (x, y + step), step)

    # CREATE PERMANENT JAM (Center)
    center_x, center_y = config.SCREEN_WIDTH // 2, config.SCREEN_HEIGHT // 2

    # CHANGED: Reduced radius from 250 to 170 to make the jam smaller
    jam_radius = 170

    for u in world.graph.adj_list:
        for edge in world.graph.adj_list[u]:
            rx, ry = u
            if abs(rx - center_x) < jam_radius and abs(ry - center_y) < jam_radius:
                edge['traffic_factor'] = config.TRAFFIC_FACTOR_JAM
            else:
                edge['traffic_factor'] = 1.0

    # CLEAR DRIVERS (Start Empty)
    world.drivers.clear()
    active_rider = None

    print("--- READY ---")
    print("RIGHT CLICK: Add Driver")
    print("LEFT CLICK: Place Rider & Dispatch Fleet")
    print("SPACEBAR: Reset")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # --- RESET ---
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    world.drivers.clear()
                    active_rider = None
                    print("Map Reset.")

            # --- MOUSE CONTROLS ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # RIGHT CLICK (Button 3) -> ADD DRIVER
                if event.button == 3:
                    new_driver = Driver(mx, my, Vehicle(1.0, 100))
                    new_driver.id = f"D-{len(world.drivers) + 1}"
                    world.drivers.append(new_driver)
                    print(f"Added {new_driver.id} at ({mx}, {my})")

                # LEFT CLICK (Button 1) -> PLACE RIDER & DISPATCH
                elif event.button == 1:
                    if not world.drivers:
                        print("Place at least one driver first (Right Click)!")
                        continue

                    active_rider = Rider(mx, my, 0, 0)

                    # TRIGGER THE ALGORITHM
                    trip_manager.request_fleet_dispatch(world.drivers, active_rider)

        world.update()
        renderer.draw_world(world)
        renderer.draw_drivers(world.drivers)
        if active_rider:
            renderer.draw_rider(active_rider)

        # UI OVERLAY
        font = pygame.font.SysFont("Arial", 16)
        controls = "Right Click: Add Driver | Left Click: Dispatch Fleet | Space: Reset"
        label = font.render(controls, True, config.BLACK)
        screen.blit(label, (10, 10))

        pygame.display.flip()
        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()