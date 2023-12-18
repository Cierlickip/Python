import pygame
import sys
import random

class Snowflake:
    def __init__(self, x, y, radius):
        self.rect = pygame.Rect(x, y, radius * 2, radius * 2)

    def move(self, speed):
        self.rect.move_ip(0, speed)

    def reached_bottom(self, screen_height):
        return self.rect.bottom >= screen_height

class SnowGame:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Gra o łapaniu śniegu")

        self.white = (255, 255, 255)
        self.blue = (135, 206, 250)

        self.snowflakes = []

        self.clock = pygame.time.Clock()
        self.game_over = False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for snowflake in self.snowflakes:
                    if snowflake.rect.colliderect(pygame.Rect(mouse_pos, (1, 1))):
                        self.snowflakes.remove(snowflake)

    def generate_snowflake(self):
        if random.random() < 0.04:
            x_pos = random.randint(0, self.width - 20 * 2)
            y_pos = 0
            snowflake = Snowflake(x_pos, y_pos, 10)
            self.snowflakes.append(snowflake)

    def check_collision(self):
        for snowflake in self.snowflakes:
                if snowflake.reached_bottom(self.height):
                    self.game_over = True

    def update_screen(self):
        self.screen.fill(self.blue)
        for snowflake in self.snowflakes:
            pygame.draw.circle(self.screen, self.white, snowflake.rect.center, 10)
        pygame.display.flip()

    def run_game(self):
        while not self.game_over:
            self.handle_events()
            self.generate_snowflake()

            for snowflake in self.snowflakes:
                snowflake.move(5)

            self.check_collision()
            self.update_screen()

            self.clock.tick(30)

        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    pygame.init()
    game = SnowGame(800, 600)
    game.run_game()
