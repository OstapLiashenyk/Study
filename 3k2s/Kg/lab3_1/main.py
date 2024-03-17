import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
import json
import sys

# JSON з радіусом 5 та іншими параметрами
json_data = '''
{
  "radius": 5,
  "rotation_axis": [1, 0, 0],
  "initial_position": [0.0, 0.0, -40.0],
  "perspective": {
    "fov": 45,
    "aspect_ratio": 1.333,
    "z_near": 0.1,
    "z_far": 50.0
  }
}
'''

data = json.loads(json_data)

def setup_lighting(lighting_enabled):
    if lighting_enabled:
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glLightfv(GL_LIGHT0, GL_POSITION, (1, 1, 1, 0))
        glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1))
        glLightfv(GL_LIGHT0, GL_DIFFUSE, (0, 1, 0, 1))  # Зелене світло для демонстрації
    else:
        glDisable(GL_LIGHTING)


def draw_3d_hexagon(radius, rotation_axis, depth_buffer_enabled):
    glColor3f(0.5, 0.5, 1) if depth_buffer_enabled else glColor3f(0.5, 0.5, 0.5)
    for angle in range(0, 360, 10):
        glPushMatrix()
        glRotatef(angle, *rotation_axis)
        draw_hexagon(radius, depth_buffer_enabled)
        glPopMatrix()

def draw_hexagon(radius, mode):
    if mode == 'wireframe':
        glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    else:
        glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

    glBegin(GL_POLYGON)
    for i in range(6):
        angle = 2 * math.pi / 6 * i
        glVertex3f(math.cos(angle) * radius, math.sin(angle) * radius, 0)
    glEnd()

# Оновлення головної функції
def main():
    # Ініціалізація та налаштування...
    mode = 'normal'  # Можливі режими: 'normal', 'wireframe', 'normals', 'texture'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    mode = 'wireframe' if mode != 'wireframe' else 'normal'
                elif event.key == pygame.K_d:
                    # Тут міг би бути код для відображення нормалей
                    pass
                elif event.key == pygame.K_f:
                    # Тут міг би бути код для активації текстур
                    pass

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        draw_hexagon(data['radius'], mode)  # Передаємо режим як параметр
        pygame.display.flip()
        pygame.time.wait(10)

main()
