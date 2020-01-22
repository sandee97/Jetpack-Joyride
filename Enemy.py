

class Enemy:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.initial=y
        self.head=['^',' ','^']
        self.face=[' ','|',' ']
        self.body=[' ','_',' ']
        self.legs=['|',' ','|']
        self.move=True
        self.lives=2

    def update_Enemies(self):
        if self.y==self.initial-12:
            self.move=False
        elif self.y==self.initial:
            self.move=True
        if self.move:
            self.y-=4
        else:
            self.y+=4

    def PlaceEnemyvertical(self,tmp_grid):
        for j in range(self.x,self.x+3):
            tmp_grid[self.y-3][j]=self.head[j-self.x]
        for j in range(self.x,self.x+3):
            tmp_grid[self.y-2][j]=self.face[j-self.x]
        for j in range(self.x,self.x+3):
            tmp_grid[self.y-1][j]=self.body[j-self.x]
        for j in range(self.x,self.x+3):
            tmp_grid[self.y][j]=self.legs[j-self.x]
        return tmp_grid
