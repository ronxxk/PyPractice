import turtle as turtle_module
import random
# import colorgram
# rgb_ = []

# color_img = colorgram.extract('hirst spot painting/image.jpg', 30)

# for i in color_img:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_.append(new_color)
    
# print(rgb_)


turtle_module.colormode(255)
jermy = turtle_module.Turtle()
jermy.speed("fastest")
jermy.penup()
jermy.hideturtle()
color_list = [(202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
jermy.setheading(225)
jermy.forward(300)
jermy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    jermy.dot(20, random.choice(color_list))
    jermy.forward(50)

    if dot_count % 10 == 0:
        jermy.setheading(90)
        jermy.forward(50)
        jermy.setheading(180)
        jermy.forward(500)
        jermy.setheading(0)



