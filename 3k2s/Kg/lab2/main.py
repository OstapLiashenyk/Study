import pygame
from OpenGL.raw.GLU import gluOrtho2D
from numpy import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
import glfw
import imgui
from imgui.integrations.glfw import GlfwRenderer


def init_opengl(width, height):
    pygame.display.set_mode((width, height), DOUBLEBUF|OPENGL)
    gluOrtho2D(0, width, height, 0)

def draw_grid(grid_size, width, height):
    glColor3fv((0.5, 0.5, 0.5))  # Сірий колір для сітки
    glBegin(GL_LINES)
    for x in range(0, width, grid_size):
        glVertex2f(x, 0)
        glVertex2f(x, height)
    for y in range(0, height, grid_size):
        glVertex2f(0, y)
        glVertex2f(width, y)
    glEnd()

def draw_hexagon(center, size, angle, color, mode="fill"):
    if mode == "fill":
        glBegin(GL_POLYGON)
    else:
        glBegin(GL_LINE_LOOP)

    glColor3fv(color)
    for i in range(6):
        angle_deg = 60 * i + angle
        x = center[0] + size * math.cos(math.radians(angle_deg))
        y = center[1] + size * math.sin(math.radians(angle_deg))
        glVertex2f(x, y)
    glEnd()

def main():
    width, height = 800, 600
    pygame.init()
    init_opengl(width, height)

    hexagons = []
    selected_hexagon = None
    draw_mode = "fill"  # Може бути "fill" або "outline"
    current_mode = "default"  # Зберігаємо стан для логічних операцій

    grid_size = 20

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button to add hexagon
                    hexagons.append({'center': pygame.mouse.get_pos(), 'size': 30, 'angle': 0, 'color': (1, 1, 1)})
                elif event.button == 3:  # Right mouse button to select hexagon
                    for i, hexagon in enumerate(hexagons):
                        mouse_pos = pygame.mouse.get_pos()
                        if math.hypot(hexagon['center'][0] - mouse_pos[0], hexagon['center'][1] - mouse_pos[1]) < hexagon['size']:
                            selected_hexagon = i
                            break
                elif event.button == 2 and selected_hexagon is not None:  # Middle mouse button to move selected hexagon
                    hexagons[selected_hexagon]['center'] = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_o:
                    current_mode = "OR"
                elif event.key == pygame.K_n:
                    current_mode = "NOT_OR"
                elif event.key == pygame.K_f:
                    current_mode = "default"
                elif event.key == pygame.K_k:  # Change to outline mode
                    draw_mode = "outline"
                elif event.key == pygame.K_l:  # Change to fill mode
                    draw_mode = "fill"
                elif event.key == pygame.K_z:
                    grid_size += 1
                elif event.key == pygame.K_x:
                    grid_size -= 1 if grid_size- 1 > 0 else 0
                if selected_hexagon is not None:
                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:  # Rotate right
                        hexagons[selected_hexagon]['angle'] += 5
                    elif event.key == pygame.K_MINUS:  # Rotate left
                        hexagons[selected_hexagon]['angle'] -= 5
                    elif event.key == pygame.K_c:  # Change color
                        hexagons[selected_hexagon]['color'] = (random.random(), random.random(), random.random())

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_grid(grid_size, width, height)  # Draw the grid

        if current_mode in ["OR", "NOT_OR"]:
            glEnable(GL_COLOR_LOGIC_OP)
            glLogicOp(GL_OR if current_mode == "OR" else GL_NOR)
        else:
            glDisable(GL_COLOR_LOGIC_OP)

        for hexagon in hexagons:
            draw_hexagon(hexagon['center'], hexagon['size'], hexagon['angle'], hexagon['color'], draw_mode)

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()

if __name__ == "__main__":
    main()
