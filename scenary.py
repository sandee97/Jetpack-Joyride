from player import Player
import time
from Bullets import Bullets
from Enemy import Enemy
from Dragon import Dragon
import random
from magnet import magnet
from Boss import Boss
from Boss import DragonBullets
class Scenary(Player,Enemy):
        def __init__(self):
            self.Up         =False
            self.Right      =False
            self.left       =False
            self.maxx       =990
            self.minx       =3
            self.miny       =1
            self.maxy       =46
            self.land       =['|'for x in range(0,1500)]
            self.__scene      =[[] for x in range(0,50)]
            self.Boundary   =['X' for x in range(0,1500)]
            self.space      =[' ' for x in range(0,1500)]
            self.black      = '\u001b[30;1m'
            self.red        = '\u001b[31;1m'
            self.green      = '\u001b[32;1m'
            self.yellow     = '\u001b[33;1m'
            self.blue       = '\u001b[34;1m'
            self.magenta    = '\u001b[35;1m'
            self.cyan       = '\u001b[36;1m'
            self.__white      = '\u001b[37;1m'
            self.maxWidth   = 1500
            self.player     =Player()
            self.reset      = '\u001b[0m'
            self.counter    =0
            self.gravity    =False
            self.bullets    =False
            self.fired      =False
            self.clouds     =[]
            self.coins      =[]
            self.Enemies    =[]
            self.vertical   =[]
            self.horizontal =[]
            self.typical    =[]
            self.score      =0
            self.shh        =False
            self.speedBoost =False
            self.boo        =2
            self.DragonBull =[]
            self.boos       =[]
            self.bullcounter=0
            self.__bosslifes =40

            for i in range(0,50):
                if i==0 or i==47 or i==49:
                    self.__scene[i]=self.Boundary[:]
                elif i==48:
                    self.__scene[i]=self.land[:]
                else:
                    self.__scene[i]=self.space[:]

        def checkCollisions(self):
            if (self.player.posx>=100 and self.player.posx<=115 and self.player.posycap-5>9) or (self.player.posx>=500 and self.player.posx<=515 and self.player.posycap-5>9) or (self.player.posx>=1000 and self.player.posx<=1015 and self.player.posycap-5>9):
                self.Up=True

            '''Bullet collision with enemy'''
            for ene in self.Enemies:
                for bull in self.player.Bull:
                    if ((bull.x>=ene.x and bull.x<=ene.x+3) or (bull.x+1>=ene.x and bull.x<=ene.x+3)) and (bull.y<=ene.y and bull.y>=ene.y-3):
                        if ene.lives==0:
                            self.Enemies.remove(ene)
                            self.score=self.score + 50
                        else:
                            ene.lives-=1
                            self.player.Bull.remove(bull)

            '''Player collision with the enemy'''
            for ene in self.Enemies:
                if (ene.x==self.player.posx+2 or ene.x==self.player.posx+1 or ene.x==self.player.posx or ene.x+1==self.player.posx) and (ene.y==self.player.posycap or ene.y==self.player.posyhead or ene.y==self.player.posybody1 or ene.y==self.player.posybody1 or ene.y==self.player.posylegs):
                    if self.player.lifes>0 and self.player.sheild==False:
                        self.player.update_lifes()
                        self.counter=0
                    elif self.player.lifes==0:
                        self.player.lost_to_boss(self.score)

            '''Player collision with the coin'''
            for co in self.coins:
                if (self.player.posx<=co.x and co.x<=self.player.posx+3) and (co.y <= self.player.posylegs and co.y >= self.player.posycap):
                    self.coins.remove(co)
                    self.score=self.score +10

            '''Player collision with the vetical beams'''
            for bea in self.vertical:
                if (bea.x>=self.player.posx and bea.x<=self.player.posx+3) and ((bea.y>=self.player.posylegs and bea.y-4<=self.player.posylegs) or (bea.y>=self.player.posycap and  bea.y-4<=self.player.posycap)):
                    if self.player.lifes>0 and self.player.sheild==False:
                        self.player.update_lifes()
                        self.counter=0
                    elif self.player.lifes==0:
                        self.player.lost_to_boss(self.score)

            '''Player collision with the horizontal beam'''
            for bea in self.horizontal:
                if (bea.x<=self.player.posx and bea.x+8 >=self.player.posx) and (bea.y>=self.player.posycap and bea.y<=self.player.posylegs):
                    if self.player.lifes>0 and self.player.sheild==False:
                        self.player.update_lifes()
                        self.counter=0
                    elif self.player.lifes==0:
                        self.player.lost_to_boss(self.score)

            '''Player collision with the typical beam'''
            for bea in self.typical:
                if (bea.x<=self.player.posx+2 and bea.x>=self.player.posx and bea.y>=self.player.posycap and bea.y <=self.player.posylegs) or ((bea.x+1)<=self.player.posx+2 and (bea.x+1)>=self.player.posx and (bea.y-1)>=self.player.posycap and (bea.y-1)<=self.player.posylegs) or ((bea.x+2)<=self.player.posx+2 and (bea.x+2)>=self.player.posx and (bea.y-2)>=self.player.posycap and (bea.y-2)<=self.player.posylegs) or ((bea.x+3)<=self.player.posx+2 and (bea.x+3)>=self.player.posx and (bea.y-3)>=self.player.posycap and (bea.y-3)<=self.player.posylegs) or ((bea.x+4)<=self.player.posx+2 and (bea.x+4)>=self.player.posx and (bea.y-4)>=self.player.posycap and (bea.y-4)<=self.player.posylegs):
                    if self.player.lifes>0 and self.player.sheild==False:
                        self.player.update_lifes()
                        self.counter=0
                    elif self.player.lifes==0:
                        self.player.lost_to_boss(self.score)

            '''Bullets colliding with the vertical beams'''
            for bea in self.vertical:
                for bul in self.player.Bull:
                    if bul.y<=bea.y and bul.y>=bea.y-4 and bul.x>=bea.x:
                        self.vertical.remove(bea)
                        self.player.Bull.remove(bul)
                        self.score+=5


            '''Bullets colliding with the horizontal beams'''
            for bea in self.horizontal:
                for bul in self.player.Bull:
                    if bul.y==bea.y and bul.x>=bea.x and bul.x<=bea.x+8:
                        self.horizontal.remove(bea)
                        self.player.Bull.remove(bul)
                        self.score+=5

            '''Bullet collision with typical beams'''
            for bea in self.typical:
                for bul in self.player.Bull:
                    if ((bul.x==bea.x or bul.x+1==bea.x or bul.x+2==bea.x ) and (bul.y==bea.y)) or ((bul.x==bea.x-1 or bul.x+1==bea.x-1 or bul.x+2==bea.x-1) and (bul.y==bea.y+1)) or ((bul.x==bea.x-2 or bul.x+1==bea.x-2 or bul.x+2==bea.x-2) and (bul.y==bea.y+2)) or ((bul.x==bea.x-3 or bul.x+1==bea.x-3 or bul.x+2==bea.x-3) and (bul.y==bea.y+3)) or ((bul.x==bea.x-4 or bul.x+1==bea.x-4 or bul.x+2==bea.x-3) and (bul.y==bea.y+4)):
                        self.typical.remove(bea)
                        self.player.Bull.remove(bul)
                        self.score+=5

            '''Collision with boss enemy bullet'''
            for dragbul in self.DragonBull:
                if dragbul.bullposx<=self.player.posx+2 and dragbul.bullposx+11 >=self.player.posx and ((self.player.posycap <=dragbul.bullposy and self.player.posylegs>=dragbul.bullposy) or (self.player.posycap>=dragbul.bullposy and self.player.posylegs>=dragbul.bullposy and dragbul.bullposy+5>=self.player.posycap) or (self.player.posycap>=dragbul.bullposy and self.player.posylegs<=dragbul.bullposy+5)):
                    if self.player.lifes>0 and self.player.sheild==False:
                        self.player.lifes=0
                        self.player.lost_to_boss(self.score)

            '''Dragon bullet removing'''
            for dragbul in self.DragonBull:
                if dragbul.bullposx <=1299:
                    self.DragonBull.remove(dragbul)

            '''Dragon killing'''
            for bull in self.player.Bull:
                if bull.x>=self.boo.x and bull.x<=self.boo.x+38 and bull.y>=self.boo.y and bull.y<=self.boo.y+14:
                    self.__bosslifes-=1
                    self.player.Bull.remove(bull)
                    self.score+=5

            if self.__bosslifes==0:
                self.player.terminateboss(self.score)

        def update_lifes(self):
            self.counter=0
            self.player.posx=self.player.start
            self.player.lifes-=1

        def prior(self):
            for x in range(8,21):
                for y in range(7,37):
                    self.__scene[x][y]=self.blue+Dragon[x-8][y-7]+self.reset
            self.__scene[11][29]=self.red +'M' + self.reset
            self.__scene[11][30]=self.red +'A' + self.reset
            self.__scene[11][31]=self.red +'N' + self.reset
            self.__scene[11][32]=self.red +'D' + self.reset
            self.__scene[11][33]=self.red +'O' + self.reset
            for i in range(9,15):
                for j in range(100,115):
                    self.__scene[i][j]=magnet[i-9][j-100]
            for i in range(9,15):
                for j in range(500,515):
                    self.__scene[i][j]=magnet[i-9][j-500]
            for i in range(9,15):
                for j in range(1000,1015):
                    self.__scene[i][j]=magnet[i-9][j-1000]

            self.vertical=createVbars()
            self.horizontal=createHbars()
            self.typical=createTbars()
            self.clouds=createClouds()
            self.coins=createCoins()
            for clo in self.clouds:
                self.__scene=clo.create(self.__scene)
            self.Enemies=creation_of_enemies()
            self.boo=Boss(1440,20)
            self.boos.append(self.boo)

        def background(self):
            if self.shh:
                self.player.sheild=True
            tmp_grid=self.player.create(self.__scene,self.counter)
            for co in self.coins:
                tmp_grid=co.create(tmp_grid)
            for bars in self.vertical:
                tmp_grid=bars.create(tmp_grid )
            for bars in self.horizontal:
                tmp_grid=bars.create(tmp_grid)
            for bars in self.typical:
                tmp_grid=bars.create(tmp_grid)
            if self.bullets:
                tmp_grid=self.player.updateBullet(tmp_grid)
            for ene in self.Enemies:
                ene.update_Enemies()
            for ene in self.Enemies:
                tmp_grid=ene.PlaceEnemyvertical(tmp_grid)
            if self.counter>1299:
                for boo in self.boos:
                    tmp_grid=self.boo.create(tmp_grid)
                self.boo.updatePosition(self.player.posybody1)
                if self.bullcounter%20==0:
                    drabu=DragonBullets(self.boo.x-8,self.boo.y+3)
                    self.DragonBull.append(drabu)
                for drabuu in self.DragonBull:
                    tmp_grid=drabuu.create(tmp_grid)
                self.bullcounter+=1
                if self.bullcounter==100:
                    self.bullcounter=0
                for drabul in self.DragonBull:
                    drabul.updateBullets()
            printScenary(tmp_grid,self.green,self.reset,self.counter)
            if self.speedBoost and self.counter<=1296:
                self.counter+=3
                self.speedBoost=False
            if self.counter<=1299:
                self.counter+=1

        def check(self):
            if self.Right:
                self.player.moveright(self.counter)
                self.Right=False
            if self.Up:
                self.player.moveup()
                self.Up=False
                self.gravity=True
            if self.gravity:
                self.gravity=self.player.Gravity()
            if self.fired:
                self.player.createbullts()
                self.fired=False
            if self.left:
                self.player.moveleft(self.counter)
                self.left=False
