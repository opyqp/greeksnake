import time
import sys
import msvcrt
import os
import random
coding="gbk"
sz=int(input("input the size of map:"))
UP='w'
DOWN='s'
RIGHT='d'
LEFT='a'

class Point:
    def __init__(self,x,y):
        self.x,self.y = x,y
    def setpoint(self,x,y):
        self.x,self.y=x,y

class Snake:
    def __init__(self):
        self.bd=list()
        i=5
        while(i>2): 
            tmp=Point(0,0)
            tmp.setpoint(2,i)
            self.bd.append(tmp)
            i-=1
        self.dir=RIGHT
    def if_alive(self):
        if((self.bd[0].x == 0) or (self.bd[0].x == (sz-1)) or (self.bd[0].y == 0) or (self.bd[0].y == (sz-1))):
            print("arrival wall")
            return False
        l=len(self.bd)-1
        while(l>0):
            if ((self.bd[l].x == self.bd[0].x) and (self.bd[l].y == self.bd[0].y)):
                print("eat self")
                return False
            else:
                return True
    def cdm(self):
        newhd=Point(0,0)
        if(self.dir == UP):
            newhd.setpoint(self.bd[0].x-1,self.bd[0].y)
        elif(self.dir == DOWN):
            newhd.setpoint(self.bd[0].x+1,self.bd[0].y)
        elif(self.dir == RIGHT):
            newhd.setpoint(self.bd[0].x,self.bd[0].y+1)
        elif(self.dir == LEFT):
            newhd.setpoint(self.bd[0].x,self.bd[0].y-1)
        else:
            print("input invalid")
        self.bd.insert(0,newhd)
    def move(self):
        self.cdm()
        a=self.bd[-1]
        del self.bd[-1]
        return a
            
class Map:
    def __init__(self):
        self.sk=Snake()
        self.food=Point(0,0)
        self.maps=[[' ' for row in range(sz)]for row in range(sz)]
        self.setfood()
    def setfood(self):
        self.food.x=self.food.y=random.randint(1,sz-2)
    def draw(self):
        self.maps[self.food.x][self.food.y]='*'
        for k in range(len(self.sk.bd)):
            self.maps[self.sk.bd[k].x][self.sk.bd[k].y]="*"
        for i in range(sz):
            for j in range(sz):
                if(i == 0 or i == sz-1 or j == 0 or j==sz-1):self.maps[i][j]="*"
        for i in range(sz):
            for j in range(sz):
                print(self.maps[i][j]),
            print("\n")
       
    def if_eaten(self):
        if(self.food.x ==self.sk.bd[0].x and self.food.y == self.sk.bd[0].y):
            return True
        else:
            return False



print("input any key to start!")
msvcrt.getch()
mp=Map()
count=0
while(mp.sk.if_alive()):
    start=time.time()
    while(time.time()-start<1 and not msvcrt.kbhit()):continue
    if(msvcrt.kbhit()):
        mp.sk.dir=str(msvcrt.getch())
    flag = False
    if(mp.if_eaten()):
        mp.setfood()
        mp.sk.bd.insert(-1,mp.sk.bd[-1])
        flag=True
    a=mp.sk.move()
    if flag:
        mp.maps[a.x][a.y]="*"
    else:
        mp.maps[a.x][a.y] = " "
    os.system("cls")
    mp.draw()
    count+=1
print("count:",count)
print("game over")
os.system("pause")