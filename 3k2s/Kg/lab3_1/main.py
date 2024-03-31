import glfw
from OpenGL.GL import *
from OpenGL.GLU import gluPerspective, gluLookAt
import numpy as np
import math


def hexagon_prism_vertices(radius, height):
    vertices = []
    for i in range(6):
        angle = 2 * math.pi * i / 6
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vertices.append([x, y, -height / 2])  # Нижній шестикутник
        vertices.append([x, y, height / 2])  # Верхній шестикутник
    return np.array(vertices, dtype=np.float32)


def draw_hexagon_prism(vertices):
    glBegin(GL_TRIANGLE_FAN)
    for i in range(1, 12, 2):
        glVertex3fv(vertices[i])
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    for i in range(0, 12, 2):
        glVertex3fv(vertices[i])
    glEnd()

    glBegin(GL_QUADS)
    for i in range(0, 12, 2):
        glVertex3fv(vertices[i])
        glVertex3fv(vertices[(i + 2) % 12])
        glVertex3fv(vertices[(i + 3) % 12])
        glVertex3fv(vertices[(i + 1) % 12])
    glEnd()


# Стан відображення
depth_test_enabled = True
lighting_enabled = True
wireframe_enabled = False

# Параметри обертання
mouse_down = False
last_pos = (0, 0)
rotation = [20, -20]


def mouse_button_callback(window, button, action, mods):
    global mouse_down
    if button == glfw.MOUSE_BUTTON_LEFT and action == glfw.PRESS:
        mouse_down = True
    elif button == glfw.MOUSE_BUTTON_LEFT and action == glfw.RELEASE:
        mouse_down = False


def cursor_position_callback(window, xpos, ypos):
    global last_pos, rotation, mouse_down
    if mouse_down:
        dx = xpos - last_pos[0]
        dy = ypos - last_pos[1]
        rotation[0] += dy * 0.5
        rotation[1] += dx * 0.5
    last_pos = (xpos, ypos)


def key_callback(window, key, scancode, action, mods):
    global depth_test_enabled, lighting_enabled, wireframe_enabled
    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_A:
            depth_test_enabled = not depth_test_enabled
            glEnable(GL_DEPTH_TEST) if depth_test_enabled else glDisable(GL_DEPTH_TEST)
        elif key == glfw.KEY_C:
            lighting_enabled = not lighting_enabled
            glEnable(GL_LIGHTING) if lighting_enabled else glDisable(GL_LIGHTING)
        elif key == glfw.KEY_Q:
            wireframe_enabled = not wireframe_enabled


def main():
    if not glfw.init():
        return

    window = glfw.create_window(640, 480, "3D Hexagon Prism", None, None)
    if not window:
        glfw.terminate()
        return

    glfw.make_context_current(window)
    glfw.set_mouse_button_callback(window, mouse_button_callback)
    glfw.set_cursor_pos_callback(window, cursor_position_callback)
    glfw.set_key_callback(window, key_callback)

    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, [1, 1, 1, 0])
    glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

    hexagon_vertices = hexagon_prism_vertices(5, 5)

    while not glfw.window_should_close(window):
        glfw.poll_events()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(45, (640 / 480), 0.1, 50.0)

        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0, 0, -20, 0, 0, 0, 0, 1, 0)

        glRotatef(rotation[0], 1, 0, 0)
        glRotatef(rotation[1], 0, 1, 0)

        if wireframe_enabled:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

        draw_hexagon_prism(hexagon_vertices)

        glfw.swap_buffers(window)

    glfw.terminate()


if __name__ == "__main__":
    main()
