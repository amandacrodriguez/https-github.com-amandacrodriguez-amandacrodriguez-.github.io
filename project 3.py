'''
Amanda Rodriguez
Project 3: Refactored Stadium Scene
Improvements made: Decomposed the large draw_scene function into reusable helper 
functions (draw_sun, draw_megaphone, draw_mat). Added parameters for position 
and size to eliminate hardcoded values, allowing for a more populated stadium 
scene with multiple cheer mats and megaphones.
'''
import turtle
import math

def draw_rectangle(t, width, height, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_square(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(4):
        t.forward(size)
        t.right(90)
    if fill_color:
        t.end_fill()

def draw_triangle(t, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    for _ in range(3):
        t.forward(size)
        t.left(120)
    if fill_color:
        t.end_fill()

def draw_circle(t, radius, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    t.circle(radius)
    if fill_color:
        t.end_fill()

def draw_polygon(t, sides, size, fill_color=None):
    if fill_color:
        t.fillcolor(fill_color)
        t.begin_fill()
    angle = 360 / sides
    for _ in range(sides):
        t.forward(size)
        t.right(angle)
    if fill_color:
        t.end_fill()

def jump_to(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def setup_turtle():
    t = turtle.Turtle()
    t.speed(0)
    screen = turtle.Screen()
    screen.title("Project 3: Refactored Scene")
    return t, screen

def draw_sun(t, x, y, size):
    jump_to(t, x, y)
    draw_circle(t, size, "yellow")

def draw_stadium_field(t):
    jump_to(t, -400, -50)
    draw_rectangle(t, 800, 250, "forestgreen")

def draw_cheer_mat(t, x, y, size, color):
    jump_to(t, x, y)
    draw_square(t, size, color)

def draw_megaphone(t, x, y, size):
    jump_to(t, x, y)
    draw_triangle(t, size, "white")


def draw_scene(t):
   
    screen = t.getscreen()
    screen.bgcolor("skyblue")
    
    # 1. Grass
    draw_stadium_field(t)
    
    # 2. Sun (Original position: 200, 150)
    draw_sun(t, 200, 150, 40)
    
    # 3. Mat (Original position: -50, -150)
    draw_cheer_mat(t, -50, -150, 100, "darkblue")
    
    # 4. Megaphone (Original position: -25, -150)
    draw_megaphone(t, -25, -150, 50)

def draw_enhanced_scene(t):
    
    draw_scene(t)
    
    draw_cheer_mat(t, 100, -150, 100, "darkgreen") 
    
    draw_megaphone(t, 125, -150, 50)
    draw_megaphone(t, -300, -100, 30) 
    
    draw_sun(t, -250, 200, 20)

def main():
    t, screen = setup_turtle()
    
    draw_scene(t)
    
    t.screen.ontimer(lambda: (t.clear(), draw_enhanced_scene(t)), 2000)
    
    screen.mainloop()

if __name__ == "__main__":
    main()