# import math
# import random
# import time
# import pygame
# pygame.init()

# WIDTH, HEIGHT = 800, 600

# WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Aim Trainer")

# TARGET_INCREMENT =  800
# TARGET_EVENT = pygame.USEREVENT

# TARGET_PADDING = 30

# BG_COLOR = (0, 25, 40)

# LIVES = 3

# TOP_BAR_HEIGHT = 50

# LABEL_FONT = pygame.font.SysFont("comicsans" , 24 , bold=True)


# class Target:
#     MAX_SIZE = 30
#     GROWTH_RATE = 0.2
#     COLOR = "red"
#     SECOND_COLOR = "white"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.size = 0
#         self.grow = True

#     def update(self):
#         if self.size + self.GROWTH_RATE >= self.MAX_SIZE:
#             self.grow = False

#         if self.grow:
#             self.size += self.GROWTH_RATE
#         else:
#             self.size -= self.GROWTH_RATE

#     def draw(self, win):
#         pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)
#         pygame.draw.circle(win, self.SECOND_COLOR,
#                            (self.x, self.y), self.size * 0.8)
#         pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size * 0.6)
#         pygame.draw.circle(win, self.SECOND_COLOR,
#                            (self.x, self.y), self.size * 0.4)

#     def collide(self , x , y):
#         distance = math.sqrt((self. x - x)**2 + (self.y - y)**2)
#         return distance <= self.size


# def draw(win, targets):
#     win.fill(BG_COLOR)

#     for target in targets:
#         target.draw(win)


# def format_time(secs):
#     milliseconds = math.floor(int(secs * 1000 % 100) / 100)
#     seconds = int(round(secs % 60 , 1))
#     minutes = int(secs // 60)

#     return f"{minutes:02d}:{seconds:02d}.{milliseconds}"

# def draw_top_bar(win , elapsed_time , targets_pressed , misses):
#     pygame.draw.rect(win , "grey" , (0 , 0 , WIDTH , TOP_BAR_HEIGHT))
#     time_label = LABEL_FONT.render(f"Time : {format_time(elapsed_time)}" , 1 , "black")


#     speed = round(targets_pressed / elapsed_time , 1)
#     speed_label = LABEL_FONT.render(f"Speed : {speed} t/s" , 1 , "black")

#     hits_label = LABEL_FONT.render(f"Hits : {targets_pressed} " , 1 , "black")

#     lives_label = LABEL_FONT.render(f"LIVES : {LIVES - misses} " , 1 , "black")

#     win.blit(time_label , (5 , 5))
#     win.blit(speed_label , (200 , 5))
#     win.blit(hits_label , (450 , 5))
#     win.blit(lives_label , (650 , 5))


# def get_middle(surface):
#     return WIDTH / 2 - surface.get_width() / 2


# def end_screen(win , elapsed_time , targets_pressed , clicks):
#     win.fill(BG_COLOR)

#     time_label = LABEL_FONT.render(f"Time : {format_time(elapsed_time)}" , 1 , "white")

#     speed = round(targets_pressed / elapsed_time , 1)
#     speed_label = LABEL_FONT.render(f"Speed : {speed} t/s" , 1 , "white")

#     hits_label = LABEL_FONT.render(f"Hits : {targets_pressed} " , 1 , "white")

#     accuracy = round(targets_pressed / clicks * 100 , 1)
#     accuracy_label = LABEL_FONT.render(f"Accuracy : {accuracy}" , 1 , "white")

#     win.blit(time_label , (get_middle(time_label) , 100))
#     win.blit(speed_label , (get_middle(speed_label) , 200))
#     win.blit(hits_label , (get_middle(hits_label) , 300))
#     win.blit(accuracy_label , (get_middle(accuracy_label) , 400))

#     pygame.display.update()

#     run = True
#     while run:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
#                 quit()


# def main():
#     run = True
#     targets = []
#     clock = pygame.time.Clock()

#     target_pressed = 0
#     clicks = 0
#     misses = 0
#     start_time = time.time()

#     pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

#     while run:
#         clock.tick(60)
#         click = False
#         mouse_pos = pygame.mouse.get_pos()
#         elapsed_time = time.time() - start_time

#         for event in pygame.event.get():

#             if event.type == pygame.QUIT:
#                 run = False
#                 break

#             if event.type == TARGET_EVENT:
#                 x = random.randint(TARGET_PADDING , WIDTH - TARGET_PADDING)
#                 y = random.randint(
#                     TARGET_PADDING + TOP_BAR_HEIGHT , HEIGHT - TARGET_PADDING)
#                 target = Target(x, y)
#                 targets.append(target)

#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 click = True
#                 clicks += 1

#         for target in targets:
#             target.update()

#             if target.size <= 0:
#                 targets.remove(target)
#                 misses += 1

#             if click and target.collide(*mouse_pos):
#                 targets.remove(target)
#                 target_pressed += 1

#             if misses >= LIVES:
#                 end_screen(WIN , elapsed_time , target_pressed , clicks)


