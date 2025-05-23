import turtle
import random
screen= turtle.Screen()
screen.screensize(500,500)
screen.bgcolor("paleturquoise")


t=turtle.Turtle()
t.speed(0)

#grass
t.penup()
t.goto(-5000,-100)
t.pendown()
t.fillcolor("yellowgreen")
t.begin_fill()
t.penup()
t.goto(5000,-100)
t.pendown()
t.penup()
t.goto(5000,-5000)
t.pendown()
t.penup()
t.goto(-5000,-5000)
t.pendown()
t.penup()
t.goto(-5000,-100)
t.pendown()
t.end_fill()

#writting
t.penup()

t.goto(0, 330)
t.pendown()
t.write("Happy Spring!", font=("times new roman", 35, "bold"), align="center")

#object1 done sun
circle = turtle.Turtle()
circle.speed(5)
circle.color("yellow")
circle.penup()
circle.goto(200, 160)
circle.pendown()

circle.begin_fill()
circle.circle(50)
circle.end_fill()





#object2  done flower
t.pencolor('green')
t.penup()
t.goto(-100,-110)
t.pendown()
t.pensize(7)
t.goto(-110,-10)
t.penup()
t.goto(-110,28)
t.pendown()
t.pencolor('pink')
t.fillcolor('pink')
for i in range(6):
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.right(60)
    t.pendown()
t.penup()
t.goto(-100,-10)
t.pendown()
t.pencolor('yellow')
t.fillcolor('yellow')
t.begin_fill()
t.circle(20)
t.end_fill()






#object3 snake done

squ= turtle.Turtle()
squ.pensize(25)
squ.color('dark green')
squ.penup()
squ.goto(-390,-290)
squ.pendown()
for i in range(20):
    squ.setheading(random.randint(-30,30))
    squ.forward(random.randint(5,15))








#object4 cloud done
t = turtle.Turtle()
t.speed(0)
t.hideturtle()

t.color("white", "white")
t.penup()
t.goto(-200, 200)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-150, 230)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-100, 200)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()

t.penup()
t.goto(-150, 170)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()


t.penup()
t.goto(-200, 140)
t.pendown()
t.begin_fill()
t.circle(50)
t.end_fill()






#object5
bird = turtle.Turtle()
bird.hideturtle()
bird.speed(3)
bird.color("black")

bird.penup()
bird.goto(100, 200)
bird.pendown()

bird.setheading(60)
bird.forward(20)
bird.setheading(-60)
bird.forward(20)

bird.penup()
bird.goto(280, 200)
bird.pendown()
bird.setheading(60)
bird.forward(20)
bird.setheading(-60)
bird.forward(20)

bird.penup()
bird.goto(310, 200)
bird.pendown()
bird.setheading(60)
bird.forward(20)
bird.setheading(-60)
bird.forward(20)





#object6
t.pencolor('brown')
t.penup()
t.goto(100,-140)
t.pendown()
t.pensize(20)
t.goto(100,-10)
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor('green')
t.fillcolor('green')
for i in range(6):
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.right(60)
    t.pendown()
t.penup()
t.goto(110,-10)
t.pendown()
t.pencolor("green")
t.fillcolor('green')
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(80,15)
t.pendown()
t.pencolor('green')
t.fillcolor('green')
for i in range(7):
    t.begin_fill()
    t.circle(25)
    t.end_fill()
    t.penup()
    t.forward(20)
    t.right(60)
    t.pendown()




#object7

balloon = turtle.Turtle()
balloon.shape("turtle")
balloon.speed(5)

balloon.penup()
balloon.goto(0, 250)
balloon.pendown()
balloon.begin_fill()
balloon.color("red")
balloon.circle(25)
balloon.end_fill()

balloon.penup()
balloon.goto(0, 300)
balloon.setheading(-90)
balloon.pendown()
balloon.width(2)
balloon.forward(100)
balloon.hideturtle()

#object8
spider = turtle.Turtle()
spider.shape("turtle")
spider.color("black")
spider.speed(5)

spider.penup()
spider.goto(-200, -200)
spider.pendown()
spider.begin_fill()
spider.circle(20)
spider.end_fill()

spider.penup()
spider.goto(-200, -160)
spider.begin_fill()
spider.circle(10)
spider.end_fill()


spider.penup()
spider.goto(-200, -180)
spider.setheading(0)
spider.pendown()
for _ in range(4):
    spider.forward(50)
    spider.backward(50)
    spider.right(45)
    spider.forward(50)
    spider.backward(50)
    spider.left(90)


















turtle.done()