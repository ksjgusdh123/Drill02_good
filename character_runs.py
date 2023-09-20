from pico2d import *
import math
open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def run_circle():
    print("CIRCLE")
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400, 90)
    delay(1)
    pass

def run_rectangle():
    print("RECTANGLE")
    pass

while True:
    run_circle()
    run_rectangle()
    break

close_canvas()  
