import turtle


wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("black")                # background colour
wn.title("Robotic Navigation Program") #title of the window
wn.setup(500,350)                  # the dimensions of the window

# class for the maze
class Maze(turtle.Turtle):              
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("white")        # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# class for the end goals
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square") #turtle shape
        self.color("green")  #colour of the turtle
        self.penup()        #lift the pen up so it do not leave the trail
        self.speed(0)

#class for the search algorithm 
class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")    #turtle shape
        self.color("blue")      #colour of the turtle
        self.penup()            #lift the pen up so it do not leave the trail
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")        #turtle shape
        self.color("yellow")       #colour of the turtle
        self.penup()             #lift the pen up so it do not leave the trail
        self.speed(0)

# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")    #turtle shape
        self.color("red")       #colour of the turtle
        self.penup()            #lift the pen up so it do not leave the trail
        self.speed(0)


#Initialise the variables 
maze = Maze()
red = Red()
yellow = Yellow()
blue = Blue()
green = Green()
mazeout = []

#To draw the wall around the maze
def setup_maze(X, Y):   
  for x in range (-1, (X+1)):
    for y in range (-1, (Y+1)):
      if((x== -1) or (x == X) or (y == -1) or (y == Y)):
        mazeout.append((x, y))
        #screen locations of each cell of the maze
        screen_x = -120 + (x * 24)         
        screen_y = 70 - (y * 24) 
        maze.goto(screen_x, screen_y)
        maze.stamp()

  return mazeout

  #end program
  def endProgram():
    wn.exitonclick()
    sys.exit()

