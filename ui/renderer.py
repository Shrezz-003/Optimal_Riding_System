import pygame
import config


class Renderer:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 18)

    def draw_world(self, world):
        self.screen.fill(config.WHITE)
        for u in world.graph.adj_list:
            for edge in world.graph.adj_list[u]:
                v = edge['to']
                # DRAW JAM ZONES IN DARK RED
                if edge['traffic_factor'] > 5.0:
                    pygame.draw.line(self.screen, config.DARK_RED, u, v, 4)
                else:
                    pygame.draw.line(self.screen, config.GREY, u, v, 1)

    def draw_drivers(self, drivers):
        for driver in drivers:
            # Draw Driver Dot
            pygame.draw.circle(self.screen, config.BLUE, (int(driver.x), int(driver.y)), 8)

            # 1. DRAW REJECTED PATHS (Thin Red Lines)
            # Use a safety check > 1 to prevent crashes
            if len(driver.comparison_path) > 1:
                pygame.draw.lines(self.screen, config.RED, False, driver.comparison_path, 1)

            # 2. DRAW WINNING PATH (Thick Green Line)
            if len(driver.current_path) > 1:
                pygame.draw.lines(self.screen, config.GREEN, False, driver.current_path, 5)

    def draw_rider(self, rider):
        pygame.draw.circle(self.screen, config.GREEN, (rider.x, rider.y), 8)
        text = self.font.render("Rider", True, config.BLACK)
        self.screen.blit(text, (rider.x + 15, rider.y))