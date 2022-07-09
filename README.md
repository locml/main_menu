(Some of thing you must know)

# First
To see the first version I made this project return to [novelpy](https://github.com/locml/novelpy) and watch menu.py for the code.

And now I remove ```draw_rect()``` and use ```pygame.draw.rect()``` even added the menu as object class instead.

I also added a frame for the list of buttons and create them in roundrect style instead of rect.

# Second
No downloadable released for this project, okay ?

# Final
I'm not allowed any fork of this since I uploaded for make as a template 

(Send me at ntienloc057@gmail.com for modified and fork).


(Making a new game with game.py)

# How to do ?

Write a variable and add ```MainMenu()``` as an object class.
LLike this:

```py
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
 ... # The code at here not inside this help.
mainmenu = MainMenu() # Replace mainmenu before the "=" of this line with your name you want
```

# Second (How to draw the rect directly to the screen add at the loop)
```py
    mainmenu.draw(screen)
```
# Final (Add the rect collidepoint in the loop event pygame.MOUSEBUTTONDOWN)
```py
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mainmenu.button_one.collidepoint(event.pos):
                print("Game started! But you are still not make a customized here!") # After done, change this or remove it.
            if mainmenu.button_two.collidepoint(event.pos):
                print("Frame-per-second: %d" % int(clock.get_fps()))
            if mainmenu.button_thr.collidepoint(event.pos):
                print("Exiting....")
                running = False
                print("Exited!")
```