def createTbars():
    bars=[]
    for x in range(0,7):
        x=random.randrange(100,1299,10)
        y=random.randrange(20,40,2)
        Vbar=typical_Beams(x,y)
        bars.append(Vbar)
    return bars

def createVbars():
    bars=[]
    for x in range(0,7):
        x=random.randrange(100,1299,10)
        y=random.randrange(20,40,2)
        Vbar=Vertical_Beams(x,y)
        bars.append(Vbar)
    return bars

def createHbars():
    bars=[]
    for x in range(0,7):
        x=random.randrange(100,1299,10)
        y=random.randrange(20,40,2)
        Hbar=HorizontalBeams(x,y)
        bars.append(Hbar)
    return bars

def creation_of_enemies():
    ene=[]
    for x in range(100,1000,100):
        enemy=Enemy(x,46)
        ene.append(enemy)
    return ene

def createClouds():
    clouds=[]
    for i in range(0,49):
        if i%2==0:
            cloud=Clouds(4,10+30*i)
            clouds.append(cloud)
        else:
            cloud=Clouds(6,10+30*i)
            clouds.append(cloud)
    return clouds

def createCoins():
    coins=[]
    for i in range(0,42):
        x=random.randrange(100,1299)
        y=random.randrange(6,45)
        co=Coins(x,y)
        coins.append(co)
    return coins

