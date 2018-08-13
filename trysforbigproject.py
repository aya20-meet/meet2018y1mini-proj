import turtle

turtle.tracer(1,0)
##river drawing
turtle.penup()
turtle.goto(0, 210)
turtle.pendown()
turtle.goto(1000,210)
turtle.goto(-1000,210)
turtle.penup()
turtle.goto(-1000, -210)
turtle.pendown()
turtle.goto(1000,-210)

turtle.tracer(1,.5)
##logs
pos_list = []
stamp_list = []
turtle.shape('square')
START_LENGTH = 10
SQUARE_SIZE = 20
turtle.shapesize(3)


turtle.penup()
log1 = turtle.clone()
log2 = turtle.clone()
log3 = turtle.clone()
#log4 = turtle.clone()
logs_list = [log1, log2, log3]#, log4]
log1.goto(900, 100)
log2.goto(900, -0)
log3.goto(900, -100)
#log4.goto(900, -210)



TIME_STEP = 100

for i  in range(START_LENGTH):
    for log in logs_list:
        x_pos,y_pos=log.pos()
            

        my_pos=(x_pos-SQUARE_SIZE,y_pos) 
        log.goto(my_pos) 
   
   
        pos_list.append(my_pos) 

                
        my_stamp = log.stamp()
        stamp_list.append(my_stamp)
        
   

def move_logs():
    for log in logs_list:
        x_pos, y_pos = log.pos()
        log.goto(x_pos - SQUARE_SIZE, y_pos)
        my_pos=log.pos() 
        pos_list.append(my_pos)

        #print(stamp_list)
        new_stamp = log.stamp()
        stamp_list.append(new_stamp)
        old_stamp = stamp_list.pop(0)
        log.clearstamp(old_stamp)
        pos_list.pop(0)
        log.hideturtle()
        
    turtle.ontimer(move_logs,TIME_STEP)
    
    
move_logs()
turtle.mainloop()

