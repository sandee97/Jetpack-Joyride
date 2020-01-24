import time
from Bullets import Bullets
import os
import sys

class Player:
    def __init__(self):
        self._lifes=2
        self.magenta='\u001b[35;1m'
        self.reset= '\u001b[0m'
        self.__white      = '\u001b[37;1m'
        self.__cap        =['_','^','_']
        self.__head       =['|','O','|']
        self.__body1      =['^','|','=']
        self.__body2      =['|','|',' ']
        self.__legs       =['/',' ','\\']
        self.posx       =20
        self.posylegs   =46
        self.posycap    =42
        self.posyhead   =43
        self.posybody1  =44
        self.posybody2  =45
        self.start      =4
        self.Bull       =[]
        self.sheild     =False
        self.sheildcoount=0
        self.green      = '\u001b[32;1m'
        self.red        ='\u001b[31;1m'
        self.gravitycounter=0
        self.gravitystepscounter=0


    def updateBullet(self,tmp_grid):
        for p in self.Bull:
            if p.checking():
                self.Bull.remove(p)
            else:
                p.x =p.x + 6
        for p in self.Bull:
            tmp_grid[p.y][p.x+1]='-'
            tmp_grid[p.y][p.x+2]='-'
        return tmp_grid

    def createbullts(self):
        bulls=Bullets(self.posx+2,self.posybody1)
        self.Bull.append(bulls)

    def create(self,scene,counter):
        if counter>self.posx:
            self.posx=counter
        tmp_grid=[[] for x in range(0,50)]
        if self.sheildcoount==100:
            self.sheild=False
            self.sheildcoount=0
        for i in range(0,50):
            tmp_grid[i]=scene[i][:]
        if self.sheild:
            self.sheildcoount+=1
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posycap][i]=self.__white + self.__cap[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posyhead][i]=self.__white + self.__head[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posybody1][i]=self.__white + self.__body1[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posybody2][i]=self.__white + self.__body2[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posylegs][i]=self.__white + self.__legs[i-self.posx] +self.reset
        else:
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posycap][i]=self.magenta + self.__cap[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posyhead][i]=self.magenta + self.__head[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posybody1][i]=self.magenta + self.__body1[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posybody2][i]=self.magenta + self.__body2[i-self.posx] +self.reset
            for i in range(self.posx,self.posx+3):
                tmp_grid[self.posylegs][i]=self.magenta + self.__legs[i-self.posx] +self.reset

        return tmp_grid

    def moveup(self):
        if self.posycap ==1:
            self.posylegs-=0
            self.posycap-=0
            self.posybody1-=0
            self.posybody2-=0
            self.posyhead-=0
        elif self.posycap == 2:
            self.posylegs-=1
            self.posycap-=1
            self.posybody1-=1
            self.posybody2-=1
            self.posyhead-=1
        elif self.posycap ==3:
            self.posylegs-=2
            self.posycap-=2
            self.posybody1-=2
            self.posybody2-=2
            self.posyhead-=2
        elif self.posycap ==4:
            self.posylegs-=3
            self.posycap-=3
            self.posybody1-=3
            self.posybody2-=3
            self.posyhead-=3
        elif self.posycap == 5:
            self.posylegs-=4
            self.posycap-=4
            self.posybody1-=4
            self.posybody2-=4
            self.posyhead-=4
        elif self.posycap ==6:
            self.posylegs-=5
            self.posycap-=5
            self.posybody1-=5
            self.posybody2-=5
            self.posyhead-=5
        else:
            self.posylegs-=6
            self.posycap-=6
            self.posybody1-=6
            self.posybody2-=6
            self.posyhead-=6

    def moveright(self,counter):
        if self.posx <=1434:
            if (counter+200)-self.posx-5 > 5 :
                self.posx+=5
            elif (counter+200)-self.posx-5 == 4:
                self.posx+=4
            elif (counter+200)-self.posx-5== 3:
                self.posx+=3
            elif (counter+200)-self.posx-5== 2:
                self.posx+=2
            elif (counter+200)-self.posx-5== 1:
                self.posx+=1

    def moveleft(self,counter):
        if self.posx<=counter:
            self.posx=counter
        else:
            self.posx-=2

    def Gravity(self):
        if (self.posylegs+self.gravitystepscounter)<=46:
            self.posylegs+=self.gravitystepscounter
            self.posycap+=self.gravitystepscounter
            self.posybody1+=self.gravitystepscounter
            self.posybody2+=self.gravitystepscounter
            self.posyhead+=self.gravitystepscounter
        else:
            self.posylegs=46
            self.posycap=42
            self.posybody1=44
            self.posybody2=45
            self.posyhead=43

        if self.gravitycounter%3==0 and self.gravitystepscounter<2:
            self.gravitystepscounter+=1
        else:
            self.gravitystepscounter=2
        if self.gravitycounter>=9:
            self.gravitystepscounter=0
            self.gravitycounter=0
        self.gravitycounter+=1

        if self.posylegs==46:
            self.gravitystepscounter=0
            self.gravitycounter=0
            return False
        else:
            return True

    def update_lifes(self):
            self._lifes-=1
            self.posx=self.start

    def terminate(self):
        self.sheild=False
        self.sheildcoount=0
        print(self.magenta + "Game Over" + self.reset)
        print("Try Again")
        sys.exit()

    def terminateboss(self,score):
        os.system("tput reset")
        print("\n")
        dragonmessage=[
                                '                                                       (  )   /\   _                 (                                                  ',
                                '                                                        \ |  (  \ ( \.(               )                      _____                      ',
                                '                                                      \  \ \         ) \             (  ___                 / _   \                     ',
                                '                                                     (_     \+   . x  ( .\            \/   \____-----------/ (o)   \_                   ',
                                '                                                    - .-               \+  ;          (  O                           \____              ',
                                '                                                                              )        \_____________                 \  /              ',
                                '                                                    (__      YOU WON   +- .( - .- <. - _  VVVVVVV VV V\                 \/              ',
                                '                                                    (_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |            ',
                                '                                                      .    /./.+-  . .- /  +--  - .     \______________//_              \_______        ',
                                '                                                      (__   /x  / x _/ (                                  \___           \     /        ',
                                '                                                     , x / (    . / .  /                                      |           \   /         ',
                                '                                                        /  /  _/ /    +                                      /              \/          ',
                                '                                                          (__/                                             /                  \         ',


        ]
        print("\n")
        print("\n")
        print("\n")
        print("\n")

        for i in range(0,12):
            print(dragonmessage[i])
        print(self.green)
        print("score" ,"                                        ",score-5)
        print(self.reset)
        sys.exit()

    def lost_to_boss(self,score):
        os.system("tput reset")
        print(self.red)
        print("                                                         Game Over                                      ")
        print(self.reset)
        dragonmessage=[
                                            '                                                                                                ___                               ',
                                            '                                                                                             .~))>>                                   ',
                                            '                                                                                            .~)>>                                     ',
                                            '                                                                                          .~))))>>>                                   ',
                                            '                                                                                        .~))>>             ___                        ',
                                            '                                                                                      .~))>>)))>>      .-~))>>                        ',
                                            '                                                                                    .~)))))>>       .-~))>>)>                         ',
                                            '                                                                                  .~)))>>))))>>  .-~)>>)>                             ',
                                            '                                                              )                 .~))>>))))>>  .-~)))))>>)>                            ',
                                            '                                                           ( )@@*)             //)>))))))  .-~))))>>)>                                ',
                                            '                                                         ).@(@@               //))>>))) .-~))>>)))))>>)>                              ',
                                            '                                                       (( @.@).              //))))) .-~)>>)))))>>)>                                  ',
                                            '                                                     ))  )@@*.@@ )          //)>))) //))))))>>))))>>)>                                ',
                                            '                                                  ((  ((@@@.@@             |/))))) //)))))>>)))>>)>                                   ',
                                            '                                                 )) @@*. )@@ )   (\_(\-\b  |))>)) //)))>>)))))))>>)>                                  ',
                                            '                                               (( @@@(.@(@ .    _/`-`  ~|b |>))) //)>>)))))))>>)>                                     ',
                                            '                                                )* @@@ )@*     (@) (@)  /\b|))) //))))))>>))))>>                                     ',
                                            '                                              (( @. )@( @ .   _/       /  \b)) //))>>)))))>>>_._                                     ',
                                            '                         YOU LOST             )@@ (@@*)@@.  (6,   6) / ^  \b)//))))))>>)))>>   ~~-.                                  ',
                                            '                                            ( @jgs@@. @@@.*@_ ~^~^~, /\  ^  \b/)>>))))>>      _.     `,                               ',
                                            '                                             ((@@ @@@*.(@@ .   \^^^/  (  ^   \b)))>>        .          `,                             ',
                                            '                                              ((@@).*@@ )@ )    `-/   ((   ^  ~)_          /             `,                           ',
                                            '                                                (@@. (@@ ).           (((   ^    `\        |               `.                         ',
                                            '                                                  (*.@*              / ((((        \        \      .         `.                       ',
                                            '                                                                    /   (((((  \    \    _.-~\     Y,         ;                       ',
                                            '                                                                   /   / (((((( \    \.-~   _.`" _.-~`,       ;                       ',
                                            '                                                                  /   /   `(((((()    )    (((((~      `,     ;                       ',
                                            '                                                                _/  _/      `"""/   /                   ;     ;                       ',
                                            '                                                            _.-~_.-~           /  /                 _.-~   _..                        ',
                                            '                                                          ((((~~              / /               _.-~ __.--~                           ',
                                            '                                                                             ((((          __.-~ _.-~                                 ',
                                            '                                                                                         .|   .~~                                     ',
                                            '                                                                                         :    ,/                                      ',
                                            '                                                                                         ~~~~~                                        '
        ]
        print("\n")
        print("\n")
        print("\n")
        print("\n")

        for i in range(0,34):
            print(dragonmessage[i])
        print(self.green)
        print("score" ,"                                        ",score)
        print(self.reset)
        sys.exit()