#         draw(WIN, targets)
#         draw_top_bar(WIN , elapsed_time , target_pressed , misses)
#         pygame.display.update()


#     pygame.quit()


# if __name__ == "__main__":
#     main()

import math
import random
import time
import pygame
pygame.init()

WIDTH, HEIGHT = 800, 600

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Aim Trainer")

TARGET_INCREMENT =  800
TARGET_EVENT = pygame.USEREVENT

TARGET_PADDING = 30

BG_COLOR = (0, 30, 40)

LIVES = 3

TOP_BAR_HEIGHT = 50

LABEL_FONT = pygame.font.SysFont("comicsans" , 24 , bold=True)
GUIDE_LABEL_FONT = pygame.font.SysFont("comicsans" , 18 , bold=True)

class Target:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 20  # Set initial size
        self.MAX_TIME = 5
        self.COLOR = "light blue"
        self.ON_SCREEN_TIME = time.time()  # Initialize ON_SCREEN_TIME

    def update(self):
        if time.time() - self.ON_SCREEN_TIME >= self.MAX_TIME:
            self.size = 0  # Make the target invisible if it exceeds MAX_TIME

    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x, self.y), self.size)

    def collide(self, x, y):
        distance = math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2)
        return distance <= self.size
        
    
def main():
    run = True
    targets = []
    clock = pygame.time.Clock()

    hits = 0
    clicks = 0
    misses = 0
    start_time = time.time()

    pygame.time.set_timer(TARGET_EVENT, TARGET_INCREMENT)

    while run:
        clock.tick(60)
        click = False
        mouse_pos = pygame.mouse.get_pos()
        elapsed_time = time.time() - start_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                run = False
                break

            if event.type == TARGET_EVENT:
                x = random.randint(TARGET_PADDING, WIDTH - TARGET_PADDING)
                y = random.randint(TARGET_PADDING + TOP_BAR_HEIGHT, HEIGHT - TARGET_PADDING)
                target = Target(x, y)
                targets.append(target)

            if event.type == pygame.MOUSEBUTTONDOWN:
                click = True
                clicks += 1

        for target in targets:
            target.update()

            if target.size <= 0:
                targets.remove(target)
                misses += 1

            if click and target.collide(*mouse_pos):
                targets.remove(target)
                hits += 1

            if misses >= LIVES:
                end_screen(WIN, elapsed_time, hits, clicks)

        draw(WIN, targets)
        draw_top_bar(WIN, elapsed_time, hits, misses)
        pygame.display.update()

    pygame.quit()
    
def format_time(secs):
    milliseconds = math.floor(int(secs * 1000 % 100) / 100)
    seconds = int(round(secs % 60 , 1))
    minutes = int(secs // 60)

    return f"{minutes:02d}:{seconds:02d}.{milliseconds}"

def draw_top_bar(win , elapsed_time , targets_pressed , misses):
    pygame.draw.rect(win , "grey" , (0 , 0 , WIDTH , TOP_BAR_HEIGHT))
    time_label = LABEL_FONT.render(f"Time : {format_time(elapsed_time)}" , 1 , "black")
    speed = round(targets_pressed / elapsed_time , 1)
    speed_label = LABEL_FONT.render(f"Speed : {speed} t/s" , 1 , "black")

    hits_label = LABEL_FONT.render(f"Hits : {targets_pressed} " , 1 , "black")

    lives_label = LABEL_FONT.render(f"LIVES : {LIVES - misses} " , 1 , "black")

    win.blit(time_label , (5 , 5))
    win.blit(speed_label , (200 , 5))
    win.blit(hits_label , (450 , 5))
    win.blit(lives_label , (650 , 5))


def draw(win, targets):
    win.fill(BG_COLOR)
    for target in targets:
        target.draw(win)

def get_middle(surface):
    return WIDTH / 2 - surface.get_width() / 2

def end_screen(win , elapsed_time , targets_pressed , clicks):
    win.fill(BG_COLOR)

    time_label = LABEL_FONT.render(f"Time : {format_time(elapsed_time)}" , 1 , "white")

    speed = round(targets_pressed / elapsed_time , 1)
    speed_label = LABEL_FONT.render(f"Speed : {speed} t/s" , 1 , "white")

    hits_label = LABEL_FONT.render(f"Hits : {targets_pressed} " , 1 , "white")

    accuracy = round(targets_pressed / clicks * 100 , 1)
    accuracy_label = LABEL_FONT.render(f"Accuracy : {accuracy}" , 1 , "white")

    message = "Press 'ESC' key or any key to Quit game Or Press 'r' key to play again"


    guide_label = GUIDE_LABEL_FONT.render(message , 1 , "grey")

    win.blit(time_label , (get_middle(time_label) , 100))
    win.blit(speed_label , (get_middle(speed_label) , 150))
    win.blit(hits_label , (get_middle(hits_label) , 200))
    win.blit(accuracy_label , (get_middle(accuracy_label) , 250))
    win.blit(guide_label , (get_middle(accuracy_label) - 230, 350))

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                main()


if __name__ == "__main__":
    main()