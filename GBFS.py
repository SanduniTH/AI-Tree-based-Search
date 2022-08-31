import sys
import time
from Turtle import Blue
from Turtle import Yellow

blue = Blue()
yellow = Yellow()

#Node class for the search algorithms
class Node:
    # Initializing the class
    def __init__(self, position:(), parent:(), direction:()):
        self.position = position
        self.parent = parent
        self.direction = direction
        self.g = 0 # Distance to start node
        self.h = 0 # Distance to goal node
        self.f = 0 # Total cost
    # definition to compare nodes 
    def __eq__(self, other):
        return self.position == other.position
    # definition to sort nodes
    def __lt__(self, other):
         return self.f < other.f

   
def gbfs_search(x1, y1, x2, y2, x3, y3, path):
    start = time.time()    
    # Create lists for frontier nodes and queue nodes and solution nodes
    frontier = []
    queue = []
    solution =[]
    count = 1 #to count the nodes that were open
    # the start node and the goal nodes
    start_node = Node((x1, y1), None, None)
    goal_node1 = Node((x2,y2), None, None)
    goal_node2 = Node((x3, y3), None, None)

    # Add the start node to the frontier
    frontier.append(start_node)
    
    # Loop until the frontier list is empty
    while len(frontier) > 0:
        #sort frontier
        frontier.sort()
        # Get the first node 
        current_node = frontier.pop(0)
        # Add the current node to the queue list
        queue.append(current_node)
        
        # If goal 1 is reached return path, count and time
        if current_node == goal_node1:
            #Send yellow turtle to goal node 1 position
            yellow.goto((-120 + (x2 * 24)), (70 - (y2 * 24)))
            yellow.stamp()
            while current_node != start_node:
                solution.append(current_node.direction)
                current_node = current_node.parent
                #calculate the screen x and y position of the current node so that the yellow sprite can be drawn
                xpath = current_node.position[0]
                ypath = current_node.position[1]
                yellow.goto((-120 + (xpath * 24)), (70 - (ypath * 24)))
                yellow.stamp() 
                   
            return (solution[::-1], count, (time.time()-start))

        # If goal 2 is reached return path, count and time
        if current_node == goal_node2:
            #Send yellow turtle to goal node 2 position
            yellow.goto((-120 + (x3 * 24)), (70 - (y3 * 24)))
            yellow.stamp()
            while current_node != start_node:
                solution.append(current_node.direction)
                current_node = current_node.parent
                #calculate the screen x and y position of the current node so that the yellow sprite can be drawn
                xpath = current_node.position[0]
                ypath = current_node.position[1]
                yellow.goto((-120 + (xpath * 24)), (70 - (ypath * 24)))
                yellow.stamp() 
            
            # Return reversed path
            return (solution[::-1], count, (time.time()-start))
        #take out the x and y of current node position to get neighbors
        (x, y) = current_node.position
        # Get neighbors in the order of up, left, down and right
        neighbors = [(x, y-1), (x-1, y), (x, y+1), (x+1, y)]
  
        for n in neighbors:
            # Check if the node is blocked
            if n not in path:
                continue
            # Create a neighbor node according to the direction
            if n == (x, y - 1):
              neighbor = Node(n, current_node, "Up; ")
            elif n == (x - 1, y):
              neighbor = Node(n, current_node, "Left; ") 
            elif n == (x, y + 1):
              neighbor = Node(n, current_node, "Down; ") 
            else:
              neighbor = Node(n, current_node, "Right; ") 

            # Check if the neighbor is in the queue list
            if(neighbor in queue):
                continue
            
            #Calculte heuristics using Manhattan distance
            goal1 = abs(neighbor.position[0] - goal_node1.position[0]) + abs(neighbor.position[1] - goal_node1.position[1])
            goal2 = abs(neighbor.position[0] - goal_node2.position[0]) + abs(neighbor.position[1] - goal_node2.position[1])
            #getting the minimum value from goal 1 and goal 2
            neighbor.h = min(goal1, goal2)
            neighbor.f = neighbor.h
            # if neighbor is in frontier list and if it has a lower f value
            if(add_to_frontier(frontier, neighbor) == True):
                #add neighbour to frontier
                frontier.append(neighbor)
                count += 1 #increase count since a neighbour is added
                #blue sprite to the neighbour location to see the pattern of the algorithm
                blue.goto((-120 + (neighbor.position[0] * 24)), (70 - (neighbor.position[1] * 24)))
                blue.stamp()
    # Return None if  no path is found
    return None


# compare the heuristic and if the heuristic value is lowest add to frontier
def add_to_frontier(frontier, neighbor):
    for node in frontier:
        if (neighbor == node and neighbor.f >= node.f):
            return False
    return True
  
