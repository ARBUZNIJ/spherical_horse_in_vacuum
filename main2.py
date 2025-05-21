from ursina import *
import math

app = Ursina()

mirror_shader = Shader.load(Shader.GLSL, vertex='mirror_shader.glsl', fragment='mirror_shader.glsl')

camera.position = Vec3(-5, 4, 10)
camera.look_at(Vec3(1.25, 1, 0))
camera.shadows = True

# Пол
ground = Entity(
    model='plane',
    scale=20,
    color=color.gray,
    position=(0, -1, 0),
    receive_shadows=True
)

# Правая стена
right_wall =Entity(
    model='cube',
    scale=20,
    color=color.azure,
    position=(14, 2, 0),
    receive_shadows=True
)

# Задняя стена
back_wall = Entity(
    model='cube',
    scale=(20, 6, 0.2),
    color=color.brown,
    position=(0, 2, -5),
    receive_shadows=True
)

ellips = Entity(
    model='sphere',
    texture='metal',  # Текстура для отражения
    scale=(2, 1, 1),
    position=(0, 1, 0),
    cast_shadows=True,
    shader=mirror_shader  # Применяем шейдер
)

light = DirectionalLight()
light.shadow = True
light.casts_shadows = True
light.frustum_size = 30
light.shadow_color = Vec4(0, 0, 0, 1)
light.look_at(Vec3(0, -1, 0))

light_visual = Entity(
    model='sphere',
    color=color.yellow,
    scale=0.5,
    position=Vec3(0, 5, 10),
    unlit=True
)

angle = 0

def update_light_position():
    global angle
    radius = 8
    height = 6
    x = radius * math.cos(math.radians(angle))
    z = radius * math.sin(math.radians(angle))
    y = height
    pos = Vec3(x, y, z)
    light.position = pos
    light.look_at(Vec3(0, 0, 0))
    light_visual.position = pos
    angle += time.dt * 20
    if angle > 360:
        angle = 0

t = 0

def update():
    global t

    x = 1.02 * math.sin(t)
    y = 1 + 0.5 * math.sin(2 * t)
    ellips.position = Vec3(x, y, 0)

    ellips.rotation_y += time.dt * 30

    t += time.dt * 2
    if t > 2 * math.pi:
        t -= 2 * math.pi

    update_light_position()

app.run()