import turtle
import random
import time
from winsound import SND_NOWAIT

#important variables required
time_slot=0.1
score=0
highest_score=0
snake_body=[]

# game screen window setup
sck=turtle.Screen()
sck.title("Snake Game")
sck.bgcolor("aquamarine")
sck.setup(width=600,height=600)

# making head of the snake
snake_head=turtle.Turtle()
snake_head.speed(0)
snake_head.shape("square")
snake_head.color("white")
snake_head.fillcolor("indigo")
snake_head.penup()
snake_head.goto(0,0)
snake_head.direction="stop"


#creating food for the snake
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("yellow")
food.fillcolor("green")
food.penup()
food.ht()    
food.goto(0,200)
food.st()


#creating score board for the game
score_board=turtle.Turtle()
score_board.shape("square")
score_board.fillcolor("grey")
score_board.penup()
score_board.ht()
score_board.goto(-250,-250)
score_board.write("Score:0 |  Highest Score: 0")


#moving the snake in all direction
def moveup():
    if snake_head.direction !="down":  # down moving snake cannot move directly in the up
        snake_head.direction="up"
       
def movedown():
    if snake_head.direction !="up":
        snake_head.direction="down"
        
def moveleft():
    if snake_head.direction !="right":
        snake_head.direction="left"
        
def moveright():
    if snake_head.direction !="left":
        snake_head.direction="right"

def movestop():
    snake_head.direction="Stop"


# changing the coordinates of the snake when it moves in differnt directions
# assuming that the whole game window is divided in four quadrants
def move():
    if snake_head.direction=="up":
        y_coordinate=snake_head.ycor()    
        snake_head.sety(y_coordinate+20)  # snake moving in upward direction @y_coordinate value increase moving upward
    if snake_head.direction=="down":
        y_coordinate=snake_head.ycor()
        snake_head.sety(y_coordinate-20) # snake moving in downward direction @y_coordinate value decreases
    if snake_head.direction=="right":
        x_coordinate=snake_head.xcor()
        snake_head.setx(x_coordinate+20) # moving right increases x_coordinate value
    if snake_head.direction=="left":
        x_coordinate=snake_head.xcor()
        snake_head.setx(x_coordinate-20)  # moving left decreses the x_coordinate value

# key mapping
sck.listen()
sck.onkey(moveup,"Up")
sck.onkey(movedown,"Down")
sck.onkey(moveleft,"Left")
sck.onkey(moveright,"Right")
sck.onkey(movestop,"space")

# developing the main logic for the game
while True:
    sck.update()
    """If the snake collide with the window then the snake started appearing from its
    opposite direction: 1)if goes from Top then return from Bottom. 2) If goes from 
    Bottom then return from the Top. 3) If goes from Left then return from Right.
    4) If goes from Right then return from the Left."""
    if snake_head.xcor()>290:
        snake_head.setx(-290)
    if snake_head.xcor()<-290:
        snake_head.setx(290)
    if snake_head.ycor()>290:
        snake_head.sety(-290)
    if snake_head.ycor()<-290:
        snake_head.sety(290)
    
    """If the food food collide with the head of snake then the food get added to the 
    body of the snake and the food is generated to some random space on the game screen"""
    if snake_head.distance(food)<20:
        x_coordinate=random.randint(-290,290)
        y_coordinate=random.randint(-290,290)
        food.goto(x_coordinate,y_coordinate)
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape("square")
        body.color("red")
        body.fillcolor("black")
        snake_body.append(body) # appending the eaten food to the body of the snake
        # as the snake eat the food the score increases
        score+=10
        # at every time we are decreasing the delay time
        time_slot-=0.001
        """comparing the current score with the highest score. If current score become
         greater than the highest score set the highest score to current score """ 
        if score>highest_score:
            highest_score=score
        score_board.clear()
        score_board.write("Score: {} Highest Score: {}".format(score,highest_score))
       
        """moving the snake on the screen.
        This snake means moving the each turtle to its ahead position.  """ 
    for i in range(len(snake_body)-1,0,-1):
        x_coordinate=snake_body[i-1].xcor()
        y_coordinate=snake_body[i-1].ycor()
        snake_body[i].goto(x_coordinate,y_coordinate)
    if len(snake_body)>0:
        x_coordinate=snake_head.xcor()
        y_coordinate=snake_head.ycor()
        snake_body[0].goto(x_coordinate,y_coordinate)
    move()  # calling the move function 
    
    """ This is to check the collision of the snake with its body. If the snake gets 
    collide with its body the game terminates and the score is set to zero again with 
    clearing the screen """
    for body in snake_body:
        if body.distance(snake_head)<20:
            time.sleep(1) #
            snake_head.goto(0,0)
            snake_head.direction="stop"
            #
            for body in snake_body:
                body.ht()
            snake_body.clear()
            score=0
            time_slot=0.1
            #
            score_board.clear()
            score_board.write("Score: {}  Highest Score: {}".format(score,highest_score))
    time.sleep(time_slot)
sck.mainloop()