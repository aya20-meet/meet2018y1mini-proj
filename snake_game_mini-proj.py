# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""
import turtle
import random
#color = input('Choose your color ')
#turtle.bgcolor(color)
'''milly = turtle.clone()
milly.penup()
milly.goto(0, 350)
milly.pendown()
milly.goto(350,350)
milly.goto(-350,350)
milly.goto(-350,-350)
milly.goto(350,-350)
milly.goto(350,350)

milly.penup()
milly.goto(-80, 400)
milly.pendown()
milly.write('SNAKE GAME!' ,font=('Ariel', 18, 'normal'))'''



#

                      
turtle.tracer(1,0) 

SIZE_X=1000
SIZE_Y=1000
SIZE_Z=670
SIZE_C=670
turtle.setup(SIZE_X, SIZE_Y) 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

scorev = 0
milly = turtle.clone()
milly.penup()
milly.goto(0, 350)
milly.pendown()
milly.goto(350,350)
milly.goto(-350,350)
milly.goto(-350,-350)
milly.goto(350,-350)
milly.goto(350,350)

milly.penup()
milly.goto(-80, 400)
milly.pendown()
milly.write('SNAKE GAME!' ,font=('David', 18, 'normal'))

def score(positionscore):
    turtle.undo()
    global scorev
    turtle.goto(positionscore)
    scorev += 1
    turtle.hideturtle()
    turtle.write(scorev, font=("Arial", 16, "normal"))
    

#turtle.bgcolor(color)


pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
turtle.hideturtle()

turtle.register_shape('ted15game.gif')


snake = turtle.clone()
#snake.shape('ted15game.gif')
snake.shape('square')


#turtle.hideturtle()


for i  in range(START_LENGTH):
    x_pos=snake.pos()[0] 
    y_pos=snake.pos()[1]

    
    x_pos+=SQUARE_SIZE

    my_pos=(x_pos,y_pos) 
    snake.goto(x_pos,y_pos) 
   
   
    pos_list.append(my_pos) 

                
    my_stamp = snake.stamp()
    stamp_list.append(my_stamp)


UP_ARROW = "Up" 
LEFT_ARROW = "Left" 
DOWN_ARROW = "Down" 
RIGHT_ARROW = "Right" 
TIME_STEP = 100 
SPACEBAR = "space"

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3



direction = UP
UP_EDGE = 340
DOWN_EDGE = -340
RIGHT_EDGE = 340
LEFT_EDGE = -340


 

def up():
    global direction 
    direction=UP 
    print("You pressed the up key!")

def down():
    global direction
    direction=DOWN
    print('you pressed the down key')

def left():
    global direction
    direction=LEFT
    print('you pressed the left key')

def right():
    global direction
    direction=RIGHT
    print('you pressed the right key')

turtle.onkeypress(up, UP_ARROW)
turtle.onkeypress(down, DOWN_ARROW)
turtle.onkeypress(left, LEFT_ARROW)
turtle.onkeypress(right, RIGHT_ARROW)





turtle.listen()

def make_food():
    min_x=-int(SIZE_Z/2/SQUARE_SIZE)+1
    max_x=int(SIZE_Z/2/SQUARE_SIZE)-1
    min_y=-int(SIZE_C/2/SQUARE_SIZE)-1
    max_y=int(SIZE_C/2/SQUARE_SIZE)+1
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food_ran_pos = (food_x, food_y)
    food.goto(food_x, food_y)
    food_pos.append(food_ran_pos)
    food_stamps.append(food.stamp())

      
def move_snake():
    global food_stamps, food_pos
    if len(food_stamps)<=6:
        make_food()        
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print('you moved up')

    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print('you moved down')

    elif direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")

    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]

    if new_x_pos >= RIGHT_EDGE:
        print('you hit the right edge!')
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print('you hit the left edge!')
        quit()
    elif new_y_pos >= UP_EDGE:
        print('you hit the up edge!')
        quit()
    elif new_y_pos <= DOWN_EDGE:
        print('you print the down edge!')
        quit()
    elif pos_list[-1] in pos_list[:-1]:
        print('you hited yourself')
        quit()
           
    

    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
   
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) 
        food.clearstamp(food_stamps[food_ind])
        score((0, -400))
                                              
        food_pos.pop(food_ind) 
        food_stamps.pop(food_ind) 
        print('You have eaten the food!')
    else:
        old_stamp = stamp_list.pop(0)
        snake.clearstamp(old_stamp)
        pos_list.pop(0)
        
  
    
    turtle.ontimer(move_snake,TIME_STEP) 
    
#turtle.register_shape('tedsnakegamefireball.gif')
turtle.register_shape('trash.gif')
food = turtle.clone()
#food.shape('tedsnakegamefireball.gif')
food.shape('trash.gif')
food_pos = [(100,100), (-100,100), (-100,-100), (100,-100)]
food_stamps = []
for this_food_pos in food_pos :
    food.goto(this_food_pos[0],this_food_pos[1])
    food_stamps.append(food.stamp())







move_snake()
