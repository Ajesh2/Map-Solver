#modules inclusion
from pyray import *
import random

#variables
backgroundColor = Color(33,34,44,255)
buildingColor   = Color(98,114,164,255)
buildingSize    = 10

#basic initiation
set_trace_log_level(LOG_NONE)
ScreenWidth,ScreenHeight = 810,410
init_window(ScreenWidth,ScreenHeight, "MapSolver")

#functions and classes and everything
areaMap = []
for i in range(40):
    temp = []
    for j in range(80):
        temp.append(1)
    areaMap.append(temp)

def showTile(Map):
    for i in range(41):
        for j in range(81):
            if Map[i][j]:
                draw_rectangle(j*buildingSize, i*buildingSize, buildingSize, buildingSize, buildingColor)
                #draw_rectangle_lines(j*buildingSize, i*buildingSize, buildingSize, buildingSize, Color(98,114,164,255))

def createMaze():
    Maze = []
    for i in range(20):
        temp = []
        for j in range(40):
            temp.append(1)
        Maze.append(temp)
    
    for i in range(20):
        Maze[i][39] = 2
    tablet = []
    for k in range(1,20):
        for i in range(40):
            if i != 39:
                if random.randint(1, 2) != 1:
                    tablet.append([k,i])
                else:
                    Maze[k][i] = 2
                    tablet.append([k,i])
                    test = random.randint(0, len(tablet) - 1)
                    if Maze[tablet[test][0] - 1][tablet[test][1]] == 1:
                        Maze[tablet[test][0] - 1][tablet[test][1]] = 3
  
                    if Maze[tablet[test][0] - 1][tablet[test][1]] == 2:
                        Maze[tablet[test][0] - 1][tablet[test][1]] = 4
  
                    tablet = []
            else:

                tablet.append([k,i])
  
                test = random.randint(0, len(tablet) - 1)
                if Maze[tablet[test][0] - 1][tablet[test][1]] == 1:
                    Maze[tablet[test][0] - 1][tablet[test][1]] = 3

                if Maze[tablet[test][0] - 1][tablet[test][1]] == 2:
                    Maze[tablet[test][0] - 1][tablet[test][1]] = 4

                tablet = []

    return Maze

def decodeMaze(maze):
    decoded = []
    for i in range(40):
        temp = []
        for j in range(80):
            temp.append(0)
        decoded.append(temp)
    for k in range(20):
        for i in range(40):
            if maze[k][i] == 1:
                decoded[k*2 + 1][i*2]     = 1
                decoded[k*2 + 1][i*2 + 1] = 1
            if maze[k][i] == 2:
                decoded[k*2 + 1][i*2]     = 1
                decoded[k*2 + 1][i*2 + 1] = 1
                decoded[k*2]    [i*2 + 1] = 1
            if maze[k][i] == 4:
                decoded[k*2 + 1][i*2 + 1] = 1
                decoded[k*2]    [i*2 + 1] = 1
    for i in range(40):
        decoded[i].insert(0,1)
    temp = []
    for i in range(81):
        temp.append(1)
    decoded.insert(0,temp)
    return decoded



areaMap = decodeMaze(createMaze())
while not window_should_close():
    begin_drawing()
    clear_background(backgroundColor)
    showTile(areaMap)
    end_drawing()
close_window()
