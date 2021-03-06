# Main Menu Template - Skeleton for a new PyGame contains Menu project
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
SKYBLUE = (0, 255, 255)

# Define our class object named "MainMenu".
class MainMenu(object):
    def __init__(self):
        font = pygame.font.SysFont("dejavu-sans", 22)
        self.start = font.render("Start Game", True, WHITE)
        self.get_fps = font.render("Get FPS", True, WHITE)
        self.quit = font.render("Quit Game", True, WHITE)
        
    def draw(self, surface):
        self.border = pygame.draw.rect(surface, SKYBLUE, (20, 280, 135, 170), 0, 12) # This is a frame for the button list.
        self.button_one = pygame.draw.rect(surface, BLUE, (20, 300, 135, 28), 0, 12)
        self.button_two = pygame.draw.rect(surface, BLUE, (20, 350, 135, 28), 0, 12)
        self.button_thr = pygame.draw.rect(surface, BLUE, (20, 400, 135, 28), 0, 12)
        surface.blit(self.start, (20, 300))
        surface.blit(self.get_fps, (20, 350))
        surface.blit(self.quit, (20, 400))
            
# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock() # Requires for second button.
mainmenu = MainMenu()
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mainmenu.button_one.collidepoint(event.pos):
                print("Game started! But you are still not make a customized here!") # After done, change this or remove it.
            if mainmenu.button_two.collidepoint(event.pos):
                print("Frame-per-second: %d" % int(clock.get_fps()))
            if mainmenu.button_thr.collidepoint(event.pos):
                print("Exiting....")
                running = False
                print("Exited!")

    # Update
    pygame.display.update() # optional
    
    # Draw / render
    screen.fill((0, 128, 255))
    mainmenu.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
