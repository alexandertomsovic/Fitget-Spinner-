# A fidget Spinner Program Created by Alex Tomsovic
# View my Github and more at linktr.ee/alextomsovic

# Please note that this program requires the pygame library to run.
# To install type "pip install pygame" into your python terminal.

import pygame
import sys
from math import *

# Pygame Window Initialization 
pygame.init()

width = 700
height = 700

display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
pygame.display.set_caption("Fidget Spinner Simulation - Alex Tomsovic")

# All Colors
background = (51, 51, 51)
white = (240, 240, 240)
red = (176, 58, 46)
dark_red = (120, 40, 31)
dark_gray = (23, 32, 42)
blue = (40, 116, 166)
dark_blue = (26, 82, 118)
yellow = (183, 149, 11)
dark_yellow = (125, 102, 8)
green = (29, 131, 72)
dark_green = (20, 90, 50)
orange = (230, 126, 34)
dark_orange = (126, 81, 9)


# Pygame Window Closing
def close():
    pygame.quit()
    sys.exit()


# Spinner Implemented onto Pygame Window
def show_spinner(angle, color, dark_color):
    d = 80
    innerd = 50
    x = width/2 - d/2
    y = height/2
    l = 200
    r = l/(3**0.5)
    w = 10
    lw = 60

# Mathmatics implemented 

    # x = originx + r*cos(angle)
    # y = originy + r*sin(angle)
    
    centre = [x, y, d, d]
    centre_inner = [x + d/2 - innerd/2, y + d/2 - innerd/2, innerd, innerd]
    
    top = [x, y - l/(3)**0.5, d, d]
    top_inner = [x, y - l/(3)**0.5, innerd, innerd]

    top[0] = x + r*cos(radians(angle))
    top[1] = y + r*sin(radians(angle))
    top_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle))
    top_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle))
    
    left = [x - l/2, y + l/(2*(3)**0.5), d, d]
    left_inner = [x, y - l/(3)**0.5, innerd, innerd]

    left[0] = x + r*cos(radians(angle - 120))
    left[1] = y + r*sin(radians(angle - 120))
    left_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle - 120))
    left_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle - 120))
    
    
    right = [x + l/2, y + l/(2*(3)**0.5), d, d]
    right_inner = [x, y - l/(3)**0.5, innerd, innerd]

    right[0] = x + r*cos(radians(angle + 120))
    right[1] = y + r*sin(radians(angle + 120))
    right_inner[0] = x + d/2 - innerd/2 + r*cos(radians(angle + 120))
    right_inner[1] = y + d/2 - innerd/2 + r*sin(radians(angle + 120))
    
    # Shape Drawings onto Pygame Window
    pygame.draw.line(display, dark_color, (top[0] + d/2, top[1] + d/2), (centre[0] + d/2, centre[1] + d/2), lw)
    pygame.draw.line(display, dark_color, (left[0] + d/2, left[1] + d/2), (centre[0] + d/2, centre[1] + d/2), lw)
    pygame.draw.line(display, dark_color, (right[0] + d/2, right[1] + d/2), (centre[0] + d/2, centre[1] + d/2), lw)
    pygame.draw.ellipse(display, color, tuple(centre))
    pygame.draw.ellipse(display, dark_color, tuple(centre_inner))
    pygame.draw.ellipse(display, color, tuple(top))
    pygame.draw.ellipse(display, dark_gray, tuple(top_inner), 10)
    pygame.draw.ellipse(display, color, tuple(left))
    pygame.draw.ellipse(display, dark_gray, tuple(left_inner), 10)
    pygame.draw.ellipse(display, color, tuple(right))
    pygame.draw.ellipse(display, dark_gray, tuple(right_inner), 10)
    

# Information on Pygame Window Displayed
def show_info(friction, speed):
    font = pygame.font.SysFont("Times New Roman", 18)
    author_name = font.render("Created by: Alex Tomsovic       " + str(friction), True, white)
    frictionText = font.render("Friction: " + str(friction), True, white)
    speedText = font.render("Spinner Speed: " + str(int(speed)), True, white)
    display.blit(author_name, (490, 15))
    display.blit(speedText, (550, 45))
    display.blit(frictionText, (590, 75))

    
    


    

# Spinner Function
def spinner():
    spin = True

    angle = 0

    speed = 0.0
    friction = 0.03
    rightPressed = False
    leftPressed = False

    direction = 1
    color = [[red, dark_red], [blue, dark_blue], [yellow, dark_yellow], [green, dark_green], [orange, dark_orange]]
    index = 0
    
    while spin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close()
                if event.key == pygame.K_RIGHT:
                    rightPressed = True
                    direction = 1
                if event.key == pygame.K_LEFT:
                    leftPressed = True
                    direction = -1
                if event.key == pygame.K_SPACE:
                    index += 1
                    if index >= len(color):
                        index = 0
            if event.type == pygame.KEYUP:
                leftPressed = False
                rightPressed = False

        # Reversing Rotational Direction 
        if direction == 1:
            if rightPressed:
                speed += 0.3
            else:
                speed -= friction
                if speed < 0:
                    speed = 0.0
        else:
            if leftPressed:
                speed -= 0.3
            else:
                speed += friction
                if speed > 0:
                    speed = 0.0

        display.fill(background)

        angle += speed

        # Spinner + Text Display
        show_spinner(angle, color[index][0], color[index][1])
        show_info(friction, speed)

        pygame.display.update()
        clock.tick(90)

spinner()
