import turtle
import tkinter as tk

my_turtle = turtle.Turtle()#タートルを生成
screen = turtle.Screen()#スクリーンを取得
screen.setup(800,800)#スクリーンのサイズを設定(幅,高さ)
screen.title("タートル")#ウィンドウのタイトルを設定
my_turtle.shape("turtle")#タートルの形を設定(亀のアイコン)
my_turtle.pensize(5)#ペンの太さを設定
#my_turtle.hideturtle()#アイコンを隠す

for i in range(4):
	my_turtle.forward(100)#前方へ100ピクセル進む
	my_turtle.left(90)#左に90度回転
	my_turtle.forward(100)
	my_turtle.right(90)#右に90度回転
	my_turtle.forward(100)
	my_turtle.left(90)
my_turtle.back(200)
screen.mainloop()#イベントループして入力待ちになるメソッド
