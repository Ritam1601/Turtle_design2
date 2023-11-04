import turtle as t
import colorsys as c
t.bgcolor('black')
t.speed('fastest')
t.pensize(2)
t.hideturtle()
for j in range(20):
	for k in range(15):
		for i in range(2):
			t.color(c.hsv_to_rgb(1/(j+1),1/(i+1),1))
			t.circle(250-j*4,90)
			t.lt(90)
		t.circle(0,24)
t.exitonclick()