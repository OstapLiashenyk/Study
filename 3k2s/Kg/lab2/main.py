import pygame
from OpenGL.raw.GLU import gluOrtho2D
from numpy import random
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
import math
import PIL.Image as Image


def load_texture():
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    img = Image.open("jpg/img.jpg")
    img_data = img.convert("RGBA").tobytes("raw", "RGBA", 0, -1)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, img.width, img.height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture


def init_opengl(width, height):
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    gluOrtho2D(0, width, height, 0)
    glEnable(GL_TEXTURE_2D)


def draw_grid(grid_size, width, height):
    glColor3fv((0.5, 0.5, 0.5))
    glBegin(GL_LINES)
    for x in range(0, width, grid_size):
        glVertex2f(x, 0)
        glVertex2f(x, height)
    for y in range(0, height, grid_size):
        glVertex2f(0, y)
        glVertex2f(width, y)
    glEnd()


def draw_hexagon(center, size, angle, color, mode="fill", texture=None):
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    if texture:
        glBindTexture(GL_TEXTURE_2D, texture)
    else:
        glColor3fv(color)

    glBegin(GL_POLYGON if mode == "fill" else GL_LINE_LOOP)
    for i in range(6):
        angle_deg = 60 * i + angle
        x = center[0] + size * math.cos(math.radians(angle_deg))
        y = center[1] + size * math.sin(math.radians(angle_deg))
        if texture:
            tx = 0.5 + 0.5 * math.cos(math.radians(angle_deg))
            ty = 0.5 + 0.5 * math.sin(math.radians(angle_deg))
            glTexCoord2f(tx, ty)
        glVertex2f(x, y)
    glEnd()
    # if texture:
    #     glDisable(GL_TEXTURE_2D)


def main():
    width, height = 800, 600
    pygame.init()
    init_opengl(width, height)

    texture = None  # Текстура спочатку не завантажена

    hexagons = []
    selected_hexagon = None
    draw_mode = "fill"
    current_mode = "default"
    grid_size = 20

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    hexagons.append(
                        {'center': pygame.mouse.get_pos(), 'size': 30, 'angle': 0, 'color': (1, 1, 1), 'texture': None})
                elif event.button == 3:
                    for i, hexagon in enumerate(hexagons):
                        mouse_pos = pygame.mouse.get_pos()
                        if math.hypot(hexagon['center'][0] - mouse_pos[0], hexagon['center'][1] - mouse_pos[1]) < \
                                hexagon['size']:
                            selected_hexagon = i
                            break
                elif event.button == 2 and selected_hexagon is not None:
                    hexagons[selected_hexagon]['center'] = pygame.mouse.get_pos()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_t and selected_hexagon is not None:
                    if texture is None:
                        texture = load_texture()  # Завантажуємо текстуру при першому натисканні
                    hexagons[selected_hexagon]['texture'] = texture if hexagons[selected_hexagon].get(
                        'texture') is None else None
                elif event.key == pygame.K_o:
                    current_mode = "OR"
                elif event.key == pygame.K_n:
                    current_mode = "NOT_OR"
                elif event.key == pygame.K_f:
                    current_mode = "default"
                elif event.key == pygame.K_k:
                    draw_mode = "outline"
                elif event.key == pygame.K_l:
                    draw_mode = "fill"
                elif event.key == pygame.K_z:
                    grid_size += 1
                elif event.key == pygame.K_x:
                    grid_size -= 1 if grid_size > 1 else 0
                if selected_hexagon is not None:
                    if event.key == pygame.K_PLUS or event.key == pygame.K_EQUALS:
                        hexagons[selected_hexagon]['angle'] += 5
                    elif event.key == pygame.K_MINUS:
                        hexagons[selected_hexagon]['angle'] -= 5
                    elif event.key == pygame.K_c:
                        hexagons[selected_hexagon]['color'] = (random.random(), random.random(), random.random())

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_grid(grid_size, width, height)

        if current_mode in ["OR", "NOT_OR"]:
            glEnable(GL_COLOR_LOGIC_OP)
            glLogicOp(GL_OR if current_mode == "OR" else GL_NOR)
        else:
            glDisable(GL_COLOR_LOGIC_OP)

        for hexagon in hexagons:
            draw_hexagon(hexagon['center'], hexagon['size'], hexagon['angle'], hexagon['color'], mode=draw_mode,
                         texture=hexagon.get('texture'))

        pygame.display.flip()
        pygame.time.wait(10)

    pygame.quit()


if __name__ == "__main__":
    main()
