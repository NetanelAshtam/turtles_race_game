from turtle import Turtle,Screen
import random

colors = ['red','blue','yellow','purple','orange','green']
names = ['netanel','tsuri','stas','irit','feli','andrei']
names_color = dict(zip(colors,names))
is_race_on = False



screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title='make your bet',prompt='Which turtle will win the race? choose name:')

#netanel = Turtle(shape='turtle')
#netanel.penup()
#netanel.goto(x=-230,y= -100)
y = -100
for index in range(0,6):
    names[index] = Turtle(shape='turtle')
    names[index].color(colors[index])
    names[index].penup()
    names[index].goto(x=-230,y= y)
    y += 40


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in names:
        if turtle.xcor()>230:
            winning_name = names_color[turtle.pencolor()]
            is_race_on = False
            print(f'The winner is {names_color[turtle.pencolor()]} turtle')
            if winning_name == user_bet:
                print('You win!!')
            else: 
                print ('You lose!!')

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)








screen.exitonclick()