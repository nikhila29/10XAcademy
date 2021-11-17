class Robot:
    def __init__(self):
        self.location=[0,0]  #index 0,1---x,y
    def moveUp(self):
        self.location[1]+=1
    def moveDown(self):
        self.location[1]-=1
    def moveRight(self):
        self.location[0]+=1
    def moveLeft(self):
        self.location[0]-=1
robot_move=Robot()
n=int(input())
for i in range(0,n):
    direction=input()
    if direction=="up":
        robot_move.moveUp()
    elif direction=="down":
        robot_move.moveDown()
    elif direction=="right":
        robot_move.moveRight()
    elif direction=="left":
        robot_move.moveLeft()
for j in robot_move.location:
    print(j)
    
    