def printScenary(tmp_grid,green,reset,counter):
    temp=['' for x in range(0,50)]
    for i in range(0,50):
        for j in range(0+counter,200+counter):
            if i==47:
                temp[i]=temp[i] + green + tmp_grid[i][j] +reset
            else:
                temp[i]=temp[i]  + tmp_grid[i][j]

    for i in range(0,50):
        print(temp[i])

class Clouds:
    def __init__(self,x,y):
        self.cyan='\u001b[36;1m'
        self.reset= '\u001b[0m'
        self.x=x
        self.y=y

    def create(self,scene):
        for i in range(self.y + 6, self.y + 10):
            scene[self.x - 2][i] =self.cyan + '_' + self.reset
        scene[self.x - 1][self.y + 10] =self.cyan + ')'+ self.reset
        for i in range(self.y, self.y + 5):
            scene[self.x - 1][i] =self.cyan + '_'+ self.reset
        for i in range(self.y + 11,self.y + 15):
            scene[self.x - 1][i] =self.cyan + '_'+ self.reset
        scene[self.x - 1][self.y + 5] = self.cyan + '('+ self.reset
        scene[self.x][self.y - 1] =self.cyan + '('+ self.reset
        for i in range(self.y, self.y + 15):
            scene[self.x][i] =self.cyan + '_'+ self.reset
        scene[self.x][self.y + 15] =self.cyan + ')'+ self.reset
        return scene

