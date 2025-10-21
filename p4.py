# ###############################################
# ### SETUP ###
import turtle
turtle.Screen().bgcolor("pink")
# ###############################################
#this starts the drawing 
t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-100, -100)
t.color("pink")
t.pendown()
#pendown makes it stop drawing

# I love these colors 
colors = ["blue", "cyan", "purple"]
for i in range(400):
    t.color( colors[i % 3])
    t.forward(75 + i)
    t.left(47)
# the speed was very slow so, i sped it up and made it 10





# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
