import turtle
import tkinter as tk

my_turtle = turtle.Turtle()#タートルを生成
screen = turtle.Screen()#スクリーンを取得
screen.setup(800,800)#スクリーンのサイズを設定(幅,高さ)
screen.title("タートル")#ウィンドウのタイトルを設定
my_turtle.shape("turtle")#タートルの形を設定(亀のアイコン)
my_turtle.pensize(5)#ペンの太さを設定
my_turtle.color("green")
my_turtle.speed(10)

def draw_line(x, y):
    my_turtle.ondrag(None)
    screen.onscreenclick(None)
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.setpos(x, y)
    my_turtle.ondrag(draw_line)
    screen.onscreenclick(move_turtle)

def move_turtle(x, y):
    my_turtle.ondrag(None)
    my_turtle.penup()
    my_turtle.setheading(my_turtle.towards(x, y))
    my_turtle.goto(x, y)
    my_turtle.pendown()
    my_turtle.ondrag(draw_line)
    screen.onscreenclick(move_turtle)

my_turtle.ondrag(draw_line)
screen.onscreenclick(move_turtle)
screen.mainloop()