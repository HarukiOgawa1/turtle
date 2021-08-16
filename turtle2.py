import turtle
import tkinter as tk

my_turtle = turtle.Turtle()
screen = turtle.Screen()
screen.setup(800,800)
screen.title("タートル")
my_turtle.shape("turtle")
my_turtle.pensize(5)#ペンの太さを設定
my_turtle.pencolor("green")#ペンの色を緑
my_turtle.fillcolor("red")#塗りの色を赤
#screen.bgcolor("yellow")#スクリーンの背景色

my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.begin_fill()#塗り開始
my_turtle.right(60)
my_turtle.forward(150)
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.end_fill()#塗り終了
my_turtle.left(90)
my_turtle.forward(150)
my_turtle.penup()#ペンを上げる
my_turtle.forward(200)
my_turtle.pendown()#ペンを下げる
my_turtle.forward(150)
my_turtle.circle(200)#円を描く
screen.mainloop()