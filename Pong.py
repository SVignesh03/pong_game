import turtle
import winsound
# from playsound import playsound

w = turtle.Screen()
w.title("Pong game")
w.bgcolor("black")
w.setup(width = 800, height = 600)
w.tracer(0)

# playsound('Wall_Bounce.mp3')

s1 = 0
s2 = 0

#paddle A


pa = turtle.Turtle()
pa.speed(0)
pa.shape("square")
pa.shapesize(stretch_wid = 5, stretch_len = 1)
pa.color("yellow")
pa.penup()
pa.goto(-350, 0)


#paddle B


pb = turtle.Turtle()
pb.speed(0)
pb.shape("square")
pb.shapesize(stretch_wid = 5, stretch_len = 1)
pb.color("yellow")
pb.penup()
pb.goto(350, 0)



#Ball

b = turtle.Turtle()
b.speed(0)
b.shape("circle")
b.color("red")
b.penup()
b.goto(0, 0)
b.dx = 0.5
b.dy = 0.5

s = turtle.Turtle()
s.speed(0)
s.color("White")
s.penup()
s.hideturtle()
s.goto(0, 260)
s.write("Player 1 : 0          Player 2 : 0", align = "center", font = ("Comic Sans MS", 24, "bold"))


def pa_up():
    y = pa.ycor()
    y = y + 20
    pa.sety(y)
    
def pa_down():
    y = pa.ycor()
    y = y - 20
    pa.sety(y)
    
def pb_up():
    y = pb.ycor()
    y = y + 20
    pb.sety(y)
    
def pb_down():
    y = pb.ycor()
    y = y - 20
    pb.sety(y)
    
def restart():
    s1 = 0
    s2 = 0
    s.clear()
    s.goto(0, 260)
    s.write("Player 1 : {}          Player 2 : {}".format(s1, s2), align = "center", font = ("Comic Sans MS", 24, "bold"))
    

w.listen()
w.onkeypress(pa_up, "w")
w.onkeypress(pa_down, "s")
w.onkeypress(pb_up, "Up")
w.onkeypress(pb_down, "Down")

while True:
    w.update()
    
    
    b.setx(b.xcor() + b.dx)
    b.sety(b.ycor() + b.dy)
    
    
    
    if b.ycor() > 290 :
        b.sety(290)
        b.dy = b.dy * -1
        winsound.PlaySound("D:\\Python Pong Game\\Wall_Bounce.mp3", winsound.SND_ASYNC)
        
    if b.ycor() < -290 :
        b.sety(-290)
        b.dy = b.dy * -1
        winsound.PlaySound("D:\\Python Pong Game\\Wall_Bounce.mp3", winsound.SND_ASYNC)
    
    if b.xcor() > 390 :
        b.goto(0, 0)
        b.dx *= -1
        s1 += 1
        s.clear()
        s.write("Player 1 : {}          Player 2 : {}".format(s1, s2), align = "center", font = ("Comic Sans MS", 24, "bold"))
        winsound.PlaySound("D:\\Python Pong Game\\Ball_Miss.mp3", winsound.SND_ASYNC)

    if b.xcor() < -390 :
        b.goto(0, 0)
        b.dx *= -1
        s2 += 1
        s.clear()
        s.write("Player 1 : {}          Player 2 : {}".format(s1, s2), align = "center", font = ("Comic Sans MS", 24, "bold"))
        winsound.PlaySound("D:\\Python Pong Game\\Ball_Miss.mp3", winsound.SND_ASYNC)
    
    if (b.xcor() > 340 and b.xcor() < 350) and (b.ycor() < pb.ycor() + 40 and b.ycor() > pb.ycor() - 40) :
        b.setx(340)
        b.dx *= -1
        winsound.PlaySound("D:\\Python Pong Game\\Paddle_Bounce.mp3", winsound.SND_ASYNC)
        
    if (b.xcor() < -340 and b.xcor() > -350) and (b.ycor() < pa.ycor() + 40 and b.ycor() > pa.ycor() - 40) :
        b.setx(-340)
        b.dx *= -1
        winsound.PlaySound("D:\\Python Pong Game\\Paddle_Bounce.mp3", winsound.SND_ASYNC)
        
    if s1 >= 10 :
        s.clear()
        s.goto(0, 0)
        s.write("Player 1 Wins", align = "center", font = ("Impact Regular", 32, "bold"))
        
    if s2 >= 10 :
        s.clear()
        s.goto(0, 0)
        s.write("Player 2 Wins", align = "center", font = ("Impact Regular", 32, "bold"))