class HorizontalBeams:
    def __init__(self,x,y):
        self.red        = '\u001b[31;1m'
        self.green      = '\u001b[32;1m'
        self.reset      = '\u001b[0m'
        self.x=x
        self.y=y

    def create(self,scene):
        for i in range(self.x,self.x+10,2):
            if i==self.x or i==self.x+8:
                scene[self.y][i]=self.red + "*" + self.reset
            else:
                scene[self.y][i]=self.green + "-" + self.reset
        return scene

class Vertical_Beams:
    def __init__(self,x,y):
        self.red        = '\u001b[31;1m'
        self.green      = '\u001b[32;1m'
        self.reset      = '\u001b[0m'
        self.x=x
        self.y=y
    def create(self,scene):
        for i in range(self.y,self.y-5,-1):
            if i==self.y or i==self.y-4:
                scene[i][self.x]=self.red + "*" + self.reset
            else:
                scene[i][self.x]=self.green + "|" + self.reset
        return scene

class typical_Beams:
    def __init__(self,x,y):
        self.red        = '\u001b[31;1m'
        self.green      = '\u001b[32;1m'
        self.reset      = '\u001b[0m'
        self.x=x
        self.y=y
    def create(self,scene):
        z=self.x
        for i in range(self.y,self.y-5,-1):
            if i==self.y or i==self.y-4:
                scene[i][z]=self.red + "*" + self.reset
            else:
                scene[i][z]=self.green + "*" + self.reset
            z+=1
        return scene

class Coins:
    def __init__(self,x,y):
        self.yellow = '\u001b[33;1m'
        self.reset = '\u001b[0m'
        self.x=x
        self.y=y

    def create(self,scene):
        scene[self.y][self.x] =self.yellow + '$' + self.reset
        return scene
