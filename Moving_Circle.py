#Importing library
import sys
import pygame
#Initialization
pygame.init()

#Setting screen size
size = 600, 500
width, height = size

console = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Circle")

radius = 30
black = 0,0,0
yellow = 255,255,0

balls = [{"x":0, "y":10, "dx":5, "dy":5},
         {"x":100, "y":100, "dx":10, "dy":10}]

#drawing a circle
def circle(x, y):
    center = (x, y)
    pygame.draw.circle(console, yellow, center, radius)

def color_ball(ball):
    circle(ball['x'], ball['y'])
    ball['x'] += ball['dx']
    ball['y'] += ball['dy']

    if(ball['x'] < 0 or ball['x'] > width):
        ball['dx'] = -ball['dx']

    if(ball['y'] < 0 or ball['y'] > height):
        ball['dy'] = -ball['dy']

def paint():
    global x
    console.fill(black)
    for ball in balls:
        color_ball(ball)

def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        paint()
        pygame.display.flip()
        pygame.time.wait(50)

main()
                
