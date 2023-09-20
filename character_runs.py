from pico2d import *
import math
open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

x = 300
y = 150
angle = 0

while 1:
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)
    x = x + math.cos(angle) * 200
    y = y + math.sin(angle) * 200
    angle = angle + 1
    delay(0.1)
close_canvas()  
