# Name: Amanda Rodriguez
# Date: April 8, 2026
# Description: A turtle scene that draws a sun and a conditional geometric shape.

from turtle import *

# 1. Background: Setting a sky blue background
bgcolor("skyblue") 

# 2. Variables: Meaningfully named values for the sun
sun_radius = 40 
sun_color = "yellow"
shape_size = 120 # Added a variable to control the triangle size

# Drawing the Sun
penup()
goto(-150, 100)  
pendown()
fillcolor(sun_color)
begin_fill()
circle(sun_radius)
end_fill()

# 3. Conditionals: Change pen color based on the size of the shape
if shape_size > 100:
    pencolor("darkgreen")
else:
    pencolor("red")

pensize(3)

# 4. Loops: Drawing a triangle using a for loop
penup()
goto(0, 0)
pendown()

for i in range(3):
    forward(shape_size)
    left(120)

# 5. Comments: Explaining the final step
# Keep the window open until it is manually closed
done()
