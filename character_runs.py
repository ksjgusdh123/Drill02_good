from pico2d import *
import math
open_canvas()

# fill here
grass = load_image('grass.png')
character = load_image('character.png')

def render_all(x, y):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x, y)
    delay(0.01)    


def run_circle():
    print("CIRCLE")
    
    cx, cy, r = 800 / 2, 600 / 2, 200
    for dig in range(0,360, 5):
        x = cx + r * math.cos(dig / 360 * 2 * math.pi)
        y = cy + r * math.sin(dig / 360 * 2 * math.pi)
        render_all(x,y)
        

def run_rectangle():
    print("RECTANGLE")

    # bottom line
  #  for x in range(50, 750+1, 10):
  #     render_all(x,90)

    for x in range(750, 50, -10):
       render_all(x,550)
    pass

while True:
    #run_circle()
    run_rectangle()
    break

close_canvas()  
