import sys
import re
from Turtle import *
from BFS import *
from DFS import *
from GBFS import *
from AStar import *

#create lists to create the maze
cells = []
path = []
blockedcells = []
solution = []

#create the grid 
def setup_grid(X, Y):
  for y in range(Y):
    for x in range(X):
      #create cells with coordinates
      cells.append((x, y))
  return cells   

#create the blocked path and GUI blocked cells
def setup_blockedpaths(X, Y, W, H):
  for x in range(X,(X+W)):
    for y in range(Y,(Y+H)):
      blockedcells.append((x, y))
      #create the blocked cells in the GUI
      screen_x = -120 + (x * 24)         
      screen_y = 70 - (y * 24) 
      #Create white square sprites
      maze.goto(screen_x, screen_y)
      maze.stamp()
  return blockedcells

#Extract values from the file 
with open(sys.argv[1]) as f:
  #extract the dimensions of the maze to set up the maze
  line1 = f.readline().strip('[]').split(',')
  YofGrid = int(line1[0])
  XofGrid = int(re.search(r'\d+', str(line1[1])).group())
  setup_maze(XofGrid,YofGrid) #for outer wall
  setup_grid(XofGrid, YofGrid) #for the grid
  
  #Extract the start position 
  line2 = f.readline().strip('()').split(',')
  start_x = int(line2[0])
  start_y = int(re.search(r'\d+', str(line2[1])).group())
  #Mark the start position with the red sprite
  red.goto((-120 + (start_x * 24)), (70 - (start_y * 24)))
  red.stamp()

  #Extract the goal positions 
  line3 = f.readline().strip('()').split('|')
  end1 = line3[0].split(',')
  end2 = line3[1].split(',')
  end1_x = int(re.search(r'\d+', str(end1[0])).group())
  end1_y = int(re.search(r'\d+', str(end1[1])).group())
  end2_x = int(re.search(r'\d+', str(end2[0])).group())
  end2_y = int(re.search(r'\d+', str(end2[1])).group())
  #Mark the end position with green sprites
  green.goto((-120 + (end1_x * 24)), (70 - (end1_y * 24)))
  green.stamp()
  green.color("green")
  green.goto((-120 + (end2_x * 24)), (70 - (end2_y * 24)))
  green.stamp()
  green.color("green")

  #extract the blocked cells 
  lines =  f.readlines()
  for line in lines:
    l = line.strip('()').split(',')
    XofBC = int(re.search(r'\d+', str(l[0])).group())
    YofBC = int(re.search(r'\d+', str(l[1])).group())
    WofBC = int(re.search(r'\d+', str(l[2])).group())
    HofBC =int(re.search(r'\d+', str(l[3])).group())
    #set up the clocked cells
    setup_blockedpaths(XofBC, YofBC, WofBC, HofBC)

#takeaway all the blocked cells from the total cell to create path
path = [loc for loc in cells if loc not in blockedcells]

#Select the the search algorithm from the command line input 
search  = sys.argv[2]

if(search == "BFS"):
    solution = bfs_search(start_x, start_y, end1_x, end1_y, end2_x, end2_y, path)
if(search == "DFS"):
    solution = dfs_search(start_x, start_y, end1_x, end1_y, end2_x, end2_y, path)
if(search == "GBFS"):
    solution = gbfs_search(start_x, start_y, end1_x, end1_y, end2_x, end2_y, path)
if(search == "AS"):
    solution = as_search(start_x, start_y, end1_x, end1_y, end2_x, end2_y, path)

#Print the filename, search method and total nodes
print(sys.argv[1] + " " +  sys.argv[2] + " " + str(solution[1]))

#print path 
print(solution[0])

#print depth of the path and time taken
print('Depth to the Final Node: {0}'.format(len(solution[0])))
print("Time Taken to serach: " + str(round((solution[2]*1000.0), 6)) + " ms")

#close GUI on click
wn.exitonclick()